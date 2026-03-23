#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn统计图形
展示Seaborn中各种统计图形的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 热力图
def heatmap():
    """热力图"""
    print("\n=== 热力图 ===")
    
    # 创建相关矩阵
    np.random.seed(42)
    data = np.random.randn(10, 10)
    corr = np.corrcoef(data)
    
    # 绘制热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", square=True)
    plt.title("Heatmap: Correlation Matrix")
    plt.savefig("heatmap_corr.png")
    plt.close()
    
    # 加载数据集
    flights = sns.load_dataset("flights")
    flights_pivot = flights.pivot("month", "year", "passengers")
    
    # 绘制航班数据热力图
    plt.figure(figsize=(10, 6))
    sns.heatmap(flights_pivot, cmap="YlGnBu", linewidths=0.5)
    plt.title("Heatmap: Flight Passengers")
    plt.savefig("heatmap_flights.png")
    plt.close()
    
    print("热力图绘制完成")

# 2. 散点图矩阵
def pairplot():
    """散点图矩阵"""
    print("\n=== 散点图矩阵 ===")
    
    # 加载数据集
    iris = sns.load_dataset("iris")
    
    # 绘制散点图矩阵
    g = sns.pairplot(iris, hue="species")
    g.fig.suptitle("Pairplot: Iris Dataset", y=1.02)
    plt.savefig("pairplot_iris.png")
    plt.close()
    
    print("散点图矩阵绘制完成")

# 3. 联合分布图
def jointplot():
    """联合分布图"""
    print("\n=== 联合分布图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 绘制联合分布图
    g = sns.jointplot(x="total_bill", y="tip", data=tips)
    g.fig.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
    plt.savefig("jointplot_basic.png")
    plt.close()
    
    # 带密度曲线的联合分布图
    g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
    g.fig.suptitle("Jointplot with KDE", y=1.02)
    plt.savefig("jointplot_kde.png")
    plt.close()
    
    print("联合分布图绘制完成")

# 4. 回归图
def regplot():
    """回归图"""
    print("\n=== 回归图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 绘制回归图
    plt.figure(figsize=(8, 6))
    sns.regplot(x="total_bill", y="tip", data=tips)
    plt.title("Regression Plot: Total Bill vs Tip")
    plt.savefig("regplot_basic.png")
    plt.close()
    
    # 带置信区间的回归图
    plt.figure(figsize=(8, 6))
    sns.regplot(x="total_bill", y="tip", data=tips, ci=95)
    plt.title("Regression Plot with Confidence Interval")
    plt.savefig("regplot_ci.png")
    plt.close()
    
    print("回归图绘制完成")

# 5. 分类图
def catplot():
    """分类图"""
    print("\n=== 分类图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 绘制分类图
    g = sns.catplot(x="day", y="total_bill", data=tips, kind="box")
    g.fig.suptitle("Catplot: Total Bill by Day", y=1.02)
    plt.savefig("catplot_box.png")
    plt.close()
    
    # 绘制分组分类图
    g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="bar")
    g.fig.suptitle("Catplot: Total Bill by Day and Gender", y=1.02)
    plt.savefig("catplot_bar.png")
    plt.close()
    
    print("分类图绘制完成")

# 6. 小提琴图
def violinplot():
    """小提琴图"""
    print("\n=== 小提琴图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 绘制小提琴图
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
    print("Seaborn Statistical Plots")
    print("=" * 50)
    
    # 运行所有示例
    heatmap()
    pairplot()
    jointplot()
    regplot()
    catplot()
    violinplot()
    
    print("\nAll statistical plots completed!")

if __name__ == "__main__":
    main()