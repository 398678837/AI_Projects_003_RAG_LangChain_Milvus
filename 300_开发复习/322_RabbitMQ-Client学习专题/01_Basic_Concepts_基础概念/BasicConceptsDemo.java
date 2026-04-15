package com.example.rabbitmq.basic;

import java.util.*;

public class BasicConceptsDemo {

    public static void main(String[] args) {
        System.out.println("=== RabbitMQ基础概念示例 ===");

        try {
            rabbitMQOverviewDemo();
            coreArchitectureDemo();
            amqpProtocolDemo();
            messageModelsDemo();
            coreConceptsDemo();
            applicationScenariosDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void rabbitMQOverviewDemo() {
        System.out.println("\n--- 1. RabbitMQ概述 ---");

        System.out.println("RabbitMQ是什么?");
        System.out.println("  - 开源的消息中间件");
        System.out.println("  - 基于AMQP协议实现");
        System.out.println("  - 使用Erlang语言开发");
        System.out.println("  - 高可靠性");
        System.out.println("  - 灵活的路由");

        System.out.println("\nRabbitMQ的特点:");
        System.out.println("  - 高可靠性");
        System.out.println("  - 灵活的路由");
        System.out.println("  - 消息集群");
        System.out.println("  - 高可用性");
        System.out.println("  - 多种协议");
        System.out.println("  - 管理界面");
        System.out.println("  - 跟踪");
        System.out.println("  - 插件系统");
    }

    private static void coreArchitectureDemo() {
        System.out.println("\n--- 2. 核心架构 ---");
        System.out.println("核心组件:");
        System.out.println("  - Producer: 生产者");
        System.out.println("  - Consumer: 消费者");
        System.out.println("  - Broker: 消息代理");
        System.out.println("  - Exchange: 交换机");
        System.out.println("  - Queue: 队列");
        System.out.println("  - Binding: 绑定");
        System.out.println("  - Virtual Host: 虚拟主机");
    }

    private static void amqpProtocolDemo() {
        System.out.println("\n--- 3. AMQP协议 ---");
        System.out.println("AMQP: Advanced Message Queuing Protocol");
        System.out.println("  - 高级消息队列协议");
        System.out.println("  - 开放的二进制协议");
        System.out.println("  - 用于消息中间件");
    }

    private static void messageModelsDemo() {
        System.out.println("\n--- 4. 消息模型 ---");
        System.out.println("1. 简单队列");
        System.out.println("2. 工作队列");
        System.out.println("3. 发布订阅");
        System.out.println("4. 路由");
        System.out.println("5. 主题");
        System.out.println("6. RPC");
    }

    private static void coreConceptsDemo() {
        System.out.println("\n--- 5. 核心概念 ---");
        System.out.println("Exchange类型:");
        System.out.println("  - Direct: 精确匹配");
        System.out.println("  - Topic: 通配符");
        System.out.println("  - Fanout: 广播");
        System.out.println("  - Headers: Header匹配");
    }

    private static void applicationScenariosDemo() {
        System.out.println("\n--- 6. 应用场景 ---");
        System.out.println("1. 异步处理");
        System.out.println("2. 流量削峰");
        System.out.println("3. 日志收集");
        System.out.println("4. 系统解耦");
        System.out.println("5. 分布式事务");
    }
}
