#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy实战应用
展示SciPy在实际应用中的使用
"""

import numpy as np
from scipy import stats, optimize, integrate, signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# 1. 物理模拟：弹簧-质量系统
print("=== 物理模拟：弹簧-质量系统 ===")

# 定义弹簧-质量系统的微分方程
def spring_mass_system(t, y, k, m, c):
    """弹簧-质量系统的微分方程：m*y'' + c*y' + k*y = 0"""
    y1, y2 = y  # y1 = 位移, y2 = 速度
    return [y2, -k/m * y1 - c/m * y2]

# 系统参数
k = 10.0  # 弹簧常数
m = 1.0   # 质量
c = 0.5   # 阻尼系数

# 初始条件 [位移, 速度]
y0 = [1.0, 0.0]

# 时间范围
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# 求解微分方程
from scipy.integrate import solve_ivp
solution = solve_ivp(spring_mass_system, t_span, y0, t_eval=t_eval, args=(k, m, c))

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='位移')
plt.plot(solution.t, solution.y[1], label='速度')
plt.title('弹簧-质量系统响应')
plt.xlabel('时间 (s)')
plt.ylabel('值')
plt.legend()
plt.grid(True)
plt.savefig('spring_mass_system.png')
print("弹簧-质量系统响应图已保存为 spring_mass_system.png")

# 2. 金融分析：投资组合优化
print("\n=== 金融分析：投资组合优化 ===")

# 生成资产收益率数据
np.random.seed(42)
num_assets = 3
num_observations = 1000

# 生成相关的收益率数据
mean_returns = np.array([0.001, 0.0008, 0.0012])
cov_matrix = np.array([[0.0001, 0.00005, 0.00003],
                       [0.00005, 0.00008, 0.00002],
                       [0.00003, 0.00002, 0.00012]])

# 生成随机收益率
returns = np.random.multivariate_normal(mean_returns, cov_matrix, num_observations)

# 定义投资组合收益和风险计算函数
def portfolio_performance(weights, mean_returns, cov_matrix):
    """计算投资组合的预期收益和风险"""
    returns = np.sum(mean_returns * weights) * 252  # 年化收益
    risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)  # 年化风险
    return returns, risk

# 定义投资组合优化目标函数（最小化风险）
def minimize_risk(weights, mean_returns, cov_matrix, target_return):
    """最小化投资组合风险"""
    returns, risk = portfolio_performance(weights, mean_returns, cov_matrix)
    # 惩罚函数，确保达到目标收益
    return risk + 100 * max(0, target_return - returns) ** 2

# 约束条件
constraints = (
    {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # 权重和为1
    {'type': 'ineq', 'fun': lambda x: x}  # 权重非负
)

# 边界条件
bounds = tuple((0, 1) for _ in range(num_assets))

# 初始权重
initial_weights = np.array([1/num_assets for _ in range(num_assets)])

# 目标收益列表
target_returns = np.linspace(0.1, 0.3, 20)

# 计算有效前沿
efficient_frontier = []
for target_return in target_returns:
    result = optimize.minimize(
        minimize_risk,
        initial_weights,
        args=(mean_returns, cov_matrix, target_return),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    if result.success:
        returns, risk = portfolio_performance(result.x, mean_returns, cov_matrix)
        efficient_frontier.append((risk, returns, result.x))

# 提取有效前沿数据
ef_risk = [point[0] for point in efficient_frontier]
ef_returns = [point[1] for point in efficient_frontier]

# 绘制有效前沿
plt.figure(figsize=(10, 6))
plt.plot(ef_risk, ef_returns, 'r-', label='有效前沿')
plt.title('投资组合有效前沿')
plt.xlabel('风险 (年化标准差)')
plt.ylabel('收益 (年化收益率)')
plt.legend()
plt.grid(True)
plt.savefig('efficient_frontier.png')
print("投资组合有效前沿图已保存为 efficient_frontier.png")

# 3. 图像处理：边缘检测
print("\n=== 图像处理：边缘检测 ===")

# 创建测试图像
from scipy import ndimage

# 创建一个简单的图像
image = np.zeros((100, 100))
image[25:75, 25:75] = 1  # 中心方块

# 添加噪声
noise = np.random.normal(0, 0.1, size=image.shape)
noisy_image = image + noise

# 使用Sobel算子进行边缘检测
sobel_x = ndimage.sobel(noisy_image, axis=0, mode='constant')
sobel_y = ndimage.sobel(noisy_image, axis=1, mode='constant')
edges = np.sqrt(sobel_x**2 + sobel_y**2)

# 绘制结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('原始图像')
plt.axis('off')

plt.subplot(132)
plt.imshow(noisy_image, cmap='gray')
plt.title('带噪声的图像')
plt.axis('off')

plt.subplot(133)
plt.imshow(edges, cmap='gray')
plt.title('边缘检测结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('edge_detection.png')
print("边缘检测结果图已保存为 edge_detection.png")

# 4. 信号处理：音频滤波
print("\n=== 信号处理：音频滤波 ===")

# 生成模拟音频信号
t = np.linspace(0, 1, 44100)  # 1秒音频，44.1kHz采样率

# 生成基频和谐波
fundamental_freq = 440  # A4音符
signal = np.sin(2 * np.pi * fundamental_freq * t)

# 添加谐波
harmonics = [2, 3, 4, 5]
for h in harmonics:
    signal += 0.5 / h * np.sin(2 * np.pi * h * fundamental_freq * t)

# 添加噪声
noise = np.random.normal(0, 0.1, size=signal.shape)
noisy_signal = signal + noise

# 设计低通滤波器
fs = 44100
cutoff = 2000  # 2kHz截止频率
order = 4
b, a = signal.butter(order, cutoff, fs=fs, btype='low')

# 应用滤波器
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# 绘制频谱
from scipy.fft import fft, fftfreq

N = len(t)
yf_noisy = fft(noisy_signal)
yf_filtered = fft(filtered_signal)
xf = fftfreq(N, 1/fs)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:1000], noisy_signal[:1000])
plt.title('带噪声的音频信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(3, 1, 2)
plt.plot(t[:1000], filtered_signal[:1000])
plt.title('滤波后的音频信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(3, 1, 3)
plt.plot(xf[:N//2], 2.0/N * np.abs(yf_noisy[:N//2]), label='带噪声的信号')
plt.plot(xf[:N//2], 2.0/N * np.abs(yf_filtered[:N//2]), 'r-', label='滤波后的信号')
plt.title('频谱分析')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')
plt.legend()
plt.xlim(0, 5000)

plt.tight_layout()
plt.savefig('audio_filtering.png')
print("音频滤波结果图已保存为 audio_filtering.png")

# 5. 数据分析：回归分析
print("\n=== 数据分析：回归分析 ===")

# 生成数据
x = np.linspace(0, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 2, size=len(x))

# 线性回归
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"线性回归结果:")
print(f"斜率: {slope:.4f}")
print(f"截距: {intercept:.4f}")
print(f"相关系数: {r_value:.4f}")
print(f"p值: {p_value:.4f}")
print(f"标准误差: {std_err:.4f}")

# 多项式回归
coefficients = np.polyfit(x, y, 2)  # 二次多项式
poly = np.poly1d(coefficients)

# 预测值
y_pred_linear = slope * x + intercept
y_pred_poly = poly(x)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='原始数据')
plt.plot(x, y_pred_linear, 'r-', label='线性回归')
plt.plot(x, y_pred_poly, 'g-', label='二次多项式回归')
plt.title('回归分析示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('regression_analysis.png')
print("回归分析结果图已保存为 regression_analysis.png")

# 6. 科学计算：积分应用
print("\n=== 科学计算：积分应用 ===")

# 计算正态分布的累积概率
def normal_pdf(x, mu=0, sigma=1):
    """正态分布概率密度函数"""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# 计算P(-1 ≤ X ≤ 1)
prob, error = integrate.quad(normal_pdf, -1, 1)
print(f"正态分布在[-1, 1]区间的概率: {prob:.4f}")
print(f"积分误差: {error:.4f}")
print(f"理论值: 0.6827")

# 7. 工程应用：结构分析
print("\n=== 工程应用：结构分析 ===")

# 定义梁的微分方程
def beam_deflection(x, y, E, I, w):
    """梁的挠度微分方程：E*I*y'' = -w*x^2/2"""
    return [y[1], -w * x**2 / (2 * E * I)]

# 梁的参数
E = 200e9  # 弹性模量 (Pa)
I = 1e-6   # 惯性矩 (m^4)
w = 1000   # 均布载荷 (N/m)

# 边界条件 [挠度, 转角]
y0 = [0, 0]  # 固定端

# 梁长
L = 1.0
t_span = (0, L)
t_eval = np.linspace(0, L, 100)

# 求解微分方程
solution = solve_ivp(beam_deflection, t_span, y0, t_eval=t_eval, args=(E, I, w))

# 理论解
theoretical_deflection = -w * t_eval**4 / (24 * E * I)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t_eval, solution.y[0], 'r-', label='数值解')
plt.plot(t_eval, theoretical_deflection, 'b--', label='理论解')
plt.title('梁的挠度')
plt.xlabel('位置 (m)')
plt.ylabel('挠度 (m)')
plt.legend()
plt.grid(True)
plt.savefig('beam_deflection.png')
print("梁的挠度图已保存为 beam_deflection.png")

print("\nSciPy实战应用示例完成！")
