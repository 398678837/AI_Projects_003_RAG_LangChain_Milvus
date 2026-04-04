# Spring MVC 响应处理

## 响应处理概述

响应处理是 Spring MVC 中的重要功能，负责生成和返回 HTTP 响应。Spring MVC 提供了多种方式来处理响应，包括视图渲染、JSON 响应、重定向等。本章节将详细介绍 Spring MVC 响应处理的方法，帮助开发者掌握响应处理的实现。

## 响应类型

### 1. 视图响应

视图响应是最常见的响应类型，返回一个视图名称，由视图解析器解析为实际的视图。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        model.addAttribute("users", userService.findAll());
        return "user-list";
    }
}
```

### 2. 模型与视图响应

模型与视图响应返回一个 ModelAndView 对象，包含模型数据和视图信息。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public ModelAndView listUsers() {
        ModelAndView mav = new ModelAndView("user-list");
        mav.addObject("users", userService.findAll());
        return mav;
    }
}
```

### 3. 重定向响应

重定向响应使用 `redirect:` 前缀，将请求重定向到其他 URL。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @PostMapping
    public String createUser(User user) {
        userService.save(user);
        return "redirect:/users";
    }
}
```

### 4. 转发响应

转发响应使用 `forward:` 前缀，将请求转发到其他控制器方法。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping("/list")
    public String listUsers() {
        return "forward:/users";
    }
}
```

### 5. 响应体

使用 `@ResponseBody` 注解，将方法返回值作为响应体。

```java
@Controller
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    @ResponseBody
    public List<User> listUsers() {
        return userService.findAll();
    }
}
```

### 6. REST 响应

使用 `@RestController` 注解，该注解是 `@Controller` 和 `@ResponseBody` 的组合。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    public List<User> listUsers() {
        return userService.findAll();
    }
}
```

### 7. ResponseEntity 响应

使用 `ResponseEntity` 类，可以设置响应状态码、响应头和响应体。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        User user = userService.findById(id);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        user = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

## 响应状态码

### 1. 成功状态码

- **200 OK**：请求成功
- **201 Created**：资源创建成功
- **202 Accepted**：请求已接受，但尚未处理
- **204 No Content**：请求成功但无内容

### 2. 客户端错误状态码

- **400 Bad Request**：请求参数错误
- **401 Unauthorized**：未授权
- **403 Forbidden**：禁止访问
- **404 Not Found**：资源不存在
- **405 Method Not Allowed**：请求方法不允许
- **406 Not Acceptable**：无法满足请求的内容类型
- **409 Conflict**：请求冲突

### 3. 服务器错误状态码

- **500 Internal Server Error**：服务器内部错误
- **501 Not Implemented**：服务器不支持该功能
- **502 Bad Gateway**：网关错误
- **503 Service Unavailable**：服务不可用
- **504 Gateway Timeout**：网关超时

## 响应头

### 1. 设置响应头

使用 `HttpServletResponse` 对象设置响应头。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping("/download")
    public void download(HttpServletResponse response) throws IOException {
        response.setHeader("Content-Disposition", "attachment; filename=users.csv");
        response.setContentType("text/csv");
        // 写入响应体
    }
}
```

### 2. 使用 ResponseEntity 设置响应头

使用 `ResponseEntity` 类设置响应头。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping("/download")
    public ResponseEntity<byte[]> download() {
        byte[] data = // 生成数据
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
        headers.setContentDispositionFormData("attachment", "users.csv");
        return new ResponseEntity<>(data, headers, HttpStatus.OK);
    }
}
```

## 响应体

### 1. JSON 响应

Spring MVC 会自动将对象转换为 JSON 响应。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    public List<User> listUsers() {
        return userService.findAll();
    }
}
```

### 2. XML 响应

Spring MVC 会自动将对象转换为 XML 响应。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping(produces = MediaType.APPLICATION_XML_VALUE)
    public List<User> listUsers() {
        return userService.findAll();
    }
}
```

### 3. 自定义响应

使用 `ResponseEntity` 类返回自定义响应。

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping("/{id}")
    public ResponseEntity<?> getUser(@PathVariable Long id) {
        User user = userService.findById(id);
        if (user == null) {
            ErrorResponse error = new ErrorResponse("User not found");
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
        }
        return ResponseEntity.ok(user);
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

## 文件下载

### 1. 基本文件下载

```java
@Controller
@RequestMapping("/download")
public class DownloadController {
    @GetMapping("/file")
    public void downloadFile(HttpServletResponse response) throws IOException {
        String fileName = "example.txt";
        response.setHeader("Content-Disposition", "attachment; filename=" + fileName);
        response.setContentType("text/plain");
        try (PrintWriter writer = response.getWriter()) {
            writer.write("Hello, World!");
        }
    }
}
```

### 2. 使用 ResponseEntity 下载

```java
@Controller
@RequestMapping("/download")
public class DownloadController {
    @GetMapping("/file")
    public ResponseEntity<Resource> downloadFile() {
        Resource resource = new ClassPathResource("example.txt");
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=example.txt");
        return ResponseEntity.ok()
                .headers(headers)
                .contentLength(resource.contentLength())
                .contentType(MediaType.APPLICATION_OCTET_STREAM)
                .body(resource);
    }
}
```

## 响应处理的最佳实践

### 1. 使用适当的响应类型

根据请求的类型和内容，选择适当的响应类型：

- **HTML 响应**：使用视图响应，返回 HTML 页面
- **API 响应**：使用 REST 响应，返回 JSON 或 XML
- **文件下载**：使用文件下载响应，返回文件

### 2. 使用适当的状态码

使用适当的 HTTP 状态码，使 API 更加清晰：

- **200 OK**：请求成功
- **201 Created**：资源创建成功
- **204 No Content**：请求成功但无内容
- **400 Bad Request**：请求参数错误
- **401 Unauthorized**：未授权
- **403 Forbidden**：禁止访问
- **404 Not Found**：资源不存在
- **500 Internal Server Error**：服务器内部错误

### 3. 统一响应格式

统一 API 响应格式，使客户端更容易处理：

```java
class ApiResponse<T> {
    private int code;
    private String message;
    private T data;
    
    public ApiResponse(int code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }
    
    // getters and setters
}

@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    public ApiResponse<List<User>> listUsers() {
        List<User> users = userService.findAll();
        return new ApiResponse<>(200, "Success", users);
    }
    
    @GetMapping("/{id}")
    public ApiResponse<User> getUser(@PathVariable Long id) {
        User user = userService.findById(id);
        if (user == null) {
            return new ApiResponse<>(404, "User not found", null);
        }
        return new ApiResponse<>(200, "Success", user);
    }
}
```

### 4. 处理异常

合理处理异常，返回友好的错误信息：

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<?>> handleException(Exception ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(new ApiResponse<>(500, ex.getMessage(), null));
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ApiResponse<?>> handleUserNotFoundException(UserNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(new ApiResponse<>(404, ex.getMessage(), null));
    }
}
```

### 5. 使用缓存

使用缓存，提高响应速度：

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
    @GetMapping
    public ResponseEntity<List<User>> listUsers() {
        List<User> users = userService.findAll();
        return ResponseEntity.ok()
                .cacheControl(CacheControl.maxAge(1, TimeUnit.HOURS))
                .body(users);
    }
}
```

## 总结

响应处理是 Spring MVC 中的重要功能，负责生成和返回 HTTP 响应。Spring MVC 提供了多种方式来处理响应，包括视图响应、模型与视图响应、重定向响应、转发响应、响应体、REST 响应和 ResponseEntity 响应。本章节详细介绍了 Spring MVC 响应处理的方法，包括响应类型、响应状态码、响应头、响应体和文件下载。通过本章节的学习，您应该了解如何选择适当的响应类型，如何设置响应状态码和响应头，如何处理不同类型的响应体，以及如何遵循响应处理的最佳实践，构建高效、可维护的 Web 应用程序。