#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn热力图
展示Seaborn中热力图的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 基本热力图
def basic_heatmap():
    """基本热力图"""
    print("\n=== 基本热力图 ===")
    
    # 创建随机数据
    np.random.seed(42)
    data = np.random.rand(10, 10)
    
    # 基本热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(data)
    plt.title("Basic Heatmap")
    plt.savefig("heatmap_basic.png")
    plt.close()
    
    # 带数值标注的热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, annot=True, fmt=".2f")
    plt.title("Heatmap with Annotations")
    plt.savefig("heatmap_annot.png")
    plt.close()
    
    print("基本热力图绘制完成")

# 2. 相关矩阵热力图
def correlation_heatmap():
    """相关矩阵热力图"""
    print("\n=== 相关矩阵热力图 ===")
    
    # 加载数据集
    iris = sns.load_dataset("iris")
    corr = iris.corr()
    
    # 相关矩阵热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix Heatmap")
    plt.savefig("heatmap_correlation.png")
    plt.close()
    
    print("相关矩阵热力图绘制完成")

# 3. 分类数据热力图
def categorical_heatmap():
    """分类数据热力图"""
    print("\n=== 分类数据热力图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 创建透视表
    pivot = tips.pivot_table(index="day", columns="time", values="total_bill", aggfunc="mean")
    
    # 分类数据热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title("Categorical Data Heatmap")
    plt.savefig("heatmap_categorical.png")
    plt.close()
    
    print("分类数据热力图绘制完成")

# 4. 时间序列热力图
def timeseries_heatmap():
    """时间序列热力图"""
    print("\n=== 时间序列热力图 ===")
    
    # 加载数据集
    flights = sns.load_dataset("flights")
    flights_pivot = flights.pivot("month", "year", "passengers")
    
    # 时间序列热力图
    plt.figure(figsize=(10, 6))
    sns.heatmap(flights_pivot, cmap="YlGnBu", linewidths=0.5)
    plt.title("Time Series Heatmap: Flight Passengers")
    plt.savefig("heatmap_timeseries.png")
    plt.close()
    
    print("时间序列热力图绘制完成")

# 5. 自定义热力图
def custom_heatmap():
    """自定义热力图"""
    print("\n=== 自定义热力图 ===")
    
    # 创建随机数据
    np.random.seed(42)
    data = np.random.rand(10, 10)
    
    # 自定义热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, 
                cmap="viridis",
                annot=True,
                fmt=".2f",
                linewidths=0.5,
                linecolor="white",
                cbar_kws={"label": "Value"})
    plt.title("Custom Heatmap")
    plt.savefig("heatmap_custom.png")
    plt.close()
    
    print("自定义热力图绘制完成")

# 6. 聚类热力图
def cluster_heatmap():
    """聚类热力图"""
    print("\n=== 聚类热力图 ===")
    
    # 加载数据集
    iris = sns.load_dataset("iris")
    
    # 聚类热力图
    plt.figure(figsize=(10, 8))
    g = sns.clustermap(iris.drop("species", axis=1), cmap="coolwarm")
    g.fig.suptitle("Cluster Heatmap: Iris Dataset", y=1.02)
    plt.savefig("heatmap_cluster.png")
    plt.close()
    
    print("聚类热力图绘制完成")

# 主函数
def main():
    print("Seaborn Heatmaps")
    print("=" * 50)
    
    # 运行所有示例
    basic_heatmap()
    correlation_heatmap()
    categorical_heatmap()
    timeseries_heatmap()
    custom_heatmap()
    cluster_heatmap()
    
    print("\nAll heatmaps completed!")

if __name__ == "__main__":
    main()