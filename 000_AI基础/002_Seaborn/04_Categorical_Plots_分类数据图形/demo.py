#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn分类数据图形
展示Seaborn中各种分类数据图形的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 条形图
def barplot():
    """条形图"""
    print("\n=== 条形图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本条形图
    plt.figure(figsize=(8, 6))
    sns.barplot(x="day", y="total_bill", data=tips)
    plt.title("Bar Plot: Total Bill by Day")
    plt.savefig("barplot_basic.png")
    plt.close()
    
    # 分组条形图
    plt.figure(figsize=(8, 6))
    sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Bar Plot: Total Bill by Day and Gender")
    plt.savefig("barplot_grouped.png")
    plt.close()
    
    # 水平条形图
    plt.figure(figsize=(8, 6))
    sns.barplot(x="total_bill", y="day", data=tips)
    plt.title("Horizontal Bar Plot: Total Bill by Day")
    plt.savefig("barplot_horizontal.png")
    plt.close()
    
    print("条形图绘制完成")

# 2. 计数图
def countplot():
    """计数图"""
    print("\n=== 计数图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本计数图
    plt.figure(figsize=(8, 6))
    sns.countplot(x="day", data=tips)
    plt.title("Count Plot: Number of Tips by Day")
    plt.savefig("countplot_basic.png")
    plt.close()
    
    # 分组计数图
    plt.figure(figsize=(8, 6))
    sns.countplot(x="day", hue="sex", data=tips)
    plt.title("Count Plot: Number of Tips by Day and Gender")
    plt.savefig("countplot_grouped.png")
    plt.close()
    
    print("计数图绘制完成")

# 3. 箱线图
def boxplot():
    """箱线图"""
    print("\n=== 箱线图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本箱线图
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.title("Box Plot: Total Bill by Day")
    plt.savefig("boxplot_basic.png")
    plt.close()
    
    # 分组箱线图
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Box Plot: Total Bill by Day and Gender")
    plt.savefig("boxplot_grouped.png")
    plt.close()
    
    print("箱线图绘制完成")

# 4. 小提琴图
def violinplot():
    """小提琴图"""
    print("\n=== 小提琴图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本小提琴图
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="day", y="total_bill", data=tips)
    plt.title("Violin Plot: Total Bill by Day")
    plt.savefig("violinplot_basic.png")
    plt.close()
    
    # 分组小提琴图
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
    plt.title("Violin Plot: Total Bill by Day and Gender")
    plt.savefig("violinplot_split.png")
    plt.close()
    
    print("小提琴图绘制完成")

# 5. 点图
def pointplot():
    """点图"""
    print("\n=== 点图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本点图
    plt.figure(figsize=(8, 6))
    sns.pointplot(x="day", y="total_bill", data=tips)
    plt.title("Point Plot: Total Bill by Day")
    plt.savefig("pointplot_basic.png")
    plt.close()
    
    # 分组点图
    plt.figure(figsize=(8, 6))
    sns.pointplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Point Plot: Total Bill by Day and Gender")
    plt.savefig("pointplot_grouped.png")
    plt.close()
    
    print("点图绘制完成")

# 6. 分类散点图
def stripplot():
    """分类散点图"""
    print("\n=== 分类散点图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本分类散点图
    plt.figure(figsize=(8, 6))
    sns.stripplot(x="day", y="total_bill", data=tips)
    plt.title("Strip Plot: Total Bill by Day")
    plt.savefig("stripplot_basic.png")
    plt.close()
    
    # 分组分类散点图
    plt.figure(figsize=(8, 6))
    sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, jitter=True)
    plt.title("Strip Plot: Total Bill by Day and Gender")
    plt.savefig("stripplot_jitter.png")
    plt.close()
    
    print("分类散点图绘制完成")

# 7. 蜂群图
def swarmplot():
    """蜂群图"""
    print("\n=== 蜂群图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本蜂群图
    plt.figure(figsize=(8, 6))
    sns.swarmplot(x="day", y="total_bill", data=tips)
    plt.title("Swarm Plot: Total Bill by Day")
    plt.savefig("swarmplot_basic.png")
    plt.close()
    
    # 分组蜂群图
    plt.figure(figsize=(8, 6))
    sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
    plt.title("Swarm Plot: Total Bill by Day and Gender")
    plt.savefig("swarmplot_grouped.png")
    plt.close()
    
    print("蜂群图绘制完成")

# 主函数
def main():
    print("Seaborn Categorical Plots")
    print("=" * 50)
    
    # 运行所有示例
    barplot()
    countplot()
    boxplot()
    violinplot()
    pointplot()
    stripplot()
    swarmplot()
    
    print("\nAll categorical plots completed!")

if __name__ == "__main__":
    main()