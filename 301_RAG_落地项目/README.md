# 301_RAG_落地项目

## 项目简介

本项目是一个严格按照5天落地计划实现的RAG（检索增强生成）全流程系统，旨在帮助AI开发岗位求职者快速掌握RAG技术栈，完成从基础概念到企业级应用的全流程落地。

## 技术栈

- **LangChain**：构建RAG工作流
- **PDF/Word切片**：支持多格式文档处理
- **Embedding**：使用sentence-transformers轻量级模型
- **Chroma向量库**：本地轻量向量库，无需部署
- **模型**：开源轻量Embedding + 本地Qwen/通义API（二选一）

## 目录结构

```
301_RAG_落地项目/
├── 01_Basic_Demos_基础Demo/            # 基础Demo
│   ├── document_splitter.py            # 文档切片脚本
│   ├── embedding_generator.py         # Embedding向量生成脚本
│   └── README.md                      # 项目说明
├── 02_Enterprise_RAG_企业级RAG系统/     # 企业级RAG系统
│   ├── docs/                          # 本地知识库文档
│   ├── chroma_db/                     # 向量库（自动生成）
│   ├── rag_chat.py                    # 主程序
│   ├── config.py                      # 配置文件
│   └── README.md                      # 项目说明
├── requirements.txt                   # 统一依赖文件
└── README.md                          # 本文件
```

## 5天落地执行计划

### Day 1：RAG核心逻辑学习
- **学习5个核心概念**：RAG、文档切片、Embedding、向量数据库、检索+生成
- **RAG全流程口诀**：文档加载 → 切片分块 → 向量编码 → 库内存储 → 语义检索 → 增强回答

### Day 2：基础Demo开发
- **完成2个可独立运行的脚本**：
  1. PDF/Word 文档切片脚本
  2. 文本 Embedding 向量生成脚本
- **同步GitHub**：创建 `rag-basic-demo` 仓库

### Day 3：项目搭建 + 文档处理
- **创建项目结构**：搭建企业级RAG系统目录结构
- **实现**：文档加载 → 智能切片 → 清洗文本
- **测试切片效果**：验证文档处理功能

### Day 4：向量库 + 检索 + 问答链
- **接入Embedding模型**：使用sentence-transformers
- **本地Chroma向量库**：创建/存储/检索
- **搭建LangChain RAG问答链**：实现检索增强问答
- **实现单轮问答**：验证核心功能

### Day 5：优化 + 测试 + GitHub + 简历
- **优化**：多轮对话、结果过滤、格式美化
- **完整测试**：上传本地文档→提问验证
- **写README**：运行步骤+功能+截图
- **上传GitHub**：创建 `enterprise-rag-system` 仓库
- **更新简历**：添加RAG全流程开发技能

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基础Demo使用

```bash
# 文档切片器
python 01_Basic_Demos_基础Demo/document_splitter.py example.pdf

# Embedding向量生成器
python 01_Basic_Demos_基础Demo/embedding_generator.py "这是一个测试文本"
```

### 企业级RAG系统使用

1. 将文档放入 `02_Enterprise_RAG_企业级RAG系统/docs/` 目录
2. 运行系统：
   ```bash
   cd 02_Enterprise_RAG_企业级RAG系统
   python rag_chat.py
   ```
3. 输入问题开始对话

## 核心功能

### 1. 文档处理
- 支持PDF、Word、TXT格式
- 智能文本切分，支持重叠窗口
- 文本清洗和预处理

### 2. 向量生成与存储
- 使用轻量级Embedding模型
- 本地Chroma向量库存储
- 向量库持久化

### 3. 语义检索
- 基于相似度的语义检索
- 可配置的top-k参数
- 评分阈值过滤

### 4. 问答对话
- 基于文档的精准回答
- 避免大模型幻觉
- 支持对话历史

### 5. 工程化特性
- 完善的日志记录
- 异常处理
- 配置化管理
- CPU可运行

## 简历更新话术

> 掌握RAG全流程开发，基于LangChain+向量数据库独立完成企业级知识库问答系统，实现文档切片、Embedding编码、语义检索与增强生成，可有效解决大模型幻觉问题，支撑企业知识问答落地。

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

## 许可证

本项目采用MIT许可证，可自由使用和修改。
