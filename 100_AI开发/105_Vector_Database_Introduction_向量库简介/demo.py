#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量库简介演示
展示向量库的基本概念和技术
"""

import os
import sys
import numpy as np
from sentence_transformers import SentenceTransformer

def demonstrate_vector_database():
    """
    演示向量库的基本概念
    """
    print("=== 向量库简介演示 ===")
    
    # 1. 向量库基本概念
    print("\n1. 向量库基本概念")
    
    # 向量库是什么
    print("   向量库是一种专门用于存储和检索向量数据的数据库。")
    
    # 向量库的作用
    print("   向量库的主要作用是实现语义相似检索，广泛应用于RAG系统、推荐系统、图像检索等领域。")
    
    # 2. 向量生成演示
    print("\n2. 向量生成演示")
    
    # 加载预训练的Embedding模型
    print("   加载预训练的Embedding模型...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # 生成文本向量
    print("   生成文本向量...")
    sentences = ["向量库是一种专门用于存储和检索向量数据的数据库。", "向量库的主要作用是实现语义相似检索。"]
    embeddings = model.encode(sentences)
    
    # 打印向量
    print("   生成的文本向量:")
    for i, embedding in enumerate(embeddings):
        print(f"      句子{i+1}的向量: {embedding[:5]}... (长度: {len(embedding)})")
    
    # 3. 向量相似度计算
    print("\n3. 向量相似度计算")
    
    # 计算余弦相似度
    print("   计算余弦相似度...")
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(embeddings)[0][1]
    
    # 打印相似度
    print(f"   两个句子的余弦相似度: {similarity:.4f}")
    
    # 4. 向量库应用场景
    print("\n4. 向量库应用场景")
    
    # RAG系统
    print("   RAG系统: 向量库用于存储知识库的向量表示，实现语义相似检索。")
    
    # 推荐系统
    print("   推荐系统: 向量库用于存储用户和物品的向量表示，实现个性化推荐。")
    
    # 图像检索
    print("   图像检索: 向量库用于存储图像的向量表示，实现相似图像检索。")
    
    # 5. 向量库选型
    print("\n5. 向量库选型")
    
    # Qdrant
    print("   Qdrant: 轻量、本地一键运行、CPU兼容、最适合快速做Demo。")
    
    # Milvus
    print("   Milvus: 企业级生产常用、功能更强、部署稍重。")

def main():
    """
    主函数
    """
    print("=== 向量库简介演示 ===")
    print("\n本演示展示了向量库的基本概念和技术，包括向量生成、向量相似度计算、向量库应用场景和选型。")
    
    # 演示向量库的基本概念
    demonstrate_vector_database()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量库的基本概念和技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的向量库和技术。")

if __name__ == "__main__":
    main()
