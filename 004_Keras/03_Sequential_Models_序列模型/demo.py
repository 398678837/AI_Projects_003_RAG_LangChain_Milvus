#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras序列模型
展示Keras的Sequential模型的使用方法
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 基本序列模型
def basic_sequential_model():
    """基本序列模型"""
    print("\n=== 基本序列模型 ===")
    
    # 创建序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
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
    
    print("基本序列模型创建完成")

# 2. 序列模型的层添加
def add_layers_to_sequential():
    """序列模型的层添加"""
    print("\n=== 序列模型的层添加 ===")
    
    # 创建空的序列模型
    model = keras.Sequential()
    
    # 添加层
    model.add(keras.layers.Flatten(input_shape=(28, 28)))
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(10, activation='softmax'))
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    print("序列模型层添加完成")

# 3. 序列模型的配置
def configure_sequential_model():
    """序列模型的配置"""
    print("\n=== 序列模型的配置 ===")
    
    # 创建序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        # 添加Dropout层
        keras.layers.Dropout(0.2),
        # 添加带正则化的Dense层
        keras.layers.Dense(128, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        # 添加BatchNormalization层
        keras.layers.BatchNormalization(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    print("序列模型配置完成")

# 4. 序列模型的训练和评估
def train_evaluate_sequential():
    """序列模型的训练和评估"""
    print("\n=== 序列模型的训练和评估 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
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
    plt.savefig('training_history.png')
    print("训练历史已保存为 training_history.png")
    
    print("序列模型训练和评估完成")

# 5. 序列模型的保存和加载
def save_load_sequential():
    """序列模型的保存和加载"""
    print("\n=== 序列模型的保存和加载 ===")
    
    # 创建序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 保存模型
    model.save('sequential_model.h5')
    print("模型已保存为 sequential_model.h5")
    
    # 加载模型
    loaded_model = keras.models.load_model('sequential_model.h5')
    print("模型已加载")
    
    # 验证模型结构
    print("\n加载的模型结构:")
    loaded_model.summary()
    
    print("序列模型保存和加载完成")

# 6. 序列模型的应用
def sequential_model_application():
    """序列模型的应用"""
    print("\n=== 序列模型的应用 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.2),
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
    
    print("序列模型应用完成")

# 主函数
def main():
    print("Keras Sequential Models")
    print("=" * 50)
    
    # 运行所有示例
    basic_sequential_model()
    add_layers_to_sequential()
    configure_sequential_model()
    train_evaluate_sequential()
    save_load_sequential()
    sequential_model_application()
    
    print("\nAll sequential model examples completed!")

if __name__ == "__main__":
    main()