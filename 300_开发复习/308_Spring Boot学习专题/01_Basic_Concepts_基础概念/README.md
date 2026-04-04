# Spring Boot 基础概念

## 什么是 Spring Boot？

Spring Boot 是由 Pivotal 团队开发的一个基于 Spring 框架的开源项目，它的主要目标是简化 Spring 应用的初始搭建和开发过程。Spring Boot 通过提供默认配置和自动化配置，使开发者能够快速构建生产级别的应用程序。

## Spring Boot 的优势

### 1. 简化配置
- 自动配置：Spring Boot 会根据项目中引入的依赖自动配置应用程序
- 约定优于配置：遵循默认约定，减少配置文件的编写
- 内嵌容器：内置 Tomcat、Jetty 等 Web 容器，无需部署 WAR 文件

### 2. 快速开发
- 起步依赖：提供一系列依赖模块，简化 Maven/Gradle 配置
- 开发工具：集成热部署、自动重启等开发工具
- 命令行界面：提供命令行工具，方便快速创建和运行应用

### 3. 生产就绪
- 监控：集成 Spring Boot Actuator，提供应用监控功能
- 健康检查：内置健康检查端点
- 外部配置：支持多种外部配置方式，适应不同环境

### 4. 生态系统
- 与 Spring 生态系统无缝集成
- 丰富的第三方库支持
- 活跃的社区

## 快速入门

### 1. 环境准备

- JDK 8 或更高版本
- Maven 3.2+ 或 Gradle 4+
- IDE（推荐 IntelliJ IDEA 或 Eclipse）

### 2. 创建 Spring Boot 项目

#### 使用 Spring Initializr

1. 访问 [Spring Initializr](https://start.spring.io/)
2. 选择项目类型（Maven 或 Gradle）
3. 选择 Spring Boot 版本
4. 填写项目元数据（Group、Artifact、Name、Description、Package Name）
5. 选择依赖（例如 Web、JPA、Security 等）
6. 点击 "Generate" 按钮下载项目

#### 使用 IDE 创建

**IntelliJ IDEA：**
1. 打开 IDEA，选择 "File" -> "New" -> "Project..."
2. 选择 "Spring Initializr"
3. 填写项目信息，选择依赖
4. 点击 "Next" -> "Finish"

### 3. 项目结构

```
my-spring-boot-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── MySpringBootApplication.java  # 主应用类
│   │   │           ├── controller/                   # 控制器
│   │   │           ├── service/                      # 服务层
│   │   │           ├── repository/                   # 数据访问层
│   │   │           └── model/                       # 实体类
│   │   └── resources/
│   │       ├── application.properties               # 配置文件
│   │       └── static/                              # 静态资源
│   └── test/
│       └── java/
│           └── com/
│               └── example/                         # 测试类
├── pom.xml                                          # Maven 配置文件
└── README.md                                         # 项目说明
```

### 4. 核心注解

#### @SpringBootApplication

这是 Spring Boot 应用的核心注解，它是以下三个注解的组合：

- `@Configuration`：标记类为配置类
- `@EnableAutoConfiguration`：启用自动配置
- `@ComponentScan`：启用组件扫描

```java
@SpringBootApplication
public class MySpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(MySpringBootApplication.class, args);
    }
}
```

#### @RestController

用于标记控制器类，使其返回 JSON 响应。

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, Spring Boot!";
    }
}
```

#### @Service

用于标记服务层类。

```java
@Service
public class HelloService {
    public String getHelloMessage() {
        return "Hello from Service!";
    }
}
```

#### @Repository

用于标记数据访问层类。

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
}
```

### 5. 运行应用

#### 使用 Maven

```bash
mvn spring-boot:run
```

#### 使用 Gradle

```bash
gradle bootRun
```

#### 运行 jar 文件

```bash
# 构建
mvn package

# 运行
java -jar target/my-spring-boot-app-1.0.0.jar
```

## 示例项目

### 简单的 REST API

#### 主应用类

```java
@SpringBootApplication
public class MySpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(MySpringBootApplication.class, args);
    }
}
```

#### 控制器

```java
@RestController
@RequestMapping("/api")
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping("/users")
    public List<User> getUsers() {
        return userService.getUsers();
    }
    
    @GetMapping("/users/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }
    
    @PostMapping("/users")
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }
    
    @PutMapping("/users/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        return userService.updateUser(id, user);
    }
    
    @DeleteMapping("/users/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

#### 服务层

```java
@Service
public class UserService {
    private final List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public UserService() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "张三", "zhangsan@example.com"));
        users.add(new User(nextId++, "李四", "lisi@example.com"));
        users.add(new User(nextId++, "王五", "wangwu@example.com"));
    }
    
    public List<User> getUsers() {
        return users;
    }
    
    public User getUserById(Long id) {
        return users.stream()
                .filter(user -> user.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
    
    public User createUser(User user) {
        user.setId(nextId++);
        users.add(user);
        return user;
    }
    
    public User updateUser(Long id, User user) {
        User existingUser = getUserById(id);
        if (existingUser != null) {
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
        }
        return existingUser;
    }
    
    public void deleteUser(Long id) {
        users.removeIf(user -> user.getId().equals(id));
    }
}
```

#### 实体类

```java
public class User {
    private Long id;
    private String name;
    private String email;
    
    // 构造方法、getter 和 setter 方法
    public User() {
    }
    
    public User(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
    
    // getter 和 setter 方法
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
}
```

## 常见问题

### 1. Spring Boot 与 Spring 的关系

Spring Boot 是基于 Spring 框架的，它提供了一种快速构建 Spring 应用的方式。Spring Boot 并不是替代 Spring，而是对 Spring 的增强和简化。

### 2. 如何选择 Spring Boot 版本

- 选择稳定版本：优先选择 GA（General Availability）版本
- 考虑兼容性：确保所选版本与项目依赖兼容
- 查看支持周期：了解版本的支持期限

### 3. 如何添加依赖

在 Maven 的 pom.xml 文件中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

在 Gradle 的 build.gradle 文件中添加依赖：

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
}
```

### 4. 如何配置应用

Spring Boot 支持多种配置方式：

- application.properties 文件
- application.yml 文件
- 环境变量
- 命令行参数

## 总结

Spring Boot 是一个强大的框架，它通过简化配置、提供默认约定和集成常用功能，使开发者能够快速构建生产级别的应用程序。通过本章节的学习，您应该对 Spring Boot 的基本概念、优势和使用方法有了初步的了解。在后续章节中，我们将深入探讨 Spring Boot 的核心配置、Web 开发、数据访问等高级特性。