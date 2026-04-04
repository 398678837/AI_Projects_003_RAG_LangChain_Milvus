#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP基础演示
展示NLP的基本概念和技术
"""

import os
import sys
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def demonstrate_nlp_basics():
    """
    演示NLP的基本概念和技术
    """
    print("=== NLP基础演示 ===")
    
    # 1. 下载NLTK数据
    print("\n1. 下载NLTK数据")
    print("   下载punkt、stopwords、wordnet数据...")
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    print("   NLTK数据下载完成。")
    
    # 2. 分词
    print("\n2. 分词")
    text = "NLP is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."
    print(f"   输入文本: {text}")
    
    # 句子分词
    sentences = sent_tokenize(text)
    print(f"   句子分词结果: {sentences}")
    
    # 单词分词
    words = word_tokenize(text)
    print(f"   单词分词结果: {words}")
    
    # 3. 停用词移除
    print("\n3. 停用词移除")
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    print(f"   停用词移除结果: {filtered_words}")
    
    # 4. 词形还原
    print("\n4. 词形还原")
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    print(f"   词形还原结果: {lemmatized_words}")
    
    # 5. 词性标注
    print("\n5. 词性标注")
    from nltk.tag import pos_tag
    tagged_words = pos_tag(lemmatized_words)
    print(f"   词性标注结果: {tagged_words}")

def main():
    """
    主函数
    """
    print("=== NLP基础演示 ===")
    print("\n本演示展示了NLP的基本概念和技术，帮助您快速掌握NLP的基础知识。")
    
    # 演示NLP基础
    demonstrate_nlp_basics()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对NLP的基本概念和技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的NLP技术和工具。")

if __name__ == "__main__":
    main()
