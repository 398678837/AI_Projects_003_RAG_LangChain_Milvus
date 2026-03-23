#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib数据可视化实战
展示Matplotlib在数据可视化中的实际应用
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 示例1：时间序列数据可视化
def time_series_visualization():
    """
    时间序列数据可视化
    """
    # 生成时间序列数据
    dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    
    # 创建图形
    plt.figure(figsize=(12, 6))
    
    # 绘制时间序列图
    plt.plot(dates, values)
    
    # 设置标题和标签（英文）
    plt.title('Time Series Data Visualization')
    plt.xlabel('Date')
    plt.ylabel('Value')
    
    # 旋转x轴标签
    plt.xticks(rotation=45)
    
    # 添加网格
    plt.grid(True, alpha=0.3)
    
    # 保存图形
    plt.savefig('time_series.png', bbox_inches='tight')
    
    # 显示图形
    plt.show()

# 示例2：多变量数据可视化
def multivariate_visualization():
    """
    多变量数据可视化
    """
    # 生成多变量数据
    np.random.seed(42)
    n = 100
    x = np.random.randn(n)
    y1 = x + np.random.randn(n) * 0.5
    y2 = -x + np.random.randn(n) * 0.5
    y3 = x**2 + np.random.randn(n) * 0.5
    
    # 创建图形
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    
    # 第一个子图
    axs[0].scatter(x, y1)
    axs[0].set_title('y1 vs x')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y1')
    axs[0].grid(True, alpha=0.3)
    
    # 第二个子图
    axs[1].scatter(x, y2)
    axs[1].set_title('y2 vs x')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y2')
    axs[1].grid(True, alpha=0.3)
    
    # 第三个子图
    axs[2].scatter(x, y3)
    axs[2].set_title('y3 vs x')
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('y3')
    axs[2].grid(True, alpha=0.3)
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('multivariate.png')
    
    # 显示图形
    plt.show()

# 示例3：分类数据可视化
def categorical_visualization():
    """
    分类数据可视化
    """
    # 生成分类数据
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values1 = [25, 30, 15, 20, 10]
    values2 = [15, 25, 20, 15, 25]
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 设置柱状图位置
    x = np.arange(len(categories))
    width = 0.35
    
    # 绘制柱状图
    plt.bar(x - width/2, values1, width, label='Value 1')
    plt.bar(x + width/2, values2, width, label='Value 2')
    
    # 设置标题和标签（英文）
    plt.title('Categorical Data Visualization')
    plt.xlabel('Category')
    plt.ylabel('Value')
    
    # 设置x轴刻度
    plt.xticks(x, categories, rotation=45)
    
    # 添加图例
    plt.legend()
    
    # 保存图形
    plt.savefig('categorical.png', bbox_inches='tight')
    
    # 显示图形
    plt.show()

# 示例4：相关性热图
def correlation_heatmap():
    """
    相关性热图
    """
    # 生成相关数据
    np.random.seed(42)
    data = np.random.randn(10, 5)
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
    corr = df.corr()
    
    # 创建图形
    plt.figure(figsize=(10, 8))
    
    # 绘制热图
    im = plt.imshow(corr, cmap='coolwarm')
    
    # 设置标题（英文）
    plt.title('Correlation Heatmap')
    
    # 添加颜色条
    plt.colorbar(im, label='Correlation')
    
    # 设置x轴和y轴标签
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    
    # 旋转x轴标签
    plt.xticks(rotation=45)
    
    # 在热图上添加数值
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            plt.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center', color='white')
    
    # 保存图形
    plt.savefig('correlation_heatmap.png', bbox_inches='tight')
    
    # 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib数据可视化实战")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 时间序列数据可视化")
    time_series_visualization()
    
    print("\n2. 多变量数据可视化")
    multivariate_visualization()
    
    print("\n3. 分类数据可视化")
    categorical_visualization()
    
    print("\n4. 相关性热图")
    correlation_heatmap()

if __name__ == "__main__":
    main()