#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深度学习推荐
展示深度学习推荐算法的基本方法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

# 尝试导入TensorFlow和Keras
try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential, Model
    from tensorflow.keras.layers import Dense, Embedding, Flatten, Concatenate, Input, Dropout
    from tensorflow.keras.optimizers import Adam
    tensorflow_available = True
    print("TensorFlow和Keras导入成功")
except ImportError:
    tensorflow_available = False
    print("TensorFlow和Keras未安装，使用模拟数据进行演示")

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
    
    # 转换为用户-物品-评分三元组
    user_item_pairs = []
    for user_idx in range(len(users)):
        for item_idx in range(len(items)):
            rating = ratings[user_idx, item_idx]
            if rating > 0:
                user_item_pairs.append((user_idx, item_idx, rating))
    
    # 转换为DataFrame
    df = pd.DataFrame(user_item_pairs, columns=['user_id', 'item_id', 'rating'])
    
    print("用户-物品-评分数据:")
    print(df)
    
    return df, len(users), len(items)

# 准备数据
df, n_users, n_items = prepare_data()

# 2. 数据预处理
print("\n=== 数据预处理 ===")

def preprocess_data(df):
    """预处理数据"""
    # 分割训练集和测试集
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    # 标准化评分
    scaler = MinMaxScaler()
    train_df['rating'] = scaler.fit_transform(train_df[['rating']])
    test_df['rating'] = scaler.transform(test_df[['rating']])
    
    print(f"训练集大小: {len(train_df)}")
    print(f"测试集大小: {len(test_df)}")
    
    return train_df, test_df, scaler

# 预处理数据
train_df, test_df, scaler = preprocess_data(df)

# 3. 深度神经网络推荐模型
print("\n=== 深度神经网络推荐模型 ===")

def build_dnn_model(n_users, n_items, embedding_dim=8):
    """构建深度神经网络推荐模型"""
    # 用户输入和嵌入
    user_input = Input(shape=(1,), name='user_input')
    user_embedding = Embedding(input_dim=n_users, output_dim=embedding_dim, name='user_embedding')(user_input)
    user_flat = Flatten(name='user_flatten')(user_embedding)
    
    # 物品输入和嵌入
    item_input = Input(shape=(1,), name='item_input')
    item_embedding = Embedding(input_dim=n_items, output_dim=embedding_dim, name='item_embedding')(item_input)
    item_flat = Flatten(name='item_flatten')(item_embedding)
    
    # 合并特征
    concatenated = Concatenate(name='concatenate')([user_flat, item_flat])
    
    # 全连接层
    dense1 = Dense(64, activation='relu', name='dense1')(concatenated)
    dropout1 = Dropout(0.2, name='dropout1')(dense1)
    dense2 = Dense(32, activation='relu', name='dense2')(dropout1)
    dropout2 = Dropout(0.2, name='dropout2')(dense2)
    output = Dense(1, activation='linear', name='output')(dropout2)
    
    # 构建模型
    model = Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    
    return model

# 4. 训练模型
print("\n=== 训练模型 ===")

def train_model(model, train_df, test_df, epochs=50, batch_size=1):
    """训练模型"""
    # 准备训练数据
    X_train_user = train_df['user_id'].values
    X_train_item = train_df['item_id'].values
    y_train = train_df['rating'].values
    
    # 准备测试数据
    X_test_user = test_df['user_id'].values
    X_test_item = test_df['item_id'].values
    y_test = test_df['rating'].values
    
    # 训练模型
    history = model.fit(
        [X_train_user, X_train_item],
        y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=([X_test_user, X_test_item], y_test),
        verbose=1
    )
    
    return history

# 5. 评估模型
print("\n=== 评估模型 ===")

def evaluate_model(model, test_df):
    """评估模型"""
    X_test_user = test_df['user_id'].values
    X_test_item = test_df['item_id'].values
    y_test = test_df['rating'].values
    
    # 预测
    y_pred = model.predict([X_test_user, X_test_item])
    
    # 计算MAE和RMSE
    mae = np.mean(np.abs(y_pred.flatten() - y_test))
    rmse = np.sqrt(np.mean((y_pred.flatten() - y_test) ** 2))
    
    return mae, rmse

# 6. 生成推荐
print("\n=== 生成推荐 ===")

def generate_recommendations(model, user_id, n_items, top_n=3):
    """为用户生成推荐"""
    # 为用户创建所有物品的输入
    user_inputs = np.full(n_items, user_id)
    item_inputs = np.arange(n_items)
    
    # 预测评分
    predictions = model.predict([user_inputs, item_inputs])
    
    # 排序并返回Top-N
    item_ratings = list(zip(item_inputs, predictions.flatten()))
    recommended_items = sorted(item_ratings, key=lambda x: x[1], reverse=True)[:top_n]
    
    return recommended_items

# 7. 深度学习推荐的实现
if tensorflow_available:
    # 构建模型
    model = build_dnn_model(n_users, n_items)
    print("模型结构:")
    model.summary()
    
    # 训练模型
    history = train_model(model, train_df, test_df)
    
    # 评估模型
    mae, rmse = evaluate_model(model, test_df)
    print(f"模型评估结果:")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    
    # 为User1生成推荐
    user_id = 0  # User1
    recommendations = generate_recommendations(model, user_id, n_items)
    print(f"\n为用户 {user_id} 推荐的物品:")
    for item_id, score in recommendations:
        print(f"Item{item_id+1}: 预测评分 = {score:.4f}")
    
    # 绘制训练历史
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('training_history.png')
    print("训练历史图已保存为 training_history.png")
else:
    # 模拟深度学习推荐
    print("使用模拟数据演示深度学习推荐:")
    print("\n模拟模型结构:")
    print("- 用户嵌入层 (8维)")
    print("- 物品嵌入层 (8维)")
    print("- 全连接层 (64 units, ReLU)")
    print("- Dropout层 (0.2)")
    print("- 全连接层 (32 units, ReLU)")
    print("- Dropout层 (0.2)")
    print("- 输出层 (1 unit, linear)")
    
    print("\n模拟训练结果:")
    print("Epoch 1/50: loss=0.1234, val_loss=0.1123")
    print("Epoch 20/50: loss=0.0567, val_loss=0.0678")
    print("Epoch 50/50: loss=0.0345, val_loss=0.0456")
    
    print("\n模拟模型评估结果:")
    print("MAE: 0.1567")
    print("RMSE: 0.2134")
    
    print("\n为用户 0 推荐的物品:")
    print("Item3: 预测评分 = 4.75")
    print("Item4: 预测评分 = 4.23")
    print("Item6: 预测评分 = 3.89")

# 8. 其他深度学习推荐模型
print("\n=== 其他深度学习推荐模型 ===")

print("常见的深度学习推荐模型:")
print("1. 深度神经网络 (DNN): 简单的全连接神经网络")
print("2. 协同过滤神经网络 (NCF): 结合矩阵分解和深度学习")
print("3. 自编码器 (Autoencoder): 学习用户和物品的潜在表示")
print("4. 卷积神经网络 (CNN): 处理图像等结构化数据")
print("5. 循环神经网络 (RNN): 处理序列数据，如用户行为序列")
print("6. 图神经网络 (GNN): 处理用户-物品交互图")
print("7. 注意力机制模型: 学习用户对不同物品特征的注意力")
print("8. 变分自编码器 (VAE): 学习用户和物品的概率分布")

# 9. 深度学习推荐的优缺点
print("\n=== 深度学习推荐的优缺点 ===")

print("深度学习推荐的优点:")
print("1. 自动特征学习: 无需手动特征工程")
print("2. 处理复杂模式: 捕捉非线性关系")
print("3. 融合多模态数据: 结合文本、图像等多种数据")
print("4. 可扩展性: 适用于大规模数据集")
print("5. 端到端学习: 从原始数据到推荐结果")

print("\n深度学习推荐的缺点:")
print("1. 数据需求大: 需要大量训练数据")
print("2. 计算成本高: 需要强大的计算资源")
print("3. 可解释性差: 模型决策过程不透明")
print("4. 调参复杂: 需要大量超参数调优")
print("5. 冷启动问题: 对新用户和新物品表现不佳")

# 10. 深度学习推荐的未来发展
print("\n=== 深度学习推荐的未来发展 ===")

print("深度学习推荐的未来发展趋势:")
print("1. 自监督学习: 利用无标签数据提高模型性能")
print("2. 联邦学习: 在保护隐私的前提下进行模型训练")
print("3. 强化学习: 优化长期用户价值")
print("4. 小样本学习: 减少对大量数据的依赖")
print("5. 多任务学习: 同时学习多个推荐相关任务")
print("6. 可解释性增强: 提高模型的可解释性")
print("7. 实时推荐: 实时捕捉用户兴趣变化")
print("8. 跨域推荐: 利用不同领域的数据进行推荐")

print("\n深度学习推荐示例完成！")
