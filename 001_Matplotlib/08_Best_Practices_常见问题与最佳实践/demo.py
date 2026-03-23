#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib常见问题与最佳实践
展示Matplotlib的常见问题解决方案和最佳实践
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 示例1：中文显示问题解决方案
def chinese_display():
    """
    解决Matplotlib中文显示问题
    """
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图
    plt.plot(x, y)
    
    # 设置标题和标签（中文）
    plt.title('中文标题')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    
    # 保存图形
    plt.savefig('chinese_display.png')
    
    # 显示图形
    plt.show()

# 示例2：图形分辨率和大小设置
def figure_size_and_dpi():
    """
    设置图形分辨率和大小
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形，设置大小和DPI
    plt.figure(figsize=(10, 6), dpi=100)
    
    # 绘制折线图
    plt.plot(x, y)
    
    # 设置标题和标签（英文）
    plt.title('Figure Size and DPI')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 保存图形，设置DPI
    plt.savefig('figure_size_dpi.png', dpi=300, bbox_inches='tight')
    
    # 显示图形
    plt.show()

# 示例3：批量处理图形
def batch_processing():
    """
    批量处理和保存图形
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    functions = [np.sin, np.cos, np.tan, np.exp]
    function_names = ['sin', 'cos', 'tan', 'exp']
    
    # 批量创建和保存图形
    for i, (func, name) in enumerate(zip(functions, function_names)):
        # 创建图形
        plt.figure(figsize=(8, 6))
        
        # 绘制折线图
        y = func(x)
        plt.plot(x, y)
        
        # 设置标题和标签（英文）
        plt.title(f'{name}(x)')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        
        # 保存图形
        plt.savefig(f'batch_{name}.png')
        
        # 关闭图形，释放内存
        plt.close()
        
        print(f'Saved {name}.png')

# 示例4：性能优化
def performance_optimization():
    """
    Matplotlib性能优化
    """
    import time
    
    # 生成大量数据
    n = 100000
    x = np.linspace(0, 10, n)
    y = np.sin(x)
    
    # 方法1：普通绘图
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Performance Test')
    plt.savefig('performance_normal.png')
    plt.close()
    normal_time = time.time() - start_time
    print(f'Normal plotting time: {normal_time:.4f} seconds')
    
    # 方法2：使用Line2D对象
    start_time = time.time()
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot([], [])
    line.set_data(x, y)
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())
    ax.set_title('Performance Test')
    plt.savefig('performance_line2d.png')
    plt.close()
    line2d_time = time.time() - start_time
    print(f'Line2D plotting time: {line2d_time:.4f} seconds')
    
    # 方法3：使用agg后端
    import matplotlib
    matplotlib.use('Agg')
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Performance Test')
    plt.savefig('performance_agg.png')
    plt.close()
    agg_time = time.time() - start_time
    print(f'Agg backend time: {agg_time:.4f} seconds')

# 示例5：最佳实践汇总
def best_practices():
    """
    Matplotlib最佳实践
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # 1. 使用面向对象API
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 2. 使用样式
    plt.style.use('seaborn-v0_8')
    
    # 3. 绘制图形
    ax.plot(x, y1, label='sin(x)', linewidth=2)
    ax.plot(x, y2, label='cos(x)', linewidth=2)
    
    # 4. 设置标题和标签（英文）
    ax.set_title('Best Practices Example', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    
    # 5. 添加图例
    ax.legend(fontsize=10)
    
    # 6. 添加网格
    ax.grid(True, alpha=0.3)
    
    # 7. 调整布局
    plt.tight_layout()
    
    # 8. 保存图形
    plt.savefig('best_practices.png', dpi=300, bbox_inches='tight')
    
    # 9. 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib常见问题与最佳实践")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 中文显示问题解决方案")
    chinese_display()
    
    print("\n2. 图形分辨率和大小设置")
    figure_size_and_dpi()
    
    print("\n3. 批量处理图形")
    batch_processing()
    
    print("\n4. 性能优化")
    performance_optimization()
    
    print("\n5. 最佳实践汇总")
    best_practices()

if __name__ == "__main__":
    main()