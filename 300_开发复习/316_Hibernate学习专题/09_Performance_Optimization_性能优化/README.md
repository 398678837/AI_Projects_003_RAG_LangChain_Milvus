# 09_Performance_Optimization_性能优化

## 学习目标
- 理解Hibernate性能优化策略
- 掌握查询优化
- 理解抓取策略
- 学会索引优化
- 理解N+1查询问题

## 关键要点
### 1. 性能优化概述
- 减少数据库访问
- 优化查询
- 合理使用缓存
- 索引优化

### 2. 查询优化
- 避免N+1查询
- 使用抓取策略
- 使用批量抓取
- 使用子查询
- 投影查询

### 3. 抓取策略
- FetchType.LAZY：懒加载
- FetchType.EAGER：立即加载
- @Fetch：抓取模式
- JOIN FETCH
- @BatchSize：批量抓取

### 4. N+1查询问题
- 问题描述
- 解决方案：JOIN FETCH
- 解决方案：@BatchSize
- 解决方案：二级缓存

### 5. 索引优化
- @Index：索引
- 复合索引
- 唯一索引
- 查询分析

### 6. 其他优化
- 使用二级缓存
- 使用查询缓存
- 批量操作
- 合理设置flush模式
- 使用StatelessSession

## 实践任务
1. 解决N+1查询问题
2. 优化抓取策略
3. 使用批量抓取
4. 添加索引优化

## 参考资料
- Hibernate Performance Tuning
