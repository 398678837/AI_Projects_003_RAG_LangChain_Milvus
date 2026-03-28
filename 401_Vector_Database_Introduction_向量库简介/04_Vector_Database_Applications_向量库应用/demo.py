#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量库应用演示
展示向量库的实际应用场景
"""

import os
import sys
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_vector_database_applications():
    """
    演示向量库的实际应用场景
    """
    print("=== 向量库应用演示 ===")
    
    # 1. RAG系统应用
    print("\n1. RAG系统应用")
    print("   RAG系统是一种基于检索增强生成的系统，广泛应用于知识库问答、文档生成等领域。")
    print("   向量库用于存储知识库的向量表示，实现语义相似检索。")
    
    # 2. 推荐系统应用
    print("\n2. 推荐系统应用")
    print("   推荐系统是一种用于个性化推荐的系统，广泛应用于电商、视频等领域。")
    print("   向量库用于存储用户和物品的向量表示，实现个性化推荐。")
    
    # 3. 图像检索应用
    print("\n3. 图像检索应用")
    print("   图像检索是一种用于相似图像检索的系统，广泛应用于图片搜索、安防监控等领域。")
    print("   向量库用于存储图像的向量表示，实现相似图像检索。")
    
    # 4. 语音识别应用
    print("\n4. 语音识别应用")
    print("   语音识别是一种用于语音转文字的系统，广泛应用于智能助理、语音搜索等领域。")
    print("   向量库用于存储语音的向量表示，实现语音识别和检索。")
    
    # 5. 实际应用示例
    print("\n5. 实际应用示例")
    print("   假设我们有一个知识库，包含以下文档:")
    print("      - 文档1: 向量库是一种专门用于存储和检索向量数据的数据库。")
    print("      - 文档2: 向量库的主要作用是实现语义相似检索。")
    print("      - 文档3: 推荐系统是一种用于个性化推荐的系统。")
    
    print("   当用户提问: 什么是向量库？")
    print("   我们可以使用向量库进行语义检索，找出语义最相似的文档。")
    
    # 加载预训练的Embedding模型
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # 生成文本向量
    documents = ["向量库是一种专门用于存储和检索向量数据的数据库。", "向量库的主要作用是实现语义相似检索。", "推荐系统是一种用于个性化推荐的系统。"]
    query = "什么是向量库？"
    
    document_embeddings = model.encode(documents)
    query_embedding = model.encode(query)
    
    # 计算余弦相似度
    similarities = cosine_similarity([query_embedding], document_embeddings)[0]
    
    # 找出最相似的文档
    most_similar_index = np.argmax(similarities)
    most_similar_document = documents[most_similar_index]
    most_similar_similarity = similarities[most_similar_index]
    
    print(f"   最相似的文档: {most_similar_document}")
    print(f"   相似度: {most_similar_similarity:.4f}")

def main():
    """
    主函数
    """
    print("=== 向量库应用演示 ===")
    print("\n本演示展示了向量库的实际应用场景，帮助您快速掌握向量库的应用技术。")
    
    # 演示向量库的应用
    demonstrate_vector_database_applications()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对向量库的应用技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的向量库和技术。")

if __name__ == "__main__":
    main()
