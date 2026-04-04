package com.example.redis.installation;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

import java.util.Properties;

/**
 * Redis 安装配置示例
 */
public class InstallationDemo {
    
    public static void main(String[] args) {
        // 测试不同连接方式
        System.out.println("=== 测试基本连接 ===");
        testBasicConnection();
        
        System.out.println("\n=== 测试带密码的连接 ===");
        testPasswordConnection();
        
        System.out.println("\n=== 测试连接池配置 ===");
        testPoolConfiguration();
        
        System.out.println("\n=== 测试环境变量配置 ===");
        testEnvironmentVariables();
    }
    
    /**
     * 测试基本连接
     */
    public static void testBasicConnection() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            System.out.println("连接成功: " + jedis.ping());
            
            // 测试基本命令
            jedis.set("test_key", "test_value");
            System.out.println("获取值: " + jedis.get("test_key"));
        }
    }
    
    /**
     * 测试带密码的连接
     */
    public static void testPasswordConnection() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            try {
                // 尝试认证
                jedis.auth("your_password");
                System.out.println("密码认证成功: " + jedis.ping());
            } catch (Exception e) {
                System.out.println("密码认证失败（可能未设置密码）: " + e.getMessage());
                // 继续测试，不使用密码
                System.out.println("不使用密码连接: " + jedis.ping());
            }
        }
    }
    
    /**
     * 测试连接池配置
     */
    public static void testPoolConfiguration() {
        // 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        
        // 最大连接数
        poolConfig.setMaxTotal(10);
        // 最大空闲连接数
        poolConfig.setMaxIdle(5);
        // 最小空闲连接数
        poolConfig.setMinIdle(1);
        // 连接超时时间
        poolConfig.setMaxWaitMillis(3000);
        // 测试连接是否有效
        poolConfig.setTestOnBorrow(true);
        
        // 创建连接池
        try (JedisPool jedisPool = new JedisPool(poolConfig, "localhost", 6379)) {
            // 从连接池获取连接
            try (Jedis jedis = jedisPool.getResource()) {
                System.out.println("连接池连接成功: " + jedis.ping());
                
                // 测试基本命令
                jedis.set("pool_test_key", "pool_test_value");
                System.out.println("获取值: " + jedis.get("pool_test_key"));
            }
            
            // 测试连接池状态
            System.out.println("连接池最大连接数: " + poolConfig.getMaxTotal());
            System.out.println("连接池最大空闲连接数: " + poolConfig.getMaxIdle());
        }
    }
    
    /**
     * 测试环境变量配置
     */
    public static void testEnvironmentVariables() {
        // 从环境变量读取配置
        String redisHost = System.getenv("REDIS_HOST");
        String redisPort = System.getenv("REDIS_PORT");
        String redisPassword = System.getenv("REDIS_PASSWORD");
        String redisDb = System.getenv("REDIS_DB");
        
        // 使用默认值
        if (redisHost == null) redisHost = "localhost";
        if (redisPort == null) redisPort = "6379";
        if (redisPassword == null) redisPassword = "";
        if (redisDb == null) redisDb = "0";
        
        System.out.println("Redis配置:");
        System.out.println("Host: " + redisHost);
        System.out.println("Port: " + redisPort);
        System.out.println("Password: " + (redisPassword.isEmpty() ? "无" : "有"));
        System.out.println("DB: " + redisDb);
        
        try (Jedis jedis = new Jedis(redisHost, Integer.parseInt(redisPort))) {
            // 如果有密码，进行认证
            if (!redisPassword.isEmpty()) {
                jedis.auth(redisPassword);
            }
            
            // 选择数据库
            jedis.select(Integer.parseInt(redisDb));
            
            System.out.println("环境变量配置连接成功: " + jedis.ping());
            
            // 测试基本命令
            jedis.set("env_test_key", "env_test_value");
            System.out.println("获取值: " + jedis.get("env_test_key"));
        }
    }
    
    /**
     * 测试Redis配置获取
     */
    public static void testRedisConfig() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            System.out.println("=== Redis配置信息 ===");
            
            // 获取服务器信息
            String info = jedis.info();
            System.out.println("服务器版本: " + extractInfo(info, "redis_version"));
            System.out.println("运行模式: " + extractInfo(info, "redis_mode"));
            System.out.println("内存使用: " + extractInfo(info, "used_memory_human"));
            
            // 获取配置信息
            System.out.println("\n=== 关键配置 ===");
            System.out.println("端口: " + jedis.configGet("port").get(1));
            System.out.println("绑定地址: " + jedis.configGet("bind").get(1));
            System.out.println("数据库数量: " + jedis.configGet("databases").get(1));
            System.out.println("最大内存: " + jedis.configGet("maxmemory").get(1));
            System.out.println("内存淘汰策略: " + jedis.configGet("maxmemory-policy").get(1));
        }
    }
    
    /**
     * 从INFO命令输出中提取指定信息
     */
    private static String extractInfo(String info, String key) {
        String[] lines = info.split("\n");
        for (String line : lines) {
            if (line.startsWith(key + ":")) {
                return line.substring(line.indexOf(":") + 1);
            }
        }
        return "未知";
    }
}
