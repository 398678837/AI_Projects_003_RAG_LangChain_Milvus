package com.example.redis.sentinel;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisSentinelPool;

import java.util.HashSet;
import java.util.Set;

/**
 * Redis 哨兵模式示例
 */
public class SentinelDemo {
    
    public static void main(String[] args) {
        // 测试哨兵模式连接
        System.out.println("=== 测试哨兵模式连接 ===");
        testSentinelConnection();
        
        // 测试哨兵模式故障转移
        System.out.println("\n=== 测试哨兵模式故障转移 ===");
        testSentinelFailover();
    }
    
    /**
     * 测试哨兵模式连接
     */
    public static void testSentinelConnection() {
        // 哨兵地址集合
        Set<String> sentinels = new HashSet<>();
        sentinels.add("127.0.0.1:26379");
        sentinels.add("127.0.0.1:26380");
        sentinels.add("127.0.0.1:26381");
        
        // 主服务器名称
        String masterName = "mymaster";
        // 密码（如果有）
        String password = "";
        
        // 创建哨兵连接池
        try (JedisSentinelPool sentinelPool = new JedisSentinelPool(masterName, sentinels, password)) {
            System.out.println("哨兵连接池创建成功");
            
            // 获取连接
            try (Jedis jedis = sentinelPool.getResource()) {
                System.out.println("获取Redis连接成功: " + jedis.ping());
                
                // 测试写入
                jedis.set("sentinel_key", "sentinel_value");
                System.out.println("写入数据: " + jedis.get("sentinel_key"));
                
                // 测试自增
                jedis.set("sentinel_counter", "0");
                jedis.incr("sentinel_counter");
                System.out.println("自增操作: " + jedis.get("sentinel_counter"));
                
                // 获取主服务器地址
                System.out.println("当前主服务器地址: " + sentinelPool.getCurrentHostMaster());
            }
        } catch (Exception e) {
            System.out.println("哨兵模式连接失败: " + e.getMessage());
            System.out.println("请确保哨兵服务已启动并配置正确");
        }
    }
    
    /**
     * 测试哨兵模式故障转移
     */
    public static void testSentinelFailover() {
        // 哨兵地址集合
        Set<String> sentinels = new HashSet<>();
        sentinels.add("127.0.0.1:26379");
        
        // 主服务器名称
        String masterName = "mymaster";
        // 密码（如果有）
        String password = "";
        
        // 创建哨兵连接池
        try (JedisSentinelPool sentinelPool = new JedisSentinelPool(masterName, sentinels, password)) {
            System.out.println("哨兵连接池创建成功");
            
            // 获取当前主服务器
            System.out.println("初始主服务器: " + sentinelPool.getCurrentHostMaster());
            
            // 模拟故障转移
            System.out.println("\n模拟故障转移...");
            System.out.println("请手动停止当前主服务器，观察哨兵是否自动故障转移");
            System.out.println("按Enter键继续...");
            System.in.read();
            
            // 等待故障转移完成
            System.out.println("等待故障转移完成...");
            try {
                Thread.sleep(10000); // 等待10秒
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            // 获取新的主服务器
            System.out.println("故障转移后的主服务器: " + sentinelPool.getCurrentHostMaster());
            
            // 测试连接新的主服务器
            try (Jedis jedis = sentinelPool.getResource()) {
                System.out.println("连接新主服务器: " + jedis.ping());
                System.out.println("读取数据: " + jedis.get("sentinel_key"));
                System.out.println("读取计数器: " + jedis.get("sentinel_counter"));
            }
        } catch (Exception e) {
            System.out.println("故障转移测试失败: " + e.getMessage());
        }
    }
    
    /**
     * 测试哨兵状态
     */
    public static void testSentinelStatus() {
        // 连接哨兵
        try (Jedis sentinel = new Jedis("localhost", 26379)) {
            System.out.println("=== 测试哨兵状态 ===");
            System.out.println("连接哨兵: " + sentinel.ping());
            
            // 获取主服务器信息
            System.out.println("\n主服务器信息:");
            System.out.println(sentinel.sentinelMasters());
            
            // 获取从服务器信息
            System.out.println("\n从服务器信息:");
            System.out.println(sentinel.sentinelSlaves("mymaster"));
            
            // 获取当前主服务器地址
            System.out.println("\n当前主服务器地址:");
            System.out.println(sentinel.sentinelGetMasterAddrByName("mymaster"));
            
            // 获取哨兵信息
            System.out.println("\n哨兵信息:");
            System.out.println(sentinel.sentinelSentinels("mymaster"));
        } catch (Exception e) {
            System.out.println("测试哨兵状态失败: " + e.getMessage());
        }
    }
    
    /**
     * 测试手动故障转移
     */
    public static void testManualFailover() {
        // 连接哨兵
        try (Jedis sentinel = new Jedis("localhost", 26379)) {
            System.out.println("=== 测试手动故障转移 ===");
            System.out.println("连接哨兵: " + sentinel.ping());
            
            // 手动触发故障转移
            System.out.println("\n手动触发故障转移...");
            String result = sentinel.sentinelFailover("mymaster");
            System.out.println("故障转移结果: " + result);
            
            // 等待故障转移完成
            System.out.println("等待故障转移完成...");
            try {
                Thread.sleep(10000); // 等待10秒
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            // 获取新的主服务器地址
            System.out.println("\n故障转移后的主服务器地址:");
            System.out.println(sentinel.sentinelGetMasterAddrByName("mymaster"));
        } catch (Exception e) {
            System.out.println("手动故障转移测试失败: " + e.getMessage());
        }
    }
}
