# 03_Scheduler_调度器

## 学习目标
- 理解Scheduler的作用
- 掌握Scheduler的生命周期
- 学会调度和取消任务
- 理解Scheduler的状态管理
- 掌握Scheduler的配置

## 关键要点
### 1. Scheduler概述
- Quartz的核心组件
- 管理Job和Trigger
- 负责任务调度
- 提供调度API

### 2. Scheduler工厂
- StdSchedulerFactory：标准工厂
- DirectSchedulerFactory：直接工厂
- 从配置文件创建
- 编程方式创建

### 3. Scheduler生命周期
- 实例化
- 启动（start()）
- 待机（standby()）
- 关闭（shutdown()）
- 停止（pause()）

### 4. 调度任务
- scheduleJob()：调度任务
- addJob()：添加Job
- triggerJob()：立即触发Job
- unscheduleJob()：取消调度
- deleteJob()：删除Job

### 5. 管理任务和触发器
- 检查Job/Trigger是否存在
- 获取Job/Trigger列表
- 获取下一次执行时间
- 暂停/恢复Job/Trigger

### 6. Scheduler状态
- isStarted()：是否启动
- isInStandbyMode()：是否待机
- isShutdown()：是否关闭
- getMetaData()：获取元数据

### 7. Scheduler配置
- quartz.properties配置文件
- 线程池配置
- 作业存储配置
- 插件配置
- 监听器配置

## 实践任务
1. 创建和启动Scheduler
2. 调度和取消任务
3. 暂停和恢复任务
4. 管理Scheduler的状态

## 参考资料
- Quartz Scheduler
