# Milvus应用场景

## 什么是Milvus？

Milvus是一个开源的向量数据库，专门用于存储和检索大规模的向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 应用场景

### 1. RAG系统

Milvus可以用于RAG系统，存储知识库的向量表示，实现语义相似检索。

```python
# 插入知识库向量
vectors = np.random.rand(2, 3).tolist()
contents = ["向量库是一种专门用于存储和检索向量数据的数据库。", "向量库的主要作用是实现语义相似检索。"]
mr = collection.insert([vectors, contents])

# 检索相似文档
query_vector = np.random.rand(1, 3).tolist()
results = collection.search(query_vector, "vector", search_params, limit=1)
print(f"检索结果: {results}")
```

### 2. 推荐系统

Milvus可以用于推荐系统，存储用户和物品的向量表示，实现个性化推荐。

```python
# 插入物品向量
vectors = np.random.rand(2, 3).tolist()
names = ["向量库入门教程", "推荐系统实战"]
mr = collection.insert([vectors, names])

# 检索相似物品
query_vector = np.random.rand(1, 3).tolist()
results = collection.search(query_vector, "vector", search_params, limit=1)
print(f"检索结果: {results}")
```

### 3. 图像检索

Milvus可以用于图像检索，存储图像的向量表示，实现相似图像检索。

```python
# 插入图像向量
vectors = np.random.rand(2, 3).tolist()
names = ["图像1", "图像2"]
mr = collection.insert([vectors, names])

# 检索相似图像
query_vector = np.random.rand(1, 3).tolist()
results = collection.search(query_vector, "vector", search_params, limit=1)
print(f"检索结果: {results}")
```

## 总结

Milvus是一个开源的向量数据库，广泛应用于RAG系统、推荐系统、图像检索等领域。本目录提供了Milvus的应用场景演示，帮助您快速掌握Milvus的应用技术。
