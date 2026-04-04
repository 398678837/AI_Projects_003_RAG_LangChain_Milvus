#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras函数式API
展示Keras的Functional API的使用方法
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 基本函数式API模型
def basic_functional_model():
    """基本函数式API模型"""
    print("\n=== 基本函数式API模型 ===")
    
    # 创建输入层
    inputs = keras.Input(shape=(28, 28))
    
    # 创建中间层
    x = keras.layers.Flatten()(inputs)
    x = keras.layers.Dense(128, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    
    # 创建模型
    model = keras.Model(inputs=inputs, outputs=outputs)
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("基本函数式API模型创建完成")

# 2. 多输入模型
def multi_input_model():
    """多输入模型"""
    print("\n=== 多输入模型 ===")
    
    # 创建输入层
    input1 = keras.Input(shape=(28, 28), name='input1')
    input2 = keras.Input(shape=(10,), name='input2')
    
    # 处理第一个输入
    x1 = keras.layers.Flatten()(input1)
    x1 = keras.layers.Dense(64, activation='relu')(x1)
    
    # 处理第二个输入
    x2 = keras.layers.Dense(64, activation='relu')(input2)
    
    # 合并输入
    merged = keras.layers.concatenate([x1, x2])
    
    # 输出层
    outputs = keras.layers.Dense(10, activation='softmax')(merged)
    
    # 创建模型
    model = keras.Model(inputs=[input1, input2], outputs=outputs)
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    print("多输入模型创建完成")

# 3. 多输出模型
def multi_output_model():
    """多输出模型"""
    print("\n=== 多输出模型 ===")
    
    # 创建输入层
    inputs = keras.Input(shape=(28, 28))
    
    # 共享层
    x = keras.layers.Flatten()(inputs)
    x = keras.layers.Dense(128, activation='relu')(x)
    
    # 输出层1：数字分类
    output1 = keras.layers.Dense(10, activation='softmax', name='digit_classification')(x)
    
    # 输出层2：数字是否大于5
    output2 = keras.layers.Dense(1, activation='sigmoid', name='greater_than_5')(x)
    
    # 创建模型
    model = keras.Model(inputs=inputs, outputs=[output1, output2])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss={
            'digit_classification': 'sparse_categorical_crossentropy',
            'greater_than_5': 'binary_crossentropy'
        },
        metrics={
            'digit_classification': 'accuracy',
            'greater_than_5': 'accuracy'
        }
    )
    
    print("多输出模型创建完成")

# 4. 复杂函数式模型
def complex_functional_model():
    """复杂函数式模型"""
    print("\n=== 复杂函数式模型 ===")
    
    # 创建输入层
    inputs = keras.Input(shape=(28, 28, 1))
    
    # 卷积层
    x = keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    
    # 展平
    x = keras.layers.Flatten()(x)
    
    # 全连接层
    x = keras.layers.Dense(64, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    
    # 创建模型
    model = keras.Model(inputs=inputs, outputs=outputs)
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    print("复杂函数式模型创建完成")

# 5. 函数式模型的训练和评估
def train_evaluate_functional():
    """函数式模型的训练和评估"""
    print("\n=== 函数式模型的训练和评估 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    # 创建函数式模型
    inputs = keras.Input(shape=(28, 28, 1))
    x = keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(64, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs)
    
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
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    print("函数式模型训练和评估完成")

# 6. 函数式模型的应用
def functional_model_application():
    """函数式模型的应用"""
    print("\n=== 函数式模型的应用 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    # 创建函数式模型
    inputs = keras.Input(shape=(28, 28, 1))
    x = keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(64, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs)
    
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
    
    print("函数式模型应用完成")

# 主函数
def main():
    print("Keras Functional API")
    print("=" * 50)
    
    # 运行所有示例
    basic_functional_model()
    multi_input_model()
    multi_output_model()
    complex_functional_model()
    train_evaluate_functional()
    functional_model_application()
    
    print("\nAll functional API examples completed!")

if __name__ == "__main__":
    main()