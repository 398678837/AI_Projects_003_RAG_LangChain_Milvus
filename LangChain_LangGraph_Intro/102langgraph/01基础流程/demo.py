#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph基础流程示例
包含2个节点+条件边判断问题类型
"""

import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph

# 配置API密钥（请根据实际情况修改）
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 定义状态类型
class State:
    def __init__(self, question: str, answer: str = "", question_type: str = ""):
        self.question = question
        self.answer = answer
        self.question_type = question_type

# 节点1：分析问题类型
def analyze_question(state: State) -> State:
    """分析问题类型"""
    print("[节点1] 分析问题类型")
    
    # 使用LLM分析问题类型
    prompt = f"请判断以下问题的类型，只需返回'技术问题'或'非技术问题'：\n{state.question}"
    response = llm.invoke(prompt)
    
    # 提取问题类型
    question_type = response.content.strip()
    state.question_type = question_type
    
    print(f"问题类型：{question_type}")
    return state

# 节点2：回答技术问题
def answer_technical_question(state: State) -> State:
    """回答技术问题"""
    print("[节点2] 回答技术问题")
    
    # 使用LLM回答技术问题
    prompt = f"请详细回答以下技术问题：\n{state.question}"
    response = llm.invoke(prompt)
    
    state.answer = response.content
    return state

# 节点3：回答非技术问题
def answer_non_technical_question(state: State) -> State:
    """回答非技术问题"""
    print("[节点3] 回答非技术问题")
    
    # 使用LLM回答非技术问题
    prompt = f"请友好回答以下非技术问题：\n{state.question}"
    response = llm.invoke(prompt)
    
    state.answer = response.content
    return state

# 条件边：根据问题类型选择路径
def route_question(state: State) -> str:
    """根据问题类型选择路径"""
    if state.question_type == "技术问题":
        return "technical"
    else:
        return "non_technical"

# 创建状态图
def create_graph() -> CompiledStateGraph:
    """创建状态图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("analyze", analyze_question)
    graph.add_node("technical", answer_technical_question)
    graph.add_node("non_technical", answer_non_technical_question)
    
    # 设置入口点
    graph.set_entry_point("analyze")
    
    # 添加条件边
    graph.add_conditional_edges(
        "analyze",
        route_question,
        {
            "technical": "technical",
            "non_technical": "non_technical"
        }
    )
    
    # 添加结束边
    graph.add_edge("technical", END)
    graph.add_edge("non_technical", END)
    
    # 编译状态图
    return graph.compile()

# 测试流程
def main():
    print("LangGraph基础流程示例")
    print("=" * 50)
    
    # 创建状态图
    app = create_graph()
    
    # 示例问题
    questions = [
        "什么是Python的装饰器？",  # 技术问题
        "今天天气怎么样？",         # 非技术问题
        "如何使用LangChain构建RAG系统？"  # 技术问题
    ]
    
    for question in questions:
        print(f"\n问题：{question}")
        print("-" * 30)
        
        # 运行流程
        result = app.invoke(State(question=question))
        
        print(f"回答：{result.answer}")
        print("-" * 30)
    
    # 交互式问答
    print("\n\n交互式问答模式")
    print("输入'quit'退出")
    print("=" * 50)
    
    while True:
        user_input = input("请输入问题：")
        if user_input.lower() == "quit":
            break
        
        result = app.invoke(State(question=user_input))
        print(f"\n回答：{result.answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()