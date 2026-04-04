#!/usr/bin/env python3
"""
领域适配示例
演示如何将大模型适配到特定领域
"""

import os
import openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_domain_adapted_chain(domain):
    """
    创建领域适配的LLM链
    
    Args:
        domain (str): 目标领域
    
    Returns:
        LLMChain: 领域适配的LLM链
    """
    # 领域特定的提示模板
    domain_prompts = {
        "医疗": "你是一位专业的医疗顾问，擅长回答关于健康和医疗的问题。请提供专业、准确的医疗建议。",
        "法律": "你是一位专业的法律顾问，擅长回答关于法律问题。请提供专业、准确的法律建议。",
        "金融": "你是一位专业的金融顾问，擅长回答关于金融和投资的问题。请提供专业、准确的金融建议。",
        "教育": "你是一位专业的教育顾问，擅长回答关于教育和学习的问题。请提供专业、准确的教育建议。"
    }
    
    # 获取领域特定的提示
    domain_prompt = domain_prompts.get(domain, "你是一位专业顾问，擅长回答各种问题。")
    
    # 创建提示模板
    template = f"{domain_prompt}\n\n用户问题: {{question}}\n\n回答:"
    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    # 创建LLM链
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return chain

def main():
    """
    主函数
    """
    print("领域适配示例")
    print("=" * 50)
    
    # 选择领域
    domains = ["医疗", "法律", "金融", "教育"]
    
    for domain in domains:
        print(f"\n=== {domain}领域示例 ===")
        
        # 创建领域适配的链
        chain = create_domain_adapted_chain(domain)
        
        # 示例问题
        if domain == "医疗":
            question = "如何预防感冒？"
        elif domain == "法律":
            question = "什么是著作权？"
        elif domain == "金融":
            question = "如何进行投资理财？"
        else:  # 教育
            question = "如何提高学习效率？"
        
        print(f"问题: {question}")
        
        # 执行查询
        try:
            result = chain.run(question)
            print(f"回答: {result}")
        except Exception as e:
            print(f"出错: {e}")

if __name__ == "__main__":
    main()