#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档处理演示
展示文档加载和切片的核心功能
"""

import os
import tempfile
from typing import List

# 尝试导入所需库
try:
    from langchain.document_loaders import PyPDFLoader, DocxLoader, TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
    langchain_support = True
except ImportError:
    langchain_support = False
    print("警告: 缺少LangChain库，请安装")

def create_sample_files():
    """
    创建示例文件
    """
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    
    # 创建示例文本文件
    txt_content = "这是一个示例文本文件。\n包含多行内容。\n用于演示文档处理功能。"
    txt_path = os.path.join(temp_dir, "sample.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(txt_content)
    
    print(f"创建示例文件: {txt_path}")
    
    return temp_dir, txt_path

def demonstrate_document_loading():
    """
    演示文档加载
    """
    if not langchain_support:
        print("错误: 缺少LangChain库，无法演示文档加载")
        return
    
    print("=== 文档加载演示 ===")
    
    # 创建示例文件
    temp_dir, txt_path = create_sample_files()
    
    try:
        # 加载文本文件
        print("\n1. 加载文本文件")
        loader = TextLoader(txt_path, encoding="utf-8")
        documents = loader.load()
        print(f"   加载成功，共 {len(documents)} 个文档")
        print(f"   文档内容: {documents[0].page_content[:100]}...")
        
        # 显示文档元数据
        print("\n2. 文档元数据")
        print(f"   元数据: {documents[0].metadata}")
        
    finally:
        # 清理临时文件
        import shutil
        shutil.rmtree(temp_dir)

def demonstrate_document_splitting():
    """
    演示文档切片
    """
    if not langchain_support:
        print("错误: 缺少LangChain库，无法演示文档切片")
        return
    
    print("\n=== 文档切片演示 ===")
    
    # 示例文本
    sample_text = """
    RAG（检索增强生成）是一种结合了检索和生成的AI技术。
    它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，
    以生成更准确、更相关的回答。
    
    RAG的核心价值包括：
    1. 解决知识过时问题
    2. 减少幻觉
    3. 提高回答准确性
    4. 领域知识增强
    
    RAG的工作流程包括：
    1. 文档加载
    2. 文档切片
    3. 向量编码
    4. 向量存储
    5. 语义检索
    6. 增强生成
    """
    
    # 使用RecursiveCharacterTextSplitter
    print("\n1. 使用RecursiveCharacterTextSplitter")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_text(sample_text)
    print(f"   切片完成，共 {len(chunks)} 个文本块")
    
    # 显示前3个切片
    print("\n2. 切片结果")
    for i, chunk in enumerate(chunks[:3]):
        print(f"   切片 {i+1} (长度: {len(chunk)}):")
        print(f"   {chunk}")
        print()
    
    # 使用CharacterTextSplitter
    print("\n3. 使用CharacterTextSplitter")
    char_splitter = CharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=30
    )
    
    char_chunks = char_splitter.split_text(sample_text)
    print(f"   切片完成，共 {len(char_chunks)} 个文本块")
    
    # 显示前2个切片
    print("\n4. 切片结果")
    for i, chunk in enumerate(char_chunks[:2]):
        print(f"   切片 {i+1} (长度: {len(chunk)}):")
        print(f"   {chunk}")
        print()

def main():
    """
    主函数
    """
    print("=== 文档处理演示 ===")
    
    # 演示文档加载
    demonstrate_document_loading()
    
    # 演示文档切片
    demonstrate_document_splitting()
    
    print("=== 演示完成 ===")
    print("\n通过本演示，您应该对文档处理的核心功能有了初步了解。")
    print("在实际应用中，您需要根据文档类型和具体需求选择合适的加载器和切片策略。")

if __name__ == "__main__":
    main()
