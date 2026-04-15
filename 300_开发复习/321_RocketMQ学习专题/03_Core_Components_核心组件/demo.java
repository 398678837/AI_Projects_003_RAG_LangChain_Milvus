package com.example.rocketmq.core;

import java.util.*;

public class CoreComponentsDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ核心组件示例 ===");

        try {
            nameServerDemo();
            brokerDemo();
            producerDemo();
            consumerDemo();
            storageStructureDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void nameServerDemo() {
        System.out.println("\n--- 1. NameServer ---");
        System.out.println("NameServer的作用:");
        System.out.println("  - 注册中心");
        System.out.println("  - 管理Broker路由信息");
        System.out.println("  - 无状态，可水平扩展");
        System.out.println("  - 轻量级，高性能");
        System.out.println("  - 心跳检测");
        System.out.println();
        System.out.println("NameServer端口: 9876");
    }

    private static void brokerDemo() {
        System.out.println("\n--- 2. Broker ---");
        System.out.println("Broker的作用:");
        System.out.println("  - 消息存储");
        System.out.println("  - 消息投递");
        System.out.println("  - 主从复制");
        System.out.println("  - 高可用");
        System.out.println();
        System.out.println("Broker端口: 10911");
        System.out.println("Broker HA端口: 10912");
        System.out.println("FastListenPort: 10909");
    }

    private static void producerDemo() {
        System.out.println("\n--- 3. Producer ---");
        System.out.println("Producer的作用:");
        System.out.println("  - 发送消息");
        System.out.println("  - 负载均衡");
        System.out.println("  - 重试机制");
        System.out.println("  - 异步发送");
        System.out.println();
        System.out.println("发送方式:");
        System.out.println("  - 同步发送: send()");
        System.out.println("  - 异步发送: send(callback)");
        System.out.println("  - Oneway发送: sendOneway()");
    }

    private static void consumerDemo() {
        System.out.println("\n--- 4. Consumer ---");
        System.out.println("Consumer的作用:");
        System.out.println("  - 拉取消息");
        System.out.println("  - 消费消息");
        System.out.println("  - 提交消费进度");
        System.out.println("  - 重试机制");
        System.out.println();
        System.out.println("消费模式:");
        System.out.println("  - Push消费: DefaultMQPushConsumer");
        System.out.println("  - Pull消费: DefaultMQPullConsumer");
        System.out.println();
        System.out.println("消费方式:");
        System.out.println("  - 集群消费: MessageModel.CLUSTERING");
        System.out.println("  - 广播消费: MessageModel.BROADCASTING");
    }

    private static void storageStructureDemo() {
        System.out.println("\n--- 5. 存储结构 ---");
        System.out.println("CommitLog:");
        System.out.println("  - 所有消息的存储");
        System.out.println("  - 顺序写入");
        System.out.println("  - 固定大小文件");
        System.out.println();
        System.out.println("ConsumeQueue:");
        System.out.println("  - 消费队列");
        System.out.println("  - Topic + Queue");
        System.out.println("  - CommitLog索引");
        System.out.println();
        System.out.println("IndexFile:");
        System.out.println("  - 消息索引");
        System.out.println("  - Key查询");
        System.out.println("  - 提高查询速度");
    }
}
