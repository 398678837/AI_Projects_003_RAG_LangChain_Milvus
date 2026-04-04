# Seaborn实战应用

本示例展示了Seaborn在实际数据分析中的应用，包括销售数据分析、客户数据分析、股票数据分析、天气数据分析和学生成绩分析。

## 功能说明

- 销售数据分析：展示产品销售趋势和对比
- 客户数据分析：分析客户年龄分布、性别与消费关系
- 股票数据分析：展示股票价格趋势和相关性
- 天气数据分析：分析温度和湿度趋势
- 学生成绩分析：分析不同科目的成绩分布

## 代码结构

```python
# 1. 销售数据分析
# 2. 客户数据分析
# 3. 股票数据分析
# 4. 天气数据分析
# 5. 学生成绩分析
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
   - 销售数据分析：sales_trend.png, sales_by_product.png
   - 客户数据分析：customer_age_dist.png, spending_by_gender.png, age_vs_spending.png
   - 股票数据分析：stock_trends.png, stock_correlation.png
   - 天气数据分析：weather_trends.png, monthly_temperature.png, temp_vs_humidity.png
   - 学生成绩分析：grade_distribution.png, grade_violin.png, overall_grade_dist.png

## 学习要点

- **销售数据分析**：使用sns.lineplot()和sns.barplot()展示销售趋势和对比
- **客户数据分析**：使用sns.histplot(), sns.boxplot()和sns.scatterplot()分析客户数据
- **股票数据分析**：使用sns.lineplot()和sns.heatmap()分析股票数据
- **天气数据分析**：使用sns.lineplot(), sns.barplot()和sns.scatterplot()分析天气数据
- **学生成绩分析**：使用sns.boxplot(), sns.violinplot()和sns.histplot()分析学生成绩

## 扩展建议

- 使用真实的数据集进行分析
- 尝试更多的Seaborn图形类型
- 结合统计分析方法进行深入分析
- 学习如何将Seaborn图形集成到Web应用中