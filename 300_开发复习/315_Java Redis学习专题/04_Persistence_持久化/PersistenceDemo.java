package com.example.redis.persistence;

import redis.clients.jedis.Jedis;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Redis 持久化示例
 */
public class PersistenceDemo {
    
    public static void main(String[] args) {
        // 测试RDB持久化
        System.out.println("=== 测试RDB持久化 ===");
        testRDBPersistence();
        
        // 测试AOF持久化
        System.out.println("\n=== 测试AOF持久化 ===");
        testAOFPersistence();
        
        // 测试持久化配置
        System.out.println("\n=== 测试持久化配置 ===");
        testPersistenceConfig();
    }
    
    /**
     * 测试RDB持久化
     */
    public static void testRDBPersistence() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 设置一些数据
            jedis.set("rdb_key1", "rdb_value1");
            jedis.set("rdb_key2", "rdb_value2");
            jedis.set("rdb_key3", "rdb_value3");
            
            System.out.println("设置的数据:");
            System.out.println("rdb_key1: " + jedis.get("rdb_key1"));
            System.out.println("rdb_key2: " + jedis.get("rdb_key2"));
            System.out.println("rdb_key3: " + jedis.get("rdb_key3"));
            
            // 手动触发BGSAVE
            System.out.println("\n手动触发BGSAVE...");
            String bgsaveResult = jedis.bgsave();
            System.out.println("BGSAVE结果: " + bgsaveResult);
            
            // 等待BGSAVE完成
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            // 检查RDB文件是否存在
            File rdbFile = new File("dump.rdb");
            if (rdbFile.exists()) {
                System.out.println("RDB文件已生成，大小: " + rdbFile.length() + " bytes");
            } else {
                System.out.println("RDB文件未生成");
            }
            
            // 删除测试数据
            jedis.del("rdb_key1", "rdb_key2", "rdb_key3");
            System.out.println("\n删除数据后:");
            System.out.println("rdb_key1: " + jedis.get("rdb_key1"));
            System.out.println("rdb_key2: " + jedis.get("rdb_key2"));
            System.out.println("rdb_key3: " + jedis.get("rdb_key3"));
            
            // 注意：要测试RDB恢复，需要重启Redis服务器
            System.out.println("\n要测试RDB恢复，请重启Redis服务器，然后再次运行此程序查看数据是否恢复");
        }
    }
    
    /**
     * 测试AOF持久化
     */
    public static void testAOFPersistence() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 检查AOF是否启用
            String appendonly = jedis.configGet("appendonly").get(1);
            System.out.println("AOF是否启用: " + appendonly);
            
            if ("yes".equals(appendonly)) {
                // 设置一些数据
                jedis.set("aof_key1", "aof_value1");
                jedis.set("aof_key2", "aof_value2");
                jedis.set("aof_key3", "aof_value3");
                
                System.out.println("设置的数据:");
                System.out.println("aof_key1: " + jedis.get("aof_key1"));
                System.out.println("aof_key2: " + jedis.get("aof_key2"));
                System.out.println("aof_key3: " + jedis.get("aof_key3"));
                
                // 手动触发AOF重写
                System.out.println("\n手动触发AOF重写...");
                String bgrewriteaofResult = jedis.bgrewriteaof();
                System.out.println("BGREWRITEAOF结果: " + bgrewriteaofResult);
                
                // 等待AOF重写完成
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                
                // 检查AOF文件是否存在
                File aofFile = new File("appendonly.aof");
                if (aofFile.exists()) {
                    System.out.println("AOF文件已生成，大小: " + aofFile.length() + " bytes");
                } else {
                    System.out.println("AOF文件未生成");
                }
                
                // 删除测试数据
                jedis.del("aof_key1", "aof_key2", "aof_key3");
                System.out.println("\n删除数据后:");
                System.out.println("aof_key1: " + jedis.get("aof_key1"));
                System.out.println("aof_key2: " + jedis.get("aof_key2"));
                System.out.println("aof_key3: " + jedis.get("aof_key3"));
                
                // 注意：要测试AOF恢复，需要重启Redis服务器
                System.out.println("\n要测试AOF恢复，请重启Redis服务器，然后再次运行此程序查看数据是否恢复");
            } else {
                System.out.println("AOF未启用，请在redis.conf中设置appendonly yes来启用AOF");
            }
        }
    }
    
    /**
     * 测试持久化配置
     */
    public static void testPersistenceConfig() {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            System.out.println("=== RDB配置 ===");
            // 获取RDB配置
            System.out.println("dbfilename: " + jedis.configGet("dbfilename").get(1));
            System.out.println("dir: " + jedis.configGet("dir").get(1));
            System.out.println("rdbcompression: " + jedis.configGet("rdbcompression").get(1));
            System.out.println("rdbchecksum: " + jedis.configGet("rdbchecksum").get(1));
            
            System.out.println("\n=== AOF配置 ===");
            // 获取AOF配置
            System.out.println("appendonly: " + jedis.configGet("appendonly").get(1));
            System.out.println("appendfilename: " + jedis.configGet("appendfilename").get(1));
            System.out.println("appendfsync: " + jedis.configGet("appendfsync").get(1));
            System.out.println("no-appendfsync-on-rewrite: " + jedis.configGet("no-appendfsync-on-rewrite").get(1));
            System.out.println("auto-aof-rewrite-percentage: " + jedis.configGet("auto-aof-rewrite-percentage").get(1));
            System.out.println("auto-aof-rewrite-min-size: " + jedis.configGet("auto-aof-rewrite-min-size").get(1));
            
            // 测试修改AOF同步策略
            System.out.println("\n=== 测试修改AOF同步策略 ===");
            System.out.println("修改前appendfsync: " + jedis.configGet("appendfsync").get(1));
            
            // 注意：在生产环境中，应该在配置文件中修改，而不是使用config set
            // jedis.configSet("appendfsync", "everysec");
            // System.out.println("修改后appendfsync: " + jedis.configGet("appendfsync").get(1));
            
            System.out.println("\n=== 持久化文件信息 ===");
            // 检查持久化文件
            checkPersistenceFiles();
        }
    }
    
    /**
     * 检查持久化文件
     */
    private static void checkPersistenceFiles() {
        // 检查RDB文件
        File rdbFile = new File("dump.rdb");
        if (rdbFile.exists()) {
            System.out.println("RDB文件:");
            System.out.println("  名称: " + rdbFile.getName());
            System.out.println("  大小: " + rdbFile.length() + " bytes");
            System.out.println("  路径: " + rdbFile.getAbsolutePath());
        } else {
            System.out.println("RDB文件不存在");
        }
        
        // 检查AOF文件
        File aofFile = new File("appendonly.aof");
        if (aofFile.exists()) {
            System.out.println("\nAOF文件:");
            System.out.println("  名称: " + aofFile.getName());
            System.out.println("  大小: " + aofFile.length() + " bytes");
            System.out.println("  路径: " + aofFile.getAbsolutePath());
            
            // 读取AOF文件的前几行
            try {
                Path path = Paths.get(aofFile.getAbsolutePath());
                System.out.println("\nAOF文件前5行:");
                Files.lines(path).limit(5).forEach(System.out::println);
            } catch (IOException e) {
                System.out.println("读取AOF文件失败: " + e.getMessage());
            }
        } else {
            System.out.println("AOF文件不存在");
        }
    }
}
