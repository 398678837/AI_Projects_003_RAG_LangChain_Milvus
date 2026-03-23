#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain集成外部工具示例
展示如何集成外部工具和API
"""

import os
import requests
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

# 外部工具：获取天气信息
def get_weather(city):
    """获取城市天气信息"""
    # 这里使用模拟数据，实际项目中可以集成真实的天气API
    weather_data = {
        "北京": "晴，温度20-25℃",
        "上海": "多云，温度18-22℃",
        "广州": "阴，温度25-30℃",
        "深圳": "晴，温度26-31℃"
    }
    return weather_data.get(city, "未知城市")

# 外部工具：获取当前时间
def get_current_time():
    """获取当前时间"""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建Prompt模板
prompt = PromptTemplate(
    input_variables=["question", "tool_results"],
    template="请根据以下工具执行结果回答问题：\n\n问题：{question}\n\n工具结果：{tool_results}\n\n回答："
)

# 创建LLM链
chain = LLMChain(
    llm=llm,
    prompt=prompt
)

# 处理问题并调用工具
def process_question(question):
    """处理问题并调用相应的工具"""
    tool_results = []
    
    # 检测是否需要天气信息
    if "天气" in question:
        # 提取城市名
        cities = ["北京", "上海", "广州", "深圳"]
        for city in cities:
            if city in question:
                weather = get_weather(city)
                tool_results.append(f"天气信息：{city} {weather}")
                break
    
    # 检测是否需要时间信息
    if "时间" in question or "几点" in question:
        current_time = get_current_time()
        tool_results.append(f"当前时间：{current_time}")
    
    # 如果没有调用工具，返回默认信息
    if not tool_results:
        tool_results.append("未调用任何工具")
    
    return "\n".join(tool_results)

# 测试链
def main():
    print("LangChain集成外部工具示例")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "北京今天天气怎么样？",
        "现在几点了？",
        "上海的天气如何？",
        "什么是LangChain？"
    ]
    
    for question in questions:
        print(f"\n问题：{question}")
        print("-" * 30)
        
        # 调用工具获取结果
        tool_results = process_question(question)
        print(f"工具结果：{tool_results}")
        
        # 运行链
        result = chain.run({
            "question": question,
            "tool_results": tool_results
        })
        
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
        
        tool_results = process_question(user_input)
        print(f"工具结果：{tool_results}")
        
        result = chain.run({
            "question": user_input,
            "tool_results": tool_results
        })
        print(f"\n回答：{result}")
        print("-" * 50)

if __name__ == "__main__":
    main()