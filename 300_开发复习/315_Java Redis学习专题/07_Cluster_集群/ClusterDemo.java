package com.example.redis.cluster;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

import java.util.HashSet;
import java.util.Set;

/**
 * Redis 集群示例
 */
public class ClusterDemo {
    
    public static void main(String[] args) {
        // 测试集群连接
        System.out.println("=== 测试集群连接 ===");
        testClusterConnection();
        
        // 测试集群操作
        System.out.println("\n=== 测试集群操作 ===");
        testClusterOperations();
    }
    
    /**
     * 测试集群连接
     */
    public static void testClusterConnection() {
        // 集群节点集合
        Set<HostAndPort> nodes = new HashSet<>();
        nodes.add(new HostAndPort("localhost", 7000));
        nodes.add(new HostAndPort("localhost", 7001));
        nodes.add(new HostAndPort("localhost", 7002));
        nodes.add(new HostAndPort("localhost", 7003));
        nodes.add(new HostAndPort("localhost", 7004));
        nodes.add(new HostAndPort("localhost", 7005));
        
        // 创建集群连接
        try (JedisCluster jedisCluster = new JedisCluster(nodes)) {
            System.out.println("集群连接成功");
            
            // 测试连接
            System.out.println("集群状态: " + jedisCluster.ping());
            
            // 获取集群节点信息
            System.out.println("\n集群节点信息:");
            jedisCluster.getClusterNodes().forEach((nodeId, node) -> {
                System.out.println(nodeId + " -> " + node.getHost() + ":" + node.getPort() + " (" + (node.isMaster() ? "master" : "slave") + ")");
            });
        } catch (Exception e) {
            System.out.println("集群连接失败: " + e.getMessage());
            System.out.println("请确保Redis集群已启动并配置正确");
        }
    }
    
    /**
     * 测试集群操作
     */
    public static void testClusterOperations() {
        // 集群节点集合
        Set<HostAndPort> nodes = new HashSet<>();
        nodes.add(new HostAndPort("localhost", 7000));
        
        // 创建集群连接
        try (JedisCluster jedisCluster = new JedisCluster(nodes)) {
            System.out.println("集群操作测试");
            
            // 测试字符串操作
            System.out.println("\n=== 测试字符串操作 ===");
            jedisCluster.set("cluster_key", "cluster_value");
            System.out.println("设置字符串: " + jedisCluster.get("cluster_key"));
            
            // 测试哈希操作
            System.out.println("\n=== 测试哈希操作 ===");
            jedisCluster.hset("cluster_hash", "field1", "value1");
            jedisCluster.hset("cluster_hash", "field2", "value2");
            System.out.println("获取哈希字段: " + jedisCluster.hget("cluster_hash", "field1"));
            System.out.println("获取所有哈希字段: " + jedisCluster.hgetAll("cluster_hash"));
            
            // 测试列表操作
            System.out.println("\n=== 测试列表操作 ===");
            jedisCluster.lpush("cluster_list", "item1", "item2", "item3");
            System.out.println("获取列表长度: " + jedisCluster.llen("cluster_list"));
            System.out.println("获取列表元素: " + jedisCluster.lrange("cluster_list", 0, -1));
            
            // 测试集合操作
            System.out.println("\n=== 测试集合操作 ===");
            jedisCluster.sadd("cluster_set", "member1", "member2", "member3");
            System.out.println("获取集合大小: " + jedisCluster.scard("cluster_set"));
            System.out.println("获取集合元素: " + jedisCluster.smembers("cluster_set"));
            
            // 测试有序集合操作
            System.out.println("\n=== 测试有序集合操作 ===");
            jedisCluster.zadd("cluster_zset", 1, "member1");
            jedisCluster.zadd("cluster_zset", 2, "member2");
            jedisCluster.zadd("cluster_zset", 3, "member3");
            System.out.println("获取有序集合大小: " + jedisCluster.zcard("cluster_zset"));
            System.out.println("获取有序集合元素: " + jedisCluster.zrange("cluster_zset", 0, -1));
            
            // 测试键操作
            System.out.println("\n=== 测试键操作 ===");
            System.out.println("键是否存在: " + jedisCluster.exists("cluster_key"));
            System.out.println("设置过期时间: " + jedisCluster.expire("cluster_key", 60));
            System.out.println("获取剩余过期时间: " + jedisCluster.ttl("cluster_key"));
            
            // 测试批量操作
            System.out.println("\n=== 测试批量操作 ===");
            for (int i = 1; i <= 10; i++) {
                jedisCluster.set("batch_key_" + i, "value_" + i);
            }
            System.out.println("批量设置10个键值对");
            
            for (int i = 1; i <= 10; i++) {
                System.out.println("batch_key_" + i + ": " + jedisCluster.get("batch_key_" + i));
            }
        } catch (Exception e) {
            System.out.println("集群操作失败: " + e.getMessage());
        }
    }
    
    /**
     * 测试集群故障转移
     */
    public static void testClusterFailover() {
        // 集群节点集合
        Set<HostAndPort> nodes = new HashSet<>();
        nodes.add(new HostAndPort("localhost", 7000));
        
        // 创建集群连接
        try (JedisCluster jedisCluster = new JedisCluster(nodes)) {
            System.out.println("=== 测试集群故障转移 ===");
            
            // 获取当前集群状态
            System.out.println("当前集群状态:");
            jedisCluster.getClusterNodes().forEach((nodeId, node) -> {
                System.out.println(nodeId + " -> " + node.getHost() + ":" + node.getPort() + " (" + (node.isMaster() ? "master" : "slave") + ")");
            });
            
            // 模拟故障转移
            System.out.println("\n模拟故障转移...");
            System.out.println("请手动停止一个主节点，观察集群是否自动故障转移");
            System.out.println("按Enter键继续...");
            System.in.read();
            
            // 等待故障转移完成
            System.out.println("等待故障转移完成...");
            try {
                Thread.sleep(15000); // 等待15秒
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            // 获取新的集群状态
            System.out.println("\n故障转移后的集群状态:");
            jedisCluster.getClusterNodes().forEach((nodeId, node) -> {
                System.out.println(nodeId + " -> " + node.getHost() + ":" + node.getPort() + " (" + (node.isMaster() ? "master" : "slave") + ")");
            });
            
            // 测试操作
            System.out.println("\n测试故障转移后的操作:");
            System.out.println("读取数据: " + jedisCluster.get("cluster_key"));
            System.out.println("写入数据: " + jedisCluster.set("new_key", "new_value"));
            System.out.println("读取新数据: " + jedisCluster.get("new_key"));
        } catch (Exception e) {
            System.out.println("故障转移测试失败: " + e.getMessage());
        }
    }
}
