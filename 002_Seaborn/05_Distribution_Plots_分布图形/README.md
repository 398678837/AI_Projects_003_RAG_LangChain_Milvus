# Seaborn分布图形

本示例展示了Seaborn中各种分布图形的绘制方法，包括直方图、核密度估计图、经验累积分布函数图、双变量分布、多变量分布和小提琴图。

## 功能说明

- 直方图：展示数据的频率分布
- 核密度估计图：展示数据的概率密度
- 经验累积分布函数图：展示数据的累积分布
- 双变量分布：展示两个变量的联合分布
- 多变量分布：展示多个变量之间的关系
- 小提琴图：展示数据的分布密度

## 代码结构

```python
# 1. 直方图
# 2. 核密度估计图
# 3. 经验累积分布函数图
# 4. 双变量分布
# 5. 多变量分布
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
   - 直方图：histplot_basic.png, histplot_kde.png, histplot_grouped.png
   - 核密度估计图：kdeplot_basic.png, kdeplot_fill.png, kdeplot_grouped.png
   - 经验累积分布函数图：ecdfplot_basic.png, ecdfplot_grouped.png
   - 双变量分布：jointplot_basic.png, jointplot_kde.png, jointplot_hist.png
   - 多变量分布：pairplot_basic.png, pairplot_hue.png
   - 小提琴图：violinplot_basic.png, violinplot_split.png

## 学习要点

- **直方图**：使用sns.histplot()，可展示数据的频率分布
- **核密度估计图**：使用sns.kdeplot()，可展示数据的概率密度
- **经验累积分布函数图**：使用sns.ecdfplot()，可展示数据的累积分布
- **双变量分布**：使用sns.jointplot()，可展示两个变量的联合分布
- **多变量分布**：使用sns.pairplot()，可展示多个变量之间的关系
- **小提琴图**：使用sns.violinplot()，可展示数据的分布密度

## 扩展建议

- 尝试不同的参数组合，如bins、bw_method等
- 探索更多Seaborn的分布图形类型
- 结合实际数据集进行分布分析
- 学习如何自定义分布图形的样式和布局