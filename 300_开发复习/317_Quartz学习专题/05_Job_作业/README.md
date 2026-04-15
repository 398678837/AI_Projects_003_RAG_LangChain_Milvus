# 05_Job_作业

## 学习目标
- 理解Job接口
- 掌握Job的创建和执行
- 理解Job的并发控制
- 掌握Job数据持久化
- 理解Job的异常处理

## 关键要点
### 1. Job接口
- 所有任务必须实现
- execute()方法
- JobExecutionContext参数
- JobExecutionException异常

### 2. JobDetail
- Job的详细信息
- Job类
- Job身份
- JobDataMap
- 持久化选项

### 3. 并发控制
- @DisallowConcurrentExecution：禁止并发
- @PersistJobDataAfterExecution：持久化JobData
- 理解并发执行的影响

### 4. Job执行上下文
- JobExecutionContext
- 获取JobDetail
- 获取Trigger
- 获取Scheduler
- 获取执行时间

### 5. Job异常处理
- JobExecutionException
- refireImmediately：立即重试
- unscheduleFiringTrigger：取消调度
- unsetSchedulerFiringTrigger：不取消调度

### 6. StatefulJob
- 有状态的Job
- 已废弃，使用注解代替
- @PersistJobDataAfterExecution

### 7. Job监听器
- JobListener接口
- jobToBeExecuted()
- jobExecutionVetoed()
- jobWasExecuted()

## 实践任务
1. 创建自定义Job
2. 使用并发控制注解
3. 持久化Job数据
4. 处理Job异常
5. 实现Job监听器

## 参考资料
- Quartz Jobs
