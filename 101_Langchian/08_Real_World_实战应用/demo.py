#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain实战应用
展示一个完整的LangChain应用示例
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

# 模拟产品数据库
PRODUCTS = [
    {
        "name": "Smartphone X",
        "price": 999.99,
        "description": "A high-end smartphone with advanced camera features and long battery life."
    },
    {
        "name": "Laptop Pro",
        "price": 1499.99,
        "description": "A powerful laptop designed for professionals with 16GB RAM and 512GB SSD."
    },
    {
        "name": "Wireless Earbuds",
        "price": 129.99,
        "description": "Premium wireless earbuds with active noise cancellation and 24-hour battery life."
    }
]

# 产品查询函数
def search_products(query):
    """根据查询搜索产品"""
    results = []
    for product in PRODUCTS:
        if (query.lower() in product["name"].lower() or 
            query.lower() in product["description"].lower()):
            results.append(product)
    return results

# 创建客服Prompt模板
support_prompt = PromptTemplate(
    input_variables=["query", "products"],
    template="""You are a customer support assistant for an electronics store. Please respond to the customer's query based on the available products.

Available products:
{products}

Customer query:
{query}

Your response should be friendly, helpful, and based on the product information provided. If you don't have information about a specific product, please apologize and offer to help with other products."""
)

# 创建客服链
support_chain = LLMChain(
    llm=llm,
    prompt=support_prompt
)

# 客服处理流程
def customer_support(query):
    """客服处理流程"""
    # 1. 搜索相关产品
    products = search_products(query)
    
    # 2. 构建产品信息字符串
    if products:
        products_str = "\n".join([f"{p['name']}: ${p['price']} - {p['description']}" for p in products])
    else:
        products_str = "No products found matching your query."
    
    # 3. 运行客服链
    response = support_chain.run({
        "query": query,
        "products": products_str
    })
    
    return response

# 测试客服系统
def main():
    print("LangChain Real World Application - Customer Support System")
    print("=" * 50)
    
    # 示例查询
    test_queries = [
        "I'm looking for a smartphone",
        "Tell me about the laptop",
        "What wireless earbuds do you have?",
        "Do you have any tablets?"
    ]
    
    for query in test_queries:
        print(f"\nCustomer: {query}")
        print("-" * 30)
        
        # 运行客服系统
        response = customer_support(query)
        
        print(f"Support: {response}")
        print("-" * 30)
    
    # 交互式客服
    print("\n\nInteractive Customer Support")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("Customer: ")
        if user_input.lower() == "quit":
            break
        
        response = customer_support(user_input)
        print(f"Support: {response}")
        print("-" * 30)

if __name__ == "__main__":
    main()