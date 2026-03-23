#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib基本图形绘制
展示Matplotlib的基本图形绘制功能
"""

import matplotlib.pyplot as plt
import numpy as np

# 示例1：折线图
def plot_line():
    """
    绘制折线图
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # 创建图形
    plt.figure(figsize=(8, 6))
    
    # 绘制折线图
    plt.plot(x, y1, label='sin(x)', linewidth=2, linestyle='-', color='blue')
    plt.plot(x, y2, label='cos(x)', linewidth=2, linestyle='--', color='red')
    
    # 设置标题和标签（英文）
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 添加图例
    plt.legend()
    
    # 显示网格
    plt.grid(True, alpha=0.3)
    
    # 保存图形
    plt.savefig('line_plot.png')
    
    # 显示图形
    plt.show()

# 示例2：散点图
def plot_scatter():
    """
    绘制散点图
    """
    # 生成数据
    x = np.random.rand(100)
    y = np.random.rand(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)
    
    # 创建图形
    plt.figure(figsize=(8, 6))
    
    # 绘制散点图
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    
    # 设置标题和标签（英文）
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 添加颜色条
    plt.colorbar(scatter, label='Color')
    
    # 保存图形
    plt.savefig('scatter_plot.png')
    
    # 显示图形
    plt.show()

# 示例3：柱状图
def plot_bar():
    """
    绘制柱状图
    """
    # 生成数据
    categories = ['A', 'B', 'C', 'D', 'E']
    values1 = [10, 15, 7, 12, 9]
    values2 = [8, 12, 9, 10, 11]
    
    # 创建图形
    plt.figure(figsize=(8, 6))
    
    # 设置柱状图位置
    x = np.arange(len(categories))
    width = 0.35
    
    # 绘制柱状图
    plt.bar(x - width/2, values1, width, label='Value 1')
    plt.bar(x + width/2, values2, width, label='Value 2')
    
    # 设置标题和标签（英文）
    plt.title('Bar Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    
    # 设置x轴刻度
    plt.xticks(x, categories)
    
    # 添加图例
    plt.legend()
    
    # 保存图形
    plt.savefig('bar_plot.png')
    
    # 显示图形
    plt.show()

# 示例4：直方图
def plot_hist():
    """
    绘制直方图
    """
    # 生成数据
    data1 = np.random.randn(1000)
    data2 = np.random.randn(1000) + 2
    
    # 创建图形
    plt.figure(figsize=(8, 6))
    
    # 绘制直方图
    plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
    plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
    
    # 设置标题和标签（英文）
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # 添加图例
    plt.legend()
    
    # 保存图形
    plt.savefig('histogram.png')
    
    # 显示图形
    plt.show()

# 示例5：饼图
def plot_pie():
    """
    绘制饼图
    """
    # 生成数据
    labels = ['A', 'B', 'C', 'D']
    sizes = [30, 25, 20, 25]
    explode = (0.1, 0, 0, 0)
    
    # 创建图形
    plt.figure(figsize=(6, 6))
    
    # 绘制饼图
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    
    # 设置标题（英文）
    plt.title('Pie Chart')
    
    # 确保饼图是圆形
    plt.axis('equal')
    
    # 保存图形
    plt.savefig('pie_chart.png')
    
    # 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib基本图形绘制")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 折线图")
    plot_line()
    
    print("\n2. 散点图")
    plot_scatter()
    
    print("\n3. 柱状图")
    plot_bar()
    
    print("\n4. 直方图")
    plot_hist()
    
    print("\n5. 饼图")
    plot_pie()

if __name__ == "__main__":
    main()