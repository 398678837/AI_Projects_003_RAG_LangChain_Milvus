# Scikit-learn无监督学习

本示例展示了Scikit-learn中各种无监督学习算法，包括聚类算法、降维算法、密度估计、异常检测和特征学习。

## 功能说明

- 聚类算法：包括K-means、层次聚类和DBSCAN
- 降维算法：包括PCA、t-SNE、Isomap和TruncatedSVD
- 密度估计：包括核密度估计和高斯混合模型
- 异常检测：包括Isolation Forest、Local Outlier Factor和Elliptic Envelope
- 特征学习：包括PCA和NMF

## 代码结构

```python
# 1. 聚类算法
# 2. 降维算法
# 3. 密度估计
# 4. 异常检测
# 5. 特征学习
```

## 配置说明

1. **依赖包**：
   - scikit-learn
   - numpy
   - pandas
   - matplotlib

2. **安装依赖**：
   ```bash
   pip install -r ../../requirements.txt
   ```

## 运行示例

1. 运行示例代码：
   ```bash
   python demo.py
   ```

## 学习要点

- **聚类算法**：用于将数据点分组到不同的簇中，如K-means、层次聚类和DBSCAN
- **降维算法**：用于减少数据的维度，如PCA、t-SNE和Isomap
- **密度估计**：用于估计数据的概率密度函数，如核密度估计和高斯混合模型
- **异常检测**：用于识别数据中的异常值，如Isolation Forest和Local Outlier Factor
- **特征学习**：用于从数据中学习有效的特征表示，如PCA和NMF

## 扩展建议

- 尝试不同的聚类算法参数
- 探索更多的降维技术
- 学习如何评估聚类结果
- 尝试使用无监督学习进行数据预处理
- 探索深度学习中的无监督学习方法