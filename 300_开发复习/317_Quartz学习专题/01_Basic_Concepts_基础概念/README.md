# 01_Basic_Concepts_基础概念

## 学习目标
- 理解Quartz的基本概念
- 掌握Quartz的核心架构
- 学会配置Quartz
- 理解Quartz的工作原理
- 掌握第一个Quartz程序的编写

## 关键要点
### 1. Quartz概述
- Quartz是一个开源的任务调度框架
- 由OpenSymphony组织开发
- 完全用Java编写
- 功能强大且灵活
- 支持简单和复杂的调度需求

### 2. Quartz核心概念
- Job：要执行的任务
- JobDetail：Job的详细信息
- Trigger：触发器，定义任务执行时间
- Scheduler：调度器，管理Job和Trigger
- JobDataMap：传递参数给Job

### 3. Quartz应用场景
- 定时发送邮件
- 定时数据备份
- 定时报表生成
- 定时数据同步
- 定时清理任务
- 定时提醒服务

### 4. Quartz特点
- 灵活的调度机制
- 支持多种触发器类型
- 支持集群部署
- 支持JDBC持久化
- 支持事务
- 支持监听器
- 支持插件

### 5. 环境搭建
- 引入Quartz依赖
- 配置quartz.properties
- 创建SchedulerFactory
- 创建Scheduler
- 启动和关闭Scheduler

## 实践任务
1. 引入Quartz依赖
2. 创建第一个Quartz程序
3. 实现简单的定时任务
4. 测试任务执行

## 参考资料
- Quartz官方文档：https://www.quartz-scheduler.org/documentation/
- 《Quartz Job Scheduling Framework》
