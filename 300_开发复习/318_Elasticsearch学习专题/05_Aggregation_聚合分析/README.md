# 05_Aggregation_聚合分析

## 学习目标
- 理解聚合的概念
- 掌握Metric聚合
- 掌握Bucket聚合
- 理解Pipeline聚合
- 学会组合使用聚合

## 关键要点
### 1. 聚合概述
- 聚合分析数据
- 类似SQL的GROUP BY
- 三种聚合类型
- 聚合可以嵌套

### 2. Metric聚合
- avg：平均值
- sum：求和
- min：最小值
- max：最大值
- stats：统计信息
- extended_stats：扩展统计
- value_count：值计数
- cardinality：基数统计
- percentiles：百分位数
- top_hits：顶部命中

### 3. Bucket聚合
- terms：词条聚合
- range：范围聚合
- date_range：日期范围
- histogram：直方图
- date_histogram：日期直方图
- filter：过滤聚合
- filters：多过滤聚合
- nested：嵌套聚合
- reverse_nested：反向嵌套

### 4. Pipeline聚合
- 基于其他聚合结果
- avg_bucket：桶平均值
- sum_bucket：桶求和
- min_bucket：桶最小值
- max_bucket：桶最大值
- stats_bucket：桶统计
- derivative：导数
- cumulative_sum：累计和
- moving_avg：移动平均

### 5. 聚合嵌套
- 多层嵌套
- Bucket中嵌套Metric
- Bucket中嵌套Bucket
- Pipeline基于其他聚合

### 6. 聚合性能
- 合理使用聚合
- 避免过度聚合
- 使用缓存
- 分片优化

## 实践任务
1. 使用Metric聚合
2. 使用Bucket聚合
3. 使用Pipeline聚合
4. 组合使用多种聚合

## 参考资料
- Elasticsearch Aggregations
