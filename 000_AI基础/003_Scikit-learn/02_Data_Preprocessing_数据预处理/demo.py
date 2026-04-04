#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn数据预处理
展示Scikit-learn中各种数据预处理方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# 1. 数据标准化
def data_standardization():
    """数据标准化"""
    print("\n=== 数据标准化 ===")
    
    from sklearn.preprocessing import StandardScaler
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print(f"Original data mean: {X.mean(axis=0)}")
    print(f"Original data std: {X.std(axis=0)}")
    print(f"Scaled data mean: {X_scaled.mean(axis=0)}")
    print(f"Scaled data std: {X_scaled.std(axis=0)}")
    
    print("数据标准化完成")

# 2. 数据归一化
def data_normalization():
    """数据归一化"""
    print("\n=== 数据归一化 ===")
    
    from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, RobustScaler
    
    # MinMaxScaler
    minmax_scaler = MinMaxScaler()
    X_minmax = minmax_scaler.fit_transform(X)
    print(f"MinMaxScaler - Min: {X_minmax.min(axis=0)}")
    print(f"MinMaxScaler - Max: {X_minmax.max(axis=0)}")
    
    # MaxAbsScaler
    maxabs_scaler = MaxAbsScaler()
    X_maxabs = maxabs_scaler.fit_transform(X)
    print(f"\nMaxAbsScaler - Min: {X_maxabs.min(axis=0)}")
    print(f"MaxAbsScaler - Max: {X_maxabs.max(axis=0)}")
    
    # RobustScaler
    robust_scaler = RobustScaler()
    X_robust = robust_scaler.fit_transform(X)
    print(f"\nRobustScaler - Mean: {X_robust.mean(axis=0)}")
    print(f"RobustScaler - Std: {X_robust.std(axis=0)}")
    
    print("数据归一化完成")

# 3. 数据编码
def data_encoding():
    """数据编码"""
    print("\n=== 数据编码 ===")
    
    from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
    
    # 标签编码
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    print(f"LabelEncoder - Classes: {label_encoder.classes_}")
    print(f"LabelEncoder - Encoded: {y_encoded[:10]}")
    
    # 独热编码
    onehot_encoder = OneHotEncoder()
    y_onehot = onehot_encoder.fit_transform(y.reshape(-1, 1))
    print(f"\nOneHotEncoder - Shape: {y_onehot.shape}")
    print(f"OneHotEncoder - Encoded: {y_onehot.toarray()[:5]}")
    
    # 序数编码
    ordinal_encoder = OrdinalEncoder()
    # 创建一个分类特征
    categorical_feature = np.array([['setosa'], ['versicolor'], ['virginica']] * 50)
    X_categorical = ordinal_encoder.fit_transform(categorical_feature)
    print(f"\nOrdinalEncoder - Classes: {ordinal_encoder.categories_}")
    print(f"OrdinalEncoder - Encoded: {X_categorical[:10].flatten()}")
    
    print("数据编码完成")

# 4. 缺失值处理
def missing_value_handling():
    """缺失值处理"""
    print("\n=== 缺失值处理 ===")
    
    from sklearn.impute import SimpleImputer, KNNImputer
    
    # 创建包含缺失值的数据
    X_with_missing = X.copy()
    # 随机设置10%的缺失值
    np.random.seed(42)
    mask = np.random.rand(*X_with_missing.shape) < 0.1
    X_with_missing[mask] = np.nan
    print(f"Original data shape: {X.shape}")
    print(f"Data with missing values shape: {X_with_missing.shape}")
    print(f"Number of missing values: {np.isnan(X_with_missing).sum()}")
    
    # 均值填充
    imputer_mean = SimpleImputer(strategy='mean')
    X_imputed_mean = imputer_mean.fit_transform(X_with_missing)
    print(f"\nMean imputation - Missing values after: {np.isnan(X_imputed_mean).sum()}")
    
    # 中位数填充
    imputer_median = SimpleImputer(strategy='median')
    X_imputed_median = imputer_median.fit_transform(X_with_missing)
    print(f"Median imputation - Missing values after: {np.isnan(X_imputed_median).sum()}")
    
    # KNN填充
    imputer_knn = KNNImputer(n_neighbors=5)
    X_imputed_knn = imputer_knn.fit_transform(X_with_missing)
    print(f"KNN imputation - Missing values after: {np.isnan(X_imputed_knn).sum()}")
    
    print("缺失值处理完成")

# 5. 特征选择
def feature_selection():
    """特征选择"""
    print("\n=== 特征选择 ===")
    
    from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold
    
    # 方差阈值选择
    selector_var = VarianceThreshold(threshold=0.1)
    X_selected_var = selector_var.fit_transform(X)
    print(f"Original features: {X.shape[1]}")
    print(f"Features after variance threshold: {X_selected_var.shape[1]}")
    print(f"Selected features: {selector_var.get_support()}")
    
    # 基于统计测试的选择
    selector_kbest = SelectKBest(f_classif, k=2)
    X_selected_kbest = selector_kbest.fit_transform(X, y)
    print(f"\nFeatures after KBest: {X_selected_kbest.shape[1]}")
    print(f"Selected features: {selector_kbest.get_support()}")
    print(f"Feature scores: {selector_kbest.scores_}")
    
    print("特征选择完成")

# 6. 数据变换
def data_transformation():
    """数据变换"""
    print("\n=== 数据变换 ===")
    
    from sklearn.preprocessing import PolynomialFeatures, FunctionTransformer
    
    # 多项式特征
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X)
    print(f"Original features: {X.shape[1]}")
    print(f"Polynomial features: {X_poly.shape[1]}")
    print(f"Feature names: {poly.get_feature_names_out(feature_names)[:10]}")
    
    # 自定义变换
    def log_transform(X):
        return np.log(X + 1)  # +1 to avoid log(0)
    
    transformer = FunctionTransformer(log_transform)
    X_log = transformer.transform(X)
    print(f"\nOriginal data range: [{X.min()}, {X.max()}]")
    print(f"Log transformed range: [{X_log.min()}, {X_log.max()}]")
    
    print("数据变换完成")

# 7. 管道
def pipeline():
    """管道"""
    print("\n=== 管道 ===")
    
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练管道
    pipeline.fit(X_train, y_train)
    
    # 评估管道
    accuracy = pipeline.score(X_test, y_test)
    print(f"Pipeline accuracy: {accuracy:.4f}")
    
    print("管道示例完成")

# 主函数
def main():
    print("Scikit-learn Data Preprocessing")
    print("=" * 50)
    
    # 运行所有示例
    data_standardization()
    data_normalization()
    data_encoding()
    missing_value_handling()
    feature_selection()
    data_transformation()
    pipeline()
    
    print("\nAll data preprocessing examples completed!")

if __name__ == "__main__":
    main()