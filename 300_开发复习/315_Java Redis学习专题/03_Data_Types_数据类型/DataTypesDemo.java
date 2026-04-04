package com.example.redis.datatypes;

import redis.clients.jedis.Jedis;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Redis 数据类型示例
 */
public class DataTypesDemo {
    
    public static void main(String[] args) {
        try (Jedis jedis = new Jedis("localhost", 6379)) {
            // 测试字符串类型
            System.out.println("=== 测试字符串类型 ===");
            testString(jedis);
            
            // 测试列表类型
            System.out.println("\n=== 测试列表类型 ===");
            testList(jedis);
            
            // 测试集合类型
            System.out.println("\n=== 测试集合类型 ===");
            testSet(jedis);
            
            // 测试哈希类型
            System.out.println("\n=== 测试哈希类型 ===");
            testHash(jedis);
            
            // 测试有序集合类型
            System.out.println("\n=== 测试有序集合类型 ===");
            testSortedSet(jedis);
            
            // 测试位图类型
            System.out.println("\n=== 测试位图类型 ===");
            testBitMap(jedis);
            
            // 测试HyperLogLog类型
            System.out.println("\n=== 测试HyperLogLog类型 ===");
            testHyperLogLog(jedis);
            
            // 测试Geo类型
            System.out.println("\n=== 测试Geo类型 ===");
            testGeo(jedis);
        }
    }
    
    /**
     * 测试字符串类型
     */
    public static void testString(Jedis jedis) {
        // 设置字符串
        jedis.set("string_key", "Hello Redis");
        System.out.println("获取字符串: " + jedis.get("string_key"));
        
        // 追加字符串
        jedis.append("string_key", " World");
        System.out.println("追加后字符串: " + jedis.get("string_key"));
        
        // 获取字符串长度
        System.out.println("字符串长度: " + jedis.strlen("string_key"));
        
        // 自增
        jedis.set("counter", "0");
        jedis.incr("counter");
        System.out.println("自增后: " + jedis.get("counter"));
        
        // 自增指定值
        jedis.incrBy("counter", 5);
        System.out.println("自增指定值后: " + jedis.get("counter"));
        
        // 自减
        jedis.decr("counter");
        System.out.println("自减后: " + jedis.get("counter"));
        
        // 同时设置多个键值对
        jedis.mset("key1", "value1", "key2", "value2", "key3", "value3");
        System.out.println("同时获取多个值: " + jedis.mget("key1", "key2", "key3"));
        
        // 设置过期时间
        jedis.setex("expire_key", 10, "expire_value");
        System.out.println("过期时间键的值: " + jedis.get("expire_key"));
        System.out.println("过期时间键的TTL: " + jedis.ttl("expire_key"));
    }
    
    /**
     * 测试列表类型
     */
    public static void testList(Jedis jedis) {
        // 清空列表
        jedis.del("list_key");
        
        // 左侧插入
        jedis.lpush("list_key", "item1", "item2", "item3");
        System.out.println("左侧插入后列表: " + jedis.lrange("list_key", 0, -1));
        
        // 右侧插入
        jedis.rpush("list_key", "item4", "item5");
        System.out.println("右侧插入后列表: " + jedis.lrange("list_key", 0, -1));
        
        // 获取列表长度
        System.out.println("列表长度: " + jedis.llen("list_key"));
        
        // 获取指定索引的元素
        System.out.println("索引为2的元素: " + jedis.lindex("list_key", 2));
        
        // 左侧弹出
        System.out.println("左侧弹出: " + jedis.lpop("list_key"));
        System.out.println("左侧弹出后列表: " + jedis.lrange("list_key", 0, -1));
        
        // 右侧弹出
        System.out.println("右侧弹出: " + jedis.rpop("list_key"));
        System.out.println("右侧弹出后列表: " + jedis.lrange("list_key", 0, -1));
        
        // 移除指定值
        jedis.lrem("list_key", 1, "item2");
        System.out.println("移除item2后列表: " + jedis.lrange("list_key", 0, -1));
        
        // 截取列表
        jedis.ltrim("list_key", 0, 1);
        System.out.println("截取后列表: " + jedis.lrange("list_key", 0, -1));
    }
    
    /**
     * 测试集合类型
     */
    public static void testSet(Jedis jedis) {
        // 清空集合
        jedis.del("set_key");
        
        // 添加元素
        jedis.sadd("set_key", "member1", "member2", "member3", "member4");
        System.out.println("集合元素: " + jedis.smembers("set_key"));
        
        // 获取集合大小
        System.out.println("集合大小: " + jedis.scard("set_key"));
        
        // 检查元素是否在集合中
        System.out.println("member1是否在集合中: " + jedis.sismember("set_key", "member1"));
        System.out.println("member5是否在集合中: " + jedis.sismember("set_key", "member5"));
        
        // 移除元素
        jedis.srem("set_key", "member2");
        System.out.println("移除member2后集合: " + jedis.smembers("set_key"));
        
        // 随机获取元素
        System.out.println("随机获取一个元素: " + jedis.srandmember("set_key"));
        System.out.println("随机获取两个元素: " + jedis.srandmember("set_key", 2));
        
        // 随机弹出元素
        System.out.println("随机弹出一个元素: " + jedis.spop("set_key"));
        System.out.println("弹出后集合: " + jedis.smembers("set_key"));
        
        // 测试集合运算
        jedis.sadd("set_key1", "a", "b", "c");
        jedis.sadd("set_key2", "b", "c", "d");
        System.out.println("set_key1: " + jedis.smembers("set_key1"));
        System.out.println("set_key2: " + jedis.smembers("set_key2"));
        System.out.println("交集: " + jedis.sinter("set_key1", "set_key2"));
        System.out.println("并集: " + jedis.sunion("set_key1", "set_key2"));
        System.out.println("差集: " + jedis.sdiff("set_key1", "set_key2"));
    }
    
    /**
     * 测试哈希类型
     */
    public static void testHash(Jedis jedis) {
        // 清空哈希
        jedis.del("hash_key");
        
        // 设置字段
        jedis.hset("hash_key", "field1", "value1");
        jedis.hset("hash_key", "field2", "value2");
        jedis.hset("hash_key", "field3", "value3");
        
        // 获取字段值
        System.out.println("field1的值: " + jedis.hget("hash_key", "field1"));
        
        // 同时设置多个字段
        jedis.hmset("hash_key", Map.of("field4", "value4", "field5", "value5"));
        
        // 同时获取多个字段值
        System.out.println("多个字段的值: " + jedis.hmget("hash_key", "field1", "field2", "field3"));
        
        // 获取所有字段和值
        System.out.println("所有字段和值: " + jedis.hgetAll("hash_key"));
        
        // 获取所有字段
        System.out.println("所有字段: " + jedis.hkeys("hash_key"));
        
        // 获取所有值
        System.out.println("所有值: " + jedis.hvals("hash_key"));
        
        // 获取字段数量
        System.out.println("字段数量: " + jedis.hlen("hash_key"));
        
        // 检查字段是否存在
        System.out.println("field1是否存在: " + jedis.hexists("hash_key", "field1"));
        System.out.println("field6是否存在: " + jedis.hexists("hash_key", "field6"));
        
        // 删除字段
        jedis.hdel("hash_key", "field1", "field2");
        System.out.println("删除字段后所有字段和值: " + jedis.hgetAll("hash_key"));
        
        // 字段值自增
        jedis.hset("hash_key", "counter", "0");
        jedis.hincrBy("hash_key", "counter", 1);
        System.out.println("counter自增后: " + jedis.hget("hash_key", "counter"));
    }
    
    /**
     * 测试有序集合类型
     */
    public static void testSortedSet(Jedis jedis) {
        // 清空有序集合
        jedis.del("zset_key");
        
        // 添加元素
        jedis.zadd("zset_key", 1, "member1");
        jedis.zadd("zset_key", 2, "member2");
        jedis.zadd("zset_key", 3, "member3");
        jedis.zadd("zset_key", 4, "member4");
        jedis.zadd("zset_key", 5, "member5");
        
        // 获取元素分数
        System.out.println("member3的分数: " + jedis.zscore("zset_key", "member3"));
        
        // 获取有序集合大小
        System.out.println("有序集合大小: " + jedis.zcard("zset_key"));
        
        // 按分数递增顺序获取元素
        System.out.println("按分数递增顺序获取元素: " + jedis.zrange("zset_key", 0, -1));
        
        // 按分数递减顺序获取元素
        System.out.println("按分数递减顺序获取元素: " + jedis.zrevrange("zset_key", 0, -1));
        
        // 按分数范围获取元素
        System.out.println("分数在2到4之间的元素: " + jedis.zrangeByScore("zset_key", 2, 4));
        
        // 获取元素排名（递增）
        System.out.println("member3的排名（递增）: " + jedis.zrank("zset_key", "member3"));
        
        // 获取元素排名（递减）
        System.out.println("member3的排名（递减）: " + jedis.zrevrank("zset_key", "member3"));
        
        // 元素分数自增
        jedis.zincrby("zset_key", 1, "member3");
        System.out.println("member3分数自增后: " + jedis.zscore("zset_key", "member3"));
        
        // 移除元素
        jedis.zrem("zset_key", "member5");
        System.out.println("移除member5后元素: " + jedis.zrange("zset_key", 0, -1));
    }
    
    /**
     * 测试位图类型
     */
    public static void testBitMap(Jedis jedis) {
        // 清空位图
        jedis.del("bitmap_key");
        
        // 设置位
        jedis.setbit("bitmap_key", 0, true);
        jedis.setbit("bitmap_key", 1, false);
        jedis.setbit("bitmap_key", 2, true);
        jedis.setbit("bitmap_key", 3, true);
        
        // 获取位
        System.out.println("位0的值: " + jedis.getbit("bitmap_key", 0));
        System.out.println("位1的值: " + jedis.getbit("bitmap_key", 1));
        System.out.println("位2的值: " + jedis.getbit("bitmap_key", 2));
        
        // 统计值为1的位的数量
        System.out.println("值为1的位的数量: " + jedis.bitcount("bitmap_key"));
        
        // 查找第一个值为1的位
        System.out.println("第一个值为1的位的位置: " + jedis.bitpos("bitmap_key", true));
        
        // 查找第一个值为0的位
        System.out.println("第一个值为0的位的位置: " + jedis.bitpos("bitmap_key", false));
    }
    
    /**
     * 测试HyperLogLog类型
     */
    public static void testHyperLogLog(Jedis jedis) {
        // 清空HyperLogLog
        jedis.del("hll_key");
        
        // 添加元素
        jedis.pfadd("hll_key", "element1", "element2", "element3", "element4", "element5");
        
        // 统计基数
        System.out.println("基数估计值: " + jedis.pfcount("hll_key"));
        
        // 添加更多元素
        jedis.pfadd("hll_key", "element6", "element7", "element8", "element9", "element10");
        System.out.println("添加更多元素后基数估计值: " + jedis.pfcount("hll_key"));
        
        // 合并HyperLogLog
        jedis.pfadd("hll_key1", "a", "b", "c");
        jedis.pfadd("hll_key2", "c", "d", "e");
        jedis.pfmerge("hll_merged", "hll_key1", "hll_key2");
        System.out.println("合并后基数估计值: " + jedis.pfcount("hll_merged"));
    }
    
    /**
     * 测试Geo类型
     */
    public static void testGeo(Jedis jedis) {
        // 清空Geo集合
        jedis.del("geo_key");
        
        // 添加地理位置
        jedis.geoadd("geo_key", 116.404, 39.915, "北京");
        jedis.geoadd("geo_key", 121.473, 31.230, "上海");
        jedis.geoadd("geo_key", 113.264, 23.129, "广州");
        jedis.geoadd("geo_key", 114.057, 22.543, "深圳");
        
        // 获取地理位置
        System.out.println("北京的经纬度: " + jedis.geopos("geo_key", "北京"));
        
        // 计算距离
        System.out.println("北京到上海的距离: " + jedis.geodist("geo_key", "北京", "上海", "km") + " km");
        
        // 获取地理位置的哈希表示
        System.out.println("北京的哈希表示: " + jedis.geohash("geo_key", "北京"));
        
        // 获取指定范围内的地理位置
        System.out.println("北京周围1000km内的城市: " + jedis.georadius("geo_key", 116.404, 39.915, 1000, "km"));
        
        // 获取指定元素周围范围内的地理位置
        System.out.println("上海周围1000km内的城市: " + jedis.georadiusbymember("geo_key", "上海", 1000, "km"));
    }
}
