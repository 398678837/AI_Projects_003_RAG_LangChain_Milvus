#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CV实战应用
展示计算机视觉在实际应用中的使用
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 二维码检测与识别
print("=== 二维码检测与识别 ===")

# 创建包含二维码的测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制一个简单的二维码图案（模拟）
# 绘制外框
cv2.rectangle(img, (50, 50), (350, 350), (255, 255, 255), -1)
# 绘制定位图案
cv2.rectangle(img, (70, 70), (120, 120), (0, 0, 0), -1)
cv2.rectangle(img, (75, 75), (115, 115), (255, 255, 255), -1)
cv2.rectangle(img, (80, 80), (110, 110), (0, 0, 0), -1)

cv2.rectangle(img, (280, 70), (330, 120), (0, 0, 0), -1)
cv2.rectangle(img, (285, 75), (325, 115), (255, 255, 255), -1)
cv2.rectangle(img, (290, 80), (320, 110), (0, 0, 0), -1)

cv2.rectangle(img, (70, 280), (120, 330), (0, 0, 0), -1)
cv2.rectangle(img, (75, 285), (115, 325), (255, 255, 255), -1)
cv2.rectangle(img, (80, 290), (110, 320), (0, 0, 0), -1)

# 绘制数据区域
for i in range(150, 250, 20):
    for j in range(150, 250, 20):
        if (i + j) % 40 == 0:
            cv2.rectangle(img, (i, j), (i+15, j+15), (0, 0, 0), -1)

# 保存测试图像
cv2.imwrite('qrcode_image.jpg', img)
print("二维码测试图像已保存为 qrcode_image.jpg")

# 尝试使用OpenCV的二维码检测器
try:
    # 加载二维码检测器
    detector = cv2.QRCodeDetector()
    
    # 读取图像
    img = cv2.imread('qrcode_image.jpg')
    
    # 检测二维码
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
    
    if data:
        print(f"二维码内容: {data}")
        # 绘制二维码边界
        if vertices_array is not None:
            vertices = vertices_array[0].astype(int)
            for i in range(len(vertices)):
                cv2.line(img, tuple(vertices[i]), tuple(vertices[(i+1)%len(vertices)]), (0, 255, 0), 2)
            print("二维码边界已绘制")
    else:
        print("未检测到二维码")
        # 模拟检测结果
        cv2.rectangle(img, (50, 50), (350, 350), (0, 255, 0), 2)
        cv2.putText(img, 'QR Code', (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
    # 保存检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(cv2.imread('qrcode_image.jpg'), cv2.COLOR_BGR2RGB))
    plt.title('原始二维码图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('二维码检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('qrcode_detection.png')
    print("二维码检测结果已保存为 qrcode_detection.png")
except Exception as e:
    print(f"二维码检测失败: {e}")
    # 模拟检测结果
    img = cv2.imread('qrcode_image.jpg')
    cv2.rectangle(img, (50, 50), (350, 350), (0, 255, 0), 2)
    cv2.putText(img, 'QR Code', (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 保存检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(cv2.imread('qrcode_image.jpg'), cv2.COLOR_BGR2RGB))
    plt.title('原始二维码图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('二维码检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('qrcode_detection.png')
    print("二维码检测结果已保存为 qrcode_detection.png")

# 2. 物体计数
print("\n=== 物体计数 ===")

# 创建包含多个物体的测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制多个圆形
for i in range(10):
    x = np.random.randint(50, 350)
    y = np.random.randint(50, 350)
    radius = np.random.randint(10, 20)
    color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    cv2.circle(img, (x, y), radius, color, -1)

# 保存测试图像
cv2.imwrite('objects_image.jpg', img)
print("物体计数测试图像已保存为 objects_image.jpg")

# 物体计数
# 转换为灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 过滤小轮廓
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

# 绘制轮廓和计数
img_counted = img.copy()
for i, contour in enumerate(filtered_contours):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img_counted, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img_counted, str(i+1), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 显示计数结果
count = len(filtered_contours)
print(f"检测到的物体数量: {count}")

# 保存计数结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(cv2.imread('objects_image.jpg'), cv2.COLOR_BGR2RGB))
plt.title('原始图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_counted, cv2.COLOR_BGR2RGB))
plt.title(f'物体计数结果 (共{count}个)')
plt.axis('off')

plt.tight_layout()
plt.savefig('object_counting.png')
print("物体计数结果已保存为 object_counting.png")

# 3. 交通标志检测
print("\n=== 交通标志检测 ===")

# 创建包含交通标志的测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制背景
cv2.rectangle(img, (0, 0), (400, 400), (135, 206, 235), -1)  # 天空蓝
# 绘制道路
cv2.rectangle(img, (0, 200), (400, 400), (169, 169, 169), -1)  # 灰色
# 绘制交通标志
# 停止标志
cv2.circle(img, (100, 150), 40, (0, 0, 255), -1)
cv2.circle(img, (100, 150), 35, (255, 255, 255), -1)
cv2.putText(img, 'STOP', (75, 155), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# 限速标志
cv2.circle(img, (300, 150), 40, (255, 255, 0), -1)
cv2.circle(img, (300, 150), 35, (255, 255, 255), -1)
cv2.putText(img, '50', (285, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

# 保存测试图像
cv2.imwrite('traffic_signs.jpg', img)
print("交通标志测试图像已保存为 traffic_signs.jpg")

# 交通标志检测
# 转换到HSV颜色空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 检测红色（停止标志）
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)

# 检测黄色（限速标志）
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

# 合并掩码
mask = mask_red + mask_yellow

# 查找轮廓
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制检测结果
img_detected = img.copy()
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_detected, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 识别标志类型
        if np.mean(img[y:y+h, x:x+w, 2]) > 150:  # 红色通道值高
            cv2.putText(img_detected, 'Stop', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.putText(img_detected, 'Speed Limit', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 保存检测结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(cv2.imread('traffic_signs.jpg'), cv2.COLOR_BGR2RGB))
plt.title('原始交通标志图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_detected, cv2.COLOR_BGR2RGB))
plt.title('交通标志检测结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('traffic_sign_detection.png')
print("交通标志检测结果已保存为 traffic_sign_detection.png")

# 4. 文档扫描
print("\n=== 文档扫描 ===")

# 创建包含文档的测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制背景
cv2.rectangle(img, (0, 0), (400, 400), (100, 100, 100), -1)
# 绘制文档（带透视变换）
pts = np.array([[80, 50], [320, 70], [300, 350], [60, 330]], np.int32)
cv2.fillPoly(img, [pts], (255, 255, 255))
# 添加文字
cv2.putText(img, 'Document', (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# 保存测试图像
cv2.imwrite('document.jpg', img)
print("文档测试图像已保存为 document.jpg")

# 文档扫描
# 转换为灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(img_gray, 50, 150)

# 查找轮廓
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大的轮廓（文档）
l最大_contour = max(contours, key=cv2.contourArea)

# 近似轮廓
epsilon = 0.02 * cv2.arcLength(l最大_contour, True)
approx = cv2.approxPolyDP(l最大_contour, epsilon, True)

# 确保找到四个角点
if len(approx) == 4:
    # 排序角点
    approx = approx.reshape(-1, 2)
    approx = approx[np.argsort(approx[:, 0]), :]
    if approx[0, 1] > approx[1, 1]:
        approx[0, :], approx[1, :] = approx[1, :].copy(), approx[0, :]
    if approx[2, 1] < approx[3, 1]:
        approx[2, :], approx[3, :] = approx[3, :].copy(), approx[2, :]
    
    # 目标点
    width, height = 300, 400
    dst = np.array([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]], np.float32)
    
    # 透视变换
    M = cv2.getPerspectiveTransform(np.float32(approx), dst)
    scanned = cv2.warpPerspective(img, M, (width, height))
    
    # 二值化
    scanned_gray = cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY)
    scanned_binary = cv2.adaptiveThreshold(scanned_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
else:
    # 模拟文档扫描结果
    scanned = cv2.resize(img, (300, 400))
    scanned_gray = cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY)
    scanned_binary = cv2.adaptiveThreshold(scanned_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 保存扫描结果
plt.figure(figsize=(15, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(cv2.imread('document.jpg'), cv2.COLOR_BGR2RGB))
plt.title('原始文档')
plt.axis('off')

plt.subplot(132)
plt.imshow(cv2.cvtColor(scanned, cv2.COLOR_BGR2RGB))
plt.title('扫描结果')
plt.axis('off')

plt.subplot(133)
plt.imshow(scanned_binary, cmap='gray')
plt.title('二值化结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('document_scanning.png')
print("文档扫描结果已保存为 document_scanning.png")

# 5.  augmented reality (AR) 示例
print("\n=== 增强现实 (AR) 示例 ===")

# 创建AR测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制背景
cv2.rectangle(img, (0, 0), (400, 400), (135, 206, 235), -1)  # 天空蓝
# 绘制地面
cv2.rectangle(img, (0, 300), (400, 400), (165, 42, 42), -1)  # 棕色
# 绘制标记点
cv2.circle(img, (100, 250), 10, (0, 0, 255), -1)
cv2.circle(img, (300, 250), 10, (0, 0, 255), -1)
cv2.circle(img, (100, 350), 10, (0, 0, 255), -1)
cv2.circle(img, (300, 350), 10, (0, 0, 255), -1)

# 保存测试图像
cv2.imwrite('ar_image.jpg', img)
print("AR测试图像已保存为 ar_image.jpg")

# AR增强
# 读取图像
img = cv2.imread('ar_image.jpg')

# 定义标记点
marker_points = np.array([[100, 250], [300, 250], [100, 350], [300, 350]], np.float32)

# 定义3D物体的顶点
cube_points = np.array([
    [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],
    [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]
], np.float32)

# 相机参数（模拟）
camera_matrix = np.array([[800, 0, 200], [0, 800, 200], [0, 0, 1]], np.float32)
dist_coeffs = np.zeros((4, 1))

# 求解位姿
_, rvec, tvec = cv2.solvePnP(cube_points, marker_points, camera_matrix, dist_coeffs)

# 投影3D点到2D
projected_points, _ = cv2.projectPoints(cube_points, rvec, tvec, camera_matrix, dist_coeffs)
projected_points = projected_points.reshape(-1, 2).astype(int)

# 绘制立方体
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
for edge in edges:
    cv2.line(img, tuple(projected_points[edge[0]]), tuple(projected_points[edge[1]]), (0, 255, 0), 2)

# 保存AR结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(cv2.imread('ar_image.jpg'), cv2.COLOR_BGR2RGB))
plt.title('原始图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('AR增强结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('ar_example.png')
print("AR增强结果已保存为 ar_example.png")

print("\nCV实战应用示例完成！")
