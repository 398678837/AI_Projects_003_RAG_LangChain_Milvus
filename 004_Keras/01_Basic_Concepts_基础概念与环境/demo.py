#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras基础概念与环境
展示Keras的基本架构、核心组件和环境配置
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 打印版本信息
print(f"TensorFlow version: {tf.__version__}")
print(f"Keras version: {keras.__version__}")

# 1. 基础概念演示
def basic_concepts():
    """基础概念演示"""
    print("\n=== 基础概念演示 ===")
    
    # 张量创建
    print("创建张量:")
    # 标量
    scalar = tf.constant(5)
    print(f"标量: {scalar}")
    
    # 向量
    vector = tf.constant([1, 2, 3])
    print(f"向量: {vector}")
    
    # 矩阵
    matrix = tf.constant([[1, 2], [3, 4]])
    print(f"矩阵: {matrix}")
    
    # 三维张量
    tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"三维张量: {tensor_3d}")
    
    # 张量操作
    print("\n张量操作:")
    a = tf.constant([1, 2, 3])
    b = tf.constant([4, 5, 6])
    print(f"a + b: {tf.add(a, b)}")
    print(f"a * b: {tf.multiply(a, b)}")
    print(f"a @ b: {tf.tensordot(a, b, axes=1)}")
    
    print("基础概念演示完成")

# 2. 数据集加载
def load_datasets():
    """数据集加载"""
    print("\n=== 数据集加载 ===")
    
    # 加载MNIST数据集
    print("加载MNIST数据集:")
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    print(f"训练集: {x_train.shape}, {y_train.shape}")
    print(f"测试集: {x_test.shape}, {y_test.shape}")
    
    # 加载CIFAR-10数据集
    print("\n加载CIFAR-10数据集:")
    (x_train_cifar, y_train_cifar), (x_test_cifar, y_test_cifar) = keras.datasets.cifar10.load_data()
    print(f"训练集: {x_train_cifar.shape}, {y_train_cifar.shape}")
    print(f"测试集: {x_test_cifar.shape}, {y_test_cifar.shape}")
    
    # 加载波士顿房价数据集
    print("\n加载波士顿房价数据集:")
    (x_train_boston, y_train_boston), (x_test_boston, y_test_boston) = keras.datasets.boston_housing.load_data()
    print(f"训练集: {x_train_boston.shape}, {y_train_boston.shape}")
    print(f"测试集: {x_test_boston.shape}, {y_test_boston.shape}")
    
    print("数据集加载完成")

# 3. 数据预处理
def data_preprocessing():
    """数据预处理"""
    print("\n=== 数据预处理 ===")
    
    # 加载MNIST数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # 数据归一化
    print("数据归一化:")
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    print(f"归一化后范围: [{x_train.min()}, {x_train.max()}]")
    
    # 数据重塑
    print("\n数据重塑:")
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    print(f"重塑后形状: {x_train.shape}")
    
    # 标签独热编码
    print("\n标签独热编码:")
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)
    print(f"独热编码后形状: {y_train.shape}")
    
    print("数据预处理完成")

# 4. 模型构建基础
def model_building_basics():
    """模型构建基础"""
    print("\n=== 模型构建基础 ===")
    
    # 创建一个简单的序列模型
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # 打印模型结构
    print("模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    print("模型构建基础示例完成")

# 5. 回调函数
def callbacks_demo():
    """回调函数演示"""
    print("\n=== 回调函数演示 ===")
    
    # 定义回调函数
    callbacks = [
        # 早停
        keras.callbacks.EarlyStopping(patience=3, monitor='val_loss'),
        # 模型检查点
        keras.callbacks.ModelCheckpoint('model_checkpoint.h5', save_best_only=True),
        # 学习率调度器
        keras.callbacks.ReduceLROnPlateau(factor=0.1, patience=2, monitor='val_loss')
    ]
    
    print("回调函数定义完成")
    print(f"回调函数数量: {len(callbacks)}")
    
    print("回调函数演示完成")

# 6. 评估指标
def metrics_demo():
    """评估指标演示"""
    print("\n=== 评估指标演示 ===")
    
    # 常用评估指标
    metrics = [
        keras.metrics.Accuracy(),
        keras.metrics.Precision(),
        keras.metrics.Recall(),
        keras.metrics.AUC()
    ]
    
    print("常用评估指标:")
    for metric in metrics:
        print(f"- {metric.name}")
    
    print("评估指标演示完成")

# 主函数
def main():
    print("Keras Basic Concepts and Environment")
    print("=" * 50)
    
    # 运行所有示例
    basic_concepts()
    load_datasets()
    data_preprocessing()
    model_building_basics()
    callbacks_demo()
    metrics_demo()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main()