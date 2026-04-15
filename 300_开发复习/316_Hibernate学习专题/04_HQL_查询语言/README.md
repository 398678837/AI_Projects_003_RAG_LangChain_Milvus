# 04_HQL_查询语言

## 学习目标
- 理解HQL的基本语法
- 掌握基本查询
- 学会条件查询
- 掌握聚合函数
- 理解关联查询

## 关键要点
### 1. HQL概述
- Hibernate Query Language
- 面向对象的查询语言
- 语法类似SQL
- 查询对象而不是表

### 2. 基本查询
- FROM：指定查询的实体
- SELECT：选择属性
- AS：别名
- DISTINCT：去重

### 3. 条件查询
- WHERE：条件子句
- 比较运算符：=, <>, <, >, <=, >=
- 逻辑运算符：AND, OR, NOT
- LIKE：模糊查询
- IN：范围查询
- BETWEEN：区间查询
- IS NULL：空值判断

### 4. 排序和分页
- ORDER BY：排序
- ASC/DESC：升序/降序
- setFirstResult()：起始位置
- setMaxResults()：每页数量

### 5. 聚合函数
- COUNT()：计数
- SUM()：求和
- AVG()：平均值
- MAX()：最大值
- MIN()：最小值
- GROUP BY：分组
- HAVING：分组条件

### 6. 关联查询
- 内连接：JOIN
- 左连接：LEFT JOIN
- 右连接：RIGHT JOIN
- 隐式连接

### 7. 子查询
- 嵌套查询
- EXISTS
- ALL
- ANY

## 实践任务
1. 编写基本HQL查询
2. 实现条件查询
3. 实现分页查询
4. 使用聚合函数
5. 实现关联查询

## 参考资料
- Hibernate Query Language
