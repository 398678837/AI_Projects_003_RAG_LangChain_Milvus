#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph复杂流程示例
包含多个节点和更复杂的流程设计
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

# 定义状态类型
class State:
    def __init__(self, query: str, analysis: str = "", answer: str = "", 
                 needs_research: bool = False, research_result: str = ""):
        self.query = query
        self.analysis = analysis
        self.answer = answer
        self.needs_research = needs_research
        self.research_result = research_result

# 节点1：分析查询
def analyze_query(state: State) -> State:
    """分析查询"""
    print("[节点1] 分析查询")
    
    # 使用LLM分析查询
    prompt = f"Please analyze the following query and determine if it requires research:\n{state.query}\n\nAnalysis:"
    response = llm.invoke(prompt)
    
    # 提取分析结果
    state.analysis = response.content
    
    # 判断是否需要研究
    if "research" in state.analysis.lower() or "needs more information" in state.analysis.lower():
        state.needs_research = True
    
    print(f"Analysis: {state.analysis}")
    print(f"Needs research: {state.needs_research}")
    return state

# 节点2：研究查询
def research_query(state: State) -> State:
    """研究查询"""
    print("[节点2] 研究查询")
    
    # 模拟研究过程
    # 实际项目中可以集成搜索引擎或数据库
    state.research_result = f"Research result for: {state.query}"
    
    print(f"Research result: {state.research_result}")
    return state

# 节点3：生成回答
def generate_answer(state: State) -> State:
    """生成回答"""
    print("[节点3] 生成回答")
    
    # 构建提示
    if state.research_result:
        prompt = f"Please answer the query based on the analysis and research:\n\nQuery: {state.query}\n\nAnalysis: {state.analysis}\n\nResearch: {state.research_result}\n\nAnswer:"
    else:
        prompt = f"Please answer the query based on the analysis:\n\nQuery: {state.query}\n\nAnalysis: {state.analysis}\n\nAnswer:"
    
    # 生成回答
    response = llm.invoke(prompt)
    state.answer = response.content
    
    print(f"Answer: {state.answer}")
    return state

# 节点4：验证回答
def validate_answer(state: State) -> State:
    """验证回答"""
    print("[节点4] 验证回答")
    
    # 验证回答质量
    prompt = f"Please evaluate if the following answer is complete and accurate for the query:\n\nQuery: {state.query}\n\nAnswer: {state.answer}\n\nEvaluation:"
    response = llm.invoke(prompt)
    
    # 提取验证结果
    evaluation = response.content
    print(f"Validation: {evaluation}")
    
    return state

# 条件边：判断是否需要研究
def route_research(state: State):
    """判断是否需要研究"""
    if state.needs_research:
        return "research"
    else:
        return "answer"

# 创建复杂状态图
def create_complex_graph():
    """创建复杂状态图"""
    # 初始化状态图
    graph = StateGraph(State)
    
    # 添加节点
    graph.add_node("analyze", analyze_query)
    graph.add_node("research", research_query)
    graph.add_node("answer", generate_answer)
    graph.add_node("validate", validate_answer)
    
    # 添加边
    graph.add_edge("analyze", route_research)
    graph.add_edge("research", "answer")
    graph.add_edge("answer", "validate")
    graph.add_edge("validate", END)
    
    # 设置入口节点
    graph.set_entry_point("analyze")
    
    # 编译图
    return graph.compile()

# 测试复杂图
def main():
    print("LangGraph Advanced Flow Example")
    print("=" * 50)
    
    # 创建并编译图
    app = create_complex_graph()
    
    # 测试查询
    test_queries = [
        "What is LangChain?",
        "How to implement a RAG system with LangChain?",
        "Tell me about the latest developments in AI."
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