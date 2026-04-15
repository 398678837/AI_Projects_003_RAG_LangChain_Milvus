package com.example.rocketmq.performance;

import java.util.*;

public class PerformanceOptimizationDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ性能优化示例 ===");

        try {
            producerOptimizationDemo();
            consumerOptimizationDemo();
            brokerOptimizationDemo();
            storageOptimizationDemo();
            monitoringDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void producerOptimizationDemo() {
        System.out.println("\n--- 1. Producer优化 ---");
        System.out.println("异步发送:");
        System.out.println("  - 性能高");
        System.out.println("  - 使用回调");
        System.out.println();
        System.out.println("批量发送:");
        System.out.println("  producer.setBatchMaxCount(100);");
        System.out.println("  producer.setBatchMaxSize(1024 * 128);");
        System.out.println();
        System.out.println("消息压缩:");
        System.out.println("  producer.setCompressMsgBodyOverHowmuch(4096);");
        System.out.println("  - 减少网络传输");
        System.out.println("  - 节省存储空间");
    }

    private static void consumerOptimizationDemo() {
        System.out.println("\n--- 2. Consumer优化 ---");
        System.out.println("批量消费:");
        System.out.println("  consumer.setConsumeMessageBatchMaxSize(32);");
        System.out.println();
        System.out.println("消费线程数:");
        System.out.println("  consumer.setConsumeThreadMin(20);");
        System.out.println("  consumer.setConsumeThreadMax(64);");
        System.out.println();
        System.out.println("消息过滤:");
        System.out.println("  - Tag过滤");
        System.out.println("  - SQL92过滤");
        System.out.println("  - 减少传输量");
    }

    private static void brokerOptimizationDemo() {
        System.out.println("\n--- 3. Broker优化 ---");
        System.out.println("刷盘策略:");
        System.out.println("  - ASYNC_FLUSH: 异步刷盘");
        System.out.println("  - SYNC_FLUSH: 同步刷盘");
        System.out.println();
        System.out.println("JVM参数:");
        System.out.println("  - Xms8g -Xmx8g");
        System.out.println("  - XX:MaxDirectMemorySize=15g");
        System.out.println();
        System.out.println("存储路径:");
        System.out.println("  - 使用SSD");
        System.out.println("  - CommitLog和ConsumeQueue分离");
    }

    private static void storageOptimizationDemo() {
        System.out.println("\n--- 4. 存储优化 ---");
        System.out.println("CommitLog:");
        System.out.println("  - 顺序写入");
        System.out.println("  - 内存映射");
        System.out.println("  - 零拷贝");
        System.out.println();
        System.out.println("ConsumeQueue:");
        System.out.println("  - 索引文件");
        System.out.println("  - 固定大小");
        System.out.println("  - 内存映射");
    }

    private static void monitoringDemo() {
        System.out.println("\n--- 5. 监控指标 ---");
        System.out.println("关键指标:");
        System.out.println("  - TPS: 每秒事务数");
        System.out.println("  - 延迟: 消息处理时间");
        System.out.println("  - 消息堆积: 未消费消息数");
        System.out.println("  - 消费进度: Offset位置");
        System.out.println("  - 系统资源: CPU/内存/磁盘");
        System.out.println();
        System.out.println("监控工具:");
        System.out.println("  - RocketMQ Console");
        System.out.println("  - Prometheus + Grafana");
        System.out.println("  - mqadmin命令");
    }
}
