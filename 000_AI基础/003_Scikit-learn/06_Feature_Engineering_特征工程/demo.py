#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn特征工程
展示Scikit-learn中各种特征工程方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. 特征提取
def feature_extraction():
    """特征提取"""
    print("\n=== 特征提取 ===")
    
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    
    # 文本数据
    texts = [
        "I love machine learning",
        "Machine learning is great",
        "I love Python programming"
    ]
    
    # CountVectorizer
    count_vectorizer = CountVectorizer()
    X_count = count_vectorizer.fit_transform(texts)
    print(f"CountVectorizer shape: {X_count.shape}")
    print(f"Features: {count_vectorizer.get_feature_names_out()}")
    print(f"Matrix:\n{X_count.toarray()}")
    
    # TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()
    X_tfidf = tfidf_vectorizer.fit_transform(texts)
    print(f"\nTfidfVectorizer shape: {X_tfidf.shape}")
    print(f"Matrix:\n{X_tfidf.toarray()}")
    
    print("特征提取示例完成")

# 2. 特征选择
def feature_selection():
    """特征选择"""
    print("\n=== 特征选择 ===")
    
    from sklearn.feature_selection import (
        SelectKBest, SelectPercentile, RFE, SelectFromModel,
        f_classif, mutual_info_classif
    )
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    print(f"Original features: {feature_names}")
    print(f"Original shape: {X.shape}")
    
    # SelectKBest
    selector_kbest = SelectKBest(f_classif, k=2)
    X_kbest = selector_kbest.fit_transform(X, y)
    selected_indices = selector_kbest.get_support(indices=True)
    selected_features = [feature_names[i] for i in selected_indices]
    print(f"\nSelectKBest selected features: {selected_features}")
    print(f"Shape after SelectKBest: {X_kbest.shape}")
    
    # RFE
    estimator = LogisticRegression()
    rfe = RFE(estimator, n_features_to_select=2)
    X_rfe = rfe.fit_transform(X, y)
    selected_rfe = [feature_names[i] for i, selected in enumerate(rfe.support_) if selected]
    print(f"\nRFE selected features: {selected_rfe}")
    print(f"Shape after RFE: {X_rfe.shape}")
    
    # SelectFromModel
    selector_model = SelectFromModel(DecisionTreeClassifier(), threshold="mean")
    X_model = selector_model.fit_transform(X, y)
    selected_model = [feature_names[i] for i, selected in enumerate(selector_model.get_support()) if selected]
    print(f"\nSelectFromModel selected features: {selected_model}")
    print(f"Shape after SelectFromModel: {X_model.shape}")
    
    print("特征选择示例完成")

# 3. 特征变换
def feature_transformation():
    """特征变换"""
    print("\n=== 特征变换 ===")
    
    from sklearn.preprocessing import (
        StandardScaler, MinMaxScaler, RobustScaler,
        PolynomialFeatures, FunctionTransformer
    )
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    print(f"Original shape: {X.shape}")
    print(f"Original data range: [{X.min()}, {X.max()}]")
    
    # 标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(f"\nStandardScaler mean: {X_scaled.mean(axis=0)}")
    print(f"StandardScaler std: {X_scaled.std(axis=0)}")
    
    # 多项式特征
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X)
    print(f"\nPolynomialFeatures shape: {X_poly.shape}")
    
    # 自定义变换
    def log_transform(X):
        return np.log(X + 1)
    
    transformer = FunctionTransformer(log_transform)
    X_log = transformer.transform(X)
    print(f"\nLog transform range: [{X_log.min()}, {X_log.max()}]")
    
    print("特征变换示例完成")

# 4. 特征组合
def feature_combination():
    """特征组合"""
    print("\n=== 特征组合 ===")
    
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score
    
    # 创建模拟数据
    np.random.seed(42)
    X = np.random.rand(100, 2)
    y = X[:, 0] ** 2 + X[:, 1] ** 2 + np.random.randn(100) * 0.1
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 线性回归
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)
    r2_linear = r2_score(y_test, y_pred_linear)
    print(f"Linear regression R2: {r2_linear:.4f}")
    
    # 多项式特征 + 线性回归
    pipeline = Pipeline([
        ('poly', PolynomialFeatures(degree=2)),
        ('model', LinearRegression())
    ])
    
    pipeline.fit(X_train, y_train)
    y_pred_poly = pipeline.predict(X_test)
    r2_poly = r2_score(y_test, y_pred_poly)
    print(f"Polynomial regression R2: {r2_poly:.4f}")
    
    print("特征组合示例完成")

# 5. 特征编码
def feature_encoding():
    """特征编码"""
    print("\n=== 特征编码 ===")
    
    from sklearn.preprocessing import (
        OneHotEncoder, LabelEncoder, OrdinalEncoder,
        LabelBinarizer
    )
    
    # 分类数据
    categorical_data = [
        ['red', 'small', 'cat'],
        ['blue', 'medium', 'dog'],
        ['green', 'large', 'cat'],
        ['red', 'medium', 'dog']
    ]
    
    # OneHotEncoder
    onehot_encoder = OneHotEncoder()
    X_onehot = onehot_encoder.fit_transform(categorical_data)
    print(f"OneHotEncoder shape: {X_onehot.shape}")
    print(f"Categories: {onehot_encoder.categories_}")
    
    # LabelEncoder
    label_encoder = LabelEncoder()
    # 对单个特征进行编码
    color_data = [row[0] for row in categorical_data]
    color_encoded = label_encoder.fit_transform(color_data)
    print(f"\nLabelEncoder classes: {label_encoder.classes_}")
    print(f"Encoded colors: {color_encoded}")
    
    # OrdinalEncoder
    ordinal_encoder = OrdinalEncoder()
    X_ordinal = ordinal_encoder.fit_transform(categorical_data)
    print(f"\nOrdinalEncoder shape: {X_ordinal.shape}")
    print(f"Categories: {ordinal_encoder.categories_}")
    print(f"Encoded data:\n{X_ordinal}")
    
    print("特征编码示例完成")

# 6. 特征工程管道
def feature_engineering_pipeline():
    """特征工程管道"""
    print("\n=== 特征工程管道 ===")
    
    from sklearn.pipeline import Pipeline, FeatureUnion
    from sklearn.preprocessing import StandardScaler, PolynomialFeatures
    from sklearn.feature_selection import SelectKBest, f_classif
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 创建特征工程管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('poly', PolynomialFeatures(degree=2)),
        ('selector', SelectKBest(f_classif, k=5)),
        ('model', LogisticRegression())
    ])
    
    # 训练管道
    pipeline.fit(X_train, y_train)
    
    # 评估管道
    accuracy = pipeline.score(X_test, y_test)
    print(f"Pipeline accuracy: {accuracy:.4f}")
    
    print("特征工程管道示例完成")

# 主函数
def main():
    print("Scikit-learn Feature Engineering")
    print("=" * 50)
    
    # 运行所有示例
    feature_extraction()
    feature_selection()
    feature_transformation()
    feature_combination()
    feature_encoding()
    feature_engineering_pipeline()
    
    print("\nAll feature engineering examples completed!")

if __name__ == "__main__":
    main()