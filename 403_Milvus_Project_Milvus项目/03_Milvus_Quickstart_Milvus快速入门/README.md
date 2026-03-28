# Milvus快速入门

## 什么是Milvus？

Milvus是一个开源的向量数据库，专门用于存储和检索大规模的向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 快速入门

### 1. 连接到Milvus

```python
from pymilvus import connections

connections.connect("default", host="localhost", port="19530")
```

### 2. 创建集合

```python
from pymilvus import FieldSchema, CollectionSchema, DataType, Collection

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=3)
]
schema = CollectionSchema(fields, "quickstart collection")
collection = Collection("quickstart", schema)
```

### 3. 插入向量

```python
import numpy as np

vectors = np.random.rand(3, 3).tolist()
mr = collection.insert([vectors])
```

### 4. 创建索引

```python
index_params = {
    "metric_type": "L2",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 128}
}
collection.create_index("vector", index_params)
```

### 5. 加载集合

```python
collection.load()
```

### 6. 检索向量

```python
query_vector = np.random.rand(1, 3).tolist()
search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10}
}
results = collection.search(query_vector, "vector", search_params, limit=1)
print(f"检索结果: {results}")
```

### 7. 删除集合

```python
from pymilvus import utility

utility.drop_collection("quickstart")
```

## 总结

Milvus是一个开源的向量数据库，使用简单，易于上手。本目录提供了Milvus的快速入门指南，帮助您快速掌握Milvus的基本使用方法。
