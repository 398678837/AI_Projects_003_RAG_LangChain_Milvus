#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain检索增强生成(RAG)
展示如何使用LangChain构建RAG系统
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 模拟文档库
DOCUMENTS = [
    "LangChain is a framework for building LLM applications, providing rich tools and components.",
    "LangChain supports multiple large models, including OpenAI, Anthropic, Google, etc.",
    "RAG (Retrieval-Augmented Generation) is a technique that combines retrieval and generation.",
    "Core components of LangChain include PromptTemplate, LLM, Chain, Agent, etc.",
    "LangGraph is a framework in the LangChain ecosystem for building stateful multi-agent systems."
]

# 简单的检索函数
def retrieve_documents(query, top_k=3):
    """根据查询检索相关文档"""
    # 这里使用简单的关键词匹配，实际项目中可以使用更复杂的检索方法
    results = []
    for doc in DOCUMENTS:
        if any(keyword in doc.lower() for keyword in query.lower().split()):
            results.append(doc)
    return results[:top_k]

# 创建RAG Prompt模板
rag_prompt = PromptTemplate(
    input_variables=["query", "documents"],
    template="Please answer the question based on the following documents:\n\nDocuments:\n{documents}\n\nQuestion: {query}\n\nAnswer:"
)

# 创建RAG链
rag_chain = LLMChain(
    llm=llm,
    prompt=rag_prompt
)

# 完整的RAG流程
def rag_pipeline(query):
    """完整的RAG处理流程"""
    # 1. 检索相关文档
    documents = retrieve_documents(query)
    print(f"Retrieved documents: {documents}")
    
    # 2. 构建文档字符串
    documents_str = "\n".join(documents)
    
    # 3. 运行RAG链
    result = rag_chain.run({
        "query": query,
        "documents": documents_str
    })
    
    return result

# 测试RAG系统
def main():
    print("LangChain Retrieval-Augmented Generation (RAG)")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "What is LangChain?",
        "Which large models does LangChain support?",
        "What is RAG?",
        "What are the core components of LangChain?",
        "What is LangGraph?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        print("-" * 30)
        
        # 运行RAG流程
        answer = rag_pipeline(question)
        
        print(f"Answer: {answer}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\nInteractive QA Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your question: ")
        if user_input.lower() == "quit":
            break
        
        answer = rag_pipeline(user_input)
        print(f"\nAnswer: {answer}")
        print("-" * 30)

if __name__ == "__main__":
    main()