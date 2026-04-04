package com.example.redis.basic;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * Redis 基础概念示例
 */
public class BasicConceptsDemo {
    
    public static void main(String[] args) {
        // 测试基本连接
        System.out.println("=== 测试基本连接 ===");
        testBasicConnection();
        
        // 测试Jedis连接池
        System.out.println("\n=== 测试Jedis连接池 ===");
        testJedisPool();
        
        // 测试基本命令
        System.out.println("\n=== 测试基本命令 ===");
        testBasicCommands();
    }
    
    /**
     * 测试基本连接
     */
    public static void testBasicConnection() {
        // 创建Jedis实例
        Jedis jedis = new Jedis("localhost", 6379);
        
        try {
            // 测试连接
            String pong = jedis.ping();
            System.out.println("Ping response: " + pong);
            
            // 测试设置和获取数据
            jedis.set("hello", "world");
            String value = jedis.get("hello");
            System.out.println("Get value: " + value);
        } finally {
            // 关闭连接
            jedis.close();
        }
    }
    
    /**
     * 测试Jedis连接池
     */
    public static void testJedisPool() {
        // 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(10);
        poolConfig.setMaxIdle(5);
        poolConfig.setMinIdle(1);
        
        // 创建连接池
        JedisPool jedisPool = new JedisPool(poolConfig, "localhost", 6379);
        
        Jedis jedis = null;
        try {
            // 从连接池获取连接
            jedis = jedisPool.getResource();
            
            // 测试命令
            jedis.set("pool_test", "Hello Redis Pool");
            String value = jedis.get("pool_test");
            System.out.println("Get value from pool: " + value);
        } finally {
            // 归还连接
            if (jedis != null) {
                jedis.close();
            }
            // 关闭连接池
            jedisPool.close();
        }
    }
    
    /**
     * 测试基本命令
     */
    public static void testBasicCommands() {
        Jedis jedis = new Jedis("localhost", 6379);
        
        try {
            // 字符串操作
            System.out.println("=== 字符串操作 ===");
            jedis.set("string_key", "Hello Redis");
            System.out.println("Get string: " + jedis.get("string_key"));
            
            // 列表操作
            System.out.println("\n=== 列表操作 ===");
            jedis.lpush("list_key", "item1", "item2", "item3");
            System.out.println("List length: " + jedis.llen("list_key"));
            System.out.println("List items: " + jedis.lrange("list_key", 0, -1));
            
            // 集合操作
            System.out.println("\n=== 集合操作 ===");
            jedis.sadd("set_key", "member1", "member2", "member3");
            System.out.println("Set size: " + jedis.scard("set_key"));
            System.out.println("Set members: " + jedis.smembers("set_key"));
            
            // 哈希操作
            System.out.println("\n=== 哈希操作 ===");
            jedis.hset("hash_key", "field1", "value1");
            jedis.hset("hash_key", "field2", "value2");
            System.out.println("Hash fields: " + jedis.hkeys("hash_key"));
            System.out.println("Hash values: " + jedis.hvals("hash_key"));
            System.out.println("Hash get: " + jedis.hget("hash_key", "field1"));
            
            // 有序集合操作
            System.out.println("\n=== 有序集合操作 ===");
            jedis.zadd("zset_key", 1, "member1");
            jedis.zadd("zset_key", 2, "member2");
            jedis.zadd("zset_key", 3, "member3");
            System.out.println("ZSet size: " + jedis.zcard("zset_key"));
            System.out.println("ZSet members: " + jedis.zrange("zset_key", 0, -1));
            
            // 键操作
            System.out.println("\n=== 键操作 ===");
            System.out.println("Keys pattern *: " + jedis.keys("*"));
            System.out.println("Exists string_key: " + jedis.exists("string_key"));
            System.out.println("TTL string_key: " + jedis.ttl("string_key"));
            
            // 设置过期时间
            jedis.expire("string_key", 60);
            System.out.println("TTL string_key after expire: " + jedis.ttl("string_key"));
            
            // 删除键
            jedis.del("string_key");
            System.out.println("Exists string_key after del: " + jedis.exists("string_key"));
        } finally {
            jedis.close();
        }
    }
}
