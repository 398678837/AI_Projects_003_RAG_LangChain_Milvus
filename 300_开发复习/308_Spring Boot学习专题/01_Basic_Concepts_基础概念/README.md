# Spring Boot 基础概念

## 什么是 Spring Boot？

Spring Boot 是由 Pivotal 团队开发的一个基于 Spring 框架的开源项目，它的主要目标是简化 Spring 应用的初始搭建和开发过程。Spring Boot 通过提供默认配置和自动化配置，使开发者能够快速构建生产级别的应用程序。

Spring Boot 的设计理念是"约定优于配置"，它通过提供合理的默认值和自动配置，减少了开发者在配置方面的工作量，让开发者能够专注于业务逻辑的实现。

## Spring Boot 的历史

- **2014 年 4 月**：Spring Boot 1.0.0 发布
- **2018 年 3 月**：Spring Boot 2.0.0 发布，引入了大量新特性和改进
- **2020 年 10 月**：Spring Boot 2.4.0 发布，改进了配置文件处理和启动时间
- **2021 年 5 月**：Spring Boot 2.5.0 发布，增强了安全性和监控功能
- **2022 年 5 月**：Spring Boot 2.6.0 发布，改进了 GraalVM 支持和性能
- **2022 年 11 月**：Spring Boot 3.0.0 发布，基于 Java 17 和 Spring Framework 6.0
- **2023 年 11 月**：Spring Boot 3.2.0 发布，引入了更多性能优化和新特性

## Spring Boot 的优势

### 1. 简化配置
- **自动配置**：Spring Boot 会根据项目中引入的依赖自动配置应用程序，减少手动配置的工作量
- **约定优于配置**：遵循默认约定，减少配置文件的编写，提高开发效率
- **内嵌容器**：内置 Tomcat、Jetty、Undertow 等 Web 容器，无需部署 WAR 文件，简化部署流程
- **统一配置管理**：通过 application.properties 或 application.yml 文件集中管理配置

### 2. 快速开发
- **起步依赖**：提供一系列依赖模块（Starter），简化 Maven/Gradle 配置
- **开发工具**：集成热部署、自动重启等开发工具，提高开发效率
- **命令行界面**：提供命令行工具（Spring Boot CLI），方便快速创建和运行应用
- **自动代码生成**：IDE 集成支持，自动生成项目结构和代码

### 3. 生产就绪
- **监控**：集成 Spring Boot Actuator，提供应用监控功能
- **健康检查**：内置健康检查端点，方便监控应用状态
- **外部配置**：支持多种外部配置方式，适应不同环境
- **日志管理**：提供统一的日志配置，支持多种日志框架
- **安全特性**：集成 Spring Security，提供安全保护

### 4. 生态系统
- **与 Spring 生态系统无缝集成**：支持 Spring MVC、Spring Data、Spring Security 等
- **丰富的第三方库支持**：通过起步依赖集成各种第三方库
- **活跃的社区**：拥有庞大的社区支持和丰富的学习资源
- **企业级支持**：提供商业支持和服务

## 快速入门

### 1. 环境准备

- **JDK**：JDK 8 或更高版本（Spring Boot 3.0+ 需要 JDK 17+）
- **构建工具**：Maven 3.2+ 或 Gradle 4+
- **IDE**：推荐 IntelliJ IDEA（ Ultimate 或 Community 版）、Eclipse（STS 插件）或 VS Code（Spring Boot 插件）
- **操作系统**：Windows、macOS、Linux 均可

### 2. 创建 Spring Boot 项目

#### 使用 Spring Initializr

1. 访问 [Spring Initializr](https://start.spring.io/)
2. 选择项目类型（Maven 或 Gradle）
3. 选择 Spring Boot 版本（建议选择稳定版本）
4. 填写项目元数据：
   - Group：组织标识，如 com.example
   - Artifact：项目名称，如 demo
   - Name：项目显示名称
   - Description：项目描述
   - Package Name：包名，如 com.example.demo
   - Java Version：Java 版本
5. 选择依赖（例如 Web、JPA、Security 等）
6. 点击 "Generate" 按钮下载项目
7. 解压下载的 zip 文件，导入到 IDE 中

#### 使用 IDE 创建

**IntelliJ IDEA：**
1. 打开 IDEA，选择 "File" -> "New" -> "Project..."
2. 选择 "Spring Initializr"
3. 选择项目 SDK（确保是 JDK 8+）
4. 点击 "Next"
5. 填写项目信息：
   - Group：组织标识
   - Artifact：项目名称
   - Version：项目版本
   - Name：项目显示名称
   - Description：项目描述
   - Package：包名
6. 选择 Spring Boot 版本
7. 选择依赖（例如 Web、JPA、Security 等）
8. 点击 "Next"
9. 选择项目保存位置
10. 点击 "Finish"

**Eclipse (STS)：**
1. 打开 Eclipse，选择 "File" -> "New" -> "Spring Starter Project"
2. 填写项目信息
3. 选择依赖
4. 点击 "Finish"

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
│   │   │           ├── model/                       # 实体类
│   │   │           ├── config/                      # 配置类
│   │   │           └── exception/                   # 异常处理
│   │   └── resources/
│   │       ├── application.properties               # 配置文件
│   │       ├── application.yml                     # YAML 配置文件
│   │       ├── static/                              # 静态资源
│   │       ├── templates/                           # 模板文件
│   │       └── META-INF/                            # 元数据
│   └── test/
│       └── java/
│           └── com/
│               └── example/                         # 测试类
├── pom.xml                                          # Maven 配置文件
├── build.gradle                                     # Gradle 配置文件（如果使用 Gradle）
└── README.md                                         # 项目说明
```

### 4. 核心注解

#### @SpringBootApplication

这是 Spring Boot 应用的核心注解，它是以下三个注解的组合：

- `@Configuration`：标记类为配置类，允许在类中定义 Bean
- `@EnableAutoConfiguration`：启用自动配置，根据项目依赖自动配置应用
- `@ComponentScan`：启用组件扫描，扫描并注册组件（如 @Controller、@Service、@Repository 等）

```java
@SpringBootApplication
public class MySpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(MySpringBootApplication.class, args);
    }
}
```

#### @RestController

用于标记控制器类，使其返回 JSON 响应。它是 `@Controller` 和 `@ResponseBody` 的组合注解。

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, Spring Boot!";
    }
    
    @GetMapping("/hello/{name}")
    public String hello(@PathVariable String name) {
        return "Hello, " + name + "!";
    }
}
```

#### @Controller

用于标记控制器类，通常与模板引擎配合使用，返回视图。

```java
@Controller
public class HomeController {
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("message", "Hello, Spring Boot!");
        return "home"; // 返回 home.html 模板
    }
}
```

#### @Service

用于标记服务层类，处理业务逻辑。

```java
@Service
public class HelloService {
    public String getHelloMessage() {
        return "Hello from Service!";
    }
    
    public String getHelloMessage(String name) {
        return "Hello, " + name + " from Service!";
    }
}
```

#### @Repository

用于标记数据访问层类，处理数据库操作。

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
    List<User> findByEmailContaining(String email);
}
```

#### @Component

通用的组件注解，用于标记任何 Spring 管理的组件。

```java
@Component
public class MyComponent {
    public void doSomething() {
        System.out.println("Doing something...");
    }
}
```

#### @Autowired

用于自动注入依赖，Spring 会自动查找并注入符合类型的 Bean。

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    private final HelloService helloService;
    
    @Autowired
    public HelloController(HelloService helloService) {
        this.helloService = helloService;
    }
    
    @GetMapping("/hello")
    public String hello() {
        return helloService.getHelloMessage();
    }
}
```

#### @Value

用于注入配置值，从 application.properties 或 application.yml 文件中获取配置。

```java
@Component
public class AppConfig {
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.version}")
    private String appVersion;
    
    // getter 方法
}
```

### 5. 运行应用

#### 使用 Maven

```bash
# 编译并运行
mvn spring-boot:run

# 编译打包
mvn package

# 运行打包后的 jar 文件
java -jar target/my-spring-boot-app-1.0.0.jar

# 运行指定环境的配置
java -jar target/my-spring-boot-app-1.0.0.jar --spring.profiles.active=prod
```

#### 使用 Gradle

```bash
# 编译并运行
gradle bootRun

# 编译打包
gradle build

# 运行打包后的 jar 文件
java -jar build/libs/my-spring-boot-app-1.0.0.jar
```

#### 使用 IDE 运行

**IntelliJ IDEA：**
1. 找到主应用类（带有 @SpringBootApplication 注解的类）
2. 右键点击类名，选择 "Run 'MySpringBootApplication'"

**Eclipse：**
1. 找到主应用类
2. 右键点击类名，选择 "Run As" -> "Spring Boot App"

## 示例项目：完整的 REST API

### 1. 项目结构

```
spring-boot-rest-api/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── SpringBootRestApiApplication.java
│   │   │           ├── controller/
│   │   │           │   └── UserController.java
│   │   │           ├── service/
│   │   │           │   └── UserService.java
│   │   │           ├── model/
│   │   │           │   └── User.java
│   │   │           └── exception/
│   │   │               ├── GlobalExceptionHandler.java
│   │   │               └── UserNotFoundException.java
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   └── SpringBootRestApiApplicationTests.java
├── pom.xml
└── README.md
```

### 2. 主应用类

```java
@SpringBootApplication
public class SpringBootRestApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootRestApiApplication.class, args);
    }
}
```

### 3. 实体类

```java
public class User {
    private Long id;
    private String name;
    private String email;
    private String phone;
    private String address;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    
    // 构造方法
    public User() {
    }
    
    public User(Long id, String name, String email, String phone, String address) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
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
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getAddress() {
        return address;
    }
    
    public void setAddress(String address) {
        this.address = address;
        this.updatedAt = LocalDateTime.now();
    }
    
    public LocalDateTime getCreatedAt() {
        return createdAt;
    }
    
    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
    
    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }
    
    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
```

### 4. 服务层

```java
@Service
public class UserService {
    private final List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public UserService() {
        // 初始化测试数据
        users.add(new User(nextId++, "张三", "zhangsan@example.com", "13800138001", "北京市朝阳区"));
        users.add(new User(nextId++, "李四", "lisi@example.com", "13900139002", "上海市浦东新区"));
        users.add(new User(nextId++, "王五", "wangwu@example.com", "13700137003", "广州市天河区"));
        users.add(new User(nextId++, "赵六", "zhaoliu@example.com", "13600136004", "深圳市南山区"));
        users.add(new User(nextId++, "孙七", "sunqi@example.com", "13500135005", "杭州市西湖区"));
    }
    
    /**
     * 获取所有用户
     */
    public List<User> getUsers() {
        return users;
    }
    
    /**
     * 根据 ID 获取用户
     */
    public User getUserById(Long id) {
        return users.stream()
                .filter(user -> user.getId().equals(id))
                .findFirst()
                .orElseThrow(() -> new UserNotFoundException("User not found with id: " + id));
    }
    
    /**
     * 创建新用户
     */
    public User createUser(User user) {
        user.setId(nextId++);
        user.setCreatedAt(LocalDateTime.now());
        user.setUpdatedAt(LocalDateTime.now());
        users.add(user);
        return user;
    }
    
    /**
     * 更新用户
     */
    public User updateUser(Long id, User user) {
        User existingUser = getUserById(id);
        existingUser.setName(user.getName());
        existingUser.setEmail(user.getEmail());
        existingUser.setPhone(user.getPhone());
        existingUser.setAddress(user.getAddress());
        existingUser.setUpdatedAt(LocalDateTime.now());
        return existingUser;
    }
    
    /**
     * 删除用户
     */
    public void deleteUser(Long id) {
        User user = getUserById(id);
        users.remove(user);
    }
    
    /**
     * 根据名称搜索用户
     */
    public List<User> searchUsersByName(String name) {
        return users.stream()
                .filter(user -> user.getName().contains(name))
                .collect(Collectors.toList());
    }
    
    /**
     * 根据邮箱搜索用户
     */
    public List<User> searchUsersByEmail(String email) {
        return users.stream()
                .filter(user -> user.getEmail().contains(email))
                .collect(Collectors.toList());
    }
}
```

### 5. 控制器

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * 获取所有用户
     */
    @GetMapping
    public ResponseEntity<List<User>> getUsers(
            @RequestParam(required = false) String name,
            @RequestParam(required = false) String email) {
        List<User> users;
        if (name != null) {
            users = userService.searchUsersByName(name);
        } else if (email != null) {
            users = userService.searchUsersByEmail(email);
        } else {
            users = userService.getUsers();
        }
        return ResponseEntity.ok(users);
    }
    
    /**
     * 根据 ID 获取用户
     */
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        User user = userService.getUserById(id);
        return ResponseEntity.ok(user);
    }
    
    /**
     * 创建新用户
     */
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User createdUser = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdUser);
    }
    
    /**
     * 更新用户
     */
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @RequestBody User user) {
        User updatedUser = userService.updateUser(id, user);
        return ResponseEntity.ok(updatedUser);
    }
    
    /**
     * 删除用户
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
```

### 6. 异常处理

#### 自定义异常

```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}
```

#### 全局异常处理器

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFoundException(UserNotFoundException ex) {
        ErrorResponse error = new ErrorResponse();
        error.setStatus(HttpStatus.NOT_FOUND.value());
        error.setMessage(ex.getMessage());
        error.setTimestamp(LocalDateTime.now());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception ex) {
        ErrorResponse error = new ErrorResponse();
        error.setStatus(HttpStatus.INTERNAL_SERVER_ERROR.value());
        error.setMessage("Internal server error");
        error.setTimestamp(LocalDateTime.now());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

#### 错误响应类

```java
public class ErrorResponse {
    private int status;
    private String message;
    private LocalDateTime timestamp;
    
    // getter 和 setter 方法
    public int getStatus() {
        return status;
    }
    
    public void setStatus(int status) {
        this.status = status;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public LocalDateTime getTimestamp() {
        return timestamp;
    }
    
    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
```

### 7. 配置文件

```yaml
# application.yml
spring:
  application:
    name: spring-boot-rest-api
  
server:
  port: 8080
  servlet:
    context-path: /api

# 自定义配置
app:
  name: Spring Boot REST API
  version: 1.0.0
  description: A simple REST API built with Spring Boot
```

## 常见问题

### 1. Spring Boot 与 Spring 的关系

Spring Boot 是基于 Spring 框架的，它提供了一种快速构建 Spring 应用的方式。Spring Boot 并不是替代 Spring，而是对 Spring 的增强和简化。Spring Boot 提供了自动配置、起步依赖等特性，使开发者能够更快速地构建 Spring 应用。

### 2. 如何选择 Spring Boot 版本

- **选择稳定版本**：优先选择 GA（General Availability）版本，避免使用 SNAPSHOT 版本
- **考虑兼容性**：确保所选版本与项目依赖兼容，特别是与 Java 版本的兼容性
- **查看支持周期**：了解版本的支持期限，选择有足够支持时间的版本
- **关注新特性**：如果需要使用新特性，可以选择较新的版本

### 3. 如何添加依赖

在 Maven 的 pom.xml 文件中添加依赖：

```xml
<!-- Web 依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- JPA 依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- 数据库驱动 -->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>

<!-- 测试依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

在 Gradle 的 build.gradle 文件中添加依赖：

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    runtimeOnly 'com.mysql:mysql-connector-j'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```

### 4. 如何配置应用

Spring Boot 支持多种配置方式：

- **application.properties 文件**：使用键值对格式配置
- **application.yml 文件**：使用 YAML 格式配置，更简洁易读
- **环境变量**：使用大写字母和下划线命名，如 SPRING_DATASOURCE_URL
- **命令行参数**：使用 -- 前缀，如 --server.port=8081
- **配置中心**：如 Spring Cloud Config

### 5. 如何部署 Spring Boot 应用

Spring Boot 应用可以通过以下方式部署：

- **jar 文件**：使用 `java -jar` 命令运行
- **war 文件**：部署到外部 Tomcat 等容器
- **Docker 容器**：构建 Docker 镜像并运行
- **云平台**：部署到 AWS、Azure、GCP 等云平台
- **Kubernetes**：部署到 Kubernetes 集群

### 6. 如何优化 Spring Boot 应用性能

- **使用合适的内嵌容器**：根据应用需求选择 Tomcat、Jetty 或 Undertow
- **配置连接池**：合理配置数据库连接池大小
- **启用缓存**：使用 Spring Cache 或 Redis 等缓存
- **优化启动时间**：减少不必要的依赖，使用懒加载
- **使用 JVM 优化**：合理配置 JVM 参数
- **监控应用**：使用 Spring Boot Actuator 监控应用状态

## 总结

Spring Boot 是一个强大的框架，它通过简化配置、提供默认约定和集成常用功能，使开发者能够快速构建生产级别的应用程序。本章节介绍了 Spring Boot 的基本概念、优势、历史、快速入门方法、核心注解、运行方式以及一个完整的 REST API 示例。

通过本章节的学习，您应该对 Spring Boot 有了全面的了解，包括：

- Spring Boot 的基本概念和优势
- 如何创建和运行 Spring Boot 项目
- Spring Boot 的核心注解和使用方法
- 如何构建一个完整的 REST API 应用
- 常见问题的解决方案

在后续章节中，我们将深入探讨 Spring Boot 的核心配置、Web 开发、数据访问、安全、微服务、监控、测试、部署和最佳实践等高级特性，帮助您成为 Spring Boot 专家。