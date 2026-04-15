package com.example.kafka.topic;

import java.util.*;

public class TopicDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka Topic示例 ===");

        try {
            createTopicDemo();
            topicConfigDemo();
            partitionCountDemo();
            replicaConfigDemo();
            topicManagementDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void createTopicDemo() {
        System.out.println("\n--- 1. 创建Topic ---");
        System.out.println("命令行创建:");
        System.out.println("  kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 2");
        System.out.println();
        System.out.println("自动创建:");
        System.out.println("  auto.create.topics.enable=true");
    }

    private static void topicConfigDemo() {
        System.out.println("\n--- 2. Topic配置 ---");
        System.out.println("分区数: --partitions");
        System.out.println("副本数: --replication-factor");
        System.out.println("清理策略: cleanup.policy");
        System.out.println("保留时间: retention.ms");
    }

    private static void partitionCountDemo() {
        System.out.println("\n--- 3. 分区数 ---");
        System.out.println("考虑因素:");
        System.out.println("  - 吞吐量");
        System.out.println("  - 并行度");
        System.out.println("  - Consumer数量");
    }

    private static void replicaConfigDemo() {
        System.out.println("\n--- 4. 副本配置 ---");
        System.out.println("副本数:");
        System.out.println("  - 1: 无副本");
        System.out.println("  - 2: 1个副本");
        System.out.println("  - 3: 2个副本");
    }

    private static void topicManagementDemo() {
        System.out.println("\n--- 5. Topic管理 ---");
        System.out.println("查看Topic列表:");
        System.out.println("  kafka-topics.sh --list --bootstrap-server localhost:9092");
        System.out.println();
        System.out.println("查看Topic详情:");
        System.out.println("  kafka-topics.sh --describe --topic my-topic --bootstrap-server localhost:9092");
    }
}
