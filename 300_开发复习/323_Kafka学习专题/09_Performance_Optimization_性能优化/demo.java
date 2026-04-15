package com.example.kafka.performance;

import java.util.*;

public class PerformanceOptimizationDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka性能优化示例 ===");

        try {
            producerOptimizationDemo();
            consumerOptimizationDemo();
            brokerOptimizationDemo();
            partitionOptimizationDemo();
            monitoringDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void producerOptimizationDemo() {
        System.out.println("\n--- 1. Producer优化 ---");
        System.out.println("批量发送:");
        System.out.println("  batch.size=16384");
        System.out.println("  linger.ms=5");
        System.out.println();
        System.out.println("压缩:");
        System.out.println("  compression.type=gzip");
        System.out.println();
        System.out.println("acks:");
        System.out.println("  acks=1");
    }

    private static void consumerOptimizationDemo() {
        System.out.println("\n--- 2. Consumer优化 ---");
        System.out.println("批量消费:");
        System.out.println("  max.poll.records=500");
        System.out.println();
        System.out.println("fetch大小:");
        System.out.println("  fetch.min.bytes=1024");
        System.out.println("  fetch.max.wait.ms=500");
    }

    private static void brokerOptimizationDemo() {
        System.out.println("\n--- 3. Broker优化 ---");
        System.out.println("JVM调优:");
        System.out.println("  -Xmx6g -Xms6g");
        System.out.println();
        System.out.println("磁盘优化:");
        System.out.println("  使用SSD");
        System.out.println("  日志目录分离");
    }

    private static void partitionOptimizationDemo() {
        System.out.println("\n--- 4. 分区优化 ---");
        System.out.println("分区数:");
        System.out.println("  根据吞吐量考虑");
        System.out.println();
        System.out.println("副本数:");
        System.out.println("  3个副本");
    }

    private static void monitoringDemo() {
        System.out.println("\n--- 5. 监控 ---");
        System.out.println("监控指标:");
        System.out.println("  - 消息速率");
        System.out.println("  - 延迟");
        System.out.println("  - 副本同步");
    }
}
