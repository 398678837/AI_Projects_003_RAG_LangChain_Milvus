#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qdrant向量库入门Demo
功能：本地Qdrant服务连接、向量生成、集合创建、向量入库、语义检索
"""

import time
from typing import List, Dict, Optional

# 尝试导入所需库
try:
    from qdrant_client import QdrantClient
    from qdrant_client.http.models import PointStruct, CollectionDescription
    from sentence_transformers import SentenceTransformer
    import numpy as np
    qdrant_support = True
except ImportError:
    qdrant_support = False
    print("警告: 缺少Qdrant或sentence-transformers库，请安装")

class QdrantDemo:
    """Qdrant向量库Demo"""
    
    def __init__(self, collection_name: str = "rag_collection"):
        """
        初始化QdrantDemo
        
        Args:
            collection_name: 集合名称
        """
        self.collection_name = collection_name
        self.client = None
        self.embedding_model = None
        self._init_components()
    
    def _init_components(self):
        """初始化组件"""
        try:
            # 初始化Qdrant客户端（本地内存模式）
            self.client = QdrantClient(location=":memory:")
            print("Qdrant客户端初始化成功（本地内存模式）")
            
            # 初始化Embedding模型
            self.embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
            print("Embedding模型初始化成功")
            
        except Exception as e:
            print(f"初始化组件失败: {e}")
    
    def create_collection(self, vector_size: int = 384):
        """
        创建集合
        
        Args:
            vector_size: 向量维度
        """
        try:
            # 检查集合是否存在
            collections = self.client.get_collections().collections
            collection_names = [col.name for col in collections]
            
            if self.collection_name in collection_names:
                # 删除已存在的集合
                self.client.delete_collection(collection_name=self.collection_name)
                print(f"已删除现有集合: {self.collection_name}")
            
            # 创建新集合
            self.client.create_collection(
                collection_name=self.collection_name,
                vector_size=vector_size,
                distance="Cosine"
            )
            print(f"集合创建成功: {self.collection_name}")
            return True
        except Exception as e:
            print(f"创建集合失败: {e}")
            return False
    
    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        生成文本的Embedding向量
        
        Args:
            text: 待编码的文本
            
        Returns:
            文本的Embedding向量
        """
        if not self.embedding_model:
            print("错误: Embedding模型未初始化")
            return None
        
        try:
            embedding = self.embedding_model.encode(text).tolist()
            return embedding
        except Exception as e:
            print(f"生成Embedding失败: {e}")
            return None
    
    def insert_vectors(self, texts: List[str]):
        """
        批量插入向量
        
        Args:
            texts: 文本列表
        """
        try:
            # 生成向量
            points = []
            for i, text in enumerate(texts):
                embedding = self.generate_embedding(text)
                if embedding:
                    point = PointStruct(
                        id=i,
                        vector=embedding,
                        payload={"text": text}
                    )
                    points.append(point)
            
            # 批量插入
            if points:
                self.client.upsert(
                    collection_name=self.collection_name,
                    points=points
                )
                print(f"成功插入 {len(points)} 个向量")
                return True
            else:
                print("没有生成有效的向量")
                return False
        except Exception as e:
            print(f"插入向量失败: {e}")
            return False
    
    def search(self, query: str, limit: int = 3) -> List[Dict]:
        """
        语义检索
        
        Args:
            query: 查询文本
            limit: 返回结果数量
            
        Returns:
            检索结果列表
        """
        try:
            # 生成查询向量
            query_vector = self.generate_embedding(query)
            if not query_vector:
                return []
            
            # 执行检索
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=limit,
                with_payload=True
            )
            
            # 处理结果
            search_results = []
            for result in results:
                search_results.append({
                    "id": result.id,
                    "score": result.score,
                    "text": result.payload.get("text", "")
                })
            
            return search_results
        except Exception as e:
            print(f"检索失败: {e}")
            return []
    
    def get_collection_info(self):
        """
        获取集合信息
        """
        try:
            collection_info = self.client.get_collection(collection_name=self.collection_name)
            print(f"集合信息: {collection_info}")
            return collection_info
        except Exception as e:
            print(f"获取集合信息失败: {e}")
            return None

def main():
    """主函数"""
    print("=== Qdrant向量库Demo ===")
    
    # 创建QdrantDemo实例
    demo = QdrantDemo()
    
    # 创建集合
    demo.create_collection()
    
    # 示例文本
    sample_texts = [
        "RAG（检索增强生成）是一种结合了检索和生成的AI技术",
        "Qdrant是一个轻量级的向量数据库，支持语义检索",
        "Embedding是将文本转换为数字向量的过程",
        "余弦相似度是衡量两个向量相似程度的指标",
        "向量数据库是专门存储和检索向量的数据库"
    ]
    
    # 插入向量
    print("\n插入示例文本向量...")
    demo.insert_vectors(sample_texts)
    
    # 获取集合信息
    print("\n集合信息:")
    demo.get_collection_info()
    
    # 示例查询
    print("\n=== 示例查询 ===")
    queries = [
        "什么是RAG？",
        "Qdrant是什么？",
        "如何衡量向量相似度？"
    ]
    
    for query in queries:
        print(f"\n查询: {query}")
        results = demo.search(query)
        
        print("检索结果:")
        for i, result in enumerate(results):
            print(f"{i+1}. 相似度: {result['score']:.4f}")
            print(f"   文本: {result['text']}")
    
    print("\n=== Demo完成 ===")

if __name__ == "__main__":
    main()
