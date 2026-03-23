#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量存储演示
展示向量库的创建、插入和检索功能
"""

import os
import shutil

# 尝试导入所需库
try:
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    vector_store_support = True
except ImportError:
    vector_store_support = False
    print("警告: 缺少必要的库，请安装langchain和sentence-transformers")

def create_sample_documents():
    """
    创建示例文档
    """
    # 创建示例文本
    sample_texts = [
        "RAG（检索增强生成）是一种结合了检索和生成的AI技术。",
        "它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中。",
        "RAG的核心价值包括：解决知识过时问题、减少幻觉、提高回答准确性、领域知识增强。",
        "RAG的工作流程包括：文档加载、文档切片、向量编码、向量存储、语义检索、增强生成。",
        "向量数据库是专门存储和检索向量数据的数据库系统。",
        "常用的向量数据库包括Chroma、Qdrant、Milvus、FAISS等。",
        "Chroma是一个轻量级的向量数据库，适合开发和测试。",
        "Qdrant是一个轻量级的向量数据库，支持本地运行和高性能检索。",
        "Milvus是一个企业级的分布式向量数据库，支持大规模向量数据。",
        "FAISS是Facebook开发的高效向量搜索库，适合实时检索。"
    ]
    
    return sample_texts

def demonstrate_vector_store():
    """
    演示向量存储
    """
    if not vector_store_support:
        print("错误: 缺少必要的库，无法演示向量存储")
        return
    
    print("=== 向量存储演示 ===")
    
    # 清理之前的向量库
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    # 初始化Embedding模型
    print("\n1. 初始化Embedding模型")
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        print("   模型初始化成功")
        
    except Exception as e:
        print(f"   模型初始化失败: {e}")
        return
    
    # 创建示例文档
    print("\n2. 创建示例文档")
    sample_texts = create_sample_documents()
    print(f"   创建了 {len(sample_texts)} 个示例文本")
    
    # 转换为LangChain文档格式
    from langchain.schema import Document
    documents = [
        Document(page_content=text, metadata={"id": i})
        for i, text in enumerate(sample_texts)
    ]
    
    # 创建向量库
    print("\n3. 创建向量库")
    try:
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        print("   向量库创建成功")
        print(f"   向量库中共有 {vector_store._collection.count()} 个向量")
        
    except Exception as e:
        print(f"   向量库创建失败: {e}")
        return
    
    # 持久化向量库
    print("\n4. 持久化向量库")
    vector_store.persist()
    print("   向量库持久化成功")
    
    # 加载向量库
    print("\n5. 加载向量库")
    try:
        loaded_vector_store = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embeddings
        )
        print("   向量库加载成功")
        print(f"   加载的向量库中共有 {loaded_vector_store._collection.count()} 个向量")
        
    except Exception as e:
        print(f"   向量库加载失败: {e}")
        return
    
    # 语义检索
    print("\n6. 语义检索")
    queries = [
        "什么是RAG？",
        "向量数据库有哪些？",
        "Chroma的特点是什么？"
    ]
    
    for query in queries:
        print(f"\n   查询: {query}")
        results = loaded_vector_store.similarity_search(
            query=query,
            k=3
        )
        
        print("   检索结果:")
        for i, result in enumerate(results):
            print(f"   {i+1}. {result.page_content}")
    
    # 使用检索器
    print("\n7. 使用检索器")
    retriever = loaded_vector_store.as_retriever(
        search_kwargs={"k": 2}
    )
    
    query = "RAG的工作流程是什么？"
    print(f"   查询: {query}")
    retrieved_docs = retriever.get_relevant_documents(query)
    
    print("   检索结果:")
    for i, doc in enumerate(retrieved_docs):
        print(f"   {i+1}. {doc.page_content}")

def main():
    """
    主函数
    """
    print("=== 向量存储演示 ===")
    print("\n向量存储是专门用于存储和检索向量数据的数据库系统。")
    print("在RAG系统中，向量存储是存储文本Embedding向量的地方，")
    print("它提供了高效的相似度搜索能力，使系统能够快速找到与用户查询语义相似的文本。")
    
    # 演示向量存储
    demonstrate_vector_store()
    
    # 清理临时文件
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量存储的核心功能有了初步了解。")
    print("在实际应用中，您需要根据项目规模和性能需求选择合适的向量库。")

if __name__ == "__main__":
    main()
