package com.example.kafka.core;

import java.util.*;

public class CoreComponentsDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka核心组件示例 ===");

        try {
            producerDemo();
            consumerDemo();
            brokerDemo();
            topicPartitionDemo();
            storageStructureDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void producerDemo() {
        System.out.println("\n--- 1. Producer ---");
        System.out.println("Producer的作用:");
        System.out.println("  - 发送消息");
        System.out.println("  - 分区选择");
        System.out.println("  - 序列化");
        System.out.println("  - 压缩");
        System.out.println("  - 批量发送");
    }

    private static void consumerDemo() {
        System.out.println("\n--- 2. Consumer ---");
        System.out.println("Consumer的作用:");
        System.out.println("  - 拉取消息");
        System.out.println("  - 消费组");
        System.out.println("  - Offset管理");
        System.out.println("  - 提交Offset");
        System.out.println("  - 重平衡");
    }

    private static void brokerDemo() {
        System.out.println("\n--- 3. Broker ---");
        System.out.println("Broker的作用:");
        System.out.println("  - 存储消息");
        System.out.println("  - 处理请求");
        System.out.println("  - 副本同步");
        System.out.println("  - Leader选举");
    }

    private static void topicPartitionDemo() {
        System.out.println("\n--- 4. Topic和Partition ---");
        System.out.println("Topic:");
        System.out.println("  - 消息分类");
        System.out.println("  - 逻辑概念");
        System.out.println();
        System.out.println("Partition:");
        System.out.println("  - Topic的分区");
        System.out.println("  - 物理存储");
        System.out.println("  - 有序");
    }

    private static void storageStructureDemo() {
        System.out.println("\n--- 5. 存储结构 ---");
        System.out.println("日志分段:");
        System.out.println("  - 分段存储");
        System.out.println("  - 固定大小");
        System.out.println();
        System.out.println("索引文件:");
        System.out.println("  - 消息索引");
        System.out.println("  - 加速查找");
    }
}
