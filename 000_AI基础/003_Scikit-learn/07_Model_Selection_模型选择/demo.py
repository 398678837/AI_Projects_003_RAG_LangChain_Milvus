#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn模型选择
展示Scikit-learn中各种模型选择方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split

# 1. 网格搜索
def grid_search():
    """网格搜索"""
    print("\n=== 网格搜索 ===")
    
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
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
    
    print("网格搜索示例完成")

# 2. 随机搜索
def random_search():
    """随机搜索"""
    print("\n=== 随机搜索 ===")
    
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.ensemble import RandomForestClassifier
    import scipy.stats as stats
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 定义参数分布
    param_dist = {
        'n_estimators': stats.randint(10, 200),
        'max_depth': stats.randint(1, 10),
        'min_samples_split': stats.randint(2, 10),
        'min_samples_leaf': stats.randint(1, 5),
        'bootstrap': [True, False]
    }
    
    # 随机搜索
    random_search = RandomizedSearchCV(
        RandomForestClassifier(),
        param_distributions=param_dist,
        n_iter=100,
        cv=5,
        scoring='accuracy',
        random_state=42,
        n_jobs=-1
    )
    
    random_search.fit(X_train, y_train)
    
    print(f"Best parameters: {random_search.best_params_}")
    print(f"Best cross-validation score: {random_search.best_score_:.4f}")
    print(f"Test score: {random_search.score(X_test, y_test):.4f}")
    
    print("随机搜索示例完成")

# 3. 贝叶斯优化
def bayesian_optimization():
    """贝叶斯优化"""
    print("\n=== 贝叶斯优化 ===")
    
    try:
        from skopt import BayesSearchCV
        from skopt.space import Real, Categorical, Integer
    except ImportError:
        print("需要安装scikit-optimize: pip install scikit-optimize")
        return
    
    from sklearn.svm import SVC
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 创建管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC())
    ])
    
    # 定义参数空间
    search_space = {
        'svm__C': Real(1e-6, 1e+6, prior='log-uniform'),
        'svm__gamma': Real(1e-6, 1e+1, prior='log-uniform'),
        'svm__kernel': Categorical(['linear', 'rbf'])
    }
    
    # 贝叶斯搜索
    bayes_search = BayesSearchCV(
        pipeline,
        search_space,
        n_iter=30,
        cv=5,
        scoring='accuracy',
        random_state=42,
        n_jobs=-1
    )
    
    bayes_search.fit(X_train, y_train)
    
    print(f"Best parameters: {bayes_search.best_params_}")
    print(f"Best cross-validation score: {bayes_search.best_score_:.4f}")
    print(f"Test score: {bayes_search.score(X_test, y_test):.4f}")
    
    print("贝叶斯优化示例完成")

# 4. 模型评估与比较
def model_evaluation_comparison():
    """模型评估与比较"""
    print("\n=== 模型评估与比较 ===")
    
    from sklearn.linear_model import LogisticRegression, LinearRegression
    from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.svm import SVC, SVR
    from sklearn.model_selection import cross_val_score
    
    # 分类任务
    iris = load_iris()
    X_clf = iris.data
    y_clf = iris.target
    
    # 回归任务
    diabetes = load_diabetes()
    X_reg = diabetes.data
    y_reg = diabetes.target
    
    # 分类模型
    classifiers = {
        "Logistic Regression": LogisticRegression(),
        "K-Nearest Neighbors": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Support Vector Machine": SVC()
    }
    
    # 回归模型
    regressors = {
        "Linear Regression": LinearRegression(),
        "K-Nearest Neighbors": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "Support Vector Machine": SVR()
    }
    
    # 评估分类模型
    print("分类模型评估:")
    for name, clf in classifiers.items():
        scores = cross_val_score(clf, X_clf, y_clf, cv=5, scoring='accuracy')
        print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")
    
    # 评估回归模型
    print("\n回归模型评估:")
    for name, reg in regressors.items():
        scores = cross_val_score(reg, X_reg, y_reg, cv=5, scoring='r2')
        print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")
    
    print("模型评估与比较示例完成")

# 5. 模型选择最佳实践
def model_selection_best_practices():
    """模型选择最佳实践"""
    print("\n=== 模型选择最佳实践 ===")
    
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, PolynomialFeatures
    from sklearn.feature_selection import SelectKBest, f_classif
    from sklearn.model_selection import GridSearchCV, StratifiedKFold
    from sklearn.ensemble import RandomForestClassifier
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # 创建完整的管道
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('poly', PolynomialFeatures(degree=2)),
        ('selector', SelectKBest(f_classif)),
        ('model', RandomForestClassifier())
    ])
    
    # 定义参数网格
    param_grid = {
        'poly__degree': [1, 2, 3],
        'selector__k': [2, 3, 4],
        'model__n_estimators': [50, 100, 200],
        'model__max_depth': [3, 5, 7]
    }
    
    # 使用分层K折交叉验证
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # 网格搜索
    grid_search = GridSearchCV(
        pipeline,
        param_grid,
        cv=cv,
        scoring='accuracy',
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X, y)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_:.4f}")
    
    # 特征重要性
    best_model = grid_search.best_estimator_['model']
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        print(f"\nFeature importances: {importances[:5]}...")
    
    print("模型选择最佳实践示例完成")

# 主函数
def main():
    print("Scikit-learn Model Selection")
    print("=" * 50)
    
    # 运行所有示例
    grid_search()
    random_search()
    bayesian_optimization()
    model_evaluation_comparison()
    model_selection_best_practices()
    
    print("\nAll model selection examples completed!")

if __name__ == "__main__":
    main()