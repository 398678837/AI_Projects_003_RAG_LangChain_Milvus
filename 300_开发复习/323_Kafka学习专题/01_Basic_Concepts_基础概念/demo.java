package com.example.kafka.basic;

import java.util.*;

public class BasicConceptsDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka基础概念示例 ===");

        try {
            kafkaOverviewDemo();
            coreArchitectureDemo();
            messageModelDemo();
            coreConceptsDemo();
            featuresDemo();
            applicationScenariosDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void kafkaOverviewDemo() {
        System.out.println("\n--- 1. Kafka概述 ---");

        System.out.println("Kafka是什么?");
        System.out.println("  - Apache Kafka");
        System.out.println("  - 分布式流处理平台");
        System.out.println("  - 高吞吐量");
        System.out.println("  - 低延迟");
        System.out.println("  - 持久化存储");
        System.out.println("  - 水平扩展");

        System.out.println("\nKafka的特点:");
        System.out.println("  - 高吞吐");
        System.out.println("  - 低延迟");
        System.out.println("  - 持久化");
        System.out.println("  - 分布式");
        System.out.println("  - 容错");
        System.out.println("  - 多副本");
        System.out.println("  - 可扩展");
    }

    private static void coreArchitectureDemo() {
        System.out.println("\n--- 2. 核心架构 ---");

        System.out.println("Kafka核心组件:");
        System.out.println();

        System.out.println("1. Producer（生产者）:");
        System.out.println("   - 发布消息到Kafka");
        System.out.println("   - 发送到Topic");
        System.out.println();

        System.out.println("2. Consumer（消费者）:");
        System.out.println("   - 从Kafka拉取消息");
        System.out.println("   - 订阅Topic");
        System.out.println("   - 消费组");
        System.out.println();

        System.out.println("3. Broker（代理）:");
        System.out.println("   - Kafka服务器");
        System.out.println("   - 存储消息");
        System.out.println("   - 处理请求");
        System.out.println();

        System.out.println("4. Topic（主题）:");
        System.out.println("   - 消息分类");
        System.out.println("   - 分区存储");
        System.out.println();

        System.out.println("5. Partition（分区）:");
        System.out.println("   - Topic的分区");
        System.out.println("   - 并行处理");
        System.out.println();

        System.out.println("6. Replica（副本）:");
        System.out.println("   - 数据备份");
        System.out.println("   - 高可用");
        System.out.println();

        System.out.println("7. ZooKeeper/KRaft:");
        System.out.println("   - 集群协调");
        System.out.println("   - 元数据管理");
    }

    private static void messageModelDemo() {
        System.out.println("\n--- 3. 消息模型 ---");

        System.out.println("发布订阅模型:");
        System.out.println("  - Producer发布到Topic");
        System.out.println("  - Consumer订阅Topic");
        System.out.println("  - 多个Consumer可订阅同一Topic");

        System.out.println("\n分区模型:");
        System.out.println("  - Topic分为多个Partition");
        System.out.println("  - 每个Partition有序");
        System.out.println("  - 提高并行度");

        System.out.println("\n消费组:");
        System.out.println("  - 多个Consumer组成消费组");
        System.out.println("  - 组内消费者分摊消费");
        System.out.println("  - 组间独立消费");

        System.out.println("\nOffset:");
        System.out.println("  - 消费位置");
        System.out.println("  - 持久化存储");
        System.out.println("  - 支持回溯");
    }

    private static void coreConceptsDemo() {
        System.out.println("\n--- 4. 核心概念 ---");

        System.out.println("Topic（主题）:");
        System.out.println("  - 消息分类");
        System.out.println("  - 逻辑概念");

        System.out.println("\nPartition（分区）:");
        System.out.println("  - Topic的分区");
        System.out.println("  - 物理存储");
        System.out.println("  - 有序");
        System.out.println("  - 可扩展");

        System.out.println("\nOffset（偏移量）:");
        System.out.println("  - 消息位置");
        System.out.println("  - 单调递增");

        System.out.println("\nReplica（副本）:");
        System.out.println("  - 数据备份");
        System.out.println("  - Leader: 主副本");
        System.out.println("  - Follower: 从副本");
    }

    private static void featuresDemo() {
        System.out.println("\n--- 5. 特性 ---");

        System.out.println("高吞吐:");
        System.out.println("  - 百万级/秒");
        System.out.println("  - 批量处理");
        System.out.println("  - 零拷贝");

        System.out.println("\n低延迟:");
        System.out.println("  - 毫秒级");
        System.out.println("  - 实时处理");

        System.out.println("\n持久化:");
        System.out.println("  - 磁盘存储");
        System.out.println("  - 可配置保留时间");

        System.out.println("\n可扩展:");
        System.out.println("  - 水平扩展");
        System.out.println("  - 增加Broker");

        System.out.println("\n容错:");
        System.out.println("  - 多副本");
        System.out.println("  - 自动故障转移");
    }

    private static void applicationScenariosDemo() {
        System.out.println("\n--- 6. 应用场景 ---");

        System.out.println("1. 消息系统:");
        System.out.println("   - 解耦系统");
        System.out.println("   - 异步处理");

        System.out.println("\n2. 日志收集:");
        System.out.println("   - 统一日志收集");
        System.out.println("   - 实时分析");

        System.out.println("\n3. 用户活动跟踪:");
        System.out.println("   - 点击流");
        System.out.println("   - 用户行为");

        System.out.println("\n4. 流处理:");
        System.out.println("   - Kafka Streams");
        System.out.println("   - 实时计算");

        System.out.println("\n5. 事件源:");
        System.out.println("   - 事件驱动");
        System.out.println("   - 审计日志");

        System.out.println("\n6. 数据管道:");
        System.out.println("   - 数据集成");
        System.out.println("   - ETL");
    }
}
