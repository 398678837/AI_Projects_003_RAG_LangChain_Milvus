#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图像分类
展示图像分类的基本方法
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. 数据准备
print("=== 数据准备 ===")

# 创建简单的图像分类数据集
# 类别1：圆形
# 类别2：正方形
# 类别3：三角形

def create_shape_dataset(num_samples=100):
    """创建形状分类数据集"""
    X = []
    y = []
    
    for i in range(num_samples):
        # 创建空白图像
        img = np.zeros((64, 64, 3), dtype=np.uint8)
        
        # 随机选择形状
        shape = np.random.randint(3)
        
        if shape == 0:  # 圆形
            center = (32, 32)
            radius = np.random.randint(10, 20)
            cv2.circle(img, center, radius, (255, 255, 255), -1)
        elif shape == 1:  # 正方形
            size = np.random.randint(20, 30)
            x = (64 - size) // 2
            y_coord = (64 - size) // 2
            cv2.rectangle(img, (x, y_coord), (x+size, y_coord+size), (255, 255, 255), -1)
        else:  # 三角形
            pts = np.array([[32, 12], [12, 52], [52, 52]], np.int32)
            cv2.fillPoly(img, [pts], (255, 255, 255))
        
        # 添加噪声
        noise = np.random.normal(0, 50, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)
        
        # 转换为灰度并扁平化
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_flat = img_gray.flatten()
        
        X.append(img_flat)
        y.append(shape)
    
    return np.array(X), np.array(y)

# 创建数据集
X, y = create_shape_dataset(300)
print(f"数据集大小: {X.shape}")
print(f"类别分布: {np.bincount(y)}")

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"训练集大小: {X_train.shape}")
print(f"测试集大小: {X_test.shape}")

# 2. 模型训练
print("\n=== 模型训练 ===")

# 创建并训练MLP分类器
clf = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
clf.fit(X_train, y_train)
print("模型训练完成")

# 3. 模型评估
print("\n=== 模型评估 ===")

# 预测
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.4f}")

# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("混淆矩阵:")
print(cm)

# 4. 可视化结果
print("\n=== 可视化结果 ===")

# 类别名称
class_names = ['圆形', '正方形', '三角形']

# 显示测试图像和预测结果
plt.figure(figsize=(12, 8))
for i in range(12):
    plt.subplot(3, 4, i+1)
    # 重塑图像
    img = X_test[i].reshape(64, 64)
    plt.imshow(img, cmap='gray')
    # 真实标签和预测标签
    true_label = class_names[y_test[i]]
    pred_label = class_names[y_pred[i]]
    # 标题
    title = f"真实: {true_label}\n预测: {pred_label}"
    # 如果预测正确，标题为绿色，否则为红色
    color = 'green' if true_label == pred_label else 'red'
    plt.title(title, color=color)
    plt.axis('off')

plt.tight_layout()
plt.savefig('classification_results.png')
print("分类结果已保存为 classification_results.png")

# 5. 特征提取
print("\n=== 特征提取 ===")

# 提取简单特征
def extract_features(img_flat):
    """提取图像特征"""
    img = img_flat.reshape(64, 64)
    
    # 计算均值
    mean = np.mean(img)
    
    # 计算标准差
    std = np.std(img)
    
    # 计算边缘密度
    edges = cv2.Canny(img, 100, 200)
    edge_density = np.sum(edges) / (64 * 64)
    
    return [mean, std, edge_density]

# 提取特征
X_train_features = np.array([extract_features(x) for x in X_train])
X_test_features = np.array([extract_features(x) for x in X_test])

print(f"提取的特征形状: {X_train_features.shape}")

# 使用特征训练模型
clf_features = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=42)
clf_features.fit(X_train_features, y_train)

# 评估特征模型
y_pred_features = clf_features.predict(X_test_features)
accuracy_features = accuracy_score(y_test, y_pred_features)
print(f"基于特征的模型准确率: {accuracy_features:.4f}")

# 6. 可视化特征
print("\n=== 可视化特征 ===")

# 绘制特征散点图
plt.figure(figsize=(12, 8))

# 均值 vs 标准差
plt.subplot(2, 2, 1)
for i in range(3):
    mask = y_test == i
    plt.scatter(X_test_features[mask, 0], X_test_features[mask, 1], label=class_names[i], alpha=0.5)
plt.xlabel('均值')
plt.ylabel('标准差')
plt.title('均值 vs 标准差')
plt.legend()

# 均值 vs 边缘密度
plt.subplot(2, 2, 2)
for i in range(3):
    mask = y_test == i
    plt.scatter(X_test_features[mask, 0], X_test_features[mask, 2], label=class_names[i], alpha=0.5)
plt.xlabel('均值')
plt.ylabel('边缘密度')
plt.title('均值 vs 边缘密度')
plt.legend()

# 标准差 vs 边缘密度
plt.subplot(2, 2, 3)
for i in range(3):
    mask = y_test == i
    plt.scatter(X_test_features[mask, 1], X_test_features[mask, 2], label=class_names[i], alpha=0.5)
plt.xlabel('标准差')
plt.ylabel('边缘密度')
plt.title('标准差 vs 边缘密度')
plt.legend()

plt.tight_layout()
plt.savefig('feature_visualization.png')
print("特征可视化结果已保存为 feature_visualization.png")

# 7. 模型保存与加载
print("\n=== 模型保存与加载 ===")

import joblib

# 保存模型
joblib.dump(clf, 'shape_classifier.pkl')
print("模型已保存为 shape_classifier.pkl")

# 加载模型
loaded_clf = joblib.load('shape_classifier.pkl')
print("模型已加载")

# 测试加载的模型
loaded_y_pred = loaded_clf.predict(X_test)
loaded_accuracy = accuracy_score(y_test, loaded_y_pred)
print(f"加载模型的准确率: {loaded_accuracy:.4f}")

print("\n图像分类示例完成！")
