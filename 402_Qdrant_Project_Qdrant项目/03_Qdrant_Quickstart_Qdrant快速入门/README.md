# Qdrant快速入门

## 什么是Qdrant？

Qdrant是一个轻量级、高性能的向量数据库，专门用于存储和检索向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 快速入门

### 1. 创建Qdrant客户端

```python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
```

### 2. 创建集合

```python
from qdrant_client.models import Distance, VectorParams

client.recreate_collection(
    collection_name="quickstart",
    vectors_config=VectorParams(size=3, distance=Distance.COSINE)
)
```

### 3. 插入向量

```python
from qdrant_client.models import PointStruct

points = [
    PointStruct(id=1, vector=[1.0, 2.0, 3.0], payload={"color": "red"}),
    PointStruct(id=2, vector=[4.0, 5.0, 6.0], payload={"color": "green"}),
    PointStruct(id=3, vector=[7.0, 8.0, 9.0], payload={"color": "blue"})
]
client.upsert(collection_name="quickstart", points=points)
```

### 4. 检索向量

```python
search_result = client.search(
    collection_name="quickstart",
    query_vector=[1.0, 2.0, 3.0],
    limit=1
)
print(f"检索结果: {search_result}")
```

### 5. 删除集合

```python
client.delete_collection(collection_name="quickstart")
```

## 总结

Qdrant是一个轻量级、高性能的向量数据库，使用简单，易于上手。本目录提供了Qdrant的快速入门指南，帮助您快速掌握Qdrant的基本使用方法。
