# Spring Boot Web 开发

## Web 开发概述

Spring Boot 提供了强大的 Web 开发支持，包括 RESTful API 开发、模板引擎、静态资源管理等功能。Spring Boot 的 Web 开发基于 Spring MVC 框架，通过自动配置简化了开发过程。

## 核心组件

### 1. 控制器（Controller）

控制器是处理 HTTP 请求的核心组件，负责接收请求、处理业务逻辑并返回响应。

#### 基本控制器

```java
@RestController
@RequestMapping("/api")
public class UserController {
    
    @GetMapping("/users")
    public List<User> getUsers() {
        // 处理逻辑
    }
    
    @PostMapping("/users")
    public User createUser(@RequestBody User user) {
        // 处理逻辑
    }
}
```

#### 路径变量

```java
@GetMapping("/users/{id}")
public User getUserById(@PathVariable Long id) {
    // 处理逻辑
}
```

#### 请求参数

```java
@GetMapping("/users")
public List<User> getUsers(
    @RequestParam("name") String name,
    @RequestParam("age") int age) {
    // 处理逻辑
}
```

### 2. 服务层（Service）

服务层负责处理业务逻辑，被控制器调用。

```java
@Service
public class UserService {
    public List<User> getUsers() {
        // 业务逻辑
    }
    
    public User createUser(User user) {
        // 业务逻辑
    }
}
```

### 3. 数据访问层（Repository）

数据访问层负责与数据库交互，提供数据持久化功能。

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name);
    List<User> findByAgeGreaterThan(int age);
}
```

## RESTful API 开发

### 1. HTTP 方法

| 方法 | 用途 | 示例 |
|------|------|------|
| GET | 获取资源 | /api/users |
| POST | 创建资源 | /api/users |
| PUT | 更新资源 | /api/users/{id} |
| DELETE | 删除资源 | /api/users/{id} |
| PATCH | 部分更新资源 | /api/users/{id} |

### 2. 响应状态码

| 状态码 | 含义 | 示例 |
|--------|------|------|
| 200 OK | 请求成功 | 获取资源 |
| 201 Created | 资源创建成功 | 创建用户 |
| 204 No Content | 请求成功但无内容 | 删除资源 |
| 400 Bad Request | 请求参数错误 | 无效的用户数据 |
| 401 Unauthorized | 未授权 | 未登录 |
| 403 Forbidden | 禁止访问 | 无权限 |
| 404 Not Found | 资源不存在 | 找不到用户 |
| 500 Internal Server Error | 服务器内部错误 | 代码异常 |

### 3. 响应格式

#### 基本响应

```json
{
  "id": 1,
  "name": "张三",
  "email": "zhangsan@example.com"
}
```

#### 集合响应

```json
[
  {
    "id": 1,
    "name": "张三",
    "email": "zhangsan@example.com"
  },
  {
    "id": 2,
    "name": "李四",
    "email": "lisi@example.com"
  }
]
```

#### 错误响应

```json
{
  "status": 400,
  "message": "无效的请求参数",
  "timestamp": "2023-06-01T10:00:00Z"
}
```

## 模板引擎

Spring Boot 支持多种模板引擎，包括 Thymeleaf、FreeMarker、Velocity 等。默认使用 Thymeleaf。

### 1. Thymeleaf 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

### 2. 模板文件

模板文件放在 `src/main/resources/templates` 目录下。

#### index.html

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Spring Boot Web</title>
</head>
<body>
    <h1>欢迎来到 Spring Boot Web 应用</h1>
    <p th:text="'当前时间：' + ${currentTime}"></p>
    <ul>
        <li th:each="user : ${users}" th:text="${user.name}"></li>
    </ul>
</body>
</html>
```

### 3. 控制器

```java
@Controller
public class HomeController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("currentTime", new Date());
        model.addAttribute("users", userService.getUsers());
        return "index";
    }
}
```

## 静态资源

Spring Boot 默认从以下位置加载静态资源：

- `src/main/resources/static`
- `src/main/resources/public`
- `src/main/resources/resources`
- `src/main/resources/META-INF/resources`

### 1. 静态资源访问

静态资源可以通过相对路径直接访问，例如：

- `http://localhost:8080/css/style.css`
- `http://localhost:8080/js/app.js`
- `http://localhost:8080/images/logo.png`

### 2. 自定义静态资源路径

在 `application.yml` 中配置：

```yaml
spring:
  web:
    resources:
      static-locations: classpath:/static/,classpath:/custom/
```

## 文件上传

### 1. 配置

在 `application.yml` 中配置文件上传大小限制：

```yaml
spring:
  servlet:
    multipart:
      max-file-size: 10MB
      max-request-size: 10MB
```

### 2. 控制器

```java
@RestController
@RequestMapping("/api/files")
public class FileController {
    
    @PostMapping("/upload")
    public String upload(@RequestParam("file") MultipartFile file) throws IOException {
        // 保存文件
        String fileName = file.getOriginalFilename();
        file.transferTo(new File("uploads/" + fileName));
        return "文件上传成功：" + fileName;
    }
}
```

## 异常处理

### 1. 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception e) {
        ErrorResponse error = new ErrorResponse();
        error.setStatus(HttpStatus.INTERNAL_SERVER_ERROR.value());
        error.setMessage(e.getMessage());
        error.setTimestamp(new Date());
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
    
    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFoundException(NotFoundException e) {
        ErrorResponse error = new ErrorResponse();
        error.setStatus(HttpStatus.NOT_FOUND.value());
        error.setMessage(e.getMessage());
        error.setTimestamp(new Date());
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }
}
```

### 2. 自定义异常

```java
public class NotFoundException extends RuntimeException {
    public NotFoundException(String message) {
        super(message);
    }
}
```

## 跨域处理

### 1. 注解方式

```java
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*", maxAge = 3600)
public class UserController {
    // 控制器方法
}
```

### 2. 全局配置

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("*")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("*")
                .maxAge(3600);
    }
}
```

## 示例：完整的 Web 应用

### 1. 项目结构

```
my-web-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── MyWebApplication.java
│   │   │           ├── controller/
│   │   │           │   ├── UserController.java
│   │   │           │   └── HomeController.java
│   │   │           ├── service/
│   │   │           │   └── UserService.java
│   │   │           ├── repository/
│   │   │           │   └── UserRepository.java
│   │   │           ├── model/
│   │   │           │   └── User.java
│   │   │           └── exception/
│   │   │               ├── GlobalExceptionHandler.java
│   │   │               └── NotFoundException.java
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── templates/
│   │       │   └── index.html
│   │       └── static/
│   │           ├── css/
│   │           │   └── style.css
│   │           └── js/
│   │               └── app.js
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
        return userService.getUserById(id)
                .orElseThrow(() -> new NotFoundException("用户不存在"));
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        return userService.updateUser(id, user)
                .orElseThrow(() -> new NotFoundException("用户不存在"));
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
    
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }
    
    public User createUser(User user) {
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

### 4. 数据访问层

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name);
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
    
    // 构造方法、getter 和 setter 方法
}
```

## 最佳实践

### 1. 控制器设计

- 遵循 RESTful 设计原则
- 使用适当的 HTTP 方法和状态码
- 控制器应该保持简洁，只负责处理请求和响应
- 业务逻辑应该放在服务层

### 2. 响应格式

- 统一响应格式
- 包含适当的状态码和消息
- 对于错误响应，提供详细的错误信息

### 3. 异常处理

- 使用全局异常处理器
- 自定义业务异常
- 提供友好的错误信息

### 4. 性能优化

- 使用缓存减少数据库查询
- 优化 SQL 查询
- 使用异步处理提高并发性能
- 合理设置连接池大小

### 5. 安全性

- 验证请求参数
- 防止 SQL 注入
- 防止 XSS 攻击
- 实现适当的认证和授权

## 常见问题

### 1. 404 错误

- 检查控制器的 `@RequestMapping` 注解
- 检查请求路径是否正确
- 检查应用上下文路径配置

### 2. 500 错误

- 检查代码中是否有异常
- 查看日志了解详细错误信息
- 检查数据库连接是否正常

### 3. 跨域问题

- 配置 CORS 策略
- 使用 `@CrossOrigin` 注解
- 检查前端请求是否包含正确的 headers

### 4. 文件上传失败

- 检查文件大小限制配置
- 检查文件路径权限
- 检查请求是否正确设置了 `Content-Type`

## 总结

Spring Boot 提供了强大的 Web 开发支持，通过自动配置和约定优于配置的原则，简化了 Web 应用的开发过程。本章节介绍了 Spring Boot Web 开发的核心组件、RESTful API 开发、模板引擎、静态资源管理、文件上传、异常处理和跨域处理等功能。通过本章节的学习，您应该能够构建一个完整的 Spring Boot Web 应用。