#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强生成演示
展示基于检索结果的增强生成功能
"""

import os
import shutil

# 尝试导入所需库
try:
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.schema import Document
    from langchain.prompts import PromptTemplate
    from langchain.chains import RetrievalQA
    augmented_generation_support = True
except ImportError:
    augmented_generation_support = False
    print("警告: 缺少必要的库，请安装langchain和sentence-transformers")

class SimpleLLM:
    """
    简单的模拟语言模型
    """
    def __init__(self):
        self.name = "SimpleLLM"
    
    def __call__(self, prompt, **kwargs):
        """
        模拟语言模型生成
        """
        # 简单的基于规则的回答
        if "什么是RAG" in prompt:
            return "RAG（检索增强生成）是一种结合了检索和生成的AI技术，通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中，以生成更准确、更相关的回答。"
        elif "RAG的工作流程" in prompt:
            return "RAG的工作流程包括：文档加载、文档切片、向量编码、向量存储、语义检索、增强生成。"
        elif "向量数据库" in prompt:
            return "向量数据库是专门存储和检索向量数据的数据库系统，常用的向量数据库包括Chroma、Qdrant、Milvus、FAISS等。"
        else:
            return "根据提供的文档，我无法回答这个问题。"

def create_sample_documents():
    """
    创建示例文档
    """
    # 创建示例文本
    sample_texts = [
        "RAG（检索增强生成）是一种结合了检索和生成的AI技术。",
        "它通过从外部知识库中检索相关信息，然后将这些信息与用户查询一起输入到语言模型中。",
        "RAG的核心价值包括：解决知识过时问题、减少幻觉、提高回答准确性、领域知识增强。",
        "RAG的工作流程包括：文档加载、文档切片、向量编码、向量存储、语义检索、增强生成。",
        "向量数据库是专门存储和检索向量数据的数据库系统。",
        "常用的向量数据库包括Chroma、Qdrant、Milvus、FAISS等。",
        "Chroma是一个轻量级的向量数据库，适合开发和测试。",
        "Qdrant是一个轻量级的向量数据库，支持本地运行和高性能检索。",
        "Milvus是一个企业级的分布式向量数据库，支持大规模向量数据。",
        "FAISS是Facebook开发的高效向量搜索库，适合实时检索。"
    ]
    
    # 转换为LangChain文档格式
    documents = [
        Document(page_content=text, metadata={"id": i})
        for i, text in enumerate(sample_texts)
    ]
    
    return documents

def demonstrate_augmented_generation():
    """
    演示增强生成
    """
    if not augmented_generation_support:
        print("错误: 缺少必要的库，无法演示增强生成")
        return
    
    print("=== 增强生成演示 ===")
    
    # 清理之前的向量库
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    # 初始化Embedding模型
    print("\n1. 初始化Embedding模型")
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        print("   模型初始化成功")
        
    except Exception as e:
        print(f"   模型初始化失败: {e}")
        return
    
    # 创建示例文档
    print("\n2. 创建示例文档")
    documents = create_sample_documents()
    print(f"   创建了 {len(documents)} 个示例文档")
    
    # 创建向量库
    print("\n3. 创建向量库")
    try:
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        print("   向量库创建成功")
        print(f"   向量库中共有 {vector_store._collection.count()} 个向量")
        
    except Exception as e:
        print(f"   向量库创建失败: {e}")
        return
    
    # 创建检索器
    print("\n4. 创建检索器")
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
    print("   检索器创建成功")
    
    # 创建提示模板
    print("\n5. 创建提示模板")
    prompt_template = """
    你是一个基于文档的问答助手，请根据以下文档内容回答用户问题。
    如果你不知道答案，直接说"根据提供的文档，我无法回答这个问题"，不要尝试编造答案。
    
    文档内容:
    {context}
    
    问题:
    {question}
    
    回答:
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    print("   提示模板创建成功")
    
    # 创建简单的语言模型
    print("\n6. 创建语言模型")
    llm = SimpleLLM()
    print(f"   语言模型创建成功: {llm.name}")
    
    # 创建问答链
    print("\n7. 创建问答链")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )
    print("   问答链创建成功")
    
    # 测试问答链
    print("\n8. 测试问答链")
    questions = [
        "什么是RAG？",
        "RAG的工作流程是什么？",
        "常用的向量数据库有哪些？",
        "什么是深度学习？"
    ]
    
    for question in questions:
        print(f"\n   问题: {question}")
        result = qa_chain.run(question)
        print(f"   回答: {result}")
    
    # 展示检索结果
    print("\n9. 展示检索结果")
    question = "什么是RAG？"
    print(f"   问题: {question}")
    
    # 手动检索相关文档
    relevant_docs = retriever.get_relevant_documents(question)
    print("   检索到的相关文档:")
    for i, doc in enumerate(relevant_docs):
        print(f"   {i+1}. {doc.page_content}")
    
    # 构建上下文
    context = "\n".join([doc.page_content for doc in relevant_docs])
    print("\n   构建的上下文:")
    print(f"   {context}")

def main():
    """
    主函数
    """
    print("=== 增强生成演示 ===")
    print("\n增强生成是RAG流程的最后一步，它将检索到的相关文本块与用户查询一起输入到语言模型中，")
    print("生成基于文档的回答。增强生成的目标是利用检索到的信息，使语言模型生成更准确、更相关的回答，")
    print("同时避免幻觉。")
    
    # 演示增强生成
    demonstrate_augmented_generation()
    
    # 清理临时文件
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对增强生成的核心功能有了初步了解。")
    print("在实际应用中，您需要选择合适的语言模型和链类型，以获得最佳的生成效果。")

if __name__ == "__main__":
    main()
