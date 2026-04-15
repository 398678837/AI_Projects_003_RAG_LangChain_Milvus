# 01_Basic_Concepts_基础概念

## 学习目标
- 理解Netty的基本概念
- 掌握Netty的核心架构
- 理解Reactor模式
- 理解事件驱动模型
- 掌握Netty的应用场景

## 关键要点
### 1. Netty概述
- Java高性能网络应用框架
- 异步事件驱动
- 基于NIO
- 高性能、高可靠
- 易于使用

### 2. Reactor模式
- 单Reactor单线程
- 单Reactor多线程
- 主从Reactor多线程
- Netty使用主从Reactor多线程

### 3. 事件驱动模型
- 事件循环（EventLoop）
- 事件处理器（Handler）
- 异步非阻塞
- 回调机制

### 4. 核心概念
- Channel：通道
- EventLoop：事件循环
- ChannelHandler：通道处理器
- ChannelPipeline：通道管道
- ByteBuf：字节缓冲区
- Future/Promise：异步结果

### 5. Netty优势
- 高性能
- 低延迟
- 高吞吐量
- 代码优雅
- 丰富的协议支持
- 活跃的社区

### 6. 应用场景
-  RPC框架
- 游戏服务器
- 即时通讯
- 推送系统
- 高性能代理
- 分布式系统

## 实践任务
1. 理解Netty核心概念
2. 理解Reactor模式
3. 理解事件驱动模型
4. 了解Netty应用场景

## 参考资料
- Netty官方文档：https://netty.io/wiki/
- 《Netty权威指南》
