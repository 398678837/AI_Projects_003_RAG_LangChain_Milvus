#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qdrant快速入门演示
展示如何使用Qdrant进行向量数据的存储和检索
"""

import os
import sys
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

def demonstrate_qdrant_quickstart():
    """
    演示如何使用Qdrant进行向量数据的存储和检索
    """
    print("=== Qdrant快速入门演示 ===")
    
    # 1. 创建Qdrant客户端
    print("\n1. 创建Qdrant客户端")
    print("   创建Qdrant客户端实例...")
    client = QdrantClient(path="./qdrant_db")
    print("   Qdrant客户端实例创建成功。")
    
    # 2. 创建集合
    print("\n2. 创建集合")
    print("   创建名为'quickstart'的集合...")
    client.recreate_collection(
        collection_name="quickstart",
        vectors_config=VectorParams(size=3, distance=Distance.COSINE)
    )
    print("   集合创建成功。")
    
    # 3. 插入向量
    print("\n3. 插入向量")
    print("   插入3个向量...")
    points = [
        PointStruct(id=1, vector=[1.0, 2.0, 3.0], payload={"color": "red"}),
        PointStruct(id=2, vector=[4.0, 5.0, 6.0], payload={"color": "green"}),
        PointStruct(id=3, vector=[7.0, 8.0, 9.0], payload={"color": "blue"})
    ]
    client.upsert(collection_name="quickstart", points=points)
    print("   向量插入成功。")
    
    # 4. 检索向量
    print("\n4. 检索向量")
    print("   检索与[1.0, 2.0, 3.0]最相似的向量...")
    search_result = client.search(
        collection_name="quickstart",
        query_vector=[1.0, 2.0, 3.0],
        limit=1
    )
    print(f"   检索结果: {search_result}")
    
    # 5. 删除集合
    print("\n5. 删除集合")
    print("   删除名为'quickstart'的集合...")
    client.delete_collection(collection_name="quickstart")
    print("   集合删除成功。")

def main():
    """
    主函数
    """
    print("=== Qdrant快速入门演示 ===")
    print("\n本演示展示了如何使用Qdrant进行向量数据的存储和检索，帮助您快速掌握Qdrant的基本使用方法。")
    
    # 演示Qdrant快速入门
    demonstrate_qdrant_quickstart()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Qdrant的基本使用方法有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的参数和技术。")

if __name__ == "__main__":
    main()
