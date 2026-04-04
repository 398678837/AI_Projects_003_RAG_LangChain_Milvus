#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn回归图形
展示Seaborn中各种回归图形的绘制方法
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 基本回归图
def regplot():
    """基本回归图"""
    print("\n=== 基本回归图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 基本回归图
    plt.figure(figsize=(8, 6))
    sns.regplot(x="total_bill", y="tip", data=tips)
    plt.title("Regression Plot: Total Bill vs Tip")
    plt.savefig("regplot_basic.png")
    plt.close()
    
    # 带置信区间的回归图
    plt.figure(figsize=(8, 6))
    sns.regplot(x="total_bill", y="tip", data=tips, ci=95)
    plt.title("Regression Plot with 95% Confidence Interval")
    plt.savefig("regplot_ci.png")
    plt.close()
    
    # 带分组的回归图
    plt.figure(figsize=(8, 6))
    sns.regplot(x="total_bill", y="tip", data=tips, hue="sex")
    plt.title("Regression Plot: Total Bill vs Tip by Gender")
    plt.savefig("regplot_hue.png")
    plt.close()
    
    print("基本回归图绘制完成")

# 2. 拟合不同类型的回归模型
def regplot_models():
    """拟合不同类型的回归模型"""
    print("\n=== 拟合不同类型的回归模型 ===")
    
    # 生成数据
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.2, 100)
    data = pd.DataFrame({"x": x, "y": y})
    
    # 线性回归
    plt.figure(figsize=(8, 6))
    sns.regplot(x="x", y="y", data=data, order=1)
    plt.title("Linear Regression")
    plt.savefig("regplot_linear.png")
    plt.close()
    
    # 多项式回归
    plt.figure(figsize=(8, 6))
    sns.regplot(x="x", y="y", data=data, order=3)
    plt.title("Polynomial Regression (Order 3)")
    plt.savefig("regplot_polynomial.png")
    plt.close()
    
    print("不同类型的回归模型拟合完成")

# 3. 残差图
def residualplot():
    """残差图"""
    print("\n=== 残差图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 残差图
    plt.figure(figsize=(8, 6))
    sns.residplot(x="total_bill", y="tip", data=tips)
    plt.title("Residual Plot: Total Bill vs Tip")
    plt.savefig("residplot_basic.png")
    plt.close()
    
    print("残差图绘制完成")

# 4. 联合回归图
def jointregplot():
    """联合回归图"""
    print("\n=== 联合回归图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 联合回归图
    g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    g.fig.suptitle("Joint Regression Plot: Total Bill vs Tip", y=1.02)
    plt.savefig("jointplot_reg.png")
    plt.close()
    
    print("联合回归图绘制完成")

# 5. 分类回归图
def catplot_reg():
    """分类回归图"""
    print("\n=== 分类回归图 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 分类回归图
    g = sns.catplot(x="day", y="total_bill", data=tips, kind="point")
    g.fig.suptitle("Categorical Regression Plot: Total Bill by Day", y=1.02)
    plt.savefig("catplot_point.png")
    plt.close()
    
    print("分类回归图绘制完成")

# 6. 复杂回归模型
def complex_regression():
    """复杂回归模型"""
    print("\n=== 复杂回归模型 ===")
    
    # 加载数据集
    tips = sns.load_dataset("tips")
    
    # 带多个预测变量的回归图
    plt.figure(figsize=(10, 8))
    g = sns.lmplot(x="total_bill", y="tip", hue="sex", col="time", data=tips)
    g.fig.suptitle("Complex Regression: Total Bill vs Tip by Gender and Time", y=1.02)
    plt.savefig("lmplot_complex.png")
    plt.close()
    
    print("复杂回归模型绘制完成")

# 主函数
def main():
    print("Seaborn Regression Plots")
    print("=" * 50)
    
    # 运行所有示例
    regplot()
    regplot_models()
    residualplot()
    jointregplot()
    catplot_reg()
    complex_regression()
    
    print("\nAll regression plots completed!")

if __name__ == "__main__":
    main()