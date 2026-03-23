#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib多子图布局
展示Matplotlib的多子图布局功能
"""

import matplotlib.pyplot as plt
import numpy as np

# 示例1：基本子图布局
def basic_subplots():
    """
    基本子图布局
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(x)
    
    # 创建2x2子图
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    
    # 第一个子图
    axs[0, 0].plot(x, y1)
    axs[0, 0].set_title('sin(x)')
    axs[0, 0].set_xlabel('X')
    axs[0, 0].set_ylabel('Y')
    
    # 第二个子图
    axs[0, 1].plot(x, y2)
    axs[0, 1].set_title('cos(x)')
    axs[0, 1].set_xlabel('X')
    axs[0, 1].set_ylabel('Y')
    
    # 第三个子图
    axs[1, 0].plot(x, y3)
    axs[1, 0].set_title('tan(x)')
    axs[1, 0].set_xlabel('X')
    axs[1, 0].set_ylabel('Y')
    
    # 第四个子图
    axs[1, 1].plot(x, y4)
    axs[1, 1].set_title('exp(x)')
    axs[1, 1].set_xlabel('X')
    axs[1, 1].set_ylabel('Y')
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('basic_subplots.png')
    
    # 显示图形
    plt.show()

# 示例2：不规则子图布局
def irregular_subplots():
    """
    不规则子图布局
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(2*x)
    
    # 创建不规则子图布局
    fig = plt.figure(figsize=(12, 8))
    
    # 第一个子图（占据第一行）
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(x, y1)
    ax1.set_title('sin(x)')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    
    # 第二个子图（占据第二行左半部分）
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.plot(x, y2)
    ax2.set_title('cos(x)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    
    # 第三个子图（占据第二行右半部分）
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.plot(x, y3)
    ax3.set_title('sin(2x)')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('irregular_subplots.png')
    
    # 显示图形
    plt.show()

# 示例3：共享坐标轴的子图
def shared_axis_subplots():
    """
    共享坐标轴的子图
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + np.cos(x)
    
    # 创建共享x轴的子图
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    
    # 第一个子图
    axs[0].plot(x, y1)
    axs[0].set_title('sin(x)')
    axs[0].set_ylabel('Y')
    
    # 第二个子图
    axs[1].plot(x, y2)
    axs[1].set_title('cos(x)')
    axs[1].set_ylabel('Y')
    
    # 第三个子图
    axs[2].plot(x, y3)
    axs[2].set_title('sin(x) + cos(x)')
    axs[2].set_xlabel('X')
    axs[2].set_ylabel('Y')
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('shared_axis_subplots.png')
    
    # 显示图形
    plt.show()

# 示例4：使用GridSpec创建复杂布局
def gridspec_subplots():
    """
    使用GridSpec创建复杂布局
    """
    from matplotlib.gridspec import GridSpec
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(x)
    y5 = np.log(x + 1)
    
    # 创建GridSpec
    fig = plt.figure(figsize=(12, 10))
    gs = GridSpec(3, 3, figure=fig)
    
    # 第一个子图（占据第一行）
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(x, y1)
    ax1.set_title('sin(x)')
    
    # 第二个子图（占据第二行第一列）
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(x, y2)
    ax2.set_title('cos(x)')
    
    # 第三个子图（占据第二行第二列）
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(x, y3)
    ax3.set_title('tan(x)')
    
    # 第四个子图（占据第二行第三列和第三行第三列）
    ax4 = fig.add_subplot(gs[1:, 2])
    ax4.plot(x, y4)
    ax4.set_title('exp(x)')
    
    # 第五个子图（占据第三行第一列和第二列）
    ax5 = fig.add_subplot(gs[2, :2])
    ax5.plot(x, y5)
    ax5.set_title('log(x+1)')
    
    # 调整子图间距
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('gridspec_subplots.png')
    
    # 显示图形
    plt.show()

# 主函数
def main():
    print("Matplotlib多子图布局")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 基本子图布局")
    basic_subplots()
    
    print("\n2. 不规则子图布局")
    irregular_subplots()
    
    print("\n3. 共享坐标轴的子图")
    shared_axis_subplots()
    
    print("\n4. 使用GridSpec创建复杂布局")
    gridspec_subplots()

if __name__ == "__main__":
    main()