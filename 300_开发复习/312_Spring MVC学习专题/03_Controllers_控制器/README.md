# Spring MVC 控制器

## 控制器概述

控制器是 Spring MVC 中的核心组件，负责处理用户请求，调用相应的业务逻辑，并返回响应。本章节将详细介绍 Spring MVC 控制器的使用方法，帮助开发者掌握控制器的编写和配置。

## 控制器的定义

在 Spring MVC 中，控制器是一个带有 `@Controller` 注解的类，用于处理 HTTP 请求。

### 基本控制器

```java
@Controller
public class HelloController {
    @GetMapping("/hello")
    public String hello(Model model) {
        model.addAttribute("message", "Hello, Spring MVC!");
        return "hello";
    }
}
```

### REST 控制器

REST 控制器是一种特殊的控制器，用于创建 RESTful API。它使用 `@RestController` 注解，该注解是 `@Controller` 和 `@ResponseBody` 的组合。

```java
@RestController
@RequestMapping("/api")
public class ApiController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, REST API!";
    }
}
```

## 控制器的映射

### 类级别映射

使用 `@RequestMapping` 注解在类级别定义基本路径。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    // 方法级别映射
}
```

### 方法级别映射

使用 `@RequestMapping` 或其变体（如 `@GetMapping`、`@PostMapping` 等）在方法级别定义具体路径。

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

## 控制器的参数

### 路径变量

使用 `@PathVariable` 注解获取 URL 中的路径变量。

```java
@GetMapping("/users/{id}")
public String getUser(@PathVariable Long id, Model model) {
    // 使用 id 参数
    return "user-detail";
}
```

### 请求参数

使用 `@RequestParam` 注解获取请求参数。

```java
@GetMapping("/users")
public String listUsers(@RequestParam("page") int page, @RequestParam("size") int size, Model model) {
    // 使用 page 和 size 参数
    return "user-list";
}
```

### 请求体

使用 `@RequestBody` 注解获取请求体。

```java
@PostMapping("/api/users")
public User createUser(@RequestBody User user) {
    // 使用 user 对象
    return user;
}
```

### 请求头

使用 `@RequestHeader` 注解获取请求头。

```java
@GetMapping("/api/users")
public List<User> listUsers(@RequestHeader("Authorization") String authorization) {
    // 使用 authorization 请求头
    return users;
}
```

### Cookie

使用 `@CookieValue` 注解获取 Cookie。

```java
@GetMapping("/api/users")
public List<User> listUsers(@CookieValue("sessionId") String sessionId) {
    // 使用 sessionId Cookie
    return users;
}
```

### 模型

使用 `Model` 接口存储模型数据。

```java
@GetMapping("/users")
public String listUsers(Model model) {
    model.addAttribute("users", userService.findAll());
    return "user-list";
}
```

### HttpServletRequest 和 HttpServletResponse

直接使用 `HttpServletRequest` 和 `HttpServletResponse` 对象。

```java
@GetMapping("/users")
public String listUsers(HttpServletRequest request, HttpServletResponse response) {
    // 使用 request 和 response 对象
    return "user-list";
}
```

### Principal

使用 `Principal` 对象获取当前用户。

```java
@GetMapping("/users/me")
public String getCurrentUser(Principal principal, Model model) {
    String username = principal.getName();
    // 使用 username
    return "user-detail";
}
```

## 控制器的返回值

### 视图名称

返回字符串作为视图名称。

```java
@GetMapping("/users")
public String listUsers(Model model) {
    return "user-list";
}
```

### ModelAndView

返回 `ModelAndView` 对象，包含模型数据和视图信息。

```java
@GetMapping("/users")
public ModelAndView listUsers() {
    ModelAndView mav = new ModelAndView("user-list");
    mav.addObject("users", userService.findAll());
    return mav;
}
```

### 重定向

使用 `redirect:` 前缀重定向到其他 URL。

```java
@PostMapping("/users")
public String createUser(User user) {
    userService.save(user);
    return "redirect:/users";
}
```

### 转发

使用 `forward:` 前缀转发到其他控制器方法。

```java
@GetMapping("/users/list")
public String listUsers() {
    return "forward:/users";
}
```

### 响应体

使用 `@ResponseBody` 注解将方法返回值作为响应体。

```java
@GetMapping("/api/users")
@ResponseBody
public List<User> listUsers() {
    return userService.findAll();
}
```

### ResponseEntity

返回 `ResponseEntity` 对象，包含响应状态码、响应头和响应体。

```java
@GetMapping("/api/users/{id}")
public ResponseEntity<User> getUser(@PathVariable Long id) {
    User user = userService.findById(id);
    if (user == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(user);
}
```

## 控制器的异常处理

### @ExceptionHandler

使用 `@ExceptionHandler` 注解处理控制器中的异常。

```java
@Controller
public class UserController {
    @GetMapping("/users/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = userService.findById(id);
        if (user == null) {
            throw new UserNotFoundException("User not found");
        }
        model.addAttribute("user", user);
        return "user-detail";
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public String handleUserNotFoundException(UserNotFoundException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "error";
    }
}
```

### @ControllerAdvice

使用 `@ControllerAdvice` 注解全局处理异常。

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public String handleException(Exception ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "error";
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public String handleUserNotFoundException(UserNotFoundException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "user-error";
    }
}
```

## 控制器的测试

### 单元测试

使用 Spring MVC Test 框架测试控制器。

```java
@RunWith(SpringRunner.class)
@WebMvcTest(UserController.class)
public class UserControllerTest {
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    public void testListUsers() throws Exception {
        List<User> users = Arrays.asList(new User(1L, "John", "Doe"));
        when(userService.findAll()).thenReturn(users);
        
        mockMvc.perform(get("/users"))
                .andExpect(status().isOk())
                .andExpect(view().name("user-list"))
                .andExpect(model().attributeExists("users"));
    }
}
```

### 集成测试

使用 Spring Boot Test 框架测试整个应用。

```java
@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class UserControllerIntegrationTest {
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    public void testListUsers() {
        ResponseEntity<List<User>> response = restTemplate.exchange(
                "/api/users",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<User>>() {}
        );
        
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody()).isNotNull();
    }
}
```

## 控制器的最佳实践

### 1. 保持控制器简洁

控制器应该只负责处理请求，调用业务逻辑，并返回响应。避免在控制器中编写业务逻辑。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;
    
    @GetMapping
    public String listUsers(Model model) {
        model.addAttribute("users", userService.findAll());
        return "user-list";
    }
}
```

### 2. 使用 REST 风格的 URL

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

### 3. 使用适当的 HTTP 方法

使用适当的 HTTP 方法，符合 REST 风格。

- **GET**：获取资源
- **POST**：创建资源
- **PUT**：更新资源
- **DELETE**：删除资源
- **PATCH**：部分更新资源

### 4. 使用适当的状态码

使用适当的 HTTP 状态码，使 API 更加清晰。

- **200 OK**：请求成功
- **201 Created**：资源创建成功
- **204 No Content**：请求成功但无内容
- **400 Bad Request**：请求参数错误
- **401 Unauthorized**：未授权
- **403 Forbidden**：禁止访问
- **404 Not Found**：资源不存在
- **500 Internal Server Error**：服务器内部错误

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

### 6. 验证输入

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

## 总结

控制器是 Spring MVC 中的核心组件，负责处理用户请求，调用相应的业务逻辑，并返回响应。本章节详细介绍了 Spring MVC 控制器的使用方法，包括控制器的定义、映射、参数、返回值、异常处理和测试。通过本章节的学习，您应该掌握控制器的编写和配置方法，了解如何创建 RESTful API，以及如何处理异常和验证输入。在实际开发中，应该遵循控制器的最佳实践，保持控制器简洁，使用 REST 风格的 URL，使用适当的 HTTP 方法和状态码，合理处理异常，验证输入数据，构建高效、可维护的 Web 应用程序。