#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档切片器
支持PDF、Word文件，自动切分文本块，带保存功能
"""

import os
import re
from typing import List, Dict, Optional

# 尝试导入所需库
try:
    from pypdf import PdfReader
    from docx import Document
    pdf_support = True
    docx_support = True
except ImportError:
    pdf_support = False
    docx_support = False
    print("警告: 缺少PDF或Word支持库，请安装pypdf和python-docx")

class DocumentSplitter:
    """文档切片器"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        初始化文档切片器
        
        Args:
            chunk_size: 每个文本块的大小
            chunk_overlap: 文本块之间的重叠部分大小
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def load_document(self, file_path: str) -> str:
        """
        加载文档内容
        
        Args:
            file_path: 文档文件路径
            
        Returns:
            文档文本内容
        """
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf' and pdf_support:
            return self._load_pdf(file_path)
        elif ext == '.docx' and docx_support:
            return self._load_docx(file_path)
        elif ext == '.txt':
            return self._load_txt(file_path)
        else:
            raise ValueError(f"不支持的文件格式: {ext}")
    
    def _load_pdf(self, file_path: str) -> str:
        """加载PDF文件"""
        text = ""
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def _load_docx(self, file_path: str) -> str:
        """加载Word文件"""
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    
    def _load_txt(self, file_path: str) -> str:
        """加载文本文件"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    
    def split_text(self, text: str) -> List[str]:
        """
        切分文本
        
        Args:
            text: 待切分的文本
            
        Returns:
            切分后的文本块列表
        """
        # 清洗文本
        text = self._clean_text(text)
        
        # 按句子分割
        sentences = self._split_into_sentences(text)
        
        # 构建文本块
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence_length = len(sentence)
            
            # 如果当前块加上新句子超过大小限制，保存当前块
            if current_length + sentence_length > self.chunk_size:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                    # 保留重叠部分
                    overlap_size = min(self.chunk_overlap, current_length)
                    # 从当前块中提取重叠部分
                    overlap_text = ' '.join(current_chunk[-overlap_size:]) if overlap_size > 0 else ''
                    current_chunk = [overlap_text, sentence]
                    current_length = len(' '.join(current_chunk))
                else:
                    # 如果单个句子就超过大小限制，直接添加
                    chunks.append(sentence)
                    current_chunk = []
                    current_length = 0
            else:
                current_chunk.append(sentence)
                current_length += sentence_length
        
        # 添加最后一个块
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def _clean_text(self, text: str) -> str:
        """清洗文本"""
        # 移除多余的空白字符
        text = re.sub(r'\s+', ' ', text)
        # 移除首尾空白
        text = text.strip()
        return text
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """将文本分割成句子"""
        # 简单的句子分割规则
        sentences = re.split(r'[。！？.!?]', text)
        # 过滤空句子
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences
    
    def process_document(self, file_path: str, output_dir: Optional[str] = None) -> List[str]:
        """
        处理文档并保存切片
        
        Args:
            file_path: 文档文件路径
            output_dir: 输出目录，None表示不保存
            
        Returns:
            切分后的文本块列表
        """
        # 加载文档
        text = self.load_document(file_path)
        
        # 切分文本
        chunks = self.split_text(text)
        
        # 保存切片
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            
            for i, chunk in enumerate(chunks):
                chunk_file = os.path.join(output_dir, f"{base_name}_chunk_{i+1}.txt")
                with open(chunk_file, 'w', encoding='utf-8') as f:
                    f.write(chunk)
                print(f"保存切片: {chunk_file}")
        
        return chunks

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="文档切片器")
    parser.add_argument("file_path", help="文档文件路径")
    parser.add_argument("--output-dir", default=None, help="输出目录")
    parser.add_argument("--chunk-size", type=int, default=1000, help="每个文本块的大小")
    parser.add_argument("--chunk-overlap", type=int, default=200, help="文本块之间的重叠部分大小")
    
    args = parser.parse_args()
    
    # 创建切片器
    splitter = DocumentSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap
    )
    
    # 处理文档
    try:
        chunks = splitter.process_document(args.file_path, args.output_dir)
        print(f"\n文档处理完成，共生成 {len(chunks)} 个切片")
        
        # 显示前3个切片的内容
        print("\n前3个切片内容:")
        for i, chunk in enumerate(chunks[:3]):
            print(f"\n切片 {i+1}:")
            print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
            
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
