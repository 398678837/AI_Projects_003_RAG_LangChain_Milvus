#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain进阶链结构示例
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
    template="请分析以下问题的核心内容和需要的专业知识：\n{question}\n\n分析结果："
)

# 创建第二个Prompt模板（详细回答）
answer_prompt = PromptTemplate(
    input_variables=["question", "analysis"],
    template="基于以下分析，详细回答问题：\n\n问题：{question}\n\n分析：{analysis}\n\n详细回答："
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
    print("LangChain进阶链结构示例")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "如何使用LangChain构建一个RAG系统？",
        "LangChain和LangGraph的区别是什么？",
        "如何优化大模型的推理性能？"
    ]
    
    for question in questions:
        print(f"\n问题：{question}")
        print("-" * 30)
        
        # 运行链
        result = sequential_chain.run(question)
        
        print(f"分析：{result['analysis']}")
        print(f"回答：{result['answer']}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\n交互式问答模式")
    print("输入'quit'退出")
    print("=" * 50)
    
    while True:
        user_input = input("请输入问题：")
        if user_input.lower() == "quit":
            break
        
        result = sequential_chain.run(user_input)
        print(f"\n分析：{result['analysis']}")
        print(f"回答：{result['answer']}")
        print("-" * 50)

if __name__ == "__main__":
    main()