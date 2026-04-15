# 04_Producer_消息生产

## 学习目标
- 掌握Producer配置
- 理解发送方式
- 掌握分区策略
- 理解序列化
- 掌握发送确认

## 关键要点
### 1. Producer配置
- bootstrap.servers
- key.serializer
- value.serializer
- acks
- retries

### 2. 发送方式
- 同步发送
- 异步发送
- Fire-and-forget

### 3. 分区策略
- 默认分区器
- 自定义分区器
- Key分区
- Round-robin

### 4. 序列化
- StringSerializer
- ByteArraySerializer
- 自定义序列化
- Avro/Protobuf

### 5. 发送确认
- acks=0
- acks=1
- acks=all

### 6. 其他配置
- batch.size
- linger.ms
- buffer.memory
- compression.type

## 实践任务
1. 配置Producer
2. 实现同步发送
3. 实现异步发送
4. 配置分区策略

## 参考资料
- Kafka Producer
