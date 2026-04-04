#!/usr/bin/env python3
"""
RAG Agent智能体示例
演示如何创建一个结合RAG功能的Agent智能体
"""

import os
import openai
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_rag_agent():
    """
    创建RAG Agent智能体
    
    Returns:
        Agent: 初始化后的RAG Agent实例
    """
    # 初始化LLM
    llm = OpenAI(temperature=0)
    
    # 准备文档
    text_files = ["data/document1.txt", "data/document2.txt"]
    documents = []
    
    try:
        for file_path in text_files:
            loader = TextLoader(file_path)
            documents.extend(loader.load())
    except Exception as e:
        print(f"文档加载失败: {e}")
        print("请确保data目录下有相关文档")
    
    # 分割文本并创建向量数据库
    if documents:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        db = Chroma.from_documents(texts, embeddings)
        
        # 创建RAG链
        rag_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
    else:
        # 如果没有文档，创建一个简单的RAG链
        def rag_placeholder(query):
            return f"这是RAG查询结果: {query}"
        
        rag_chain = rag_placeholder
    
    # 定义工具
    def rag_tool(query):
        """RAG工具函数"""
        if callable(rag_chain):
            return rag_chain(query)
        else:
            result = rag_chain({"query": query})
            return result["result"]
    
    # 工具列表
    tools = [
        Tool(
            name="RAG检索",
            func=rag_tool,
            description="用于从文档库中检索信息，回答关于特定领域的问题"
        )
    ]
    
    # 初始化Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    
    return agent

def main():
    """
    主函数
    """
    print("RAG Agent智能体示例")
    print("=" * 50)
    
    try:
        # 创建RAG Agent
        agent = create_rag_agent()
        
        # 示例查询
        query = "解释一下RAG系统的工作原理"
        print(f"\n查询: {query}")
        result = agent.run(query)
        print(f"\n结果: {result}")
        
    except Exception as e:
        print(f"出错: {e}")
        print("请确保已配置正确的API密钥")

if __name__ == "__main__":
    main()