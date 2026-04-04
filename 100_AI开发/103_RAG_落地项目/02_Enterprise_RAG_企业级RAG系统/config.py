#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
"""

# 文档处理配置
DOCUMENT_CONFIG = {
    "chunk_size": 1000,         # 文本块大小
    "chunk_overlap": 200,       # 文本块重叠部分
    "clean_text": True,         # 是否清洗文本
    "supported_formats": [".pdf", ".docx", ".txt"]  # 支持的文件格式
}

# Embedding配置
EMBEDDING_CONFIG = {
    "model_name": "paraphrase-multilingual-MiniLM-L12-v2",  # 使用的预训练模型
    "embedding_dim": 384,                                  # 向量维度
    "batch_size": 32                                        # 批处理大小
}

# 向量库配置
VECTOR_STORE_CONFIG = {
    "persist_directory": "./chroma_db",  # 向量库存储目录
    "collection_name": "rag_collection"   # 集合名称
}

# 大模型配置
LLM_CONFIG = {
    "use_local_model": False,  # 是否使用本地模型
    "local_model_path": "",   # 本地模型路径
    "api_key": "",            # API密钥
    "api_base": "",           # API基础URL
    "model_name": "qwen-turbo"  # 模型名称
}

# 检索配置
RETRIEVAL_CONFIG = {
    "k": 5,                    # 检索top-k个结果
    "score_threshold": 0.5      # 评分阈值
}

# 日志配置
LOG_CONFIG = {
    "level": "INFO",           # 日志级别
    "log_file": "rag_chat.log"  # 日志文件
}

# 应用配置
APP_CONFIG = {
    "docs_dir": "./docs",      # 文档目录
    "max_history": 5,           # 对话历史长度
    "temperature": 0.7,         # 生成温度
    "max_tokens": 1024          # 最大生成 tokens
}
