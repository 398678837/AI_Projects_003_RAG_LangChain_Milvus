# 05_Criteria_API_CriteriaAPI

## 学习目标
- 理解Criteria API的基本概念
- 掌握基本查询
- 学会条件查询
- 理解关联查询
- 掌握动态查询

## 关键要点
### 1. Criteria API概述
- 类型安全的查询API
- 面向对象的查询方式
- 动态查询构建
- 替代HQL的另一种方式

### 2. 基本查询
- createCriteria()：创建Criteria对象
- list()：执行查询返回列表
- uniqueResult()：返回单个结果

### 3. 条件查询
- Restrictions：条件类
- eq()：等于
- ne()：不等于
- gt()/lt()：大于/小于
- ge()/le()：大于等于/小于等于
- like()：模糊查询
- in()：范围查询
- between()：区间查询
- isNull()/isNotNull()：空值判断
- and()/or()：逻辑运算

### 4. 排序
- Order：排序类
- asc()：升序
- desc()：降序
- addOrder()：添加排序

### 5. 分页
- setFirstResult()：起始位置
- setMaxResults()：每页数量

### 6. 投影
- Projections：投影类
- property()：属性投影
- count()：计数
- sum()/avg()/max()/min()：聚合
- group()：分组

### 7. 关联查询
- createAlias()：创建别名
- createCriteria()：创建子Criteria
- fetch：关联加载

## 实践任务
1. 使用Criteria API进行基本查询
2. 实现条件查询
3. 实现排序和分页
4. 使用投影和聚合
5. 实现关联查询

## 参考资料
- Hibernate Criteria API
