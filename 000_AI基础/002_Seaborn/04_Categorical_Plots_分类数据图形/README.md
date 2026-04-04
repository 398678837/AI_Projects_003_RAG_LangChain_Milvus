# Seaborn分类数据图形

本示例展示了Seaborn中各种分类数据图形的绘制方法，包括条形图、计数图、箱线图、小提琴图、点图、分类散点图和蜂群图。

## 功能说明

- 条形图：展示分类数据的均值和置信区间
- 计数图：展示分类数据的计数
- 箱线图：展示分类数据的统计分布
- 小提琴图：展示分类数据的分布密度
- 点图：展示分类数据的趋势
- 分类散点图：展示分类数据的分布
- 蜂群图：展示分类数据的分布，避免点重叠

## 代码结构

```python
# 1. 条形图
# 2. 计数图
# 3. 箱线图
# 4. 小提琴图
# 5. 点图
# 6. 分类散点图
# 7. 蜂群图
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
   - 条形图：barplot_basic.png, barplot_grouped.png, barplot_horizontal.png
   - 计数图：countplot_basic.png, countplot_grouped.png
   - 箱线图：boxplot_basic.png, boxplot_grouped.png
   - 小提琴图：violinplot_basic.png, violinplot_split.png
   - 点图：pointplot_basic.png, pointplot_grouped.png
   - 分类散点图：stripplot_basic.png, stripplot_jitter.png
   - 蜂群图：swarmplot_basic.png, swarmplot_grouped.png

## 学习要点

- **条形图**：使用sns.barplot()，展示分类数据的均值和置信区间
- **计数图**：使用sns.countplot()，展示分类数据的计数
- **箱线图**：使用sns.boxplot()，展示分类数据的统计分布
- **小提琴图**：使用sns.violinplot()，展示分类数据的分布密度
- **点图**：使用sns.pointplot()，展示分类数据的趋势
- **分类散点图**：使用sns.stripplot()，展示分类数据的分布
- **蜂群图**：使用sns.swarmplot()，展示分类数据的分布，避免点重叠

## 扩展建议

- 尝试不同的参数组合，如order、hue_order等
- 探索更多Seaborn的分类图形类型
- 结合实际数据集进行分类分析
- 学习如何自定义分类图形的样式和布局