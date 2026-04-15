# 08_ACK_确认机制

## 学习目标
- 理解确认机制
- 掌握手动确认
- 理解批量确认
- 掌握拒绝消息
- 理解死信队列

## 关键要点
### 1. 确认概述
- 为什么需要确认
- 自动确认
- 手动确认

### 2. 手动确认
- basicAck
- deliveryTag
- multiple

### 3. 批量确认
- multiple=true
- 批量确认优化

### 4. 拒绝消息
- basicNack
- basicReject
- requeue

### 5. 死信队列
- 死信交换机
- 死信路由
- 消息TTL
- 队列长度

## 实践任务
1. 使用手动确认
2. 使用批量确认
3. 拒绝消息
4. 配置死信队列

## 参考资料
- RabbitMQ Acknowledgements
