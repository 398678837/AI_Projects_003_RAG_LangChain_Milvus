# 08_Batch_Operations_批量操作

## 学习目标
- 理解批量操作的重要性
- 掌握批量插入
- 学会批量更新
- 掌握批量删除
- 理解批量操作优化

## 关键要点
### 1. 批量操作概述
- 减少数据库往返
- 提高性能
- 批量插入、批量更新、批量删除

### 2. 批量插入
- hibernate.jdbc.batch_size
- flush()和clear()
- Session.flush()：强制刷新
- Session.clear()：清除一级缓存
- StatelessSession：无状态会话

### 3. 批量更新
- HQL批量更新
- Criteria批量更新
- SQL批量更新
- 注意一级缓存

### 4. 批量删除
- HQL批量删除
- Criteria批量删除
- SQL批量删除
- 级联删除

### 5. 性能优化
- 合理设置batch_size
- 及时flush和clear
- 使用StatelessSession
- 禁用二级缓存
- 使用JDBC批量操作

## 实践任务
1. 使用批量插入
2. 使用批量更新
3. 使用批量删除
4. 优化批量操作性能

## 参考资料
- Hibernate Batch Processing
