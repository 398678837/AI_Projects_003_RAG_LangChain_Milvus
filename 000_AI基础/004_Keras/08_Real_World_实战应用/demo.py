#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras实战应用
展示Keras在实际应用中的使用
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 图像分类实战
def image_classification():
    """图像分类实战"""
    print("\n=== 图像分类实战 ===")
    
    # 加载数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 类别名称
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
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
        batch_size=64,
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    # 进行预测
    print("\n进行预测:")
    predictions = model.predict(x_test[:10])
    
    # 打印预测结果
    print("预测结果:")
    for i in range(10):
        predicted_label = class_names[np.argmax(predictions[i])]
        true_label = class_names[y_test[i][0]]
        print(f"样本 {i+1}: 预测={predicted_label}, 真实={true_label}, 正确={predicted_label == true_label}")
    
    print("图像分类实战完成")

# 2. 文本分类实战
def text_classification():
    """文本分类实战"""
    print("\n=== 文本分类实战 ===")
    
    # 加载IMDB数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=10000)
    
    # 数据预处理
    def vectorize_sequences(sequences, dimension=10000):
        results = np.zeros((len(sequences), dimension))
        for i, sequence in enumerate(sequences):
            results[i, sequence] = 1.
        return results
    
    x_train = vectorize_sequences(x_train)
    x_test = vectorize_sequences(x_test)
    y_train = np.asarray(y_train).astype('float32')
    y_test = np.asarray(y_test).astype('float32')
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.Dense(16, activation='relu', input_shape=(10000,)),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    # 训练模型
    print("训练模型:")
    history = model.fit(
        x_train, y_train,
        epochs=10,
        batch_size=512,
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    print("文本分类实战完成")

# 3. 时间序列预测实战
def time_series_prediction():
    """时间序列预测实战"""
    print("\n=== 时间序列预测实战 ===")
    
    # 创建合成时间序列数据
    def create_time_series_data():
        time = np.arange(0, 1000, 0.1)
        series = np.sin(time) + np.random.randn(len(time)) * 0.1
        return time, series
    
    time, series = create_time_series_data()
    
    # 准备数据
    def prepare_data(series, window_size=30):
        X = []
        y = []
        for i in range(len(series) - window_size):
            X.append(series[i:i+window_size])
            y.append(series[i+window_size])
        return np.array(X), np.array(y)
    
    window_size = 30
    X, y = prepare_data(series, window_size)
    
    # 分割数据
    split = int(len(X) * 0.8)
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]
    
    # 重塑数据
    X_train = X_train.reshape(-1, window_size, 1)
    X_test = X_test.reshape(-1, window_size, 1)
    
    # 创建模型
    model = keras.Sequential([
        keras.layers.LSTM(64, input_shape=(window_size, 1)),
        keras.layers.Dense(1)
    ])
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mae']
    )
    
    # 训练模型
    print("训练模型:")
    history = model.fit(
        X_train, y_train,
        epochs=10,
        batch_size=32,
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估模型:")
    test_loss, test_mae = model.evaluate(X_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试MAE: {test_mae:.4f}")
    
    # 进行预测
    print("\n进行预测:")
    predictions = model.predict(X_test[:10])
    
    # 打印预测结果
    print("预测结果:")
    for i in range(10):
        print(f"样本 {i+1}: 预测={predictions[i][0]:.4f}, 真实={y_test[i]:.4f}")
    
    print("时间序列预测实战完成")

# 4. 模型部署准备
def model_deployment():
    """模型部署准备"""
    print("\n=== 模型部署准备 ===")
    
    # 加载MNIST数据集
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
    
    # 保存模型
    model.save('mnist_model.h5')
    print("模型已保存为 mnist_model.h5")
    
    # 转换为TFLite格式
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    
    with open('mnist_model.tflite', 'wb') as f:
        f.write(tflite_model)
    print("模型已转换为TFLite格式并保存为 mnist_model.tflite")
    
    print("模型部署准备完成")

# 5. 自定义回调函数
def custom_callback():
    """自定义回调函数"""
    print("\n=== 自定义回调函数 ===")
    
    # 自定义回调函数
    class CustomCallback(keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs=None):
            if logs.get('val_accuracy') > 0.9:
                print(f"\n验证准确率达到90%，提前停止训练！")
                self.model.stop_training = True
    
    # 加载MNIST数据集
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
        epochs=20,
        batch_size=32,
        validation_split=0.2,
        callbacks=[CustomCallback()],
        verbose=1
    )
    
    print("自定义回调函数示例完成")

# 主函数
def main():
    print("Keras Real World Applications")
    print("=" * 50)
    
    # 运行所有示例
    image_classification()
    text_classification()
    time_series_prediction()
    model_deployment()
    custom_callback()
    
    print("\nAll real world application examples completed!")

if __name__ == "__main__":
    main()