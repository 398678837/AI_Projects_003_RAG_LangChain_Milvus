#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图像处理基础
展示图像处理的基本操作
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 图像读取与预处理
print("=== 图像读取与预处理 ===")

# 创建测试图像
img = np.zeros((300, 300, 3), dtype=np.uint8)
# 绘制一个红色圆形
cv2.circle(img, (150, 150), 100, (0, 0, 255), -1)
# 绘制一个蓝色矩形
cv2.rectangle(img, (50, 50), (250, 250), (255, 0, 0), 2)
# 绘制一个绿色三角形
pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 0), 2)

# 保存测试图像
cv2.imwrite('test_image.jpg', img)
print("测试图像已保存为 test_image.jpg")

# 读取图像
img = cv2.imread('test_image.jpg')
print(f"图像形状: {img.shape}")

# 2. 颜色空间转换
print("\n=== 颜色空间转换 ===")

# BGR转RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR转灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR转HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 保存颜色空间转换结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img_rgb)
plt.title('RGB')
plt.axis('off')

plt.subplot(132)
plt.imshow(img_gray, cmap='gray')
plt.title('灰度')
plt.axis('off')

plt.subplot(133)
plt.imshow(img_hsv)
plt.title('HSV')
plt.axis('off')

plt.tight_layout()
plt.savefig('color_spaces.png')
print("颜色空间转换结果已保存为 color_spaces.png")

# 3. 图像阈值处理
print("\n=== 图像阈值处理 ===")

# 全局阈值
ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

# 自适应阈值
thresh6 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh7 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 保存阈值处理结果
titles = ['原始图像', '二值化', '反二值化', '截断', '低于阈值置零', '高于阈值置零', '自适应均值阈值', '自适应高斯阈值']
images = [img_gray, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7]

plt.figure(figsize=(12, 6))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('thresholding.png')
print("阈值处理结果已保存为 thresholding.png")

# 4. 形态学操作
print("\n=== 形态学操作 ===")

# 创建结构元素
kernel = np.ones((5, 5), np.uint8)

# 腐蚀
erosion = cv2.erode(thresh1, kernel, iterations=1)

# 膨胀
dilation = cv2.dilate(thresh1, kernel, iterations=1)

# 开运算（先腐蚀后膨胀）
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

# 闭运算（先膨胀后腐蚀）
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

# 梯度
gradient = cv2.morphologyEx(thresh1, cv2.MORPH_GRADIENT, kernel)

# 顶帽
tophat = cv2.morphologyEx(thresh1, cv2.MORPH_TOPHAT, kernel)

# 黑帽
blackhat = cv2.morphologyEx(thresh1, cv2.MORPH_BLACKHAT, kernel)

# 保存形态学操作结果
titles = ['原始二值图', '腐蚀', '膨胀', '开运算', '闭运算', '梯度', '顶帽', '黑帽']
images = [thresh1, erosion, dilation, opening, closing, gradient, tophat, blackhat]

plt.figure(figsize=(12, 6))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('morphology.png')
print("形态学操作结果已保存为 morphology.png")

# 5. 图像变换
print("\n=== 图像变换 ===")

# 平移
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 50], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (cols, rows))

# 旋转
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

# 缩放
scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 仿射变换
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(img, M, (cols, rows))

# 透视变换
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(img, M, (300, 300))

# 保存图像变换结果
titles = ['原始图像', '平移', '旋转', '缩放', '仿射变换', '透视变换']
images = [img_rgb, cv2.cvtColor(translated, cv2.COLOR_BGR2RGB), cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB), 
          cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB), cv2.cvtColor(affine, cv2.COLOR_BGR2RGB), 
          cv2.cvtColor(perspective, cv2.COLOR_BGR2RGB)]

plt.figure(figsize=(12, 6))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('transformations.png')
print("图像变换结果已保存为 transformations.png")

# 6. 图像滤波
print("\n=== 图像滤波 ===")

# 添加高斯噪声
noise = np.random.normal(0, 25, img.shape).astype(np.uint8)
img_noisy = cv2.add(img, noise)

# 均值滤波
blur = cv2.blur(img_noisy, (5, 5))

# 高斯滤波
gaussian_blur = cv2.GaussianBlur(img_noisy, (5, 5), 0)

# 中值滤波
median_blur = cv2.medianBlur(img_noisy, 5)

# 双边滤波
bilateral_blur = cv2.bilateralFilter(img_noisy, 9, 75, 75)

# 保存滤波结果
titles = ['原始图像', '带噪声的图像', '均值滤波', '高斯滤波', '中值滤波', '双边滤波']
images = [img_rgb, cv2.cvtColor(img_noisy, cv2.COLOR_BGR2RGB), cv2.cvtColor(blur, cv2.COLOR_BGR2RGB), 
          cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB), cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB), 
          cv2.cvtColor(bilateral_blur, cv2.COLOR_BGR2RGB)]

plt.figure(figsize=(12, 6))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('filtering.png')
print("滤波结果已保存为 filtering.png")

# 7. 边缘检测
print("\n=== 边缘检测 ===")

# Canny边缘检测
edges = cv2.Canny(img_gray, 100, 200)

# Sobel边缘检测
sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)
sobel = np.sqrt(sobelx**2 + sobely**2)
sobel = np.uint8(sobel)

# Laplacian边缘检测
laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# 保存边缘检测结果
titles = ['原始灰度图', 'Canny边缘', 'Sobel边缘', 'Laplacian边缘']
images = [img_gray, edges, sobel, laplacian]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('edge_detection.png')
print("边缘检测结果已保存为 edge_detection.png")

print("\n图像处理基础示例完成！")
