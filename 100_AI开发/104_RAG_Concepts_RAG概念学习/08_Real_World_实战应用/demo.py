#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实战应用演示
展示企业知识库问答系统的核心功能
"""

import os
import shutil
import tempfile
from typing import List, Dict

# 尝试导入所需库
try:
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.schema import Document
    from langchain.prompts import PromptTemplate
    from langchain.chains import RetrievalQA
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    real_world_support = True
except ImportError:
    real_world_support = False
    print("警告: 缺少必要的库，请安装langchain和sentence-transformers")

class SimpleLLM:
    """
    简单的模拟语言模型
    """
    def __init__(self):
        self.name = "SimpleLLM"
    
    def __call__(self, prompt, **kwargs):
        """
        模拟语言模型生成
        """
        # 简单的基于规则的回答
        if "什么是RAG" in prompt:
            return "RAG（检索增强生成）是一种结合了检索和生成的AI技术，通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，以生成更准确、更相关的回答。"
        elif "RAG的工作流程" in prompt:
            return "RAG的工作流程包括：文档加载、文档切片、向量编码、向量存储、语义检索、增强生成。"
        elif "向量数据库" in prompt:
            return "向量数据库是专门存储和检索向量数据的数据库系统，常用的向量数据库包括Chroma、Qdrant、Milvus、FAISS等。"
        elif "如何使用RAG" in prompt:
            return "使用RAG的步骤包括：1. 收集和整理文档；2. 处理文档并生成向量；3. 构建向量数据库；4. 实现检索和生成功能；5. 部署和维护系统。"
        else:
            return "根据提供的文档，我无法回答这个问题。"

def create_sample_knowledge_base():
    """
    创建示例知识库
    """
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    
    # 创建示例文档
    documents = [
        {
            "filename": "rag_introduction.txt",
            "content": "RAG（检索增强生成）是一种结合了检索和生成的AI技术。它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，以生成更准确、更相关的回答。RAG的核心价值包括：解决知识过时问题、减少幻觉、提高回答准确性、领域知识增强。"
        },
        {
            "filename": "rag_workflow.txt",
            "content": "RAG的工作流程包括：1. 文档加载：将各种格式的文档加载到系统中；2. 文档切片：将长文档切分为较小的文本块；3. 向量编码：将文本转换为数字向量；4. 向量存储：将向量存储到向量数据库中；5. 语义检索：根据用户查询检索相关文本块；6. 增强生成：基于检索结果生成回答。"
        },
        {
            "filename": "vector_databases.txt",
            "content": "向量数据库是专门存储和检索向量数据的数据库系统。常用的向量数据库包括：1. Chroma：轻量级，适合开发和测试；2. Qdrant：轻量级，支持本地运行和高性能检索；3. Milvus：企业级，支持大规模向量数据；4. FAISS：Facebook开发的高效向量搜索库，适合实时检索。"
        },
        {
            "filename": "rag_implementation.txt",
            "content": "实现RAG系统的步骤包括：1. 收集和整理文档：确保文档的质量和相关性；2. 处理文档：加载、切片和编码文档；3. 构建向量数据库：选择合适的向量库并存储向量；4. 实现检索功能：优化检索参数和策略；5. 实现生成功能：选择合适的语言模型和提示模板；6. 部署和维护：监控系统性能并持续优化。"
        }
    ]
    
    # 写入文件
    for doc in documents:
        file_path = os.path.join(temp_dir, doc["filename"])
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(doc["content"])
    
    return temp_dir

def load_documents(directory: str) -> List[Document]:
    """
    加载目录中的文档
    """
    documents = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            # 添加元数据
            for doc in docs:
                doc.metadata["filename"] = filename
            documents.extend(docs)
    
    return documents

def create_rag_system():
    """
    创建RAG系统
    """
    # 初始化Embedding模型
    embeddings = HuggingFaceEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    
    # 创建示例知识库
    knowledge_base_dir = create_sample_knowledge_base()
    
    # 加载文档
    documents = load_documents(knowledge_base_dir)
    
    # 切片文档
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)
    
    # 创建向量库
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    # 创建检索器
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    
    # 创建提示模板
    prompt_template = """
    你是一个企业知识库问答助手，请根据以下文档内容回答用户问题。
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
    
    # 创建语言模型
    llm = SimpleLLM()
    
    # 创建问答链
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain, knowledge_base_dir

def demonstrate_knowledge_base_qa():
    """
    演示企业知识库问答系统
    """
    if not real_world_support:
        print("错误: 缺少必要的库，无法演示企业知识库问答系统")
        return
    
    print("=== 企业知识库问答系统演示 ===")
    
    # 清理之前的向量库
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    # 创建RAG系统
    print("\n1. 初始化系统")
    qa_chain, knowledge_base_dir = create_rag_system()
    print("   系统初始化成功")
    
    # 展示知识库
    print("\n2. 知识库内容")
    for filename in os.listdir(knowledge_base_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(knowledge_base_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"   文件名: {filename}")
            print(f"   内容: {content[:100]}...")
            print()
    
    # 测试问答
    print("\n3. 测试问答")
    questions = [
        "什么是RAG？",
        "RAG的工作流程是什么？",
        "常用的向量数据库有哪些？",
        "如何实现RAG系统？",
        "什么是深度学习？"
    ]
    
    for question in questions:
        print(f"\n   问题: {question}")
        result = qa_chain.run(question)
        print(f"   回答: {result}")
    
    # 清理临时文件
    shutil.rmtree(knowledge_base_dir)
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")

def main():
    """
    主函数
    """
    print("=== 实战应用演示 ===")
    print("\n本演示展示了企业知识库问答系统的核心功能，包括文档加载、向量存储、语义检索和增强生成。")
    print("企业知识库问答系统是RAG技术的典型应用，它可以帮助企业快速构建智能问答系统，")
    print("提高员工获取信息的效率，减少重复问题的处理，提升企业运营效率。")
    
    # 演示企业知识库问答系统
    demonstrate_knowledge_base_qa()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对RAG系统的实际应用有了初步了解。")
    print("在实际项目中，您需要根据具体需求选择合适的技术栈和优化策略，以构建高性能、高准确性的RAG系统。")

if __name__ == "__main__":
    main()
