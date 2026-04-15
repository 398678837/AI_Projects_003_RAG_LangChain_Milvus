package com.example.rocketmq.cluster;

import java.util.*;

public class BrokerClusterDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ Broker集群示例 ===");

        try {
            clusterArchitectureDemo();
            masterSlaveDemo();
            replicationDemo();
            clusterModeDemo();
            failoverDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void clusterArchitectureDemo() {
        System.out.println("\n--- 1. 集群架构 ---");
        System.out.println("集群模式:");
        System.out.println("  - 多Master模式");
        System.out.println("  - Master-Slave模式");
        System.out.println("  - Dledger模式");
        System.out.println();
        System.out.println("多Master模式:");
        System.out.println("  - 多个Master");
        System.out.println("  - 无Slave");
        System.out.println("  - 单Master故障影响该Master上的消息");
        System.out.println();
        System.out.println("Master-Slave模式:");
        System.out.println("  - 每个Master有Slave");
        System.out.println("  - 高可用");
        System.out.println("  - Master故障可切换到Slave");
    }

    private static void masterSlaveDemo() {
        System.out.println("\n--- 2. 主从复制 ---");
        System.out.println("Master配置:");
        System.out.println("  brokerRole=SYNC_MASTER/ASYNC_MASTER");
        System.out.println("  brokerId=0");
        System.out.println();
        System.out.println("Slave配置:");
        System.out.println("  brokerRole=SLAVE");
        System.out.println("  brokerId>0");
        System.out.println();
        System.out.println("HA端口: 10912");
    }

    private static void replicationDemo() {
        System.out.println("\n--- 3. 同步/异步复制 ---");
        System.out.println("同步复制 (SYNC_MASTER):");
        System.out.println("  - Master等待Slave确认");
        System.out.println("  - 可靠性高");
        System.out.println("  - 性能稍低");
        System.out.println();
        System.out.println("异步复制 (ASYNC_MASTER):");
        System.out.println("  - Master不等待Slave确认");
        System.out.println("  - 性能高");
        System.out.println("  - 可靠性稍低");
    }

    private static void clusterModeDemo() {
        System.out.println("\n--- 4. 集群模式 ---");
        System.out.println("2m-2s-async:");
        System.out.println("  - 2个Master");
        System.out.println("  - 每个Master 2个Slave");
        System.out.println("  - 异步复制");
        System.out.println();
        System.out.println("2m-2s-sync:");
        System.out.println("  - 2个Master");
        System.out.println("  - 每个Master 2个Slave");
        System.out.println("  - 同步复制");
    }

    private static void failoverDemo() {
        System.out.println("\n--- 5. 故障转移 ---");
        System.out.println("Master故障:");
        System.out.println("  - Slave提升为Master");
        System.out.println("  - 需要人工介入");
        System.out.println("  - 或使用Dledger自动切换");
        System.out.println();
        System.out.println("Dledger模式:");
        System.out.println("  - 基于Raft");
        System.out.println("  - 自动选主");
        System.out.println("  - 自动故障转移");
    }
}
