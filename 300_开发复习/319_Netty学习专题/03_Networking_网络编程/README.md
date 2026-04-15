# 03_Networking_网络编程

## 学习目标
- 掌握TCP服务端和客户端
- 理解编解码器的使用
- 掌握粘包拆包问题
- 理解心跳机制
- 掌握断线重连

## 关键要点
### 1. TCP服务端
- ServerBootstrap
- NioServerSocketChannel
- 绑定端口
- 接受连接
- ChannelInitializer

### 2. TCP客户端
- Bootstrap
- NioSocketChannel
- 连接服务端
- 发送和接收数据
- ChannelInitializer

### 3. 编解码器
- ByteToMessageDecoder
- MessageToByteEncoder
- StringDecoder
- StringEncoder
- LineBasedFrameDecoder
- DelimiterBasedFrameDecoder
- FixedLengthFrameDecoder

### 4. 粘包拆包
- 问题原因
- 解决方案
- 固定长度
- 分隔符
- 长度字段

### 5. 心跳机制
- IdleStateHandler
- 读空闲
- 写空闲
- 读写空闲
- 心跳包设计

### 6. 断线重连
- ChannelInactive
- 定时重连
- 指数退避
- 最大重试次数

## 实践任务
1. 实现TCP服务端和客户端
2. 解决粘包拆包问题
3. 实现心跳机制
4. 实现断线重连

## 参考资料
- Netty User Guide
