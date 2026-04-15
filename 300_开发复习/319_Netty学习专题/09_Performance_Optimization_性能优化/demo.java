package com.example.netty.performance;

import io.netty.buffer.ByteBufAllocator;
import io.netty.buffer.PooledByteBufAllocator;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;

public class PerformanceOptimizationDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty性能优化示例 ===");

        try {
            memoryManagementDemo();
            poolingDemo();
            tuningParametersDemo();
            eventLoopTuningDemo();
            handlerOptimizationDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void memoryManagementDemo() {
        System.out.println("\n--- 1. 内存管理 ---");
        System.out.println("ByteBufAllocator:");
        System.out.println("  PooledByteBufAllocator.DEFAULT (推荐)");
        System.out.println("  UnpooledByteBufAllocator.DEFAULT");
        System.out.println();
        System.out.println("内存类型:");
        System.out.println("  堆内存: 分配快，受GC影响");
        System.out.println("  直接内存: 零拷贝，不受GC影响");
        System.out.println();
        System.out.println("引用计数:");
        System.out.println("  release(): 释放");
        System.out.println("  retain(): 增加引用");
        System.out.println("  refCnt(): 引用计数");
    }

    private static void poolingDemo() {
        System.out.println("\n--- 2. 池化技术 ---");
        System.out.println("ByteBuf池:");
        System.out.println("  PooledByteBufAllocator.DEFAULT.buffer(1024)");
        System.out.println();
        System.out.println("EventLoop线程池:");
        System.out.println("  Boss: 1-2线程");
        System.out.println("  Worker: CPU核心数 * 2");
        System.out.println();
        System.out.println("对象池:");
        System.out.println("  复用对象，减少GC");
    }

    private static void tuningParametersDemo() {
        System.out.println("\n--- 3. 调优参数 ---");
        System.out.println("ChannelOption:");
        System.out.println("  SO_BACKLOG: 1024");
        System.out.println("  TCP_NODELAY: true");
        System.out.println("  SO_SNDBUF: 65535");
        System.out.println("  SO_RCVBUF: 65535");
        System.out.println("  WRITE_BUFFER_LOW_WATERMARK: 32768");
        System.out.println("  WRITE_BUFFER_HIGH_WATERMARK: 65536");
    }

    private static void eventLoopTuningDemo() {
        System.out.println("\n--- 4. EventLoop调优 ---");
        System.out.println("EventLoopGroup bossGroup = new NioEventLoopGroup(1);");
        System.out.println("EventLoopGroup workerGroup = new NioEventLoopGroup(Runtime.getRuntime().availableProcessors() * 2);");
        System.out.println();
        System.out.println("注意:");
        System.out.println("  - 不要在EventLoop中执行阻塞操作");
        System.out.println("  - 阻塞操作使用其他线程池");
    }

    private static void handlerOptimizationDemo() {
        System.out.println("\n--- 5. Handler优化 ---");
        System.out.println("@ChannelHandler.Sharable");
        System.out.println("public class MyHandler extends ChannelInboundHandlerAdapter {");
        System.out.println("    // 可以被多个Channel共享");
        System.out.println("}");
        System.out.println();
        System.out.println("优化建议:");
        System.out.println("  - 减少Handler数量");
        System.out.println("  - 使用@Sharable");
        System.out.println("  - 避免在Handler中创建对象");
        System.out.println("  - 使用ThreadLocal");
    }
}
