#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain智能代理
展示如何使用LangChain创建智能代理
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 工具定义
class CalculatorTool:
    """计算器工具"""
    def run(self, expression):
        """执行计算"""
        try:
            result = eval(expression)
            return f"The result of {expression} is {result}"
        except Exception as e:
            return f"Error: {str(e)}"

class WeatherTool:
    """天气查询工具"""
    def run(self, city):
        """查询天气"""
        weather_data = {
            "Beijing": "Sunny, 20-25°C",
            "Shanghai": "Cloudy, 18-22°C",
            "Guangzhou": "Overcast, 25-30°C",
            "Shenzhen": "Sunny, 26-31°C"
        }
        return weather_data.get(city, "Unknown city")

# 创建工具实例
calculator = CalculatorTool()
weather_tool = WeatherTool()

# 创建代理Prompt模板
agent_prompt = PromptTemplate(
    input_variables=["input", "tools", "tool_results"],
    template="""You are an intelligent assistant. Please analyze the user's input and decide whether to use a tool or directly answer.

Available tools:
1. Calculator: Use this tool to perform mathematical calculations. Input format: Calculator(expression)
2. Weather: Use this tool to query weather information. Input format: Weather(city)

If you need to use a tool, output the tool call in the format:
Tool: ToolName(parameters)

If you can directly answer the user's question, output:
Answer: Your answer

User input: {input}

Previous tool results:
{tool_results}

Your response:"""
)

# 创建代理链
agent_chain = LLMChain(
    llm=llm,
    prompt=agent_prompt
)

# 代理处理流程
def agent_process(input_text):
    """代理处理流程"""
    tool_results = ""
    
    while True:
        # 运行代理链
        response = agent_chain.run({
            "input": input_text,
            "tools": "Calculator, Weather",
            "tool_results": tool_results
        })
        
        # 检查是否需要调用工具
        if response.startswith("Tool:"):
            # 解析工具调用
            tool_call = response[5:].strip()
            print(f"Tool call: {tool_call}")
            
            # 处理工具调用
            if tool_call.startswith("Calculator(") and tool_call.endswith(")"):
                expression = tool_call[11:-1]
                result = calculator.run(expression)
                tool_results = f"Calculator: {result}"
            elif tool_call.startswith("Weather(") and tool_call.endswith(")"):
                city = tool_call[8:-1]
                result = weather_tool.run(city)
                tool_results = f"Weather: {result}"
            else:
                tool_results = "Invalid tool call"
        else:
            # 直接回答
            if response.startswith("Answer:"):
                return response[7:].strip()
            else:
                return response

# 测试代理
def main():
    print("LangChain Intelligent Agent")
    print("=" * 50)
    
    # 示例问题
    test_inputs = [
        "What is 2 + 2?",
        "What's the weather in Beijing?",
        "What is LangChain?",
        "Calculate 123 * 456"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print("-" * 30)
        
        # 运行代理
        result = agent_process(input_text)
        
        print(f"Output: {result}")
        print("-" * 30)
    
    # 交互式模式
    print("\n\nInteractive Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your request: ")
        if user_input.lower() == "quit":
            break
        
        result = agent_process(user_input)
        print(f"\nOutput: {result}")
        print("-" * 50)

if __name__ == "__main__":
    main()