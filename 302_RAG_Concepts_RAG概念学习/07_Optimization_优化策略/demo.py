#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化策略演示
展示RAG系统的各种优化技术
"""

import os
import shutil
import time
import threading
from functools import lru_cache

# 尝试导入所需库
try:
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.schema import Document
    from langchain.prompts import PromptTemplate
    from langchain.chains import RetrievalQA
    optimization_support = True
except ImportError:
    optimization_support = False
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
        else:
            return "根据提供的文档，我无法回答这个问题。"

class CachedRetriever:
    """
    带缓存的检索器
    """
    def __init__(self, retriever):
        self.retriever = retriever
        self.cache = {}
    
    @lru_cache(maxsize=100)
    def get_relevant_documents(self, query):
        """
        带缓存的文档检索
        """
        print(f"   缓存未命中，执行检索: {query}")
        return self.retriever.get_relevant_documents(query)

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
    
    # 转换为LangChain文档格式
    documents = [
        Document(page_content=text, metadata={"id": i})
        for i, text in enumerate(sample_texts)
    ]
    
    return documents

def demonstrate_caching():
    """
    演示缓存机制
    """
    print("=== 缓存机制演示 ===")
    
    # 初始化Embedding模型
    embeddings = HuggingFaceEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    
    # 创建示例文档
    documents = create_sample_documents()
    
    # 创建向量库
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    # 创建普通检索器
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    
    # 创建带缓存的检索器
    cached_retriever = CachedRetriever(retriever)
    
    # 测试缓存效果
    queries = ["什么是RAG？", "RAG的工作流程是什么？", "什么是RAG？"]
    
    for query in queries:
        print(f"\n查询: {query}")
        start_time = time.time()
        results = cached_retriever.get_relevant_documents(query)
        end_time = time.time()
        print(f"检索时间: {end_time - start_time:.4f}秒")
        print(f"检索到 {len(results)} 个文档")

def demonstrate_batch_processing():
    """
    演示批处理
    """
    print("\n=== 批处理演示 ===")
    
    # 初始化Embedding模型
    embeddings = HuggingFaceEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    
    # 单个文本编码
    single_text = "这是一个测试文本"
    start_time = time.time()
    single_embedding = embeddings.embed_query(single_text)
    single_time = time.time() - start_time
    print(f"单个文本编码时间: {single_time:.4f}秒")
    
    # 批量文本编码
    batch_texts = [f"测试文本{i}" for i in range(10)]
    start_time = time.time()
    batch_embeddings = embeddings.embed_documents(batch_texts)
    batch_time = time.time() - start_time
    print(f"批量文本编码时间: {batch_time:.4f}秒")
    print(f"平均每个文本编码时间: {batch_time / len(batch_texts):.4f}秒")
    print(f"批量处理速度提升: {single_time / (batch_time / len(batch_texts)):.2f}倍")

def demonstrate_parallel_processing():
    """
    演示并行处理
    """
    print("\n=== 并行处理演示 ===")
    
    # 初始化Embedding模型
    embeddings = HuggingFaceEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    
    # 测试文本
    test_texts = [f"测试文本{i}" for i in range(20)]
    
    # 顺序处理
    start_time = time.time()
    for text in test_texts:
        embeddings.embed_query(text)
    sequential_time = time.time() - start_time
    print(f"顺序处理时间: {sequential_time:.4f}秒")
    
    # 并行处理
    def process_text(text):
        return embeddings.embed_query(text)
    
    start_time = time.time()
    threads = []
    for text in test_texts:
        thread = threading.Thread(target=process_text, args=(text,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    parallel_time = time.time() - start_time
    print(f"并行处理时间: {parallel_time:.4f}秒")
    print(f"并行处理速度提升: {sequential_time / parallel_time:.2f}倍")

def demonstrate_optimization():
    """
    演示优化策略
    """
    if not optimization_support:
        print("错误: 缺少必要的库，无法演示优化策略")
        return
    
    print("=== 优化策略演示 ===")
    
    # 清理之前的向量库
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    # 演示缓存机制
    demonstrate_caching()
    
    # 演示批处理
    demonstrate_batch_processing()
    
    # 演示并行处理
    demonstrate_parallel_processing()

def main():
    """
    主函数
    """
    print("=== 优化策略演示 ===")
    print("\nRAG系统的性能和效果受到多种因素的影响，包括文档处理、检索质量、生成质量等。")
    print("优化RAG系统可以提高回答的准确性、减少幻觉、提升响应速度，从而提供更好的用户体验。")
    
    # 演示优化策略
    demonstrate_optimization()
    
    # 清理临时文件
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对RAG系统的优化策略有了初步了解。")
    print("在实际应用中，您需要根据具体场景选择合适的优化策略，以获得最佳的系统性能。")

if __name__ == "__main__":
    main()
