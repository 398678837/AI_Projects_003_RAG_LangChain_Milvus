# MyBatis 缓存机制

## 缓存概述

MyBatis 提供了强大的缓存机制，用于提高查询性能。缓存可以减少数据库查询次数，提高应用程序的响应速度。MyBatis 支持一级缓存和二级缓存。

## 1. 一级缓存

### 1.1 一级缓存概述

一级缓存是 SqlSession 级别的缓存，默认开启。当使用同一个 SqlSession 执行多次相同的 SQL 语句时，第一次执行会将结果缓存，后续执行会直接从缓存中获取，而不会再次查询数据库。

### 1.2 一级缓存工作原理

1. 当执行查询操作时，MyBatis 会先检查一级缓存中是否存在该查询结果。
2. 如果存在，直接返回缓存中的结果。
3. 如果不存在，执行 SQL 查询，将结果存入一级缓存，然后返回结果。
4. 当执行增删改操作时，一级缓存会被清空，以保证数据的一致性。

### 1.3 一级缓存示例

```java
SqlSession sqlSession = sqlSessionFactory.openSession();
UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

// 第一次查询，从数据库获取
User user1 = userMapper.getUserById(1);
System.out.println(user1);

// 第二次查询，从一级缓存获取
User user2 = userMapper.getUserById(1);
System.out.println(user2);

// 执行更新操作，清空一级缓存
userMapper.updateUser(new User(1, "张三", "123456"));
sqlSession.commit();

// 第三次查询，从数据库获取（因为缓存已清空）
User user3 = userMapper.getUserById(1);
System.out.println(user3);

sqlSession.close();
```

### 1.4 一级缓存配置

一级缓存默认开启，不需要额外配置。但可以通过以下方式关闭一级缓存：

```xml
<settings>
    <setting name="localCacheScope" value="STATEMENT"/>
</settings>
```

其中，`localCacheScope` 的值可以是：
- `SESSION`：默认值，缓存会话中的所有查询
- `STATEMENT`：缓存单个语句，即关闭一级缓存

## 2. 二级缓存

### 2.1 二级缓存概述

二级缓存是 Mapper 级别的缓存，默认关闭。当多个 SqlSession 执行相同的 SQL 语句时，第一次执行会将结果缓存，后续执行会直接从缓存中获取，而不会再次查询数据库。

### 2.2 二级缓存工作原理

1. 当执行查询操作时，MyBatis 会先检查二级缓存中是否存在该查询结果。
2. 如果存在，直接返回缓存中的结果。
3. 如果不存在，检查一级缓存中是否存在该查询结果。
4. 如果一级缓存中存在，返回一级缓存中的结果。
5. 如果一级缓存中也不存在，执行 SQL 查询，将结果存入一级缓存和二级缓存，然后返回结果。
6. 当执行增删改操作时，二级缓存会被清空，以保证数据的一致性。

### 2.3 二级缓存配置

#### 2.3.1 开启二级缓存

在 MyBatis 配置文件中开启二级缓存：

```xml
<settings>
    <setting name="cacheEnabled" value="true"/>
</settings>
```

#### 2.3.2 在 Mapper XML 中配置二级缓存

```xml
<mapper namespace="com.example.mapper.UserMapper">
    <!-- 配置二级缓存 -->
    <cache
        eviction="LRU"
        flushInterval="60000"
        size="1024"
        readOnly="false"/>
    
    <!-- SQL 语句 -->
</mapper>
```

其中，`cache` 标签的属性含义如下：
- `eviction`：缓存淘汰策略，可选值有 LRU（默认）、FIFO、SOFT、WEAK
- `flushInterval`：缓存刷新间隔，单位毫秒
- `size`：缓存大小，默认 1024
- `readOnly`：是否只读，默认 false

#### 2.3.3 在 Mapper 接口中配置二级缓存

在 Mapper 接口上使用 `@CacheNamespace` 注解：

```java
@CacheNamespace(eviction = LruCache.class, flushInterval = 60000, size = 1024, readWrite = true)
public interface UserMapper {
    // 方法定义
}
```

### 2.4 二级缓存示例

```java
// 第一个 SqlSession
SqlSession sqlSession1 = sqlSessionFactory.openSession();
UserMapper userMapper1 = sqlSession1.getMapper(UserMapper.class);
User user1 = userMapper1.getUserById(1);
System.out.println(user1);
sqlSession1.close(); // 关闭 SqlSession 时，会将一级缓存中的数据写入二级缓存

// 第二个 SqlSession
SqlSession sqlSession2 = sqlSessionFactory.openSession();
UserMapper userMapper2 = sqlSession2.getMapper(UserMapper.class);
User user2 = userMapper2.getUserById(1); // 从二级缓存获取
System.out.println(user2);
sqlSession2.close();
```

### 2.5 二级缓存的使用条件

1. 实体类需要实现 `Serializable` 接口
2. 开启二级缓存配置
3. 在 Mapper XML 或 Mapper 接口中配置二级缓存

## 3. 缓存淘汰策略

MyBatis 提供了以下缓存淘汰策略：

### 3.1 LRU（Least Recently Used）

最近最少使用策略，当缓存达到上限时，会删除最久未使用的缓存项。这是默认的淘汰策略。

### 3.2 FIFO（First In First Out）

先进先出策略，当缓存达到上限时，会删除最早进入缓存的缓存项。

### 3.3 SOFT

软引用策略，当内存不足时，会删除软引用的缓存项。

### 3.4 WEAK

弱引用策略，当垃圾回收时，会删除弱引用的缓存项。

## 4. 缓存的优缺点

### 4.1 优点

- **提高查询性能**：减少数据库查询次数，提高应用程序的响应速度。
- **减少网络流量**：减少与数据库的交互，降低网络流量。
- **减轻数据库压力**：减少数据库的查询次数，减轻数据库的压力。

### 4.2 缺点

- **内存占用**：缓存会占用一定的内存空间。
- **数据一致性**：缓存可能会导致数据不一致的问题，需要合理配置缓存策略。
- **复杂度增加**：缓存的使用会增加系统的复杂度，需要更多的配置和管理。

## 5. 缓存的最佳实践

1. **合理使用缓存**：根据实际需求选择合适的缓存策略。

2. **注意数据一致性**：对于经常修改的数据，应该合理设置缓存的刷新间隔或禁用缓存。

3. **使用二级缓存**：对于不经常修改的数据，可以使用二级缓存来提高性能。

4. **实现 Serializable 接口**：使用二级缓存时，实体类需要实现 Serializable 接口。

5. **合理配置缓存大小**：根据实际情况配置缓存的大小，避免内存溢出。

6. **监控缓存性能**：定期监控缓存的使用情况，及时调整缓存策略。

7. **使用第三方缓存**：对于复杂的应用场景，可以考虑使用第三方缓存框架，如 Redis、EhCache 等。

## 6. 缓存与 Spring 集成

当 MyBatis 与 Spring 集成时，可以使用 Spring 提供的缓存抽象来管理缓存。

### 6.1 配置 Spring 缓存

```xml
<bean id="cacheManager" class="org.springframework.cache.support.SimpleCacheManager">
    <property name="caches">
        <set>
            <bean class="org.springframework.cache.concurrent.ConcurrentMapCacheFactoryBean">
                <property name="name" value="userCache"/>
            </bean>
        </set>
    </property>
</bean>

<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource"/>
    <property name="mapperLocations" value="classpath:mappers/*.xml"/>
    <property name="configuration">
        <bean class="org.apache.ibatis.session.Configuration">
            <property name="cacheEnabled" value="true"/>
        </bean>
    </property>
</bean>
```

### 6.2 使用 Spring 缓存注解

```java
@Service
@CacheConfig(cacheNames = "userCache")
public class UserService {
    
    @Autowired
    private UserMapper userMapper;
    
    @Cacheable(key = "#id")
    public User getUserById(int id) {
        return userMapper.getUserById(id);
    }
    
    @CacheEvict(key = "#user.id")
    public void updateUser(User user) {
        userMapper.updateUser(user);
    }
    
    @CacheEvict(key = "#id")
    public void deleteUser(int id) {
        userMapper.deleteUserById(id);
    }
}
```

## 7. 总结

MyBatis 提供了强大的缓存机制，包括一级缓存和二级缓存。合理使用缓存可以提高应用程序的性能，但也需要注意数据一致性的问题。在实际开发中，应该根据具体的需求选择合适的缓存策略，并合理配置缓存参数。