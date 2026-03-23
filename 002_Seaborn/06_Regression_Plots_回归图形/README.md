# Seaborn回归图形

本示例展示了Seaborn中各种回归图形的绘制方法，包括基本回归图、不同类型的回归模型、残差图、联合回归图、分类回归图和复杂回归模型。

## 功能说明

- 基本回归图：展示变量之间的线性关系
- 不同类型的回归模型：拟合线性和多项式回归
- 残差图：展示回归模型的残差分布
- 联合回归图：结合散点图和回归分析
- 分类回归图：展示分类数据的回归关系
- 复杂回归模型：包含多个预测变量的回归分析

## 代码结构

```python
# 1. 基本回归图
# 2. 拟合不同类型的回归模型
# 3. 残差图
# 4. 联合回归图
# 5. 分类回归图
# 6. 复杂回归模型
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
   - 基本回归图：regplot_basic.png, regplot_ci.png, regplot_hue.png
   - 不同类型的回归模型：regplot_linear.png, regplot_polynomial.png
   - 残差图：residplot_basic.png
   - 联合回归图：jointplot_reg.png
   - 分类回归图：catplot_point.png
   - 复杂回归模型：lmplot_complex.png

## 学习要点

- **基本回归图**：使用sns.regplot()，可展示变量之间的线性关系
- **不同类型的回归模型**：通过order参数拟合不同阶数的多项式回归
- **残差图**：使用sns.residplot()，可展示回归模型的残差分布
- **联合回归图**：使用sns.jointplot() with kind="reg"，可结合散点图和回归分析
- **分类回归图**：使用sns.catplot() with kind="point"，可展示分类数据的回归关系
- **复杂回归模型**：使用sns.lmplot()，可包含多个预测变量的回归分析

## 扩展建议

- 尝试不同的回归参数，如robust、logistic等
- 探索更多Seaborn的回归图形类型
- 结合实际数据集进行回归分析
- 学习如何自定义回归图形的样式和布局