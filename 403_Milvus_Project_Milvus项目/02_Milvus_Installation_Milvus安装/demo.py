#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milvus安装演示
展示如何安装Milvus
"""

import os
import sys
import subprocess

def demonstrate_milvus_installation():
    """
    演示如何安装Milvus
    """
    print("=== Milvus安装演示 ===")
    
    # 1. 安装Milvus客户端
    print("\n1. 安装Milvus客户端")
    print("   使用pip安装Milvus客户端...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pymilvus"])
    print("   Milvus客户端安装完成。")
    
    # 2. 验证安装
    print("\n2. 验证安装")
    print("   导入Milvus客户端...")
    from pymilvus import connections
    print("   Milvus客户端导入成功。")
    
    # 3. 启动Milvus
    print("\n3. 启动Milvus")
    print("   连接到Milvus服务器...")
    try:
        connections.connect("default", host="localhost", port="19530")
        print("   连接到Milvus服务器成功。")
    except Exception as e:
        print(f"   连接到Milvus服务器失败: {e}")
        print("   请确保Milvus服务器已启动。")
    
    # 4. 安装完成
    print("\n4. 安装完成")
    print("   Milvus安装完成，可以开始使用了。")

def main():
    """
    主函数
    """
    print("=== Milvus安装演示 ===")
    print("\n本演示展示了如何安装Milvus，帮助您快速掌握Milvus的安装方法。")
    
    # 演示Milvus安装
    demonstrate_milvus_installation()
    
    print("\n=== 演示完成 ===")
    print("\n通过本演示，您应该对Milvus的安装方法有了基本了解。")
    print("在实际应用中，您需要根据具体场景选择合适的安装方式和技术。")

if __name__ == "__main__":
    main()
