# Seaborn统计图形

本示例展示了Seaborn中各种统计图形的绘制方法，包括热力图、散点图矩阵、联合分布图、回归图、分类图和小提琴图。

## 功能说明

- 热力图：展示数据矩阵的相关性
- 散点图矩阵：展示多个变量之间的关系
- 联合分布图：展示两个变量的联合分布
- 回归图：展示变量之间的线性关系
- 分类图：展示分类数据的分布
- 小提琴图：展示数据的分布密度

## 代码结构

```python
# 1. 热力图
# 2. 散点图矩阵
# 3. 联合分布图
# 4. 回归图
# 5. 分类图
# 6. 小提琴图
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
   - 热力图：heatmap_corr.png, heatmap_flights.png
   - 散点图矩阵：pairplot_iris.png
   - 联合分布图：jointplot_basic.png, jointplot_kde.png
   - 回归图：regplot_basic.png, regplot_ci.png
   - 分类图：catplot_box.png, catplot_bar.png
   - 小提琴图：violinplot_basic.png, violinplot_split.png

## 学习要点

- **热力图**：使用sns.heatmap()，可展示数据矩阵的相关性
- **散点图矩阵**：使用sns.pairplot()，可展示多个变量之间的关系
- **联合分布图**：使用sns.jointplot()，可展示两个变量的联合分布
- **回归图**：使用sns.regplot()，可展示变量之间的线性关系
- **分类图**：使用sns.catplot()，可展示分类数据的分布
- **小提琴图**：使用sns.violinplot()，可展示数据的分布密度

## 扩展建议

- 尝试不同的颜色映射和参数设置
- 探索更多Seaborn的统计图形类型
- 结合实际数据集进行统计分析
- 学习如何自定义统计图形的样式和布局