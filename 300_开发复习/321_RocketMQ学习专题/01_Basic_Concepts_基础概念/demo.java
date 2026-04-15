package com.example.rocketmq.basic;

import java.util.*;

public class BasicConceptsDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ基础概念示例 ===");

        try {
            rocketMQOverviewDemo();
            coreArchitectureDemo();
            messageModelDemo();
            coreConceptsDemo();
            messageTypesDemo();
            applicationScenariosDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void rocketMQOverviewDemo() {
        System.out.println("\n--- 1. RocketMQ概述 ---");

        System.out.println("RocketMQ是什么?");
        System.out.println("  - 阿里巴巴开源的消息中间件");
        System.out.println("  - 分布式消息队列系统");
        System.out.println("  - 低延迟、高可靠");
        System.out.println("  - 支持万亿级消息");
        System.out.println("  - 金融级可靠性");

        System.out.println("\nRocketMQ的特点:");
        System.out.println("  - 高吞吐量");
        System.out.println("  - 低延迟");
        System.out.println("  - 高可靠性");
        System.out.println("  - 支持事务消息");
        System.out.println("  - 支持顺序消息");
        System.out.println("  - 支持延时消息");
        System.out.println("  - 支持消息回溯");

        System.out.println("\nRocketMQ vs 其他MQ:");
        System.out.println("  - vs Kafka: 可靠性更高，支持事务消息");
        System.out.println("  - vs RabbitMQ: 吞吐量更高，延迟更低");
        System.out.println("  - vs ActiveMQ: 性能更好，功能更强大");
    }

    private static void coreArchitectureDemo() {
        System.out.println("\n--- 2. 核心架构 ---");

        System.out.println("RocketMQ核心组件:");
        System.out.println();

        System.out.println("1. NameServer（注册中心）:");
        System.out.println("   - 轻量级的注册中心");
        System.out.println("   - 管理Broker的路由信息");
        System.out.println("   - 无状态，可水平扩展");
        System.out.println("   - Producer和Consumer从中获取路由");
        System.out.println();

        System.out.println("2. Broker（消息存储）:");
        System.out.println("   - 负责消息的存储和投递");
        System.out.println("   - 消息持久化到磁盘");
        System.out.println("   - 支持主从复制");
        System.out.println("   - 支持多队列");
        System.out.println();

        System.out.println("3. Producer（消息生产者）:");
        System.out.println("   - 发送消息到Broker");
        System.out.println("   - 支持同步和异步发送");
        System.out.println("   - 支持事务消息");
        System.out.println("   - 支持顺序消息");
        System.out.println();

        System.out.println("4. Consumer（消息消费者）:");
        System.out.println("   - 从Broker拉取消息");
        System.out.println("   - 支持集群消费和广播消费");
        System.out.println("   - 支持并发消费和顺序消费");
        System.out.println("   - 支持消息重试");

        System.out.println("\n架构关系图:");
        System.out.println("  Producer ──┐");
        System.out.println("             ├──> NameServer");
        System.out.println("  Consumer ──┘        ↑");
        System.out.println("                       │");
        System.out.println("                    Broker");

        System.out.println("\n数据流向:");
        System.out.println("  Producer -> NameServer（获取路由） -> Broker（存储消息）");
        System.out.println("  Consumer -> NameServer（获取路由） -> Broker（拉取消息）");
    }

    private static void messageModelDemo() {
        System.out.println("\n--- 3. 消息模型 ---");

        System.out.println("发布/订阅模型:");
        System.out.println("  - Producer发布消息到Topic");
        System.out.println("  - Consumer订阅Topic接收消息");
        System.out.println("  - 一个Topic可以有多个Producer");
        System.out.println("  - 一个Topic可以有多个Consumer");

        System.out.println("\n集群消费（Clustering）:");
        System.out.println("  - 一个Consumer Group中的Consumer分摊消费");
        System.out.println("  - 一条消息只被一个Consumer消费");
        System.out.println("  - 适用于负载均衡");
        System.out.println();
        System.out.println("  Producer ──> Topic ──┬─> Consumer1");
        System.out.println("                      ├─> Consumer2");
        System.out.println("                      └─> Consumer3");
        System.out.println("  (同一条消息只给其中一个Consumer)");

        System.out.println("\n广播消费（Broadcasting）:");
        System.out.println("  - 一个Consumer Group中的每个Consumer都消费");
        System.out.println("  - 一条消息被所有Consumer消费");
        System.out.println("  - 适用于通知类场景");
        System.out.println();
        System.out.println("  Producer ──> Topic ──┬─> Consumer1");
        System.out.println("                      ├─> Consumer2");
        System.out.println("                      └─> Consumer3");
        System.out.println("  (同一条消息给所有Consumer)");
    }

    private static void coreConceptsDemo() {
        System.out.println("\n--- 4. 核心概念 ---");

        System.out.println("Topic（消息主题）:");
        System.out.println("  - 消息的分类");
        System.out.println("  - 一级消息类型");
        System.out.println("  - 例如: order_topic, user_topic");

        System.out.println("\nTag（消息标签）:");
        System.out.println("  - Topic下的细分");
        System.out.println("  - 二级消息类型");
        System.out.println("  - 例如: order_create, order_pay");
        System.out.println("  - 用于消息过滤");

        System.out.println("\nKey（消息键）:");
        System.out.println("  - 消息的业务唯一标识");
        System.out.println("  - 用于查询消息");
        System.out.println("  - 例如: order_id:12345");

        System.out.println("\nQueue（消息队列）:");
        System.out.println("  - Topic下的分区");
        System.out.println("  - 提高并行度");
        System.out.println("  - 一个Topic可以有多个Queue");
        System.out.println("  - 顺序消息的保证");

        System.out.println("\nOffset（消费进度）:");
        System.out.println("  - 记录消费位置");
        System.out.println("  - 支持消息回溯");
        System.out.println("  - 持久化存储");
        System.out.println("  - 可重置");

        System.out.println("\nTopic和Queue关系:");
        System.out.println("  Topic: order_topic");
        System.out.println("    Queue 0: [消息1, 消息4, ...]");
        System.out.println("    Queue 1: [消息2, 消息5, ...]");
        System.out.println("    Queue 2: [消息3, 消息6, ...]");
        System.out.println("    Queue 3: [消息7, 消息10, ...]");
    }

    private static void messageTypesDemo() {
        System.out.println("\n--- 5. 消息类型 ---");

        System.out.println("1. 普通消息:");
        System.out.println("   - 最常用的消息类型");
        System.out.println("   - 异步发送");
        System.out.println("   - 高吞吐量");
        System.out.println("   - 不保证顺序");

        System.out.println("\n2. 顺序消息:");
        System.out.println("   - 保证消息顺序");
        System.out.println("   - 同一队列有序");
        System.out.println("   - 全局有序或分区有序");
        System.out.println("   - 吞吐量稍低");

        System.out.println("\n3. 延时消息:");
        System.out.println("   - 延迟投递");
        System.out.println("   - 支持固定延时等级");
        System.out.println("   - 1s/5s/10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h");
        System.out.println("   - 适用于订单超时等场景");

        System.out.println("\n4. 事务消息:");
        System.out.println("   - 保证消息和本地事务一致");
        System.out.println("   - 两阶段提交");
        System.out.println("   - 回查机制");
        System.out.println("   - 适用于分布式事务");

        System.out.println("\n消息发送方式:");
        System.out.println("  - 同步发送: 等待响应");
        System.out.println("  - 异步发送: 回调通知");
        System.out.println("  - Oneway发送: 不等待响应");
    }

    private static void applicationScenariosDemo() {
        System.out.println("\n--- 6. 应用场景 ---");

        System.out.println("1. 异步解耦:");
        System.out.println("   - 订单系统 -> MQ -> 库存系统");
        System.out.println("   - 订单系统 -> MQ -> 积分系统");
        System.out.println("   - 订单系统 -> MQ -> 通知系统");
        System.out.println("   - 提高系统可用性");

        System.out.println("\n2. 流量削峰:");
        System.out.println("   - 秒杀活动 -> MQ -> 订单处理");
        System.out.println("   - 大促流量 -> MQ -> 业务系统");
        System.out.println("   - 保护后端系统");
        System.out.println("   - 平滑流量");

        System.out.println("\n3. 数据同步:");
        System.out.println("   - 系统A -> MQ -> 系统B");
        System.out.println("   - 数据库变更 -> MQ -> 缓存更新");
        System.out.println("   - 跨系统数据同步");
        System.out.println("   - 最终一致性");

        System.out.println("\n4. 事件驱动:");
        System.out.println("   - 用户注册 -> MQ -> 发送欢迎邮件");
        System.out.println("   - 订单完成 -> MQ -> 发送通知");
        System.out.println("   - 业务解耦");
        System.out.println("   - 扩展性好");

        System.out.println("\n5. 日志收集:");
        System.out.println("   - 应用日志 -> MQ -> 日志分析");
        System.out.println("   - 访问日志 -> MQ -> 监控系统");
        System.out.println("   - 统一收集");
        System.out.println("   - 实时分析");

        System.out.println("\n使用RocketMQ的知名项目:");
        System.out.println("  - 阿里巴巴内部众多系统");
        System.out.println("  - 淘宝");
        System.out.println("  - 天猫");
        System.out.println("  - 支付宝");
        System.out.println("  - 菜鸟");
    }
}
