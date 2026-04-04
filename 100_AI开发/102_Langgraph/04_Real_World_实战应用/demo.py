#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph实战应用
展示一个完整的LangGraph应用示例
"""

import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# 配置API密钥
api_key = os.getenv("API_KEY", "your-api-key")

# 配置大模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Qwen模型的API地址
)

# 模拟知识库
KNOWLEDGE_BASE = {
    "langchain": "LangChain is a framework for building applications powered by language models. It provides tools and components for working with LLMs.",
    "langgraph": "LangGraph is a framework for building stateful, multi-agent applications. It extends LangChain with graph-based workflows.",
    "rag": "RAG (Retrieval-Augmented Generation) is a technique that combines retrieval of relevant information with generation to produce more accurate responses."
}

# 定义状态类型
class State:
    def __init__(self, query: str, intent: str = "", 
                 knowledge: str = "", answer: str = ""):
        self.query = query
        self.intent = intent
        self.knowledge = knowledge
        self.answer = answer

# 节点1：意图识别
def identify_intent(state: State) -> State:
    """识别用户意图"""
    print("[节点1] 识别用户意图")
    
    # 使用LLM识别意图
    prompt = f"Please identify the intent of the following query. Possible intents: 'question', 'conversation', 'command'.\nQuery: {state.query}\n\nIntent:"
    response = llm.invoke(prompt)
    
    # 提取意图
    state.intent = response.content.strip()
    
    print(f"Intent: {state.intent}")
    return state

# 节点2：知识检索
def retrieve_knowledge(state: State) -> State:
    """检索相关知识"""
    print("[节点2] 检索相关知识")
    
    # 简单的知识检索
    for key, value in KNOWLEDGE_BASE.items():
        if key in state.query.lower():
            state.knowledge = value
            break
    
    print(f"Retrieved knowledge: {state.knowledge}")
    return state

# 节点3：生成回答
def generate_answer(state: State) -> State:
    """生成回答"""
    print("[节点3] 生成回答")
    
    # 根据意图和知识生成回答
    if state.intent == "question":
        if state.knowledge:
            prompt = f"Based on the knowledge, answer the question:\n\nKnowledge: {state.knowledge}\n\nQuestion: {state.query}\n\nAnswer:"
        else:
            prompt = f"Answer the question:\n\nQuestion: {state.query}\n\nAnswer:"
    elif state.intent == "conversation":
        prompt = f"Have a conversation about:\n\n{state.query}\n\nResponse:"
    else:
        prompt = f"Execute the command:\n\n{state.query}\n\nResponse:"
    
    # 生成回答
    response = llm.invoke(prompt)
    state.answer = response.content
    
    print(f"Generated answer: {state.answer}")
    return state

# 节点4：回答验证
def validate_answer(state: State) -> State:
    """验证回答"""
    print("[节点4] 验证回答")
    
    # 验证回答质量
    prompt = f"Please evaluate if the following answer is appropriate for the query:\n\nQuery: {state.query}\n\nAnswer: {state.answer}\n\nEvaluation:"
    response = llm.invoke(prompt)
    
    # 提取验证结果
    evaluation = response.content
    print(f"Validation: {evaluation}")
    
    return state

# 条件边：判断是否需要知识检索
def route_knowledge(state: State):
    """判断是否需要知识检索"""
    if state.intent == "question":
        return "retrieve"
    else:
        return "answer"

# 创建实战应用图
def create_real_world_graph():
    """创建实战应用图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("intent", identify_intent)
    graph.add_node("retrieve", retrieve_knowledge)
    graph.add_node("answer", generate_answer)
    graph.add_node("validate", validate_answer)
    
    # 添加边
    graph.add_edge("intent", route_knowledge)
    graph.add_edge("retrieve", "answer")
    graph.add_edge("answer", "validate")
    graph.add_edge("validate", END)
    
    # 设置入口节点
    graph.set_entry_point("intent")
    
    # 编译图
    return graph.compile()

# 测试实战应用
def main():
    print("LangGraph Real World Application")
    print("=" * 50)
    
    # 创建并编译图
    app = create_real_world_graph()
    
    # 测试查询
    test_queries = [
        "What is LangChain?",
        "Tell me a joke about AI.",
        "How to use RAG with LangChain?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        
        # 运行图
        result = app.invoke(State(query=query))
        
        print(f"Final Answer: {result.answer}")
        print("-" * 50)
    
    # 交互式测试
    print("\n\nInteractive Mode")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Please enter your query: ")
        if user_input.lower() == "quit":
            break
        
        result = app.invoke(State(query=user_input))
        print(f"\nFinal Answer: {result.answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()