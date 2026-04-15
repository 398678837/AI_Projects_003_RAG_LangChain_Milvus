package com.example.rabbitmq.bestpractices;

public class BestPracticesDemo {

    public static void main(String[] args) {
        System.out.println("=== RabbitMQ最佳实践示例 ===");

        try {
            messageDesignDemo();
            exceptionHandlingDemo();
            resourceManagementDemo();
            performanceOptimizationDemo();
            monitoringOpsDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void messageDesignDemo() {
        System.out.println("\n--- 1. 消息设计 ---");
        System.out.println("Exchange设计:");
        System.out.println("  - 按业务划分");
        System.out.println("  - 合理选择类型");
        System.out.println();
        System.out.println("Queue设计:");
        System.out.println("  - 有意义的命名");
        System.out.println("  - 考虑持久化");
        System.out.println();
        System.out.println("消息大小:");
        System.out.println("  - 建议小于128K");
        System.out.println("  - 大消息拆分");
    }

    private static void exceptionHandlingDemo() {
        System.out.println("\n--- 2. 异常处理 ---");
        System.out.println("发送异常:");
        System.out.println("  - 发布确认");
        System.out.println("  - 重试");
        System.out.println("  - 记录日志");
        System.out.println();
        System.out.println("消费异常:");
        System.out.println("  - 手动确认");
        System.out.println("  - Nack重入队列");
        System.out.println("  - 死信队列");
    }

    private static void resourceManagementDemo() {
        System.out.println("\n--- 3. 资源管理 ---");
        System.out.println("连接管理:");
        System.out.println("  - 单例Connection");
        System.out.println("  - 应用关闭时关闭");
        System.out.println();
        System.out.println("通道管理:");
        System.out.println("  - 复用Channel");
        System.out.println("  - 线程安全考虑");
    }

    private static void performanceOptimizationDemo() {
        System.out.println("\n--- 4. 性能优化 ---");
        System.out.println("发布确认:");
        System.out.println("  - 异步确认");
        System.out.println("  - 批量确认");
        System.out.println();
        System.out.println("QoS设置:");
        System.out.println("  - 合理的预取计数");
        System.out.println("  - 公平分发");
    }

    private static void monitoringOpsDemo() {
        System.out.println("\n--- 5. 监控和运维 ---");
        System.out.println("监控指标:");
        System.out.println("  - 队列消息数");
        System.out.println("  - 消费者数");
        System.out.println("  - 消息速率");
        System.out.println();
        System.out.println("告警:");
        System.out.println("  - 队列堆积");
        System.out.println("  - 无消费者");
        System.out.println("  - 连接异常");
    }
}
