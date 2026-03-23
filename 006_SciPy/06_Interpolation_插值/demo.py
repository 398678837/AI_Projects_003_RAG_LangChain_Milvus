#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy插值
展示SciPy的插值功能
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# 1. 一维插值
print("=== 一维插值 ===")

# 创建原始数据
x = np.linspace(0, 10, 10)
y = np.sin(x)

print(f"原始数据点数量: {len(x)}")
print(f"原始x值: {x}")
print(f"原始y值: {y}")

# 创建插值函数
f_linear = interpolate.interp1d(x, y, kind='linear')
f_cubic = interpolate.interp1d(x, y, kind='cubic')

# 创建新的x值
x_new = np.linspace(0, 10, 100)

# 计算插值结果
y_linear = f_linear(x_new)
y_cubic = f_cubic(x_new)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='原始数据')
plt.plot(x_new, y_linear, 'r-', label='线性插值')
plt.plot(x_new, y_cubic, 'g-', label='三次样条插值')
plt.plot(x_new, np.sin(x_new), 'b--', label='真实函数')
plt.title('一维插值示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('interpolation_1d.png')
print("一维插值图已保存为 interpolation_1d.png")

# 2. 二维插值
print("\n=== 二维插值 ===")

# 创建二维网格数据
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

print(f"原始数据网格大小: {z.shape}")

# 创建插值函数
f_2d = interpolate.interp2d(x[0], y[:, 0], z, kind='cubic')

# 创建新的网格
x_new = np.linspace(-5, 5, 100)
y_new = np.linspace(-5, 5, 100)
z_new = f_2d(x_new, y_new)

# 绘制结果
fig = plt.figure(figsize=(12, 10))

ax1 = fig.add_subplot(221, projection='3d')
ax1.scatter(x, y, z, label='原始数据')
ax1.set_title('原始数据')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax2 = fig.add_subplot(222, projection='3d')
x_new_grid, y_new_grid = np.meshgrid(x_new, y_new)
ax2.plot_surface(x_new_grid, y_new_grid, z_new, cmap='viridis')
ax2.set_title('二维插值')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

ax3 = fig.add_subplot(223)
ax3.contourf(x, y, z)
ax3.set_title('原始数据等高线')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

ax4 = fig.add_subplot(224)
ax4.contourf(x_new_grid, y_new_grid, z_new)
ax4.set_title('插值数据等高线')
ax4.set_xlabel('x')
ax4.set_ylabel('y')

plt.tight_layout()
plt.savefig('interpolation_2d.png')
print("二维插值图已保存为 interpolation_2d.png")

# 3. 样条插值
print("\n=== 样条插值 ===")

# 创建数据
x = np.linspace(0, 10, 20)
y = np.sin(x) + np.random.normal(0, 0.1, size=len(x))

print(f"样条插值数据点数量: {len(x)}")

# 创建样条插值
# 三次样条
cs = interpolate.CubicSpline(x, y)
# 二次样条
qs = interpolate.UnivariateSpline(x, y, k=2)

# 创建新的x值
x_new = np.linspace(0, 10, 100)

# 计算插值结果
y_cubic = cs(x_new)
y_quadratic = qs(x_new)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='原始数据')
plt.plot(x_new, y_cubic, 'r-', label='三次样条插值')
plt.plot(x_new, y_quadratic, 'g-', label='二次样条插值')
plt.plot(x_new, np.sin(x_new), 'b--', label='真实函数')
plt.title('样条插值示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('spline_interpolation.png')
print("样条插值图已保存为 spline_interpolation.png")

# 4. 径向基函数插值
print("\n=== 径向基函数插值 ===")

# 创建数据
x = np.linspace(-10, 10, 20)
y = np.sin(x)

print(f"径向基函数插值数据点数量: {len(x)}")

# 创建径向基函数插值
rbf = interpolate.Rbf(x, y, function='gaussian')

# 创建新的x值
x_new = np.linspace(-10, 10, 100)

# 计算插值结果
y_rbf = rbf(x_new)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='原始数据')
plt.plot(x_new, y_rbf, 'r-', label='径向基函数插值')
plt.plot(x_new, np.sin(x_new), 'b--', label='真实函数')
plt.title('径向基函数插值示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('rbf_interpolation.png')
print("径向基函数插值图已保存为 rbf_interpolation.png")

# 5. 插值误差分析
print("\n=== 插值误差分析 ===")

# 创建测试数据
x_test = np.linspace(0, 10, 100)
y_true = np.sin(x_test)

# 计算不同插值方法的误差
y_linear_error = np.abs(y_linear - y_true)
y_cubic_error = np.abs(y_cubic - y_true)
y_rbf_error = np.abs(rbf(x_test) - y_true)

print(f"线性插值平均误差: {np.mean(y_linear_error):.6f}")
print(f"三次样条插值平均误差: {np.mean(y_cubic_error):.6f}")
print(f"径向基函数插值平均误差: {np.mean(y_rbf_error):.6f}")

# 绘制误差
plt.figure(figsize=(10, 6))
plt.plot(x_test, y_linear_error, 'r-', label='线性插值误差')
plt.plot(x_test, y_cubic_error, 'g-', label='三次样条插值误差')
plt.plot(x_test, y_rbf_error, 'b-', label='径向基函数插值误差')
plt.title('不同插值方法的误差')
plt.xlabel('x')
plt.ylabel('误差')
plt.legend()
plt.grid(True)
plt.savefig('interpolation_error.png')
print("插值误差图已保存为 interpolation_error.png")

# 6. 不规则数据插值
print("\n=== 不规则数据插值 ===")

# 创建不规则数据
np.random.seed(42)
x_irr = np.random.uniform(-5, 5, 50)
y_irr = np.random.uniform(-5, 5, 50)
z_irr = np.sin(np.sqrt(x_irr**2 + y_irr**2))

print(f"不规则数据点数量: {len(x_irr)}")

# 创建网格
xi = np.linspace(-5, 5, 100)
yi = np.linspace(-5, 5, 100)
xi, yi = np.meshgrid(xi, yi)

# 使用griddata进行插值
zi_linear = interpolate.griddata((x_irr, y_irr), z_irr, (xi, yi), method='linear')
zi_cubic = interpolate.griddata((x_irr, y_irr), z_irr, (xi, yi), method='cubic')
zi_nearest = interpolate.griddata((x_irr, y_irr), z_irr, (xi, yi), method='nearest')

# 绘制结果
fig = plt.figure(figsize=(15, 10))

ax1 = fig.add_subplot(221)
ax1.scatter(x_irr, y_irr, c=z_irr, cmap='viridis')
ax1.set_title('原始不规则数据')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2 = fig.add_subplot(222)
ax2.contourf(xi, yi, zi_linear, cmap='viridis')
ax2.set_title('线性插值')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax3 = fig.add_subplot(223)
ax3.contourf(xi, yi, zi_cubic, cmap='viridis')
ax3.set_title('三次插值')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

ax4 = fig.add_subplot(224)
ax4.contourf(xi, yi, zi_nearest, cmap='viridis')
ax4.set_title('最近邻插值')
ax4.set_xlabel('x')
ax4.set_ylabel('y')

plt.tight_layout()
plt.savefig('irregular_interpolation.png')
print("不规则数据插值图已保存为 irregular_interpolation.png")

print("\nSciPy插值示例完成！")
