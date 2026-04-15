# 07_API_Interface_API接口

## 学习目标
- 掌握RESTful API
- 理解HTTP方法
- 掌握索引API
- 掌握文档API
- 掌握搜索API

## 关键要点
### 1. RESTful API
- 基于HTTP
- JSON格式
- 标准HTTP方法
  - GET：查询
  - POST：创建/更新
  - PUT：创建/更新
  - DELETE：删除
  - HEAD：检查存在

### 2. 索引API
- 创建索引：PUT /index
- 删除索引：DELETE /index
- 获取索引：GET /index
- 检查存在：HEAD /index
- 打开/关闭：POST /index/_open/_close
- 刷新：POST /index/_refresh

### 3. 文档API
- 创建文档：POST /index/_doc
- 创建指定ID：PUT /index/_doc/id
- 获取文档：GET /index/_doc/id
- 更新文档：POST /index/_update/id
- 删除文档：DELETE /index/_doc/id
- 批量操作：_bulk
- 多文档获取：_mget

### 4. 搜索API
- 基本搜索：GET /index/_search
- URI搜索：使用q参数
- Request Body搜索：JSON查询
- 分页：from和size
- 排序：sort
- 过滤：_source
- 高亮：highlight

### 5. 批量API
- _bulk API
- 批量索引
- 批量更新
- 批量删除
- 格式要求

### 6. 集群API
- 集群健康：_cluster/health
- 集群状态：_cluster/state
- 节点信息：_nodes
- 节点统计：_nodes/stats
- 任务管理：_tasks

### 7. 其他API
- 别名API：_aliases
- 模板API：_index_template
- 重新索引：_reindex
- 更新设置：_settings
- 更新映射：_mapping

## 实践任务
1. 使用索引API
2. 使用文档API
3. 使用搜索API
4. 使用批量API

## 参考资料
- Elasticsearch REST API
