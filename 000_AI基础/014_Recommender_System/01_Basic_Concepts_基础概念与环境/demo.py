#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推荐系统基础概念与环境
展示推荐系统的基本概念和环境设置
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. 推荐系统基础概念
print("=== 推荐系统基础概念 ===")

print("推荐系统的定义:")
print("推荐系统是一种信息过滤系统，用于预测用户对物品的偏好或评分。")
print("\n推荐系统的主要类型:")
print("1. 协同过滤 (Collaborative Filtering)")
print("2. 基于内容的推荐 (Content-Based)")
print("3. 混合推荐 (Hybrid Methods)")
print("4. 基于知识的推荐 (Knowledge-Based)")
print("5. 基于流行度的推荐 (Popularity-Based)")

# 2. 数据集创建
print("\n=== 数据集创建 ===")

def create_sample_data():
    """创建示例推荐系统数据集"""
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
    
    # 创建用户特征
    user_features = pd.DataFrame({
        "user_id": users,
        "age": [25, 30, 35, 20, 40],
        "gender": ["M", "F", "M", "M", "F"],
        "occupation": ["Engineer", "Doctor", "Teacher", "Student", "Manager"]
    })
    
    # 创建物品特征
    item_features = pd.DataFrame({
        "item_id": items,
        "category": ["Action", "Comedy", "Action", "Comedy", "Drama", "Drama"],
        "year": [2020, 2019, 2021, 2020, 2018, 2019],
        "director": ["Director A", "Director B", "Director A", "Director C", "Director B", "Director D"]
    })
    
    print("创建示例数据集:")
    print("\n用户-物品评分矩阵:")
    print(pd.DataFrame(ratings, index=users, columns=items))
    print("\n用户特征:")
    print(user_features)
    print("\n物品特征:")
    print(item_features)
    
    return users, items, ratings, user_features, item_features

# 创建示例数据
users, items, ratings, user_features, item_features = create_sample_data()

# 3. 数据可视化
print("\n=== 数据可视化 ===")

def visualize_data(ratings, users, items):
    """可视化评分数据"""
    plt.figure(figsize=(10, 6))
    plt.imshow(ratings, cmap='viridis')
    plt.colorbar(label='Rating')
    plt.xticks(np.arange(len(items)), items, rotation=45)
    plt.yticks(np.arange(len(users)), users)
    plt.xlabel('Items')
    plt.ylabel('Users')
    plt.title('User-Item Rating Matrix')
    plt.tight_layout()
    plt.savefig('rating_matrix.png')
    print("评分矩阵可视化已保存为 rating_matrix.png")

# 可视化评分矩阵
visualize_data(ratings, users, items)

# 4. 推荐系统评估指标
print("\n=== 推荐系统评估指标 ===")

def calculate_mae(predictions, actual):
    """计算平均绝对误差"""
    return np.mean(np.abs(predictions - actual))

def calculate_rmse(predictions, actual):
    """计算均方根误差"""
    return np.sqrt(np.mean((predictions - actual) ** 2))

# 示例评估
actual_ratings = np.array([5, 4, 3, 5, 4])
predicted_ratings = np.array([4.5, 4.2, 2.8, 4.7, 3.9])

mae = calculate_mae(predicted_ratings, actual_ratings)
rmse = calculate_rmse(predicted_ratings, actual_ratings)

print(f"示例评估:")
print(f"实际评分: {actual_ratings}")
print(f"预测评分: {predicted_ratings}")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# 5. 基于流行度的推荐
print("\n=== 基于流行度的推荐 ===")

def popularity_based_recommendation(ratings, items, top_n=3):
    """基于流行度的推荐"""
    # 计算每个物品的平均评分
    item_ratings = ratings.sum(axis=0) / (ratings != 0).sum(axis=0)
    # 排序并返回Top-N
    popular_items = sorted(zip(items, item_ratings), key=lambda x: x[1], reverse=True)[:top_n]
    return popular_items

# 计算基于流行度的推荐
popular_items = popularity_based_recommendation(ratings, items)
print("基于流行度的推荐:")
for item, score in popular_items:
    print(f"{item}: {score:.2f}")

# 6. 基于用户的协同过滤（简单版）
print("\n=== 基于用户的协同过滤（简单版） ===")

def user_based_collaborative_filtering(ratings, user_index, top_n=2):
    """基于用户的协同过滤"""
    # 计算用户之间的相似度（皮尔逊相关系数）
    similarities = []
    for i in range(len(ratings)):
        if i == user_index:
            similarities.append(-1)  # 排除自己
        else:
            # 找到两个用户共同评分的物品
            common_items = np.where((ratings[user_index] != 0) & (ratings[i] != 0))[0]
            if len(common_items) > 0:
                # 计算皮尔逊相关系数
                user_ratings = ratings[user_index][common_items]
                other_ratings = ratings[i][common_items]
                mean_user = np.mean(user_ratings)
                mean_other = np.mean(other_ratings)
                numerator = np.sum((user_ratings - mean_user) * (other_ratings - mean_other))
                denominator = np.sqrt(np.sum((user_ratings - mean_user) ** 2) * np.sum((other_ratings - mean_other) ** 2))
                if denominator > 0:
                    similarity = numerator / denominator
                else:
                    similarity = 0
            else:
                similarity = 0
            similarities.append(similarity)
    
    # 找到最相似的用户
    similar_users = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:top_n]
    
    print(f"用户 {users[user_index]} 的相似用户:")
    for user_idx, sim in similar_users:
        print(f"{users[user_idx]}: 相似度 = {sim:.4f}")
    
    return similar_users

# 测试基于用户的协同过滤
user_based_collaborative_filtering(ratings, 0)  # 为User1找到相似用户

# 7. 推荐系统的应用场景
print("\n=== 推荐系统的应用场景 ===")

print("推荐系统在以下领域有广泛应用:")
print("1. 电子商务: 推荐商品，如Amazon、淘宝")
print("2. 视频平台: 推荐视频，如Netflix、YouTube")
print("3. 音乐平台: 推荐音乐，如Spotify、网易云音乐")
print("4. 新闻平台: 推荐新闻，如今日头条、百度新闻")
print("5. 社交网络: 推荐好友、内容，如Facebook、微博")
print("6. 搜索引擎: 个性化搜索结果")
print("7. 广告系统: 个性化广告推荐")
print("8. 教育平台: 推荐学习内容")

# 8. 推荐系统的挑战
print("\n=== 推荐系统的挑战 ===")

print("推荐系统面临的主要挑战:")
print("1. 冷启动问题: 新用户或新物品的推荐")
print("2. 数据稀疏性: 用户-物品矩阵通常非常稀疏")
print("3. 计算复杂度: 大规模推荐系统的计算问题")
print("4. 多样性与准确性的平衡: 推荐结果的多样性")
print("5. 可解释性: 推荐结果的可解释性")
print("6. 隐私保护: 用户数据的隐私保护")
print("7. 实时性: 实时推荐的需求")
print("8. 公平性: 推荐结果的公平性")

# 9. 推荐系统的未来发展
print("\n=== 推荐系统的未来发展 ===")

print("推荐系统技术的未来发展趋势:")
print("1. 深度学习: 使用深度学习模型提高推荐质量")
print("2. 强化学习: 使用强化学习优化长期用户价值")
print("3. 图神经网络: 利用图结构建模用户-物品关系")
print("4. 联邦学习: 在保护隐私的前提下进行模型训练")
print("5. 多模态融合: 结合文本、图像、视频等多模态信息")
print("6. 可解释性增强: 提高推荐结果的可解释性")
print("7. 实时推荐: 实时捕捉用户兴趣变化")
print("8. 跨域推荐: 利用不同领域的数据进行推荐")

print("\n推荐系统基础概念与环境示例完成！")
