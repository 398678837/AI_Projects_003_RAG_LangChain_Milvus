#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn监督学习
展示Scikit-learn中各种监督学习算法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

# 1. 分类算法
def classification():
    """分类算法"""
    print("\n=== 分类算法 ===")
    
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVC
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 定义分类器
    classifiers = {
        "Logistic Regression": LogisticRegression(),
        "K-Nearest Neighbors": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Support Vector Machine": SVC()
    }
    
    # 训练和评估
    for name, clf in classifiers.items():
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"{name}: {accuracy:.4f}")
    
    print("分类算法示例完成")

# 2. 回归算法
def regression():
    """回归算法"""
    print("\n=== 回归算法 ===")
    
    from sklearn.datasets import load_diabetes
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor
    
    # 加载数据集
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 定义回归器
    regressors = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(),
        "Lasso Regression": Lasso(),
        "K-Nearest Neighbors": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor()
    }
    
    # 训练和评估
    for name, reg in regressors.items():
        reg.fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"{name}: MSE={mse:.4f}, R2={r2:.4f}")
    
    print("回归算法示例完成")

# 3. 支持向量机
def support_vector_machine():
    """支持向量机"""
    print("\n=== 支持向量机 ===")
    
    from sklearn.datasets import load_iris
    from sklearn.svm import SVC, SVR
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    
    # 分类
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 创建SVM分类器管道
    svm_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVC(kernel="rbf", C=1.0, gamma="scale"))
    ])
    
    svm_clf.fit(X_train, y_train)
    accuracy = svm_clf.score(X_test, y_test)
    print(f"SVM Classification Accuracy: {accuracy:.4f}")
    
    # 回归
    from sklearn.datasets import load_diabetes
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 创建SVM回归器管道
    svm_reg = Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVR(kernel="rbf", C=1.0, gamma="scale"))
    ])
    
    svm_reg.fit(X_train, y_train)
    r2 = svm_reg.score(X_test, y_test)
    print(f"SVM Regression R2: {r2:.4f}")
    
    print("支持向量机示例完成")

# 4. 决策树和随机森林
def tree_based_models():
    """决策树和随机森林"""
    print("\n=== 决策树和随机森林 ===")
    
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.model_selection import cross_val_score
    
    # 分类
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 决策树分类器
    dt_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    dt_scores = cross_val_score(dt_clf, X, y, cv=5)
    print(f"Decision Tree Classification: {dt_scores.mean():.4f} ± {dt_scores.std():.4f}")
    
    # 随机森林分类器
    rf_clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
    rf_scores = cross_val_score(rf_clf, X, y, cv=5)
    print(f"Random Forest Classification: {rf_scores.mean():.4f} ± {rf_scores.std():.4f}")
    
    # 回归
    from sklearn.datasets import load_diabetes
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    
    # 决策树回归器
    dt_reg = DecisionTreeRegressor(max_depth=3, random_state=42)
    dt_reg_scores = cross_val_score(dt_reg, X, y, cv=5, scoring="r2")
    print(f"\nDecision Tree Regression: {dt_reg_scores.mean():.4f} ± {dt_reg_scores.std():.4f}")
    
    # 随机森林回归器
    rf_reg = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=42)
    rf_reg_scores = cross_val_score(rf_reg, X, y, cv=5, scoring="r2")
    print(f"Random Forest Regression: {rf_reg_scores.mean():.4f} ± {rf_reg_scores.std():.4f}")
    
    print("决策树和随机森林示例完成")

# 5. 集成学习
def ensemble_learning():
    """集成学习"""
    print("\n=== 集成学习 ===")
    
    from sklearn.datasets import load_iris
    from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # AdaBoost
    ada_clf = AdaBoostClassifier(n_estimators=50, random_state=42)
    ada_scores = cross_val_score(ada_clf, X, y, cv=5)
    print(f"AdaBoost Classification: {ada_scores.mean():.4f} ± {ada_scores.std():.4f}")
    
    # Gradient Boosting
    gb_clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb_scores = cross_val_score(gb_clf, X, y, cv=5)
    print(f"Gradient Boosting Classification: {gb_scores.mean():.4f} ± {gb_scores.std():.4f}")
    
    # Voting Classifier
    estimators = [
        ("lr", LogisticRegression()),
        ("dt", DecisionTreeClassifier()),
        ("svc", SVC(probability=True))
    ]
    voting_clf = VotingClassifier(estimators=estimators, voting="soft")
    voting_scores = cross_val_score(voting_clf, X, y, cv=5)
    print(f"Voting Classifier: {voting_scores.mean():.4f} ± {voting_scores.std():.4f}")
    
    print("集成学习示例完成")

# 主函数
def main():
    print("Scikit-learn Supervised Learning")
    print("=" * 50)
    
    # 运行所有示例
    classification()
    regression()
    support_vector_machine()
    tree_based_models()
    ensemble_learning()
    
    print("\nAll supervised learning examples completed!")

if __name__ == "__main__":
    main()