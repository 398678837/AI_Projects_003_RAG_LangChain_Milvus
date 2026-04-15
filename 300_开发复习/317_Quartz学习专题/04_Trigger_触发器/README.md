# 04_Trigger_触发器

## 学习目标
- 理解Trigger的作用
- 掌握SimpleTrigger的使用
- 掌握CronTrigger的使用
- 理解其他Trigger类型
- 掌握Trigger的优先级和Misfire策略

## 关键要点
### 1. Trigger概述
- 定义任务执行时间
- 多种Trigger类型
- 可以被暂停和恢复
- 支持优先级
- 支持Misfire策略

### 2. SimpleTrigger
- 简单触发器
- 固定间隔执行
- 指定执行次数
- startAt/endAt
- repeatInterval/repeatCount

### 3. CronTrigger
- Cron表达式触发器
- 灵活的时间表达式
- 复杂的调度需求
- Cron表达式语法
- 常用Cron表达式示例

### 4. CalendarIntervalTrigger
- 日历间隔触发器
- 基于日历的间隔
- 支持年、月、周、日、小时、分钟、秒
- 自动处理夏令时

### 5. DailyTimeIntervalTrigger
- 每日时间间隔触发器
- 每天特定时间段执行
- 指定开始和结束时间
- 指定执行间隔
- 指定星期几

### 6. Trigger优先级
- 多个Trigger同时触发时
- 优先级高的先执行
- 默认优先级5
- 范围1-10

### 7. Misfire策略
- 错过触发时间的处理
- SimpleTrigger的Misfire策略
- CronTrigger的Misfire策略
- 选择合适的Misfire策略

## 实践任务
1. 使用SimpleTrigger
2. 使用CronTrigger
3. 使用其他Trigger类型
4. 设置Trigger优先级
5. 配置Misfire策略

## 参考资料
- Quartz Triggers
