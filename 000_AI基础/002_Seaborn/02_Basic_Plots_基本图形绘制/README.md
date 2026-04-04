# Seaborn基本图形绘制

本示例展示了Seaborn中各种基本图形的绘制方法，包括散点图、线图、柱状图、直方图、箱线图和小提琴图。

## 功能说明

- 散点图：展示两个变量之间的关系
- 线图：展示数据随时间的变化趋势
- 柱状图：比较不同类别的数据
- 直方图：展示数据的分布情况
- 箱线图：展示数据的统计分布
- 小提琴图：结合箱线图和密度图的特点

## 代码结构

```python
# 1. 散点图
# 2. 线图
# 3. 柱状图
# 4. 直方图
# 5. 箱线图
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
   - 散点图：scatter_basic.png, scatter_categories.png
   - 线图：line_basic.png, line_multiple.png
   - 柱状图：bar_basic.png, bar_error.png
   - 直方图：hist_basic.png, hist_density.png
   - 箱线图：box_basic.png, box_grouped.png
   - 小提琴图：violin_basic.png, violin_grouped.png

## 学习要点

- **散点图**：使用sns.scatterplot()，可通过hue和style参数添加分类信息
- **线图**：使用sns.lineplot()，可绘制时间序列和多条线
- **柱状图**：使用sns.barplot()，自动计算误差条
- **直方图**：使用sns.histplot()，可添加密度曲线
- **箱线图**：使用sns.boxplot()，展示数据的四分位数
- **小提琴图**：使用sns.violinplot()，展示数据的分布密度

## 扩展建议

- 尝试不同的参数组合，如size、alpha等
- 探索更多Seaborn的图形类型
- 结合实际数据集进行可视化
- 学习如何自定义图形样式和布局