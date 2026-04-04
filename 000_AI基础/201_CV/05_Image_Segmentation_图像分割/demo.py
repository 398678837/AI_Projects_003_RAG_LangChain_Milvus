#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图像分割
展示图像分割的基本方法
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 基础图像分割方法
print("=== 基础图像分割方法 ===")

# 创建测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制不同颜色的区域
cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 255), -1)   # 红色矩形
cv2.circle(img, (300, 100), 50, (0, 255, 0), -1)            # 绿色圆形
cv2.rectangle(img, (100, 250), (300, 350), (255, 0, 0), -1)  # 蓝色矩形

# 保存测试图像
cv2.imwrite('test_image.jpg', img)
print("测试图像已保存为 test_image.jpg")

# 读取图像
img = cv2.imread('test_image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. 基于阈值的分割
print("\n=== 基于阈值的分割 ===")

# 转换为灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 全局阈值
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 自适应阈值
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 保存阈值分割结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img_gray, cmap='gray')
plt.title('灰度图像')
plt.axis('off')

plt.subplot(132)
plt.imshow(thresh, cmap='gray')
plt.title('全局阈值')
plt.axis('off')

plt.subplot(133)
plt.imshow(adaptive_thresh, cmap='gray')
plt.title('自适应阈值')
plt.axis('off')

plt.tight_layout()
plt.savefig('threshold_segmentation.png')
print("阈值分割结果已保存为 threshold_segmentation.png")

# 3. 基于颜色的分割
print("\n=== 基于颜色的分割 ===")

# 转换到HSV颜色空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义颜色范围
# 红色
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
# 绿色
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
# 蓝色
lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

# 创建掩码
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)

# 合并掩码
mask = mask_red + mask_green + mask_blue

# 应用掩码
result = cv2.bitwise_and(img, img, mask=mask)

# 保存颜色分割结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img_rgb)
plt.title('原始图像')
plt.axis('off')

plt.subplot(132)
plt.imshow(mask, cmap='gray')
plt.title('掩码')
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('颜色分割结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('color_segmentation.png')
print("颜色分割结果已保存为 color_segmentation.png")

# 4. 基于边缘的分割
print("\n=== 基于边缘的分割 ===")

# Canny边缘检测
edges = cv2.Canny(img_gray, 100, 200)

# 闭运算填充边缘
kernel = np.ones((5, 5), np.uint8)
edges_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# 查找轮廓
contours, _ = cv2.findContours(edges_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# 填充轮廓
img_filled = np.zeros_like(img)
for contour in contours:
    cv2.drawContours(img_filled, [contour], -1, (255, 255, 255), -1)

# 保存边缘分割结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(edges, cmap='gray')
plt.title('Canny边缘')
plt.axis('off')

plt.subplot(132)
plt.imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB))
plt.title('轮廓')
plt.axis('off')

plt.subplot(133)
plt.imshow(img_filled, cmap='gray')
plt.title('填充轮廓')
plt.axis('off')

plt.tight_layout()
plt.savefig('edge_segmentation.png')
print("边缘分割结果已保存为 edge_segmentation.png")

# 5. 基于区域的分割
print("\n=== 基于区域的分割 ===")

# 分水岭算法
# 转换为灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 去除噪声
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 确定背景区域
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 寻找前景区域
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# 找到未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 标记标签
ret, markers = cv2.connectedComponents(sure_fg)

# 为所有标签加1，确保背景是0而不是1
markers = markers + 1

# 标记未知区域为0
markers[unknown == 255] = 0

# 应用分水岭算法
markers = cv2.watershed(img, markers)
img[markers == -1] = [0, 255, 0]  # 边界标记为绿色

# 保存分水岭分割结果
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img_gray, cmap='gray')
plt.title('灰度图像')
plt.axis('off')

plt.subplot(132)
plt.imshow(markers, cmap='jet')
plt.title('标记')
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('分水岭分割结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('watershed_segmentation.png')
print("分水岭分割结果已保存为 watershed_segmentation.png")

# 6. 基于聚类的分割
print("\n=== 基于聚类的分割 ===")

# 重塑图像为2D数组
Z = img.reshape((-1, 3))
Z = np.float32(Z)

# 定义聚类参数
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 转换回uint8
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# 保存聚类分割结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(img_rgb)
plt.title('原始图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(res2)
plt.title('K-means聚类分割结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('kmeans_segmentation.png')
print("K-means聚类分割结果已保存为 kmeans_segmentation.png")

# 7. 分割结果分析
print("\n=== 分割结果分析 ===")

# 计算分割区域的面积
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(f"区域 {i+1} 的面积: {area}")

# 计算分割区域的周长
for i, contour in enumerate(contours):
    perimeter = cv2.arcLength(contour, True)
    print(f"区域 {i+1} 的周长: {perimeter}")

# 计算分割区域的中心点
for i, contour in enumerate(contours):
    M = cv2.moments(contour)
    if M['m00'] > 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        print(f"区域 {i+1} 的中心点: ({cx}, {cy})")

print("\n图像分割示例完成！")
