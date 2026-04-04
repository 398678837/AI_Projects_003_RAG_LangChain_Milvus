#!/usr/bin/env python3
"""
RAG系统评测示例
演示如何评测RAG系统的性能
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
import json

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_rag_system():
    """
    创建RAG系统
    
    Returns:
        RetrievalQA: RAG系统实例
    """
    # 示例文档
    text_files = ["data/document1.txt", "data/document2.txt"]
    documents = []
    
    try:
        for file_path in text_files:
            loader = TextLoader(file_path)
            documents.extend(loader.load())
    except Exception as e:
        print(f"文档加载失败: {e}")
        print("使用示例数据创建RAG系统")
        # 使用示例数据
        from langchain.document_loaders import TextLoader
        from io import StringIO
        
        # 创建示例文档
        sample_doc1 = "RAG系统是一种结合检索和生成的AI技术，通过从外部知识库检索相关信息，增强大模型的生成能力。RAG系统的核心组件包括向量数据库、嵌入模型和大语言模型。"
        sample_doc2 = "RAG系统的工作流程包括：1. 数据准备阶段：收集和预处理文档数据；2. 索引阶段：将文档转换为向量并存储到向量数据库；3. 检索阶段：根据用户查询检索相关文档；4. 生成阶段：结合检索结果和大模型生成回答。"
        
        # 加载示例文档
        from langchain.docstore.document import Document
        doc1 = Document(page_content=sample_doc1, metadata={"source": "sample_doc1"})
        doc2 = Document(page_content=sample_doc2, metadata={"source": "sample_doc2"})
        documents.extend([doc1, doc2])
    
    # 分割文本
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    # 创建向量数据库
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    
    # 创建RAG系统
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    
    return qa

def evaluate_rag_system(qa, test_questions):
    """
    评测RAG系统
    
    Args:
        qa (RetrievalQA): RAG系统实例
        test_questions (list): 测试问题列表
    
    Returns:
        dict: 评测结果
    """
    results = []
    
    for question in test_questions:
        try:
            # 执行查询
            result = qa({"query": question})
            
            # 保存结果
            results.append({
                "question": question,
                "answer": result["result"],
                "sources": [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]
            })
            
        except Exception as e:
            print(f"评测出错: {e}")
            results.append({
                "question": question,
                "answer": "出错",
                "sources": []
            })
    
    return results

def calculate_metrics(results):
    """
    计算评测指标
    
    Args:
        results (list): 评测结果列表
    
    Returns:
        dict: 评测指标
    """
    # 简单的评测指标
    metrics = {
        "total_questions": len(results),
        "successful_answers": sum(1 for r in results if r["answer"] != "出错"),
        "avg_sources": sum(len(r["sources"]) for r in results) / len(results) if results else 0
    }
    
    metrics["success_rate"] = metrics["successful_answers"] / metrics["total_questions"] * 100
    
    return metrics

def main():
    """
    主函数
    """
    print("RAG系统评测示例")
    print("=" * 50)
    
    # 创建RAG系统
    print("正在创建RAG系统...")
    qa = create_rag_system()
    
    # 测试问题
    test_questions = [
        "什么是RAG系统？",
        "RAG系统的工作流程是什么？",
        "RAG系统的核心组件有哪些？",
        "如何实现一个RAG系统？"
    ]
    
    # 评测RAG系统
    print("\n正在评测RAG系统...")
    results = evaluate_rag_system(qa, test_questions)
    
    # 计算评测指标
    metrics = calculate_metrics(results)
    
    # 输出结果
    print("\n评测结果:")
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    
    print("\n详细结果:")
    for i, result in enumerate(results):
        print(f"\n问题 {i+1}: {result['question']}")
        print(f"回答: {result['answer']}")
        print(f"参考文档: {result['sources']}")

if __name__ == "__main__":
    main()