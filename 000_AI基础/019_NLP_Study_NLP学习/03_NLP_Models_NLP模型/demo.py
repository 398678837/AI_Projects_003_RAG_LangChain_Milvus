#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP模型演示
展示NLP的常见模型
"""

import os
import sys
from transformers import pipeline

def demonstrate_nlp_models():
    """
    演示NLP的常见模型
    """
    print("=== NLP模型演示 ===")
    
    # 1. BERT模型
    print("\n1. BERT模型")
    print("   加载BERT模型进行情感分析...")
    sentiment_analysis = pipeline("sentiment-analysis", model="bert-base-uncased")
    result = sentiment_analysis("I love NLP! It's amazing.")
    print(f"   BERT模型情感分析结果: {result}")
    
    # 2. GPT模型
    print("\n2. GPT模型")
    print("   加载GPT模型进行文本生成...")
    text_generation = pipeline("text-generation", model="gpt2")
    result = text_generation("NLP is", max_length=50, num_return_sequences=1)
    print(f"   GPT模型文本生成结果: {result}")
    
    # 3. T5模型
    print("\n3. T5模型")
    print("   加载T5模型进行文本摘要...")
    summarization = pipeline("summarization", model="t5-small")
    text = "NLP is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."
    result = summarization(text, max_length=30, min_length=10)
    print(f"   T5模型文本摘要结果: {result}")
    
    # 4. BART模型
    print("\n4. BART模型")
    print("   加载BART模型进行文本翻译...")
    translation = pipeline("translation_en_to_fr", model="facebook/bart-base")
    result = translation("Hello, world!")
    print(f"   BART模型文本翻译结果: {result}")
    
    # 5. RoBERTa模型
    print("\n5. RoBERTa模型")
    print("   加载RoBERTa模型进行文本分类...")
    text_classification = pipeline("text-classification", model="roberta-base")
    result = text_classification("NLP is a subfield of artificial intelligence.")
    print(f"   RoBERTa模型文本分类结果: {result}")

def main():
    """
    主函数
    """
    print("=== NLP模型演示 ===")
    print("\n本演示展示了NLP的常见模型，帮助您快速掌握NLP的模型类型。")
    
    # 演示NLP模型
    demonstrate_nlp_models()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对NLP的常见模型有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的NLP模型和工具。")

if __name__ == "__main__":
    main()
