# 04_Search_Query_搜索查询

## 学习目标
- 掌握基本搜索
- 理解Query DSL
- 掌握常见查询类型
- 理解过滤器
- 掌握复合查询

## 关键要点
### 1. 基本搜索
- URI搜索
- Request Body搜索
- match查询
- match_all查询
- 返回字段过滤

### 2. Query DSL
- JSON格式查询
- Leaf queries：叶子查询
- Compound queries：复合查询
- 查询上下文
- 过滤上下文

### 3. 全文查询
- match查询
- match_phrase查询
- match_phrase_prefix查询
- multi_match查询
- query_string查询
- simple_query_string查询

### 4. 术语查询
- term查询
- terms查询
- range查询
- exists查询
- prefix查询
- wildcard查询
- regexp查询
- fuzzy查询

### 5. 复合查询
- bool查询
  - must：必须匹配
  - filter：过滤
  - should：应该匹配
  - must_not：必须不匹配
- boosting查询
- constant_score查询
- dis_max查询
- function_score查询

### 6. 过滤器
- filter上下文
- 不计算相关性评分
- 缓存结果
- 性能更好

### 7. 搜索结果
- 分页
- from和size
- sort排序
- source过滤
- highlight高亮

## 实践任务
1. 使用基本搜索
2. 使用Query DSL
3. 实现全文搜索
4. 使用复合查询
5. 实现分页和排序

## 参考资料
- Elasticsearch Query DSL
