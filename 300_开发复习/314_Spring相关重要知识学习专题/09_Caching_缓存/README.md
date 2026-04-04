# Spring 缓存

## 1. 缓存概述

缓存是一种提高应用程序性能的重要技术，它通过存储频繁访问的数据，减少对底层数据源的访问次数。Spring框架提供了全面的缓存抽象，允许开发者轻松集成各种缓存实现，如EhCache、Redis、Caffeine等。

### 1.1 缓存的重要性

- **提高性能**：减少对数据库等慢速资源的访问
- **降低负载**：减轻底层系统的负担
- **改善用户体验**：加快响应速度
- **提高系统可靠性**：在底层系统暂时不可用时提供缓存数据

### 1.2 Spring缓存的核心概念

- **缓存抽象**：统一的缓存操作接口
- **缓存注解**：声明式缓存配置
- **缓存管理器**：管理缓存的生命周期
- **缓存存储**：实际存储缓存数据的组件

## 2. Spring缓存抽象

### 2.1 核心接口

- **Cache**：缓存接口，定义了缓存的基本操作
- **CacheManager**：缓存管理器，管理多个Cache实例
- **CacheResolver**：缓存解析器，决定使用哪个缓存
- **KeyGenerator**：缓存键生成器，生成缓存键

### 2.2 缓存操作

- **获取**：从缓存中获取数据
- **放入**：将数据放入缓存
- **删除**：从缓存中删除数据
- **清空**：清空缓存中的所有数据

## 3. 缓存注解

### 3.1 @EnableCaching

启用Spring的缓存支持：

```java
@Configuration
@EnableCaching
public class CacheConfig {
    // 缓存配置
}
```

### 3.2 @Cacheable

标记方法的结果应该被缓存：

```java
@Cacheable(value = "users", key = "#id")
public User getUser(int id) {
    // 从数据库获取用户
    return userRepository.findById(id);
}
```

### 3.3 @CachePut

更新缓存中的数据：

```java
@CachePut(value = "users", key = "#user.id")
public User updateUser(User user) {
    // 更新数据库
    return userRepository.save(user);
}
```

### 3.4 @CacheEvict

从缓存中删除数据：

```java
@CacheEvict(value = "users", key = "#id")
public void deleteUser(int id) {
    // 从数据库删除用户
    userRepository.deleteById(id);
}

@CacheEvict(value = "users", allEntries = true)
public void clearAllUsers() {
    // 清空所有用户
    userRepository.deleteAll();
}
```

### 3.5 @Caching

组合多个缓存操作：

```java
@Caching(
    cacheable = @Cacheable(value = "users", key = "#id"),
    evict = @CacheEvict(value = "userCounts", allEntries = true)
)
public User getUser(int id) {
    // 从数据库获取用户
    return userRepository.findById(id);
}
```

### 3.6 @CacheConfig

类级别的缓存配置：

```java
@CacheConfig(cacheNames = "users")
public class UserService {
    
    @Cacheable(key = "#id")
    public User getUser(int id) {
        // 从数据库获取用户
        return userRepository.findById(id);
    }
}
```

## 4. 缓存配置

### 4.1 简单缓存配置

```java
@Configuration
@EnableCaching
public class CacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        SimpleCacheManager cacheManager = new SimpleCacheManager();
        List<Cache> caches = new ArrayList<>();
        caches.add(new ConcurrentMapCache("users"));
        caches.add(new ConcurrentMapCache("products"));
        cacheManager.setCaches(caches);
        return cacheManager;
    }
}
```

### 4.2 使用Caffeine缓存

```java
@Configuration
@EnableCaching
public class CaffeineCacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        CaffeineCacheManager cacheManager = new CaffeineCacheManager("users", "products");
        cacheManager.setCaffeine(Caffeine.newBuilder()
            .expireAfterWrite(10, TimeUnit.MINUTES)
            .maximumSize(1000)
        );
        return cacheManager;
    }
}
```

### 4.3 使用Redis缓存

```java
@Configuration
@EnableCaching
public class RedisCacheConfig {
    
    @Bean
    public RedisConnectionFactory redisConnectionFactory() {
        return new LettuceConnectionFactory();
    }
    
    @Bean
    public CacheManager cacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(10))
            .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new Jackson2JsonRedisSerializer<>(Object.class)));
        
        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .build();
    }
}
```

## 5. 缓存键生成

### 5.1 默认键生成策略

Spring使用SimpleKeyGenerator生成缓存键：

- 无参数方法：使用SimpleKey.EMPTY
- 单个参数方法：使用参数值
- 多个参数方法：使用包含所有参数的SimpleKey

### 5.2 自定义键生成

```java
@Configuration
public class CacheConfig {
    
    @Bean
    public KeyGenerator customKeyGenerator() {
        return (target, method, params) -> {
            StringBuilder key = new StringBuilder();
            key.append(target.getClass().getName()).append(".");
            key.append(method.getName()).append("(");
            for (int i = 0; i < params.length; i++) {
                if (i > 0) {
                    key.append(", ");
                }
                key.append(params[i]);
            }
            key.append(")");
            return key.toString();
        };
    }
}
```

### 5.3 使用SpEL表达式

```java
@Cacheable(value = "users", key = "#id")
public User getUser(int id) {
    // 实现
}

@Cacheable(value = "users", key = "#user.id")
public User getUser(User user) {
    // 实现
}

@Cacheable(value = "users", key = "#root.methodName + #id")
public User getUser(int id) {
    // 实现
}
```

## 6. 缓存条件

### 6.1 条件缓存

使用condition属性：

```java
@Cacheable(value = "users", key = "#id", condition = "#id > 0")
public User getUser(int id) {
    // 实现
}
```

### 6.2 除非条件

使用unless属性：

```java
@Cacheable(value = "users", key = "#id", unless = "#result == null")
public User getUser(int id) {
    // 实现
}
```

## 7. 缓存同步

### 7.1 同步缓存

使用sync属性：

```java
@Cacheable(value = "users", key = "#id", sync = true)
public User getUser(int id) {
    // 实现
}
```

### 7.2 缓存锁

对于缓存未命中的情况，sync=true会确保只有一个线程执行方法，其他线程等待结果，避免缓存击穿。

## 8. 缓存实现

### 8.1 内置缓存

- **ConcurrentMapCache**：基于ConcurrentHashMap的内存缓存
- **SimpleCacheManager**：管理多个ConcurrentMapCache

### 8.2 第三方缓存

- **Caffeine**：高性能的Java内存缓存库
- **EhCache**：成熟的Java缓存库
- **Redis**：分布式缓存
- **Hazelcast**：分布式内存数据网格
- **Infinispan**：分布式缓存和数据网格

## 9. 缓存最佳实践

### 9.1 缓存设计

- **缓存策略**：选择合适的缓存策略（如LRU、LFU）
- **过期时间**：设置合理的缓存过期时间
- **缓存大小**：限制缓存大小，避免内存溢出
- **缓存键设计**：使用唯一、稳定的缓存键

### 9.2 缓存使用

- **缓存热点数据**：只缓存频繁访问的数据
- **避免缓存大数据**：避免缓存过大的数据
- **合理设置过期时间**：根据数据变化频率设置过期时间
- **考虑缓存一致性**：确保缓存与数据源的一致性

### 9.3 性能优化

- **批量操作**：使用批量操作减少缓存访问次数
- **缓存预热**：在应用启动时预热缓存
- **缓存监控**：监控缓存命中率和性能
- **缓存降级**：在缓存不可用时降级到原始数据源

### 9.4 缓存一致性

- **更新策略**：更新数据时同时更新缓存
- **过期策略**：使用合理的过期策略
- **事件驱动**：使用事件驱动的方式更新缓存
- **分布式锁**：在分布式环境中使用分布式锁确保一致性

## 10. 缓存的挑战

### 10.1 缓存一致性

- **问题**：缓存与数据源不同步
- **解决方案**：使用@CachePut、@CacheEvict，或实现事件驱动的更新

### 10.2 缓存穿透

- **问题**：查询不存在的数据，导致每次都访问数据源
- **解决方案**：缓存空结果，使用布隆过滤器

### 10.3 缓存击穿

- **问题**：热点数据过期，导致大量请求同时访问数据源
- **解决方案**：使用sync=true，设置永不过期的热点数据

### 10.4 缓存雪崩

- **问题**：大量缓存同时过期，导致系统压力骤增
- **解决方案**：使用随机过期时间，分级缓存

### 10.5 内存消耗

- **问题**：缓存占用过多内存
- **解决方案**：设置合理的缓存大小，使用过期策略

## 11. 总结

Spring缓存是Spring框架的重要特性，它通过提供统一的缓存抽象，使开发者能够轻松集成各种缓存实现，提高应用程序的性能和可靠性。理解Spring缓存的核心概念和最佳实践，对于构建高性能的Spring应用至关重要。

本章节介绍了Spring缓存的核心概念、缓存注解、缓存配置、缓存键生成、缓存条件、缓存同步、缓存实现等内容，以及缓存的最佳实践和挑战。通过学习这些知识，开发者可以更有效地使用Spring缓存，构建高质量的Spring应用。