#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基于内容的推荐
展示基于内容的推荐算法的基本方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# 1. 基于内容的推荐基础
print("=== 基于内容的推荐基础 ===")

def create_item_content_data():
    """创建物品内容数据"""
    items = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6"]
    
    # 物品内容描述
    item_descriptions = {
        "Item1": "action adventure fantasy",
        "Item2": "comedy romance",
        "Item3": "action sci-fi",
        "Item4": "comedy drama",
        "Item5": "drama romance",
        "Item6": "drama historical"
    }
    
    # 用户评分
    users = ["User1", "User2", "User3", "User4", "User5"]
    ratings = np.array([
        [5, 4, 0, 0, 3, 0],
        [0, 5, 5, 0, 0, 3],
        [4, 0, 0, 5, 0, 0],
        [0, 0, 4, 0, 5, 5],
        [3, 0, 0, 4, 0, 0]
    ])
    
    print("物品内容描述:")
    for item, desc in item_descriptions.items():
        print(f"{item}: {desc}")
    
    print("\n用户评分矩阵:")
    print(pd.DataFrame(ratings, index=users, columns=items))
    
    return items, item_descriptions, users, ratings

# 创建物品内容数据
items, item_descriptions, users, ratings = create_item_content_data()

# 2. 文本特征提取
print("\n=== 文本特征提取 ===")

def extract_features(item_descriptions):
    """提取物品内容特征"""
    # 使用TF-IDF提取特征
    vectorizer = TfidfVectorizer()
    item_texts = list(item_descriptions.values())
    tfidf_matrix = vectorizer.fit_transform(item_texts)
    
    # 获取特征名称
    feature_names = vectorizer.get_feature_names_out()
    
    print("提取的特征:")
    print(feature_names)
    
    print("\nTF-IDF矩阵:")
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), index=items, columns=feature_names)
    print(tfidf_df)
    
    return tfidf_matrix, feature_names

# 提取特征
tfidf_matrix, feature_names = extract_features(item_descriptions)

# 3. 物品相似度计算
print("\n=== 物品相似度计算 ===")

def calculate_content_similarity(tfidf_matrix, items):
    """计算物品之间的相似度"""
    # 计算余弦相似度
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    print("物品相似度矩阵:")
    similarity_df = pd.DataFrame(similarity_matrix, index=items, columns=items)
    print(similarity_df)
    
    return similarity_matrix

# 计算物品相似度
content_similarity = calculate_content_similarity(tfidf_matrix, items)

# 4. 基于内容的推荐
print("\n=== 基于内容的推荐 ===")

def content_based_recommendation(ratings, content_similarity, user_index, top_n=3):
    """基于内容的推荐"""
    user_ratings = ratings[user_index]
    n_items = ratings.shape[1]
    
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
            similarity = content_similarity[item_idx, rated_item_idx]
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
user_index = 0  # User1
recommendations = content_based_recommendation(ratings, content_similarity, user_index)
print(f"为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 预测评分 = {score:.4f}")

# 5. 用户画像构建
print("\n=== 用户画像构建 ===")

def build_user_profile(ratings, tfidf_matrix, user_index):
    """构建用户画像"""
    user_ratings = ratings[user_index]
    rated_items = np.where(user_ratings > 0)[0]
    
    if len(rated_items) == 0:
        return np.zeros(tfidf_matrix.shape[1])
    
    # 基于用户评分构建用户画像
    user_profile = np.zeros(tfidf_matrix.shape[1])
    total_rating = np.sum(user_ratings[rated_items])
    
    for item_idx in rated_items:
        item_vector = tfidf_matrix[item_idx].toarray()[0]
        user_profile += user_ratings[item_idx] * item_vector
    
    if total_rating > 0:
        user_profile /= total_rating
    
    return user_profile

# 构建用户画像
user_profile = build_user_profile(ratings, tfidf_matrix, user_index)
print(f"用户 {users[user_index]} 的画像:")
profile_df = pd.DataFrame([user_profile], columns=feature_names, index=[users[user_index]])
print(profile_df)

# 基于用户画像的推荐
def user_profile_recommendation(tfidf_matrix, user_profile, items, user_ratings, top_n=3):
    """基于用户画像的推荐"""
    # 计算用户画像与每个物品的相似度
    item_vectors = tfidf_matrix.toarray()
    similarities = []
    
    for i, item_vector in enumerate(item_vectors):
        # 如果用户已经评分，跳过
        if user_ratings[i] > 0:
            similarities.append(0)
            continue
        
        # 计算余弦相似度
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

# 基于用户画像推荐
user_ratings = ratings[user_index]
recommendations = user_profile_recommendation(tfidf_matrix, user_profile, items, user_ratings)
print(f"\n基于用户画像为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 相似度 = {score:.4f}")

# 6. 多特征融合
print("\n=== 多特征融合 ===")

def create_multi_feature_data():
    """创建多特征数据"""
    items = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6"]
    
    # 多特征数据
    item_features = pd.DataFrame({
        "item_id": items,
        "category": ["Action", "Comedy", "Action", "Comedy", "Drama", "Drama"],
        "year": [2020, 2019, 2021, 2020, 2018, 2019],
        "duration": [120, 90, 130, 100, 110, 125],
        "rating": [4.8, 4.5, 4.7, 4.3, 4.6, 4.4]
    })
    
    print("多特征数据:")
    print(item_features)
    
    return item_features

# 创建多特征数据
item_features = create_multi_feature_data()

# 特征处理
def process_features(item_features):
    """处理多特征数据"""
    # 类别特征编码
    category_encoded = pd.get_dummies(item_features['category'])
    
    # 数值特征标准化
    numerical_features = item_features[['year', 'duration', 'rating']]
    numerical_features = (numerical_features - numerical_features.mean()) / numerical_features.std()
    
    # 合并特征
    processed_features = pd.concat([category_encoded, numerical_features], axis=1)
    
    print("\n处理后的特征:")
    print(processed_features)
    
    return processed_features

# 处理特征
processed_features = process_features(item_features)

# 基于多特征的推荐
def multi_feature_recommendation(processed_features, user_ratings, top_n=3):
    """基于多特征的推荐"""
    # 构建用户偏好向量
    rated_items = np.where(user_ratings > 0)[0]
    if len(rated_items) == 0:
        return []
    
    user_preference = np.zeros(processed_features.shape[1])
    total_rating = np.sum(user_ratings[rated_items])
    
    for item_idx in rated_items:
        item_vector = processed_features.iloc[item_idx].values
        user_preference += user_ratings[item_idx] * item_vector
    
    if total_rating > 0:
        user_preference /= total_rating
    
    # 计算相似度
    similarities = []
    for i in range(len(processed_features)):
        if user_ratings[i] > 0:
            similarities.append(0)
            continue
        
        item_vector = processed_features.iloc[i].values
        norm_user = np.linalg.norm(user_preference)
        norm_item = np.linalg.norm(item_vector)
        if norm_user > 0 and norm_item > 0:
            similarity = np.dot(user_preference, item_vector) / (norm_user * norm_item)
        else:
            similarity = 0
        similarities.append(similarity)
    
    # 排序并返回Top-N
    item_similarities = list(zip(items, similarities))
    recommended_items = sorted(item_similarities, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 基于多特征推荐
recommendations = multi_feature_recommendation(processed_features, user_ratings)
print(f"\n基于多特征为用户 {users[user_index]} 推荐的物品:")
for item, score in recommendations:
    print(f"{item}: 相似度 = {score:.4f}")

# 7. 基于内容的推荐的优缺点
print("\n=== 基于内容的推荐的优缺点 ===")

print("基于内容的推荐的优点:")
print("1. 不存在冷启动问题")
print("2. 推荐结果具有可解释性")
print("3. 能够推荐小众物品")
print("4. 不需要用户历史数据")
print("5. 计算复杂度相对较低")

print("\n基于内容的推荐的缺点:")
print("1. 推荐结果可能缺乏多样性")
print("2. 特征提取和表示的质量影响推荐效果")
print("3. 难以发现用户的潜在兴趣")
print("4. 需要大量的物品特征数据")
print("5. 对新用户的推荐效果可能较差")

# 8. 基于内容的推荐的改进方法
print("\n=== 基于内容的推荐的改进方法 ===")

print("基于内容的推荐的改进方法:")
print("1. 深度学习特征提取: 使用神经网络自动提取特征")
print("2. 多模态融合: 结合文本、图像、视频等多模态信息")
print("3. 特征选择: 选择最相关的特征")
print("4. 特征权重优化: 优化特征权重以提高推荐效果")
print("5. 混合方法: 结合协同过滤等其他推荐算法")
print("6. 实时特征更新: 实时更新物品特征")
print("7. 用户反馈融入: 利用用户反馈改进特征表示")

print("\n基于内容的推荐示例完成！")
