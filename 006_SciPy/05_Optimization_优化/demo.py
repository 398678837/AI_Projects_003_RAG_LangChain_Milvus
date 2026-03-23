#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy优化
展示SciPy的优化功能
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# 1. 无约束优化
print("=== 无约束优化 ===")

# 定义目标函数
def f(x):
    return x ** 2 + 10 * np.sin(x)

# 绘制目标函数
x = np.linspace(-10, 10, 1000)
y = f(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('目标函数 f(x) = x² + 10sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('objective_function.png')
print("目标函数图已保存为 objective_function.png")

# 使用minimize进行优化
result = optimize.minimize(f, x0=0)
print(f"最小值点: {result.x[0]}")
print(f"最小值: {result.fun}")
print(f"迭代次数: {result.nit}")
print(f"是否成功: {result.success}")

# 2. 有约束优化
print("\n=== 有约束优化 ===")

# 定义目标函数
def f_constrained(x):
    return (x[0] - 1) ** 2 + (x[1] - 2.5) ** 2

# 定义约束条件
constraints = [
    {'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
    {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2}
]

# 定义边界条件
bounds = [(-10, 10), (-10, 10)]

# 求解有约束优化问题
result_constrained = optimize.minimize(f_constrained, x0=[0, 0], method='SLSQP', bounds=bounds, constraints=constraints)
print(f"最小值点: {result_constrained.x}")
print(f"最小值: {result_constrained.fun}")
print(f"是否成功: {result_constrained.success}")

# 3. 全局优化
print("\n=== 全局优化 ===")

# 使用differential_evolution进行全局优化
result_global = optimize.differential_evolution(f, bounds=[(-10, 10)])
print(f"全局最小值点: {result_global.x[0]}")
print(f"全局最小值: {result_global.fun}")
print(f"迭代次数: {result_global.nit}")
print(f"是否成功: {result_global.success}")

# 4. 最小二乘优化
print("\n=== 最小二乘优化 ===")

# 定义模型函数
def model(x, a, b, c):
    return a * np.exp(-b * x) + c

# 生成带噪声的数据
x_data = np.linspace(0, 4, 50)
y_data = model(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(x_data))

# 初始参数猜测
initial_guess = [1, 1, 1]

# 使用curve_fit进行曲线拟合
popt, pcov = optimize.curve_fit(model, x_data, y_data, p0=initial_guess)
print(f"拟合参数: a={popt[0]}, b={popt[1]}, c={popt[2]}")

# 可视化拟合结果
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='数据点')
plt.plot(x_data, model(x_data, *popt), 'r-', label='拟合曲线')
plt.title('曲线拟合示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('curve_fit.png')
print("曲线拟合图已保存为 curve_fit.png")

# 5. 方程求解
print("\n=== 方程求解 ===")

# 定义方程
def equation(x):
    return x ** 3 - x - 2

# 使用fsolve求解方程
root = optimize.fsolve(equation, x0=1)
print(f"方程 x³ - x - 2 = 0 的根: {root[0]}")
print(f"验证: {equation(root[0])}")

# 6. 线性规划
print("\n=== 线性规划 ===")

# 定义目标函数系数（最小化 c·x）
c = [-1, -2]  # 注意：linprog默认最小化，所以最大化问题需要取负

# 定义不等式约束矩阵 A·x ≤ b
A = [[2, 1], [1, 2]]
b = [4, 5]

# 定义变量边界
x0_bounds = (0, None)
x1_bounds = (0, None)

# 求解线性规划
result_lp = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
print(f"最优解: x0={result_lp.x[0]}, x1={result_lp.x[1]}")
print(f"最优值: {-result_lp.fun}")  # 转换回最大化问题的目标值
print(f"是否成功: {result_lp.success}")

# 7. 二次规划
print("\n=== 二次规划 ===")

# 定义二次项系数矩阵
P = np.array([[2, 0], [0, 2]])

# 定义一次项系数向量
q = np.array([-2, -3])

# 定义不等式约束矩阵
G = np.array([[-1, 0], [0, -1], [1, 2]])
h = np.array([0, 0, 4])

# 求解二次规划
result_qp = optimize.minimize(
    lambda x: 0.5 * x.T @ P @ x + q.T @ x,
    x0=[0, 0],
    constraints={'type': 'ineq', 'fun': lambda x: h - G @ x},
    method='SLSQP'
)
print(f"最优解: x0={result_qp.x[0]}, x1={result_qp.x[1]}")
print(f"最优值: {result_qp.fun}")
print(f"是否成功: {result_qp.success}")

# 8. 多目标优化
print("\n=== 多目标优化 ===")

# 定义目标函数
def multi_objective(x):
    return [
        (x[0] - 1) ** 2 + (x[1] - 2) ** 2,
        (x[0] + 1) ** 2 + (x[1] + 2) ** 2
    ]

# 使用NSGA-II算法进行多目标优化
from scipy.optimize import minimize

# 这里使用标量化方法（将多目标转化为单目标）
def scalarized_objective(x, weights):
    objectives = multi_objective(x)
    return weights[0] * objectives[0] + weights[1] * objectives[1]

# 不同权重下的优化
weights_list = [[0.1, 0.9], [0.5, 0.5], [0.9, 0.1]]
results = []

for weights in weights_list:
    result = optimize.minimize(scalarized_objective, x0=[0, 0], args=(weights,))
    results.append(result.x)
    print(f"权重 {weights} 下的最优解: {result.x}")

# 可视化帕累托前沿
plt.figure(figsize=(10, 6))
# 生成帕累托前沿
pareto_x = np.linspace(-2, 2, 100)
pareto_y = np.sqrt(4 - (pareto_x + 1)**2) - 2
plt.plot(pareto_x, pareto_y, 'b-', label='帕累托前沿')
# 绘制不同权重下的解
for i, (x, weights) in enumerate(zip(results, weights_list)):
    plt.plot(x[0], x[1], 'o', label=f'权重 {weights}')
plt.title('多目标优化示例')
plt.xlabel('x0')
plt.ylabel('x1')
plt.legend()
plt.grid(True)
plt.savefig('multi_objective.png')
print("多目标优化图已保存为 multi_objective.png")

print("\nSciPy优化示例完成！")
