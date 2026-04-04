# Spring Boot 测试

## 测试概述

测试是软件开发过程中的重要环节，它确保应用程序的质量和可靠性。Spring Boot 提供了全面的测试支持，包括单元测试、集成测试和端到端测试。本章节将介绍 Spring Boot 中的测试方法和工具。

## 测试类型

### 1. 单元测试

单元测试是对应用程序中最小的可测试单元进行测试，通常是对单个方法或类的测试。

### 2. 集成测试

集成测试是测试应用程序的多个组件之间的交互，确保它们能够正确协同工作。

### 3. 端到端测试

端到端测试是测试整个应用程序的流程，从用户输入到系统响应的完整流程。

## 核心依赖

在 `pom.xml` 中添加测试依赖：

```xml
<dependencies>
    <!-- 测试核心依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    
    <!-- Mockito 用于模拟对象 -->
    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-core</artifactId>
        <scope>test</scope>
    </dependency>
    
    <!-- JUnit 5 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <scope>test</scope>
    </dependency>
    
    <!-- AssertJ 用于断言 -->
    <dependency>
        <groupId>org.assertj</groupId>
        <artifactId>assertj-core</artifactId>
        <scope>test</scope>
    </dependency>
    
    <!-- Testcontainers 用于集成测试 -->
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>junit-jupiter</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>mysql</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

## 单元测试

### 1. 基本单元测试

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

class UserServiceTest {
    
    @Test
    void testGetUserById() {
        // 模拟 UserRepository
        UserRepository userRepository = mock(UserRepository.class);
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        
        // 创建 UserService
        UserService userService = new UserService(userRepository);
        
        // 测试方法
        User result = userService.getUserById(1L);
        
        // 验证结果
        assertEquals("张三", result.getName());
        assertEquals("zhangsan@example.com", result.getEmail());
        
        // 验证方法调用
        verify(userRepository, times(1)).findById(1L);
    }
}
```

### 2. 使用 @Mock 和 @InjectMocks

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testGetUserById() {
        // 准备数据
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        
        // 测试方法
        User result = userService.getUserById(1L);
        
        // 验证结果
        assertEquals("张三", result.getName());
        assertEquals("zhangsan@example.com", result.getEmail());
        
        // 验证方法调用
        verify(userRepository, times(1)).findById(1L);
    }
}
```

## 集成测试

### 1. 使用 @SpringBootTest

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class UserServiceIntegrationTest {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testCreateUser() {
        // 准备数据
        User user = new User(null, "李四", "lisi@example.com");
        
        // 测试方法
        User result = userService.createUser(user);
        
        // 验证结果
        assertEquals("李四", result.getName());
        assertEquals("lisi@example.com", result.getEmail());
        assertEquals(1L, result.getId());
        
        // 验证数据已保存
        User savedUser = userRepository.findById(1L).orElse(null);
        assertEquals("李四", savedUser.getName());
    }
}
```

### 2. 使用 Testcontainers

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import static org.junit.jupiter.api.Assertions.assertEquals;

@Testcontainers
@SpringBootTest
class UserServiceIntegrationTest {
    
    @Container
    static MySQLContainer<?> mysqlContainer = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("test")
            .withUsername("test")
            .withPassword("test");
    
    @DynamicPropertySource
    static void registerProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysqlContainer::getJdbcUrl);
        registry.add("spring.datasource.username", mysqlContainer::getUsername);
        registry.add("spring.datasource.password", mysqlContainer::getPassword);
    }
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testCreateUser() {
        // 准备数据
        User user = new User(null, "李四", "lisi@example.com");
        
        // 测试方法
        User result = userService.createUser(user);
        
        // 验证结果
        assertEquals("李四", result.getName());
        assertEquals("lisi@example.com", result.getEmail());
        assertEquals(1L, result.getId());
        
        // 验证数据已保存
        User savedUser = userRepository.findById(1L).orElse(null);
        assertEquals("李四", savedUser.getName());
    }
}
```

## Web 测试

### 1. 使用 MockMvc

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testGetUserById() throws Exception {
        // 准备数据
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userService.getUserById(1L)).thenReturn(user);
        
        // 执行请求
        mockMvc.perform(get("/api/users/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("张三"))
                .andExpect(jsonPath("$.email").value("zhangsan@example.com"));
    }
}
```

### 2. 使用 WebTestClient

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.reactive.WebFluxTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.reactive.server.WebTestClient;
import static org.mockito.Mockito.when;

@WebFluxTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private WebTestClient webTestClient;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testGetUserById() {
        // 准备数据
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userService.getUserById(1L)).thenReturn(user);
        
        // 执行请求
        webTestClient.get()
                .uri("/api/users/1")
                .exchange()
                .expectStatus().isOk()
                .expectBody(User.class)
                .isEqualTo(user);
    }
}
```

## 数据测试

### 1. 使用 @DataJpaTest

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import static org.junit.jupiter.api.Assertions.assertEquals;

@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testFindByEmail() {
        // 准备数据
        User user = new User(null, "张三", "zhangsan@example.com");
        entityManager.persist(user);
        entityManager.flush();
        
        // 测试方法
        User result = userRepository.findByEmail("zhangsan@example.com").orElse(null);
        
        // 验证结果
        assertEquals("张三", result.getName());
        assertEquals("zhangsan@example.com", result.getEmail());
    }
}
```

### 2. 使用 @Sql

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.jdbc.Sql;
import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
@Sql(scripts = {"classpath:data.sql"})
class UserServiceIntegrationTest {
    
    @Autowired
    private UserService userService;
    
    @Test
    void testGetUsers() {
        // 测试方法
        List<User> users = userService.getUsers();
        
        // 验证结果
        assertEquals(2, users.size());
        assertEquals("张三", users.get(0).getName());
        assertEquals("李四", users.get(1).getName());
    }
}
```

## 测试工具

### 1. JUnit 5

JUnit 5 是 Java 中最流行的测试框架，它提供了丰富的测试注解和断言方法。

**常用注解**：
- `@Test`：标记测试方法
- `@BeforeEach`：在每个测试方法之前执行
- `@AfterEach`：在每个测试方法之后执行
- `@BeforeAll`：在所有测试方法之前执行
- `@AfterAll`：在所有测试方法之后执行
- `@DisplayName`：设置测试方法的显示名称
- `@Disabled`：禁用测试方法

### 2. Mockito

Mockito 是一个用于模拟对象的框架，它允许你创建和配置模拟对象，以便在测试中使用。

**常用方法**：
- `mock(Class<T> classToMock)`：创建一个模拟对象
- `when(T methodCall).thenReturn(T value)`：设置模拟方法的返回值
- `verify(T mock).methodCall()`：验证方法是否被调用
- `@Mock`：标记模拟对象
- `@InjectMocks`：将模拟对象注入到被测试对象中

### 3. AssertJ

AssertJ 是一个用于断言的库，它提供了流畅的断言 API，使测试代码更加易读。

**常用方法**：
- `assertThat(T actual).isEqualTo(T expected)`：断言两个对象相等
- `assertThat(T actual).isNotNull()`：断言对象不为 null
- `assertThat(Collection<?> collection).hasSize(int size)`：断言集合大小
- `assertThat(String string).contains(String substring)`：断言字符串包含子字符串

### 4. Testcontainers

Testcontainers 是一个用于集成测试的库，它允许你在测试中使用真实的容器化服务。

**常用容器**：
- `MySQLContainer`：MySQL 数据库
- `PostgreSQLContainer`：PostgreSQL 数据库
- `RedisContainer`：Redis 缓存
- `RabbitMQContainer`：RabbitMQ 消息队列

## 最佳实践

### 1. 测试命名

- 测试类名：`{被测试类名}Test`
- 测试方法名：`test{方法名}{测试场景}`
- 使用 `@DisplayName` 为测试方法设置更具描述性的名称

### 2. 测试结构

- **Given**：准备测试数据和环境
- **When**：执行被测试的方法
- **Then**：验证测试结果

### 3. 测试覆盖

- 测试覆盖率目标：80% 以上
- 重点测试核心业务逻辑
- 测试边界情况和异常情况

### 4. 测试隔离

- 每个测试方法应该独立运行
- 测试之间不应该共享状态
- 使用 `@BeforeEach` 和 `@AfterEach` 清理测试数据

### 5. 测试性能

- 避免在测试中使用真实的网络调用
- 避免在测试中使用真实的数据库操作（单元测试）
- 使用模拟对象和存根数据

### 6. 测试维护

- 定期运行测试
- 及时修复失败的测试
- 保持测试代码的整洁和可读性
- 随着代码的变化更新测试

## 示例：完整的测试配置

### 1. 项目结构

```
my-test-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── MyApplication.java
│   │   │           ├── controller/
│   │   │           │   └── UserController.java
│   │   │           ├── service/
│   │   │           │   └── UserService.java
│   │   │           ├── repository/
│   │   │           │   └── UserRepository.java
│   │   │           └── model/
│   │   │               └── User.java
│   │   └── resources/
│   │       ├── application.yml
│   │       └── data.sql
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── controller/
│       │           │   └── UserControllerTest.java
│       │           ├── service/
│       │           │   └── UserServiceTest.java
│       │           └── repository/
│       │               └── UserRepositoryTest.java
│       └── resources/
│           └── application-test.yml
├── pom.xml
└── README.md
```

### 2. 单元测试

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testGetUserById() {
        // Given
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        
        // When
        User result = userService.getUserById(1L);
        
        // Then
        assertEquals("张三", result.getName());
        assertEquals("zhangsan@example.com", result.getEmail());
        verify(userRepository, times(1)).findById(1L);
    }
    
    @Test
    void testCreateUser() {
        // Given
        User user = new User(null, "李四", "lisi@example.com");
        User savedUser = new User(1L, "李四", "lisi@example.com");
        when(userRepository.save(user)).thenReturn(savedUser);
        
        // When
        User result = userService.createUser(user);
        
        // Then
        assertEquals(1L, result.getId());
        assertEquals("李四", result.getName());
        assertEquals("lisi@example.com", result.getEmail());
        verify(userRepository, times(1)).save(user);
    }
}
```

### 3. 集成测试

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.jdbc.Sql;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

@SpringBootTest
@Sql(scripts = {"classpath:data.sql"})
class UserServiceIntegrationTest {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testGetUsers() {
        // When
        List<User> users = userService.getUsers();
        
        // Then
        assertNotNull(users);
        assertEquals(2, users.size());
        assertEquals("张三", users.get(0).getName());
        assertEquals("李四", users.get(1).getName());
    }
    
    @Test
    void testCreateUser() {
        // Given
        User user = new User(null, "王五", "wangwu@example.com");
        
        // When
        User result = userService.createUser(user);
        
        // Then
        assertNotNull(result);
        assertNotNull(result.getId());
        assertEquals("王五", result.getName());
        assertEquals("wangwu@example.com", result.getEmail());
        
        // 验证数据已保存
        User savedUser = userRepository.findById(result.getId()).orElse(null);
        assertNotNull(savedUser);
        assertEquals("王五", savedUser.getName());
    }
}
```

### 4. Web 测试

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testGetUserById() throws Exception {
        // Given
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userService.getUserById(1L)).thenReturn(user);
        
        // When & Then
        mockMvc.perform(get("/api/users/1")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("张三"))
                .andExpect(jsonPath("$.email").value("zhangsan@example.com"));
    }
    
    @Test
    void testCreateUser() throws Exception {
        // Given
        User user = new User(1L, "李四", "lisi@example.com");
        when(userService.createUser(any(User.class))).thenReturn(user);
        
        // When & Then
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"name\": \"李四\", \"email\": \"lisi@example.com\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("李四"))
                .andExpect(jsonPath("$.email").value("lisi@example.com"));
    }
}
```

## 常见问题

### 1. 测试失败

- 检查测试数据是否正确
- 检查模拟对象的配置是否正确
- 检查被测试方法的逻辑是否正确
- 检查测试断言是否合理

### 2. 测试速度慢

- 减少集成测试的数量
- 使用内存数据库进行测试
- 避免在测试中使用真实的网络调用
- 合理使用测试并行执行

### 3. 测试覆盖不足

- 识别未测试的代码
- 为核心业务逻辑添加测试
- 测试边界情况和异常情况
- 使用测试覆盖率工具评估测试覆盖情况

### 4. 测试维护困难

- 保持测试代码的整洁和可读性
- 使用描述性的测试方法名
- 避免测试代码中的重复
- 随着代码的变化更新测试

## 总结

Spring Boot 提供了全面的测试支持，包括单元测试、集成测试和端到端测试。本章节介绍了 Spring Boot 中的测试方法和工具，包括 JUnit 5、Mockito、AssertJ 和 Testcontainers 等。通过本章节的学习，您应该了解如何在 Spring Boot 应用中编写有效的测试，如何使用测试工具和框架，以及如何遵循测试最佳实践。在实际开发中，应该重视测试，编写高质量的测试代码，确保应用程序的质量和可靠性。同时，应该定期运行测试，及时发现和解决问题，保持测试代码的更新和维护。