# Scikit-learn数据预处理

本示例展示了Scikit-learn中各种数据预处理方法，包括数据标准化、归一化、编码、缺失值处理、特征选择、数据变换和管道。

## 功能说明

- 数据标准化：将数据转换为均值为0，标准差为1的分布
- 数据归一化：将数据缩放到特定范围
- 数据编码：将分类数据转换为数值表示
- 缺失值处理：处理数据中的缺失值
- 特征选择：选择对模型最有价值的特征
- 数据变换：对数据进行各种变换
- 管道：将多个预处理步骤组合成一个流程

## 代码结构

```python
# 1. 数据标准化
# 2. 数据归一化
# 3. 数据编码
# 4. 缺失值处理
# 5. 特征选择
# 6. 数据变换
# 7. 管道
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

- **数据标准化**：使用StandardScaler，适用于大多数机器学习算法
- **数据归一化**：使用MinMaxScaler、MaxAbsScaler和RobustScaler，适用于对特征范围有要求的算法
- **数据编码**：使用LabelEncoder、OneHotEncoder和OrdinalEncoder，处理分类数据
- **缺失值处理**：使用SimpleImputer和KNNImputer，处理数据中的缺失值
- **特征选择**：使用VarianceThreshold和SelectKBest，选择重要特征
- **数据变换**：使用PolynomialFeatures和FunctionTransformer，创建新特征
- **管道**：使用Pipeline，将多个预处理步骤组合成一个流程

## 扩展建议

- 尝试不同的预处理方法组合
- 探索更多的特征选择方法
- 学习如何处理文本数据和时间序列数据
- 尝试自定义预处理转换器
- 学习如何使用ColumnTransformer处理混合类型的数据