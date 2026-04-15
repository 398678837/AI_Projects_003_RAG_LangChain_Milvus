# 06_Event_Loop_事件循环

## 学习目标
- 理解EventLoop的概念
- 掌握EventLoopGroup
- 理解线程模型
- 掌握任务调度
- 理解事件处理

## 关键要点
### 1. EventLoop概述
- 事件循环
- 单线程执行
- 处理I/O事件
- 执行任务
- 线程安全

### 2. EventLoopGroup
- NioEventLoopGroup
- EpollEventLoopGroup
- 管理EventLoop
- next()方法
- 优雅关闭

### 3. 线程模型
- 主从Reactor
- Boss Group
- Worker Group
- 一个EventLoop多个Channel
- 一个Channel一个EventLoop

### 4. 任务执行
- execute()
- submit()
- schedule()
- scheduleAtFixedRate()
- scheduleWithFixedDelay()

### 5. 事件处理
- 选择器（Selector）
- 就绪事件
- 事件分发
- Handler调用

### 6. 线程安全
- EventLoop内串行
- EventLoop外异步
- 避免阻塞
- 使用异步任务

## 实践任务
1. 使用EventLoopGroup
2. 理解线程模型
3. 使用任务调度
4. 理解线程安全

## 参考资料
- Netty EventLoop
