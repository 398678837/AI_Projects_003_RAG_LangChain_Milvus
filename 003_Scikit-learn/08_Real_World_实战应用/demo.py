#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn实战应用
展示Scikit-learn在实际应用中的使用
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error, r2_score

# 1. 分类实战：鸢尾花分类
def iris_classification():
    """鸢尾花分类"""
    print("\n=== 鸢尾花分类 ===")
    
    from sklearn.datasets import load_iris
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # 训练模型
    pipeline.fit(X_train, y_train)
    
    # 评估模型
    y_pred = pipeline.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # 特征重要性
    feature_importances = pipeline.named_steps['model'].feature_importances_
    print("\nFeature Importances:")
    for name, importance in zip(feature_names, feature_importances):
        print(f"{name}: {importance:.4f}")
    
    print("鸢尾花分类示例完成")

# 2. 回归实战：房价预测
def house_price_prediction():
    """房价预测"""
    print("\n=== 房价预测 ===")
    
    from sklearn.datasets import fetch_california_housing
    
    # 加载数据集
    housing = fetch_california_housing()
    X = housing.data
    y = housing.target
    feature_names = housing.feature_names
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    # 训练模型
    pipeline.fit(X_train, y_train)
    
    # 评估模型
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    
    # 特征重要性
    feature_importances = pipeline.named_steps['model'].feature_importances_
    print("\nFeature Importances:")
    for name, importance in zip(feature_names, feature_importances):
        print(f"{name}: {importance:.4f}")
    
    print("房价预测示例完成")

# 3. 预处理实战：处理混合类型数据
def mixed_data_preprocessing():
    """处理混合类型数据"""
    print("\n=== 处理混合类型数据 ===")
    
    # 创建模拟数据
    np.random.seed(42)
    data = {
        'age': np.random.randint(18, 70, 100),
        'income': np.random.normal(50000, 15000, 100),
        'gender': np.random.choice(['Male', 'Female'], 100),
        'occupation': np.random.choice(['Engineer', 'Doctor', 'Teacher', 'Lawyer'], 100),
        'score': np.random.normal(75, 10, 100)
    }
    
    # 添加缺失值
    for i in range(5):
        data['age'][i] = np.nan
        data['income'][i+5] = np.nan
        data['gender'][i+10] = np.nan
    
    df = pd.DataFrame(data)
    print(f"Original data shape: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}")
    
    # 定义特征和目标
    X = df.drop('score', axis=1)
    y = df['score']
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 定义预处理步骤
    numeric_features = ['age', 'income']
    categorical_features = ['gender', 'occupation']
    
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # 组合预处理步骤
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
    
    # 创建完整管道
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    # 训练模型
    pipeline.fit(X_train, y_train)
    
    # 评估模型
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    
    print("处理混合类型数据示例完成")

# 4. 模型选择实战：网格搜索调优
def grid_search_tuning():
    """网格搜索调优"""
    print("\n=== 网格搜索调优 ===")
    
    from sklearn.datasets import load_wine
    from sklearn.svm import SVC
    
    # 加载数据集
    wine = load_wine()
    X = wine.data
    y = wine.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC())
    ])
    
    # 定义参数网格
    param_grid = {
        'svm__C': [0.1, 1, 10, 100],
        'svm__kernel': ['linear', 'rbf', 'poly'],
        'svm__gamma': ['scale', 'auto']
    }
    
    # 网格搜索
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_:.4f}")
    print(f"Test score: {grid_search.score(X_test, y_test):.4f}")
    
    print("网格搜索调优示例完成")

# 5. 集成学习实战：堆叠模型
def stacking_ensemble():
    """堆叠模型"""
    print("\n=== 堆叠模型 ===")
    
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import StackingClassifier
    
    # 加载数据集
    cancer = load_breast_cancer()
    X = cancer.data
    y = cancer.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 定义基础模型
    base_estimators = [
        ('knn', KNeighborsClassifier()),
        ('dt', DecisionTreeClassifier()),
        ('lr', LogisticRegression())
    ]
    
    # 定义堆叠分类器
    stacking_clf = StackingClassifier(
        estimators=base_estimators,
        final_estimator=LogisticRegression(),
        cv=5
    )
    
    # 训练模型
    stacking_clf.fit(X_train, y_train)
    
    # 评估模型
    accuracy = stacking_clf.score(X_test, y_test)
    print(f"Stacking Classifier Accuracy: {accuracy:.4f}")
    
    # 比较基础模型
    for name, model in base_estimators:
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(f"{name} Accuracy: {score:.4f}")
    
    print("堆叠模型示例完成")

# 主函数
def main():
    print("Scikit-learn Real World Applications")
    print("=" * 50)
    
    # 运行所有示例
    iris_classification()
    house_price_prediction()
    mixed_data_preprocessing()
    grid_search_tuning()
    stacking_ensemble()
    
    print("\nAll real world application examples completed!")

if __name__ == "__main__":
    main()