#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib图形美化与定制
展示Matplotlib的图形美化和定制功能
"""

import matplotlib.pyplot as plt
import numpy as np

# 示例1：颜色和线型定制
def customize_colors_and_lines():
    """
    定制颜色和线型
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图，定制颜色和线型
    plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2, marker='o', markersize=4)
    plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2, marker='s', markersize=4)
    plt.plot(x, y3, label='tan(x)', color='green', linestyle=':', linewidth=2, marker='^', markersize=4)
    
    # 设置标题和标签（英文）
    plt.title('Custom Colors and Lines')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 添加图例
    plt.legend()
    
    # 显示网格
    plt.grid(True, alpha=0.3)
    
    # 保存图形
    plt.savefig('custom_colors_lines.png')
    
    # 显示图形
    plt.show()

# 示例2：字体和文本定制
def customize_fonts_and_text():
    """
    定制字体和文本
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图
    plt.plot(x, y)
    
    # 设置标题和标签（英文），定制字体
    plt.title('Custom Fonts and Text', fontsize=16, fontweight='bold', fontstyle='italic')
    plt.xlabel('X-axis', fontsize=12, fontweight='medium')
    plt.ylabel('Y-axis', fontsize=12, fontweight='medium')
    
    # 添加文本注释
    plt.text(5, 0, 'sin(x) function', fontsize=12, ha='center', va='center', 
             bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))
    
    # 添加箭头注释
    plt.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    # 保存图形
    plt.savefig('custom_fonts_text.png')
    
    # 显示图形
    plt.show()

# 示例3：坐标轴定制
def customize_axes():
    """
    定制坐标轴
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图
    plt.plot(x, y)
    
    # 设置标题和标签（英文）
    plt.title('Custom Axes')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 定制坐标轴范围
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    
    # 定制坐标轴刻度
    plt.xticks(np.arange(0, 11, 2))
    plt.yticks(np.arange(-1, 1.1, 0.5))
    
    # 定制坐标轴样式
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    
    # 保存图形
    plt.savefig('custom_axes.png')
    
    # 显示图形
    plt.show()

# 示例4：背景和网格定制
def customize_background_and_grid():
    """
    定制背景和网格
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 设置背景颜色
    ax = plt.gca()
    ax.set_facecolor('#f0f0f0')
    
    # 绘制折线图
    plt.plot(x, y, color='blue', linewidth=2)
    
    # 设置标题和标签（英文）
    plt.title('Custom Background and Grid')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 定制网格
    plt.grid(True, color='white', linestyle='-', linewidth=1, alpha=0.8)
    
    # 保存图形
    plt.savefig('custom_background_grid.png')
    
    # 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib图形美化与定制")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 颜色和线型定制")
    customize_colors_and_lines()
    
    print("\n2. 字体和文本定制")
    customize_fonts_and_text()
    
    print("\n3. 坐标轴定制")
    customize_axes()
    
    print("\n4. 背景和网格定制")
    customize_background_and_grid()

if __name__ == "__main__":
    main()