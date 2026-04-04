#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy统计函数
展示SciPy的统计函数功能
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 设置随机种子
np.random.seed(42)

# 1. 描述性统计
print("=== 描述性统计 ===")

# 创建随机数据
data = np.random.normal(100, 15, 1000)
print(f"数据均值: {np.mean(data)}")
print(f"数据中位数: {np.median(data)}")
print(f"数据标准差: {np.std(data)}")
print(f"数据方差: {np.var(data)}")
print(f"数据最小值: {np.min(data)}")
print(f"数据最大值: {np.max(data)}")
print(f"数据四分位数: {np.percentile(data, [25, 50, 75])}")

# 2. 概率分布
print("\n=== 概率分布 ===")

# 正态分布
print("\n正态分布:")
norm_dist = stats.norm(loc=0, scale=1)  # 均值为0，标准差为1的正态分布
print(f"正态分布在x=0处的概率密度: {norm_dist.pdf(0)}")
print(f"正态分布在x=0处的累积概率: {norm_dist.cdf(0)}")
print(f"正态分布的分位数（0.5）: {norm_dist.ppf(0.5)}")

# 生成正态分布随机数
norm_rvs = norm_dist.rvs(size=1000)
print(f"正态分布随机数的均值: {np.mean(norm_rvs)}")
print(f"正态分布随机数的标准差: {np.std(norm_rvs)}")

# 二项分布
print("\n二项分布:")
binom_dist = stats.binom(n=10, p=0.5)  # n=10次试验，成功概率p=0.5
print(f"二项分布在k=5处的概率质量: {binom_dist.pmf(5)}")
print(f"二项分布在k=5处的累积概率: {binom_dist.cdf(5)}")

# 泊松分布
print("\n泊松分布:")
poisson_dist = stats.poisson(mu=3)  # 均值为3的泊松分布
print(f"泊松分布在k=3处的概率质量: {poisson_dist.pmf(3)}")
print(f"泊松分布在k=3处的累积概率: {poisson_dist.cdf(3)}")

# 3. 假设检验
print("\n=== 假设检验 ===")

# t检验
print("\nt检验:")
# 生成两个正态分布样本
sample1 = np.random.normal(100, 15, 100)
sample2 = np.random.normal(105, 15, 100)

# 独立样本t检验
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print(f"t统计量: {t_stat}")
print(f"p值: {p_value}")
print(f"是否拒绝原假设（α=0.05）: {p_value < 0.05}")

# 配对样本t检验
sample3 = np.random.normal(100, 15, 100)
sample4 = sample3 + np.random.normal(5, 10, 100)
t_stat_paired, p_value_paired = stats.ttest_rel(sample3, sample4)
print(f"\n配对样本t检验:")
print(f"t统计量: {t_stat_paired}")
print(f"p值: {p_value_paired}")
print(f"是否拒绝原假设（α=0.05）: {p_value_paired < 0.05}")

# 卡方检验
print("\n卡方检验:")
# 观察频数
observed = np.array([10, 20, 30, 40])
# 期望频数
expected = np.array([25, 25, 25, 25])
chi2_stat, chi2_p_value = stats.chisquare(observed, expected)
print(f"卡方统计量: {chi2_stat}")
print(f"p值: {chi2_p_value}")
print(f"是否拒绝原假设（α=0.05）: {chi2_p_value < 0.05}")

# 4. 相关分析
print("\n=== 相关分析 ===")

# 生成两个相关的变量
x = np.random.normal(100, 15, 100)
y = x + np.random.normal(0, 10, 100)

# 皮尔逊相关系数
pearson_corr, pearson_p_value = stats.pearsonr(x, y)
print(f"皮尔逊相关系数: {pearson_corr}")
print(f"p值: {pearson_p_value}")

# 斯皮尔曼相关系数
spearman_corr, spearman_p_value = stats.spearmanr(x, y)
print(f"斯皮尔曼相关系数: {spearman_corr}")
print(f"p值: {spearman_p_value}")

# 肯德尔相关系数
kendall_corr, kendall_p_value = stats.kendalltau(x, y)
print(f"肯德尔相关系数: {kendall_corr}")
print(f"p值: {kendall_p_value}")

# 5. 分布拟合
print("\n=== 分布拟合 ===")

# 拟合正态分布
norm_params = stats.norm.fit(data)
print(f"正态分布拟合参数（均值, 标准差）: {norm_params}")

# 拟合指数分布
exp_params = stats.expon.fit(data)
print(f"指数分布拟合参数（位置, 尺度）: {exp_params}")

# 6. 统计检验
print("\n=== 统计检验 ===")

# 正态性检验（Shapiro-Wilk检验）
shapiro_stat, shapiro_p_value = stats.shapiro(data)
print(f"Shapiro-Wilk正态性检验:")
print(f"统计量: {shapiro_stat}")
print(f"p值: {shapiro_p_value}")
print(f"数据是否符合正态分布（α=0.05）: {shapiro_p_value > 0.05}")

# 方差齐性检验（Levene检验）
levene_stat, levene_p_value = stats.levene(sample1, sample2)
print(f"\nLevene方差齐性检验:")
print(f"统计量: {levene_stat}")
print(f"p值: {levene_p_value}")
print(f"方差是否齐性（α=0.05）: {levene_p_value > 0.05}")

# 7. 可视化
print("\n=== 可视化 ===")

# 直方图和正态分布拟合
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='数据直方图')

# 绘制拟合的正态分布曲线
x_range = np.linspace(min(data), max(data), 100)
norm_pdf = stats.norm.pdf(x_range, *norm_params)
plt.plot(x_range, norm_pdf, 'r-', lw=2, label='拟合的正态分布')

plt.title('数据直方图与正态分布拟合')
plt.xlabel('值')
plt.ylabel('密度')
plt.legend()
plt.grid(True)
plt.savefig('normal_fit.png')
print("正态分布拟合图已保存为 normal_fit.png")

# 箱线图
plt.figure(figsize=(10, 6))
plt.boxplot([sample1, sample2], labels=['样本1', '样本2'])
plt.title('箱线图')
plt.ylabel('值')
plt.grid(True)
plt.savefig('boxplot.png')
print("箱线图已保存为 boxplot.png")

# 散点图和相关性
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6)
plt.title(f'散点图（皮尔逊相关系数: {pearson_corr:.3f}）')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('scatter_plot.png')
print("散点图已保存为 scatter_plot.png")

print("\nSciPy统计函数示例完成！")
