#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain评估与优化
展示如何评估和优化LangChain应用
"""

import os
import time
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

# 评估数据集
EVALUATION_DATA = [
    {
        "question": "What is LangChain?",
        "reference_answer": "LangChain is a framework for building applications powered by language models."
    },
    {
        "question": "What are the core components of LangChain?",
        "reference_answer": "Core components of LangChain include Prompts, Language Models, Chains, Agents, and Memory."
    },
    {
        "question": "What is RAG?",
        "reference_answer": "RAG (Retrieval-Augmented Generation) is a technique that combines retrieval of relevant information with generation to produce more accurate and contextually appropriate responses."
    }
]

# 创建基础Prompt模板
basic_prompt = PromptTemplate(
    input_variables=["question"],
    template="Please answer the following question:\n{question}\n\nAnswer:"
)

# 创建优化后的Prompt模板
optimized_prompt = PromptTemplate(
    input_variables=["question"],
    template="Please provide a clear, concise, and accurate answer to the following question:\n{question}\n\nAnswer:"
)

# 创建链
basic_chain = LLMChain(llm=llm, prompt=basic_prompt)
optimized_chain = LLMChain(llm=llm, prompt=optimized_prompt)

# 评估函数
def evaluate_chain(chain, data):
    """评估链的性能"""
    results = []
    total_time = 0
    
    for item in data:
        start_time = time.time()
        response = chain.run(item["question"])
        end_time = time.time()
        
        # 计算响应时间
        response_time = end_time - start_time
        total_time += response_time
        
        # 简单的评估指标
        # 这里使用基于字符长度的简单评估，实际项目中可以使用更复杂的评估方法
        length_score = min(len(response) / len(item["reference_answer"]), 1.0)
        
        results.append({
            "question": item["question"],
            "response": response,
            "reference_answer": item["reference_answer"],
            "response_time": response_time,
            "length_score": length_score
        })
    
    # 计算平均响应时间和平均得分
    avg_response_time = total_time / len(data)
    avg_length_score = sum(item["length_score"] for item in results) / len(results)
    
    return results, avg_response_time, avg_length_score

# 测试评估
def main():
    print("LangChain Evaluation and Optimization")
    print("=" * 50)
    
    # 评估基础链
    print("Evaluating basic chain...")
    basic_results, basic_time, basic_score = evaluate_chain(basic_chain, EVALUATION_DATA)
    
    # 评估优化后的链
    print("\nEvaluating optimized chain...")
    optimized_results, optimized_time, optimized_score = evaluate_chain(optimized_chain, EVALUATION_DATA)
    
    # 输出评估结果
    print("\n\nEvaluation Results")
    print("=" * 50)
    
    print(f"Basic Chain:")
    print(f"Average response time: {basic_time:.4f} seconds")
    print(f"Average length score: {basic_score:.4f}")
    print()
    
    print(f"Optimized Chain:")
    print(f"Average response time: {optimized_time:.4f} seconds")
    print(f"Average length score: {optimized_score:.4f}")
    print()
    
    # 详细结果
    print("\nDetailed Results")
    print("=" * 50)
    
    for i, (basic, optimized) in enumerate(zip(basic_results, optimized_results)):
        print(f"\nQuestion {i+1}: {basic['question']}")
        print("-" * 50)
        print(f"Reference Answer: {basic['reference_answer']}")
        print(f"Basic Response: {basic['response']}")
        print(f"Optimized Response: {optimized['response']}")
        print(f"Basic Time: {basic['response_time']:.4f}s, Score: {basic['length_score']:.4f}")
        print(f"Optimized Time: {optimized['response_time']:.4f}s, Score: {optimized['length_score']:.4f}")

if __name__ == "__main__":
    main()