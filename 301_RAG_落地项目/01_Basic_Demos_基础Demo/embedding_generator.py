#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Embedding向量生成器
用sentence-transformers将文本转为向量，输出向量维度和内容
"""

import os
import json
from typing import List, Dict, Optional

# 尝试导入所需库
try:
    from sentence_transformers import SentenceTransformer
    embedding_support = True
except ImportError:
    embedding_support = False
    print("警告: 缺少sentence-transformers库，请安装")

class EmbeddingGenerator:
    """Embedding向量生成器"""
    
    def __init__(self, model_name: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        """
        初始化Embedding生成器
        
        Args:
            model_name: 使用的预训练模型名称
        """
        self.model_name = model_name
        self.model = None
        if embedding_support:
            try:
                self.model = SentenceTransformer(model_name)
                print(f"加载模型成功: {model_name}")
            except Exception as e:
                print(f"加载模型失败: {e}")
                self.model = None
    
    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        生成文本的Embedding向量
        
        Args:
            text: 待编码的文本
            
        Returns:
            文本的Embedding向量
        """
        if not self.model:
            print("错误: 模型未加载")
            return None
        
        try:
            embedding = self.model.encode(text).tolist()
            return embedding
        except Exception as e:
            print(f"生成Embedding失败: {e}")
            return None
    
    def process_texts(self, texts: List[str]) -> List[Dict[str, any]]:
        """
        处理多个文本，生成Embedding向量
        
        Args:
            texts: 文本列表
            
        Returns:
            包含文本和对应Embedding的字典列表
        """
        results = []
        
        for i, text in enumerate(texts):
            embedding = self.generate_embedding(text)
            if embedding:
                results.append({
                    "id": i + 1,
                    "text": text,
                    "embedding": embedding,
                    "embedding_dim": len(embedding)
                })
            else:
                results.append({
                    "id": i + 1,
                    "text": text,
                    "embedding": None,
                    "error": "生成Embedding失败"
                })
        
        return results
    
    def process_file(self, file_path: str, output_file: Optional[str] = None) -> List[Dict[str, any]]:
        """
        处理文件中的文本，生成Embedding向量
        
        Args:
            file_path: 文本文件路径
            output_file: 输出文件路径，None表示不保存
            
        Returns:
            包含文本和对应Embedding的字典列表
        """
        # 读取文件
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
        except Exception as e:
            print(f"读取文件失败: {e}")
            return []
        
        # 简单分割文本
        texts = self._split_text(text)
        
        # 生成Embedding
        results = self.process_texts(texts)
        
        # 保存结果
        if output_file:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"保存结果到: {output_file}")
        
        return results
    
    def _split_text(self, text: str) -> List[str]:
        """简单分割文本"""
        # 按换行符分割
        texts = text.split('\n')
        # 过滤空文本
        texts = [t.strip() for t in texts if t.strip()]
        return texts

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Embedding向量生成器")
    parser.add_argument("text_or_file", help="文本或文件路径")
    parser.add_argument("--output", default=None, help="输出文件路径")
    parser.add_argument("--model", default="paraphrase-multilingual-MiniLM-L12-v2", help="使用的预训练模型")
    
    args = parser.parse_args()
    
    # 创建Embedding生成器
    generator = EmbeddingGenerator(model_name=args.model)
    
    # 检查输入是文本还是文件
    if os.path.exists(args.text_or_file):
        # 处理文件
        results = generator.process_file(args.text_or_file, args.output)
    else:
        # 处理文本
        results = generator.process_texts([args.text_or_file])
    
    # 显示结果
    print(f"\n处理完成，共生成 {len(results)} 个Embedding")
    
    # 显示前3个结果
    print("\n前3个结果:")
    for result in results[:3]:
        print(f"\nID: {result['id']}")
        print(f"文本: {result['text'][:100]}..." if len(result['text']) > 100 else f"文本: {result['text']}")
        if 'embedding' in result and result['embedding']:
            print(f"Embedding维度: {len(result['embedding'])}")
            print(f"Embedding前5个值: {result['embedding'][:5]}")
        else:
            print(f"错误: {result.get('error', '未知错误')}")

if __name__ == "__main__":
    main()
