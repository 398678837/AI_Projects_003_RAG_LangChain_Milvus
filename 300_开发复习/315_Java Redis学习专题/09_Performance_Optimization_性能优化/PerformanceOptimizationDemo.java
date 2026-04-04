package com.example.redis.performance;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.Pipeline;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Redis 性能优化示例
 */
public class PerformanceOptimizationDemo {
    
    public static void main(String[] args) {
        // 测试连接池性能
        System.out.println("=== 测试连接池性能 ===");
        testConnectionPool();
        
        // 测试批量操作性能
        System.out.println("\n=== 测试批量操作性能 ===");
        testBatchOperations();
        
        // 测试管道性能
        System.out.println("\n=== 测试管道性能 ===");
        testPipeline();
        
        // 测试数据结构优化
        System.out.println("\n=== 测试数据结构优化 ===");
        testDataStructureOptimization();
        
        // 测试命令优化
        System.out.println("\n=== 测试命令优化 ===");
        testCommandOptimization();
    }
    
    /**
     * 测试连接池性能
     */
    public static void testConnectionPool() {
        // 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(100);
        poolConfig.setMaxIdle(50);
        poolConfig.setMinIdle(10);
        poolConfig.setMaxWaitMillis(3000);
        
        // 创建连接池
        try (JedisPool jedisPool = new JedisPool(poolConfig, "localhost", 6379)) {
            long startTime = System.currentTimeMillis();
            
            // 测试1000次连接获取和释放
            for (int i = 0; i < 1000; i++) {
                try (Jedis jedis = jedisPool.getResource()) {
                    jedis.ping();
                }
            }
            
            long endTime = System.currentTimeMillis();
            System.out.println("1000次连接操作耗时: " + (endTime - startTime) + "ms");
        }
    }
    
    /**
     * 测试批量操作性能
     */
    public static void testBatchOperations() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试单个操作
            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                jedis.set("batch_key_" + i, "value_" + i);
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println("1000次单个SET操作耗时: " + (endTime1 - startTime1) + "ms");
            
            // 测试批量操作
            long startTime2 = System.currentTimeMillis();
            Map<String, String> keyValueMap = IntStream.range(0, 1000)
                .boxed()
                .collect(Collectors.toMap(i -> "batch_key_" + i, i -> "value_" + i));
            jedis.mset(keyValueMap);
            long endTime2 = System.currentTimeMillis();
            System.out.println("1000次批量SET操作耗时: " + (endTime2 - startTime2) + "ms");
            
            // 清理数据
            jedis.del(IntStream.range(0, 1000).mapToObj(i -> "batch_key_" + i).toArray(String[]::new));
        }
    }
    
    /**
     * 测试管道性能
     */
    public static void testPipeline() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试普通操作
            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                jedis.set("pipeline_key_" + i, "value_" + i);
                jedis.get("pipeline_key_" + i);
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println("1000次普通操作耗时: " + (endTime1 - startTime1) + "ms");
            
            // 测试管道操作
            long startTime2 = System.currentTimeMillis();
            Pipeline pipeline = jedis.pipelined();
            for (int i = 0; i < 1000; i++) {
                pipeline.set("pipeline_key_" + i, "value_" + i);
                pipeline.get("pipeline_key_" + i);
            }
            pipeline.sync();
            long endTime2 = System.currentTimeMillis();
            System.out.println("1000次管道操作耗时: " + (endTime2 - startTime2) + "ms");
            
            // 清理数据
            jedis.del(IntStream.range(0, 1000).mapToObj(i -> "pipeline_key_" + i).toArray(String[]::new));
        }
    }
    
    /**
     * 测试数据结构优化
     */
    public static void testDataStructureOptimization() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试使用多个String存储对象
            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                jedis.set("user_" + i + "_name", "User" + i);
                jedis.set("user_" + i + "_email", "user" + i + "@example.com");
                jedis.set("user_" + i + "_age", String.valueOf(20 + i % 10));
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println("使用多个String存储1000个用户耗时: " + (endTime1 - startTime1) + "ms");
            
            // 测试使用Hash存储对象
            long startTime2 = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                jedis.hset("user:" + i, "name", "User" + i);
                jedis.hset("user:" + i, "email", "user" + i + "@example.com");
                jedis.hset("user:" + i, "age", String.valueOf(20 + i % 10));
            }
            long endTime2 = System.currentTimeMillis();
            System.out.println("使用Hash存储1000个用户耗时: " + (endTime2 - startTime2) + "ms");
            
            // 清理数据
            // 清理String
            List<String> stringKeys = new ArrayList<>();
            for (int i = 0; i < 1000; i++) {
                stringKeys.add("user_" + i + "_name");
                stringKeys.add("user_" + i + "_email");
                stringKeys.add("user_" + i + "_age");
            }
            jedis.del(stringKeys.toArray(new String[0]));
            
            // 清理Hash
            List<String> hashKeys = IntStream.range(0, 1000)
                .mapToObj(i -> "user:" + i)
                .collect(Collectors.toList());
            jedis.del(hashKeys.toArray(new String[0]));
        }
    }
    
    /**
     * 测试命令优化
     */
    public static void testCommandOptimization() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 准备数据
            for (int i = 0; i < 1000; i++) {
                jedis.set("command_key_" + i, "value_" + i);
            }
            
            // 测试KEYS命令
            long startTime1 = System.currentTimeMillis();
            jedis.keys("command_key_*");
            long endTime1 = System.currentTimeMillis();
            System.out.println("使用KEYS命令耗时: " + (endTime1 - startTime1) + "ms");
            
            // 测试SCAN命令
            long startTime2 = System.currentTimeMillis();
            String cursor = "0";
            do {
                redis.clients.jedis.ScanResult<String> result = jedis.scan(cursor, new redis.clients.jedis.ScanParams().match("command_key_*").count(100));
                cursor = result.getCursor();
            } while (!cursor.equals("0"));
            long endTime2 = System.currentTimeMillis();
            System.out.println("使用SCAN命令耗时: " + (endTime2 - startTime2) + "ms");
            
            // 清理数据
            jedis.del(IntStream.range(0, 1000).mapToObj(i -> "command_key_" + i).toArray(String[]::new));
        }
    }
    
    /**
     * 测试内存优化
     */
    public static void testMemoryOptimization() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试不同数据结构的内存使用
            System.out.println("\n=== 测试内存使用 ===");
            
            // 存储1000个String
            for (int i = 0; i < 1000; i++) {
                jedis.set("memory_string_" + i, "value_" + i);
            }
            
            // 存储1000个Hash
            for (int i = 0; i < 1000; i++) {
                jedis.hset("memory_hash", "field_" + i, "value_" + i);
            }
            
            // 获取内存使用情况
            String info = jedis.info("memory");
            System.out.println("内存使用情况:");
            System.out.println(info);
            
            // 清理数据
            jedis.del(IntStream.range(0, 1000).mapToObj(i -> "memory_string_" + i).toArray(String[]::new));
            jedis.del("memory_hash");
        }
    }
    
    /**
     * 测试过期时间设置
     */
    public static void testExpiration() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试单个设置过期时间
            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                jedis.set("expire_key_" + i, "value_" + i);
                jedis.expire("expire_key_" + i, 60);
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println("单个设置过期时间耗时: " + (endTime1 - startTime1) + "ms");
            
            // 测试批量设置过期时间
            long startTime2 = System.currentTimeMillis();
            Pipeline pipeline = jedis.pipelined();
            for (int i = 0; i < 1000; i++) {
                pipeline.set("expire_key_" + i, "value_" + i);
                pipeline.expire("expire_key_" + i, 60);
            }
            pipeline.sync();
            long endTime2 = System.currentTimeMillis();
            System.out.println("批量设置过期时间耗时: " + (endTime2 - startTime2) + "ms");
            
            // 清理数据
            jedis.del(IntStream.range(0, 1000).mapToObj(i -> "expire_key_" + i).toArray(String[]::new));
        }
    }
}
