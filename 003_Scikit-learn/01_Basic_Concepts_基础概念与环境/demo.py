#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn基础概念与环境
展示Scikit-learn的基本架构、核心组件和环境配置
"""

import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 打印Scikit-learn版本
print(f"Scikit-learn version: {sklearn.__version__}")

# 1. 基础数据结构
def basic_data_structures():
    """基础数据结构"""
    print("\n=== 基础数据结构 ===")
    
    # 创建特征矩阵 (n_samples, n_features)
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Feature matrix shape: {X.shape}")
    print(f"Feature matrix:\n{X}")
    
    # 创建目标向量 (n_samples,)
    y = np.array([0, 1, 0])
    print(f"\nTarget vector shape: {y.shape}")
    print(f"Target vector: {y}")
    
    # 使用pandas DataFrame
    df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
    df['target'] = y
    print(f"\nDataFrame:\n{df}")
    
    print("基础数据结构示例完成")

# 2. 数据集加载
def load_datasets():
    """数据集加载"""
    print("\n=== 数据集加载 ===")
    
    # 加载内置数据集
    from sklearn.datasets import load_iris, load_digits, load_wine
    
    # 加载iris数据集
    iris = load_iris()
    print(f"Iris dataset: {iris.data.shape} samples, {iris.data.shape[1]} features")
    print(f"Target names: {iris.target_names}")
    print(f"Feature names: {iris.feature_names}")
    
    # 加载digits数据集
    digits = load_digits()
    print(f"\nDigits dataset: {digits.data.shape} samples, {digits.data.shape[1]} features")
    
    # 加载wine数据集
    wine = load_wine()
    print(f"\nWine dataset: {wine.data.shape} samples, {wine.data.shape[1]} features")
    
    print("数据集加载完成")

# 3. 数据预处理
def data_preprocessing():
    """数据预处理"""
    print("\n=== 数据预处理 ===")
    
    # 加载数据集
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(f"Original data mean: {X.mean(axis=0)}")
    print(f"Scaled data mean: {X_scaled.mean(axis=0)}")
    print(f"Scaled data std: {X_scaled.std(axis=0)}")
    
    # 归一化
    minmax_scaler = MinMaxScaler()
    X_minmax = minmax_scaler.fit_transform(X)
    print(f"\nMinMax scaled data range: [{X_minmax.min()}, {X_minmax.max()}]")
    
    # 独热编码
    encoder = OneHotEncoder()
    y_onehot = encoder.fit_transform(y.reshape(-1, 1))
    print(f"\nOne-hot encoded target shape: {y_onehot.shape}")
    
    print("数据预处理示例完成")

# 4. 模型训练与预测
def model_training():
    """模型训练与预测"""
    print("\n=== 模型训练与预测 ===")
    
    # 加载数据集
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # 训练模型
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    print(f"\nPredictions: {y_pred}")
    print(f"True values: {y_test}")
    
    # 计算准确率
    accuracy = model.score(X_test, y_test)
    print(f"\nAccuracy: {accuracy:.4f}")
    
    print("模型训练与预测示例完成")

# 5. 模型评估
def model_evaluation():
    """模型评估"""
    print("\n=== 模型评估 ===")
    
    # 加载数据集
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练模型
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 计算评估指标
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    
    print("模型评估示例完成")

# 6. 交叉验证
def cross_validation():
    """交叉验证"""
    print("\n=== 交叉验证 ===")
    
    # 加载数据集
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 创建模型
    model = LogisticRegression()
    
    # 5折交叉验证
    scores = cross_val_score(model, X, y, cv=5)
    print(f"Cross-validation scores: {scores}")
    print(f"Mean score: {scores.mean():.4f}")
    print(f"Standard deviation: {scores.std():.4f}")
    
    print("交叉验证示例完成")

# 主函数
def main():
    print("Scikit-learn Basic Concepts and Environment")
    print("=" * 50)
    
    # 运行所有示例
    basic_data_structures()
    load_datasets()
    data_preprocessing()
    model_training()
    model_evaluation()
    cross_validation()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main()