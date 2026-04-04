#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras循环神经网络
展示Keras的循环神经网络的使用方法
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 基本循环神经网络
def basic_rnn():
    """基本循环神经网络"""
    print("\n=== 基本循环神经网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # 循环层
        keras.layers.SimpleRNN(64, input_shape=(28, 28)),
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("基本循环神经网络创建完成")

# 2. LSTM网络
def lstm_network():
    """LSTM网络"""
    print("\n=== LSTM网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # LSTM层
        keras.layers.LSTM(64, input_shape=(28, 28)),
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("LSTM网络创建完成")

# 3. GRU网络
def gru_network():
    """GRU网络"""
    print("\n=== GRU网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # GRU层
        keras.layers.GRU(64, input_shape=(28, 28)),
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("GRU网络创建完成")

# 4. 双向循环神经网络
def bidirectional_rnn():
    """双向循环神经网络"""
    print("\n=== 双向循环神经网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # 双向LSTM层
        keras.layers.Bidirectional(keras.layers.LSTM(64), input_shape=(28, 28)),
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("双向循环神经网络创建完成")

# 5. 多层循环神经网络
def stacked_rnn():
    """多层循环神经网络"""
    print("\n=== 多层循环神经网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # 第一层LSTM
        keras.layers.LSTM(64, return_sequences=True, input_shape=(28, 28)),
        # 第二层LSTM
        keras.layers.LSTM(64),
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("多层循环神经网络创建完成")

# 6. 循环神经网络的训练和评估
def train_evaluate_rnn():
    """循环神经网络的训练和评估"""
    print("\n=== 循环神经网络的训练和评估 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建LSTM模型
    model = keras.Sequential([
        keras.layers.LSTM(64, input_shape=(28, 28)),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 训练模型
    print("训练模型:")
    history = model.fit(
        x_train, y_train,
        epochs=10,
        batch_size=32,
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    # 绘制训练历史
    plt.figure(figsize=(12, 4))
    
    # 绘制损失
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    
    # 绘制准确率
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('rnn_training_history.png')
    print("训练历史已保存为 rnn_training_history.png")
    
    print("循环神经网络训练和评估完成")

# 7. 循环神经网络的应用
def rnn_application():
    """循环神经网络的应用"""
    print("\n=== 循环神经网络的应用 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建LSTM模型
    model = keras.Sequential([
        keras.layers.LSTM(64, input_shape=(28, 28)),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 训练模型
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2, verbose=0)
    
    # 进行预测
    print("进行预测:")
    predictions = model.predict(x_test[:10])
    
    # 打印预测结果
    print("预测结果:")
    for i in range(10):
        predicted_label = np.argmax(predictions[i])
        true_label = y_test[i]
        print(f"样本 {i+1}: 预测={predicted_label}, 真实={true_label}, 正确={predicted_label == true_label}")
    
    print("循环神经网络应用完成")

# 主函数
def main():
    print("Keras Recurrent Neural Networks")
    print("=" * 50)
    
    # 运行所有示例
    basic_rnn()
    lstm_network()
    gru_network()
    bidirectional_rnn()
    stacked_rnn()
    train_evaluate_rnn()
    rnn_application()
    
    print("\nAll RNN examples completed!")

if __name__ == "__main__":
    main()