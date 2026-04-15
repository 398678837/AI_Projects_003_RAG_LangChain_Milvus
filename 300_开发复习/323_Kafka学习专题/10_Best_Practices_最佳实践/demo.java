package com.example.kafka.bestpractices;

import java.util.*;

public class BestPracticesDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka最佳实践示例 ===");

        try {
            messageDesignDemo();
            exceptionHandlingDemo();
            resourceManagementDemo();
            securityDemo();
            monitoringOpsDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void messageDesignDemo() {
        System.out.println("\n--- 1. 消息设计 ---");
        System.out.println("Topic设计:");
        System.out.println("  - 按业务划分");
        System.out.println("  - 合理命名");
        System.out.println();
        System.out.println("Key设计:");
        System.out.println("  - 有业务含义");
        System.out.println("  - 用于分区");
        System.out.println();
        System.out.println("消息大小:");
        System.out.println("  - 建议小于1MB");
        System.out.println("  - 大消息拆分");
    }

    private static void exceptionHandlingDemo() {
        System.out.println("\n--- 2. 异常处理 ---");
        System.out.println("发送异常:");
        System.out.println("  - 重试");
        System.out.println("  - 记录日志");
        System.out.println();
        System.out.println("消费异常:");
        System.out.println("  - 重试");
        System.out.println("  - 死信队列");
    }

    private static void resourceManagementDemo() {
        System.out.println("\n--- 3. 资源管理 ---");
        System.out.println("Producer管理:");
        System.out.println("  - 单例");
        System.out.println("  - 应用关闭时关闭");
        System.out.println();
        System.out.println("Consumer管理:");
        System.out.println("  - 单例");
        System.out.println("  - 优雅关闭");
    }

    private static void securityDemo() {
        System.out.println("\n--- 4. 安全 ---");
        System.out.println("认证:");
        System.out.println("  - SASL");
        System.out.println("  - SSL/TLS");
        System.out.println();
        System.out.println("授权:");
        System.out.println("  - ACL");
        System.out.println("  - 最小权限");
    }

    private static void monitoringOpsDemo() {
        System.out.println("\n--- 5. 监控运维 ---");
        System.out.println("监控指标:");
        System.out.println("  - 消息速率");
        System.out.println("  - 延迟");
        System.out.println("  - 副本同步");
        System.out.println();
        System.out.println("告警:");
        System.out.println("  - 延迟过高");
        System.out.println("  - 副本不同步");
    }
}
