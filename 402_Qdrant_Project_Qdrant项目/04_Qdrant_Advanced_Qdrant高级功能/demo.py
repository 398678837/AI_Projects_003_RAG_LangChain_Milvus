#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qdrant高级功能演示
展示Qdrant的高级功能
"""

import os
import sys
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

def demonstrate_qdrant_advanced():
    """
    演示Qdrant的高级功能
    """
    print("=== Qdrant高级功能演示 ===")
    
    # 1. 创建Qdrant客户端
    print("\n1. 创建Qdrant客户端")
    print("   创建Qdrant客户端实例...")
    client = QdrantClient(path="./qdrant_db")
    print("   Qdrant客户端实例创建成功。")
    
    # 2. 创建集合
    print("\n2. 创建集合")
    print("   创建名为'advanced'的集合...")
    client.recreate_collection(
        collection_name="advanced",
        vectors_config=VectorParams(size=3, distance=Distance.COSINE)
    )
    print("   集合创建成功。")
    
    # 3. 插入向量
    print("\n3. 插入向量")
    print("   插入6个向量...")
    points = [
        PointStruct(id=1, vector=[1.0, 2.0, 3.0], payload={"color": "red", "size": 10}),
        PointStruct(id=2, vector=[4.0, 5.0, 6.0], payload={"color": "green", "size": 20}),
        PointStruct(id=3, vector=[7.0, 8.0, 9.0], payload={"color": "blue", "size": 30}),
        PointStruct(id=4, vector=[1.0, 2.0, 3.0], payload={"color": "red", "size": 40}),
        PointStruct(id=5, vector=[4.0, 5.0, 6.0], payload={"color": "green", "size": 50}),
        PointStruct(id=6, vector=[7.0, 8.0, 9.0], payload={"color": "blue", "size": 60})
    ]
    client.upsert(collection_name="advanced", points=points)
    print("   向量插入成功。")
    
    # 4. 过滤检索
    print("\n4. 过滤检索")
    print("   检索颜色为'red'且大小大于10的向量...")
    search_result = client.search(
        collection_name="advanced",
        query_vector=[1.0, 2.0, 3.0],
        limit=1,
        query_filter=Filter(
            must=[
                FieldCondition(key="color", match=MatchValue(value="red")),
                FieldCondition(key="size", range={"gt": 10})
            ]
        )
    )
    print(f"   检索结果: {search_result}")
    
    # 5. 删除集合
    print("\n5. 删除集合")
    print("   删除名为'advanced'的集合...")
    client.delete_collection(collection_name="advanced")
    print("   集合删除成功。")

def main():
    """
    主函数
    """
    print("=== Qdrant高级功能演示 ===")
    print("\n本演示展示了Qdrant的高级功能，帮助您快速掌握Qdrant的高级使用方法。")
    
    # 演示Qdrant高级功能
    demonstrate_qdrant_advanced()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Qdrant的高级使用方法有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的参数和技术。")

if __name__ == "__main__":
    main()
