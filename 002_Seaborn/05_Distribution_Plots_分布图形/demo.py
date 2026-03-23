#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn分布图形
展示Seaborn中各种分布图形的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 直方图
def histogram():
    """直方图"""
    print("\n=== 直方图 ===")
    
    # 生成随机数据
    np.random.seed(42)
    data = np.random.normal(size=1000)
    
    # 基本直方图
    plt.figure(figsize=(8, 6))
    sns.histplot(data)
    plt.title("Histogram: Normal Distribution")
    plt.savefig("histplot_basic.png")
    plt.close()
    
    # 带密度曲线的直方图
    plt.figure(figsize=(8, 6))
    sns.histplot(data, kde=True)
    plt.title("Histogram with KDE")
    plt.savefig("histplot_kde.png")
    plt.close()
    
    # 分组直方图
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(8, 6))
    sns.histplot(data=tips, x="total_bill", hue="sex")
    plt.title("Histogram: Total Bill by Gender")
    plt.savefig("histplot_grouped.png")
    plt.close()
    
    print("直方图绘制完成")

# 2. 核密度估计图
def kdeplot():
    """核密度估计图"""
    print("\n=== 核密度估计图 ===")
    
    # 生成随机数据
    np.random.seed(42)
    data = np.random.normal(size=1000)
    
    # 基本核密度估计图
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data)
    plt.title("KDE Plot: Normal Distribution")
    plt.savefig("kdeplot_basic.png")
    plt.close()
    
    # 填充核密度估计图
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data, fill=True)
    plt.title("KDE Plot with Fill")
    plt.savefig("kdeplot_fill.png")
    plt.close()
    
    # 分组核密度估计图
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=tips, x="total_bill", hue="sex")
    plt.title("KDE Plot: Total Bill by Gender")
    plt.savefig("kdeplot_grouped.png")
    plt.close()
    
    print("核密度估计图绘制完成")

# 3. 经验累积分布函数图
def ecdfplot():
    """经验累积分布函数图"""
    print("\n=== 经验累积分布函数图 ===")
    
    # 生成随机数据
    np.random.seed(42)
    data = np.random.normal(size=1000)
    
    # 基本经验累积分布函数图
    plt.figure(figsize=(8, 6))
    sns.ecdfplot(data)
    plt.title("ECDF Plot: Normal Distribution")
    plt.savefig("ecdfplot_basic.png")
    plt.close()
    
    # 分组经验累积分布函数图
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(8, 6))
    sns.ecdfplot(data=tips, x="total_bill", hue="sex")
    plt.title("ECDF Plot: Total Bill by Gender")
    plt.savefig("ecdfplot_grouped.png")
    plt.close()
    
    print("经验累积分布函数图绘制完成")

# 4. 双变量分布
def jointplot():
    """双变量分布"""
    print("\n=== 双变量分布 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本双变量分布
    g = sns.jointplot(x="total_bill", y="tip", data=tips)
    g.fig.suptitle("Joint Plot: Total Bill vs Tip", y=1.02)
    plt.savefig("jointplot_basic.png")
    plt.close()
    
    # 带密度曲线的双变量分布
    g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
    g.fig.suptitle("Joint Plot with KDE", y=1.02)
    plt.savefig("jointplot_kde.png")
    plt.close()
    
    # 带直方图的双变量分布
    g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hist")
    g.fig.suptitle("Joint Plot with Histograms", y=1.02)
    plt.savefig("jointplot_hist.png")
    plt.close()
    
    print("双变量分布绘制完成")

# 5. 多变量分布
def pairplot():
    """多变量分布"""
    print("\n=== 多变量分布 ===")
    
    # 加载数据集
    iris = sns.load_dataset("iris")
    
    # 基本多变量分布
    g = sns.pairplot(iris)
    g.fig.suptitle("Pair Plot: Iris Dataset", y=1.02)
    plt.savefig("pairplot_basic.png")
    plt.close()
    
    # 带分类的多变量分布
    g = sns.pairplot(iris, hue="species")
    g.fig.suptitle("Pair Plot: Iris Dataset by Species", y=1.02)
    plt.savefig("pairplot_hue.png")
    plt.close()
    
    print("多变量分布绘制完成")

# 6. 小提琴图
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

# 主函数
def main():
    print("Seaborn Distribution Plots")
    print("=" * 50)
    
    # 运行所有示例
    histogram()
    kdeplot()
    ecdfplot()
    jointplot()
    pairplot()
    violinplot()
    
    print("\nAll distribution plots completed!")

if __name__ == "__main__":
    main()