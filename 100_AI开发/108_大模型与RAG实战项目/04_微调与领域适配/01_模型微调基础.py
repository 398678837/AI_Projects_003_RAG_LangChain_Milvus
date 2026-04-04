#!/usr/bin/env python3
"""
模型微调基础示例
演示如何对大模型进行基础微调
"""

import os
import openai
from dotenv import load_dotenv
import json

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def prepare_fine_tuning_data():
    """
    准备微调数据
    
    Returns:
        str: 训练数据文件路径
    """
    # 示例训练数据
    training_data = [
        {
            "prompt": "如何使用Python进行文件操作?",
            "completion": "在Python中，你可以使用内置的open()函数来进行文件操作。例如，要读取文件，可以使用open('file.txt', 'r')，要写入文件，可以使用open('file.txt', 'w')。你还可以使用with语句来自动处理文件关闭，例如：with open('file.txt', 'r') as f: content = f.read()。"
        },
        {
            "prompt": "Python中的列表推导式是什么?",
            "completion": "列表推导式是Python中一种简洁的创建列表的方法。它的基本语法是：[expression for item in iterable if condition]。例如，要创建一个包含1到10的平方的列表，可以使用：[x**2 for x in range(1, 11)]。"
        },
        {
            "prompt": "如何在Python中处理异常?",
            "completion": "在Python中，你可以使用try-except语句来处理异常。例如：try: # 可能会引发异常的代码，except Exception as e: # 处理异常的代码。你还可以使用finally块来执行无论是否发生异常都需要执行的代码。"
        }
    ]
    
    # 保存训练数据
    data_path = "training_data.jsonl"
    with open(data_path, "w", encoding="utf-8") as f:
        for item in training_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    return data_path

def fine_tune_model():
    """
    微调模型
    
    Returns:
        str: 微调后的模型ID
    """
    try:
        # 准备训练数据
        data_path = prepare_fine_tuning_data()
        
        # 上传训练数据
        print("正在上传训练数据...")
        with open(data_path, "rb") as f:
            response = openai.File.create(
                file=f,
                purpose="fine-tune"
            )
        file_id = response["id"]
        print(f"训练数据上传成功，文件ID: {file_id}")
        
        # 创建微调任务
        print("正在创建微调任务...")
        response = openai.FineTuningJob.create(
            training_file=file_id,
            model="gpt-3.5-turbo"
        )
        job_id = response["id"]
        print(f"微调任务创建成功，任务ID: {job_id}")
        
        # 等待微调完成（实际应用中可能需要轮询）
        print("微调任务已启动，请等待完成...")
        print("可以使用 openai.FineTuningJob.retrieve(job_id) 查看任务状态")
        
        return job_id
        
    except Exception as e:
        print(f"微调出错: {e}")
        return None

def use_fine_tuned_model(model_id, prompt):
    """
    使用微调后的模型
    
    Args:
        model_id (str): 微调后的模型ID
        prompt (str): 用户输入的提示词
    
    Returns:
        str: 模型的回复
    """
    try:
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "你是一个Python编程助手。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"模型调用出错: {e}")
        return None

def main():
    """
    主函数
    """
    print("模型微调基础示例")
    print("=" * 50)
    
    # 启动微调任务
    job_id = fine_tune_model()
    
    if job_id:
        print(f"\n微调任务已启动，任务ID: {job_id}")
        print("\n当微调完成后，你可以使用以下代码调用微调后的模型:")
        print(f"\nmodel_id = 'your_fine_tuned_model_id'")
        print("prompt = '如何使用Python进行网络请求?'")
        print("response = use_fine_tuned_model(model_id, prompt)")
        print("print(response)")

if __name__ == "__main__":
    main()