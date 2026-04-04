package com.example.redis.spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableCaching;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.io.Serializable;
import java.time.Duration;

/**
 * Redis 与 Spring 集成示例
 */
public class SpringIntegrationDemo {
    
    public static void main(String[] args) {
        // 创建Spring容器
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(RedisConfig.class);
        
        // 测试RedisTemplate
        System.out.println("=== 测试RedisTemplate ===");
        RedisTemplate<String, Object> redisTemplate = context.getBean(RedisTemplate.class);
        testRedisTemplate(redisTemplate);
        
        // 测试StringRedisTemplate
        System.out.println("\n=== 测试StringRedisTemplate ===");
        StringRedisTemplate stringRedisTemplate = context.getBean(StringRedisTemplate.class);
        testStringRedisTemplate(stringRedisTemplate);
        
        // 测试缓存注解
        System.out.println("\n=== 测试缓存注解 ===");
        UserService userService = context.getBean(UserService.class);
        testCacheAnnotation(userService);
        
        // 关闭容器
        context.close();
    }
    
    /**
     * 测试RedisTemplate
     */
    public static void testRedisTemplate(RedisTemplate<String, Object> redisTemplate) {
        // 测试字符串操作
        System.out.println("\n=== 测试字符串操作 ===");
        redisTemplate.opsForValue().set("redis_template_key", "redis_template_value");
        System.out.println("获取字符串: " + redisTemplate.opsForValue().get("redis_template_key"));
        
        // 测试哈希操作
        System.out.println("\n=== 测试哈希操作 ===");
        redisTemplate.opsForHash().put("redis_template_hash", "field1", "value1");
        redisTemplate.opsForHash().put("redis_template_hash", "field2", "value2");
        System.out.println("获取哈希字段: " + redisTemplate.opsForHash().get("redis_template_hash", "field1"));
        System.out.println("获取所有哈希字段: " + redisTemplate.opsForHash().entries("redis_template_hash"));
        
        // 测试列表操作
        System.out.println("\n=== 测试列表操作 ===");
        redisTemplate.opsForList().leftPush("redis_template_list", "item1");
        redisTemplate.opsForList().leftPush("redis_template_list", "item2");
        redisTemplate.opsForList().leftPush("redis_template_list", "item3");
        System.out.println("获取列表长度: " + redisTemplate.opsForList().size("redis_template_list"));
        System.out.println("获取列表元素: " + redisTemplate.opsForList().range("redis_template_list", 0, -1));
        
        // 测试集合操作
        System.out.println("\n=== 测试集合操作 ===");
        redisTemplate.opsForSet().add("redis_template_set", "member1", "member2", "member3");
        System.out.println("获取集合大小: " + redisTemplate.opsForSet().size("redis_template_set"));
        System.out.println("获取集合元素: " + redisTemplate.opsForSet().members("redis_template_set"));
        
        // 测试有序集合操作
        System.out.println("\n=== 测试有序集合操作 ===");
        redisTemplate.opsForZSet().add("redis_template_zset", "member1", 1.0);
        redisTemplate.opsForZSet().add("redis_template_zset", "member2", 2.0);
        redisTemplate.opsForZSet().add("redis_template_zset", "member3", 3.0);
        System.out.println("获取有序集合大小: " + redisTemplate.opsForZSet().size("redis_template_zset"));
        System.out.println("获取有序集合元素: " + redisTemplate.opsForZSet().range("redis_template_zset", 0, -1));
        
        // 测试对象序列化
        System.out.println("\n=== 测试对象序列化 ===");
        User user = new User(1L, "Alice", "alice@example.com");
        redisTemplate.opsForValue().set("redis_template_user", user);
        User savedUser = (User) redisTemplate.opsForValue().get("redis_template_user");
        System.out.println("获取保存的用户: " + savedUser);
    }
    
    /**
     * 测试StringRedisTemplate
     */
    public static void testStringRedisTemplate(StringRedisTemplate stringRedisTemplate) {
        // 测试字符串操作
        stringRedisTemplate.opsForValue().set("string_template_key", "string_template_value");
        System.out.println("获取字符串: " + stringRedisTemplate.opsForValue().get("string_template_key"));
        
        // 测试哈希操作
        stringRedisTemplate.opsForHash().put("string_template_hash", "field1", "value1");
        stringRedisTemplate.opsForHash().put("string_template_hash", "field2", "value2");
        System.out.println("获取哈希字段: " + stringRedisTemplate.opsForHash().get("string_template_hash", "field1"));
        
        // 测试列表操作
        stringRedisTemplate.opsForList().leftPush("string_template_list", "item1");
        stringRedisTemplate.opsForList().leftPush("string_template_list", "item2");
        System.out.println("获取列表元素: " + stringRedisTemplate.opsForList().range("string_template_list", 0, -1));
    }
    
    /**
     * 测试缓存注解
     */
    public static void testCacheAnnotation(UserService userService) {
        // 第一次调用，从数据库获取
        System.out.println("第一次调用getUser(1)");
        User user1 = userService.getUser(1L);
        System.out.println("获取用户: " + user1);
        
        // 第二次调用，从缓存获取
        System.out.println("\n第二次调用getUser(1)");
        User user2 = userService.getUser(1L);
        System.out.println("获取用户: " + user2);
        System.out.println("user1 == user2: " + (user1 == user2));
        
        // 更新用户，同时更新缓存
        System.out.println("\n调用updateUser");
        user1.setName("Alice Updated");
        User updatedUser = userService.updateUser(user1);
        System.out.println("更新后的用户: " + updatedUser);
        
        // 再次获取，从缓存获取更新后的数据
        System.out.println("\n第三次调用getUser(1)");
        User user3 = userService.getUser(1L);
        System.out.println("获取用户: " + user3);
        
        // 删除用户，同时从缓存删除
        System.out.println("\n调用deleteUser(1)");
        userService.deleteUser(1L);
        
        // 再次获取，从数据库获取（缓存已删除）
        System.out.println("\n第四次调用getUser(1)");
        User user4 = userService.getUser(1L);
        System.out.println("获取用户: " + user4);
    }
}

/**
 * Redis配置类
 */
@Configuration
@EnableCaching
class RedisConfig {
    
    @Bean
    public RedisConnectionFactory redisConnectionFactory() {
        JedisConnectionFactory factory = new JedisConnectionFactory();
        factory.setHostName("localhost");
        factory.setPort(6379);
        factory.setPassword("");
        factory.setDatabase(0);
        return factory;
    }
    
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new Jackson2JsonRedisSerializer<>(Object.class));
        template.setHashKeySerializer(new StringRedisSerializer());
        template.setHashValueSerializer(new Jackson2JsonRedisSerializer<>(Object.class));
        return template;
    }
    
    @Bean
    public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory connectionFactory) {
        return new StringRedisTemplate(connectionFactory);
    }
    
    @Bean
    public UserService userService() {
        return new UserService();
    }
}

/**
 * 用户类
 */
class User implements Serializable {
    private Long id;
    private String name;
    private String email;
    
    public User() {
    }
    
    public User(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "', email='" + email + "'}";
    }
}

/**
 * 用户服务
 */
class UserService {
    
    // 模拟数据库
    private User getUserFromDatabase(Long id) {
        System.out.println("从数据库获取用户: " + id);
        // 模拟数据库查询
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return new User(id, "Alice", "alice@example.com");
    }
    
    /**
     * 获取用户（缓存）
     */
    @Cacheable(value = "users", key = "#id")
    public User getUser(Long id) {
        return getUserFromDatabase(id);
    }
    
    /**
     * 更新用户（更新缓存）
     */
    @org.springframework.cache.annotation.CachePut(value = "users", key = "#user.id")
    public User updateUser(User user) {
        System.out.println("更新数据库用户: " + user.getId());
        // 模拟数据库更新
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return user;
    }
    
    /**
     * 删除用户（从缓存删除）
     */
    @org.springframework.cache.annotation.CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        System.out.println("从数据库删除用户: " + id);
        // 模拟数据库删除
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
