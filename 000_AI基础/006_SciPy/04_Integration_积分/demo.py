#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy积分
展示SciPy的积分功能
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# 1. 一维积分
print("=== 一维积分 ===")

# 定义被积函数
def f(x):
    return x ** 2

# 使用quad进行数值积分
result, error = integrate.quad(f, 0, 1)
print(f"积分结果 ∫0^1 x² dx: {result}")
print(f"积分误差: {error}")
print(f"理论值: 0.3333333333333333")

# 另一个示例：高斯函数积分
def gaussian(x):
    return np.exp(-x ** 2)

result_gaussian, error_gaussian = integrate.quad(gaussian, -np.inf, np.inf)
print(f"\n高斯函数积分 ∫-∞^∞ e^(-x²) dx: {result_gaussian}")
print(f"积分误差: {error_gaussian}")
print(f"理论值: {np.sqrt(np.pi)}")

# 2. 二重积分
print("\n=== 二重积分 ===")

# 定义二元被积函数
def f2d(x, y):
    return x * y

# 使用dblquad进行二重积分
result_2d, error_2d = integrate.dblquad(f2d, 0, 1, lambda x: 0, lambda x: 1)
print(f"二重积分 ∫0^1 ∫0^1 xy dy dx: {result_2d}")
print(f"积分误差: {error_2d}")
print(f"理论值: 0.25")

# 3. 三重积分
print("\n=== 三重积分 ===")

# 定义三元被积函数
def f3d(x, y, z):
    return x * y * z

# 使用tplquad进行三重积分
result_3d, error_3d = integrate.tplquad(f3d, 0, 1, lambda x: 0, lambda x: 1, lambda x, y: 0, lambda x, y: 1)
print(f"三重积分 ∫0^1 ∫0^1 ∫0^1 xyz dz dy dx: {result_3d}")
print(f"积分误差: {error_3d}")
print(f"理论值: 0.125")

# 4. 固定步长积分
print("\n=== 固定步长积分 ===")

# 创建样本点
x = np.linspace(0, 1, 100)
y = f(x)

# 使用trapezoid方法（梯形法则）
result_trapz = integrate.trapz(y, x)
print(f"梯形法则积分结果: {result_trapz}")

# 使用simpson方法（辛普森法则）
result_simps = integrate.simps(y, x)
print(f"辛普森法则积分结果: {result_simps}")

# 5. 常微分方程（ODE）求解
print("\n=== 常微分方程（ODE）求解 ===")

# 定义ODE系统
def ode_system(t, y):
    return -2 * y

# 初始条件
y0 = [1.0]

# 时间点
t_span = (0, 5)
t_eval = np.linspace(0, 5, 100)

# 使用solve_ivp求解ODE
solution = integrate.solve_ivp(ode_system, t_span, y0, t_eval=t_eval)

# 打印结果
print(f"ODE求解结果（t=5）: {solution.y[0][-1]}")
print(f"理论值: {np.exp(-10)}")

# 可视化ODE解
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], 'b-', label='数值解')
plt.plot(solution.t, np.exp(-2 * solution.t), 'r--', label='解析解')
plt.title('常微分方程求解')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('ode_solution.png')
print("ODE解可视化图已保存为 ode_solution.png")

# 6. 偏微分方程（PDE）求解示例
print("\n=== 偏微分方程（PDE）求解示例 ===")

# 这里展示一个简单的热传导方程求解
# 热传导方程: ∂u/∂t = α ∂²u/∂x²

def heat_eqn(t, u, alpha, dx):
    """热传导方程的有限差分近似"""
    d2u_dx2 = np.zeros_like(u)
    d2u_dx2[1:-1] = (u[2:] - 2*u[1:-1] + u[:-2]) / dx**2
    # 边界条件
    d2u_dx2[0] = (u[1] - 2*u[0] + u[0]) / dx**2  # u(0,t) = 0
    d2u_dx2[-1] = (u[-1] - 2*u[-1] + u[-2]) / dx**2  # u(L,t) = 0
    return alpha * d2u_dx2

# 初始条件和参数
L = 1.0  # 杆长
N = 100  # 空间网格数
dx = L / (N - 1)
x = np.linspace(0, L, N)

# 初始温度分布（高斯分布）
u0 = np.exp(-50 * (x - 0.5)**2)

# 参数
alpha = 0.01  # 热扩散系数

# 时间范围
t_span = (0, 1.0)
t_eval = np.linspace(0, 1.0, 10)

# 求解PDE
solution_pde = integrate.solve_ivp(
    heat_eqn, t_span, u0, t_eval=t_eval, args=(alpha, dx)
)

# 可视化PDE解
plt.figure(figsize=(10, 6))
for i, t in enumerate(t_eval):
    plt.plot(x, solution_pde.y[:, i], label=f't={t:.2f}')
plt.title('热传导方程求解')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.legend()
plt.grid(True)
plt.savefig('heat_equation.png')
print("热传导方程解可视化图已保存为 heat_equation.png")

# 7. 积分变换
print("\n=== 积分变换 ===")

# 这里展示傅里叶变换的使用
from scipy.fft import fft, ifft

# 创建信号
t = np.linspace(0, 1, 1000)
freq = 5
x = np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

# 傅里叶变换
X = fft(x)
freqs = np.fft.fftfreq(len(t), t[1] - t[0])

# 逆傅里叶变换
x_reconstructed = ifft(X)

# 可视化
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('原始信号')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 1, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(X)[:len(X)//2])
plt.title('傅里叶变换')
plt.xlabel('频率')
plt.ylabel('幅度')

plt.subplot(3, 1, 3)
plt.plot(t, np.real(x_reconstructed))
plt.title('逆傅里叶变换')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.tight_layout()
plt.savefig('fourier_transform.png')
print("傅里叶变换可视化图已保存为 fourier_transform.png")

print("\nSciPy积分示例完成！")
