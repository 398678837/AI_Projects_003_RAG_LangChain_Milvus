#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milvus高级功能演示
展示Milvus的高级功能
"""

import os
import sys
import numpy as np
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility, Partition

def demonstrate_milvus_advanced():
    """
    演示Milvus的高级功能
    """
    print("=== Milvus高级功能演示 ===")
    
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
    print("   创建名为'advanced'的集合...")
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=3),
        FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=100)
    ]
    schema = CollectionSchema(fields, "advanced collection")
    collection = Collection("advanced", schema)
    print("   集合创建成功。")
    
    # 3. 创建分区
    print("\n3. 创建分区")
    print("   创建名为'partition1'的分区...")
    partition = Partition(collection, "partition1")
    print("   分区创建成功。")
    
    # 4. 插入向量
    print("\n4. 插入向量")
    print("   插入6个向量...")
    vectors = np.random.rand(6, 3).tolist()
    categories = ["category1", "category1", "category1", "category2", "category2", "category2"]
    mr = collection.insert([vectors, categories])
    print("   向量插入成功。")
    
    # 5. 创建索引
    print("\n5. 创建索引")
    print("   创建IVF_FLAT索引...")
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index("vector", index_params)
    print("   索引创建成功。")
    
    # 6. 加载集合
    print("\n6. 加载集合")
    print("   加载集合到内存...")
    collection.load()
    print("   集合加载成功。")
    
    # 7. 过滤检索
    print("\n7. 过滤检索")
    print("   检索category为'category1'的向量...")
    query_vector = np.random.rand(1, 3).tolist()
    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10}
    }
    expr = "category == 'category1'"
    results = collection.search(query_vector, "vector", search_params, limit=1, expr=expr)
    print(f"   检索结果: {results}")
    
    # 8. 删除集合
    print("\n8. 删除集合")
    print("   删除名为'advanced'的集合...")
    utility.drop_collection("advanced")
    print("   集合删除成功。")

def main():
    """
    主函数
    """
    print("=== Milvus高级功能演示 ===")
    print("\n本演示展示了Milvus的高级功能，帮助您快速掌握Milvus的高级使用方法。")
    
    # 演示Milvus高级功能
    demonstrate_milvus_advanced()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Milvus的高级使用方法有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的参数和技术。")

if __name__ == "__main__":
    main()
