#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG基础概念演示
展示RAG的基本工作流程和核心组件
"""

import time

def demonstrate_rag_workflow():
    """
    演示RAG的工作流程
    """
    print("=== RAG工作流程演示 ===")
    print("\n1. 文档加载阶段")
    print("   - 加载PDF、Word、TXT等格式的文档")
    print("   - 提取文本内容")
    time.sleep(1)
    
    print("\n2. 文档切片阶段")
    print("   - 将长文档切分为较小的文本块")
    print("   - 设置块大小和重叠部分")
    time.sleep(1)
    
    print("\n3. 向量编码阶段")
    print("   - 使用Embedding模型将文本转换为向量")
    print("   - 生成语义表示")
    time.sleep(1)
    
    print("\n4. 向量存储阶段")
    print("   - 将向量存储到向量数据库中")
    print("   - 建立索引以加速检索")
    time.sleep(1)
    
    print("\n5. 语义检索阶段")
    print("   - 接收用户查询")
    print("   - 将查询转换为向量")
    print("   - 在向量库中检索相关文本块")
    time.sleep(1)
    
    print("\n6. 增强生成阶段")
    print("   - 将检索到的文本块与查询一起输入到语言模型")
    print("   - 生成基于文档的回答")
    time.sleep(1)
    
    print("\n7. 生成回答阶段")
    print("   - 向用户返回准确的回答")
    print("   - 可能包含引用的文档来源")
    time.sleep(1)
    
    print("\n=== RAG工作流程演示完成 ===")

def compare_rag_with_llm():
    """
    比较RAG与传统LLM
    """
    print("\n=== RAG与传统LLM的区别 ===")
    print("\n| 特性 | 传统LLM | RAG |")
    print("|------|---------|-----|")
    print("| 知识来源 | 训练数据 | 外部文档 + 训练数据 |")
    print("| 知识时效性 | 截止训练时间 | 实时更新的文档 |")
    print("| 回答准确性 | 可能产生幻觉 | 基于文档，更准确 |")
    print("| 领域适应性 | 需要微调 | 直接使用领域文档 |")
    print("| 可解释性 | 低 | 高（可引用来源） |")

def main():
    """
    主函数
    """
    print("=== RAG基础概念演示 ===")
    print("\nRAG（Retrieval-Augmented Generation）是一种结合了检索和生成的AI技术。")
    print("它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，")
    print("以生成更准确、更相关的回答。")
    
    # 演示RAG工作流程
    demonstrate_rag_workflow()
    
    # 比较RAG与传统LLM
    compare_rag_with_llm()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对RAG的基本概念和工作流程有了初步了解。")
    print("在后续的章节中，我们将详细介绍RAG的各个组件和实现方法。")

if __name__ == "__main__":
    main()
