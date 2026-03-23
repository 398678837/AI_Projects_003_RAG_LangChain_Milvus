# Seaborn基础概念与环境

本示例展示了Seaborn的基本概念、样式设置和配置参数，帮助您快速上手Seaborn库。

## 功能说明

- 展示Seaborn的版本信息
- 演示不同的样式设置
- 展示颜色主题设置
- 演示上下文设置
- 加载和使用示例数据集
- 创建基本图形示例

## 代码结构

```python
# 1. 打印Seaborn版本
# 2. 基础样式设置
# 3. 颜色主题设置
# 4. 上下文设置
# 5. 加载示例数据集
# 6. 基本图形示例
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
   - 样式设置图表：style_*.png
   - 颜色主题图表：palette_*.png
   - 上下文设置图表：context_*.png
   - 基本散点图：basic_scatter.png

## 学习要点

- **Seaborn架构**：基于Matplotlib的高级数据可视化库
- **样式系统**：提供多种预设样式，如darkgrid、whitegrid等
- **颜色主题**：内置多种颜色方案，支持自定义调色板
- **上下文设置**：适应不同输出媒介的布局设置
- **示例数据集**：内置多个常用数据集，方便快速测试

## 扩展建议

- 尝试创建自定义颜色主题
- 探索更多Seaborn的配置选项
- 结合实际数据集进行可视化
- 学习Seaborn的高级功能和API