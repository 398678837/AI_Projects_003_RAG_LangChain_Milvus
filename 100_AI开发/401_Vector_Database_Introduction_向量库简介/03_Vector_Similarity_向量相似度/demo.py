#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量相似度演示
展示如何计算向量之间的相似度
"""

import os
import sys
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_vector_similarity():
    """
    演示如何计算向量之间的相似度
    """
    print("=== 向量相似度演示 ===")
    
    # 1. 加载预训练的Embedding模型
    print("\n1. 加载预训练的Embedding模型")
    print("   加载sentence-transformers的all-MiniLM-L6-v2模型...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("   模型加载完成。")
    
    # 2. 生成文本向量
    print("\n2. 生成文本向量")
    sentences = ["向量库是一种专门用于存储和检索向量数据的数据库。", "向量库的主要作用是实现语义相似检索。", "推荐系统是一种用于个性化推荐的系统。"]
    print("   输入文本:")
    for i, sentence in enumerate(sentences):
        print(f"      句子{i+1}: {sentence}")
    
    print("   生成文本向量...")
    embeddings = model.encode(sentences)
    print("   向量生成完成。")
    
    # 3. 计算余弦相似度
    print("\n3. 计算余弦相似度")
    print("   计算句子1和句子2的余弦相似度...")
    similarity_1_2 = cosine_similarity(embeddings)[0][1]
    print(f"   句子1和句子2的余弦相似度: {similarity_1_2:.4f}")
    
    print("\n   计算句子1和句子3的余弦相似度...")
    similarity_1_3 = cosine_similarity(embeddings)[0][2]
    print(f"   句子1和句子3的余弦相似度: {similarity_1_3:.4f}")
    
    print("\n   计算句子2和句子3的余弦相似度...")
    similarity_2_3 = cosine_similarity(embeddings)[1][2]
    print(f"   句子2和句子3的余弦相似度: {similarity_2_3:.4f}")
    
    # 4. 相似度的应用
    print("\n4. 相似度的应用")
    print("   - 语义检索: 输入问题向量，找出语义最相似的文本")
    print("   - 文本分类: 将向量输入分类模型，进行文本分类")
    print("   - 聚类分析: 将向量输入聚类模型，进行聚类分析")
    print("   - 推荐系统: 将向量用于个性化推荐")

def main():
    """
    主函数
    """
    print("=== 向量相似度演示 ===")
    print("\n本演示展示了如何计算向量之间的相似度，帮助您快速掌握向量相似度的技术。")
    
    # 演示向量相似度
    demonstrate_vector_similarity()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量相似度的技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的相似度计算方法和技术。")

if __name__ == "__main__":
    main()
