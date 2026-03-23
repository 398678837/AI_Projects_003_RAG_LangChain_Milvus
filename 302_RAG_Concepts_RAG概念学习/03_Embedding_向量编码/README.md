# 向量编码

## 什么是向量编码？

向量编码（Embedding）是将文本转换为数字向量的过程，使计算机能够理解文本的语义。在RAG系统中，向量编码是连接文本和向量数据库的桥梁，它将文本的语义信息转换为可计算的向量表示。

## Embedding模型

### 常用模型

| 模型 | 描述 | 向量维度 | 适用场景 |
|------|------|----------|----------|
| paraphrase-multilingual-MiniLM-L12-v2 | 轻量级多语言模型 | 384 | 多语言场景，CPU可跑 |
| all-MiniLM-L6-v2 | 轻量级英文模型 | 384 | 英文场景，CPU可跑 |
| bge-small-zh | 中文优化模型 | 384 | 中文场景，CPU可跑 |
| text-embedding-ada-002 | OpenAI模型 | 1536 | 高质量场景，需要API |
| m3e-small | 中文通用模型 | 768 | 中文场景，中等性能 |

### 模型选择考虑因素

1. **语言支持**：选择支持目标语言的模型
2. **向量维度**：维度越高，语义表示越丰富，但存储和计算成本也越高
3. **性能**：轻量级模型适合CPU运行，重量级模型需要GPU
4. **精度**：根据应用场景选择合适精度的模型
5. **许可**：考虑模型的许可条款和商业使用限制

## 向量编码的作用

1. **语义表示**：将文本的语义信息转换为向量
2. **相似度计算**：通过向量距离衡量文本语义相似度
3. **检索基础**：向量数据库基于向量相似度进行检索
4. **跨模态对齐**：将不同模态的信息映射到同一向量空间

## 向量编码的计算

### 单文本编码

```python
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

text = "这是一个测试文本"
vector = embeddings.embed_query(text)
print(f"向量维度: {len(vector)}")
print(f"向量前5个值: {vector[:5]}")
```

### 批量编码

```python
texts = ["文本1", "文本2", "文本3"]
vectors = embeddings.embed_documents(texts)
for i, vector in enumerate(vectors):
    print(f"文本{i+1}向量维度: {len(vector)}")
```

## 向量相似度

### 常用相似度度量

1. **余弦相似度**：衡量两个向量的方向一致性
   - 取值范围：[-1, 1]
   - 值越大，相似度越高

2. **欧氏距离**：衡量两个向量的空间距离
   - 取值范围：[0, ∞)
   - 值越小，相似度越高

3. **点积**：衡量两个向量的相似度
   - 取值范围：(-∞, ∞)
   - 值越大，相似度越高

### 相似度计算示例

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    """计算余弦相似度"""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 示例向量
vec1 = embeddings.embed_query("人工智能")
vec2 = embeddings.embed_query("机器学习")
vec3 = embeddings.embed_query("天气")

# 计算相似度
print(f"'人工智能'与'机器学习'的相似度: {cosine_similarity(vec1, vec2):.4f}")
print(f"'人工智能'与'天气'的相似度: {cosine_similarity(vec1, vec3):.4f}")
```

## 最佳实践

1. **模型选择**：
   - 开发测试：使用轻量级模型（如paraphrase-multilingual-MiniLM-L12-v2）
   - 生产环境：根据性能和精度需求选择合适的模型

2. **编码优化**：
   - 批量编码：减少API调用或模型加载次数
   - 缓存机制：缓存常见文本的向量
   - 并行处理：使用多线程或多进程加速编码

3. **向量质量**：
   - 文本清洗：去除噪声和无关内容
   - 标准化：确保文本格式一致
   - 长度控制：避免过长文本影响编码质量

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 编码速度慢 | 模型较大或硬件性能不足 | 使用轻量级模型或GPU加速 |
| 内存占用高 | 批量编码时内存不足 | 减小批量大小或使用流式处理 |
| 语义表示差 | 模型不适合目标语言或领域 | 选择更适合的模型或进行微调 |
| 向量维度过高 | 存储和计算成本高 | 选择低维度模型或使用降维技术 |
