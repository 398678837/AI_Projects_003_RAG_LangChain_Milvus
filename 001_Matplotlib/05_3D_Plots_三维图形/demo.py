#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib三维图形
展示Matplotlib的三维图形绘制功能
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 示例1：三维散点图
def plot_3d_scatter():
    """
    绘制三维散点图
    """
    # 生成数据
    n = 100
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)
    colors = np.random.rand(n)
    sizes = 1000 * np.random.rand(n)
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制三维散点图
    scatter = ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    
    # 设置标题和标签（英文）
    ax.set_title('3D Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    # 添加颜色条
    fig.colorbar(scatter, ax=ax, label='Color')
    
    # 保存图形
    plt.savefig('3d_scatter.png')
    
    # 显示图形
    plt.show()

# 示例2：三维曲面图
def plot_3d_surface():
    """
    绘制三维曲面图
    """
    # 生成数据
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制三维曲面图
    surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    
    # 设置标题和标签（英文）
    ax.set_title('3D Surface Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    # 添加颜色条
    fig.colorbar(surface, ax=ax, label='Z-value')
    
    # 保存图形
    plt.savefig('3d_surface.png')
    
    # 显示图形
    plt.show()

# 示例3：三维线图
def plot_3d_line():
    """
    绘制三维线图
    """
    # 生成数据
    t = np.linspace(0, 20, 1000)
    x = np.sin(t)
    y = np.cos(t)
    z = t
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制三维线图
    ax.plot(x, y, z, linewidth=2, color='blue')
    
    # 设置标题和标签（英文）
    ax.set_title('3D Line Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    # 保存图形
    plt.savefig('3d_line.png')
    
    # 显示图形
    plt.show()

# 示例4：三维柱状图
def plot_3d_bar():
    """
    绘制三维柱状图
    """
    # 生成数据
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 1, 4, 5]
    z = [0, 0, 0, 0, 0]
    dx = [0.5, 0.5, 0.5, 0.5, 0.5]
    dy = [0.5, 0.5, 0.5, 0.5, 0.5]
    dz = [1, 2, 3, 4, 5]
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制三维柱状图
    ax.bar3d(x, y, z, dx, dy, dz, color='blue', alpha=0.8)
    
    # 设置标题和标签（英文）
    ax.set_title('3D Bar Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    # 保存图形
    plt.savefig('3d_bar.png')
    
    # 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib三维图形")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 三维散点图")
    plot_3d_scatter()
    
    print("\n2. 三维曲面图")
    plot_3d_surface()
    
    print("\n3. 三维线图")
    plot_3d_line()
    
    print("\n4. 三维柱状图")
    plot_3d_bar()

if __name__ == "__main__":
    main()