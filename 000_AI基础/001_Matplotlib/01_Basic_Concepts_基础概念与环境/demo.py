#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib基础概念与环境设置
展示Matplotlib的基本概念和环境配置
"""

import matplotlib.pyplot as plt
import numpy as np

# 示例1：Matplotlib基本架构演示
def basic_architecture():
    """
    演示Matplotlib的基本架构
    Figure: 整个图形
    Axes: 子图
    Artist: 图形元素
    """
    # 创建Figure对象
    fig = plt.figure()
    
    # 添加Axes对象
    ax = fig.add_subplot(111)
    
    # 绘制数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    
    # 设置标题和标签（英文）
    ax.set_title('Basic Architecture')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # 保存图形
    plt.savefig('basic_architecture.png')
    
    # 显示图形
    plt.show()

# 示例2：Matplotlib样式设置
def style_settings():
    """
    演示Matplotlib的样式设置
    """
    # 查看可用样式
    print("可用的Matplotlib样式:")
    print(plt.style.available[:10])  # 只显示前10个
    
    # 使用不同样式
    styles = ['default', 'ggplot', 'seaborn-v0_8', 'fivethirtyeight']
    
    for style in styles:
        # 应用样式
        plt.style.use(style)
        
        # 创建图形
        plt.figure(figsize=(6, 4))
        
        # 绘制数据
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        
        # 设置标题和标签（英文）
        plt.title(f'Style: {style}')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        
        # 保存图形
        plt.savefig(f'style_{style}.png')
        
        # 显示图形
        plt.show()

# 示例3：Matplotlib配置参数
def config_parameters():
    """
    演示Matplotlib的配置参数
    """
    # 查看默认配置
    print("Matplotlib默认配置:")
    print(f"默认字体大小: {plt.rcParams['font.size']}")
    print(f"默认 figure 大小: {plt.rcParams['figure.figsize']}")
    print(f"默认 dpi: {plt.rcParams['figure.dpi']}")
    
    # 临时修改配置
    with plt.rc_context({'font.size': 12, 'figure.figsize': (8, 6)}):
        # 创建图形
        plt.figure()
        
        # 绘制数据
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        
        # 设置标题和标签（英文）
        plt.title('Custom Configuration')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        
        # 保存图形
        plt.savefig('custom_config.png')
        
        # 显示图形
        plt.show()

# 主函数
def main():
    print("Matplotlib基础概念与环境设置")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 基本架构演示")
    basic_architecture()
    
    print("\n2. 样式设置")
    style_settings()
    
    print("\n3. 配置参数")
    config_parameters()

if __name__ == "__main__":
    main()