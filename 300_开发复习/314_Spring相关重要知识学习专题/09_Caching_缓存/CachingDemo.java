package com.example.spring.caching;

import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.*;
import org.springframework.cache.concurrent.ConcurrentMapCacheManager;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableCaching;

import java.util.HashMap;
import java.util.Map;

/**
 * Spring 缓存示例
 */
public class CachingDemo {
    
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(CacheConfig.class);
        UserService userService = context.getBean(UserService.class);
        
        // 第一次调用，从数据库获取
        System.out.println("=== 第一次调用 getUser(1) ===");
        User user1 = userService.getUser(1);
        System.out.println("User: " + user1);
        
        // 第二次调用，从缓存获取
        System.out.println("\n=== 第二次调用 getUser(1) ===");
        User user2 = userService.getUser(1);
        System.out.println("User: " + user2);
        System.out.println("user1 == user2: " + (user1 == user2));
        
        // 更新用户，同时更新缓存
        System.out.println("\n=== 调用 updateUser ===");
        user1.setName("Alice Updated");
        User updatedUser = userService.updateUser(user1);
        System.out.println("Updated user: " + updatedUser);
        
        // 再次获取，从缓存获取更新后的数据
        System.out.println("\n=== 调用 getUser(1) 获取更新后的数据 ===");
        User user3 = userService.getUser(1);
        System.out.println("User: " + user3);
        
        // 删除用户，同时从缓存删除
        System.out.println("\n=== 调用 deleteUser(1) ===");
        userService.deleteUser(1);
        
        // 再次获取，从数据库获取（缓存已删除）
        System.out.println("\n=== 调用 getUser(1) 缓存已删除 ===");
        User user4 = userService.getUser(1);
        System.out.println("User: " + user4);
        System.out.println("user3 == user4: " + (user3 == user4));
        
        // 清空所有缓存
        System.out.println("\n=== 调用 clearCache() ===");
        userService.clearCache();
        
        context.close();
    }
}

/**
 * 缓存配置
 */
@Configuration
@EnableCaching
class CacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        ConcurrentMapCacheManager cacheManager = new ConcurrentMapCacheManager("users");
        return cacheManager;
    }
}

/**
 * 用户类
 */
class User {
    private int id;
    private String name;
    
    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "'}";
    }
}

/**
 * 用户服务
 */
@CacheConfig(cacheNames = "users")
class UserService {
    
    private final Map<Integer, User> userDatabase = new HashMap<>();
    
    public UserService() {
        // 初始化模拟数据库
        userDatabase.put(1, new User(1, "Alice"));
        userDatabase.put(2, new User(2, "Bob"));
        userDatabase.put(3, new User(3, "Charlie"));
    }
    
    /**
     * 获取用户（缓存）
     */
    @Cacheable(key = "#id")
    public User getUser(int id) {
        System.out.println("从数据库获取用户: " + id);
        return userDatabase.get(id);
    }
    
    /**
     * 更新用户（更新缓存）
     */
    @CachePut(key = "#user.id")
    public User updateUser(User user) {
        System.out.println("更新数据库用户: " + user.getId());
        userDatabase.put(user.getId(), user);
        return user;
    }
    
    /**
     * 删除用户（从缓存删除）
     */
    @CacheEvict(key = "#id")
    public void deleteUser(int id) {
        System.out.println("从数据库删除用户: " + id);
        userDatabase.remove(id);
    }
    
    /**
     * 清空缓存
     */
    @CacheEvict(allEntries = true)
    public void clearCache() {
        System.out.println("清空所有缓存");
    }
    
    /**
     * 条件缓存
     */
    @Cacheable(key = "#id", condition = "#id > 0")
    public User getValidUser(int id) {
        System.out.println("从数据库获取有效用户: " + id);
        return userDatabase.get(id);
    }
    
    /**
     * 除非条件缓存
     */
    @Cacheable(key = "#id", unless = "#result == null")
    public User getNotNullUser(int id) {
        System.out.println("从数据库获取非空用户: " + id);
        return userDatabase.get(id);
    }
    
    /**
     * 同步缓存
     */
    @Cacheable(key = "#id", sync = true)
    public User getSyncUser(int id) {
        System.out.println("从数据库获取同步用户: " + id);
        // 模拟耗时操作
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userDatabase.get(id);
    }
}

/**
 * 产品服务
 */
class ProductService {
    
    private final Map<Integer, String> productDatabase = new HashMap<>();
    
    public ProductService() {
        // 初始化模拟数据库
        productDatabase.put(1, "Product 1");
        productDatabase.put(2, "Product 2");
        productDatabase.put(3, "Product 3");
    }
    
    /**
     * 获取产品（缓存）
     */
    @Cacheable(value = "products", key = "#id")
    public String getProduct(int id) {
        System.out.println("从数据库获取产品: " + id);
        return productDatabase.get(id);
    }
    
    /**
     * 更新产品（更新缓存）
     */
    @CachePut(value = "products", key = "#id")
    public String updateProduct(int id, String name) {
        System.out.println("更新数据库产品: " + id);
        productDatabase.put(id, name);
        return name;
    }
    
    /**
     * 删除产品（从缓存删除）
     */
    @CacheEvict(value = "products", key = "#id")
    public void deleteProduct(int id) {
        System.out.println("从数据库删除产品: " + id);
        productDatabase.remove(id);
    }
}
