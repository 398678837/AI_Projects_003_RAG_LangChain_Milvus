# Qdrant向量库入门Demo

本项目是一个基于Qdrant向量数据库的入门Demo，演示了向量库的核心功能：本地服务连接、向量生成、集合创建、向量入库和语义检索。

## 目录结构

```
01_Qdrant/
├── qdrant_demo.py    # 主程序：连接+入库+检索
└── README.md         # 项目说明
```

## 功能特性

- **本地运行**：使用Qdrant的内存模式，无需部署服务器
- **轻量高效**：使用sentence-transformers的轻量级模型，CPU可运行
- **完整流程**：包含向量生成、集合创建、向量入库、语义检索全流程
- **详细注释**：代码中包含详细的注释，便于理解

## 技术栈

- **Qdrant**：轻量级向量数据库
- **sentence-transformers**：文本Embedding模型
- **Python**：核心开发语言

## 安装依赖

```bash
pip install qdrant-client sentence-transformers numpy
```

## 使用方法

### 1. 运行Demo

```bash
python qdrant_demo.py
```

### 2. 预期输出

```
=== Qdrant向量库Demo ===
Qdrant客户端初始化成功（本地内存模式）
Embedding模型初始化成功
集合创建成功: rag_collection

插入示例文本向量...
成功插入 5 个向量

集合信息:
集合信息: CollectionDescription(name='rag_collection', vectors_config={'size': 384, 'distance': 'Cosine'}, sparse_vectors_config={}, hnsw_config=None, optimizers_config=None, quantization_config=None, sharding_config=None, replication_factor=None, write_consistency_factor=None, on_disk_payload=None)

=== 示例查询 ===

查询: 什么是RAG？
检索结果:
1. 相似度: 0.7892
   文本: RAG（检索增强生成）是一种结合了检索和生成的AI技术
2. 相似度: 0.3456
   文本: 向量数据库是专门存储和检索向量的数据库
3. 相似度: 0.2345
   文本: Embedding是将文本转换为数字向量的过程

查询: Qdrant是什么？
检索结果:
1. 相似度: 0.8921
   文本: Qdrant是一个轻量级的向量数据库，支持语义检索
2. 相似度: 0.4567
   文本: 向量数据库是专门存储和检索向量的数据库
3. 相似度: 0.3456
   文本: Embedding是将文本转换为数字向量的过程

查询: 如何衡量向量相似度？
检索结果:
1. 相似度: 0.8765
   文本: 余弦相似度是衡量两个向量相似程度的指标
2. 相似度: 0.5432
   文本: Embedding是将文本转换为数字向量的过程
3. 相似度: 0.3210
   文本: 向量数据库是专门存储和检索向量的数据库

=== Demo完成 ===
```

## 核心概念

1. **向量 (Vector)**：文字转成的数字数组（Embedding结果）
2. **集合 (Collection)**：相当于普通数据库的「表」
3. **入库**：把切片后的文档向量存进库
4. **检索**：输入问题向量，找出语义最相似的文本
5. **相似度**：用余弦相似度判断文本语义远近

## 扩展建议

1. **使用持久化存储**：将Qdrant配置为使用磁盘存储，而非内存模式
2. **增加文档处理**：结合之前的文档切片器，处理实际文档
3. **集成到RAG系统**：将本Demo集成到之前的RAG系统中
4. **优化检索参数**：调整检索的limit、score_threshold等参数
5. **添加用户界面**：构建简单的Web界面，方便用户交互

## 注意事项

1. 首次运行时，系统会下载预训练的Embedding模型，可能需要一些时间
2. 本Demo使用Qdrant的内存模式，数据不会持久化，重启后需要重新插入数据
3. 处理大量文本时，建议使用批量插入以提高性能
4. 实际应用中，建议使用Qdrant的持久化存储模式

## 许可证

本项目采用MIT许可证，可自由使用和修改。
