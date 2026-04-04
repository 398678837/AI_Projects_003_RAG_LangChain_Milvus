# Qdrant高级功能

## 什么是Qdrant？

Qdrant是一个轻量级、高性能的向量数据库，专门用于存储和检索向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 高级功能

### 1. 过滤检索

Qdrant支持过滤检索，可以根据向量的元数据进行过滤。

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue

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
print(f"检索结果: {search_result}")
```

### 2. 批量操作

Qdrant支持批量操作，可以一次性插入、更新或删除多个向量。

```python
points = [
    PointStruct(id=1, vector=[1.0, 2.0, 3.0], payload={"color": "red"}),
    PointStruct(id=2, vector=[4.0, 5.0, 6.0], payload={"color": "green"}),
    PointStruct(id=3, vector=[7.0, 8.0, 9.0], payload={"color": "blue"})
]
client.upsert(collection_name="advanced", points=points)
```

### 3. 索引优化

Qdrant支持索引优化，可以提高检索性能。

```python
client.create_index(
    collection_name="advanced",
    field_name="color",
    index_config={"type": "fulltext"}
)
```

### 4. 多向量检索

Qdrant支持多向量检索，可以一次性检索多个向量。

```python
search_result = client.search_batch(
    collection_name="advanced",
    query_vectors=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
    limit=1
)
print(f"检索结果: {search_result}")
```

## 总结

Qdrant是一个轻量级、高性能的向量数据库，支持多种高级功能，如过滤检索、批量操作、索引优化和多向量检索。本目录提供了Qdrant的高级功能演示，帮助您快速掌握Qdrant的高级使用方法。
