package com.example.rocketmq.bestpractices;

import java.util.*;

public class BestPracticesDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ最佳实践示例 ===");

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
        System.out.println("  - 业务隔离");
        System.out.println("  - 避免过多Topic");
        System.out.println("  - 命名规范");
        System.out.println();
        System.out.println("Tag设计:");
        System.out.println("  - 消息细分");
        System.out.println("  - 用于过滤");
        System.out.println("  - 不宜过多");
        System.out.println();
        System.out.println("Key设计:");
        System.out.println("  - 业务唯一标识");
        System.out.println("  - 用于查询");
        System.out.println("  - 去重");
        System.out.println();
        System.out.println("消息大小:");
        System.out.println("  - 建议小于4K");
        System.out.println("  - 大消息拆分");
        System.out.println("  - 压缩");
    }

    private static void exceptionHandlingDemo() {
        System.out.println("\n--- 2. 异常处理 ---");
        System.out.println("发送异常:");
        System.out.println("  - 重试");
        System.out.println("  - 记录日志");
        System.out.println("  - 告警");
        System.out.println();
        System.out.println("消费异常:");
        System.out.println("  - 返回RECONSUME_LATER重试");
        System.out.println("  - 记录异常");
        System.out.println("  - 告警");
        System.out.println();
        System.out.println("死信处理:");
        System.out.println("  - 监听死信队列");
        System.out.println("  - 人工处理");
        System.out.println("  - 重新发送");
    }

    private static void resourceManagementDemo() {
        System.out.println("\n--- 3. 资源管理 ---");
        System.out.println("Producer管理:");
        System.out.println("  - 单例模式");
        System.out.println("  - 应用启动时创建");
        System.out.println("  - 应用关闭时关闭");
        System.out.println();
        System.out.println("Consumer管理:");
        System.out.println("  - 单例模式");
        System.out.println("  - 应用启动时创建");
        System.out.println("  - 应用关闭时关闭");
        System.out.println();
        System.out.println("内存管理:");
        System.out.println("  - 合理设置JVM堆");
        System.out.println("  - 注意直接内存");
        System.out.println("  - 监控内存使用");
    }

    private static void securityDemo() {
        System.out.println("\n--- 4. 安全 ---");
        System.out.println("认证:");
        System.out.println("  - ACL控制");
        System.out.println("  - 用户密码");
        System.out.println("  - Token认证");
        System.out.println();
        System.out.println("授权:");
        System.out.println("  - Topic权限");
        System.out.println("  - Group权限");
        System.out.println("  - 最小权限原则");
        System.out.println();
        System.out.println("网络安全:");
        System.out.println("  - TLS加密");
        System.out.println("  - 内网部署");
        System.out.println("  - 防火墙");
    }

    private static void monitoringOpsDemo() {
        System.out.println("\n--- 5. 监控和运维 ---");
        System.out.println("监控指标:");
        System.out.println("  - TPS");
        System.out.println("  - 延迟");
        System.out.println("  - 消息堆积");
        System.out.println("  - 消费进度");
        System.out.println();
        System.out.println("告警规则:");
        System.out.println("  - 消息堆积告警");
        System.out.println("  - 消费失败告警");
        System.out.println("  - 系统资源告警");
        System.out.println();
        System.out.println("容量规划:");
        System.out.println("  - Topic数量");
        System.out.println("  - 消息量预估");
        System.out.println("  - 存储容量");
        System.out.println("  - Broker扩容");
    }
}
