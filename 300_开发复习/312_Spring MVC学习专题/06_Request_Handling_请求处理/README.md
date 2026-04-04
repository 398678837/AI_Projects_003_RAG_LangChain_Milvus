# Spring MVC 请求处理

## 请求处理概述

请求处理是 Spring MVC 中的核心功能，负责处理客户端发送的 HTTP 请求。Spring MVC 提供了多种方式来处理请求，包括路径映射、参数解析、文件上传等。本章节将详细介绍 Spring MVC 请求处理的方法，帮助开发者掌握请求处理的实现。

## 请求映射

### 1. 路径映射

使用 `@RequestMapping` 及其变体注解进行路径映射。

#### @RequestMapping

`@RequestMapping` 注解可以指定 HTTP 方法、路径、参数等。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @RequestMapping(method = RequestMethod.GET)
    public String listUsers(Model model) {
        // 处理 GET 请求
        return "user-list";
    }
    
    @RequestMapping(method = RequestMethod.POST)
    public String createUser(User user) {
        // 处理 POST 请求
        return "redirect:/users";
    }
}
```

#### @GetMapping

`@GetMapping` 注解用于映射 HTTP GET 请求。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        // 处理 GET 请求
        return "user-list";
    }
    
    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        // 处理 GET 请求，获取指定 ID 的用户
        return "user-detail";
    }
}
```

#### @PostMapping

`@PostMapping` 注解用于映射 HTTP POST 请求。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @PostMapping
    public String createUser(User user) {
        // 处理 POST 请求，创建用户
        return "redirect:/users";
    }
}
```

#### @PutMapping

`@PutMapping` 注解用于映射 HTTP PUT 请求。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        // 处理 PUT 请求，更新用户
        return user;
    }
}
```

#### @DeleteMapping

`@DeleteMapping` 注解用于映射 HTTP DELETE 请求。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        // 处理 DELETE 请求，删除用户
    }
}
```

#### @PatchMapping

`@PatchMapping` 注解用于映射 HTTP PATCH 请求。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @PatchMapping("/{id}")
    public User patchUser(@PathVariable Long id, @RequestBody Map<String, Object> updates) {
        // 处理 PATCH 请求，部分更新用户
        return user;
    }
}
```

### 2. 路径变量

使用 `@PathVariable` 注解获取 URL 中的路径变量。

```java
@GetMapping("/users/{id}")
public String getUser(@PathVariable Long id, Model model) {
    // 使用 id 参数
    return "user-detail";
}
```

### 3. 请求参数

使用 `@RequestParam` 注解获取请求参数。

```java
@GetMapping("/users")
public String listUsers(@RequestParam("page") int page, @RequestParam("size") int size, Model model) {
    // 使用 page 和 size 参数
    return "user-list";
}
```

### 4. 请求头

使用 `@RequestHeader` 注解获取请求头。

```java
@GetMapping("/api/users")
public List<User> listUsers(@RequestHeader("Authorization") String authorization) {
    // 使用 authorization 请求头
    return users;
}
```

### 5. Cookie

使用 `@CookieValue` 注解获取 Cookie。

```java
@GetMapping("/api/users")
public List<User> listUsers(@CookieValue("sessionId") String sessionId) {
    // 使用 sessionId Cookie
    return users;
}
```

## 参数解析

### 1. 基本类型参数

Spring MVC 会自动将请求参数转换为基本类型。

```java
@GetMapping("/users")
public String listUsers(@RequestParam("page") int page, @RequestParam("size") int size, Model model) {
    // 使用 page 和 size 参数
    return "user-list";
}
```

### 2. 对象参数

Spring MVC 会自动将请求参数绑定到对象的属性。

```java
@PostMapping("/users")
public String createUser(User user) {
    // 使用 user 对象
    return "redirect:/users";
}
```

### 3. 嵌套对象参数

Spring MVC 会自动将请求参数绑定到嵌套对象的属性。

```java
class User {
    private Long id;
    private String firstName;
    private String lastName;
    private Address address;
    // getters and setters
}

class Address {
    private String street;
    private String city;
    private String state;
    private String zipCode;
    // getters and setters
}

@PostMapping("/users")
public String createUser(User user) {
    // 使用 user 对象，包括嵌套的 address 对象
    return "redirect:/users";
}
```

### 4. 集合参数

Spring MVC 会自动将请求参数绑定到集合。

```java
@PostMapping("/users/batch-delete")
public String batchDelete(@RequestParam("ids") List<Long> ids) {
    // 使用 ids 集合
    return "redirect:/users";
}
```

### 5. 数组参数

Spring MVC 会自动将请求参数绑定到数组。

```java
@PostMapping("/users/batch-delete")
public String batchDelete(@RequestParam("ids") Long[] ids) {
    // 使用 ids 数组
    return "redirect:/users";
}
```

### 6. 地图参数

Spring MVC 会自动将请求参数绑定到 Map。

```java
@PostMapping("/users/update")
public String updateUser(@RequestParam Map<String, String> params) {
    // 使用 params Map
    return "redirect:/users";
}
```

### 7. 请求体参数

使用 `@RequestBody` 注解获取请求体。

```java
@PostMapping("/api/users")
public User createUser(@RequestBody User user) {
    // 使用 user 对象
    return user;
}
```

## 文件上传

### 1. 单文件上传

使用 `@RequestParam` 注解获取上传的文件。

```java
@PostMapping("/upload")
public String uploadFile(@RequestParam("file") MultipartFile file) {
    // 处理上传的文件
    return "upload-success";
}
```

### 2. 多文件上传

使用 `@RequestParam` 注解获取上传的多个文件。

```java
@PostMapping("/upload-multiple")
public String uploadMultipleFiles(@RequestParam("files") MultipartFile[] files) {
    // 处理上传的多个文件
    return "upload-success";
}
```

### 3. 配置文件上传

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Bean
    public MultipartResolver multipartResolver() {
        CommonsMultipartResolver resolver = new CommonsMultipartResolver();
        resolver.setMaxUploadSize(10485760); // 10MB
        return resolver;
    }
}
```

**application.properties**：

```properties
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=10MB
```

## 请求处理的最佳实践

### 1. 使用 REST 风格的 URL

使用 REST 风格的 URL，使 API 更加清晰和一致。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    public List<User> listUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.save(user);
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return userService.save(user);
    }
    
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.delete(id);
    }
}
```

### 2. 使用适当的 HTTP 方法

使用适当的 HTTP 方法，符合 REST 风格。

- **GET**：获取资源
- **POST**：创建资源
- **PUT**：更新资源
- **DELETE**：删除资源
- **PATCH**：部分更新资源

### 3. 使用适当的状态码

使用适当的 HTTP 状态码，使 API 更加清晰。

- **200 OK**：请求成功
- **201 Created**：资源创建成功
- **204 No Content**：请求成功但无内容
- **400 Bad Request**：请求参数错误
- **401 Unauthorized**：未授权
- **403 Forbidden**：禁止访问
- **404 Not Found**：资源不存在
- **500 Internal Server Error**：服务器内部错误

### 4. 验证输入

验证用户输入，确保数据的合法性。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user, BindingResult result) {
        if (result.hasErrors()) {
            return ResponseEntity.badRequest().build();
        }
        return ResponseEntity.status(HttpStatus.CREATED).body(userService.save(user));
    }
}

class User {
    @NotNull
    @Size(min = 1, max = 50)
    private String firstName;
    
    @NotNull
    @Size(min = 1, max = 50)
    private String lastName;
    
    // getters and setters
}
```

### 5. 处理异常

合理处理异常，返回友好的错误信息。

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public ResponseEntity<?> handleException(Exception ex) {
        ErrorResponse error = new ErrorResponse(ex.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<?> handleUserNotFoundException(UserNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
}

class ErrorResponse {
    private String message;
    
    public ErrorResponse(String message) {
        this.message = message;
    }
    
    public String getMessage() {
        return message;
    }
}
```

### 6. 使用 DTO 模式

使用 DTO（Data Transfer Object）模式，避免直接使用实体类作为请求和响应对象。

```java
class UserDTO {
    private Long id;
    private String firstName;
    private String lastName;
    // getters and setters
}

@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody UserDTO userDTO) {
        User user = new User();
        user.setFirstName(userDTO.getFirstName());
        user.setLastName(userDTO.getLastName());
        user = userService.save(user);
        userDTO.setId(user.getId());
        return ResponseEntity.status(HttpStatus.CREATED).body(userDTO);
    }
}
```

## 总结

请求处理是 Spring MVC 中的核心功能，负责处理客户端发送的 HTTP 请求。Spring MVC 提供了多种方式来处理请求，包括路径映射、参数解析、文件上传等。本章节详细介绍了 Spring MVC 请求处理的方法，包括请求映射、参数解析、文件上传和最佳实践。通过本章节的学习，您应该了解如何使用注解进行路径映射，如何解析请求参数，如何处理文件上传，以及如何遵循请求处理的最佳实践，构建高效、可维护的 Web 应用程序。