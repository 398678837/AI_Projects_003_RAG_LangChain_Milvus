#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph复杂流程示例
展示更复杂的多节点流程
"""

import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 定义状态类型
class State:
    def __init__(self, question: str, answer: str = "", question_type: str = "", analysis: str = ""):
        self.question = question
        self.answer = answer
        self.question_type = question_type
        self.analysis = analysis

# 节点1：分析问题类型
def analyze_question(state: State) -> State:
    """分析问题类型"""
    print("[节点1] 分析问题类型")
    
    prompt = f"请判断以下问题的类型，只需返回'技术问题'、'非技术问题'或'需要检索'：\n{state.question}"
    response = llm.invoke(prompt)
    
    state.question_type = response.content.strip()
    print(f"问题类型：{state.question_type}")
    return state

# 节点2：分析问题内容
def analyze_content(state: State) -> State:
    """分析问题内容"""
    print("[节点2] 分析问题内容")
    
    prompt = f"请分析以下问题的核心内容和需要的信息：\n{state.question}"
    response = llm.invoke(prompt)
    
    state.analysis = response.content
    print(f"分析结果：{state.analysis}")
    return state

# 节点3：回答技术问题
def answer_technical_question(state: State) -> State:
    """回答技术问题"""
    print("[节点3] 回答技术问题")
    
    prompt = f"基于以下分析，详细回答技术问题：\n\n问题：{state.question}\n\n分析：{state.analysis}\n\n详细回答："
    response = llm.invoke(prompt)
    
    state.answer = response.content
    return state

# 节点4：回答非技术问题
def answer_non_technical_question(state: State) -> State:
    """回答非技术问题"""
    print("[节点4] 回答非技术问题")
    
    prompt = f"基于以下分析，友好回答非技术问题：\n\n问题：{state.question}\n\n分析：{state.analysis}\n\n友好回答："
    response = llm.invoke(prompt)
    
    state.answer = response.content
    return state

# 节点5：检索相关信息
def retrieve_information(state: State) -> State:
    """检索相关信息"""
    print("[节点5] 检索相关信息")
    
    # 模拟检索结果
    retrieval_results = "LangChain是一个用于构建LLM应用的框架，它提供了丰富的工具和组件。RAG是一种结合检索和生成的技术。"
    
    # 基于检索结果回答问题
    prompt = f"基于以下检索结果回答问题：\n\n检索结果：{retrieval_results}\n\n问题：{state.question}\n\n回答："
    response = llm.invoke(prompt)
    
    state.answer = response.content
    return state

# 条件边1：根据问题类型选择路径
def route_question(state: State) -> str:
    """根据问题类型选择路径"""
    if state.question_type == "需要检索":
        return "retrieve"
    else:
        return "analyze_content"

# 条件边2：根据问题类型选择回答路径
def route_answer(state: State) -> str:
    """根据问题类型选择回答路径"""
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
    graph.add_node("analyze_question", analyze_question)
    graph.add_node("analyze_content", analyze_content)
    graph.add_node("technical", answer_technical_question)
    graph.add_node("non_technical", answer_non_technical_question)
    graph.add_node("retrieve", retrieve_information)
    
    # 设置入口点
    graph.set_entry_point("analyze_question")
    
    # 添加条件边
    graph.add_conditional_edges(
        "analyze_question",
        route_question,
        {
            "retrieve": "retrieve",
            "analyze_content": "analyze_content"
        }
    )
    
    graph.add_conditional_edges(
        "analyze_content",
        route_answer,
        {
            "technical": "technical",
            "non_technical": "non_technical"
        }
    )
    
    # 添加结束边
    graph.add_edge("technical", END)
    graph.add_edge("non_technical", END)
    graph.add_edge("retrieve", END)
    
    # 编译状态图
    return graph.compile()

# 测试流程
def main():
    print("LangGraph复杂流程示例")
    print("=" * 50)
    
    # 创建状态图
    app = create_graph()
    
    # 示例问题
    questions = [
        "什么是Python的装饰器？",  # 技术问题
        "今天天气怎么样？",         # 非技术问题
        "LangChain是什么？"         # 需要检索
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