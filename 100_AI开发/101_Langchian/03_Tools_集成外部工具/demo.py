#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain集成外部工具
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
        "Beijing": "Sunny, temperature 20-25°C",
        "Shanghai": "Cloudy, temperature 18-22°C",
        "Guangzhou": "Overcast, temperature 25-30°C",
        "Shenzhen": "Sunny, temperature 26-31°C"
    }
    return weather_data.get(city, "Unknown city")

# 外部工具：获取当前时间
def get_current_time():
    """获取当前时间"""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建Prompt模板
prompt = PromptTemplate(
    input_variables=["question", "tool_results"],
    template="Please answer the question based on the following tool execution results:\n\nQuestion: {question}\n\nTool results: {tool_results}\n\nAnswer:"
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
    if "weather" in question.lower():
        # 提取城市名
        cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
        for city in cities:
            if city.lower() in question.lower():
                weather = get_weather(city)
                tool_results.append(f"Weather information: {city} {weather}")
                break
    
    # 检测是否需要时间信息
    if "time" in question.lower() or "what time" in question.lower():
        current_time = get_current_time()
        tool_results.append(f"Current time: {current_time}")
    
    # 如果没有调用工具，返回默认信息
    if not tool_results:
        tool_results.append("No tools called")
    
    return "\n".join(tool_results)

# 测试链
def main():
    print("LangChain Integration with External Tools")
    print("=" * 50)
    
    # 示例问题
    questions = [
        "What's the weather in Beijing today?",
        "What time is it now?",
        "How's the weather in Shanghai?",
        "What is LangChain?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        print("-" * 30)
        
        # 调用工具获取结果
        tool_results = process_question(question)
        print(f"Tool results: {tool_results}")
        
        # 运行链
        result = chain.run({
            "question": question,
            "tool_results": tool_results
        })
        
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
        
        tool_results = process_question(user_input)
        print(f"Tool results: {tool_results}")
        
        result = chain.run({
            "question": user_input,
            "tool_results": tool_results
        })
        print(f"\nAnswer: {result}")
        print("-" * 50)

if __name__ == "__main__":
    main()