#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain基础问答链示例
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
        "什么是LangChain？",
        "LangChain和LangGraph的区别是什么？",
        "如何使用LangChain构建一个问答系统？"
    ]
    
    for question in questions:
        print(f"\n问题：{question}")
        print("-" * 30)
        
        # 运行链
        result = chain.run(question)
        
        print(f"回答：{result}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\n交互式问答模式")
    print("输入'quit'退出")
    print("=" * 50)
    
    while True:
        user_input = input("请输入问题：")
        if user_input.lower() == "quit":
            break
        
        result = chain.run(user_input)
        print(f"\n回答：{result}")
        print("-" * 50)

if __name__ == "__main__":
    main()