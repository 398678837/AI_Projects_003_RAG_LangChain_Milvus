# 文档处理

## 什么是文档处理？

文档处理是RAG流程的第一步，主要包括**文档加载**和**文档切片**两个核心步骤。它的目标是将各种格式的文档转换为适合向量编码和检索的文本块。

## 文档加载

### 支持的文档格式

| 格式 | 描述 | 工具 |
|------|------|------|
| PDF | 便携式文档格式 | PyPDFLoader |
| Word | Microsoft Word文档 | DocxLoader |
| TXT | 纯文本文件 | TextLoader |
| Markdown | 标记语言 | UnstructuredMarkdownLoader |
| HTML | 网页格式 | UnstructuredHTMLLoader |
| 图片 | 包含文本的图片 | UnstructuredImageLoader |

### 常用加载器

1. **PyPDFLoader**：加载PDF文档
   ```python
   from langchain.document_loaders import PyPDFLoader
   loader = PyPDFLoader("example.pdf")
   documents = loader.load()
   ```

2. **DocxLoader**：加载Word文档
   ```python
   from langchain.document_loaders import DocxLoader
   loader = DocxLoader("example.docx")
   documents = loader.load()
   ```

3. **TextLoader**：加载文本文件
   ```python
   from langchain.document_loaders import TextLoader
   loader = TextLoader("example.txt", encoding='utf-8')
   documents = loader.load()
   ```

4. **DirectoryLoader**：批量加载目录中的文档
   ```python
   from langchain.document_loaders import DirectoryLoader
   loader = DirectoryLoader("./docs", glob="*.pdf")
   documents = loader.load()
   ```

## 文档切片

### 为什么需要切片？

1. **限制输入长度**：语言模型有上下文窗口限制
2. **提高检索精度**： smaller chunks are more likely to be relevant to a query
3. **减少噪声**：避免无关内容影响回答质量

### 常用切片器

1. **RecursiveCharacterTextSplitter**：递归字符分割
   - 按照指定的分隔符递归分割文本
   - 适合大多数文本类型

2. **SentenceTransformersTokenTextSplitter**：基于Token的分割
   - 使用与Embedding模型相同的Tokenization
   - 确保分割点在语义上合理

3. **CharacterTextSplitter**：基于字符的分割
   - 简单直接，按字符数分割
   - 适合结构简单的文本

### 核心参数

- **chunk_size**：每个文本块的大小（字符数或Token数）
- **chunk_overlap**：文本块之间的重叠部分
- **separator**：分割符（如换行符、句号等）

### 切片策略

1. **固定大小**：每个块大小相同
2. **语义分割**：基于句子或段落分割
3. **混合策略**：结合固定大小和语义分割

## 最佳实践

1. **根据文档类型选择切片器**：
   - 结构化文档：使用RecursiveCharacterTextSplitter
   - 非结构化文档：使用SentenceTransformersTokenTextSplitter

2. **调整切片参数**：
   - 长文档：chunk_size = 1000-2000, chunk_overlap = 200-300
   - 短文档：chunk_size = 500-1000, chunk_overlap = 100-200

3. **添加元数据**：
   - 为每个文本块添加文档来源、页码等元数据
   - 便于后续检索和引用

4. **文本清洗**：
   - 去除多余的空白字符
   - 处理特殊字符和格式
   - 移除无关内容

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 切片过大 | chunk_size设置不当 | 减小chunk_size |
| 切片过小 | chunk_size设置不当 | 增大chunk_size |
| 上下文断裂 | 缺少重叠部分 | 增加chunk_overlap |
| 语义不完整 | 分割点选择不当 | 使用语义分割器 |
| 加载失败 | 格式不支持 | 尝试其他加载器或转换格式 |
