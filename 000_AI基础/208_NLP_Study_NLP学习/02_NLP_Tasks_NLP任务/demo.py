#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP任务演示
展示NLP的常见任务
"""

import os
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag

def demonstrate_nlp_tasks():
    """
    演示NLP的常见任务
    """
    print("=== NLP任务演示 ===")
    
    # 1. 下载NLTK数据
    print("\n1. 下载NLTK数据")
    print("   下载vader_lexicon、maxent_ne_chunker、words数据...")
    nltk.download('vader_lexicon')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    print("   NLTK数据下载完成。")
    
    # 2. 情感分析
    print("\n2. 情感分析")
    text = "I love NLP! It's amazing."
    print(f"   输入文本: {text}")
    
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(f"   情感分析结果: {sentiment}")
    
    # 3. 命名实体识别
    print("\n3. 命名实体识别")
    text = "Barack Obama was born in Hawaii."
    print(f"   输入文本: {text}")
    
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    ne_tree = ne_chunk(tagged_words)
    print(f"   命名实体识别结果: {ne_tree}")
    
    # 4. 文本分类
    print("\n4. 文本分类")
    text = "NLP is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."
    print(f"   输入文本: {text}")
    
    # 简单的文本分类示例
    if "NLP" in text:
        print("   文本分类结果: NLP相关")
    else:
        print("   文本分类结果: 非NLP相关")
    
    # 5. 机器翻译
    print("\n5. 机器翻译")
    text = "Hello, world!"
    print(f"   输入文本: {text}")
    
    # 简单的机器翻译示例
    print("   机器翻译结果: 你好，世界！")

def main():
    """
    主函数
    """
    print("=== NLP任务演示 ===")
    print("\n本演示展示了NLP的常见任务，帮助您快速掌握NLP的任务类型。")
    
    # 演示NLP任务
    demonstrate_nlp_tasks()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对NLP的常见任务有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的NLP任务和工具。")

if __name__ == "__main__":
    main()
