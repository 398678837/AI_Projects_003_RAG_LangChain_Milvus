package com.example.netty.channel;

import io.netty.bootstrap.Bootstrap;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.buffer.ByteBuf;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;

public class ChannelDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty Channel示例 ===");

        try {
            channelOverviewDemo();
            channelLifecycleDemo();
            channelMethodsDemo();
            channelOptionDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void channelOverviewDemo() {
        System.out.println("\n--- 1. Channel概述 ---");
        System.out.println("Channel类型:");
        System.out.println("  - NioSocketChannel: 客户端TCP");
        System.out.println("  - NioServerSocketChannel: 服务端TCP");
        System.out.println("  - EpollSocketChannel: Linux高性能");
        System.out.println("  - KQueueSocketChannel: Mac高性能");
    }

    private static void channelLifecycleDemo() {
        System.out.println("\n--- 2. Channel生命周期 ---");
        System.out.println("Channel状态:");
        System.out.println("  1. Unregistered: 未注册");
        System.out.println("  2. Registered: 已注册");
        System.out.println("  3. Active: 活跃（连接建立）");
        System.out.println("  4. Inactive: 非活跃（连接断开）");
        System.out.println();
        System.out.println("状态检查方法:");
        System.out.println("  channel.isOpen()");
        System.out.println("  channel.isRegistered()");
        System.out.println("  channel.isActive()");
        System.out.println("  channel.isWritable()");
    }

    private static void channelMethodsDemo() {
        System.out.println("\n--- 3. Channel常用方法 ---");
        System.out.println("写数据:");
        System.out.println("  channel.write(msg); // 写入缓冲区");
        System.out.println("  channel.flush(); // 刷新到网络");
        System.out.println("  channel.writeAndFlush(msg); // 写入并刷新");
        System.out.println();
        System.out.println("其他方法:");
        System.out.println("  channel.read();");
        System.out.println("  channel.close();");
        System.out.println("  channel.localAddress();");
        System.out.println("  channel.remoteAddress();");
        System.out.println("  channel.pipeline();");
        System.out.println("  channel.eventLoop();");
        System.out.println("  channel.config();");
    }

    private static void channelOptionDemo() {
        System.out.println("\n--- 4. ChannelOption ---");
        System.out.println("常用ChannelOption:");
        System.out.println("  ChannelOption.SO_BACKLOG: 1024");
        System.out.println("  ChannelOption.SO_KEEPALIVE: true");
        System.out.println("  ChannelOption.SO_REUSEADDR: true");
        System.out.println("  ChannelOption.TCP_NODELAY: true");
        System.out.println("  ChannelOption.CONNECT_TIMEOUT_MILLIS: 5000");
    }
}
