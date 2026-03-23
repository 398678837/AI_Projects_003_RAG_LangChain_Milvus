#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn基本图形绘制
展示Seaborn中各种基本图形的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 散点图
def scatter_plot():
    """散点图"""
    print("\n=== 散点图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本散点图
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="total_bill", y="tip", data=tips)
    plt.title("Scatter Plot: Total Bill vs Tip")
    plt.savefig("scatter_basic.png")
    plt.close()
    
    # 带分类的散点图
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="total_bill", y="tip", hue="sex", style="time", data=tips)
    plt.title("Scatter Plot with Categories")
    plt.savefig("scatter_categories.png")
    plt.close()
    
    print("散点图绘制完成")

# 2. 线图
def line_plot():
    """线图"""
    print("\n=== 线图 ===")
    
    # 创建时间序列数据
    dates = pd.date_range("2024-01-01", periods=30)
    values = np.random.randn(30).cumsum()
    data = pd.DataFrame({"date": dates, "value": values})
    
    # 基本线图
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="date", y="value", data=data)
    plt.title("Line Plot: Time Series Data")
    plt.savefig("line_basic.png")
    plt.close()
    
    # 多条线图
    data["value2"] = np.random.randn(30).cumsum()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data[["value", "value2"]])
    plt.title("Line Plot: Multiple Lines")
    plt.savefig("line_multiple.png")
    plt.close()
    
    print("线图绘制完成")

# 3. 柱状图
def bar_plot():
    """柱状图"""
    print("\n=== 柱状图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本柱状图
    plt.figure(figsize=(8, 6))
    sns.barplot(x="day", y="total_bill", data=tips)
    plt.title("Bar Plot: Total Bill by Day")
    plt.savefig("bar_basic.png")
    plt.close()
    
    # 带误差条的柱状图
    plt.figure(figsize=(8, 6))
    sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Bar Plot with Error Bars")
    plt.savefig("bar_error.png")
    plt.close()
    
    print("柱状图绘制完成")

# 4. 直方图
def histogram():
    """直方图"""
    print("\n=== 直方图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本直方图
    plt.figure(figsize=(8, 6))
    sns.histplot(tips["total_bill"])
    plt.title("Histogram: Total Bill Distribution")
    plt.savefig("hist_basic.png")
    plt.close()
    
    # 带密度曲线的直方图
    plt.figure(figsize=(8, 6))
    sns.histplot(tips["total_bill"], kde=True)
    plt.title("Histogram with Density Curve")
    plt.savefig("hist_density.png")
    plt.close()
    
    print("直方图绘制完成")

# 5. 箱线图
def box_plot():
    """箱线图"""
    print("\n=== 箱线图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本箱线图
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.title("Box Plot: Total Bill by Day")
    plt.savefig("box_basic.png")
    plt.close()
    
    # 分组箱线图
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Box Plot: Total Bill by Day and Gender")
    plt.savefig("box_grouped.png")
    plt.close()
    
    print("箱线图绘制完成")

# 6. 小提琴图
def violin_plot():
    """小提琴图"""
    print("\n=== 小提琴图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本小提琴图
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="day", y="total_bill", data=tips)
    plt.title("Violin Plot: Total Bill by Day")
    plt.savefig("violin_basic.png")
    plt.close()
    
    # 分组小提琴图
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
    plt.title("Violin Plot: Total Bill by Day and Gender")
    plt.savefig("violin_grouped.png")
    plt.close()
    
    print("小提琴图绘制完成")

# 主函数
def main():
    print("Seaborn Basic Plots")
    print("=" * 50)
    
    # 运行所有示例
    scatter_plot()
    line_plot()
    bar_plot()
    histogram()
    box_plot()
    violin_plot()
    
    print("\nAll basic plots completed!")

if __name__ == "__main__":
    main()