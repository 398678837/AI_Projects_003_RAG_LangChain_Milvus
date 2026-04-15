# 09_Performance_Optimization_性能优化

## 学习目标
- 理解Netty性能优化
- 掌握内存管理
- 理解池化技术
- 掌握调优参数
- 理解性能监控

## 关键要点
### 1. 内存管理
- PooledByteBufAllocator
- UnpooledByteBufAllocator
- 堆内存 vs 直接内存
- 引用计数
- 及时释放

### 2. 池化技术
- ByteBuf池
- EventLoop线程数
- ChannelPool
- 对象池
- 减少GC

### 3. 调优参数
- SO_BACKLOG
- TCP_NODELAY
- SO_SNDBUF/SO_RCVBUF
- WRITE_BUFFER_LOW_WATERMARK
- WRITE_BUFFER_HIGH_WATERMARK

### 4. EventLoop调优
- 线程数
- Boss Group
- Worker Group
- 任务调度
- 避免阻塞

### 5. Handler优化
- 减少Handler数量
- 合理使用Sharable
- 避免频繁创建对象
- 使用ThreadLocal

### 6. 性能监控
- JVM监控
- Netty指标
- GC监控
- 内存监控
- 线程监控

## 实践任务
1. 使用池化ByteBuf
2. 调优EventLoop
3. 优化Handler
4. 监控性能

## 参考资料
- Netty Performance
