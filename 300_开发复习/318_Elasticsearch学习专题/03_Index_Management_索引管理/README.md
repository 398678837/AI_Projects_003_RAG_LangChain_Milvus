# 03_Index_Management_索引管理

## 学习目标
- 掌握索引的创建和删除
- 理解映射（Mapping）
- 掌握索引配置
- 学会索引别名
- 理解索引模板

## 关键要点
### 1. 创建索引
- PUT /index_name
- settings配置
- mappings配置
- 分片和副本配置
- 响应状态码

### 2. 删除索引
- DELETE /index_name
- 多个索引删除
- 删除所有索引

### 3. 索引信息
- GET /index_name
- GET /_cat/indices
- GET /index_name/_settings
- GET /index_name/_mapping

### 4. 映射（Mapping）
- 动态映射
- 显式映射
- 字段类型
- 字段属性
- 嵌套对象
- 动态模板

### 5. 索引设置
- 分片数
- 副本数
- 刷新间隔
- 只读设置
- 分析器配置

### 6. 索引别名
- 创建别名
- 删除别名
- 别名操作
- 路由别名
- 过滤别名

### 7. 索引模板
- 创建模板
- 模板优先级
- 索引模式匹配
- 动态模板

### 8. 索引操作
- 打开/关闭索引
- 收缩索引
- 拆分索引
- 重新索引

## 实践任务
1. 创建和删除索引
2. 配置索引映射
3. 使用索引别名
4. 创建索引模板

## 参考资料
- Elasticsearch Index Management
