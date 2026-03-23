# 向量存储

## 什么是向量存储？

向量存储（Vector Storage）是专门用于存储和检索向量数据的数据库系统。在RAG系统中，向量存储是存储文本Embedding向量的地方，它提供了高效的相似度搜索能力，使系统能够快速找到与用户查询语义相似的文本。

## 常用向量库

### 1. Chroma

**特点**：
- 轻量级，适合开发和测试
- 本地运行，无需部署
- 支持内存模式和持久化存储
- 易于集成到LangChain

**使用示例**：
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 持久化
vector_store.persist()
```

### 2. Qdrant

**特点**：
- 轻量级，支持本地运行
- 高性能，支持快速检索
- 丰富的API和功能
- 支持多种索引类型

**使用示例**：
```python
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

client = QdrantClient(location=":memory:")

# 创建集合
client.create_collection(
    collection_name="rag_collection",
    vector_size=384,
    distance="Cosine"
)

# 插入向量
points = [
    PointStruct(
        id=i,
        vector=embedding,
        payload={"text": text}
    )
    for i, (text, embedding) in enumerate(zip(texts, embeddings))
]

client.upsert(
    collection_name="rag_collection",
    points=points
)
```

### 3. Milvus

**特点**：
- 企业级分布式向量库
- 支持大规模向量数据
- 高性能，支持高并发
- 丰富的企业级特性

**使用示例**：
```python
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

# 连接Milvus
connections.connect("default", host="localhost", port="19530")

# 定义集合schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=512)
]
schema = CollectionSchema(fields, "RAG知识库")

# 创建集合
collection = Collection("rag_collection", schema)
```

### 4. FAISS

**特点**：
- Facebook开发的高效向量搜索库
- 内存型向量库，适合小规模数据
- 支持多种索引类型
- 速度快，适合实时检索

**使用示例**：
```python
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

# 保存到磁盘
vector_store.save_local("./faiss_index")

# 从磁盘加载
vector_store = FAISS.load_local(
    "./faiss_index",
    embeddings
)
```

## 向量库选择指南

| 场景 | 推荐向量库 | 理由 |
|------|------------|------|
| 开发测试 | Chroma, FAISS | 轻量级，易于使用 |
| 小型项目 | Qdrant | 平衡性能和易用性 |
| 企业级应用 | Milvus | 分布式架构，支持大规模数据 |
| 内存受限 | Chroma (持久化模式) | 支持磁盘存储 |
| 高并发场景 | Milvus, Qdrant | 支持高并发访问 |

## 核心操作

### 1. 创建集合

```python
# Chroma
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Qdrant
client.create_collection(
    collection_name="rag_collection",
    vector_size=384,
    distance="Cosine"
)
```

### 2. 插入向量

```python
# Chroma (自动处理)
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

# Qdrant
client.upsert(
    collection_name="rag_collection",
    points=points
)
```

### 3. 检索向量

```python
# Chroma
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

relevant_docs = retriever.get_relevant_documents("什么是RAG？")

# Qdrant
results = client.search(
    collection_name="rag_collection",
    query_vector=query_embedding,
    limit=5,
    with_payload=True
)
```

### 4. 更新向量

```python
# Chroma (通过重新创建)
vector_store = Chroma.from_documents(
    documents=all_chunks,  # 包含新文档
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Qdrant
client.upsert(
    collection_name="rag_collection",
    points=new_points
)
```

### 5. 删除向量

```python
# Chroma (通过重新创建)
# Qdrant
client.delete(
    collection_name="rag_collection",
    points_selector=Filter(
        must=[
            FieldCondition(
                key="id",
                match=MatchValue(value=1)
            )
        ]
    )
)
```

## 最佳实践

1. **选择合适的向量库**：根据项目规模和性能需求选择
2. **索引优化**：根据数据量和查询模式选择合适的索引类型
3. **批量操作**：使用批量插入和批量查询提高性能
4. **缓存机制**：缓存常见查询的结果
5. **监控和维护**：定期检查向量库的性能和健康状态

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 检索速度慢 | 索引未优化或数据量过大 | 优化索引参数或使用更适合的向量库 |
| 内存占用高 | 向量库使用内存模式 | 切换到持久化模式或使用更轻量级的向量库 |
| 部署复杂 | 向量库需要额外服务 | 选择本地运行的向量库如Chroma或Qdrant |
| 扩展性差 | 向量库不支持分布式 | 使用Milvus等分布式向量库 |
