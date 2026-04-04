#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP应用场景演示
展示NLP的实际应用场景
"""

import os
import sys
from transformers import pipeline

def demonstrate_nlp_applications():
    """
    演示NLP的实际应用场景
    """
    print("=== NLP应用场景演示 ===")
    
    # 1. 智能客服
    print("\n1. 智能客服")
    print("   加载GPT模型进行智能客服对话...")
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
    user_input = "Hello, how can I help you?"
    response = chatbot(user_input)
    print(f"   智能客服回复: {response}")
    
    # 2. 机器翻译
    print("\n2. 机器翻译")
    print("   加载BART模型进行机器翻译...")
    translation = pipeline("translation_en_to_fr", model="facebook/bart-base")
    result = translation("Hello, world!")
    print(f"   机器翻译结果: {result}")
    
    # 3. 文本摘要
    print("\n3. 文本摘要")
    print("   加载T5模型进行文本摘要...")
    summarization = pipeline("summarization", model="t5-small")
    text = "NLP is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."
    result = summarization(text, max_length=30, min_length=10)
    print(f"   文本摘要结果: {result}")
    
    # 4. 情感分析
    print("\n4. 情感分析")
    print("   加载BERT模型进行情感分析...")
    sentiment_analysis = pipeline("sentiment-analysis", model="bert-base-uncased")
    result = sentiment_analysis("I love NLP! It's amazing.")
    print(f"   情感分析结果: {result}")
    
    # 5. 文本生成
    print("\n5. 文本生成")
    print("   加载GPT模型进行文本生成...")
    text_generation = pipeline("text-generation", model="gpt2")
    result = text_generation("NLP is", max_length=50, num_return_sequences=1)
    print(f"   文本生成结果: {result}")

def main():
    """
    主函数
    """
    print("=== NLP应用场景演示 ===")
    print("\n本演示展示了NLP的实际应用场景，帮助您快速掌握NLP的应用技术。")
    
    # 演示NLP应用场景
    demonstrate_nlp_applications()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对NLP的应用技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的NLP技术和工具。")

if __name__ == "__main__":
    main()
