#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推荐系统评估指标
展示推荐系统评估指标的计算方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

# 1. 基础评估指标
print("=== 基础评估指标 ===")

def calculate_basic_metrics(actual, predicted):
    """计算基础评估指标"""
    # 计算MAE
    mae = mean_absolute_error(actual, predicted)
    # 计算RMSE
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    # 计算MSE
    mse = mean_squared_error(actual, predicted)
    # 计算R²
    r2 = 1 - (np.sum((actual - predicted) ** 2) / np.sum((actual - np.mean(actual)) ** 2))
    
    return mae, rmse, mse, r2

# 示例数据
actual_ratings = np.array([5, 4, 3, 5, 4, 5, 3, 2, 4, 5])
predicted_ratings = np.array([4.5, 4.2, 2.8, 4.7, 3.9, 4.8, 3.2, 2.5, 3.8, 4.9])

# 计算基础指标
mae, rmse, mse, r2 = calculate_basic_metrics(actual_ratings, predicted_ratings)
print("基础评估指标:")
print(f"MAE (平均绝对误差): {mae:.4f}")
print(f"RMSE (均方根误差): {rmse:.4f}")
print(f"MSE (均方误差): {mse:.4f}")
print(f"R² (决定系数): {r2:.4f}")

# 2. 排序评估指标
print("\n=== 排序评估指标 ===")

def calculate_precision_at_k(actual, predicted, k=5):
    """计算Precision@K"""
    if len(predicted) < k:
        k = len(predicted)
    relevant_items = set(actual)
    recommended_items = set(predicted[:k])
    return len(relevant_items & recommended_items) / k

def calculate_recall_at_k(actual, predicted, k=5):
    """计算Recall@K"""
    if len(predicted) < k:
        k = len(predicted)
    relevant_items = set(actual)
    if len(relevant_items) == 0:
        return 0
    recommended_items = set(predicted[:k])
    return len(relevant_items & recommended_items) / len(relevant_items)

def calculate_f1_at_k(actual, predicted, k=5):
    """计算F1@K"""
    precision = calculate_precision_at_k(actual, predicted, k)
    recall = calculate_recall_at_k(actual, predicted, k)
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

def calculate_ndcg_at_k(actual, predicted, k=5):
    """计算NDCG@K"""
    if len(predicted) < k:
        k = len(predicted)
    
    # 计算DCG
    dcg = 0
    for i, item in enumerate(predicted[:k]):
        if item in actual:
            dcg += 1 / np.log2(i + 2)  # i从0开始，所以+2
    
    # 计算IDCG
    idcg = 0
    for i in range(min(len(actual), k)):
        idcg += 1 / np.log2(i + 2)
    
    if idcg == 0:
        return 0
    return dcg / idcg

def calculate_map_at_k(actual, predicted, k=5):
    """计算MAP@K"""
    if len(predicted) < k:
        k = len(predicted)
    
    relevant_items = set(actual)
    if len(relevant_items) == 0:
        return 0
    
    precision_sum = 0
    relevant_count = 0
    
    for i, item in enumerate(predicted[:k]):
        if item in relevant_items:
            relevant_count += 1
            precision_sum += relevant_count / (i + 1)
    
    return precision_sum / len(relevant_items)

# 示例数据
actual_items = ["Item1", "Item3", "Item5"]
predicted_items = ["Item1", "Item2", "Item3", "Item4", "Item6"]

# 计算排序指标
precision_5 = calculate_precision_at_k(actual_items, predicted_items, k=5)
recall_5 = calculate_recall_at_k(actual_items, predicted_items, k=5)
f1_5 = calculate_f1_at_k(actual_items, predicted_items, k=5)
ndcg_5 = calculate_ndcg_at_k(actual_items, predicted_items, k=5)
map_5 = calculate_map_at_k(actual_items, predicted_items, k=5)

print("排序评估指标 (K=5):")
print(f"Precision@5: {precision_5:.4f}")
print(f"Recall@5: {recall_5:.4f}")
print(f"F1@5: {f1_5:.4f}")
print(f"NDCG@5: {ndcg_5:.4f}")
print(f"MAP@5: {map_5:.4f}")

# 3. 覆盖率和多样性指标
print("\n=== 覆盖率和多样性指标 ===")

def calculate_coverage(recommended_items, total_items):
    """计算覆盖率"""
    unique_recommended = set()
    for user_items in recommended_items:
        unique_recommended.update(user_items)
    return len(unique_recommended) / total_items

def calculate_diversity(recommended_items, item_similarity):
    """计算多样性"""
    total_similarity = 0
    count = 0
    
    for user_items in recommended_items:
        if len(user_items) < 2:
            continue
        
        for i in range(len(user_items)):
            for j in range(i + 1, len(user_items)):
                item1 = user_items[i]
                item2 = user_items[j]
                if item1 in item_similarity and item2 in item_similarity[item1]:
                    total_similarity += item_similarity[item1][item2]
                    count += 1
    
    if count == 0:
        return 0
    
    avg_similarity = total_similarity / count
    return 1 - avg_similarity

# 示例数据
recommended_items = [
    ["Item1", "Item2", "Item3"],
    ["Item2", "Item4", "Item5"],
    ["Item1", "Item3", "Item6"]
]
total_items = 6

# 物品相似度矩阵
item_similarity = {
    "Item1": {"Item2": 0.8, "Item3": 0.9, "Item4": 0.2, "Item5": 0.3, "Item6": 0.1},
    "Item2": {"Item1": 0.8, "Item3": 0.7, "Item4": 0.6, "Item5": 0.4, "Item6": 0.2},
    "Item3": {"Item1": 0.9, "Item2": 0.7, "Item4": 0.3, "Item5": 0.2, "Item6": 0.1},
    "Item4": {"Item1": 0.2, "Item2": 0.6, "Item3": 0.3, "Item5": 0.8, "Item6": 0.7},
    "Item5": {"Item1": 0.3, "Item2": 0.4, "Item3": 0.2, "Item4": 0.8, "Item6": 0.9},
    "Item6": {"Item1": 0.1, "Item2": 0.2, "Item3": 0.1, "Item4": 0.7, "Item5": 0.9}
}

# 计算覆盖率和多样性
coverage = calculate_coverage(recommended_items, total_items)
diversity = calculate_diversity(recommended_items, item_similarity)

print("覆盖率和多样性指标:")
print(f"覆盖率: {coverage:.4f}")
print(f"多样性: {diversity:.4f}")

# 4. 新颖性指标
print("\n=== 新颖性指标 ===")

def calculate_novelty(recommended_items, item_popularity):
    """计算新颖性"""
    total_novelty = 0
    count = 0
    
    for user_items in recommended_items:
        for item in user_items:
            if item in item_popularity:
                # 新颖性 = 1 / 流行度
                total_novelty += 1 / (item_popularity[item] + 1)  # +1 避免除零
                count += 1
    
    if count == 0:
        return 0
    
    return total_novelty / count

# 物品流行度（示例数据）
item_popularity = {
    "Item1": 100,
    "Item2": 80,
    "Item3": 90,
    "Item4": 40,
    "Item5": 30,
    "Item6": 20
}

# 计算新颖性
novelty = calculate_novelty(recommended_items, item_popularity)
print(f"新颖性: {novelty:.4f}")

# 5. 实时性指标
print("\n=== 实时性指标 ===")

def calculate_latency(start_time, end_time):
    """计算延迟"""
    return end_time - start_time

# 示例数据
start_time = 10.0
end_time = 10.05
latency = calculate_latency(start_time, end_time)
print(f"延迟: {latency:.4f} 秒")

# 6. 综合评估
print("\n=== 综合评估 ===")

def comprehensive_evaluation(actual_ratings, predicted_ratings, actual_items, predicted_items, 
                           recommended_items, total_items, item_similarity, item_popularity):
    """综合评估推荐系统"""
    # 基础指标
    mae, rmse, mse, r2 = calculate_basic_metrics(actual_ratings, predicted_ratings)
    
    # 排序指标
    precision_5 = calculate_precision_at_k(actual_items, predicted_items, k=5)
    recall_5 = calculate_recall_at_k(actual_items, predicted_items, k=5)
    f1_5 = calculate_f1_at_k(actual_items, predicted_items, k=5)
    ndcg_5 = calculate_ndcg_at_k(actual_items, predicted_items, k=5)
    map_5 = calculate_map_at_k(actual_items, predicted_items, k=5)
    
    # 覆盖率和多样性
    coverage = calculate_coverage(recommended_items, total_items)
    diversity = calculate_diversity(recommended_items, item_similarity)
    
    # 新颖性
    novelty = calculate_novelty(recommended_items, item_popularity)
    
    # 构建评估报告
    evaluation_report = {
        "基础指标": {
            "MAE": mae,
            "RMSE": rmse,
            "MSE": mse,
            "R²": r2
        },
        "排序指标": {
            "Precision@5": precision_5,
            "Recall@5": recall_5,
            "F1@5": f1_5,
            "NDCG@5": ndcg_5,
            "MAP@5": map_5
        },
        "覆盖率和多样性": {
            "覆盖率": coverage,
            "多样性": diversity
        },
        "新颖性": novelty
    }
    
    return evaluation_report

# 综合评估
evaluation_report = comprehensive_evaluation(
    actual_ratings, predicted_ratings,
    actual_items, predicted_items,
    recommended_items, total_items,
    item_similarity, item_popularity
)

print("综合评估报告:")
for category, metrics in evaluation_report.items():
    print(f"\n{category}:")
    if isinstance(metrics, dict):
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
    else:
        print(f"  {category}: {metrics:.4f}")

# 7. 评估指标的选择
print("\n=== 评估指标的选择 ===")

print("评估指标的选择依据:")
print("1. 推荐任务类型: 评分预测 vs 排序推荐")
print("2. 业务目标: 准确性 vs 多样性 vs 新颖性")
print("3. 数据特性: 稀疏性、分布等")
print("4. 计算复杂度: 实时性要求")
print("5. 可解释性: 指标的可理解性")

print("\n不同场景的指标选择:")
print("- 电子商务: 转化率、点击率、销售额")
print("- 视频平台: 观看时长、点击率、留存率")
print("- 音乐平台: 播放时长、跳过率、重复播放率")
print("- 新闻平台: 阅读时长、点击率、分享率")

# 8. 评估实验设计
print("\n=== 评估实验设计 ===")

print("评估实验设计步骤:")
print("1. 数据分割: 训练集、验证集、测试集")
print("2. 评估方法: 留一法、K折交叉验证、时间分割")
print("3. 基线模型: 流行度、随机推荐等")
print("4. 超参数调优: 网格搜索、随机搜索")
print("5. 统计显著性检验: t检验、方差分析")
print("6. 结果分析: 性能分析、错误分析")

# 9. 评估工具和库
print("\n=== 评估工具和库 ===")

print("推荐系统评估工具和库:")
print("1. Surprise: 专门用于推荐系统评估的Python库")
print("2. scikit-learn: 提供基础评估指标")
print("3. TensorFlow Recommenders: TensorFlow推荐系统库")
print("4. PyTorch RecSys: PyTorch推荐系统库")
print("5. EvalRS: 推荐系统评估工具")
print("6. RecTools: 推荐系统工具包")

print("\n推荐系统评估指标示例完成！")
