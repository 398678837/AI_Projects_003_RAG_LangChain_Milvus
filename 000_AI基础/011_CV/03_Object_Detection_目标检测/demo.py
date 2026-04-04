#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
目标检测
展示目标检测的基本方法
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 基础目标检测方法
print("=== 基础目标检测方法 ===")

# 创建测试图像
img = np.zeros((400, 400, 3), dtype=np.uint8)
# 绘制多个不同颜色的圆形
cv2.circle(img, (100, 100), 30, (0, 0, 255), -1)  # 红色圆形
cv2.circle(img, (300, 100), 40, (0, 255, 0), -1)  # 绿色圆形
cv2.circle(img, (200, 250), 50, (255, 0, 0), -1)  # 蓝色圆形

# 保存测试图像
cv2.imwrite('test_image.jpg', img)
print("测试图像已保存为 test_image.jpg")

# 读取图像
img = cv2.imread('test_image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. 基于颜色的目标检测
print("\n=== 基于颜色的目标检测 ===")

# 转换到HSV颜色空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义红色的HSV范围
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 定义绿色的HSV范围
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# 定义蓝色的HSV范围
lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

# 创建掩码
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)

# 查找轮廓
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制边界框
img_color_detection = img.copy()
for contour in contours_red:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img_color_detection, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img_color_detection, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

for contour in contours_green:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img_color_detection, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img_color_detection, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

for contour in contours_blue:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img_color_detection, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img_color_detection, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# 保存颜色检测结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(img_rgb)
plt.title('原始图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_color_detection, cv2.COLOR_BGR2RGB))
plt.title('颜色检测结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('color_detection.png')
print("颜色检测结果已保存为 color_detection.png")

# 3. 基于 Haar 级联分类器的目标检测
print("\n=== 基于 Haar 级联分类器的目标检测 ===")

# 尝试加载预训练的人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 检查分类器是否加载成功
if face_cascade.empty():
    print("无法加载人脸检测器，使用模拟数据进行演示")
    # 创建模拟人脸图像
    img_face = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img_face, (200, 200), 80, (255, 220, 180), -1)
    # 绘制眼睛
    cv2.circle(img_face, (170, 180), 15, (0, 0, 0), -1)
    cv2.circle(img_face, (230, 180), 15, (0, 0, 0), -1)
    # 绘制嘴巴
    cv2.ellipse(img_face, (200, 230), (30, 20), 0, 0, 180, (0, 0, 0), 2)
    
    # 保存模拟人脸图像
    cv2.imwrite('face_image.jpg', img_face)
    img_face_rgb = cv2.cvtColor(img_face, cv2.COLOR_BGR2RGB)
    
    # 绘制模拟检测结果
    img_face_detected = img_face.copy()
    cv2.rectangle(img_face_detected, (120, 120), (280, 280), (0, 255, 0), 2)
    cv2.putText(img_face_detected, 'Face', (120, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 保存人脸检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(img_face_rgb)
    plt.title('模拟人脸图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_face_detected, cv2.COLOR_BGR2RGB))
    plt.title('人脸检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_detection.png')
    print("人脸检测结果已保存为 face_detection.png")
else:
    print("人脸检测器加载成功")
    # 创建模拟人脸图像
    img_face = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img_face, (200, 200), 80, (255, 220, 180), -1)
    # 绘制眼睛
    cv2.circle(img_face, (170, 180), 15, (0, 0, 0), -1)
    cv2.circle(img_face, (230, 180), 15, (0, 0, 0), -1)
    # 绘制嘴巴
    cv2.ellipse(img_face, (200, 230), (30, 20), 0, 0, 180, (0, 0, 0), 2)
    
    # 保存模拟人脸图像
    cv2.imwrite('face_image.jpg', img_face)
    img_face_gray = cv2.cvtColor(img_face, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(img_face_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 绘制检测结果
    img_face_detected = img_face.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(img_face_detected, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img_face_detected, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 保存人脸检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img_face, cv2.COLOR_BGR2RGB))
    plt.title('模拟人脸图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_face_detected, cv2.COLOR_BGR2RGB))
    plt.title('人脸检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_detection.png')
    print("人脸检测结果已保存为 face_detection.png")

# 4. 基于轮廓的目标检测
print("\n=== 基于轮廓的目标检测 ===")

# 读取图像并转换为灰度
img = cv2.imread('test_image.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓和边界框
img_contour_detection = img.copy()
for i, contour in enumerate(contours):
    # 计算轮廓面积
    area = cv2.contourArea(contour)
    # 过滤小轮廓
    if area > 100:
        # 绘制轮廓
        cv2.drawContours(img_contour_detection, [contour], -1, (0, 255, 0), 2)
        # 绘制边界框
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_contour_detection, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 计算中心点
        M = cv2.moments(contour)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img_contour_detection, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(img_contour_detection, f'Object {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 保存轮廓检测结果
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('原始图像')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_contour_detection, cv2.COLOR_BGR2RGB))
plt.title('轮廓检测结果')
plt.axis('off')

plt.tight_layout()
plt.savefig('contour_detection.png')
print("轮廓检测结果已保存为 contour_detection.png")

# 5. 目标跟踪
print("\n=== 目标跟踪 ===")

# 创建视频帧序列
frames = []
for i in range(10):
    frame = np.zeros((400, 400, 3), dtype=np.uint8)
    # 移动的红色圆形
    x = 50 + i * 30
    y = 200
    cv2.circle(frame, (x, y), 30, (0, 0, 255), -1)
    frames.append(frame)

# 保存视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tracking_video.avi', fourcc, 10.0, (400, 400))
for frame in frames:
    out.write(frame)
out.release()
print("跟踪视频已保存为 tracking_video.avi")

# 简单的目标跟踪示例
plt.figure(figsize=(15, 6))
for i, frame in enumerate(frames[::2]):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title(f'Frame {i*2+1}')
    plt.axis('off')

plt.tight_layout()
plt.savefig('tracking_frames.png')
print("跟踪帧已保存为 tracking_frames.png")

print("\n目标检测示例完成！")
