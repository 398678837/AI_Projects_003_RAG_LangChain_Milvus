# 05_Consumer_消息消费

## 学习目标
- 掌握Consumer配置
- 理解消费组
- 掌握订阅主题
- 理解Offset管理
- 掌握重平衡

## 关键要点
### 1. Consumer配置
- bootstrap.servers
- key.deserializer
- value.deserializer
- group.id
- enable.auto.commit

### 2. 消费组
- 组概念
- 组内消费
- 组间独立
- 分区分配

### 3. 订阅主题
- subscribe
- assign
- 正则订阅

### 4. Offset管理
- 自动提交
- 手动提交
- 同步提交
- 异步提交

### 5. 重平衡
- 触发条件
- 重平衡监听器
- 分区分配策略

### 6. 其他配置
- auto.offset.reset
- max.poll.records
- fetch.min.bytes
- fetch.max.wait.ms

## 实践任务
1. 配置Consumer
2. 订阅主题
3. 管理Offset
4. 处理重平衡

## 参考资料
- Kafka Consumer
