#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keras迁移学习
展示Keras的迁移学习的使用方法
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. 加载预训练模型
def load_pretrained_model():
    """加载预训练模型"""
    print("\n=== 加载预训练模型 ===")
    
    # 加载MobileNetV2预训练模型
    base_model = keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # 打印模型结构
    print("预训练模型结构:")
    base_model.summary()
    
    print("预训练模型加载完成")
    return base_model

# 2. 冻结预训练模型层
def freeze_pretrained_layers(base_model):
    """冻结预训练模型层"""
    print("\n=== 冻结预训练模型层 ===")
    
    # 冻结所有层
    base_model.trainable = False
    
    # 打印可训练参数
    print(f"冻结后可训练参数: {len(base_model.trainable_variables)}")
    
    print("预训练模型层冻结完成")
    return base_model

# 3. 构建迁移学习模型
def build_transfer_learning_model(base_model):
    """构建迁移学习模型"""
    print("\n=== 构建迁移学习模型 ===")
    
    # 创建新的模型
    inputs = keras.Input(shape=(224, 224, 3))
    
    # 使用预训练模型作为特征提取器
    x = base_model(inputs, training=False)
    
    # 添加全局平均池化层
    x = keras.layers.GlobalAveragePooling2D()(x)
    
    # 添加分类层
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    
    # 创建模型
    model = keras.Model(inputs=inputs, outputs=outputs)
    
    # 打印模型结构
    print("迁移学习模型结构:")
    model.summary()
    
    # 编译模型
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("迁移学习模型构建完成")
    return model

# 4. 数据预处理
def preprocess_data():
    """数据预处理"""
    print("\n=== 数据预处理 ===")
    
    # 加载CIFAR-10数据集
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # 调整图像大小以适应MobileNetV2的输入要求
    x_train = tf.image.resize(x_train, (224, 224))
    x_test = tf.image.resize(x_test, (224, 224))
    
    # 使用MobileNetV2的预处理函数
    x_train = keras.applications.mobilenet_v2.preprocess_input(x_train)
    x_test = keras.applications.mobilenet_v2.preprocess_input(x_test)
    
    print(f"训练集: {x_train.shape}, {y_train.shape}")
    print(f"测试集: {x_test.shape}, {y_test.shape}")
    
    print("数据预处理完成")
    return (x_train, y_train), (x_test, y_test)

# 5. 训练迁移学习模型
def train_transfer_learning_model(model, x_train, y_train, x_test, y_test):
    """训练迁移学习模型"""
    print("\n=== 训练迁移学习模型 ===")
    
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
    plt.savefig('transfer_learning_history.png')
    print("训练历史已保存为 transfer_learning_history.png")
    
    print("迁移学习模型训练完成")

# 6. 微调模型
def fine_tune_model(base_model, model, x_train, y_train, x_test, y_test):
    """微调模型"""
    print("\n=== 微调模型 ===")
    
    # 解冻部分层
    base_model.trainable = True
    
    # 冻结前100层
    for layer in base_model.layers[:100]:
        layer.trainable = False
    
    # 重新编译模型
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-5),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 微调模型
    print("微调模型:")
    history = model.fit(
        x_train, y_train,
        epochs=5,
        batch_size=32,
        validation_split=0.2,
        verbose=1
    )
    
    # 评估模型
    print("\n评估微调后的模型:")
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_acc:.4f}")
    
    print("模型微调完成")

# 7. 迁移学习的应用
def transfer_learning_application(model, x_test, y_test):
    """迁移学习的应用"""
    print("\n=== 迁移学习的应用 ===")
    
    # 进行预测
    print("进行预测:")
    predictions = model.predict(x_test[:10])
    
    # CIFAR-10类别名称
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    # 打印预测结果
    print("预测结果:")
    for i in range(10):
        predicted_label = class_names[np.argmax(predictions[i])]
        true_label = class_names[y_test[i][0]]
        print(f"样本 {i+1}: 预测={predicted_label}, 真实={true_label}, 正确={predicted_label == true_label}")
    
    print("迁移学习应用完成")

# 主函数
def main():
    print("Keras Transfer Learning")
    print("=" * 50)
    
    # 加载预训练模型
    base_model = load_pretrained_model()
    
    # 冻结预训练模型层
    base_model = freeze_pretrained_layers(base_model)
    
    # 构建迁移学习模型
    model = build_transfer_learning_model(base_model)
    
    # 数据预处理
    (x_train, y_train), (x_test, y_test) = preprocess_data()
    
    # 训练迁移学习模型
    train_transfer_learning_model(model, x_train, y_train, x_test, y_test)
    
    # 微调模型
    fine_tune_model(base_model, model, x_train, y_train, x_test, y_test)
    
    # 迁移学习的应用
    transfer_learning_application(model, x_test, y_test)
    
    print("\nAll transfer learning examples completed!")

if __name__ == "__main__":
    main()