#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain实战应用示例
展示完整的RAG系统实现
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
    "LangChain是一个用于构建LLM应用的框架，它提供了丰富的工具和组件。",
    "LangChain支持多种大模型，包括OpenAI、Anthropic、Google等。",
    "RAG（Retrieval-Augmented Generation）是一种结合检索和生成的技术。",
    "LangChain的核心组件包括PromptTemplate、LLM、Chain、Agent等。",
    "LangGraph是LangChain生态中的一个框架，用于构建状态化的多智能体系统。"
]

# 简单的检索函数
def retrieve_documents(query, top_k=3):
    """根据查询检索相关文档"""
    # 这里使用简单的关键词匹配，实际项目中可以使用更复杂的检索方法
    results = []
    for doc in DOCUMENTS:
        if any(keyword in doc for keyword in query.split()):
            results.append(doc)
    return results[:top_k]

# 创建RAG Prompt模板
rag_prompt = PromptTemplate(
    input_variables=["query", "documents"],
    template="请根据以下文档回答问题：\n\n文档：\n{documents}\n\n问题：{query}\n\n回答："
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
    print(f"检索到的文档：{documents}")
    
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
    print("LangChain实战应用示例 - RAG系统")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "什么是LangChain？",
        "LangChain支持哪些大模型？",
        "什么是RAG？",
        "LangChain的核心组件有哪些？",
        "LangGraph是什么？"
    ]
    
    for question in questions:
        print(f"\n问题：{question}")
        print("-" * 30)
        
        # 运行RAG流程
        answer = rag_pipeline(question)
        
        print(f"回答：{answer}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\n交互式问答模式")
    print("输入'quit'退出")
    print("=" * 50)
    
    while True:
        user_input = input("请输入问题：")
        if user_input.lower() == "quit":
            break
        
        answer = rag_pipeline(user_input)
        print(f"\n回答：{answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()