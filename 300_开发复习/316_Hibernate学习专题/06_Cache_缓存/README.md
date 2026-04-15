# 06_Cache_缓存

## 学习目标
- 理解Hibernate缓存机制
- 掌握一级缓存
- 理解二级缓存
- 学会查询缓存
- 理解缓存策略

## 关键要点
### 1. 缓存概述
- 提高查询性能
- 减少数据库访问
- 一级缓存和二级缓存
- 查询缓存

### 2. 一级缓存
- Session级别缓存
- 默认开启
- 同一会话内有效
- 自动管理
- evict()：清除单个对象
- clear()：清除所有对象
- contains()：判断是否在缓存中

### 3. 二级缓存
- SessionFactory级别缓存
- 需要手动配置
- 跨会话共享
- 常用缓存提供商：Ehcache、Infinispan
- @Cacheable：标记可缓存
- @Cache：缓存配置

### 4. 查询缓存
- 缓存查询结果
- 需要手动启用
- setCacheable(true)
- query.setCacheRegion()
- 依赖二级缓存

### 5. 缓存策略
- READ_ONLY：只读
- READ_WRITE：读写
- NONSTRICT_READ_WRITE：非严格读写
- TRANSACTIONAL：事务型

## 实践任务
1. 使用一级缓存
2. 配置和使用二级缓存
3. 使用查询缓存
4. 选择合适的缓存策略

## 参考资料
- Hibernate Caching
