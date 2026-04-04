#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scikit-learn无监督学习
展示Scikit-learn中各种无监督学习算法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, make_blobs, make_moons

# 1. 聚类算法
def clustering():
    """聚类算法"""
    print("\n=== 聚类算法 ===")
    
    from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
    from sklearn.metrics import silhouette_score
    
    # 创建模拟数据
    X, y = make_blobs(n_samples=300, centers=4, random_state=42)
    print(f"Data shape: {X.shape}")
    
    # K-means聚类
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)
    kmeans_score = silhouette_score(X, kmeans_labels)
    print(f"K-means silhouette score: {kmeans_score:.4f}")
    
    # 层次聚类
    agglomerative = AgglomerativeClustering(n_clusters=4)
    agglomerative_labels = agglomerative.fit_predict(X)
    agglomerative_score = silhouette_score(X, agglomerative_labels)
    print(f"Agglomerative silhouette score: {agglomerative_score:.4f}")
    
    # DBSCAN聚类
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X)
    # 计算轮廓系数（排除噪声点）
    if len(set(dbscan_labels)) > 1:
        dbscan_score = silhouette_score(X, dbscan_labels)
        print(f"DBSCAN silhouette score: {dbscan_score:.4f}")
    else:
        print("DBSCAN found only one cluster or all noise points")
    
    print("聚类算法示例完成")

# 2. 降维算法
def dimensionality_reduction():
    """降维算法"""
    print("\n=== 降维算法 ===")
    
    from sklearn.decomposition import PCA, TruncatedSVD
    from sklearn.manifold import TSNE, Isomap
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    y = iris.target
    print(f"Original data shape: {X.shape}")
    
    # PCA降维
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    print(f"PCA reduced shape: {X_pca.shape}")
    print(f"PCA explained variance ratio: {pca.explained_variance_ratio_}")
    
    # t-SNE降维
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X)
    print(f"t-SNE reduced shape: {X_tsne.shape}")
    
    # Isomap降维
    isomap = Isomap(n_components=2)
    X_isomap = isomap.fit_transform(X)
    print(f"Isomap reduced shape: {X_isomap.shape}")
    
    # TruncatedSVD降维
    svd = TruncatedSVD(n_components=2)
    X_svd = svd.fit_transform(X)
    print(f"TruncatedSVD reduced shape: {X_svd.shape}")
    
    print("降维算法示例完成")

# 3. 密度估计
def density_estimation():
    """密度估计"""
    print("\n=== 密度估计 ===")
    
    from sklearn.neighbors import KernelDensity
    from sklearn.mixture import GaussianMixture
    import numpy as np
    
    # 创建模拟数据
    np.random.seed(42)
    X = np.concatenate([
        np.random.normal(0, 1, 1000),
        np.random.normal(5, 1, 1000)
    ]).reshape(-1, 1)
    print(f"Data shape: {X.shape}")
    
    # 核密度估计
    kde = KernelDensity(kernel='gaussian', bandwidth=0.5)
    kde.fit(X)
    
    # 生成测试点
    x_test = np.linspace(-5, 10, 1000).reshape(-1, 1)
    log_density = kde.score_samples(x_test)
    density = np.exp(log_density)
    print(f"KDE - Min density: {density.min():.4f}, Max density: {density.max():.4f}")
    
    # 高斯混合模型
    gmm = GaussianMixture(n_components=2, random_state=42)
    gmm.fit(X)
    gmm_density = np.exp(gmm.score_samples(x_test))
    print(f"GMM - Min density: {gmm_density.min():.4f}, Max density: {gmm_density.max():.4f}")
    
    print("密度估计示例完成")

# 4. 异常检测
def anomaly_detection():
    """异常检测"""
    print("\n=== 异常检测 ===")
    
    from sklearn.ensemble import IsolationForest
    from sklearn.neighbors import LocalOutlierFactor
    from sklearn.covariance import EllipticEnvelope
    
    # 创建包含异常值的数据
    np.random.seed(42)
    X = np.concatenate([
        np.random.normal(0, 1, (200, 2)),
        np.random.normal(10, 1, (20, 2))  # 异常值
    ])
    print(f"Data shape: {X.shape}")
    
    # Isolation Forest
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    iso_labels = iso_forest.fit_predict(X)
    print(f"Isolation Forest - Number of outliers: {np.sum(iso_labels == -1)}")
    
    # Local Outlier Factor
    lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
    lof_labels = lof.fit_predict(X)
    print(f"Local Outlier Factor - Number of outliers: {np.sum(lof_labels == -1)}")
    
    # Elliptic Envelope
    ee = EllipticEnvelope(contamination=0.1, random_state=42)
    ee_labels = ee.fit_predict(X)
    print(f"Elliptic Envelope - Number of outliers: {np.sum(ee_labels == -1)}")
    
    print("异常检测示例完成")

# 5. 特征学习
def feature_learning():
    """特征学习"""
    print("\n=== 特征学习 ===")
    
    from sklearn.decomposition import PCA, NMF
    from sklearn.preprocessing import StandardScaler
    
    # 加载数据集
    iris = load_iris()
    X = iris.data
    print(f"Original data shape: {X.shape}")
    
    # 标准化数据
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # PCA特征学习
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    print(f"PCA features shape: {X_pca.shape}")
    
    # NMF特征学习
    nmf = NMF(n_components=2, random_state=42)
    X_nmf = nmf.fit_transform(X_scaled)
    print(f"NMF features shape: {X_nmf.shape}")
    
    print("特征学习示例完成")

# 主函数
def main():
    print("Scikit-learn Unsupervised Learning")
    print("=" * 50)
    
    # 运行所有示例
    clustering()
    dimensionality_reduction()
    density_estimation()
    anomaly_detection()
    feature_learning()
    
    print("\nAll unsupervised learning examples completed!")

if __name__ == "__main__":
    main()