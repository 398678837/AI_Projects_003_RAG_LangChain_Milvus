# 03_Core_Components_核心组件

## 学习目标
- 理解NameServer的作用
- 理解Broker的作用
- 掌握Producer和Consumer
- 理解存储结构
- 理解消息流程

## 关键要点
### 1. NameServer
- 注册中心
- 管理Broker路由
- 无状态，可扩展
- 轻量级
- 心跳检测

### 2. Broker
- 消息存储
- 主从架构
- CommitLog
- ConsumeQueue
- IndexFile

### 3. Producer
- 消息发送
- 负载均衡
- 重试机制
- 异步发送
- 事务消息

### 4. Consumer
- 消息拉取
- 消费模式
- 消费进度
- 重试机制
- 消息回溯

### 5. 存储结构
- CommitLog：消息存储
- ConsumeQueue：消费队列
- IndexFile：索引文件

### 6. 消息流程
- 发送流程
- 存储流程
- 消费流程
- 确认流程

## 实践任务
1. 理解NameServer
2. 理解Broker
3. 理解Producer和Consumer
4. 理解存储结构

## 参考资料
- RocketMQ Architecture
