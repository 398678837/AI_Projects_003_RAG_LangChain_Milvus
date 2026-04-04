#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain记忆管理
展示如何使用LangChain实现记忆管理
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

# 定义记忆类
class ConversationMemory:
    """对话记忆管理"""
    def __init__(self, max_history=5):
        """初始化记忆"""
        self.max_history = max_history
        self.history = []
    
    def add_message(self, role, content):
        """添加消息到记忆"""
        self.history.append({"role": role, "content": content})
        # 保持记忆长度
        if len(self.history) > self.max_history * 2:  # 每个对话包含用户和助手的消息
            self.history = self.history[-self.max_history * 2:]
    
    def get_history(self):
        """获取记忆"""
        return self.history
    
    def get_history_str(self):
        """获取记忆字符串"""
        history_str = ""
        for msg in self.history:
            if msg["role"] == "user":
                history_str += f"User: {msg['content']}\n"
            else:
                history_str += f"Assistant: {msg['content']}\n"
        return history_str

# 创建Prompt模板
memory_prompt = PromptTemplate(
    input_variables=["input", "history"],
    template="""You are a helpful assistant. Please answer the user's question based on the conversation history and the current input.

Conversation history:
{history}

Current input:
{input}

Your response:"""
)

# 创建链
memory_chain = LLMChain(
    llm=llm,
    prompt=memory_prompt
)

# 测试记忆管理
def main():
    print("LangChain Memory Management")
    print("=" * 50)
    
    # 创建记忆实例
    memory = ConversationMemory(max_history=3)
    
    # 示例对话
    conversations = [
        "Hello, my name is Alice.",
        "What's my name?",
        "I'm learning LangChain.",
        "What am I learning?",
        "Can you recommend some resources for LangChain?"
    ]
    
    for i, input_text in enumerate(conversations):
        print(f"\nTurn {i+1}")
        print(f"User: {input_text}")
        print("-" * 30)
        
        # 获取历史对话
        history_str = memory.get_history_str()
        print(f"History:\n{history_str}")
        
        # 运行链
        response = memory_chain.run({
            "input": input_text,
            "history": history_str
        })
        
        print(f"Assistant: {response}")
        
        # 添加到记忆
        memory.add_message("user", input_text)
        memory.add_message("assistant", response)
        print("-" * 30)
    
    # 交互式对话
    print("\n\nInteractive Conversation")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        
        # 获取历史对话
        history_str = memory.get_history_str()
        
        # 运行链
        response = memory_chain.run({
            "input": user_input,
            "history": history_str
        })
        
        print(f"Assistant: {response}")
        
        # 添加到记忆
        memory.add_message("user", user_input)
        memory.add_message("assistant", response)
        print("-" * 30)

if __name__ == "__main__":
    main()