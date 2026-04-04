# Seaborn热力图

本示例展示了Seaborn中热力图的绘制方法，包括基本热力图、相关矩阵热力图、分类数据热力图、时间序列热力图、自定义热力图和聚类热力图。

## 功能说明

- 基本热力图：展示二维数据矩阵
- 相关矩阵热力图：展示变量之间的相关性
- 分类数据热力图：展示分类数据的聚合结果
- 时间序列热力图：展示时间序列数据的变化
- 自定义热力图：自定义热力图的样式和参数
- 聚类热力图：展示数据的聚类结果

## 代码结构

```python
# 1. 基本热力图
# 2. 相关矩阵热力图
# 3. 分类数据热力图
# 4. 时间序列热力图
# 5. 自定义热力图
# 6. 聚类热力图
```

## 配置说明

1. **依赖包**：
   - seaborn
   - matplotlib
   - numpy
   - pandas

2. **安装依赖**：
   ```bash
   pip install -r ../../requirements.txt
   ```

## 运行示例

1. 运行示例代码：
   ```bash
   python demo.py
   ```

2. 查看生成的图表：
   - 基本热力图：heatmap_basic.png, heatmap_annot.png
   - 相关矩阵热力图：heatmap_correlation.png
   - 分类数据热力图：heatmap_categorical.png
   - 时间序列热力图：heatmap_timeseries.png
   - 自定义热力图：heatmap_custom.png
   - 聚类热力图：heatmap_cluster.png

## 学习要点

- **基本热力图**：使用sns.heatmap()，可展示二维数据矩阵
- **相关矩阵热力图**：使用sns.heatmap()展示相关矩阵，可使用cmap参数设置颜色映射
- **分类数据热力图**：先创建透视表，再使用sns.heatmap()展示
- **时间序列热力图**：使用pivot()创建时间序列矩阵，再使用sns.heatmap()展示
- **自定义热力图**：通过各种参数自定义热力图的样式
- **聚类热力图**：使用sns.clustermap()，可展示数据的聚类结果

## 扩展建议

- 尝试不同的颜色映射和参数设置
- 探索更多Seaborn的热力图功能
- 结合实际数据集创建热力图
- 学习如何自定义热力图的样式和布局