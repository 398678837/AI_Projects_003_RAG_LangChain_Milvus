# MyBatis 实战应用

## 1. 项目结构

### 1.1 基本项目结构

```
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── pojo/          # 实体类
│   │   │           ├── mapper/         # Mapper 接口
│   │   │           ├── service/        # 服务层
│   │   │           ├── controller/     # 控制器
│   │   │           ├── config/         # 配置类
│   │   │           └── utils/          # 工具类
│   │   └── resources/
│   │       ├── application.yml        # 应用配置文件
│   │       └── mapper/                 # XML 映射文件
│   └── test/
│       └── java/                       # 测试代码
├── pom.xml                             # Maven 配置文件
```

### 1.2 依赖配置

```xml
<dependencies>
    <!-- Spring Boot 核心依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- MyBatis 依赖 -->
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.2.2</version>
    </dependency>
    
    <!-- 数据库驱动 -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- 连接池 -->
    <dependency>
        <groupId>com.zaxxer</groupId>
        <artifactId>HikariCP</artifactId>
    </dependency>
    
    <!-- 测试依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

## 2. 配置文件

### 2.1 应用配置文件 (application.yml)

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mybatis_demo?useSSL=false&serverTimezone=UTC
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5

mybatis:
  mapper-locations: classpath:mapper/*.xml
  type-aliases-package: com.example.pojo
  configuration:
    map-underscore-to-camel-case: true
    cache-enabled: true
```

### 2.2 MyBatis 配置类

```java
@Configuration
@MapperScan(basePackages = "com.example.mapper")
public class MyBatisConfig {
    
    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        SqlSessionFactoryBean factoryBean = new SqlSessionFactoryBean();
        factoryBean.setDataSource(dataSource);
        return factoryBean.getObject();
    }
    
    @Bean
    public SqlSessionTemplate sqlSessionTemplate(SqlSessionFactory sqlSessionFactory) {
        return new SqlSessionTemplate(sqlSessionFactory);
    }
}
```

## 3. 实体类

### 3.1 User 实体类

```java
public class User {
    private Long id;
    private String name;
    private String password;
    private String email;
    private Integer age;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;
    
    // getter 和 setter 方法
    // toString 方法
}
```

### 3.2 Order 实体类

```java
public class Order {
    private Long id;
    private String orderNo;
    private Long userId;
    private BigDecimal amount;
    private Integer status;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;
    
    // getter 和 setter 方法
    // toString 方法
}
```

## 4. Mapper 接口

### 4.1 UserMapper 接口

```java
public interface UserMapper {
    User getUserById(Long id);
    List<User> getUserList();
    int addUser(User user);
    int updateUser(User user);
    int deleteUser(Long id);
    List<User> getUserByCondition(User user);
}
```

### 4.2 OrderMapper 接口

```java
public interface OrderMapper {
    Order getOrderById(Long id);
    List<Order> getOrderList();
    int addOrder(Order order);
    int updateOrder(Order order);
    int deleteOrder(Long id);
    List<Order> getOrderByUserId(Long userId);
}
```

## 5. XML 映射文件

### 5.1 UserMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">
    <resultMap id="UserResultMap" type="User">
        <id property="id" column="id"/>
        <result property="name" column="name"/>
        <result property="password" column="password"/>
        <result property="email" column="email"/>
        <result property="age" column="age"/>
        <result property="createTime" column="create_time"/>
        <result property="updateTime" column="update_time"/>
    </resultMap>
    
    <select id="getUserById" parameterType="Long" resultMap="UserResultMap">
        select * from user where id = #{id}
    </select>
    
    <select id="getUserList" resultMap="UserResultMap">
        select * from user
    </select>
    
    <insert id="addUser" parameterType="User" useGeneratedKeys="true" keyProperty="id">
        insert into user (name, password, email, age, create_time, update_time)
        values (#{name}, #{password}, #{email}, #{age}, now(), now())
    </insert>
    
    <update id="updateUser" parameterType="User">
        update user
        <set>
            <if test="name != null">name = #{name},</if>
            <if test="password != null">password = #{password},</if>
            <if test="email != null">email = #{email},</if>
            <if test="age != null">age = #{age},</if>
            update_time = now()
        </set>
        where id = #{id}
    </update>
    
    <delete id="deleteUser" parameterType="Long">
        delete from user where id = #{id}
    </delete>
    
    <select id="getUserByCondition" parameterType="User" resultMap="UserResultMap">
        select * from user
        <where>
            <if test="name != null and name != ''">
                and name like concat('%', #{name}, '%')
            </if>
            <if test="age != null">
                and age = #{age}
            </if>
            <if test="email != null and email != ''">
                and email like concat('%', #{email}, '%')
            </if>
        </where>
    </select>
</mapper>
```

### 5.2 OrderMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.OrderMapper">
    <resultMap id="OrderResultMap" type="Order">
        <id property="id" column="id"/>
        <result property="orderNo" column="order_no"/>
        <result property="userId" column="user_id"/>
        <result property="amount" column="amount"/>
        <result property="status" column="status"/>
        <result property="createTime" column="create_time"/>
        <result property="updateTime" column="update_time"/>
    </resultMap>
    
    <select id="getOrderById" parameterType="Long" resultMap="OrderResultMap">
        select * from order where id = #{id}
    </select>
    
    <select id="getOrderList" resultMap="OrderResultMap">
        select * from order
    </select>
    
    <insert id="addOrder" parameterType="Order" useGeneratedKeys="true" keyProperty="id">
        insert into order (order_no, user_id, amount, status, create_time, update_time)
        values (#{orderNo}, #{userId}, #{amount}, #{status}, now(), now())
    </insert>
    
    <update id="updateOrder" parameterType="Order">
        update order
        <set>
            <if test="orderNo != null">order_no = #{orderNo},</if>
            <if test="amount != null">amount = #{amount},</if>
            <if test="status != null">status = #{status},</if>
            update_time = now()
        </set>
        where id = #{id}
    </update>
    
    <delete id="deleteOrder" parameterType="Long">
        delete from order where id = #{id}
    </delete>
    
    <select id="getOrderByUserId" parameterType="Long" resultMap="OrderResultMap">
        select * from order where user_id = #{userId}
    </select>
</mapper>
```

## 6. 服务层

### 6.1 UserService 接口

```java
public interface UserService {
    User getUserById(Long id);
    List<User> getUserList();
    int addUser(User user);
    int updateUser(User user);
    int deleteUser(Long id);
    List<User> getUserByCondition(User user);
}
```

### 6.2 UserService 实现

```java
@Service
public class UserServiceImpl implements UserService {
    
    @Autowired
    private UserMapper userMapper;
    
    @Override
    public User getUserById(Long id) {
        return userMapper.getUserById(id);
    }
    
    @Override
    public List<User> getUserList() {
        return userMapper.getUserList();
    }
    
    @Override
    @Transactional
    public int addUser(User user) {
        return userMapper.addUser(user);
    }
    
    @Override
    @Transactional
    public int updateUser(User user) {
        return userMapper.updateUser(user);
    }
    
    @Override
    @Transactional
    public int deleteUser(Long id) {
        return userMapper.deleteUser(id);
    }
    
    @Override
    public List<User> getUserByCondition(User user) {
        return userMapper.getUserByCondition(user);
    }
}
```

## 7. 控制器

### 7.1 UserController

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        User user = userService.getUserById(id);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }
    
    @GetMapping
    public ResponseEntity<List<User>> getUserList() {
        List<User> users = userService.getUserList();
        return ResponseEntity.ok(users);
    }
    
    @PostMapping
    public ResponseEntity<User> addUser(@RequestBody User user) {
        int result = userService.addUser(user);
        if (result > 0) {
            return ResponseEntity.ok(user);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        int result = userService.updateUser(user);
        if (result > 0) {
            return ResponseEntity.ok(user);
        }
        return ResponseEntity.badRequest().build();
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        int result = userService.deleteUser(id);
        if (result > 0) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.badRequest().build();
    }
    
    @PostMapping("/condition")
    public ResponseEntity<List<User>> getUserByCondition(@RequestBody User user) {
        List<User> users = userService.getUserByCondition(user);
        return ResponseEntity.ok(users);
    }
}
```

## 8. 测试

### 8.1 单元测试

```java
@SpringBootTest
class UserMapperTest {
    
    @Autowired
    private UserMapper userMapper;
    
    @Test
    void testGetUserById() {
        User user = userMapper.getUserById(1L);
        assertNotNull(user);
        assertEquals("张三", user.getName());
    }
    
    @Test
    void testGetUserList() {
        List<User> users = userMapper.getUserList();
        assertNotNull(users);
        assertTrue(users.size() > 0);
    }
    
    @Test
    void testAddUser() {
        User user = new User();
        user.setName("测试用户");
        user.setPassword("123456");
        user.setEmail("test@example.com");
        user.setAge(25);
        
        int result = userMapper.addUser(user);
        assertTrue(result > 0);
        assertNotNull(user.getId());
    }
}
```

### 8.2 集成测试

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class UserControllerTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    void testGetUserById() {
        ResponseEntity<User> response = restTemplate.getForEntity("/api/users/1", User.class);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("张三", response.getBody().getName());
    }
    
    @Test
    void testGetUserList() {
        ResponseEntity<List> response = restTemplate.getForEntity("/api/users", List.class);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertTrue(response.getBody().size() > 0);
    }
}
```

## 9. 部署

### 9.1 构建项目

```bash
mvn clean package
```

### 9.2 运行项目

```bash
java -jar target/mybatis-demo-1.0.0.jar
```

### 9.3 容器化部署

#### Dockerfile

```dockerfile
FROM openjdk:11
COPY target/mybatis-demo-1.0.0.jar /app/mybatis-demo.jar
WORKDIR /app
EXPOSE 8080
CMD ["java", "-jar", "mybatis-demo.jar"]
```

#### 构建镜像

```bash
docker build -t mybatis-demo .
```

#### 运行容器

```bash
docker run -p 8080:8080 mybatis-demo
```

## 10. 监控与维护

### 10.1 日志配置

```yaml
logging:
  level:
    com.example.mapper: debug
    org.apache.ibatis: debug
```

### 10.2 性能监控

- 使用 Spring Boot Actuator 监控应用状态
- 使用 MyBatis 提供的监控功能
- 使用数据库监控工具监控 SQL 执行情况

### 10.3 常见问题

#### 10.3.1 SQL 注入

- 原因：使用 `${}` 进行字符串替换
- 解决方案：使用 `#{}` 进行参数绑定

#### 10.3.2 延迟加载问题

- 原因：延迟加载配置不当
- 解决方案：正确配置 `lazyLoadingEnabled` 和 `aggressiveLazyLoading`

#### 10.3.3 缓存一致性问题

- 原因：缓存未及时更新
- 解决方案：在增删改操作后手动清理缓存或使用缓存失效机制

## 11. 总结

本实战应用展示了如何在 Spring Boot 项目中使用 MyBatis 进行数据库操作。通过合理的项目结构、配置和代码组织，可以构建一个高效、可维护的 MyBatis 应用。在实际开发中，应该根据具体的需求和场景，选择合适的实现方式，以达到最佳的效果。