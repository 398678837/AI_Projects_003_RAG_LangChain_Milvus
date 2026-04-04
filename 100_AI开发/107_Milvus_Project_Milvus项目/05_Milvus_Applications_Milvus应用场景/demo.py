#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milvus应用场景演示
展示Milvus的实际应用场景
"""

import os
import sys
import numpy as np
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility

def demonstrate_milvus_applications():
    """
    演示Milvus的实际应用场景
    """
    print("=== Milvus应用场景演示 ===")
    
    # 1. 连接到Milvus
    print("\n1. 连接到Milvus")
    print("   连接到Milvus服务器...")
    try:
        connections.connect("default", host="localhost", port="19530")
        print("   连接到Milvus服务器成功。")
    except Exception as e:
        print(f"   连接到Milvus服务器失败: {e}")
        print("   请确保Milvus服务器已启动。")
        return
    
    # 2. 创建集合
    print("\n2. 创建集合")
    print("   创建名为'applications'的集合...")
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=3),
        FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=100),
        FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=100)
    ]
    schema = CollectionSchema(fields, "applications collection")
    collection = Collection("applications", schema)
    print("   集合创建成功。")
    
    # 3. 插入向量
    print("\n3. 插入向量")
    print("   插入3个向量...")
    vectors = np.random.rand(3, 3).tolist()
    categories = ["RAG", "推荐系统", "图像检索"]
    names = ["向量库", "个性化推荐", "相似图像检索"]
    mr = collection.insert([vectors, categories, names])
    print("   向量插入成功。")
    
    # 4. 创建索引
    print("\n4. 创建索引")
    print("   创建IVF_FLAT索引...")
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index("vector", index_params)
    print("   索引创建成功。")
    
    # 5. 加载集合
    print("\n5. 加载集合")
    print("   加载集合到内存...")
    collection.load()
    print("   集合加载成功。")
    
    # 6. 检索向量
    print("\n6. 检索向量")
    print("   检索与随机向量最相似的向量...")
    query_vector = np.random.rand(1, 3).tolist()
    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10}
    }
    results = collection.search(query_vector, "vector", search_params, limit=1)
    print(f"   检索结果: {results}")
    
    # 7. 删除集合
    print("\n7. 删除集合")
    print("   删除名为'applications'的集合...")
    utility.drop_collection("applications")
    print("   集合删除成功。")

def main():
    """
    主函数
    """
    print("=== Milvus应用场景演示 ===")
    print("\n本演示展示了Milvus的实际应用场景，帮助您快速掌握Milvus的应用技术。")
    
    # 演示Milvus应用场景
    demonstrate_milvus_applications()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Milvus的应用技术有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的参数和技术。")

if __name__ == "__main__":
    main()
