# 658 大模型与RAG实战项目

## 项目简介

本项目是一个综合性的大模型与RAG实战项目，涵盖了从基础API调用到复杂RAG系统构建的完整学习路径。

## 目录结构

```
658_大模型与RAG实战项目/
├── 01_大模型API调用/                 # 大模型API调用示例
│   ├── 01_OpenAI_API调用示例.py      # OpenAI GPT模型调用
│   ├── 02_百度文心一言API调用示例.py  # 百度文心一言模型调用
│   └── README.md                    # 大模型API调用说明
├── 02_RAG系统_向量数据库_检索增强/   # RAG系统实现
│   ├── 01_RAG基础示例.py           # RAG基础实现
│   ├── 02_Milvus向量数据库示例.py   # Milvus向量数据库实现
│   └── README.md                    # RAG系统说明
├── 03_Agent智能体_多工具协作/        # Agent智能体开发
│   ├── 01_Basic_Agent示例.py         # 基础Agent智能体示例
│   ├── 02_RAG_Agent示例.py           # RAG Agent智能体示例
│   └── README.md                     # Agent智能体说明
├── 04_微调与领域适配/               # 大模型微调与适配
│   ├── 01_模型微调基础.py             # 模型微调基础示例
│   ├── 02_领域适配示例.py             # 领域适配示例
│   └── README.md                     # 微调与领域适配说明
├── 05_评测与优化/                   # 系统评测与优化
│   ├── 01_RAG系统评测.py               # RAG系统评测示例
│   └── README.md                      # 评测与优化说明
└── README.md                        # 本文件
```

## 学习路径

### 入门阶段
1. **大模型API调用** - 掌握各种大模型的API调用方法
2. **RAG基础** - 理解RAG系统的基本原理和实现

### 进阶阶段
3. **向量数据库** - 学习使用Milvus等向量数据库
4. **Agent智能体** - 开发多工具协作的智能体系统

### 高级阶段
5. **模型微调** - 掌握大模型的微调技术
6. **系统优化** - 学习RAG系统的评测和优化方法

## 环境配置

### 基础依赖
```bash
pip install openai python-dotenv requests langchain
```

### 向量数据库依赖
```bash
pip install chromadb pymilvus
```

### Agent智能体依赖
```bash
pip install google-search-results
```

## 推荐资源

### 官方文档
- OpenAI API文档: https://platform.openai.com/docs
- LangChain文档: https://python.langchain.com/docs
- Milvus文档: https://milvus.io/docs

### 学习资料
- RAG技术白皮书
- 大模型微调实战指南
- Agent智能体开发教程

## 贡献指南

欢迎提交PR和Issue，共同完善本实战项目。