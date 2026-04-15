# 07_Transaction_Message_事务消息

## 学习目标
- 理解事务消息概念
- 掌握两阶段提交
- 理解回查机制
- 实现事务消息
- 理解事务状态

## 关键要点
### 1. 事务消息概念
- 分布式事务
- 消息和本地事务一致
- 两阶段提交
- 回查机制

### 2. 两阶段提交
- 第一阶段：发送Half消息
- 第二阶段：提交或回滚
- Commit/Rollback

### 3. 回查机制
- 定时回查
- 检查本地事务状态
- 最长回查时间
- 回查次数

### 4. 事务监听器
- TransactionListener
- executeLocalTransaction
- checkLocalTransaction

### 5. 事务状态
- TransactionStatus.COMMIT_MESSAGE
- TransactionStatus.ROLLBACK_MESSAGE
- TransactionStatus.UNKNOWN

## 实践任务
1. 实现事务消息
2. 实现事务监听器
3. 处理回查
4. 理解事务状态

## 参考资料
- RocketMQ Transaction Message
