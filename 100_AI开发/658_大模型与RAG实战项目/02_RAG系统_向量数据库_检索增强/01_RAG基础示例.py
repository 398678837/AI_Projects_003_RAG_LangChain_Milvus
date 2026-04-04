#!/usr/bin/env python3
"""
RAG（检索增强生成）基础示例
演示如何结合向量数据库和大模型实现检索增强生成
"""

import os
import openai
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_vector_db(text_files):
    """
    创建向量数据库
    
    Args:
        text_files (list): 文本文件路径列表
    
    Returns:
        Chroma: 向量数据库实例
    """
    # 加载文档
    documents = []
    for file_path in text_files:
        loader = TextLoader(file_path)
        documents.extend(loader.load())
    
    # 分割文本
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    # 创建向量数据库
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    
    return db

def create_rag_chain(db):
    """
    创建RAG检索增强生成链
    
    Args:
        db (Chroma): 向量数据库实例
    
    Returns:
        RetrievalQA: RAG检索链
    """
    # 创建检索器
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    # 创建RAG链
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    
    return qa

def main():
    """主函数"""
    print("RAG（检索增强生成）基础示例")
    print("=" * 50)
    
    # 示例文档
    # 注意：实际使用时需要准备相关文本文件
    text_files = ["data/document1.txt", "data/document2.txt"]
    
    try:
        # 创建向量数据库
        print("正在创建向量数据库...")
        db = create_vector_db(text_files)
        
        # 创建RAG链
        print("正在创建RAG链...")
        qa = create_rag_chain(db)
        
        # 示例查询
        query = "解释一下RAG系统的工作原理"
        print(f"\n查询: {query}")
        
        # 执行查询
        result = qa({"query": query})
        
        # 输出结果
        print(f"\n回答: {result['result']}")
        print("\n参考文档:")
        for i, doc in enumerate(result['source_documents']):
            print(f"  {i+1}. {doc.metadata['source']}")
            
    except Exception as e:
        print(f"出错: {e}")
        print("请确保已准备好示例文本文件并配置正确的API密钥")

if __name__ == "__main__":
    main()