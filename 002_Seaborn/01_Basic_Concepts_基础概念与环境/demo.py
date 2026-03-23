#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn基础概念与环境
展示Seaborn的基本架构、样式设置和配置参数
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 打印Seaborn版本
print(f"Seaborn version: {sns.__version__}")

# 设置Seaborn样式
print("\nAvailable Seaborn styles:")
print(sns.get_dataset_names())

# 1. 基础样式设置
def basic_styling():
    """基础样式设置"""
    print("\n=== 基础样式设置 ===")
    
    # 可用的样式
    styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
    
    # 创建一个简单的数据集
    np.random.seed(42)
    data = np.random.randn(100)
    
    # 测试不同样式
    for style in styles:
        sns.set_style(style)
        plt.figure(figsize=(6, 4))
        sns.histplot(data)
        plt.title(f'Style: {style}')
        plt.savefig(f'style_{style}.png')
        plt.close()
    
    print("基础样式设置完成")

# 2. 颜色主题设置
def color_palettes():
    """颜色主题设置"""
    print("\n=== 颜色主题设置 ===")
    
    # 查看默认颜色主题
    default_palette = sns.color_palette()
    print(f"Default palette: {default_palette}")
    
    # 内置颜色主题
    palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
    
    for palette in palettes:
        sns.set_palette(palette)
        plt.figure(figsize=(6, 4))
        sns.histplot(np.random.randn(100))
        plt.title(f'Palette: {palette}')
        plt.savefig(f'palette_{palette}.png')
        plt.close()
    
    print("颜色主题设置完成")

# 3. 上下文设置
def contexts():
    """上下文设置"""
    print("\n=== 上下文设置 ===")
    
    # 可用的上下文
    contexts = ['paper', 'notebook', 'talk', 'poster']
    
    for context in contexts:
        sns.set_context(context)
        plt.figure(figsize=(6, 4))
        sns.histplot(np.random.randn(100))
        plt.title(f'Context: {context}')
        plt.savefig(f'context_{context}.png')
        plt.close()
    
    print("上下文设置完成")

# 4. 加载示例数据集
def load_datasets():
    """加载示例数据集"""
    print("\n=== 加载示例数据集 ===")
    
    # 加载几个常用的示例数据集
    datasets = ['tips', 'iris', 'titanic', 'mpg']
    
    for dataset in datasets:
        try:
            data = sns.load_dataset(dataset)
            print(f"Loaded {dataset} dataset with shape: {data.shape}")
            print(f"Columns: {list(data.columns)}")
            print(data.head())
            print()
        except Exception as e:
            print(f"Error loading {dataset}: {e}")
    
    print("示例数据集加载完成")

# 5. 基本图形示例
def basic_plot_example():
    """基本图形示例"""
    print("\n=== 基本图形示例 ===")
    
    # 加载tips数据集
    tips = sns.load_dataset('tips')
    
    # 创建一个简单的散点图
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='total_bill', y='tip', data=tips)
    plt.title('Scatter plot of Total Bill vs Tip')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.savefig('basic_scatter.png')
    plt.close()
    
    print("基本图形示例完成")

# 主函数
def main():
    print("Seaborn Basic Concepts and Environment")
    print("=" * 50)
    
    # 运行所有示例
    basic_styling()
    color_palettes()
    contexts()
    load_datasets()
    basic_plot_example()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main()