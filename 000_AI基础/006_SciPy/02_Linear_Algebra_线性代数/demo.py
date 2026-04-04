#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy线性代数
展示SciPy的线性代数功能
"""

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# 1. 基本线性代数操作
print("=== 基本线性代数操作 ===")

# 创建矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"矩阵A:\n{A}")
print(f"矩阵B:\n{B}")

# 矩阵加法
print(f"\n矩阵加法 A + B:\n{A + B}")

# 矩阵减法
print(f"\n矩阵减法 A - B:\n{A - B}")

# 矩阵乘法
print(f"\n矩阵乘法 A @ B:\n{A @ B}")

# 标量乘法
print(f"\n标量乘法 2 * A:\n{2 * A}")

# 2. 矩阵属性
print("\n=== 矩阵属性 ===")
print(f"矩阵A的行列式: {linalg.det(A)}")
print(f"矩阵A的迹: {np.trace(A)}")
print(f"矩阵A的秩: {np.linalg.matrix_rank(A)}")

# 3. 矩阵逆和伪逆
print("\n=== 矩阵逆和伪逆 ===")
# 矩阵逆
A_inv = linalg.inv(A)
print(f"矩阵A的逆:\n{A_inv}")
print(f"A @ A_inv:\n{A @ A_inv}")

# 伪逆（对于奇异矩阵）
C = np.array([[1, 2], [2, 4]])
print(f"\n矩阵C:\n{C}")
print(f"矩阵C的行列式: {linalg.det(C)}")
C_pinv = linalg.pinv(C)
print(f"矩阵C的伪逆:\n{C_pinv}")

# 4. 特征值和特征向量
print("\n=== 特征值和特征向量 ===")
# 计算特征值和特征向量
eigenvalues, eigenvectors = linalg.eig(A)
print(f"特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 验证 Av = λv
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lambda_v = eigenvalues[i] * v
    Av = A @ v
    print(f"\n特征值 {eigenvalues[i]}:")
    print(f"Av: {Av}")
    print(f"λv: {lambda_v}")

# 5. 奇异值分解
print("\n=== 奇异值分解 ===")
U, s, Vh = linalg.svd(A)
print(f"U矩阵:\n{U}")
print(f"奇异值: {s}")
print(f"Vh矩阵:\n{Vh}")

# 重构矩阵
S = np.zeros_like(A)
np.fill_diagonal(S, s)
A_reconstructed = U @ S @ Vh
print(f"\n重构后的矩阵:\n{A_reconstructed}")

# 6. 求解线性方程组
print("\n=== 求解线性方程组 ===")
# 解 Ax = b
b = np.array([5, 11])
x = linalg.solve(A, b)
print(f"方程组 Ax = b 的解 x: {x}")
print(f"验证 A @ x: {A @ x}")
print(f"b: {b}")

# 7. 最小二乘问题
print("\n=== 最小二乘问题 ===")
# 构造超定方程组
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([2, 3, 4, 5])

# 求解最小二乘
beta, residual, rank, singular_values = linalg.lstsq(X, y)
print(f"最小二乘解 beta: {beta}")
print(f"残差平方和: {residual}")
print(f"矩阵的秩: {rank}")
print(f"奇异值: {singular_values}")

# 可视化最小二乘拟合
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 1], y, label='数据点')
plt.plot(X[:, 1], X @ beta, 'r-', label='最小二乘拟合')
plt.title('最小二乘拟合示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('least_squares_fit.png')
print("最小二乘拟合图已保存为 least_squares_fit.png")

# 8. 矩阵分解
print("\n=== 矩阵分解 ===")

# LU分解
P, L, U = linalg.lu(A)
print(f"P矩阵 (置换矩阵):\n{P}")
print(f"L矩阵 (下三角矩阵):\n{L}")
print(f"U矩阵 (上三角矩阵):\n{U}")
print(f"验证 P @ L @ U:\n{P @ L @ U}")

# Cholesky分解（仅适用于正定矩阵）
D = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
L_chol = linalg.cholesky(D)
print(f"\nCholesky分解 L:\n{L_chol}")
print(f"验证 L @ L.T:\n{L_chol @ L_chol.T}")
print(f"原始矩阵 D:\n{D}")

# QR分解
Q, R = linalg.qr(A)
print(f"\nQR分解 Q:\n{Q}")
print(f"QR分解 R:\n{R}")
print(f"验证 Q @ R:\n{Q @ R}")

# 9. 范数计算
print("\n=== 范数计算 ===")
print(f"矩阵A的1-范数: {linalg.norm(A, 1)}")
print(f"矩阵A的2-范数: {linalg.norm(A, 2)}")
print(f"矩阵A的无穷范数: {linalg.norm(A, np.inf)}")
print(f"矩阵A的Frobenius范数: {linalg.norm(A, 'fro')}")

# 10. 条件数
print("\n=== 条件数 ===")
print(f"矩阵A的条件数: {linalg.cond(A)}")
print(f"矩阵C的条件数: {linalg.cond(C)}")

print("\nSciPy线性代数示例完成！")
