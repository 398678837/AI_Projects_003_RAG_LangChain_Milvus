# 企业级RAG知识库问答系统

本项目是一个基于LangChain和Chroma向量库的企业级RAG（检索增强生成）知识库问答系统，支持多文档加载、智能切片、向量入库、语义检索和问答对话。

## 目录结构

```
02_Enterprise_RAG_企业级RAG系统/
├── docs/                # 本地知识库文档（PDF/Word/TXT）
├── chroma_db/           # 向量库（自动生成）
├── rag_chat.py          # 主程序
├── config.py            # 配置文件
└── README.md            # 本文件
```

## 功能特性

- **多文档加载**：支持PDF、Word、TXT格式文档
- **智能切片**：自动切分文本块，支持重叠窗口
- **向量入库**：使用本地Chroma向量库存储Embedding
- **语义检索**：基于相似度的语义检索
- **问答对话**：支持单轮问答，可扩展为多轮对话
- **日志/异常处理**：完善的日志记录和异常处理
- **CPU可跑**：使用轻量级Embedding模型，支持CPU运行

## 技术栈

- **LangChain**：构建RAG工作流
- **Chroma**：本地轻量级向量库
- **sentence-transformers**：轻量级Embedding模型
- **pypdf/python-docx**：文档解析

## 安装依赖

```bash
pip install langchain pypdf python-docx sentence-transformers chromadb huggingface-hub
```

## 配置说明

配置文件 `config.py` 包含以下配置项：

- **DOCUMENT_CONFIG**：文档处理配置（块大小、重叠部分等）
- **EMBEDDING_CONFIG**：Embedding配置（模型名称、向量维度等）
- **VECTOR_STORE_CONFIG**：向量库配置（存储目录、集合名称等）
- **LLM_CONFIG**：大模型配置（是否使用本地模型、API配置等）
- **RETRIEVAL_CONFIG**：检索配置（top-k、评分阈值等）
- **LOG_CONFIG**：日志配置（级别、日志文件等）
- **APP_CONFIG**：应用配置（文档目录、对话历史长度等）

## 使用方法

### 1. 准备文档

将需要作为知识库的PDF、Word或TXT文档放入 `docs/` 目录。

### 2. 运行系统

```bash
python rag_chat.py
```

系统会自动：
- 加载 `docs/` 目录中的文档
- 切分文档为文本块
- 生成Embedding向量
- 创建/加载向量库
- 初始化问答链

### 3. 开始对话

系统启动后，会提示您输入问题。您可以：

- 输入问题，系统会基于知识库回答
- 输入"退出"结束对话

## 示例输出

```
=== 企业级RAG知识库问答系统 ===

初始化系统...
2026-03-24 00:07:00,000 - __main__ - INFO - 初始化Embedding模型: paraphrase-multilingual-MiniLM-L12-v2
2026-03-24 00:07:00,000 - __main__ - INFO - 初始化文本分割器: chunk_size=1000, chunk_overlap=200
2026-03-24 00:07:00,000 - __main__ - INFO - 加载向量库成功，存储在: ./chroma_db

系统已就绪，输入问题开始对话（输入'退出'结束）

用户: 什么是RAG？

助手: 根据文档，什么是RAG？的答案是...

参考文档:
RAG（检索增强生成）是一种结合了检索和生成的AI技术，它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，以生成更准确、更相关的回答...

用户: 如何实现RAG系统？

助手: 根据文档，如何实现RAG系统？的答案是...

参考文档:
实现RAG系统的基本步骤包括：1. 文档加载和预处理；2. 文本切分；3. 生成Embedding向量；4. 向量入库；5. 语义检索；6. 生成回答...

用户: 退出
再见！
```

## 自定义配置

您可以修改 `config.py` 文件来自定义系统配置：

- **更改Embedding模型**：修改 `EMBEDDING_CONFIG["model_name"]`
- **调整文本块大小**：修改 `DOCUMENT_CONFIG["chunk_size"]`
- **更改向量库存储位置**：修改 `VECTOR_STORE_CONFIG["persist_directory"]`
- **调整检索参数**：修改 `RETRIEVAL_CONFIG["k"]`

## 注意事项

1. 首次运行时，系统会下载预训练的Embedding模型，可能需要一些时间
2. 处理大文档时，可能会消耗较多内存
3. 本系统使用的是基于相似度的简单回答，实际应用中建议使用真实的大模型
4. 向量库会自动保存在 `chroma_db/` 目录，下次运行时会直接加载

## 扩展建议

1. **集成真实大模型**：替换SimpleQA为真实的大模型，如GPT-3.5、Qwen等
2. **添加多轮对话支持**：使用ConversationalRetrievalChain
3. **优化检索策略**：使用混合检索（BM25+向量检索）
4. **添加用户界面**：构建Web或桌面界面
5. **增加文档更新机制**：支持增量更新向量库
