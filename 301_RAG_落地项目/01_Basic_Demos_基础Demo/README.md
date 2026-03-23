# RAG基础Demo

本项目包含两个基础Demo脚本，用于RAG系统的文档处理和Embedding生成。

## 目录结构

```
01_Basic_Demos_基础Demo/
├── document_splitter.py  # 文档切片器
├── embedding_generator.py # Embedding向量生成器
└── README.md            # 本文件
```

## 功能说明

### 1. 文档切片器 (document_splitter.py)
- 支持PDF、Word、TXT文件格式
- 自动切分文本块，可设置块大小和重叠部分
- 支持保存切片结果到指定目录

### 2. Embedding向量生成器 (embedding_generator.py)
- 使用sentence-transformers生成文本的向量表示
- 支持处理单个文本或文本文件
- 输出向量维度和内容
- 支持保存结果到JSON文件

## 安装依赖

```bash
pip install langchain pypdf python-docx sentence-transformers chromadb
```

## 使用方法

### 文档切片器

```bash
# 基本用法
python document_splitter.py example.pdf

# 指定输出目录
python document_splitter.py example.pdf --output-dir chunks

# 自定义块大小和重叠部分
python document_splitter.py example.pdf --chunk-size 1500 --chunk-overlap 300
```

### Embedding向量生成器

```bash
# 处理单个文本
python embedding_generator.py "这是一个测试文本"

# 处理文本文件
python embedding_generator.py example.txt

# 保存结果到文件
python embedding_generator.py example.txt --output embedding_results.json

# 使用指定模型
python embedding_generator.py example.txt --model "all-MiniLM-L6-v2"
```

## 示例输出

### 文档切片器输出

```
保存切片: chunks/example_chunk_1.txt
保存切片: chunks/example_chunk_2.txt
保存切片: chunks/example_chunk_3.txt

文档处理完成，共生成 3 个切片

前3个切片内容:

切片 1:
这是文档的第一部分内容...

切片 2:
这是文档的第二部分内容...

切片 3:
这是文档的第三部分内容...
```

### Embedding向量生成器输出

```
加载模型成功: paraphrase-multilingual-MiniLM-L12-v2

处理完成，共生成 1 个Embedding

前3个结果:

ID: 1
文本: 这是一个测试文本
Embedding维度: 384
Embedding前5个值: [-0.0321, 0.0456, -0.0123, 0.0678, -0.0234]
```

## 注意事项

1. 处理大文件时可能会消耗较多内存
2. Embedding生成需要下载预训练模型，首次运行会较慢
3. 建议在CPU环境下使用轻量级模型，如`paraphrase-multilingual-MiniLM-L12-v2`
