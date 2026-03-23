# 语义检索

## 什么是语义检索？

语义检索（Semantic Retrieval）是根据用户查询的语义含义，在向量库中检索最相关的文本块的过程。与传统的关键词检索不同，语义检索能够理解文本的深层含义，即使查询和文档使用不同的词汇，也能找到语义相关的内容。

## 语义检索的原理

1. **查询编码**：将用户查询转换为向量
2. **相似度计算**：计算查询向量与向量库中所有向量的相似度
3. **排序**：按相似度对结果进行排序
4. **返回结果**：返回相似度最高的文本块

## 常用检索方法

### 1. 相似度搜索

```python
# 使用Chroma进行相似度搜索
results = vector_store.similarity_search(
    query="什么是RAG？",
    k=5
)

# 使用Qdrant进行相似度搜索
results = client.search(
    collection_name="rag_collection",
    query_vector=query_embedding,
    limit=5,
    with_payload=True
)
```

### 2. 带分数的相似度搜索

```python
# 使用Chroma进行带分数的相似度搜索
results = vector_store.similarity_search_with_score(
    query="什么是RAG？",
    k=5
)

for doc, score in results:
    print(f"相似度: {score:.4f}, 内容: {doc.page_content}")
```

### 3. MMR搜索

MMR（Maximal Marginal Relevance）是一种平衡相关性和多样性的检索方法，它不仅考虑文档与查询的相关性，还考虑文档之间的多样性。

```python
# 使用Chroma进行MMR搜索
results = vector_store.max_marginal_relevance_search(
    query="什么是RAG？",
    k=5,
    fetch_k=20,
    lambda_mult=0.5
)
```

### 4. 带过滤器的搜索

```python
# 使用Chroma进行带过滤器的搜索
results = vector_store.similarity_search(
    query="什么是RAG？",
    k=5,
    filter={"source": "document1.pdf"}
)
```

## 检索参数优化

### 1. k值

**k值**：返回的相关文本块数量

- **较小的k值**：返回最相关的结果，但可能缺少一些相关信息
- **较大的k值**：返回更多结果，增加信息覆盖率，但可能引入噪声

**推荐值**：3-5（根据具体应用调整）

### 2. 相似度阈值

**相似度阈值**：过滤掉相似度低于阈值的结果

- **较高的阈值**：只返回高度相关的结果
- **较低的阈值**：返回更多结果，增加信息覆盖率

**推荐值**：0.5-0.7（根据具体应用调整）

### 3. MMR参数

- **fetch_k**：初始检索的文档数量
- **lambda_mult**：相关性和多样性的权重（0-1）
  - 接近1：更注重相关性
  - 接近0：更注重多样性

**推荐值**：fetch_k=20, lambda_mult=0.5

## 检索器（Retriever）

检索器是LangChain中用于检索相关文档的组件，它封装了向量库的检索功能，提供了统一的接口。

### 创建检索器

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# 创建检索器
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

# 使用检索器
relevant_docs = retriever.get_relevant_documents("什么是RAG？")
```

### 自定义检索器

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.llms import OpenAI

# 创建基础检索器
base_retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}
)

# 创建压缩器
compressor = LLMChainExtractor.from_llm(OpenAI())

# 创建压缩检索器
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# 使用压缩检索器
compressed_docs = compression_retriever.get_relevant_documents("什么是RAG？")
```

## 混合检索

混合检索是结合关键词检索和向量检索的方法，能够提高检索的准确性和召回率。

### BM25 + 向量检索

```python
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# 创建BM25检索器
bm25_retriever = BM25Retriever.from_documents(documents)

# 创建向量检索器
vector_retriever = vector_store.as_retriever()

# 创建集成检索器
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]
)

# 使用集成检索器
results = ensemble_retriever.get_relevant_documents("什么是RAG？")
```

## 最佳实践

1. **选择合适的检索方法**：
   - 简单场景：使用相似度搜索
   - 需要多样性：使用MMR搜索
   - 需要过滤：使用带过滤器的搜索

2. **优化检索参数**：
   - 根据应用场景调整k值
   - 设置合适的相似度阈值
   - 调整MMR参数以平衡相关性和多样性

3. **使用混合检索**：
   - 结合关键词检索和向量检索
   - 提高检索的准确性和召回率

4. **缓存机制**：
   - 缓存常见查询的结果
   - 减少重复检索的开销

5. **监控和评估**：
   - 监控检索性能
   - 评估检索结果的质量

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 检索结果不相关 | 向量编码质量差或检索参数不当 | 选择更好的Embedding模型或调整检索参数 |
| 检索速度慢 | 向量库未优化或数据量过大 | 优化向量库索引或使用更适合的向量库 |
| 结果缺少多样性 | 检索方法过于注重相关性 | 使用MMR搜索或调整lambda_mult参数 |
| 召回率低 | k值过小或相似度阈值过高 | 增加k值或降低相似度阈值 |
