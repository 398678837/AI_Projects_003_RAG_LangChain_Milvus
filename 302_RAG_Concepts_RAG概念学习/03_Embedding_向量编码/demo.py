#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量编码演示
展示文本到向量的转换和相似度计算
"""

import numpy as np

# 尝试导入所需库
try:
    from langchain.embeddings import HuggingFaceEmbeddings
    embedding_support = True
except ImportError:
    embedding_support = False
    print("警告: 缺少langchain或sentence-transformers库，请安装")

def cosine_similarity(vec1, vec2):
    """
    计算余弦相似度
    """
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def demonstrate_embedding():
    """
    演示向量编码
    """
    if not embedding_support:
        print("错误: 缺少必要的库，无法演示向量编码")
        return
    
    print("=== 向量编码演示 ===")
    
    # 初始化Embedding模型
    print("\n1. 初始化Embedding模型")
    print("   使用模型: paraphrase-multilingual-MiniLM-L12-v2")
    
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        print("   模型初始化成功")
        
    except Exception as e:
        print(f"   模型初始化失败: {e}")
        return
    
    # 单文本编码
    print("\n2. 单文本编码")
    text = "这是一个测试文本"
    vector = embeddings.embed_query(text)
    print(f"   文本: {text}")
    print(f"   向量维度: {len(vector)}")
    print(f"   向量前5个值: {vector[:5]}")
    
    # 批量编码
    print("\n3. 批量编码")
    texts = [
        "人工智能是研究如何使计算机模拟人类智能的科学",
        "机器学习是人工智能的一个分支，专注于算法设计",
        "深度学习是机器学习的一个子集，使用神经网络",
        "天气今天很好，适合户外活动"
    ]
    
    vectors = embeddings.embed_documents(texts)
    print(f"   批量编码完成，共 {len(vectors)} 个文本")
    for i, (text, vector) in enumerate(zip(texts, vectors)):
        print(f"   文本{i+1} (长度: {len(text)}): {text[:30]}...")
        print(f"     向量维度: {len(vector)}")
    
    # 相似度计算
    print("\n4. 相似度计算")
    # 计算前三个文本之间的相似度
    for i in range(3):
        for j in range(i+1, 3):
            sim = cosine_similarity(vectors[i], vectors[j])
            print(f"   文本{i+1}与文本{j+1}的相似度: {sim:.4f}")
    
    # 计算与第四个文本的相似度
    print("\n5. 与无关文本的相似度")
    for i in range(3):
        sim = cosine_similarity(vectors[i], vectors[3])
        print(f"   文本{i+1}与文本4的相似度: {sim:.4f}")

def main():
    """
    主函数
    """
    print("=== 向量编码演示 ===")
    print("\n向量编码是将文本转换为数字向量的过程，使计算机能够理解文本的语义。")
    print("在RAG系统中，向量编码是连接文本和向量数据库的桥梁。")
    
    # 演示向量编码
    demonstrate_embedding()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量编码的核心功能有了初步了解。")
    print("在实际应用中，您需要根据语言类型和性能需求选择合适的Embedding模型。")

if __name__ == "__main__":
    main()
