#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推荐系统实战应用
展示推荐系统在实际应用中的使用
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# 1. 电影推荐系统
print("=== 电影推荐系统 ===")

def create_movie_data():
    """创建电影数据集"""
    movies = [
        {"id": 1, "title": "电影A", "genre": "动作,冒险,科幻", "year": 2020, "rating": 4.8},
        {"id": 2, "title": "电影B", "genre": "喜剧,爱情", "year": 2019, "rating": 4.5},
        {"id": 3, "title": "电影C", "genre": "动作,科幻", "year": 2021, "rating": 4.7},
        {"id": 4, "title": "电影D", "genre": "喜剧,剧情", "year": 2020, "rating": 4.3},
        {"id": 5, "title": "电影E", "genre": "剧情,爱情", "year": 2018, "rating": 4.6},
        {"id": 6, "title": "电影F", "genre": "剧情,历史", "year": 2019, "rating": 4.4},
        {"id": 7, "title": "电影G", "genre": "恐怖,惊悚", "year": 2020, "rating": 4.2},
        {"id": 8, "title": "电影H", "genre": "动画,冒险", "year": 2021, "rating": 4.9}
    ]
    
    # 用户评分
    users = ["User1", "User2", "User3", "User4", "User5"]
    ratings = np.array([
        [5, 4, 0, 0, 3, 0, 0, 0],
        [0, 5, 5, 0, 0, 3, 0, 0],
        [4, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 4, 0, 5, 5, 0, 0],
        [3, 0, 0, 4, 0, 0, 0, 0]
    ])
    
    # 转换为DataFrame
    movies_df = pd.DataFrame(movies)
    ratings_df = pd.DataFrame(ratings, index=users, columns=[movie["title"] for movie in movies])
    
    print("电影数据:")
    print(movies_df)
    print("\n用户评分:")
    print(ratings_df)
    
    return movies, movies_df, users, ratings

# 创建电影数据
movies, movies_df, users, ratings = create_movie_data()

# 电影推荐系统类
class MovieRecommender:
    """电影推荐系统"""
    
    def __init__(self, movies, ratings, users):
        self.movies = movies
        self.ratings = ratings
        self.users = users
        self.movie_titles = [movie["title"] for movie in movies]
        self._build_content_features()
    
    def _build_content_features(self):
        """构建内容特征"""
        # 提取电影类型特征
        genres = [movie["genre"] for movie in self.movies]
        vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(","))
        self.genre_features = vectorizer.fit_transform(genres)
        self.genre_names = vectorizer.get_feature_names_out()
    
    def content_based_recommendation(self, user_index, top_n=3):
        """基于内容的推荐"""
        user_ratings = self.ratings[user_index]
        
        # 计算电影相似度
        movie_similarity = cosine_similarity(self.genre_features)
        
        # 预测评分
        predicted_ratings = []
        for i, movie in enumerate(self.movies):
            if user_ratings[i] > 0:
                predicted_ratings.append(0)
                continue
            
            # 找到用户喜欢的电影
            liked_movies = np.where(user_ratings > 3)[0]
            if len(liked_movies) == 0:
                predicted_ratings.append(0)
                continue
            
            # 计算加权平均相似度
            similarity_sum = 0
            rating_sum = 0
            for liked_idx in liked_movies:
                similarity = movie_similarity[i, liked_idx]
                similarity_sum += similarity
                rating_sum += similarity * user_ratings[liked_idx]
            
            if similarity_sum > 0:
                predicted_rating = rating_sum / similarity_sum
            else:
                predicted_rating = 0
            
            predicted_ratings.append(predicted_rating)
        
        # 排序并返回Top-N
        movie_ratings = list(zip(self.movie_titles, predicted_ratings))
        recommended_movies = sorted(movie_ratings, key=lambda x: x[1], reverse=True)[:top_n]
        
        return recommended_movies
    
    def collaborative_filtering_recommendation(self, user_index, top_n=3):
        """基于协同过滤的推荐"""
        user_ratings = self.ratings[user_index]
        n_users, n_movies = self.ratings.shape
        
        # 计算用户相似度
        user_similarity = np.zeros(n_users)
        for i in range(n_users):
            if i == user_index:
                user_similarity[i] = -1
            else:
                common_movies = np.where((user_ratings > 0) & (self.ratings[i] > 0))[0]
                if len(common_movies) > 0:
                    user_i = user_ratings[common_movies]
                    user_j = self.ratings[i][common_movies]
                    norm_i = np.linalg.norm(user_i)
                    norm_j = np.linalg.norm(user_j)
                    if norm_i > 0 and norm_j > 0:
                        user_similarity[i] = np.dot(user_i, user_j) / (norm_i * norm_j)
                else:
                    user_similarity[i] = 0
        
        # 预测评分
        predicted_ratings = []
        for i in range(n_movies):
            if user_ratings[i] > 0:
                predicted_ratings.append(0)
                continue
            
            # 找到对该电影有评分的用户
            rated_users = np.where(self.ratings[:, i] > 0)[0]
            if len(rated_users) == 0:
                predicted_ratings.append(0)
                continue
            
            # 计算加权平均评分
            numerator = 0
            denominator = 0
            for other_user in rated_users:
                similarity = user_similarity[other_user]
                if similarity > 0:
                    numerator += similarity * self.ratings[other_user, i]
                    denominator += similarity
            
            if denominator > 0:
                predicted_rating = numerator / denominator
            else:
                predicted_rating = 0
            
            predicted_ratings.append(predicted_rating)
        
        # 排序并返回Top-N
        movie_ratings = list(zip(self.movie_titles, predicted_ratings))
        recommended_movies = sorted(movie_ratings, key=lambda x: x[1], reverse=True)[:top_n]
        
        return recommended_movies
    
    def hybrid_recommendation(self, user_index, top_n=3):
        """混合推荐"""
        # 获取基于内容的推荐
        content_recs = dict(self.content_based_recommendation(user_index, top_n=len(self.movies)))
        # 获取基于协同过滤的推荐
        cf_recs = dict(self.collaborative_filtering_recommendation(user_index, top_n=len(self.movies)))
        
        # 计算混合评分
        hybrid_scores = {}
        for movie in self.movie_titles:
            content_score = content_recs.get(movie, 0)
            cf_score = cf_recs.get(movie, 0)
            # 加权平均
            hybrid_score = 0.6 * content_score + 0.4 * cf_score
            hybrid_scores[movie] = hybrid_score
        
        # 过滤已评分的电影
        user_ratings = self.ratings[user_index]
        for i, movie in enumerate(self.movie_titles):
            if user_ratings[i] > 0:
                hybrid_scores[movie] = 0
        
        # 排序并返回Top-N
        recommended_movies = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        return recommended_movies

# 初始化电影推荐系统
recommender = MovieRecommender(movies, ratings, users)

# 测试推荐系统
user_index = 0  # User1
print(f"\n为用户 {users[user_index]} 推荐电影:")

print("\n基于内容的推荐:")
content_recs = recommender.content_based_recommendation(user_index)
for movie, score in content_recs:
    print(f"{movie}: {score:.4f}")

print("\n基于协同过滤的推荐:")
cf_recs = recommender.collaborative_filtering_recommendation(user_index)
for movie, score in cf_recs:
    print(f"{movie}: {score:.4f}")

print("\n混合推荐:")
hybrid_recs = recommender.hybrid_recommendation(user_index)
for movie, score in hybrid_recs:
    print(f"{movie}: {score:.4f}")

# 2. 商品推荐系统
print("\n=== 商品推荐系统 ===")

def create_product_data():
    """创建商品数据集"""
    products = [
        {"id": 1, "name": "商品A", "category": "电子产品", "price": 1999, "rating": 4.8},
        {"id": 2, "name": "商品B", "category": "服装", "price": 299, "rating": 4.5},
        {"id": 3, "name": "商品C", "category": "电子产品", "price": 2999, "rating": 4.7},
        {"id": 4, "name": "商品D", "category": "家居", "price": 599, "rating": 4.3},
        {"id": 5, "name": "商品E", "category": "服装", "price": 499, "rating": 4.6},
        {"id": 6, "name": "商品F", "category": "家居", "price": 899, "rating": 4.4}
    ]
    
    # 用户行为数据（1表示购买，0表示未购买）
    users = ["User1", "User2", "User3", "User4", "User5"]
    behavior = np.array([
        [1, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0]
    ])
    
    # 转换为DataFrame
    products_df = pd.DataFrame(products)
    behavior_df = pd.DataFrame(behavior, index=users, columns=[product["name"] for product in products])
    
    print("商品数据:")
    print(products_df)
    print("\n用户购买行为:")
    print(behavior_df)
    
    return products, products_df, users, behavior

# 创建商品数据
products, products_df, users, behavior = create_product_data()

# 商品推荐系统类
class ProductRecommender:
    """商品推荐系统"""
    
    def __init__(self, products, behavior, users):
        self.products = products
        self.behavior = behavior
        self.users = users
        self.product_names = [product["name"] for product in products]
    
    def popularity_based_recommendation(self, top_n=3):
        """基于流行度的推荐"""
        # 计算每个商品的购买次数
        popularity = np.sum(self.behavior, axis=0)
        # 排序并返回Top-N
        product_popularity = list(zip(self.product_names, popularity))
        recommended_products = sorted(product_popularity, key=lambda x: x[1], reverse=True)[:top_n]
        return recommended_products
    
    def user_based_recommendation(self, user_index, top_n=3):
        """基于用户的协同过滤推荐"""
        user_behavior = self.behavior[user_index]
        n_users, n_products = self.behavior.shape
        
        # 计算用户相似度
        user_similarity = np.zeros(n_users)
        for i in range(n_users):
            if i == user_index:
                user_similarity[i] = -1
            else:
                # 使用Jaccard相似度
                intersection = np.sum(np.logical_and(user_behavior, self.behavior[i]))
                union = np.sum(np.logical_or(user_behavior, self.behavior[i]))
                if union > 0:
                    user_similarity[i] = intersection / union
                else:
                    user_similarity[i] = 0
        
        # 预测购买概率
        predicted_behavior = []
        for i in range(n_products):
            if user_behavior[i] == 1:
                predicted_behavior.append(0)
                continue
            
            # 找到购买过该商品的用户
            purchased_users = np.where(self.behavior[:, i] == 1)[0]
            if len(purchased_users) == 0:
                predicted_behavior.append(0)
                continue
            
            # 计算加权平均相似度
            similarity_sum = 0
            for other_user in purchased_users:
                similarity_sum += user_similarity[other_user]
            
            if similarity_sum > 0:
                predicted_prob = similarity_sum / len(purchased_users)
            else:
                predicted_prob = 0
            
            predicted_behavior.append(predicted_prob)
        
        # 排序并返回Top-N
        product_probs = list(zip(self.product_names, predicted_behavior))
        recommended_products = sorted(product_probs, key=lambda x: x[1], reverse=True)[:top_n]
        
        return recommended_products

# 初始化商品推荐系统
product_recommender = ProductRecommender(products, behavior, users)

# 测试商品推荐系统
print("\n基于流行度的商品推荐:")
popular_recs = product_recommender.popularity_based_recommendation()
for product, score in popular_recs:
    print(f"{product}: 购买次数 = {score}")

user_index = 0  # User1
print(f"\n为用户 {users[user_index]} 推荐商品:")
user_recs = product_recommender.user_based_recommendation(user_index)
for product, score in user_recs:
    print(f"{product}: 预测购买概率 = {score:.4f}")

# 3. 新闻推荐系统
print("\n=== 新闻推荐系统 ===")

def create_news_data():
    """创建新闻数据集"""
    news = [
        {"id": 1, "title": "科技新闻A", "category": "科技", "content": "人工智能技术取得重大突破...", "timestamp": "2023-07-01"},
        {"id": 2, "title": "体育新闻B", "category": "体育", "content": "世界杯足球赛精彩瞬间...", "timestamp": "2023-07-02"},
        {"id": 3, "title": "科技新闻C", "category": "科技", "content": "新手机发布，性能强劲...", "timestamp": "2023-07-03"},
        {"id": 4, "title": "娱乐新闻D", "category": "娱乐", "content": "电影票房创新高...", "timestamp": "2023-07-04"},
        {"id": 5, "title": "体育新闻E", "category": "体育", "content": "篮球比赛精彩对决...", "timestamp": "2023-07-05"},
        {"id": 6, "title": "科技新闻F", "category": "科技", "content": "云计算技术发展趋势...", "timestamp": "2023-07-06"}
    ]
    
    # 用户阅读行为（1表示阅读，0表示未阅读）
    users = ["User1", "User2", "User3"]
    behavior = np.array([
        [1, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0]
    ])
    
    # 转换为DataFrame
    news_df = pd.DataFrame(news)
    behavior_df = pd.DataFrame(behavior, index=users, columns=[news_item["title"] for news_item in news])
    
    print("新闻数据:")
    print(news_df[['id', 'title', 'category', 'timestamp']])
    print("\n用户阅读行为:")
    print(behavior_df)
    
    return news, news_df, users, behavior

# 创建新闻数据
news, news_df, users, behavior = create_news_data()

# 新闻推荐系统类
class NewsRecommender:
    """新闻推荐系统"""
    
    def __init__(self, news, behavior, users):
        self.news = news
        self.behavior = behavior
        self.users = users
        self.news_titles = [news_item["title"] for news_item in news]
        self._build_content_features()
    
    def _build_content_features(self):
        """构建内容特征"""
        # 提取新闻标题和内容特征
        texts = [f"{item['title']} {item['content']}" for item in self.news]
        vectorizer = TfidfVectorizer()
        self.content_features = vectorizer.fit_transform(texts)
    
    def content_based_recommendation(self, user_index, top_n=3):
        """基于内容的推荐"""
        user_behavior = self.behavior[user_index]
        
        # 计算新闻相似度
        news_similarity = cosine_similarity(self.content_features)
        
        # 预测阅读概率
        predicted_behavior = []
        for i, news_item in enumerate(self.news):
            if user_behavior[i] == 1:
                predicted_behavior.append(0)
                continue
            
            # 找到用户阅读过的新闻
            read_news = np.where(user_behavior == 1)[0]
            if len(read_news) == 0:
                predicted_behavior.append(0)
                continue
            
            # 计算加权平均相似度
            similarity_sum = 0
            for read_idx in read_news:
                similarity_sum += news_similarity[i, read_idx]
            
            if similarity_sum > 0:
                predicted_prob = similarity_sum / len(read_news)
            else:
                predicted_prob = 0
            
            predicted_behavior.append(predicted_prob)
        
        # 排序并返回Top-N
        news_probs = list(zip(self.news_titles, predicted_behavior))
        recommended_news = sorted(news_probs, key=lambda x: x[1], reverse=True)[:top_n]
        
        return recommended_news
    
    def time_based_recommendation(self, top_n=3):
        """基于时间的推荐"""
        # 按时间排序
        sorted_news = sorted(self.news, key=lambda x: x['timestamp'], reverse=True)[:top_n]
        recommended_news = [(news_item['title'], news_item['timestamp']) for news_item in sorted_news]
        return recommended_news

# 初始化新闻推荐系统
news_recommender = NewsRecommender(news, behavior, users)

# 测试新闻推荐系统
user_index = 0  # User1
print(f"\n为用户 {users[user_index]} 推荐新闻:")
content_recs = news_recommender.content_based_recommendation(user_index)
for news_item, score in content_recs:
    print(f"{news_item}: 相似度 = {score:.4f}")

print("\n基于时间的新闻推荐:")
time_recs = news_recommender.time_based_recommendation()
for news_item, timestamp in time_recs:
    print(f"{news_item}: {timestamp}")

# 4. 推荐系统的实际应用挑战
print("\n=== 推荐系统的实际应用挑战 ===")

print("推荐系统在实际应用中面临的挑战:")
print("1. 数据质量: 数据不完整、噪声大、稀疏性高")
print("2. 冷启动: 新用户和新物品的推荐")
print("3. 实时性: 需要实时处理用户行为并更新推荐")
print("4. 可扩展性: 处理大规模用户和物品数据")
print("5. 多样性和新颖性: 避免推荐过于相似的物品")
print("6. 隐私保护: 保护用户数据隐私")
print("7. 可解释性: 提供推荐理由")
print("8. 多目标优化: 平衡准确性、多样性、新颖性等")

# 5. 推荐系统的部署策略
print("\n=== 推荐系统的部署策略 ===")

print("推荐系统的部署策略:")
print("1. 离线计算: 预计算用户和物品的相似度、特征等")
print("2. 在线计算: 实时处理用户行为并更新推荐")
print("3. 混合架构: 结合离线和在线计算")
print("4. A/B测试: 通过实验评估推荐算法性能")
print("5. 模型更新: 定期更新推荐模型")
print("6. 监控和反馈: 监控系统性能并收集用户反馈")
print("7. 缓存策略: 缓存热门推荐结果")
print("8. 负载均衡: 处理高并发请求")

# 6. 推荐系统的未来趋势
print("\n=== 推荐系统的未来趋势 ===")

print("推荐系统的未来发展趋势:")
print("1. 深度学习: 使用更复杂的深度学习模型")
print("2. 多模态融合: 结合文本、图像、视频等多种数据")
print("3. 强化学习: 优化长期用户价值")
print("4. 联邦学习: 在保护隐私的前提下进行模型训练")
print("5. 图神经网络: 利用用户-物品交互图")
print("6. 可解释性增强: 提高推荐结果的可解释性")
print("7. 跨域推荐: 利用不同领域的数据进行推荐")
print("8. 个性化程度提升: 更精准地捕捉用户兴趣")

print("\n推荐系统实战应用示例完成！")
