package com.example.redis.masterslave;

import redis.clients.jedis.Jedis;

import java.util.Map;

/**
 * Redis 主从复制示例
 */
public class MasterSlaveDemo {
    
    public static void main(String[] args) {
        // 测试主服务器写入
        System.out.println("=== 测试主服务器写入 ===");
        testMasterWrite();
        
        // 测试从服务器读取
        System.out.println("\n=== 测试从服务器读取 ===");
        testSlaveRead();
        
        // 测试主从复制状态
        System.out.println("\n=== 测试主从复制状态 ===");
        testReplicationStatus();
    }
    
    /**
     * 测试主服务器写入
     */
    public static void testMasterWrite() {
        // 连接主服务器
        try (Jedis master = new Jedis("localhost", 6379)) {
            System.out.println("连接主服务器: " + master.ping());
            
            // 写入数据
            master.set("master_key", "master_value");
            master.set("counter", "0");
            master.incr("counter");
            
            // 读取数据
            System.out.println("主服务器数据:");
            System.out.println("master_key: " + master.get("master_key"));
            System.out.println("counter: " + master.get("counter"));
        }
    }
    
    /**
     * 测试从服务器读取
     */
    public static void testSlaveRead() {
        // 连接从服务器（默认端口6380）
        try (Jedis slave = new Jedis("localhost", 6380)) {
            try {
                System.out.println("连接从服务器: " + slave.ping());
                
                // 读取数据
                System.out.println("从服务器数据:");
                System.out.println("master_key: " + slave.get("master_key"));
                System.out.println("counter: " + slave.get("counter"));
                
                // 尝试写入数据（从服务器默认只读）
                try {
                    slave.set("slave_key", "slave_value");
                    System.out.println("从服务器写入成功（可能未开启只读模式）");
                } catch (Exception e) {
                    System.out.println("从服务器写入失败（只读模式）: " + e.getMessage());
                }
            } catch (Exception e) {
                System.out.println("连接从服务器失败: " + e.getMessage());
                System.out.println("请确保从服务器已启动并配置为主从复制");
            }
        }
    }
    
    /**
     * 测试主从复制状态
     */
    public static void testReplicationStatus() {
        // 检查主服务器状态
        try (Jedis master = new Jedis("localhost", 6379)) {
            System.out.println("=== 主服务器状态 ===");
            String masterInfo = master.info("replication");
            System.out.println(masterInfo);
        }
        
        // 检查从服务器状态
        try (Jedis slave = new Jedis("localhost", 6380)) {
            try {
                System.out.println("\n=== 从服务器状态 ===");
                String slaveInfo = slave.info("replication");
                System.out.println(slaveInfo);
            } catch (Exception e) {
                System.out.println("连接从服务器失败: " + e.getMessage());
            }
        }
    }
    
    /**
     * 测试主从复制故障转移
     */
    public static void testFailover() {
        // 连接从服务器
        try (Jedis slave = new Jedis("localhost", 6380)) {
            try {
                System.out.println("=== 测试故障转移 ===");
                
                // 停止从服务器的复制
                System.out.println("停止从服务器的复制...");
                String result = slave.slaveofNoOne();
                System.out.println("结果: " + result);
                
                // 检查状态
                String info = slave.info("replication");
                System.out.println("从服务器新状态:\n" + info);
                
                // 尝试写入数据
                slave.set("new_key", "new_value");
                System.out.println("写入新数据: " + slave.get("new_key"));
                
                // 恢复主从复制
                System.out.println("\n恢复主从复制...");
                result = slave.slaveof("localhost", 6379);
                System.out.println("结果: " + result);
                
                // 检查状态
                info = slave.info("replication");
                System.out.println("从服务器恢复状态:\n" + info);
            } catch (Exception e) {
                System.out.println("故障转移测试失败: " + e.getMessage());
            }
        }
    }
    
    /**
     * 测试批量写入和复制
     */
    public static void testBatchWrite() {
        // 连接主服务器
        try (Jedis master = new Jedis("localhost", 6379)) {
            System.out.println("=== 测试批量写入和复制 ===");
            
            // 批量写入数据
            for (int i = 1; i <= 10; i++) {
                master.set("batch_key_" + i, "value_" + i);
            }
            System.out.println("批量写入10条数据");
            
            // 验证主服务器数据
            System.out.println("\n主服务器数据:");
            for (int i = 1; i <= 10; i++) {
                System.out.println("batch_key_" + i + ": " + master.get("batch_key_" + i));
            }
            
            // 验证从服务器数据
            try (Jedis slave = new Jedis("localhost", 6380)) {
                try {
                    System.out.println("\n从服务器数据:");
                    for (int i = 1; i <= 10; i++) {
                        System.out.println("batch_key_" + i + ": " + slave.get("batch_key_" + i));
                    }
                } catch (Exception e) {
                    System.out.println("连接从服务器失败: " + e.getMessage());
                }
            }
        }
    }
}
