package com.example.redis.bestpractices;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.Pipeline;

import java.util.*;
import java.util.concurrent.TimeUnit;

/**
 * Redis 最佳实践示例
 */
public class BestPracticesDemo {
    
    public static void main(String[] args) {
        // 测试连接池使用
        System.out.println("=== 测试连接池使用 ===");
        testConnectionPool();
        
        // 测试键名设计
        System.out.println("\n=== 测试键名设计 ===");
        testKeyNaming();
        
        // 测试分布式锁
        System.out.println("\n=== 测试分布式锁 ===");
        testDistributedLock();
        
        // 测试缓存策略
        System.out.println("\n=== 测试缓存策略 ===");
        testCacheStrategy();
        
        // 测试消息队列
        System.out.println("\n=== 测试消息队列 ===");
        testMessageQueue();
        
        // 测试排行榜
        System.out.println("\n=== 测试排行榜 ===");
        testLeaderboard();
    }
    
    /**
     * 测试连接池使用
     */
    public static void testConnectionPool() {
        // 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(50);
        poolConfig.setMaxIdle(25);
        poolConfig.setMinIdle(5);
        poolConfig.setMaxWaitMillis(3000);
        poolConfig.setTestOnBorrow(true);
        
        // 创建连接池
        try (JedisPool jedisPool = new JedisPool(poolConfig, "localhost", 6379)) {
            System.out.println("连接池创建成功");
            
            // 测试多线程使用连接池
            Thread[] threads = new Thread[10];
            for (int i = 0; i < threads.length; i++) {
                final int threadId = i;
                threads[i] = new Thread(() -> {
                    try (Jedis jedis = jedisPool.getResource()) {
                        System.out.println("线程" + threadId + "获取连接成功: " + jedis.ping());
                        jedis.set("thread_key_" + threadId, "value_" + threadId);
                        System.out.println("线程" + threadId + "设置值: " + jedis.get("thread_key_" + threadId));
                    }
                });
                threads[i].start();
            }
            
            // 等待所有线程完成
            for (Thread thread : threads) {
                try {
                    thread.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            
            System.out.println("所有线程执行完成");
        }
    }
    
    /**
     * 测试键名设计
     */
    public static void testKeyNaming() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 推荐的键名设计
            String userKey = "user:123";
            String productKey = "product:456";
            String orderKey = "order:789";
            
            // 设置用户信息
            jedis.hset(userKey, "name", "Alice");
            jedis.hset(userKey, "email", "alice@example.com");
            jedis.hset(userKey, "age", "30");
            
            // 设置商品信息
            jedis.hset(productKey, "name", "Redis Guide");
            jedis.hset(productKey, "price", "99.99");
            jedis.hset(productKey, "stock", "100");
            
            // 设置订单信息
            jedis.hset(orderKey, "user_id", "123");
            jedis.hset(orderKey, "product_id", "456");
            jedis.hset(orderKey, "amount", "99.99");
            jedis.hset(orderKey, "status", "pending");
            
            // 获取用户信息
            System.out.println("用户信息: " + jedis.hgetAll(userKey));
            
            // 获取商品信息
            System.out.println("商品信息: " + jedis.hgetAll(productKey));
            
            // 获取订单信息
            System.out.println("订单信息: " + jedis.hgetAll(orderKey));
            
            // 清理数据
            jedis.del(userKey, productKey, orderKey);
        }
    }
    
    /**
     * 测试分布式锁
     */
    public static void testDistributedLock() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            String lockKey = "lock:resource";
            String requestId = UUID.randomUUID().toString();
            int expireTime = 10; // 10秒
            
            // 获取锁
            boolean acquired = acquireLock(jedis, lockKey, requestId, expireTime);
            System.out.println("获取锁结果: " + acquired);
            
            if (acquired) {
                try {
                    // 执行业务逻辑
                    System.out.println("执行业务逻辑...");
                    Thread.sleep(5000); // 模拟业务逻辑执行
                } finally {
                    // 释放锁
                    boolean released = releaseLock(jedis, lockKey, requestId);
                    System.out.println("释放锁结果: " + released);
                }
            }
        }
    }
    
    /**
     * 获取分布式锁
     */
    public static boolean acquireLock(Jedis jedis, String lockKey, String requestId, int expireTime) {
        String result = jedis.set(lockKey, requestId, "NX", "EX", expireTime);
        return "OK".equals(result);
    }
    
    /**
     * 释放分布式锁
     */
    public static boolean releaseLock(Jedis jedis, String lockKey, String requestId) {
        String script = "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end";
        Object result = jedis.eval(script, Collections.singletonList(lockKey), Collections.singletonList(requestId));
        return Long.valueOf(1).equals(result);
    }
    
    /**
     * 测试缓存策略
     */
    public static void testCacheStrategy() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            String cacheKey = "cache:user:123";
            
            // 测试缓存命中
            System.out.println("测试缓存命中");
            jedis.set(cacheKey, "{\"id\":123,\"name\":\"Alice\",\"email\":\"alice@example.com\"}");
            jedis.expire(cacheKey, 60); // 设置60秒过期
            
            String cachedData = jedis.get(cacheKey);
            System.out.println("缓存命中: " + cachedData);
            
            // 测试缓存穿透防护
            System.out.println("\n测试缓存穿透防护");
            String nonExistentKey = "cache:user:999";
            
            // 缓存空结果
            String data = jedis.get(nonExistentKey);
            if (data == null) {
                // 从数据库获取（模拟）
                System.out.println("从数据库获取数据");
                // 缓存空结果，设置较短的过期时间
                jedis.set(nonExistentKey, "{}");
                jedis.expire(nonExistentKey, 5); // 5秒过期
            } else {
                System.out.println("从缓存获取空结果: " + data);
            }
            
            // 测试缓存预热
            System.out.println("\n测试缓存预热");
            for (int i = 1; i <= 5; i++) {
                String预热Key = "cache:user:" + i;
                jedis.set(预热Key, "{\"id\":" + i + ",\"name\":\"User" + i + "\"}");
                jedis.expire(预热Key, 3600); // 1小时过期
            }
            System.out.println("缓存预热完成");
            
            // 清理数据
            jedis.del(cacheKey, nonExistentKey);
            for (int i = 1; i <= 5; i++) {
                jedis.del("cache:user:" + i);
            }
        }
    }
    
    /**
     * 测试消息队列
     */
    public static void testMessageQueue() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            String queueKey = "queue:messages";
            
            // 生产者：发送消息
            System.out.println("生产者：发送消息");
            for (int i = 1; i <= 5; i++) {
                String message = "Message " + i;
                jedis.lpush(queueKey, message);
                System.out.println("发送消息: " + message);
            }
            
            // 消费者：接收消息
            System.out.println("\n消费者：接收消息");
            while (true) {
                List<String> messages = jedis.brpop(1, queueKey);
                if (messages != null) {
                    String message = messages.get(1);
                    System.out.println("接收消息: " + message);
                } else {
                    break;
                }
            }
            
            // 清理数据
            jedis.del(queueKey);
        }
    }
    
    /**
     * 测试排行榜
     */
    public static void testLeaderboard() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            String leaderboardKey = "leaderboard:scores";
            
            // 添加分数
            System.out.println("添加分数");
            jedis.zadd(leaderboardKey, 100, "user1");
            jedis.zadd(leaderboardKey, 200, "user2");
            jedis.zadd(leaderboardKey, 150, "user3");
            jedis.zadd(leaderboardKey, 250, "user4");
            jedis.zadd(leaderboardKey, 180, "user5");
            
            // 获取排行榜（降序）
            System.out.println("\n排行榜（降序）");
            Set<String> leaderboard = jedis.zrevrange(leaderboardKey, 0, -1);
            int rank = 1;
            for (String user : leaderboard) {
                double score = jedis.zscore(leaderboardKey, user);
                System.out.println("第" + rank + "名: " + user + " (" + score + ")");
                rank++;
            }
            
            // 获取用户排名
            System.out.println("\n用户排名");
            long user2Rank = jedis.zrevrank(leaderboardKey, "user2") + 1;
            System.out.println("user2的排名: " + user2Rank);
            
            // 更新分数
            System.out.println("\n更新分数");
            jedis.zincrby(leaderboardKey, 50, "user1");
            System.out.println("user1的新分数: " + jedis.zscore(leaderboardKey, "user1"));
            
            // 再次获取排行榜
            System.out.println("\n更新后的排行榜");
            leaderboard = jedis.zrevrange(leaderboardKey, 0, -1);
            rank = 1;
            for (String user : leaderboard) {
                double score = jedis.zscore(leaderboardKey, user);
                System.out.println("第" + rank + "名: " + user + " (" + score + ")");
                rank++;
            }
            
            // 清理数据
            jedis.del(leaderboardKey);
        }
    }
    
    /**
     * 测试批量操作
     */
    public static void testBatchOperations() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            System.out.println("\n=== 测试批量操作 ===");
            
            // 批量设置
            Map<String, String> keyValueMap = new HashMap<>();
            for (int i = 1; i <= 10; i++) {
                keyValueMap.put("batch:key:" + i, "value:" + i);
            }
            jedis.mset(keyValueMap);
            System.out.println("批量设置10个键值对");
            
            // 批量获取
            List<String> keys = new ArrayList<>();
            for (int i = 1; i <= 10; i++) {
                keys.add("batch:key:" + i);
            }
            List<String> values = jedis.mget(keys.toArray(new String[0]));
            System.out.println("批量获取10个键值对: " + values);
            
            // 使用管道
            System.out.println("\n使用管道批量操作");
            Pipeline pipeline = jedis.pipelined();
            for (int i = 11; i <= 20; i++) {
                pipeline.set("pipeline:key:" + i, "value:" + i);
                pipeline.get("pipeline:key:" + i);
            }
            List<Object> results = pipeline.syncAndReturnAll();
            System.out.println("管道操作结果数量: " + results.size());
            
            // 清理数据
            for (int i = 1; i <= 10; i++) {
                jedis.del("batch:key:" + i);
            }
            for (int i = 11; i <= 20; i++) {
                jedis.del("pipeline:key:" + i);
            }
        }
    }
}
