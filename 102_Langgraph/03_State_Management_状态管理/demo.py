#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph状态管理示例
展示如何管理和持久化状态
"""

import os
import json
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 定义状态类型
class State:
    def __init__(self, query: str = "", conversation_history: list = None, 
                 current_answer: str = "", context: dict = None):
        self.query = query
        self.conversation_history = conversation_history or []
        self.current_answer = current_answer
        self.context = context or {}
    
    def to_dict(self):
        """转换为字典"""
        return {
            "query": self.query,
            "conversation_history": self.conversation_history,
            "current_answer": self.current_answer,
            "context": self.context
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建"""
        return cls(
            query=data.get("query", ""),
            conversation_history=data.get("conversation_history", []),
            current_answer=data.get("current_answer", ""),
            context=data.get("context", {})
        )

# 节点1：处理输入
def process_input(state: State) -> State:
    """处理输入"""
    print("[节点1] 处理输入")
    
    # 添加到对话历史
    if state.query:
        state.conversation_history.append({"role": "user", "content": state.query})
    
    print(f"Input: {state.query}")
    print(f"Conversation history length: {len(state.conversation_history)}")
    return state

# 节点2：生成回答
def generate_answer(state: State) -> State:
    """生成回答"""
    print("[节点2] 生成回答")
    
    # 构建对话历史
    history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in state.conversation_history])
    
    # 生成回答
    prompt = f"Based on the conversation history, please generate a response:\n\n{history_str}\n\nAssistant:"
    response = llm.invoke(prompt)
    
    # 更新状态
    state.current_answer = response.content
    state.conversation_history.append({"role": "assistant", "content": state.current_answer})
    
    print(f"Answer: {state.current_answer}")
    return state

# 节点3：更新上下文
def update_context(state: State) -> State:
    """更新上下文"""
    print("[节点3] 更新上下文")
    
    # 提取关键信息
    prompt = f"Extract key information from the conversation:\n\n{state.current_answer}\n\nKey information:"
    response = llm.invoke(prompt)
    
    # 更新上下文
    state.context["key_information"] = response.content
    state.context["last_updated"] = "2026-03-23"
    
    print(f"Context updated: {state.context}")
    return state

# 节点4：持久化状态
def persist_state(state: State) -> State:
    """持久化状态"""
    print("[节点4] 持久化状态")
    
    # 模拟持久化
    # 实际项目中可以保存到数据库或文件
    with open("conversation_state.json", "w", encoding="utf-8") as f:
        json.dump(state.to_dict(), f, ensure_ascii=False, indent=2)
    
    print("State persisted to conversation_state.json")
    return state

# 创建状态管理图
def create_state_management_graph():
    """创建状态管理图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("process", process_input)
    graph.add_node("answer", generate_answer)
    graph.add_node("context", update_context)
    graph.add_node("persist", persist_state)
    
    # 添加边
    graph.add_edge("process", "answer")
    graph.add_edge("answer", "context")
    graph.add_edge("context", "persist")
    graph.add_edge("persist", END)
    
    # 设置入口节点
    graph.set_entry_point("process")
    
    # 编译图
    return graph.compile()

# 加载状态
def load_state():
    """加载状态"""
    try:
        with open("conversation_state.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return State.from_dict(data)
    except FileNotFoundError:
        return State()

# 测试状态管理
def main():
    print("LangGraph State Management Example")
    print("=" * 50)
    
    # 加载历史状态
    initial_state = load_state()
    print(f"Loaded state with {len(initial_state.conversation_history)} messages")
    
    # 创建并编译图
    app = create_state_management_graph()
    
    # 测试查询
    test_queries = [
        "Hello, how are you?",
        "What's your name?",
        "What can you do?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        
        # 更新查询
        initial_state.query = query
        
        # 运行图
        result = app.invoke(initial_state)
        
        # 更新初始状态
        initial_state = result
        
        print(f"Final Answer: {result.current_answer}")
        print("-" * 50)
    
    # 交互式测试
    print("\n\nInteractive Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your message: ")
        if user_input.lower() == "quit":
            break
        
        # 更新查询
        initial_state.query = user_input
        
        # 运行图
        result = app.invoke(initial_state)
        
        # 更新初始状态
        initial_state = result
        
        print(f"\nAnswer: {result.current_answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()