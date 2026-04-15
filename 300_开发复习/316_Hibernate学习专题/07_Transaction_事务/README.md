# 07_Transaction_事务

## 学习目标
- 理解事务的ACID特性
- 掌握Hibernate事务管理
- 理解并发问题
- 掌握事务隔离级别
- 理解声明式事务

## 关键要点
### 1. 事务概述
- ACID特性：原子性、一致性、隔离性、持久性
- 保证数据完整性
- 回滚机制

### 2. Hibernate事务管理
- beginTransaction()：开始事务
- commit()：提交事务
- rollback()：回滚事务
- getTransaction()：获取当前事务

### 3. 事务边界
- 每个操作一个事务
- 多个操作一个事务
- 长事务 vs 短事务
- 会话与事务的关系

### 4. 并发问题
- 脏读
- 不可重复读
- 幻读
- 更新丢失

### 5. 事务隔离级别
- READ_UNCOMMITTED：读未提交
- READ_COMMITTED：读已提交（默认）
- REPEATABLE_READ：可重复读
- SERIALIZABLE：串行化

### 6. 锁机制
- 乐观锁
- 悲观锁
- @Version：乐观锁版本号
- LockMode：锁模式

### 7. 声明式事务
- Spring集成
- @Transactional注解
- 事务传播行为
- 事务回滚规则

## 实践任务
1. 使用编程式事务
2. 处理事务回滚
3. 使用乐观锁和悲观锁
4. 配置事务隔离级别

## 参考资料
- Hibernate Transactions
