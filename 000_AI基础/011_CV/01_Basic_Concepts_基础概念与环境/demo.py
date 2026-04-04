#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CV基础概念与环境
展示计算机视觉的基础概念和环境设置
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 基础概念介绍
print("=== 计算机视觉基础概念 ===")
print("计算机视觉是一门研究如何使机器"看"的科学，涉及图像处理、模式识别、机器学习等多个领域。")
print("核心任务包括：图像分类、目标检测、图像分割、人脸识别等。")

# 2. 环境检查
print("\n=== 环境检查 ===")
print(f"OpenCV版本: {cv2.__version__}")
print(f"NumPy版本: {np.__version__}")
print(f"Matplotlib版本: {plt.__version__}")

# 3. 图像读取与显示
print("\n=== 图像读取与显示 ===")

# 创建一个测试图像
img = np.zeros((200, 200, 3), dtype=np.uint8)
img[50:150, 50:150] = [0, 255, 0]  # 绿色方块

# 保存测试图像
cv2.imwrite('test_image.jpg', img)
print("测试图像已保存为 test_image.jpg")

# 读取图像
img_read = cv2.imread('test_image.jpg')
print(f"图像形状: {img_read.shape}")
print(f"图像数据类型: {img_read.dtype}")

# 转换颜色空间（BGR to RGB）
img_rgb = cv2.cvtColor(img_read, cv2.COLOR_BGR2RGB)

# 显示图像
plt.figure(figsize=(6, 6))
plt.imshow(img_rgb)
plt.title('测试图像')
plt.axis('off')
plt.savefig('display_image.png')
print("图像显示结果已保存为 display_image.png")

# 4. 图像基本操作
print("\n=== 图像基本操作 ===")

# 调整大小
img_resized = cv2.resize(img_read, (100, 100))
print(f"调整大小后的图像形状: {img_resized.shape}")

# 裁剪
img_cropped = img_read[75:125, 75:125]
print(f"裁剪后的图像形状: {img_cropped.shape}")

# 旋转
rows, cols = img_read.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
img_rotated = cv2.warpAffine(img_read, M, (cols, rows))

# 保存操作结果
cv2.imwrite('resized_image.jpg', img_resized)
cv2.imwrite('cropped_image.jpg', img_cropped)
cv2.imwrite('rotated_image.jpg', img_rotated)
print("图像操作结果已保存")

# 5. 图像直方图
print("\n=== 图像直方图 ===")

# 计算直方图
img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

# 绘制直方图
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.imshow(img_gray, cmap='gray')
plt.title('灰度图像')
plt.axis('off')

plt.subplot(122)
plt.plot(hist)
plt.title('灰度直方图')
plt.xlabel('像素值')
plt.ylabel('频率')
plt.tight_layout()
plt.savefig('histogram.png')
print("直方图已保存为 histogram.png")

# 6. 边缘检测
print("\n=== 边缘检测 ===")

# Canny边缘检测
edges = cv2.Canny(img_gray, 100, 200)

# 保存边缘检测结果
plt.figure(figsize=(6, 6))
plt.imshow(edges, cmap='gray')
plt.title('Canny边缘检测')
plt.axis('off')
plt.savefig('edges.png')
print("边缘检测结果已保存为 edges.png")

# 7. 轮廓检测
print("\n=== 轮廓检测 ===")

# 二值化
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
img_contours = img_read.copy()
cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 2)

# 保存轮廓检测结果
img_contours_rgb = cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(6, 6))
plt.imshow(img_contours_rgb)
plt.title('轮廓检测')
plt.axis('off')
plt.savefig('contours.png')
print("轮廓检测结果已保存为 contours.png")

# 8. 图像滤波
print("\n=== 图像滤波 ===")

# 添加噪声
noise = np.random.normal(0, 25, img_read.shape).astype(np.uint8)
img_noisy = cv2.add(img_read, noise)

# 高斯滤波
img_blur = cv2.GaussianBlur(img_noisy, (5, 5), 0)

# 保存滤波结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img_read, cv2.COLOR_BGR2RGB))
plt.title('原始图像')
plt.axis('off')

plt.subplot(132)
plt.imshow(cv2.cvtColor(img_noisy, cv2.COLOR_BGR2RGB))
plt.title('带噪声的图像')
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB))
plt.title('高斯滤波')
plt.axis('off')

plt.tight_layout()
plt.savefig('filtering.png')
print("滤波结果已保存为 filtering.png")

print("\nCV基础概念与环境设置示例完成！")
