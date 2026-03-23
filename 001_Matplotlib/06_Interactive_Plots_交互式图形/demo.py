#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib交互式图形
展示Matplotlib的交互式图形功能
"""

import matplotlib.pyplot as plt
import numpy as np

# 示例1：基本交互功能
def basic_interactivity():
    """
    基本交互功能
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图
    plt.plot(x, y)
    
    # 设置标题和标签（英文）
    plt.title('Basic Interactivity')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # 启用交互模式
    plt.ion()
    
    # 显示图形
    plt.show()
    
    # 等待用户交互
    input("按回车键继续...")
    
    # 禁用交互模式
    plt.ioff()
    
    # 保存图形
    plt.savefig('basic_interactivity.png')
    
    # 关闭图形
    plt.close()

# 示例2：事件处理
def event_handling():
    """
    事件处理
    """
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制折线图
    line, = ax.plot(x, y)
    
    # 设置标题和标签（英文）
    ax.set_title('Event Handling')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # 定义鼠标移动事件处理函数
    def on_move(event):
        if event.inaxes == ax:
            print(f'Mouse position: x={event.xdata:.2f}, y={event.ydata:.2f}')
    
    # 定义鼠标点击事件处理函数
    def on_click(event):
        if event.inaxes == ax:
            print(f'Mouse clicked at: x={event.xdata:.2f}, y={event.ydata:.2f}')
            # 在点击位置添加标记
            ax.plot(event.xdata, event.ydata, 'ro')
            fig.canvas.draw_idle()
    
    # 连接事件处理函数
    fig.canvas.mpl_connect('motion_notify_event', on_move)
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    # 显示图形
    plt.show()
    
    # 保存图形
    plt.savefig('event_handling.png')

# 示例3：交互式控件
def interactive_widgets():
    """
    交互式控件
    """
    from matplotlib.widgets import Slider, Button
    
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.25)
    
    # 绘制折线图
    line, = ax.plot(x, y)
    
    # 设置标题和标签（英文）
    ax.set_title('Interactive Widgets')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_ylim(-1.5, 1.5)
    
    # 创建滑块控件
    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider = Slider(
        ax=ax_slider,
        label='Frequency',
        valmin=0.1,
        valmax=5.0,
        valinit=1.0,
        valstep=0.1
    )
    
    # 创建按钮控件
    ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(ax_button, 'Reset')
    
    # 定义滑块更新函数
    def update(val):
        freq = slider.val
        y = np.sin(freq * x)
        line.set_ydata(y)
        fig.canvas.draw_idle()
    
    # 定义按钮点击函数
    def reset(event):
        slider.reset()
    
    # 连接控件事件
    slider.on_changed(update)
    button.on_clicked(reset)
    
    # 显示图形
    plt.show()
    
    # 保存图形
    plt.savefig('interactive_widgets.png')

# 主函数
def main():
    print("Matplotlib交互式图形")
    print("=" * 50)
    
    # 运行各个示例
    print("1. 基本交互功能")
    basic_interactivity()
    
    print("\n2. 事件处理")
    event_handling()
    
    print("\n3. 交互式控件")
    interactive_widgets()

if __name__ == "__main__":
    main()