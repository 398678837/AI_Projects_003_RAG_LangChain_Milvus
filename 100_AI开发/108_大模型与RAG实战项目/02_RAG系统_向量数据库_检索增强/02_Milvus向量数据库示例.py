#!/usr/bin/env python3
"""
Milvus向量数据库示例
演示如何使用Milvus作为向量数据库实现RAG系统
"""

import os
import openai
from dotenv import load_dotenv
from langchain.vectorstores import Milvus
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_milvus_vector_db(text_files):
    """
    创建Milvus向量数据库
    
    Args:
        text_files (list): 文本文件路径列表
    
    Returns:
        Milvus: Milvus向量数据库实例
    """
    # 加载文档
    documents = []
    for file_path in text_files:
        loader = TextLoader(file_path)
        documents.extend(loader.load())
    
    # 分割文本
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    # 创建Milvus向量数据库
    embeddings = OpenAIEmbeddings()
    db = Milvus.from_documents(
        texts,
        embeddings,
        connection_args={"host": "localhost", "port": "19530"},
    )
    
    return db

def create_rag_chain_with_milvus():
    """
    创建基于Milvus的RAG检索增强生成链
    
    Returns:
        RetrievalQA: RAG检索链
    """
    # 加载向量数据库
    embeddings = OpenAIEmbeddings()
    db = Milvus(
        embeddings,
        connection_args={"host": "localhost", "port": "19530"},
    )
    
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
    """
    主函数
    """
    print("Milvus向量数据库RAG示例")
    print("=" * 50)
    
    # 示例文档
    text_files = ["data/document1.txt", "data/document2.txt"]
    
    try:
        # 创建Milvus向量数据库
        print("正在创建Milvus向量数据库...")
        db = create_milvus_vector_db(text_files)
        
        # 创建RAG链
        print("正在创建RAG链...")
        qa = create_rag_chain_with_milvus()
        
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
        print("请确保Milvus服务已启动并配置正确的API密钥")

if __name__ == "__main__":
    main()