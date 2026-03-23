#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人脸识别
展示人脸识别的基本方法
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 人脸检测
print("=== 人脸检测 ===")

# 加载预训练的人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 检查分类器是否加载成功
if face_cascade.empty() or eye_cascade.empty():
    print("无法加载人脸或眼睛检测器，使用模拟数据进行演示")
    # 创建模拟人脸图像
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img, (200, 200), 80, (255, 220, 180), -1)
    # 绘制眼睛
    cv2.circle(img, (170, 180), 15, (0, 0, 0), -1)
    cv2.circle(img, (230, 180), 15, (0, 0, 0), -1)
    # 绘制嘴巴
    cv2.ellipse(img, (200, 230), (30, 20), 0, 0, 180, (0, 0, 0), 2)
    
    # 保存模拟人脸图像
    cv2.imwrite('face_image.jpg', img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 绘制模拟检测结果
    img_detected = img.copy()
    cv2.rectangle(img_detected, (120, 120), (280, 280), (0, 255, 0), 2)
    cv2.putText(img_detected, 'Face', (120, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # 绘制眼睛检测
    cv2.circle(img_detected, (170, 180), 20, (0, 0, 255), 2)
    cv2.circle(img_detected, (230, 180), 20, (0, 0, 255), 2)
    
    # 保存人脸检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(img_rgb)
    plt.title('模拟人脸图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_detected, cv2.COLOR_BGR2RGB))
    plt.title('人脸检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_detection.png')
    print("人脸检测结果已保存为 face_detection.png")
else:
    print("人脸和眼睛检测器加载成功")
    # 创建模拟人脸图像
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img, (200, 200), 80, (255, 220, 180), -1)
    # 绘制眼睛
    cv2.circle(img, (170, 180), 15, (0, 0, 0), -1)
    cv2.circle(img, (230, 180), 15, (0, 0, 0), -1)
    # 绘制嘴巴
    cv2.ellipse(img, (200, 230), (30, 20), 0, 0, 180, (0, 0, 0), 2)
    
    # 保存模拟人脸图像
    cv2.imwrite('face_image.jpg', img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 绘制检测结果
    img_detected = img.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(img_detected, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img_detected, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # 在人脸区域检测眼睛
        roi_gray = img_gray[y:y+h, x:x+w]
        roi_color = img_detected[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
    
    # 保存人脸检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('模拟人脸图像')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_detected, cv2.COLOR_BGR2RGB))
    plt.title('人脸检测结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_detection.png')
    print("人脸检测结果已保存为 face_detection.png")

# 2. 人脸识别
print("\n=== 人脸识别 ===")

# 尝试加载人脸识别模型
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# 创建训练数据
def create_training_data():
    """创建人脸识别训练数据"""
    faces = []
    labels = []
    
    # 创建第一个人的人脸
    for i in range(3):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        # 绘制不同表情的人脸
        if i == 0:  # 微笑
            cv2.circle(img, (50, 50), 40, (255, 220, 180), -1)
            cv2.circle(img, (35, 40), 8, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 8, (0, 0, 0), -1)
            cv2.ellipse(img, (50, 60), (15, 10), 0, 0, 180, (0, 0, 0), 2)
        elif i == 1:  # 严肃
            cv2.circle(img, (50, 50), 40, (255, 220, 180), -1)
            cv2.circle(img, (35, 40), 8, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 8, (0, 0, 0), -1)
            cv2.line(img, (35, 65), (65, 65), (0, 0, 0), 2)
        else:  # 惊讶
            cv2.circle(img, (50, 50), 40, (255, 220, 180), -1)
            cv2.circle(img, (35, 40), 10, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 10, (0, 0, 0), -1)
            cv2.circle(img, (50, 65), 8, (0, 0, 0), -1)
        
        # 转换为灰度
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces.append(img_gray)
        labels.append(0)  # 第一个人的标签
    
    # 创建第二个人的人脸
    for i in range(3):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        # 绘制不同表情的人脸
        if i == 0:  # 微笑
            cv2.rectangle(img, (10, 10), (90, 90), (255, 200, 160), -1)
            cv2.circle(img, (35, 40), 8, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 8, (0, 0, 0), -1)
            cv2.ellipse(img, (50, 60), (15, 10), 0, 0, 180, (0, 0, 0), 2)
        elif i == 1:  # 严肃
            cv2.rectangle(img, (10, 10), (90, 90), (255, 200, 160), -1)
            cv2.circle(img, (35, 40), 8, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 8, (0, 0, 0), -1)
            cv2.line(img, (35, 65), (65, 65), (0, 0, 0), 2)
        else:  # 惊讶
            cv2.rectangle(img, (10, 10), (90, 90), (255, 200, 160), -1)
            cv2.circle(img, (35, 40), 10, (0, 0, 0), -1)
            cv2.circle(img, (65, 40), 10, (0, 0, 0), -1)
            cv2.circle(img, (50, 65), 8, (0, 0, 0), -1)
        
        # 转换为灰度
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces.append(img_gray)
        labels.append(1)  # 第二个人的标签
    
    return faces, labels

# 创建训练数据
faces, labels = create_training_data()
print(f"训练数据大小: {len(faces)}")
print(f"标签: {labels}")

# 训练模型
face_recognizer.train(faces, np.array(labels))
print("模型训练完成")

# 保存模型
face_recognizer.save('face_recognizer.yml')
print("模型已保存为 face_recognizer.yml")

# 加载模型
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')
print("模型已加载")

# 测试模型
def test_face_recognition():
    """测试人脸识别模型"""
    # 创建测试图像
    test_images = []
    test_labels = []
    
    # 第一个人的测试图像
    img1 = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.circle(img1, (50, 50), 40, (255, 220, 180), -1)
    cv2.circle(img1, (35, 40), 8, (0, 0, 0), -1)
    cv2.circle(img1, (65, 40), 8, (0, 0, 0), -1)
    cv2.ellipse(img1, (50, 60), (15, 10), 0, 0, 180, (0, 0, 0), 2)
    test_images.append(img1)
    test_labels.append(0)
    
    # 第二个人的测试图像
    img2 = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img2, (10, 10), (90, 90), (255, 200, 160), -1)
    cv2.circle(img2, (35, 40), 8, (0, 0, 0), -1)
    cv2.circle(img2, (65, 40), 8, (0, 0, 0), -1)
    cv2.line(img2, (35, 65), (65, 65), (0, 0, 0), 2)
    test_images.append(img2)
    test_labels.append(1)
    
    return test_images, test_labels

# 测试模型
test_images, test_labels = test_face_recognition()

# 识别结果
results = []
for i, test_img in enumerate(test_images):
    img_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    label, confidence = face_recognizer.predict(img_gray)
    results.append((label, confidence))
    print(f"测试图像 {i+1}: 预测标签={label}, 置信度={confidence:.2f}")

# 可视化识别结果
plt.figure(figsize=(12, 6))
for i, (test_img, true_label, (pred_label, confidence)) in enumerate(zip(test_images, test_labels, results)):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB))
    # 标题
    title = f"真实标签: {true_label}\n预测标签: {pred_label}\n置信度: {confidence:.2f}"
    # 如果预测正确，标题为绿色，否则为红色
    color = 'green' if true_label == pred_label else 'red'
    plt.title(title, color=color)
    plt.axis('off')

plt.tight_layout()
plt.savefig('face_recognition_results.png')
print("人脸识别结果已保存为 face_recognition_results.png")

# 3. 人脸特征点检测
print("\n=== 人脸特征点检测 ===")

# 尝试加载预训练的人脸特征点检测器
try:
    # 加载Dlib的人脸特征点检测器（如果安装了Dlib）
    import dlib
    print("Dlib加载成功")
    # 创建模拟特征点图像
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img, (200, 200), 80, (255, 220, 180), -1)
    
    # 绘制特征点
    feature_points = [
        (170, 180), (230, 180),  # 眼睛
        (200, 200),              # 鼻子
        (180, 230), (220, 230)   # 嘴巴
    ]
    
    for (x, y) in feature_points:
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    
    # 保存特征点检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('人脸特征点检测')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_landmarks.png')
    print("人脸特征点检测结果已保存为 face_landmarks.png")
except ImportError:
    print("Dlib未安装，使用模拟数据进行演示")
    # 创建模拟特征点图像
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # 绘制模拟人脸
    cv2.circle(img, (200, 200), 80, (255, 220, 180), -1)
    
    # 绘制特征点
    feature_points = [
        (170, 180), (230, 180),  # 眼睛
        (200, 200),              # 鼻子
        (180, 230), (220, 230)   # 嘴巴
    ]
    
    for (x, y) in feature_points:
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    
    # 保存特征点检测结果
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('人脸特征点检测')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('face_landmarks.png')
    print("人脸特征点检测结果已保存为 face_landmarks.png")

# 4. 人脸表情识别
print("\n=== 人脸表情识别 ===")

# 创建表情识别示例
def create_emotion_examples():
    """创建表情示例"""
    emotions = ['开心', '悲伤', '惊讶', '愤怒', '中性']
    images = []
    
    for i, emotion in enumerate(emotions):
        img = np.zeros((200, 200, 3), dtype=np.uint8)
        # 绘制人脸
        cv2.circle(img, (100, 100), 80, (255, 220, 180), -1)
        
        if emotion == '开心':
            # 微笑
            cv2.ellipse(img, (100, 120), (30, 20), 0, 0, 180, (0, 0, 0), 2)
        elif emotion == '悲伤':
            # 悲伤的嘴巴
            cv2.ellipse(img, (100, 130), (30, 20), 180, 0, 180, (0, 0, 0), 2)
        elif emotion == '惊讶':
            # 惊讶的嘴巴和眼睛
            cv2.circle(img, (100, 120), 10, (0, 0, 0), 2)
            cv2.circle(img, (70, 80), 12, (0, 0, 0), 2)
            cv2.circle(img, (130, 80), 12, (0, 0, 0), 2)
        elif emotion == '愤怒':
            # 愤怒的眉毛和嘴巴
            cv2.line(img, (70, 70), (90, 80), (0, 0, 0), 2)
            cv2.line(img, (110, 80), (130, 70), (0, 0, 0), 2)
            cv2.line(img, (70, 130), (130, 130), (0, 0, 0), 2)
        else:  # 中性
            # 中性表情
            cv2.line(img, (70, 120), (130, 120), (0, 0, 0), 2)
        
        # 绘制眼睛
        cv2.circle(img, (70, 80), 10, (0, 0, 0), -1)
        cv2.circle(img, (130, 80), 10, (0, 0, 0), -1)
        
        images.append(img)
    
    return images, emotions

# 创建表情示例
emotion_images, emotion_names = create_emotion_examples()

# 保存表情识别结果
plt.figure(figsize=(15, 6))
for i, (img, name) in enumerate(zip(emotion_images, emotion_names)):
    plt.subplot(1, 5, i+1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(name)
    plt.axis('off')

plt.tight_layout()
plt.savefig('emotion_recognition.png')
print("表情识别示例已保存为 emotion_recognition.png")

print("\n人脸识别示例完成！")
