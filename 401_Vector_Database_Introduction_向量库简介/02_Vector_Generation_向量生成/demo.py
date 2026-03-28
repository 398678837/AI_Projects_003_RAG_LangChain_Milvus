#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量生成演示
展示如何将文本转换为向量表示
"""

import os
import sys
import numpy as np
from sentence_transformers import SentenceTransformer

def demonstrate_vector_generation():
    """
    演示如何将文本转换为向量表示
    """
    print("=== 向量生成演示 ===")
    
    # 1. 加载预训练的Embedding模型
    print("\n1. 加载预训练的Embedding模型")
    print("   加载sentence-transformers的all-MiniLM-L6-v2模型...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("   模型加载完成。")
    
    # 2. 生成文本向量
    print("\n2. 生成文本向量")
    sentences = ["向量库是一种专门用于存储和检索向量数据的数据库。", "向量库的主要作用是实现语义相似检索。"]
    print("   输入文本:")
    for i, sentence in enumerate(sentences):
        print(f"      句子{i+1}: {sentence}")
    
    print("   生成文本向量...")
    embeddings = model.encode(sentences)
    print("   向量生成完成。")
    
    # 3. 打印向量
    print("\n3. 打印向量")
    print("   生成的文本向量:")
    for i, embedding in enumerate(embeddings):
        print(f"      句子{i+1}的向量: {embedding[:5]}... (长度: {len(embedding)})")
    
    # 4. 向量的应用
    print("\n4. 向量的应用")
    print("   - 语义检索: 输入问题向量，找出语义最相似的文本")
    print("   - 文本分类: 将向量输入分类模型，进行文本分类")
    print("   - 聚类分析: 将向量输入聚类模型，进行聚类分析")
    print("   - 推荐系统: 将向量用于个性化推荐")

def main():
    """
    主函数
    """
    print("=== 向量生成演示 ===")
    print("\n本演示展示了如何将文本转换为向量表示，帮助您快速掌握向量生成的技术。")
    
    # 演示向量生成
    demonstrate_vector_generation()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量生成的技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的Embedding模型和技术。")

if __name__ == "__main__":
    main()
