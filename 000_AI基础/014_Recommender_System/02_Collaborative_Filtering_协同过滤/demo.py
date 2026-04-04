#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
协同过滤
展示协同过滤推荐算法的基本方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import os

# 1. 基于用户的协同过滤
print("=== 基于用户的协同过滤 ===")

def create_user_item_matrix():
    """创建用户-物品评分矩阵"""
    users = ["User1", "User2", "User3", "User4", "User5"]
    items = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6"]
    
    # 评分矩阵 (1-5分，0表示未评分)
    ratings = np.array([
        [5, 4, 0, 0, 3, 0],
        [0, 5, 5, 0, 0, 3],
        [4, 0, 0, 5, 0, 0],
        [0, 0, 4, 0, 5, 5],
        [3, 0, 0, 4, 0, 0]
    ])
    
    return users, items, ratings

# 创建用户-物品矩阵
users, items, ratings = create_user_item_matrix()

print("用户-物品评分矩阵:")
print(pd.DataFrame(ratings, index=users, columns=items))

# 计算用户相似度
def calculate_user_similarity(ratings):
    """计算用户之间的相似度"""
    # 去除未评分的物品，计算用户向量
    user_vectors = []
    for user_ratings in ratings:
        # 只考虑有评分的物品
        user_vector = user_ratings[user_ratings != 0]
        # 标准化（减去均值）
        if len(user_vector) > 0:
            user_vector = user_vector - np.mean(user_vector)
        user_vectors.append(user_vector)
    
    # 计算相似度矩阵
    n_users = ratings.shape[0]
    similarity_matrix = np.zeros((n_users, n_users))
    
    for i in range(n_users):
        for j in range(n_users):
            if i == j:
                similarity_matrix[i, j] = 1.0
            else:
                # 找到两个用户共同评分的物品
                common_items = np.where((ratings[i] != 0) & (ratings[j] != 0))[0]
                if len(common_items) > 0:
                    # 提取共同评分
                    user_i_ratings = ratings[i][common_items]
                    user_j_ratings = ratings[j][common_items]
                    
                    # 计算余弦相似度
                    norm_i = np.linalg.norm(user_i_ratings)
                    norm_j = np.linalg.norm(user_j_ratings)
                    if norm_i > 0 and norm_j > 0:
                        similarity = np.dot(user_i_ratings, user_j_ratings) / (norm_i * norm_j)
                    else:
                        similarity = 0
                else:
                    similarity = 0
                similarity_matrix[i, j] = similarity
    
    return similarity_matrix

# 计算用户相似度矩阵
user_similarity = calculate_user_similarity(ratings)
print("\n用户相似度矩阵:")
print(pd.DataFrame(user_similarity, index=users, columns=users))

# 基于用户的协同过滤推荐
def user_based_recommendation(ratings, user_similarity, user_index, top_n=3):
    """基于用户的协同过滤推荐"""
    n_items = ratings.shape[1]
    user_ratings = ratings[user_index]
    
    # 计算每个物品的预测评分
    predicted_ratings = []
    for item_idx in range(n_items):
        # 如果用户已经评分，跳过
        if user_ratings[item_idx] > 0:
            predicted_ratings.append(0)
            continue
        
        # 找到对该物品有评分的用户
        rated_users = np.where(ratings[:, item_idx] > 0)[0]
        if len(rated_users) == 0:
            predicted_ratings.append(0)
            continue
        
        # 计算加权平均评分
        numerator = 0
        denominator = 0
        for other_user_idx in rated_users:
            similarity = user_similarity[user_index, other_user_idx]
            if similarity > 0:
                numerator += similarity * ratings[other_user_idx, item_idx]
                denominator += similarity
        
        if denominator > 0:
            predicted_rating = numerator / denominator
        else:
            predicted_rating = 0
        
        predicted_ratings.append(predicted_rating)
    
    # 排序并返回Top-N
    item_ratings = list(zip(items, predicted_ratings))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 为User1推荐物品
user_index = 0  # User1
recommendations = user_based_recommendation(ratings, user_similarity, user_index)
print(f"\n为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 预测评分 = {score:.4f}")

# 2. 基于物品的协同过滤
print("\n=== 基于物品的协同过滤 ===")

# 计算物品相似度
def calculate_item_similarity(ratings):
    """计算物品之间的相似度"""
    n_items = ratings.shape[1]
    similarity_matrix = np.zeros((n_items, n_items))
    
    for i in range(n_items):
        for j in range(n_items):
            if i == j:
                similarity_matrix[i, j] = 1.0
            else:
                # 找到同时对两个物品有评分的用户
                common_users = np.where((ratings[:, i] != 0) & (ratings[:, j] != 0))[0]
                if len(common_users) > 0:
                    # 提取共同评分
                    item_i_ratings = ratings[common_users, i]
                    item_j_ratings = ratings[common_users, j]
                    
                    # 计算余弦相似度
                    norm_i = np.linalg.norm(item_i_ratings)
                    norm_j = np.linalg.norm(item_j_ratings)
                    if norm_i > 0 and norm_j > 0:
                        similarity = np.dot(item_i_ratings, item_j_ratings) / (norm_i * norm_j)
                    else:
                        similarity = 0
                else:
                    similarity = 0
                similarity_matrix[i, j] = similarity
    
    return similarity_matrix

# 计算物品相似度矩阵
item_similarity = calculate_item_similarity(ratings)
print("物品相似度矩阵:")
print(pd.DataFrame(item_similarity, index=items, columns=items))

# 基于物品的协同过滤推荐
def item_based_recommendation(ratings, item_similarity, user_index, top_n=3):
    """基于物品的协同过滤推荐"""
    n_items = ratings.shape[1]
    user_ratings = ratings[user_index]
    
    # 计算每个物品的预测评分
    predicted_ratings = []
    for item_idx in range(n_items):
        # 如果用户已经评分，跳过
        if user_ratings[item_idx] > 0:
            predicted_ratings.append(0)
            continue
        
        # 找到用户已经评分的物品
        rated_items = np.where(user_ratings > 0)[0]
        if len(rated_items) == 0:
            predicted_ratings.append(0)
            continue
        
        # 计算加权平均评分
        numerator = 0
        denominator = 0
        for rated_item_idx in rated_items:
            similarity = item_similarity[item_idx, rated_item_idx]
            if similarity > 0:
                numerator += similarity * user_ratings[rated_item_idx]
                denominator += similarity
        
        if denominator > 0:
            predicted_rating = numerator / denominator
        else:
            predicted_rating = 0
        
        predicted_ratings.append(predicted_rating)
    
    # 排序并返回Top-N
    item_ratings = list(zip(items, predicted_ratings))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 为User1推荐物品
recommendations = item_based_recommendation(ratings, item_similarity, user_index)
print(f"\n基于物品的协同过滤为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 预测评分 = {score:.4f}")

# 3. 矩阵分解
print("\n=== 矩阵分解 ===")

def matrix_factorization(ratings, k=2, iterations=100, learning_rate=0.01, lambda_reg=0.01):
    """矩阵分解推荐算法"""
    n_users, n_items = ratings.shape
    
    # 初始化用户和物品矩阵
    P = np.random.randn(n_users, k)
    Q = np.random.randn(n_items, k)
    
    # 训练模型
    for iteration in range(iterations):
        for i in range(n_users):
            for j in range(n_items):
                if ratings[i, j] > 0:
                    # 计算误差
                    error = ratings[i, j] - np.dot(P[i, :], Q[j, :].T)
                    # 更新P和Q
                    P[i, :] += learning_rate * (error * Q[j, :] - lambda_reg * P[i, :])
                    Q[j, :] += learning_rate * (error * P[i, :] - lambda_reg * Q[j, :])
        
        # 计算均方误差
        mse = 0
        for i in range(n_users):
            for j in range(n_items):
                if ratings[i, j] > 0:
                    mse += (ratings[i, j] - np.dot(P[i, :], Q[j, :].T)) ** 2
        mse /= np.sum(ratings > 0)
        
        if (iteration + 1) % 20 == 0:
            print(f"迭代 {iteration + 1}/{iterations}, MSE: {mse:.4f}")
    
    # 预测评分
    predicted_ratings = np.dot(P, Q.T)
    
    return predicted_ratings, P, Q

# 应用矩阵分解
predicted_ratings, P, Q = matrix_factorization(ratings)
print("\n矩阵分解预测评分:")
print(pd.DataFrame(predicted_ratings, index=users, columns=items))

# 基于矩阵分解的推荐
def matrix_factorization_recommendation(predicted_ratings, user_index, top_n=3):
    """基于矩阵分解的推荐"""
    user_predicted = predicted_ratings[user_index]
    # 找到用户未评分的物品
    unrated_items = np.where(ratings[user_index] == 0)[0]
    # 对未评分物品进行排序
    item_ratings = list(zip([items[i] for i in unrated_items], user_predicted[unrated_items]))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    return recommended_items

# 为User1推荐物品
recommendations = matrix_factorization_recommendation(predicted_ratings, user_index)
print(f"\n基于矩阵分解为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 预测评分 = {score:.4f}")

# 4. 协同过滤的评估
print("\n=== 协同过滤的评估 ===")

def evaluate_collaborative_filtering(ratings, predicted_ratings):
    """评估协同过滤算法"""
    # 只考虑有真实评分的物品
    mask = ratings > 0
    actual = ratings[mask]
    predicted = predicted_ratings[mask]
    
    # 计算MAE
    mae = np.mean(np.abs(predicted - actual))
    # 计算RMSE
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    
    return mae, rmse

# 评估矩阵分解
mae, rmse = evaluate_collaborative_filtering(ratings, predicted_ratings)
print(f"矩阵分解评估结果:")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# 5. 协同过滤的优缺点
print("\n=== 协同过滤的优缺点 ===")

print("协同过滤的优点:")
print("1. 不需要物品的特征信息")
print("2. 能够发现用户的潜在兴趣")
print("3. 推荐结果的多样性较好")
print("4. 实现相对简单")

print("\n协同过滤的缺点:")
print("1. 冷启动问题: 新用户或新物品难以推荐")
print("2. 数据稀疏性: 用户-物品矩阵通常非常稀疏")
print("3. 可扩展性: 大规模系统计算复杂度高")
print("4. 热门物品的推荐偏差")
print("5. 缺乏可解释性")

# 6. 协同过滤的改进方法
print("\n=== 协同过滤的改进方法 ===")

print("协同过滤的改进方法:")
print("1. 矩阵分解: SVD、NMF等方法")
print("2. 正则化: 防止过拟合")
print("3. 隐式反馈: 利用用户的行为数据")
print("4. 时间因素: 考虑用户兴趣的变化")
print("5. 混合方法: 结合其他推荐算法")
print("6. 并行计算: 提高大规模系统的性能")

print("\n协同过滤示例完成！")
