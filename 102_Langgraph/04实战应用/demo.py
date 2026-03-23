#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph实战应用示例
展示完整的流程应用开发
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

# 模拟知识库
def knowledge_base_query(query):
    """查询知识库"""
    # 模拟知识库查询结果
    knowledge_base = {
        "LangChain": "LangChain是一个用于构建LLM应用的框架，它提供了丰富的工具和组件。",
        "LangGraph": "LangGraph是LangChain生态中的一个框架，用于构建状态化的多智能体系统。",
        "RAG": "RAG（Retrieval-Augmented Generation）是一种结合检索和生成的技术。",
        "Prompt Engineering": "提示工程是设计和优化提示以获得更好的模型输出的过程。"
    }
    
    # 简单的关键词匹配
    for key, value in knowledge_base.items():
        if key.lower() in query.lower():
            return value
    return "未找到相关信息"

# 定义状态类型
class State:
    def __init__(self, user_input: str, response: str = "", intent: str = "", knowledge: str = ""):
        self.user_input = user_input
        self.response = response
        self.intent = intent
        self.knowledge = knowledge

# 节点1：意图识别
def intent_recognition(state: State) -> State:
    """识别用户意图"""
    print("[节点1] 意图识别")
    
    prompt = f"请识别用户输入的意图，只需返回'查询'、'对话'或'其他'：\n{state.user_input}"
    response = llm.invoke(prompt)
    
    state.intent = response.content.strip()
    print(f"识别的意图：{state.intent}")
    return state

# 节点2：知识库查询
def knowledge_retrieval(state: State) -> State:
    """查询知识库"""
    print("[节点2] 知识库查询")
    
    # 查询知识库
    state.knowledge = knowledge_base_query(state.user_input)
    print(f"知识库查询结果：{state.knowledge}")
    
    # 生成回答
    prompt = f"基于知识库查询结果回答用户问题：\n\n查询结果：{state.knowledge}\n\n用户问题：{state.user_input}\n\n回答："
    response = llm.invoke(prompt)
    
    state.response = response.content
    return state

# 节点3：对话处理
def conversation(state: State) -> State:
    """处理对话"""
    print("[节点3] 对话处理")
    
    prompt = f"请友好地回答用户的问题：\n{state.user_input}\n\n回答："
    response = llm.invoke(prompt)
    
    state.response = response.content
    return state

# 节点4：其他处理
def other_processing(state: State) -> State:
    """处理其他意图"""
    print("[节点4] 其他处理")
    
    prompt = f"请处理用户的请求：\n{state.user_input}\n\n处理结果："
    response = llm.invoke(prompt)
    
    state.response = response.content
    return state

# 条件边：根据意图选择路径
def route_intent(state: State) -> str:
    """根据意图选择路径"""
    if state.intent == "查询":
        return "retrieve"
    elif state.intent == "对话":
        return "conversation"
    else:
        return "other"

# 创建状态图
def create_graph() -> CompiledStateGraph:
    """创建状态图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("intent", intent_recognition)
    graph.add_node("retrieve", knowledge_retrieval)
    graph.add_node("conversation", conversation)
    graph.add_node("other", other_processing)
    
    # 设置入口点
    graph.set_entry_point("intent")
    
    # 添加条件边
    graph.add_conditional_edges(
        "intent",
        route_intent,
        {
            "retrieve": "retrieve",
            "conversation": "conversation",
            "other": "other"
        }
    )
    
    # 添加结束边
    graph.add_edge("retrieve", END)
    graph.add_edge("conversation", END)
    graph.add_edge("other", END)
    
    # 编译状态图
    return graph.compile()

# 测试流程
def main():
    print("LangGraph实战应用示例")
    print("=" * 50)
    
    # 创建状态图
    app = create_graph()
    
    # 示例输入
    test_inputs = [
        "什么是LangChain？",  # 查询
        "你好，今天天气怎么样？",  # 对话
        "帮我写一首诗",  # 其他
        "什么是RAG？"  # 查询
    ]
    
    for user_input in test_inputs:
        print(f"\n用户输入：{user_input}")
        print("-" * 30)
        
        # 运行流程
        result = app.invoke(State(user_input=user_input))
        
        print(f"回答：{result.response}")
        print("-" * 30)
    
    # 交互式模式
    print("\n\n交互式模式")
    print("输入'quit'退出")
    print("=" * 50)
    
    while True:
        user_input = input("请输入：")
        if user_input.lower() == "quit":
            break
        
        result = app.invoke(State(user_input=user_input))
        print(f"\n回答：{result.response}")
        print("-" * 50)

if __name__ == "__main__":
    main()