#!/usr/bin/env python3
"""
百度文心一言API调用示例
演示如何使用百度文心一言模型进行文本生成
"""

import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def chat_with_ernie(prompt, model="ernie-3.5"):
    """
    使用百度文心一言模型进行对话
    
    Args:
        prompt (str): 用户输入的提示词
        model (str): 使用的模型名称
    
    Returns:
        str: 文心一言模型的回复
    """
    try:
        # 配置API参数
        api_key = os.getenv("BAIDU_API_KEY")
        secret_key = os.getenv("BAIDU_SECRET_KEY")
        
        # 获取access_token
        token_url = "https://aip.baidubce.com/oauth/2.0/token"
        token_params = {
            "grant_type": "client_credentials",
            "client_id": api_key,
            "client_secret": secret_key
        }
        token_response = requests.post(token_url, params=token_params)
        access_token = token_response.json().get("access_token")
        
        # 调用对话API
        chat_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions"
        chat_params = {
            "access_token": access_token
        }
        chat_data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        chat_response = requests.post(chat_url, params=chat_params, json=chat_data)
        result = chat_response.json()
        
        if "result" in result:
            return result["result"]
        else:
            print(f"API调用出错: {result}")
            return None
            
    except Exception as e:
        print(f"API调用出错: {e}")
        return None

def main():
    """主函数"""
    print("百度文心一言API调用示例")
    print("=" * 50)
    
    # 示例: 对话
    prompt = "解释一下什么是RAG（检索增强生成）"
    print(f"用户: {prompt}")
    response = chat_with_ernie(prompt)
    print(f"文心一言: {response}\n")

if __name__ == "__main__":
    main()