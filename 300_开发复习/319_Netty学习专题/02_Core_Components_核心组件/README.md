# 02_Core_Components_核心组件

## 学习目标
- 掌握Bootstrap和ServerBootstrap
- 理解EventLoopGroup
- 掌握Channel
- 理解ChannelFuture
- 掌握ByteBuf

## 关键要点
### 1. Bootstrap
- 客户端启动类
- 配置客户端参数
- 连接远程服务器
- 设置EventLoopGroup
- 设置Channel类型
- 设置Handler

### 2. ServerBootstrap
- 服务端启动类
- 配置服务端参数
- 绑定端口
- BossGroup和WorkerGroup
- 父通道和子通道
- 两个ChannelInitializer

### 3. EventLoopGroup
- NioEventLoopGroup
- EpollEventLoopGroup
- KQueueEventLoopGroup
- 线程数量
- 优雅关闭

### 4. Channel
- NioServerSocketChannel
- NioSocketChannel
- EpollServerSocketChannel
- EpollSocketChannel
- Channel生命周期
- Channel状态

### 5. ChannelFuture
- 异步操作结果
- addListener
- sync()
- await()
- isSuccess()
- cause()

### 6. ByteBuf
- 池化 vs 非池化
- 堆内存 vs 直接内存
- 读写索引
- 常用方法
- 引用计数
- 释放资源

## 实践任务
1. 使用Bootstrap和ServerBootstrap
2. 理解EventLoopGroup
3. 使用Channel和ChannelFuture
4. 使用ByteBuf

## 参考资料
- Netty Core Components
