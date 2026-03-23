#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn模型评估
展示Scikit-learn中各种模型评估方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_diabetes

# 1. 分类模型评估
def classification_evaluation():
    """分类模型评估"""
    print("\n=== 分类模型评估 ===")
    
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score, f1_score,
        confusion_matrix, classification_report, roc_curve, auc
    )
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练模型
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)
    
    # 评估指标
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    
    # 混淆矩阵
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix:\n{cm}")
    
    # 分类报告
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # ROC曲线和AUC（二分类）
    if len(np.unique(y)) == 2:
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        print(f"\nROC AUC: {roc_auc:.4f}")
    
    print("分类模型评估示例完成")

# 2. 回归模型评估
def regression_evaluation():
    """回归模型评估"""
    print("\n=== 回归模型评估 ===")
    
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import (
        mean_squared_error, mean_absolute_error, r2_score,
        mean_squared_log_error, median_absolute_error
    )
    
    # 加载数据集
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # 评估指标
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    msle = mean_squared_log_error(y_test, y_pred)
    medae = median_absolute_error(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"Mean Absolute Error: {mae:.4f}")
    print(f"R2 Score: {r2:.4f}")
    print(f"Mean Squared Log Error: {msle:.4f}")
    print(f"Median Absolute Error: {medae:.4f}")
    
    print("回归模型评估示例完成")

# 3. 交叉验证
def cross_validation():
    """交叉验证"""
    print("\n=== 交叉验证 ===")
    
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 创建模型
    model = LogisticRegression()
    
    # K折交叉验证
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=kfold)
    print(f"KFold Cross-Validation Scores: {scores}")
    print(f"Mean Score: {scores.mean():.4f}")
    print(f"Standard Deviation: {scores.std():.4f}")
    
    # 分层K折交叉验证
    stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    stratified_scores = cross_val_score(model, X, y, cv=stratified_kfold)
    print(f"\nStratified KFold Cross-Validation Scores: {stratified_scores}")
    print(f"Mean Score: {stratified_scores.mean():.4f}")
    print(f"Standard Deviation: {stratified_scores.std():.4f}")
    
    print("交叉验证示例完成")

# 4. 模型选择
def model_selection():
    """模型选择"""
    print("\n=== 模型选择 ===")
    
    from sklearn.linear_model import LogisticRegression, Ridge
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    
    # 网格搜索
    param_grid = {
        'model__C': [0.1, 1, 10, 100],
        'model__penalty': ['l1', 'l2'],
        'model__solver': ['liblinear']
    }
    
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X, y)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_:.4f}")
    
    # 随机搜索
    param_dist = {
        'model__C': np.logspace(-3, 3, 7),
        'model__penalty': ['l1', 'l2'],
        'model__solver': ['liblinear']
    }
    
    random_search = RandomizedSearchCV(pipeline, param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)
    random_search.fit(X, y)
    
    print(f"\nRandomized search best parameters: {random_search.best_params_}")
    print(f"Randomized search best score: {random_search.best_score_:.4f}")
    
    print("模型选择示例完成")

# 5. 模型持久化
def model_persistence():
    """模型持久化"""
    print("\n=== 模型持久化 ===")
    
    from sklearn.linear_model import LogisticRegression
    import joblib
    import os
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 训练模型
    model = LogisticRegression()
    model.fit(X, y)
    
    # 保存模型
    model_path = "model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
    # 加载模型
    loaded_model = joblib.load(model_path)
    print("Model loaded successfully")
    
    # 测试加载的模型
    test_sample = X[0:1]
    prediction = loaded_model.predict(test_sample)
    print(f"Test prediction: {prediction}")
    
    # 清理
    if os.path.exists(model_path):
        os.remove(model_path)
        print(f"Model file {model_path} removed")
    
    print("模型持久化示例完成")

# 主函数
def main():
    print("Scikit-learn Model Evaluation")
    print("=" * 50)
    
    # 运行所有示例
    classification_evaluation()
    regression_evaluation()
    cross_validation()
    model_selection()
    model_persistence()
    
    print("\nAll model evaluation examples completed!")

if __name__ == "__main__":
    main()