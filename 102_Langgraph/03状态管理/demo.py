#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph状态管理示例
展示如何管理和持久化流程状态
"""

import os
import json
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
    def __init__(self, question: str, answer: str = "", history: list = None, session_id: str = ""):
        self.question = question
        self.answer = answer
        self.history = history or []
        self.session_id = session_id

    def to_dict(self):
        """将状态转换为字典"""
        return {
            "question": self.question,
            "answer": self.answer,
            "history": self.history,
            "session_id": self.session_id
        }

    @classmethod
    def from_dict(cls, data):
        """从字典创建状态"""
        return cls(
            question=data.get("question", ""),
            answer=data.get("answer", ""),
            history=data.get("history", []),
            session_id=data.get("session_id", "")
        )

# 状态持久化函数
def save_state(state: State, filename: str):
    """保存状态到文件"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(state.to_dict(), f, ensure_ascii=False, indent=2)

# 状态加载函数
def load_state(filename: str) -> State:
    """从文件加载状态"""
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return State.from_dict(data)

# 节点1：回答问题
def answer_question(state: State) -> State:
    """回答问题"""
    print("[节点1] 回答问题")
    
    # 构建历史上下文
    history_str = "\n".join([f"Q: {item['question']}\nA: {item['answer']}" for item in state.history])
    
    # 构建提示
    prompt = f"根据历史对话和当前问题回答：\n\n历史对话：\n{history_str}\n\n当前问题：{state.question}\n\n回答："
    
    # 调用大模型
    response = llm.invoke(prompt)
    state.answer = response.content
    
    # 更新历史记录
    state.history.append({
        "question": state.question,
        "answer": state.answer
    })
    
    print(f"回答：{state.answer}")
    return state

# 节点2：保存状态
def save_session_state(state: State) -> State:
    """保存会话状态"""
    print("[节点2] 保存会话状态")
    
    # 生成会话文件名
    session_file = f"session_{state.session_id}.json"
    
    # 保存状态
    save_state(state, session_file)
    print(f"会话状态已保存到 {session_file}")
    
    return state

# 创建状态图
def create_graph() -> CompiledStateGraph:
    """创建状态图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("answer", answer_question)
    graph.add_node("save", save_session_state)
    
    # 设置入口点
    graph.set_entry_point("answer")
    
    # 添加边
    graph.add_edge("answer", "save")
    graph.add_edge("save", END)
    
    # 编译状态图
    return graph.compile()

# 测试流程
def main():
    print("LangGraph状态管理示例")
    print("=" * 50)
    
    # 创建状态图
    app = create_graph()
    
    # 测试多轮对话
    session_id = "test_session_1"
    state = State(session_id=session_id)
    
    # 示例问题
    questions = [
        "什么是LangChain？",
        "它有哪些核心组件？",
        "如何使用它构建RAG系统？"
    ]
    
    for i, question in enumerate(questions):
        print(f"\n轮次 {i+1}")
        print(f"问题：{question}")
        print("-" * 30)
        
        # 更新当前问题
        state.question = question
        
        # 运行流程
        state = app.invoke(state)
        
        print(f"历史记录长度：{len(state.history)}")
        print("-" * 30)
    
    # 测试加载状态
    print("\n\n测试加载状态")
    print("=" * 50)
    
    # 加载保存的状态
    loaded_state = load_state(f"session_{session_id}.json")
    print(f"加载的会话ID：{loaded_state.session_id}")
    print(f"加载的历史记录长度：{len(loaded_state.history)}")
    
    # 继续对话
    new_question = "LangGraph是什么？"
    print(f"\n新问题：{new_question}")
    print("-" * 30)
    
    loaded_state.question = new_question
    result = app.invoke(loaded_state)
    
    print(f"回答：{result.answer}")
    print(f"更新后的历史记录长度：{len(result.history)}")
    print("-" * 30)

if __name__ == "__main__":
    main()