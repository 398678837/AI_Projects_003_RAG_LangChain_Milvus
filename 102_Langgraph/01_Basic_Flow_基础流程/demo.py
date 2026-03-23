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
    prompt = f"Please determine the type of the following question, just return 'technical' or 'non-technical':\n{state.question}"
    response = llm.invoke(prompt)
    
    # 提取问题类型
    question_type = response.content.strip()
    state.question_type = question_type
    
    print(f"Question type: {question_type}")
    return state

# 节点2：回答技术问题
def answer_technical_question(state: State) -> State:
    """回答技术问题"""
    print("[节点2] 回答技术问题")
    
    # 使用LLM回答技术问题
    prompt = f"Please answer the following technical question: {state.question}"
    response = llm.invoke(prompt)
    
    # 提取回答
    state.answer = response.content
    
    print(f"Technical answer: {state.answer}")
    return state

# 节点3：回答非技术问题
def answer_non_technical_question(state: State) -> State:
    """回答非技术问题"""
    print("[节点3] 回答非技术问题")
    
    # 使用LLM回答非技术问题
    prompt = f"Please answer the following non-technical question: {state.question}"
    response = llm.invoke(prompt)
    
    # 提取回答
    state.answer = response.content
    
    print(f"Non-technical answer: {state.answer}")
    return state

# 条件边：根据问题类型选择路径
def route_question(state: State):
    """根据问题类型选择路径"""
    if "technical" in state.question_type.lower():
        return "technical"
    else:
        return "non_technical"

# 创建状态图
def create_graph():
    """创建状态图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("analyze", analyze_question)
    graph.add_node("technical", answer_technical_question)
    graph.add_node("non_technical", answer_non_technical_question)
    
    # 添加边
    graph.add_edge("analyze", route_question)
    graph.add_edge("technical", END)
    graph.add_edge("non_technical", END)
    
    # 设置入口节点
    graph.set_entry_point("analyze")
    
    # 编译图
    return graph.compile()

# 测试图
def main():
    print("LangGraph Basic Flow Example")
    print("=" * 50)
    
    # 创建并编译图
    app = create_graph()
    
    # 测试问题
    test_questions = [
        "What is LangChain?",
        "What's the weather today?",
        "How to build a RAG system?",
        "Tell me a joke."
    ]
    
    for question in test_questions:
        print(f"\nQuestion: {question}")
        print("-" * 50)
        
        # 运行图
        result = app.invoke(State(question=question))
        
        print(f"Answer: {result.answer}")
        print("-" * 50)
    
    # 交互式测试
    print("\n\nInteractive Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your question: ")
        if user_input.lower() == "quit":
            break
        
        result = app.invoke(State(question=user_input))
        print(f"\nAnswer: {result.answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()