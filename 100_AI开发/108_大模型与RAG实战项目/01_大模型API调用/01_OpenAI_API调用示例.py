#!/usr/bin/env python3
"""
OpenAI API调用示例
演示如何使用OpenAI的GPT模型进行文本生成
"""

import openai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    """
    使用OpenAI的GPT模型进行对话
    
    Args:
        prompt (str): 用户输入的提示词
        model (str): 使用的模型名称
    
    Returns:
        str: GPT模型的回复
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个乐于助人的助手。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"API调用出错: {e}")
        return None

def generate_text(prompt, model="text-davinci-003"):
    """
    使用OpenAI的文本生成模型
    
    Args:
        prompt (str): 用户输入的提示词
        model (str): 使用的模型名称
    
    Returns:
        str: 生成的文本
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"API调用出错: {e}")
        return None

def main():
    """主函数"""
    print("OpenAI API调用示例")
    print("=" * 50)
    
    # 示例1: 对话
    prompt1 = "解释一下什么是RAG（检索增强生成）"
    print(f"用户: {prompt1}")
    response1 = chat_with_gpt(prompt1)
    print(f"GPT: {response1}\n")
    
    # 示例2: 文本生成
    prompt2 = "写一篇关于人工智能未来发展的短文"
    print(f"用户: {prompt2}")
    response2 = generate_text(prompt2)
    print(f"GPT: {response2}\n")

if __name__ == "__main__":
    main()