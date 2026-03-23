#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras卷积神经网络
展示Keras的卷积神经网络的使用方法
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 基本卷积神经网络
def basic_cnn():
    """基本卷积神经网络"""
    print("\n=== 基本卷积神经网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # 卷积层
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        
        # 卷积层
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        
        # 展平层
        keras.layers.Flatten(),
        
        # 全连接层
        keras.layers.Dense(64, activation='relu'),
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
    
    print("基本卷积神经网络创建完成")

# 2. 深度卷积神经网络
def deep_cnn():
    """深度卷积神经网络"""
    print("\n=== 深度卷积神经网络 ===")
    
    # 创建模型
    model = keras.Sequential([
        # 卷积层1
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Dropout(0.25),
        
        # 卷积层2
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Dropout(0.25),
        
        # 卷积层3
        keras.layers.Conv2D(128, (3, 3), activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.25),
        
        # 展平层
        keras.layers.Flatten(),
        
        # 全连接层1
        keras.layers.Dense(128, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.5),
        
        # 输出层
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    print("深度卷积神经网络创建完成")

# 3. 卷积神经网络的训练和评估
def train_evaluate_cnn():
    """卷积神经网络的训练和评估"""
    print("\n=== 卷积神经网络的训练和评估 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
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
    plt.savefig('cnn_training_history.png')
    print("训练历史已保存为 cnn_training_history.png")
    
    print("卷积神经网络训练和评估完成")

# 4. 卷积神经网络的应用
def cnn_application():
    """卷积神经网络的应用"""
    print("\n=== 卷积神经网络的应用 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
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
    
    print("卷积神经网络应用完成")

# 5. 卷积神经网络的可视化
def cnn_visualization():
    """卷积神经网络的可视化"""
    print("\n=== 卷积神经网络的可视化 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
        keras.layers.MaxPooling2D((2, 2), name='pool1'),
        keras.layers.Conv2D(64, (3, 3), activation='relu', name='conv2'),
        keras.layers.MaxPooling2D((2, 2), name='pool2'),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
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
    
    # 创建特征提取模型
    layer_names = ['conv1', 'pool1', 'conv2', 'pool2']
    layer_outputs = [model.get_layer(name).output for name in layer_names]
    feature_extractor = keras.Model(inputs=model.input, outputs=layer_outputs)
    
    # 提取特征
    sample = x_test[0:1]
    features = feature_extractor.predict(sample)
    
    # 可视化特征
    print(f"特征图数量: {len(features)}")
    for i, (name, feature) in enumerate(zip(layer_names, features)):
        print(f"{name} 输出形状: {feature.shape}")
    
    print("卷积神经网络可视化完成")

# 主函数
def main():
    print("Keras Convolutional Neural Networks")
    print("=" * 50)
    
    # 运行所有示例
    basic_cnn()
    deep_cnn()
    train_evaluate_cnn()
    cnn_application()
    cnn_visualization()
    
    print("\nAll CNN examples completed!")

if __name__ == "__main__":
    main()