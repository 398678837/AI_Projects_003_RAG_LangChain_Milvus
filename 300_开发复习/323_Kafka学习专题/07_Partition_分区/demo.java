package com.example.kafka.partition;

import java.util.*;

public class PartitionDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka Partition示例 ===");

        try {
            partitionConceptDemo();
            partitionStrategyDemo();
            partitionAssignmentDemo();
            replicaSyncDemo();
            leaderElectionDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void partitionConceptDemo() {
        System.out.println("\n--- 1. 分区概念 ---");
        System.out.println("分区作用:");
        System.out.println("  - 提高吞吐");
        System.out.println("  - 并行处理");
        System.out.println("  - 扩展性");
    }

    private static void partitionStrategyDemo() {
        System.out.println("\n--- 2. 分区策略 ---");
        System.out.println("默认分区器:");
        System.out.println("  - 有Key: Key Hash");
        System.out.println("  - 无Key: Round-robin");
    }

    private static void partitionAssignmentDemo() {
        System.out.println("\n--- 3. 分区分配 ---");
        System.out.println("Range策略:");
        System.out.println("  - 按Topic分配");
        System.out.println();
        System.out.println("Round-robin策略:");
        System.out.println("  - 轮询分配");
    }

    private static void replicaSyncDemo() {
        System.out.println("\n--- 4. 副本同步 ---");
        System.out.println("ISR:");
        System.out.println("  - In-Sync Replicas");
        System.out.println("  - 同步副本");
    }

    private static void leaderElectionDemo() {
        System.out.println("\n--- 5. Leader选举 ---");
        System.out.println("选举触发:");
        System.out.println("  - Leader故障");
        System.out.println("  - 从ISR选举");
    }
}
