# Spring Boot 数据访问

## 数据访问概述

Spring Boot 提供了丰富的数据访问选项，支持多种数据库和访问方式。本章节将介绍 Spring Boot 中常用的数据访问技术，包括 JPA、MyBatis、JDBC 等。

## JPA (Java Persistence API)

### 1. 概述

JPA 是 Java 持久化 API 的缩写，是一种 ORM（对象关系映射）规范。Spring Boot 通过 Spring Data JPA 提供了对 JPA 的支持，简化了数据库操作。

### 2. 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

在 `application.yml` 中配置数据库连接：

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: password
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
```

### 3. 实体类

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "name", nullable = false)
    private String name;
    
    @Column(name = "email", unique = true, nullable = false)
    private String email;
    
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    // 构造方法、getter 和 setter 方法
}
```

### 4. 仓库接口

```java
public interface UserRepository extends JpaRepository<User, Long> {
    // 按名称查询用户
    List<User> findByName(String name);
    
    // 按邮箱查询用户
    Optional<User> findByEmail(String email);
    
    // 按名称模糊查询
    List<User> findByNameContaining(String name);
    
    // 按创建时间排序
    List<User> findAllByOrderByCreatedAtDesc();
}
```

### 5. 服务层

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public List<User> getUsers() {
        return userRepository.findAll();
    }
    
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }
    
    public User createUser(User user) {
        user.setCreatedAt(LocalDateTime.now());
        return userRepository.save(user);
    }
    
    public Optional<User> updateUser(Long id, User user) {
        return userRepository.findById(id)
                .map(existingUser -> {
                    existingUser.setName(user.getName());
                    existingUser.setEmail(user.getEmail());
                    return userRepository.save(existingUser);
                });
    }
    
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

### 6. 自定义查询

```java
public interface UserRepository extends JpaRepository<User, Long> {
    // 使用 @Query 注解自定义查询
    @Query("SELECT u FROM User u WHERE u.name = :name AND u.email = :email")
    List<User> findByNameAndEmail(@Param("name") String name, @Param("email") String email);
    
    // 原生 SQL 查询
    @Query(value = "SELECT * FROM users WHERE name = ?1", nativeQuery = true)
    List<User> findByNameNative(String name);
}
```

## MyBatis

### 1. 概述

MyBatis 是一种半自动 ORM 框架，它允许开发者直接编写 SQL 语句，同时提供了对象关系映射功能。

### 2. 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.3.1</version>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

在 `application.yml` 中配置数据库连接：

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: password

mybatis:
  mapper-locations: classpath:mappers/*.xml
  type-aliases-package: com.example.model
```

### 3. 实体类

```java
public class User {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime createdAt;
    
    // 构造方法、getter 和 setter 方法
}
```

### 4. Mapper 接口

```java
@Mapper
public interface UserMapper {
    List<User> findAll();
    User findById(Long id);
    int insert(User user);
    int update(User user);
    int delete(Long id);
    List<User> findByName(String name);
}
```

### 5. Mapper XML 文件

在 `src/main/resources/mappers` 目录下创建 `UserMapper.xml`：

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findAll" resultType="User">
        SELECT * FROM users
    </select>
    
    <select id="findById" resultType="User" parameterType="Long">
        SELECT * FROM users WHERE id = #{id}
    </select>
    
    <insert id="insert" parameterType="User" useGeneratedKeys="true" keyProperty="id">
        INSERT INTO users (name, email, created_at) VALUES (#{name}, #{email}, #{createdAt})
    </insert>
    
    <update id="update" parameterType="User">
        UPDATE users SET name = #{name}, email = #{email} WHERE id = #{id}
    </update>
    
    <delete id="delete" parameterType="Long">
        DELETE FROM users WHERE id = #{id}
    </delete>
    
    <select id="findByName" resultType="User" parameterType="String">
        SELECT * FROM users WHERE name = #{name}
    </select>
</mapper>
```

### 6. 服务层

```java
@Service
public class UserService {
    private final UserMapper userMapper;
    
    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }
    
    public List<User> getUsers() {
        return userMapper.findAll();
    }
    
    public User getUserById(Long id) {
        return userMapper.findById(id);
    }
    
    public User createUser(User user) {
        user.setCreatedAt(LocalDateTime.now());
        userMapper.insert(user);
        return user;
    }
    
    public User updateUser(Long id, User user) {
        user.setId(id);
        userMapper.update(user);
        return user;
    }
    
    public void deleteUser(Long id) {
        userMapper.delete(id);
    }
}
```

## JDBC

### 1. 概述

JDBC（Java Database Connectivity）是 Java 提供的用于访问数据库的标准 API。Spring Boot 通过 `JdbcTemplate` 提供了对 JDBC 的简化支持。

### 2. 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

在 `application.yml` 中配置数据库连接：

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: password
```

### 3. 服务层

```java
@Service
public class UserService {
    private final JdbcTemplate jdbcTemplate;
    
    public UserService(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    
    public List<User> getUsers() {
        String sql = "SELECT * FROM users";
        return jdbcTemplate.query(sql, (rs, rowNum) -> {
            User user = new User();
            user.setId(rs.getLong("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
            return user;
        });
    }
    
    public User getUserById(Long id) {
        String sql = "SELECT * FROM users WHERE id = ?";
        return jdbcTemplate.queryForObject(sql, new Object[]{id}, (rs, rowNum) -> {
            User user = new User();
            user.setId(rs.getLong("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            user.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
            return user;
        });
    }
    
    public User createUser(User user) {
        String sql = "INSERT INTO users (name, email, created_at) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql, user.getName(), user.getEmail(), LocalDateTime.now());
        return user;
    }
    
    public User updateUser(Long id, User user) {
        String sql = "UPDATE users SET name = ?, email = ? WHERE id = ?";
        jdbcTemplate.update(sql, user.getName(), user.getEmail(), id);
        return user;
    }
    
    public void deleteUser(Long id) {
        String sql = "DELETE FROM users WHERE id = ?";
        jdbcTemplate.update(sql, id);
    }
}
```

## 事务管理

### 1. 概述

事务管理是数据访问中的重要概念，它确保一组操作要么全部成功，要么全部失败。Spring Boot 提供了声明式事务管理，通过 `@Transactional` 注解实现。

### 2. 使用 @Transactional 注解

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Transactional
    public void transferFunds(Long fromUserId, Long toUserId, double amount) {
        // 从用户1扣除金额
        User fromUser = userRepository.findById(fromUserId).orElseThrow();
        fromUser.setBalance(fromUser.getBalance() - amount);
        userRepository.save(fromUser);
        
        // 向用户2添加金额
        User toUser = userRepository.findById(toUserId).orElseThrow();
        toUser.setBalance(toUser.getBalance() + amount);
        userRepository.save(toUser);
    }
}
```

### 3. 事务属性

```java
@Transactional(
    propagation = Propagation.REQUIRED,  // 事务传播行为
    isolation = Isolation.READ_COMMITTED, // 事务隔离级别
    timeout = 30,  // 事务超时时间（秒）
    readOnly = false,  // 是否为只读事务
    rollbackFor = Exception.class  // 触发回滚的异常类型
)
public void performTransaction() {
    // 事务操作
}
```

## 缓存

### 1. 概述

缓存可以提高应用程序的性能，减少数据库查询次数。Spring Boot 提供了对多种缓存实现的支持，包括 EhCache、Redis、Caffeine 等。

### 2. 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
<!-- 可选：添加具体的缓存实现 -->
<dependency>
    <groupId>com.github.ben-manes.caffeine</groupId>
    <artifactId>caffeine</artifactId>
</dependency>
```

在主应用类上添加 `@EnableCaching` 注解：

```java
@SpringBootApplication
@EnableCaching
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### 3. 使用缓存

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(Long id) {
        System.out.println("查询数据库获取用户：" + id);
        return userRepository.findById(id).orElse(null);
    }
    
    @CachePut(value = "users", key = "#user.id")
    public User saveUser(User user) {
        return userRepository.save(user);
    }
    
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

## 示例：完整的数据访问应用

### 1. 项目结构

```
my-data-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── MyDataApplication.java
│   │   │           ├── controller/
│   │   │           │   └── UserController.java
│   │   │           ├── service/
│   │   │           │   └── UserService.java
│   │   │           ├── repository/
│   │   │           │   └── UserRepository.java
│   │   │           ├── model/
│   │   │           │   └── User.java
│   │   │           └── config/
│   │   │               └── CacheConfig.java
│   │   └── resources/
│   │       ├── application.yml
│   │       └── mappers/ (MyBatis 配置)
│   └── test/
│       └── java/
│           └── com/
│               └── example/
├── pom.xml
└── README.md
```

### 2. 控制器

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping
    public List<User> getUsers() {
        return userService.getUsers();
    }
    
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        return userService.updateUser(id, user);
    }
    
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

### 3. 服务层

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public List<User> getUsers() {
        return userRepository.findAll();
    }
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }
    
    @Transactional
    @CachePut(value = "users", key = "#user.id")
    public User createUser(User user) {
        user.setCreatedAt(LocalDateTime.now());
        return userRepository.save(user);
    }
    
    @Transactional
    @CachePut(value = "users", key = "#id")
    public User updateUser(Long id, User user) {
        User existingUser = userRepository.findById(id).orElse(null);
        if (existingUser != null) {
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
            return userRepository.save(existingUser);
        }
        return null;
    }
    
    @Transactional
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

### 4. 数据访问层

```java
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name);
    Optional<User> findByEmail(String email);
}
```

### 5. 实体类

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String name;
    private String email;
    private LocalDateTime createdAt;
    
    // 构造方法、getter 和 setter 方法
}
```

## 最佳实践

### 1. 选择合适的数据访问技术

- **JPA**：适用于大多数场景，特别是需要对象关系映射的应用
- **MyBatis**：适用于需要灵活控制 SQL 的场景
- **JDBC**：适用于简单的数据库操作，或者需要直接使用 SQL 的场景

### 2. 数据库连接池配置

- 使用 HikariCP 作为默认连接池
- 合理设置连接池大小，避免资源浪费
- 配置连接超时时间，避免长时间占用连接

### 3. 事务管理

- 使用声明式事务管理（@Transactional）
- 合理设置事务隔离级别
- 避免事务嵌套，减少事务开销

### 4. 缓存策略

- 合理使用缓存，减少数据库查询
- 选择合适的缓存实现
- 注意缓存一致性问题

### 5. 性能优化

- 优化 SQL 查询
- 使用索引
- 避免 N+1 查询问题
- 批量操作数据

### 6. 安全性

- 防止 SQL 注入
- 使用参数化查询
- 验证输入数据
- 加密敏感数据

## 常见问题

### 1. 数据库连接失败

- 检查数据库是否启动
- 检查数据库连接配置是否正确
- 检查数据库用户权限

### 2. 事务回滚问题

- 检查异常是否被正确捕获
- 检查事务传播行为设置
- 检查是否在非 public 方法上使用 @Transactional 注解

### 3. 缓存不一致

- 确保修改数据后更新或清除缓存
- 使用缓存注解时确保 key 正确
- 考虑使用分布式缓存解决集群环境下的缓存一致性问题

### 4. 性能问题

- 检查 SQL 查询是否优化
- 检查是否存在 N+1 查询问题
- 检查连接池配置是否合理
- 考虑使用二级缓存

## 总结

Spring Boot 提供了丰富的数据访问选项，包括 JPA、MyBatis、JDBC 等。通过本章节的学习，您应该了解了如何在 Spring Boot 应用中实现数据访问，包括配置数据库连接、定义实体类、创建仓库接口、实现服务层和控制器，以及如何使用事务管理和缓存提高应用性能。在实际开发中，应该根据项目的具体需求选择合适的数据访问技术，并遵循最佳实践，确保数据访问的效率和安全性。