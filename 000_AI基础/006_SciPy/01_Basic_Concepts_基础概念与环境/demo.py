#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy基础概念与环境
展示SciPy的基本概念、环境配置和简单示例
"""

import numpy as np
import scipy as sp
from scipy import constants
from scipy import special
from scipy import stats
import matplotlib.pyplot as plt

# 打印SciPy版本
print(f"SciPy版本: {sp.__version__}")
print(f"NumPy版本: {np.__version__}")

# 1. 常量
print("\n=== 常量 ===")
print(f"π: {constants.pi}")
print(f"e: {constants.e}")
print(f"光速: {constants.c}")
print(f"普朗克常数: {constants.h}")
print(f"阿伏伽德罗常数: {constants.N_A}")
print(f"玻尔兹曼常数: {constants.k}")

# 2. 特殊函数
print("\n=== 特殊函数 ===")
print(f"伽马函数 Γ(5): {special.gamma(5)}")
print(f"贝塞尔函数 J0(0): {special.j0(0)}")
print(f"误差函数 erf(1): {special.erf(1)}")
print(f"正弦积分 Si(1): {special.sici(1)[0]}")

# 3. 基本数组操作
print("\n=== 基本数组操作 ===")
# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(f"原始数组: {arr}")
print(f"数组均值: {np.mean(arr)}")
print(f"数组标准差: {np.std(arr)}")
print(f"数组求和: {np.sum(arr)}")

# 4. 线性代数基础
print("\n=== 线性代数基础 ===")
# 创建矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"矩阵A:\n{A}")
print(f"矩阵B:\n{B}")
print(f"矩阵加法 A + B:\n{A + B}")
print(f"矩阵乘法 A @ B:\n{A @ B}")
print(f"矩阵行列式 det(A): {np.linalg.det(A)}")
print(f"矩阵逆 inv(A):\n{np.linalg.inv(A)}")

# 5. 统计函数
print("\n=== 统计函数 ===")
# 创建随机数据
np.random.seed(42)
data = np.random.normal(0, 1, 1000)
print(f"数据均值: {np.mean(data)}")
print(f"数据中位数: {np.median(data)}")
print(f"数据标准差: {np.std(data)}")
print(f"数据最大值: {np.max(data)}")
print(f"数据最小值: {np.min(data)}")

# 6. 可视化
print("\n=== 可视化 ===")
# 绘制正态分布
x = np.linspace(-3, 3, 100)
y = stats.norm.pdf(x)
plt.plot(x, y)
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid(True)
plt.savefig('normal_distribution.png')
print("正态分布图已保存为 normal_distribution.png")

# 7. 积分示例
print("\n=== 积分示例 ===")
def f(x):
    return x ** 2

from scipy import integrate
result, error = integrate.quad(f, 0, 1)
print(f"积分结果 ∫0^1 x² dx: {result}")
print(f"积分误差: {error}")

# 8. 优化示例
print("\n=== 优化示例 ===")
def f(x):
    return x ** 2 + 10 * np.sin(x)

from scipy import optimize
min_result = optimize.minimize(f, x0=0)
print(f"函数 f(x) = x² + 10sin(x) 的最小值点: {min_result.x[0]}")
print(f"最小值: {min_result.fun}")

# 9. 插值示例
print("\n=== 插值示例 ===")
x = np.linspace(0, 10, 10)
y = np.sin(x)

from scipy import interpolate
f = interpolate.interp1d(x, y)
x_new = np.linspace(0, 10, 100)
y_new = f(x_new)

plt.plot(x, y, 'o', label='原始数据')
plt.plot(x_new, y_new, '-', label='插值数据')
plt.title('Interpolation Example')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.savefig('interpolation_example.png')
print("插值示例图已保存为 interpolation_example.png")

# 10. 信号处理示例
print("\n=== 信号处理示例 ===")
t = np.linspace(0, 1, 1000)
freq = 5
x = np.sin(2 * np.pi * freq * t)

from scipy import signal
# 添加噪声
noise = np.random.normal(0, 0.1, x.shape)
x_noisy = x + noise

# 低通滤波
b, a = signal.butter(4, 0.1, 'low')
x_filtered = signal.filtfilt(b, a, x_noisy)

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.subplot(3, 1, 2)
plt.plot(t, x_noisy)
plt.title('Noisy Signal')
plt.subplot(3, 1, 3)
plt.plot(t, x_filtered)
plt.title('Filtered Signal')
plt.tight_layout()
plt.savefig('signal_processing_example.png')
print("信号处理示例图已保存为 signal_processing_example.png")

print("\nSciPy基础概念与环境示例完成！")
