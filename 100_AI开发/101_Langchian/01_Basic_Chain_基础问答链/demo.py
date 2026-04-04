#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain基础问答链
使用PromptTemplate+LLM链式调用
适配Qwen等通用大模型
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 配置API密钥（请根据实际情况修改）
# 可以通过环境变量设置：export API_KEY="your-api-key"
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
# 这里使用OpenAI兼容接口，可以适配Qwen等模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
    # 其他模型的base_url示例：
    # base_url="https://open.bigmodel.cn/api/mcp"
    # base_url="https://api.openai.com/v1"
)

# 创建Prompt模板
prompt = PromptTemplate(
    input_variables=["question"],
    template="请回答以下问题：\n{question}\n\n回答："
)

# 创建LLM链
chain = LLMChain(
    llm=llm,
    prompt=prompt
)

# 测试问答
def main():
    print("LangChain基础问答链示例")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "What is LangChain?",
        "What are the core components of LangChain?",
        "How to use LangChain to build a QA system?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        print("-" * 30)
        
        # 运行链
        result = chain.run(question)
        
        print(f"Answer: {result}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\nInteractive QA Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your question: ")
        if user_input.lower() == "quit":
            break
        
        result = chain.run(user_input)
        print(f"\nAnswer: {result}")
        print("-" * 50)

if __name__ == "__main__":
    main()