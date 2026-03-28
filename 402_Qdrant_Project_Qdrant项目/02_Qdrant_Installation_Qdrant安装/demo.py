#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qdrant安装演示
展示如何安装Qdrant
"""

import os
import sys
import subprocess

def demonstrate_qdrant_installation():
    """
    演示如何安装Qdrant
    """
    print("=== Qdrant安装演示 ===")
    
    # 1. 安装Qdrant
    print("\n1. 安装Qdrant")
    print("   使用pip安装Qdrant客户端...")
    subprocess.run([sys.executable, "-m", "pip", "install", "qdrant-client"])
    print("   Qdrant客户端安装完成。")
    
    # 2. 验证安装
    print("\n2. 验证安装")
    print("   导入Qdrant客户端...")
    from qdrant_client import QdrantClient
    print("   Qdrant客户端导入成功。")
    
    # 3. 启动Qdrant
    print("\n3. 启动Qdrant")
    print("   创建Qdrant客户端实例...")
    client = QdrantClient(path="./qdrant_db")
    print("   Qdrant客户端实例创建成功。")
    
    # 4. 安装完成
    print("\n4. 安装完成")
    print("   Qdrant安装完成，可以开始使用了。")

def main():
    """
    主函数
    """
    print("=== Qdrant安装演示 ===")
    print("\n本演示展示了如何安装Qdrant，帮助您快速掌握Qdrant的安装方法。")
    
    # 演示Qdrant安装
    demonstrate_qdrant_installation()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Qdrant的安装方法有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的安装方式和技术。")

if __name__ == "__main__":
    main()
