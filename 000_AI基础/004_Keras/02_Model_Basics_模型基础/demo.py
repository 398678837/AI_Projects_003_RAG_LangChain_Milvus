#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras模型基础
展示Keras的模型基础概念和操作
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 模型创建
def model_creation():
    """模型创建"""
    print("\n=== 模型创建 ===")
    
    # 使用Sequential API创建模型
    print("使用Sequential API创建模型:")
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    model.summary()
    
    # 使用Functional API创建模型
    print("\n使用Functional API创建模型:")
    inputs = keras.Input(shape=(28, 28))
    x = keras.layers.Flatten()(inputs)
    x = keras.layers.Dense(128, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    model_func = keras.Model(inputs=inputs, outputs=outputs)
    
    # 打印模型结构
    model_func.summary()
    
    print("模型创建示例完成")

# 2. 模型编译
def model_compilation():
    """模型编译"""
    print("\n=== 模型编译 ===")
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 编译模型 - 使用不同的优化器
    print("使用Adam优化器:")
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 编译模型 - 使用SGD优化器
    print("\n使用SGD优化器:")
    model.compile(
        optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 编译模型 - 使用RMSprop优化器
    print("\n使用RMSprop优化器:")
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("模型编译示例完成")

# 3. 模型训练
def model_training():
    """模型训练"""
    print("\n=== 模型训练 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建模型
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
        epochs=5,
        batch_size=32,
        validation_split=0.2
    )
    
    # 打印训练历史
    print("\n训练历史:")
    print(f"训练损失: {history.history['loss']}")
    print(f"验证损失: {history.history['val_loss']}")
    print(f"训练准确率: {history.history['accuracy']}")
    print(f"验证准确率: {history.history['val_accuracy']}")
    
    print("模型训练示例完成")

# 4. 模型评估
def model_evaluation():
    """模型评估"""
    print("\n=== 模型评估 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建模型
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
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2, verbose=0)
    
    # 评估模型
    print("评估模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    print("模型评估示例完成")

# 5. 模型预测
def model_prediction():
    """模型预测"""
    print("\n=== 模型预测 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 创建模型
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
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2, verbose=0)
    
    # 进行预测
    print("进行预测:")
    predictions = model.predict(x_test[:5])
    
    # 打印预测结果
    print("预测结果:")
    for i in range(5):
        predicted_label = np.argmax(predictions[i])
        true_label = y_test[i]
        print(f"样本 {i+1}: 预测={predicted_label}, 真实={true_label}")
    
    print("模型预测示例完成")

# 6. 模型保存和加载
def model_saving_loading():
    """模型保存和加载"""
    print("\n=== 模型保存和加载 ===")
    
    # 创建模型
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
    model.save('model.h5')
    print("模型已保存为 model.h5")
    
    # 加载模型
    loaded_model = keras.models.load_model('model.h5')
    print("模型已加载")
    
    # 验证模型结构
    print("\n加载的模型结构:")
    loaded_model.summary()
    
    print("模型保存和加载示例完成")

# 主函数
def main():
    print("Keras Model Basics")
    print("=" * 50)
    
    # 运行所有示例
    model_creation()
    model_compilation()
    model_training()
    model_evaluation()
    model_prediction()
    model_saving_loading()
    
    print("\nAll model basics examples completed!")

if __name__ == "__main__":
    main()