#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语义检索演示
展示不同的检索方法和参数优化
"""

import os
import shutil

# 尝试导入所需库
try:
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.schema import Document
    semantic_retrieval_support = True
except ImportError:
    semantic_retrieval_support = False
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
        "FAISS是Facebook开发的高效向量搜索库，适合实时检索。",
        "文档加载是RAG流程的第一步，将各种格式的文档加载到系统中。",
        "文档切片是将长文档切分为较小的文本块，以便于向量编码和检索。",
        "向量编码是将文本转换为数字向量，使计算机能够理解文本的语义。",
        "语义检索是根据用户查询的语义含义，在向量库中检索最相关的文本块。",
        "增强生成是将检索到的文本块与查询一起输入到语言模型中，生成基于文档的回答。"
    ]
    
    # 转换为LangChain文档格式
    documents = [
        Document(page_content=text, metadata={"id": i, "category": "rag" if i < 4 else "vector_db" if i < 10 else "process"})
        for i, text in enumerate(sample_texts)
    ]
    
    return documents

def demonstrate_semantic_retrieval():
    """
    演示语义检索
    """
    if not semantic_retrieval_support:
        print("错误: 缺少必要的库，无法演示语义检索")
        return
    
    print("=== 语义检索演示 ===")
    
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
    documents = create_sample_documents()
    print(f"   创建了 {len(documents)} 个示例文档")
    
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
    
    # 1. 基本相似度搜索
    print("\n4. 基本相似度搜索")
    query = "什么是RAG？"
    print(f"   查询: {query}")
    
    results = vector_store.similarity_search(
        query=query,
        k=3
    )
    
    print("   检索结果:")
    for i, result in enumerate(results):
        print(f"   {i+1}. {result.page_content}")
    
    # 2. 带分数的相似度搜索
    print("\n5. 带分数的相似度搜索")
    results_with_score = vector_store.similarity_search_with_score(
        query=query,
        k=3
    )
    
    print("   检索结果:")
    for i, (doc, score) in enumerate(results_with_score):
        print(f"   {i+1}. 相似度: {score:.4f}, 内容: {doc.page_content}")
    
    # 3. MMR搜索
    print("\n6. MMR搜索")
    results_mmr = vector_store.max_marginal_relevance_search(
        query=query,
        k=3,
        fetch_k=10,
        lambda_mult=0.5
    )
    
    print("   检索结果:")
    for i, result in enumerate(results_mmr):
        print(f"   {i+1}. {result.page_content}")
    
    # 4. 带过滤器的搜索
    print("\n7. 带过滤器的搜索")
    query = "什么是向量数据库？"
    print(f"   查询: {query}")
    
    results_filtered = vector_store.similarity_search(
        query=query,
        k=3,
        filter={"category": "vector_db"}
    )
    
    print("   检索结果 (只返回vector_db类别的文档):")
    for i, result in enumerate(results_filtered):
        print(f"   {i+1}. {result.page_content}")
    
    # 5. 使用检索器
    print("\n8. 使用检索器")
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    
    query = "RAG的工作流程是什么？"
    print(f"   查询: {query}")
    
    retrieved_docs = retriever.get_relevant_documents(query)
    
    print("   检索结果:")
    for i, doc in enumerate(retrieved_docs):
        print(f"   {i+1}. {doc.page_content}")
    
    # 6. 不同k值的影响
    print("\n9. 不同k值的影响")
    query = "向量编码是什么？"
    print(f"   查询: {query}")
    
    for k in [1, 3, 5]:
        results = vector_store.similarity_search(
            query=query,
            k=k
        )
        print(f"   k={k}时的检索结果:")
        for i, result in enumerate(results):
            print(f"     {i+1}. {result.page_content}")
        print()

def main():
    """
    主函数
    """
    print("=== 语义检索演示 ===")
    print("\n语义检索是根据用户查询的语义含义，在向量库中检索最相关的文本块的过程。")
    print("与传统的关键词检索不同，语义检索能够理解文本的深层含义，")
    print("即使查询和文档使用不同的词汇，也能找到语义相关的内容。")
    
    # 演示语义检索
    demonstrate_semantic_retrieval()
    
    # 清理临时文件
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对语义检索的核心功能有了初步了解。")
    print("在实际应用中，您需要根据具体场景选择合适的检索方法和参数。")

if __name__ == "__main__":
    main()
