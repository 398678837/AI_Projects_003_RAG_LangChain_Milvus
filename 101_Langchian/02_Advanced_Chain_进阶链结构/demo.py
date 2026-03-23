#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain进阶链结构
展示更复杂的链结构，如SequentialChain
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain, SequentialChain

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 创建第一个Prompt模板（问题分析）
analysis_prompt = PromptTemplate(
    input_variables=["question"],
    template="Please analyze the core content and required expertise of the following question:\n{question}\n\nAnalysis result:"
)

# 创建第二个Prompt模板（详细回答）
answer_prompt = PromptTemplate(
    input_variables=["question", "analysis"],
    template="Based on the following analysis, provide a detailed answer to the question:\n\nQuestion: {question}\n\nAnalysis: {analysis}\n\nDetailed answer:"
)

# 创建第一个链（分析链）
analysis_chain = LLMChain(
    llm=llm,
    prompt=analysis_prompt,
    output_key="analysis"
)

# 创建第二个链（回答链）
answer_chain = LLMChain(
    llm=llm,
    prompt=answer_prompt,
    output_key="answer"
)

# 创建顺序链
sequential_chain = SequentialChain(
    chains=[analysis_chain, answer_chain],
    input_variables=["question"],
    output_variables=["analysis", "answer"]
)

# 测试链
def main():
    print("LangChain Advanced Chain Structure")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "How to build a RAG system using LangChain?",
        "What is the difference between LangChain and LangGraph?",
        "How to optimize LLM inference performance?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        print("-" * 30)
        
        # 运行链
        result = sequential_chain.run(question)
        
        print(f"Analysis: {result['analysis']}")
        print(f"Answer: {result['answer']}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\nInteractive QA Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your question: ")
        if user_input.lower() == "quit":
            break
        
        result = sequential_chain.run(user_input)
        print(f"\nAnalysis: {result['analysis']}")
        print(f"Answer: {result['answer']}")
        print("-" * 30)

if __name__ == "__main__":
    main()