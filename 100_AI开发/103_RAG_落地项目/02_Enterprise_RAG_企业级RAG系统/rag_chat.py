#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
企业级RAG知识库问答系统
基于LangChain+Chroma，支持多文档加载、智能切片、向量入库、语义检索和问答对话
"""

import os
import logging
import time
from typing import List, Dict, Optional

# 导入配置
from config import (
    DOCUMENT_CONFIG,
    EMBEDDING_CONFIG,
    VECTOR_STORE_CONFIG,
    LLM_CONFIG,
    RETRIEVAL_CONFIG,
    LOG_CONFIG,
    APP_CONFIG
)

# 尝试导入所需库
try:
    from langchain.document_loaders import PyPDFLoader, DocxLoader, TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma
    from langchain.chains import RetrievalQA
    from langchain.prompts import PromptTemplate
    from langchain.memory import ConversationBufferMemory
    from langchain.chains import ConversationalRetrievalChain
    langchain_support = True
except ImportError:
    langchain_support = False
    print("警告: 缺少LangChain相关库，请安装")

# 配置日志
logging.basicConfig(
    level=getattr(logging, LOG_CONFIG["level"]),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_CONFIG["log_file"]),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class RAGChat:
    """RAG聊天系统"""
    
    def __init__(self):
        """初始化RAG聊天系统"""
        self.vector_store = None
        self.qa_chain = None
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            max_len=APP_CONFIG["max_history"]
        )
        self._init_components()
    
    def _init_components(self):
        """初始化组件"""
        try:
            # 初始化Embedding
            self.embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_CONFIG["model_name"]
            )
            logger.info(f"初始化Embedding模型: {EMBEDDING_CONFIG['model_name']}")
            
            # 初始化文本分割器
            self.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=DOCUMENT_CONFIG["chunk_size"],
                chunk_overlap=DOCUMENT_CONFIG["chunk_overlap"]
            )
            logger.info(f"初始化文本分割器: chunk_size={DOCUMENT_CONFIG['chunk_size']}, chunk_overlap={DOCUMENT_CONFIG['chunk_overlap']}")
            
        except Exception as e:
            logger.error(f"初始化组件失败: {e}")
    
    def load_documents(self, docs_dir: str) -> List:
        """
        加载文档
        
        Args:
            docs_dir: 文档目录
            
        Returns:
            文档列表
        """
        documents = []
        
        try:
            for file in os.listdir(docs_dir):
                file_path = os.path.join(docs_dir, file)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in DOCUMENT_CONFIG["supported_formats"]:
                        try:
                            if ext == ".pdf":
                                loader = PyPDFLoader(file_path)
                            elif ext == ".docx":
                                loader = DocxLoader(file_path)
                            elif ext == ".txt":
                                loader = TextLoader(file_path, encoding='utf-8')
                            else:
                                continue
                            
                            docs = loader.load()
                            documents.extend(docs)
                            logger.info(f"加载文档: {file}, 页数: {len(docs)}")
                        except Exception as e:
                            logger.error(f"加载文档 {file} 失败: {e}")
        except Exception as e:
            logger.error(f"加载文档失败: {e}")
        
        return documents
    
    def process_documents(self, documents: List) -> List:
        """
        处理文档
        
        Args:
            documents: 文档列表
            
        Returns:
            处理后的文档块列表
        """
        try:
            # 分割文档
            splits = self.text_splitter.split_documents(documents)
            logger.info(f"分割文档完成，共生成 {len(splits)} 个文本块")
            return splits
        except Exception as e:
            logger.error(f"处理文档失败: {e}")
            return []
    
    def create_vector_store(self, documents: List):
        """
        创建向量库
        
        Args:
            documents: 文档块列表
        """
        try:
            # 创建向量库
            self.vector_store = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=VECTOR_STORE_CONFIG["persist_directory"],
                collection_name=VECTOR_STORE_CONFIG["collection_name"]
            )
            # 持久化
            self.vector_store.persist()
            logger.info(f"创建向量库成功，存储在: {VECTOR_STORE_CONFIG['persist_directory']}")
        except Exception as e:
            logger.error(f"创建向量库失败: {e}")
    
    def load_vector_store(self):
        """
        加载向量库
        """
        try:
            if os.path.exists(VECTOR_STORE_CONFIG["persist_directory"]):
                self.vector_store = Chroma(
                    persist_directory=VECTOR_STORE_CONFIG["persist_directory"],
                    embedding_function=self.embeddings,
                    collection_name=VECTOR_STORE_CONFIG["collection_name"]
                )
                logger.info(f"加载向量库成功，存储在: {VECTOR_STORE_CONFIG['persist_directory']}")
                return True
            else:
                logger.warning(f"向量库目录不存在: {VECTOR_STORE_CONFIG['persist_directory']}")
                return False
        except Exception as e:
            logger.error(f"加载向量库失败: {e}")
            return False
    
    def init_qa_chain(self):
        """
        初始化问答链
        """
        try:
            if not self.vector_store:
                logger.error("向量库未初始化")
                return
            
            # 创建检索器
            retriever = self.vector_store.as_retriever(
                search_kwargs={"k": RETRIEVAL_CONFIG["k"]}
            )
            
            # 提示模板
            prompt_template = """
            你是一个基于文档的问答助手，请根据以下文档内容回答用户问题。
            如果你不知道答案，直接说"根据提供的文档，我无法回答这个问题"，不要尝试编造答案。
            
            文档内容:
            {context}
            
            问题:
            {question}
            
            回答:
            """
            
            PROMPT = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            
            # 由于我们没有实际的大模型，这里使用一个简单的基于相似度的回答
            # 在实际应用中，这里应该使用真实的大模型
            class SimpleQA:
                def __init__(self, retriever):
                    self.retriever = retriever
                
                def run(self, question):
                    docs = self.retriever.get_relevant_documents(question)
                    context = "\n".join([doc.page_content for doc in docs])
                    # 简单的基于上下文的回答
                    return f"根据文档，{question}的答案是...\n\n参考文档:\n{context[:500]}..."
            
            self.qa_chain = SimpleQA(retriever)
            logger.info("初始化问答链成功")
        except Exception as e:
            logger.error(f"初始化问答链失败: {e}")
    
    def add_documents(self, docs_dir: str):
        """
        添加文档到向量库
        
        Args:
            docs_dir: 文档目录
        """
        try:
            # 加载文档
            documents = self.load_documents(docs_dir)
            if not documents:
                logger.warning("没有加载到文档")
                return
            
            # 处理文档
            splits = self.process_documents(documents)
            if not splits:
                logger.warning("文档处理失败")
                return
            
            # 创建或更新向量库
            if self.vector_store:
                # 更新向量库
                self.vector_store.add_documents(splits)
                self.vector_store.persist()
                logger.info(f"更新向量库成功，添加了 {len(splits)} 个文本块")
            else:
                # 创建新向量库
                self.create_vector_store(splits)
            
            # 重新初始化问答链
            self.init_qa_chain()
        except Exception as e:
            logger.error(f"添加文档失败: {e}")
    
    def ask(self, question: str) -> str:
        """
        回答问题
        
        Args:
            question: 问题
            
        Returns:
            回答
        """
        try:
            if not self.qa_chain:
                return "错误: 问答链未初始化，请先添加文档"
            
            # 记录开始时间
            start_time = time.time()
            
            # 调用问答链
            answer = self.qa_chain.run(question)
            
            # 记录结束时间
            end_time = time.time()
            logger.info(f"回答问题: {question}, 用时: {end_time - start_time:.2f}秒")
            
            # 更新对话历史
            self.memory.chat_memory.add_user_message(question)
            self.memory.chat_memory.add_ai_message(answer)
            
            return answer
        except Exception as e:
            logger.error(f"回答问题失败: {e}")
            return f"错误: {str(e)}"
    
    def clear_memory(self):
        """
        清除对话历史
        """
        self.memory.clear()
        logger.info("清除对话历史成功")

def main():
    """主函数"""
    print("=== 企业级RAG知识库问答系统 ===")
    print("\n初始化系统...")
    
    # 创建RAGChat实例
    rag_chat = RAGChat()
    
    # 尝试加载向量库
    if not rag_chat.load_vector_store():
        print("\n未找到向量库，正在处理文档...")
        # 处理文档
        docs_dir = APP_CONFIG["docs_dir"]
        if os.path.exists(docs_dir):
            rag_chat.add_documents(docs_dir)
        else:
            print(f"错误: 文档目录不存在: {docs_dir}")
            print("请在docs目录中添加PDF/Word/TXT文档")
    
    # 主循环
    print("\n系统已就绪，输入问题开始对话（输入'退出'结束）")
    while True:
        try:
            question = input("\n用户: ")
            if question.strip() == "退出":
                print("再见！")
                break
            
            answer = rag_chat.ask(question)
            print(f"\n助手: {answer}")
            
        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
