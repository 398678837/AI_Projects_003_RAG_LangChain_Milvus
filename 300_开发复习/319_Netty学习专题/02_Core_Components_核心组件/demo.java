package com.example.netty.core;

import io.netty.bootstrap.Bootstrap;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;

import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class CoreComponentsDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty核心组件示例 ===");

        try {
            bootstrapDemo();
            serverBootstrapDemo();
            eventLoopGroupDemo();
            channelFutureDemo();
            byteBufDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void bootstrapDemo() {
        System.out.println("\n--- 1. Bootstrap（客户端启动类） ---");

        System.out.println("Bootstrap的作用:");
        System.out.println("  - 配置Netty客户端");
        System.out.println("  - 设置EventLoopGroup");
        System.out.println("  - 设置Channel类型");
        System.out.println("  - 设置ChannelHandler");
        System.out.println("  - 连接远程服务器");

        System.out.println("\nBootstrap示例代码:");
        System.out.println("EventLoopGroup group = new NioEventLoopGroup();");
        System.out.println("try {");
        System.out.println("    Bootstrap bootstrap = new Bootstrap();");
        System.out.println("    bootstrap.group(group)");
        System.out.println("             .channel(NioSocketChannel.class)");
        System.out.println("             .handler(new ChannelInitializer<SocketChannel>() {");
        System.out.println("                 @Override");
        System.out.println("                 protected void initChannel(SocketChannel ch) {");
        System.out.println("                     ch.pipeline().addLast(new SimpleChannelInboundHandler<ByteBuf>() {");
        System.out.println("                         @Override");
        System.out.println("                         protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) {");
        System.out.println("                             System.out.println(msg.toString(StandardCharsets.UTF_8));");
        System.out.println("                         }");
        System.out.println("                     });");
        System.out.println("                 }");
        System.out.println("             });");
        System.out.println("    ChannelFuture future = bootstrap.connect(\"localhost\", 8080).sync();");
        System.out.println("    future.channel().closeFuture().sync();");
        System.out.println("} finally {");
        System.out.println("    group.shutdownGracefully();");
        System.out.println("}");

        System.out.println("\nBootstrap常用方法:");
        System.out.println("  - group(): 设置EventLoopGroup");
        System.out.println("  - channel(): 设置Channel类型");
        System.out.println("  - handler(): 设置ChannelHandler");
        System.out.println("  - option(): 设置ChannelOption");
        System.out.println("  - attr(): 设置Attribute");
        System.out.println("  - connect(): 连接服务器");
        System.out.println("  - remoteAddress(): 设置远程地址");
    }

    private static void serverBootstrapDemo() {
        System.out.println("\n--- 2. ServerBootstrap（服务端启动类） ---");

        System.out.println("ServerBootstrap的作用:");
        System.out.println("  - 配置Netty服务端");
        System.out.println("  - 设置BossGroup和WorkerGroup");
        System.out.println("  - 设置父通道和子通道");
        System.out.println("  - 设置两个ChannelHandler");
        System.out.println("  - 绑定端口监听");

        System.out.println("\nServerBootstrap示例代码:");
        System.out.println("EventLoopGroup bossGroup = new NioEventLoopGroup();");
        System.out.println("EventLoopGroup workerGroup = new NioEventLoopGroup();");
        System.out.println("try {");
        System.out.println("    ServerBootstrap bootstrap = new ServerBootstrap();");
        System.out.println("    bootstrap.group(bossGroup, workerGroup)");
        System.out.println("             .channel(NioServerSocketChannel.class)");
        System.out.println("             .option(ChannelOption.SO_BACKLOG, 1024)");
        System.out.println("             .childOption(ChannelOption.SO_KEEPALIVE, true)");
        System.out.println("             .handler(new LoggingHandler(LogLevel.INFO))");
        System.out.println("             .childHandler(new ChannelInitializer<SocketChannel>() {");
        System.out.println("                 @Override");
        System.out.println("                 protected void initChannel(SocketChannel ch) {");
        System.out.println("                     ch.pipeline().addLast(new SimpleChannelInboundHandler<ByteBuf>() {");
        System.out.println("                         @Override");
        System.out.println("                         protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) {");
        System.out.println("                             System.out.println(msg.toString(StandardCharsets.UTF_8));");
        System.out.println("                             ctx.writeAndFlush(Unpooled.copiedBuffer(\"OK\", StandardCharsets.UTF_8));");
        System.out.println("                         }");
        System.out.println("                     });");
        System.out.println("                 }");
        System.out.println("             });");
        System.out.println("    ChannelFuture future = bootstrap.bind(8080).sync();");
        System.out.println("    future.channel().closeFuture().sync();");
        System.out.println("} finally {");
        System.out.println("    bossGroup.shutdownGracefully();");
        System.out.println("    workerGroup.shutdownGracefully();");
        System.out.println("}");

        System.out.println("\nServerBootstrap vs Bootstrap:");
        System.out.println("  ServerBootstrap:");
        System.out.println("    - 两个EventLoopGroup（boss和worker）");
        System.out.println("    - 两个ChannelHandler（handler和childHandler）");
        System.out.println("    - bind()方法绑定端口");
        System.out.println("    - option()设置父通道参数");
        System.out.println("    - childOption()设置子通道参数");
        System.out.println();
        System.out.println("  Bootstrap:");
        System.out.println("    - 一个EventLoopGroup");
        System.out.println("    - 一个ChannelHandler");
        System.out.println("    - connect()方法连接服务器");
        System.out.println("    - option()设置通道参数");
    }

    private static void eventLoopGroupDemo() {
        System.out.println("\n--- 3. EventLoopGroup ---");

        System.out.println("EventLoopGroup的实现类:");
        System.out.println("  - NioEventLoopGroup: 基于Java NIO");
        System.out.println("  - EpollEventLoopGroup: Linux专用，性能更好");
        System.out.println("  - KQueueEventLoopGroup: Mac OS专用");
        System.out.println("  - OioEventLoopGroup: 旧IO（已废弃）");

        System.out.println("\nEventLoopGroup构造参数:");
        System.out.println("  new NioEventLoopGroup(): 默认线程数=CPU核心数*2");
        System.out.println("  new NioEventLoopGroup(4): 指定线程数为4");
        System.out.println("  new NioEventLoopGroup(4, threadFactory): 自定义线程工厂");

        System.out.println("\nEventLoopGroup常用方法:");
        System.out.println("  - next(): 获取下一个EventLoop");
        System.out.println("  - shutdownGracefully(): 优雅关闭");
        System.out.println("  - isShutdown(): 是否已关闭");
        System.out.println("  - isTerminated(): 是否已终止");
        System.out.println("  - terminationFuture(): 终止异步结果");

        System.out.println("\n线程数建议:");
        System.out.println("  BossGroup: 通常1-2个线程");
        System.out.println("  WorkerGroup: CPU核心数 * 2");
        System.out.println("  根据实际业务调整");
    }

    private static void channelFutureDemo() {
        System.out.println("\n--- 4. ChannelFuture ---");

        System.out.println("ChannelFuture的作用:");
        System.out.println("  - 表示异步操作的结果");
        System.out.println("  - 支持回调机制");
        System.out.println("  - 支持同步等待");
        System.out.println("  - 获取操作状态");

        System.out.println("\nChannelFuture示例:");
        System.out.println("// 方式1: 使用监听器");
        System.out.println("ChannelFuture future = bootstrap.connect(\"localhost\", 8080);");
        System.out.println("future.addListener(new ChannelFutureListener() {");
        System.out.println("    @Override");
        System.out.println("    public void operationComplete(ChannelFuture f) {");
        System.out.println("        if (f.isSuccess()) {");
        System.out.println("            System.out.println(\"连接成功\");");
        System.out.println("        } else {");
        System.out.println("            System.out.println(\"连接失败: \" + f.cause());");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("});");
        System.out.println();
        System.out.println("// 方式2: 同步等待");
        System.out.println("ChannelFuture future = bootstrap.connect(\"localhost\", 8080).sync();");
        System.out.println("if (future.isSuccess()) {");
        System.out.println("    System.out.println(\"连接成功\");");
        System.out.println("}");

        System.out.println("\nChannelFuture常用方法:");
        System.out.println("  - addListener(): 添加监听器");
        System.out.println("  - removeListener(): 移除监听器");
        System.out.println("  - sync(): 同步等待完成（阻塞）");
        System.out.println("  - await(): 等待完成（不抛异常）");
        System.out.println("  - isSuccess(): 是否成功");
        System.out.println("  - isDone(): 是否已完成");
        System.out.println("  - isCancelled(): 是否已取消");
        System.out.println("  - cause(): 获取失败原因");
        System.out.println("  - channel(): 获取Channel");
    }

    private static void byteBufDemo() {
        System.out.println("\n--- 5. ByteBuf ---");

        System.out.println("ByteBuf vs ByteBuffer:");
        System.out.println("  ByteBuffer (Java NIO):");
        System.out.println("    - 一个索引（position）");
        System.out.println("    - 读写需要flip()");
        System.out.println("    - API不够友好");
        System.out.println();
        System.out.println("  ByteBuf (Netty):");
        System.out.println("    - 两个索引（readerIndex, writerIndex）");
        System.out.println("    - 读写不需要flip()");
        System.out.println("    - API更丰富");
        System.out.println("    - 支持池化");
        System.out.println("    - 零拷贝");

        System.out.println("\nByteBuf分类:");
        System.out.println("  按内存类型:");
        System.out.println("    - 堆内存（Heap Buffer）: JVM堆内");
        System.out.println("    - 直接内存（Direct Buffer）: 堆外内存");
        System.out.println();
        System.out.println("  按是否池化:");
        System.out.println("    - 池化（Pooled）: 从池中获取，性能好");
        System.out.println("    - 非池化（Unpooled）: 每次创建新的");

        System.out.println("\n创建ByteBuf:");
        System.out.println("// 堆内存，非池化");
        System.out.println("ByteBuf heapBuf = Unpooled.buffer(10);");
        System.out.println();
        System.out.println("// 直接内存，非池化");
        System.out.println("ByteBuf directBuf = Unpooled.directBuffer(10);");
        System.out.println();
        System.out.println("// 池化（推荐）");
        System.out.println("ByteBuf pooledBuf = PooledByteBufAllocator.DEFAULT.buffer(10);");

        System.out.println("\nByteBuf常用方法:");
        System.out.println("  写操作:");
        System.out.println("    - writeByte(): 写入字节");
        System.out.println("    - writeInt(): 写入int");
        System.out.println("    - writeBytes(): 写入字节数组");
        System.out.println("    - writeCharSequence(): 写入字符串");
        System.out.println();
        System.out.println("  读操作:");
        System.out.println("    - readByte(): 读取字节");
        System.out.println("    - readInt(): 读取int");
        System.out.println("    - readBytes(): 读取字节数组");
        System.out.println("    - toString(): 转换为字符串");
        System.out.println();
        System.out.println("  索引操作:");
        System.out.println("    - readerIndex(): 获取读索引");
        System.out.println("    - writerIndex(): 获取写索引");
        System.out.println("    - readerIndex(int): 设置读索引");
        System.out.println("    - writerIndex(int): 设置写索引");
        System.out.println("    - markReaderIndex(): 标记读索引");
        System.out.println("    - resetReaderIndex(): 重置读索引");
        System.out.println();
        System.out.println("  其他:");
        System.out.println("    - capacity(): 容量");
        System.out.println("    - readableBytes(): 可读字节数");
        System.out.println("    - writableBytes(): 可写字节数");
        System.out.println("    - release(): 释放（引用计数）");
        System.out.println("    - retain(): 增加引用计数");
        System.out.println("    - refCnt(): 引用计数");

        System.out.println("\nByteBuf示例:");
        System.out.println("ByteBuf buf = Unpooled.buffer(10);");
        System.out.println("buf.writeBytes(\"Hello\".getBytes(StandardCharsets.UTF_8));");
        System.out.println("System.out.println(\"writerIndex: \" + buf.writerIndex()); // 5");
        System.out.println("System.out.println(\"readerIndex: \" + buf.readerIndex()); // 0");
        System.out.println("System.out.println(\"readable: \" + buf.readableBytes()); // 5");
        System.out.println();
        System.out.println("byte[] data = new byte[buf.readableBytes()];");
        System.out.println("buf.readBytes(data);");
        System.out.println("System.out.println(new String(data, StandardCharsets.UTF_8)); // Hello");
        System.out.println("System.out.println(\"readerIndex: \" + buf.readerIndex()); // 5");
        System.out.println();
        System.out.println("buf.release(); // 释放资源");
    }
}
