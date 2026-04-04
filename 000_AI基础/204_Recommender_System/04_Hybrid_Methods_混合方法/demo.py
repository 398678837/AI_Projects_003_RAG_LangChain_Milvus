#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
混合推荐方法
展示混合推荐算法的基本方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# 1. 数据准备
print("=== 数据准备 ===")

def prepare_data():
    """准备推荐系统数据"""
    # 用户-物品评分矩阵
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
    
    # 物品内容描述
    item_descriptions = {
        "Item1": "action adventure fantasy",
        "Item2": "comedy romance",
        "Item3": "action sci-fi",
        "Item4": "comedy drama",
        "Item5": "drama romance",
        "Item6": "drama historical"
    }
    
    print("用户-物品评分矩阵:")
    print(pd.DataFrame(ratings, index=users, columns=items))
    
    print("\n物品内容描述:")
    for item, desc in item_descriptions.items():
        print(f"{item}: {desc}")
    
    return users, items, ratings, item_descriptions

# 准备数据
users, items, ratings, item_descriptions = prepare_data()

# 2. 基础推荐算法实现
print("\n=== 基础推荐算法实现 ===")

# 基于用户的协同过滤
def user_based_collaborative_filtering(ratings, user_index, top_n=3):
    """基于用户的协同过滤"""
    n_users, n_items = ratings.shape
    user_ratings = ratings[user_index]
    
    # 计算用户相似度
    user_similarity = np.zeros(n_users)
    for i in range(n_users):
        if i == user_index:
            user_similarity[i] = -1
        else:
            common_items = np.where((ratings[user_index] != 0) & (ratings[i] != 0))[0]
            if len(common_items) > 0:
                user_i = ratings[user_index][common_items]
                user_j = ratings[i][common_items]
                norm_i = np.linalg.norm(user_i)
                norm_j = np.linalg.norm(user_j)
                if norm_i > 0 and norm_j > 0:
                    user_similarity[i] = np.dot(user_i, user_j) / (norm_i * norm_j)
            else:
                user_similarity[i] = 0
    
    # 预测评分
    predicted_ratings = np.zeros(n_items)
    for item_idx in range(n_items):
        if user_ratings[item_idx] > 0:
            predicted_ratings[item_idx] = 0
            continue
        
        rated_users = np.where(ratings[:, item_idx] > 0)[0]
        if len(rated_users) == 0:
            predicted_ratings[item_idx] = 0
            continue
        
        numerator = 0
        denominator = 0
        for other_user in rated_users:
            similarity = user_similarity[other_user]
            if similarity > 0:
                numerator += similarity * ratings[other_user, item_idx]
                denominator += similarity
        
        if denominator > 0:
            predicted_ratings[item_idx] = numerator / denominator
    
    # 排序并返回Top-N
    item_ratings = list(zip(items, predicted_ratings))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items, predicted_ratings

# 基于内容的推荐
def content_based_recommendation(ratings, item_descriptions, user_index, top_n=3):
    """基于内容的推荐"""
    # 提取特征
    vectorizer = TfidfVectorizer()
    item_texts = list(item_descriptions.values())
    tfidf_matrix = vectorizer.fit_transform(item_texts)
    
    # 计算物品相似度
    content_similarity = cosine_similarity(tfidf_matrix)
    
    # 预测评分
    user_ratings = ratings[user_index]
    n_items = ratings.shape[1]
    predicted_ratings = np.zeros(n_items)
    
    for item_idx in range(n_items):
        if user_ratings[item_idx] > 0:
            predicted_ratings[item_idx] = 0
            continue
        
        rated_items = np.where(user_ratings > 0)[0]
        if len(rated_items) == 0:
            predicted_ratings[item_idx] = 0
            continue
        
        numerator = 0
        denominator = 0
        for rated_item_idx in rated_items:
            similarity = content_similarity[item_idx, rated_item_idx]
            if similarity > 0:
                numerator += similarity * user_ratings[rated_item_idx]
                denominator += similarity
        
        if denominator > 0:
            predicted_ratings[item_idx] = numerator / denominator
    
    # 排序并返回Top-N
    item_ratings = list(zip(items, predicted_ratings))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items, predicted_ratings

# 基于流行度的推荐
def popularity_based_recommendation(ratings, top_n=3):
    """基于流行度的推荐"""
    # 计算每个物品的平均评分
    item_ratings = np.sum(ratings, axis=0) / (np.sum(ratings != 0, axis=0) + 1e-10)
    # 排序并返回Top-N
    popular_items = sorted(zip(items, item_ratings), key=lambda x: x[1], reverse=True)[:top_n]
    return popular_items, item_ratings

# 测试基础推荐算法
user_index = 0  # User1

print("基于用户的协同过滤推荐:")
cf_recommendations, cf_ratings = user_based_collaborative_filtering(ratings, user_index)
for item, score in cf_recommendations:
    print(f"{item}: {score:.4f}")

print("\n基于内容的推荐:")
cb_recommendations, cb_ratings = content_based_recommendation(ratings, item_descriptions, user_index)
for item, score in cb_recommendations:
    print(f"{item}: {score:.4f}")

print("\n基于流行度的推荐:")
pop_recommendations, pop_ratings = popularity_based_recommendation(ratings)
for item, score in pop_recommendations:
    print(f"{item}: {score:.4f}")

# 3. 混合推荐方法
print("\n=== 混合推荐方法 ===")

# 加权混合
def weighted_hybrid_recommendation(cf_ratings, cb_ratings, pop_ratings, user_ratings, weights=[0.5, 0.3, 0.2], top_n=3):
    """加权混合推荐"""
    # 归一化评分
    def normalize(ratings):
        max_rating = np.max(ratings)
        if max_rating > 0:
            return ratings / max_rating
        return ratings
    
    cf_norm = normalize(cf_ratings)
    cb_norm = normalize(cb_ratings)
    pop_norm = normalize(pop_ratings)
    
    # 计算加权评分
    hybrid_ratings = weights[0] * cf_norm + weights[1] * cb_norm + weights[2] * pop_norm
    
    # 过滤已评分的物品
    for i in range(len(hybrid_ratings)):
        if user_ratings[i] > 0:
            hybrid_ratings[i] = 0
    
    # 排序并返回Top-N
    item_ratings = list(zip(items, hybrid_ratings))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 测试加权混合推荐
user_ratings = ratings[user_index]
print("加权混合推荐:")
hybrid_recommendations = weighted_hybrid_recommendation(cf_ratings, cb_ratings, pop_ratings, user_ratings)
for item, score in hybrid_recommendations:
    print(f"{item}: {score:.4f}")

# 切换混合
def switching_hybrid_recommendation(ratings, user_index, top_n=3):
    """切换混合推荐"""
    # 计算用户的评分数量
    user_rated_items = np.sum(ratings[user_index] > 0)
    
    if user_rated_items < 2:
        # 新用户，使用基于流行度的推荐
        print("使用基于流行度的推荐 (新用户)")
        return popularity_based_recommendation(ratings, top_n)[0]
    else:
        # 老用户，使用协同过滤
        print("使用基于用户的协同过滤 (老用户)")
        return user_based_collaborative_filtering(ratings, user_index, top_n)[0]

# 测试切换混合推荐
print("\n切换混合推荐:")
switch_recommendations = switching_hybrid_recommendation(ratings, user_index)
for item, score in switch_recommendations:
    print(f"{item}: {score:.4f}")

# 特征组合混合
def feature_combination_hybrid(ratings, item_descriptions, user_index, top_n=3):
    """特征组合混合推荐"""
    # 提取内容特征
    vectorizer = TfidfVectorizer()
    item_texts = list(item_descriptions.values())
    tfidf_matrix = vectorizer.fit_transform(item_texts)
    content_features = tfidf_matrix.toarray()
    
    # 提取协同过滤特征（用户评分）
    user_ratings = ratings[user_index]
    
    # 构建混合特征
    n_items = ratings.shape[1]
    hybrid_features = []
    
    for i in range(n_items):
        # 跳过已评分的物品
        if user_ratings[i] > 0:
            hybrid_features.append([0] * (content_features.shape[1] + 1))
            continue
        
        # 内容特征 + 平均评分
        item_avg_rating = np.sum(ratings[:, i]) / (np.sum(ratings[:, i] > 0) + 1e-10)
        hybrid_feature = np.concatenate([content_features[i], [item_avg_rating]])
        hybrid_features.append(hybrid_feature)
    
    hybrid_features = np.array(hybrid_features)
    
    # 构建用户偏好向量
    rated_items = np.where(user_ratings > 0)[0]
    if len(rated_items) == 0:
        return []
    
    user_profile = np.zeros(hybrid_features.shape[1])
    total_rating = np.sum(user_ratings[rated_items])
    
    for item_idx in rated_items:
        item_vector = np.concatenate([content_features[item_idx], [np.sum(ratings[:, item_idx]) / (np.sum(ratings[:, item_idx] > 0) + 1e-10)]])
        user_profile += user_ratings[item_idx] * item_vector
    
    if total_rating > 0:
        user_profile /= total_rating
    
    # 计算相似度
    similarities = []
    for i in range(n_items):
        if user_ratings[i] > 0:
            similarities.append(0)
            continue
        
        item_vector = hybrid_features[i]
        norm_user = np.linalg.norm(user_profile)
        norm_item = np.linalg.norm(item_vector)
        if norm_user > 0 and norm_item > 0:
            similarity = np.dot(user_profile, item_vector) / (norm_user * norm_item)
        else:
            similarity = 0
        similarities.append(similarity)
    
    # 排序并返回Top-N
    item_similarities = list(zip(items, similarities))
    recommended_items = sorted(item_similarities, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 测试特征组合混合推荐
print("\n特征组合混合推荐:")
feature_comb_recommendations = feature_combination_hybrid(ratings, item_descriptions, user_index)
for item, score in feature_comb_recommendations:
    print(f"{item}: {score:.4f}")

# 4. 混合推荐的评估
print("\n=== 混合推荐的评估 ===")

def evaluate_recommendation(actual, predicted):
    """评估推荐系统"""
    # 计算MAE
    mae = np.mean(np.abs(predicted - actual))
    # 计算RMSE
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    return mae, rmse

# 模拟评估数据
actual_ratings = np.array([5, 4, 3, 5, 4])
predicted_ratings = np.array([4.5, 4.2, 2.8, 4.7, 3.9])

mae, rmse = evaluate_recommendation(actual_ratings, predicted_ratings)
print(f"评估结果:")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# 5. 混合推荐的优缺点
print("\n=== 混合推荐的优缺点 ===")

print("混合推荐的优点:")
print("1. 结合多种推荐算法的优势")
print("2. 缓解冷启动问题")
print("3. 提高推荐系统的准确性")
print("4. 增加推荐结果的多样性")
print("5. 提高系统的鲁棒性")

print("\n混合推荐的缺点:")
print("1. 实现复杂度较高")
print("2. 参数调优困难")
print("3. 计算成本增加")
print("4. 系统维护难度增大")
print("5. 可能存在过拟合风险")

# 6. 混合推荐的应用场景
print("\n=== 混合推荐的应用场景 ===")

print("混合推荐适用于以下场景:")
print("1. 新用户冷启动: 结合基于内容和基于流行度的推荐")
print("2. 新物品冷启动: 结合基于内容和协同过滤的推荐")
print("3. 多样性需求: 结合不同推荐算法增加多样性")
print("4. 高精度需求: 结合多种算法提高推荐准确性")
print("5. 大规模系统: 结合不同算法的可扩展性优势")

# 7. 混合推荐的实现策略
print("\n=== 混合推荐的实现策略 ===")

print("混合推荐的实现策略:")
print("1. 加权混合: 为不同推荐算法分配权重")
print("2. 切换混合: 根据用户或物品特征选择推荐算法")
print("3. 特征组合: 将不同推荐算法的特征组合在一起")
print("4. 层叠混合: 将一个推荐算法的输出作为另一个的输入")
print("5. 混合排序: 对不同推荐算法的结果进行排序融合")

print("\n混合推荐方法示例完成！")
