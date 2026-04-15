package com.example.netty.eventloop;

import io.netty.channel.EventLoop;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;

import java.util.concurrent.TimeUnit;

public class EventLoopDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty EventLoop示例 ===");

        try {
            eventLoopGroupDemo();
            threadModelDemo();
            taskSchedulingDemo();
            threadSafetyDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void eventLoopGroupDemo() {
        System.out.println("\n--- 1. EventLoopGroup ---");
        System.out.println("EventLoopGroup实现:");
        System.out.println("  - NioEventLoopGroup");
        System.out.println("  - EpollEventLoopGroup");
        System.out.println("  - KQueueEventLoopGroup");
        System.out.println();
        System.out.println("创建EventLoopGroup:");
        System.out.println("  EventLoopGroup group = new NioEventLoopGroup();");
        System.out.println("  EventLoopGroup group = new NioEventLoopGroup(4);");
        System.out.println();
        System.out.println("获取EventLoop:");
        System.out.println("  EventLoop loop = group.next();");
        System.out.println();
        System.out.println("优雅关闭:");
        System.out.println("  group.shutdownGracefully();");
    }

    private static void threadModelDemo() {
        System.out.println("\n--- 2. 线程模型 ---");
        System.out.println("主从Reactor多线程模型:");
        System.out.println("  Boss Group: 接收连接");
        System.out.println("  Worker Group: 处理I/O");
        System.out.println();
        System.out.println("规则:");
        System.out.println("  - 一个Channel绑定一个EventLoop");
        System.out.println("  - 一个EventLoop可以处理多个Channel");
        System.out.println("  - Channel的所有操作在EventLoop中串行执行");
    }

    private static void taskSchedulingDemo() {
        System.out.println("\n--- 3. 任务调度 ---");
        System.out.println("EventLoopGroup group = new NioEventLoopGroup();");
        System.out.println("EventLoop loop = group.next();");
        System.out.println();
        System.out.println("执行任务:");
        System.out.println("  loop.execute(() -> System.out.println(\"执行任务\"));");
        System.out.println();
        System.out.println("延迟执行:");
        System.out.println("  loop.schedule(() -> System.out.println(\"延迟1秒\"), 1, TimeUnit.SECONDS);");
        System.out.println();
        System.out.println("固定速率:");
        System.out.println("  loop.scheduleAtFixedRate(() -> {}, 0, 1, TimeUnit.SECONDS);");
        System.out.println();
        System.out.println("固定延迟:");
        System.out.println("  loop.scheduleWithFixedDelay(() -> {}, 0, 1, TimeUnit.SECONDS);");
    }

    private static void threadSafetyDemo() {
        System.out.println("\n--- 4. 线程安全 ---");
        System.out.println("线程安全原则:");
        System.out.println("  - EventLoop内串行执行");
        System.out.println("  - 不需要synchronized");
        System.out.println("  - 避免在EventLoop中执行阻塞操作");
        System.out.println("  - 阻塞操作放到其他线程池");
    }
}
