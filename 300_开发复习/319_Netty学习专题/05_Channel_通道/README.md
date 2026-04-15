# 05_Channel_通道

## 学习目标
- 理解Channel的概念
- 掌握Channel的生命周期
- 理解Channel的状态
- 掌握Channel常用方法
- 理解ChannelOption

## 关键要点
### 1. Channel概述
- 网络连接的抽象
- NioSocketChannel
- NioServerSocketChannel
- EpollSocketChannel
- KQueueSocketChannel

### 2. Channel生命周期
- Unregistered
- Registered
- Active
- Inactive

### 3. Channel状态
- isOpen()
- isRegistered()
- isActive()
- isWritable()

### 4. Channel常用方法
- write()
- writeAndFlush()
- read()
- close()
- flush()
- localAddress()
- remoteAddress()
- pipeline()
- eventLoop()
- config()

### 5. ChannelFuture
- 异步操作
- addListener()
- sync()
- await()

### 6. ChannelOption
- SO_BACKLOG
- SO_KEEPALIVE
- SO_REUSEADDR
- SO_SNDBUF/SO_RCVBUF
- TCP_NODELAY
- CONNECT_TIMEOUT_MILLIS

### 7. ChannelConfig
- 获取和设置配置
- setOption()
- getOption()

## 实践任务
1. 使用Channel操作
2. 理解Channel生命周期
3. 使用ChannelOption
4. 使用ChannelFuture

## 参考资料
- Netty Channel
