# 08_Spring_Integration_Spring集成

## 学习目标
- 理解Quartz与Spring集成
- 掌握Spring配置Quartz
- 学会使用SchedulerFactoryBean
- 理解声明式调度
- 掌握Spring Boot集成

## 关键要点
### 1. Spring集成概述
- SchedulerFactoryBean
- JobDetailFactoryBean
- CronTriggerFactoryBean
- SimpleTriggerFactoryBean
- 自动配置

### 2. SchedulerFactoryBean
- 创建和配置Scheduler
- 自动启动
- 配置JobStore
- 配置数据源
- 配置监听器

### 3. Job配置
- JobDetailFactoryBean
- MethodInvokingJobDetailFactoryBean
- 调用Bean方法
- 传递参数

### 4. Trigger配置
- CronTriggerFactoryBean
- SimpleTriggerFactoryBean
- 配置JobDetail
- 配置调度时间

### 5. 声明式调度
- @Scheduled注解
- 启用调度
- Cron表达式
- 固定间隔
- 固定延迟

### 6. Spring Boot集成
- 自动配置
- spring-boot-starter-quartz
- 配置属性
- yml/properties配置

### 7. 最佳实践
- 合理配置线程池
- 使用持久化
- 监控调度
- 异常处理

## 实践任务
1. 使用XML配置Quartz
2. 使用Java配置Quartz
3. 使用@Scheduled注解
4. Spring Boot集成Quartz

## 参考资料
- Spring Quartz Integration
