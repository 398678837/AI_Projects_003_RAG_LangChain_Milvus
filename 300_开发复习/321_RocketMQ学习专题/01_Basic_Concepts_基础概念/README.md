# 01_Basic_Concepts_基础概念

## 学习目标
- 理解RocketMQ的基本概念
- 掌握RocketMQ的核心架构
- 理解消息模型
- 理解消息类型
- 掌握RocketMQ的应用场景

## 关键要点
### 1. RocketMQ概述
- 阿里巴巴开源的消息中间件
- 分布式消息队列
- 低延迟、高可靠
- 万亿级消息
- 金融级可靠性

### 2. 核心架构
- NameServer：注册中心
- Broker：消息存储
- Producer：消息生产者
- Consumer：消息消费者
- Topic：消息主题
- Queue：消息队列

### 3. 消息模型
- 发布/订阅模型
- 点对点模型
- 集群消费
- 广播消费

### 4. 核心概念
- Topic：消息主题
- Tag：消息标签
- Key：消息键
- Queue：消息队列
- Offset：消费进度

### 5. 消息类型
- 普通消息
- 顺序消息
- 延时消息
- 事务消息

### 6. 消费模式
- 集群消费（Clustering）
- 广播消费（Broadcasting）

### 7. 应用场景
- 异步解耦
- 流量削峰
- 数据同步
- 事件驱动
- 日志收集

## 实践任务
1. 理解RocketMQ核心概念
2. 理解消息模型
3. 理解消息类型
4. 了解应用场景

## 参考资料
- RocketMQ官方文档：https://rocketmq.apache.org/zh/
- 《RocketMQ实战》
