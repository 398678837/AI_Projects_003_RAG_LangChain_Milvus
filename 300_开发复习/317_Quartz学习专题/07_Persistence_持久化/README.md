# 07_Persistence_持久化

## 学习目标
- 理解Quartz持久化的作用
- 掌握JDBC JobStore配置
- 学会配置数据源
- 理解集群持久化
- 掌握持久化数据管理

## 关键要点
### 1. 持久化概述
- RAMJobStore：内存存储
- JDBCJobStore：数据库持久化
- 应用重启后恢复
- 集群支持

### 2. RAMJobStore
- 默认存储
- 内存存储，速度快
- 重启丢失数据
- 适合开发测试
- 不支持集群

### 3. JDBCJobStore
- 数据库持久化
- 支持多种数据库
- 应用重启不丢失
- 支持集群
- 需要配置数据源

### 4. 配置持久化
- quartz.properties配置
- 数据源配置
- 表结构初始化
- 事务配置

### 5. 数据库表
- QRTZ_JOB_DETAILS：Job详情
- QRTZ_TRIGGERS：触发器
- QRTZ_CRON_TRIGGERS：Cron触发器
- QRTZ_SIMPLE_TRIGGERS：简单触发器
- QRTZ_BLOB_TRIGGERS：Blob触发器
- QRTZ_SCHEDULER_STATE：调度器状态
- QRTZ_LOCKS：锁表

### 6. 数据源配置
- 使用连接池
- DBCP/C3P0/HikariCP
- JNDI数据源
- 事务管理器

### 7. 持久化最佳实践
- 合理选择存储方式
- 定期清理历史数据
- 备份数据库
- 监控数据库性能

## 实践任务
1. 配置JDBCJobStore
2. 初始化数据库表
3. 测试持久化功能
4. 重启应用恢复任务

## 参考资料
- Quartz Job Storage
