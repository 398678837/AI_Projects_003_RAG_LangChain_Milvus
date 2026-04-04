#!/usr/bin/env python3
"""
基础Agent智能体示例
演示如何创建一个基础的Agent智能体
"""

import os
import openai
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from langchain.utilities import SerpAPIWrapper

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_basic_agent():
    """
    创建基础Agent智能体
    
    Returns:
        Agent: 初始化后的Agent实例
    """
    # 初始化LLM
    llm = OpenAI(temperature=0)
    
    # 初始化工具
    # 1. 搜索工具
    search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))
    
    # 2. 数学计算工具
    llm_math_chain = LLMMathChain(llm=llm, verbose=True)
    
    # 定义工具列表
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="用于搜索最新信息，回答关于当前事件、新闻、天气等问题"
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="用于进行数学计算，回答数学问题"
        )
    ]
    
    # 初始化Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    
    return agent

def main():
    """
    主函数
    """
    print("基础Agent智能体示例")
    print("=" * 50)
    
    try:
        # 创建Agent
        agent = create_basic_agent()
        
        # 示例1: 搜索问题
        print("\n示例1: 搜索问题")
        query1 = "2026年4月4日的天气如何？"
        print(f"查询: {query1}")
        result1 = agent.run(query1)
        print(f"结果: {result1}")
        
        # 示例2: 数学计算
        print("\n示例2: 数学计算")
        query2 = "3.14的平方乘以100等于多少？"
        print(f"查询: {query2}")
        result2 = agent.run(query2)
        print(f"结果: {result2}")
        
    except Exception as e:
        print(f"出错: {e}")
        print("请确保已配置正确的API密钥")

if __name__ == "__main__":
    main()