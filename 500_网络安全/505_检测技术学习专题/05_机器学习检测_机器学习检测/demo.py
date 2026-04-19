import os
import sys
import json
import time
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

class MachineLearningDetection:
    def __init__(self):
        # 模拟恶意代码和良性代码的特征数据
        self.feature_names = [
            "file_size",  # 文件大小
            "num_sections",  # 节数量
            "has_debug",  # 是否有调试信息
            "has_imports",  # 是否有导入表
            "num_imports",  # 导入函数数量
            "has_exports",  # 是否有导出表
            "has_resources",  # 是否有资源
            "entropy",  # 熵值
            "num_strings",  # 字符串数量
            "has_network",  # 是否有网络连接
            "has_file_operations",  # 是否有文件操作
            "has_registry_operations"  # 是否有注册表操作
        ]
        
        # 生成模拟数据
        self.generate_sample_data()
        
        # 初始化分类器
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
    
    def generate_sample_data(self):
        """生成模拟数据"""
        # 生成恶意代码样本
        malware_samples = []
        for _ in range(500):
            sample = {
                "file_size": np.random.randint(10000, 1000000),
                "num_sections": np.random.randint(3, 10),
                "has_debug": np.random.choice([0, 1], p=[0.8, 0.2]),
                "has_imports": 1,
                "num_imports": np.random.randint(10, 50),
                "has_exports": np.random.choice([0, 1], p=[0.7, 0.3]),
                "has_resources": np.random.choice([0, 1], p=[0.5, 0.5]),
                "entropy": np.random.uniform(5.0, 8.0),
                "num_strings": np.random.randint(50, 200),
                "has_network": np.random.choice([0, 1], p=[0.3, 0.7]),
                "has_file_operations": np.random.choice([0, 1], p=[0.2, 0.8]),
                "has_registry_operations": np.random.choice([0, 1], p=[0.3, 0.7]),
                "label": 1  # 恶意代码
            }
            malware_samples.append(sample)
        
        # 生成良性代码样本
        benign_samples = []
        for _ in range(500):
            sample = {
                "file_size": np.random.randint(10000, 500000),
                "num_sections": np.random.randint(2, 6),
                "has_debug": np.random.choice([0, 1], p=[0.5, 0.5]),
                "has_imports": 1,
                "num_imports": np.random.randint(5, 30),
                "has_exports": np.random.choice([0, 1], p=[0.8, 0.2]),
                "has_resources": np.random.choice([0, 1], p=[0.6, 0.4]),
                "entropy": np.random.uniform(2.0, 6.0),
                "num_strings": np.random.randint(20, 100),
                "has_network": np.random.choice([0, 1], p=[0.7, 0.3]),
                "has_file_operations": np.random.choice([0, 1], p=[0.5, 0.5]),
                "has_registry_operations": np.random.choice([0, 1], p=[0.6, 0.4]),
                "label": 0  # 良性代码
            }
            benign_samples.append(sample)
        
        # 合并样本
        self.samples = malware_samples + benign_samples
        np.random.shuffle(self.samples)
        
        # 提取特征和标签
        self.X = []
        self.y = []
        for sample in self.samples:
            features = [sample[feature] for feature in self.feature_names]
            self.X.append(features)
            self.y.append(sample["label"])
        
        self.X = np.array(self.X)
        self.y = np.array(self.y)
    
    def train_model(self):
        """训练模型"""
        print("\n--- 训练模型 ---")
        
        # 分割数据集
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        # 特征缩放
        self.scaler.fit(X_train)
        X_train_scaled = self.scaler.transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # 训练模型
        start_time = time.time()
        self.classifier.fit(X_train_scaled, y_train)
        training_time = time.time() - start_time
        
        # 评估模型
        y_pred = self.classifier.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        print(f"训练时间: {training_time:.2f} 秒")
        print(f"模型准确率: {accuracy:.2f}")
        print("分类报告:")
        print(report)
        
        return {
            "accuracy": accuracy,
            "report": report,
            "training_time": training_time
        }
    
    def extract_features(self, file_path):
        """提取文件特征"""
        print(f"\n--- 提取文件特征: {file_path} ---")
        
        # 模拟特征提取
        features = {
            "file_size": os.path.getsize(file_path) if os.path.exists(file_path) else np.random.randint(10000, 1000000),
            "num_sections": np.random.randint(2, 10),
            "has_debug": np.random.choice([0, 1]),
            "has_imports": 1,
            "num_imports": np.random.randint(5, 50),
            "has_exports": np.random.choice([0, 1]),
            "has_resources": np.random.choice([0, 1]),
            "entropy": np.random.uniform(2.0, 8.0),
            "num_strings": np.random.randint(20, 200),
            "has_network": np.random.choice([0, 1]),
            "has_file_operations": np.random.choice([0, 1]),
            "has_registry_operations": np.random.choice([0, 1])
        }
        
        print("提取的特征:")
        for feature, value in features.items():
            print(f"  - {feature}: {value}")
        
        # 转换为特征向量
        feature_vector = [features[feature] for feature in self.feature_names]
        return np.array(feature_vector).reshape(1, -1)
    
    def predict(self, file_path):
        """预测文件是否为恶意代码"""
        print(f"\n--- 预测文件: {file_path} ---")
        
        # 提取特征
        feature_vector = self.extract_features(file_path)
        
        # 特征缩放
        feature_vector_scaled = self.scaler.transform(feature_vector)
        
        # 预测
        prediction = self.classifier.predict(feature_vector_scaled)[0]
        probability = self.classifier.predict_proba(feature_vector_scaled)[0]
        
        # 输出结果
        if prediction == 1:
            print(f"预测结果: 恶意代码 (概率: {probability[1]:.2f})")
        else:
            print(f"预测结果: 良性代码 (概率: {probability[0]:.2f})")
        
        return {
            "prediction": "恶意代码" if prediction == 1 else "良性代码",
            "probability": float(probability[prediction])
        }
    
    def feature_importance(self):
        """分析特征重要性"""
        print("\n--- 分析特征重要性 ---")
        
        importances = self.classifier.feature_importances_
        feature_importance = list(zip(self.feature_names, importances))
        feature_importance.sort(key=lambda x: x[1], reverse=True)
        
        print("特征重要性排序:")
        for feature, importance in feature_importance:
            print(f"  - {feature}: {importance:.4f}")
        
        return feature_importance
    
    def generate_ml_report(self, predictions):
        """生成机器学习检测报告"""
        print("\n--- 生成机器学习检测报告 ---")
        
        report = {
            "report_info": {
                "title": "机器学习检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "detector": "MachineLearningDetection"
            },
            "model_info": {
                "model_type": "Random Forest",
                "feature_count": len(self.feature_names),
                "feature_names": self.feature_names
            },
            "predictions": predictions,
            "feature_importance": self.feature_importance(),
            "recommendations": [
                "定期更新训练数据，提高模型准确性",
                "结合其他检测技术，提高检测覆盖率",
                "持续优化特征提取方法",
                "使用集成学习方法，提高模型性能"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_ml_detection(self):
        """演示机器学习检测"""
        print("=== 机器学习检测演示 ===")
        print("========================")
        
        # 1. 显示特征列表
        print("\n1. 特征列表:")
        for i, feature in enumerate(self.feature_names, 1):
            print(f"   {i}. {feature}")
        
        # 2. 训练模型
        print("\n2. 训练模型:")
        self.train_model()
        
        # 3. 创建测试文件
        print("\n3. 创建测试文件:")
        test_files = ["test_file_1.exe", "test_file_2.exe", "test_file_3.exe"]
        for file in test_files:
            with open(file, 'w') as f:
                f.write("This is a test file.")
            print(f"创建测试文件: {file}")
        
        # 4. 预测测试文件
        print("\n4. 预测测试文件:")
        predictions = []
        for file in test_files:
            prediction = self.predict(file)
            predictions.append({
                "file": file,
                "prediction": prediction["prediction"],
                "probability": prediction["probability"]
            })
        
        # 5. 分析特征重要性
        print("\n5. 分析特征重要性:")
        self.feature_importance()
        
        # 6. 生成检测报告
        print("\n6. 生成检测报告:")
        self.generate_ml_report(predictions)
        
        # 7. 清理测试文件
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
                print(f"\n清理测试文件: {file}")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了机器学习在检测技术中的应用。")
        print("机器学习检测可以自动学习恶意代码的特征，提高检测的准确性和覆盖率。")

if __name__ == "__main__":
    ml_detection = MachineLearningDetection()
    ml_detection.demonstrate_ml_detection()