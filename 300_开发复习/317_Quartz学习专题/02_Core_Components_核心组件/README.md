# 02_Core_Components_核心组件

## 学习目标
- 理解Quartz的核心组件
- 掌握Job和JobDetail
- 理解Trigger的类型和使用
- 掌握Scheduler的使用
- 理解JobDataMap的作用

## 关键要点
### 1. Job接口
- 所有任务必须实现的接口
- 只有一个execute()方法
- 无参构造函数
- 可以抛出JobExecutionException

### 2. JobDetail
- Job的详细信息
- Job的元数据
- JobDataMap
- Job的身份标识（name/group）
- 持久化选项
- 并发执行控制

### 3. Trigger
- 定义任务执行时间
- 多种Trigger类型
- SimpleTrigger：简单触发器
- CronTrigger：Cron表达式触发器
- CalendarIntervalTrigger：日历间隔触发器
- DailyTimeIntervalTrigger：每日时间间隔触发器

### 4. Scheduler
- Quartz的核心调度器
- 管理Job和Trigger
- 启动、暂停、恢复、停止
- 调度任务
- 监听任务执行

### 5. JobDataMap
- 传递参数给Job
- Map类型的数据结构
- 支持基本类型和对象
- 可以从JobDetail或Trigger获取

### 6. JobBuilder和TriggerBuilder
- 链式API
- 简化JobDetail和Trigger创建
- 提供常用配置方法

## 实践任务
1. 使用JobBuilder创建JobDetail
2. 使用TriggerBuilder创建Trigger
3. 使用JobDataMap传递参数
4. 理解不同Trigger类型的使用

## 参考资料
- Quartz Core Components
