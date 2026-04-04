#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qdrant应用场景演示
展示Qdrant的实际应用场景
"""

import os
import sys
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

def demonstrate_qdrant_applications():
    """
    演示Qdrant的实际应用场景
    """
    print("=== Qdrant应用场景演示 ===")
    
    # 1. 创建Qdrant客户端
    print("\n1. 创建Qdrant客户端")
    print("   创建Qdrant客户端实例...")
    client = QdrantClient(path="./qdrant_db")
    print("   Qdrant客户端实例创建成功。")
    
    # 2. 创建集合
    print("\n2. 创建集合")
    print("   创建名为'applications'的集合...")
    client.recreate_collection(
        collection_name="applications",
        vectors_config=VectorParams(size=3, distance=Distance.COSINE)
    )
    print("   集合创建成功。")
    
    # 3. 插入向量
    print("\n3. 插入向量")
    print("   插入3个向量...")
    points = [
        PointStruct(id=1, vector=[1.0, 2.0, 3.0], payload={"category": "RAG", "name": "向量库"}),
        PointStruct(id=2, vector=[4.0, 5.0, 6.0], payload={"category": "推荐系统", "name": "个性化推荐"}),
        PointStruct(id=3, vector=[7.0, 8.0, 9.0], payload={"category": "图像检索", "name": "相似图像检索"})
    ]
    client.upsert(collection_name="applications", points=points)
    print("   向量插入成功。")
    
    # 4. 检索向量
    print("\n4. 检索向量")
    print("   检索与[1.0, 2.0, 3.0]最相似的向量...")
    search_result = client.search(
        collection_name="applications",
        query_vector=[1.0, 2.0, 3.0],
        limit=1
    )
    print(f"   检索结果: {search_result}")
    
    # 5. 删除集合
    print("\n5. 删除集合")
    print("   删除名为'applications'的集合...")
    client.delete_collection(collection_name="applications")
    print("   集合删除成功。")

def main():
    """
    主函数
    """
    print("=== Qdrant应用场景演示 ===")
    print("\n本演示展示了Qdrant的实际应用场景，帮助您快速掌握Qdrant的应用技术。")
    
    # 演示Qdrant应用场景
    demonstrate_qdrant_applications()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Qdrant的应用技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的参数和技术。")

if __name__ == "__main__":
    main()
