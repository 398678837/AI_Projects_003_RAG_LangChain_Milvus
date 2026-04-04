# Spring MVC 模型

## 模型概述

模型是 Spring MVC 中的重要组件，用于存储和传递数据。模型可以在控制器和视图之间传递数据，也可以用于存储业务逻辑处理的结果。本章节将详细介绍 Spring MVC 模型的使用方法，帮助开发者掌握模型的创建和使用。

## 模型的类型

### 1. Model

Model 是一个接口，用于存储模型数据。它是 Spring MVC 中最常用的模型类型。

#### 主要方法

- **addAttribute(String attributeName, Object attributeValue)**：添加模型属性
- **addAttribute(Object attributeValue)**：添加模型属性，使用对象的类名作为属性名
- **addAllAttributes(Collection<?> attributes)**：添加多个模型属性
- **addAllAttributes(Map<String, ?> attributes)**：添加多个模型属性
- **getAttribute(String attributeName)**：获取模型属性
- **containsAttribute(String attributeName)**：检查模型是否包含指定属性
- **asMap()**：将模型转换为 Map

#### 示例

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        List<User> users = userService.findAll();
        model.addAttribute("users", users);
        model.addAttribute("message", "User List");
        return "user-list";
    }
}
```

### 2. ModelMap

ModelMap 是 Model 接口的实现类，继承自 LinkedHashMap，具有 Map 的所有功能。

#### 主要方法

- **addAttribute(String attributeName, Object attributeValue)**：添加模型属性
- **addAttribute(Object attributeValue)**：添加模型属性，使用对象的类名作为属性名
- **addAllAttributes(Collection<?> attributes)**：添加多个模型属性
- **addAllAttributes(Map<String, ?> attributes)**：添加多个模型属性
- **get(Object key)**：获取模型属性
- **containsKey(Object key)**：检查模型是否包含指定属性
- **put(String key, Object value)**：添加模型属性

#### 示例

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(ModelMap model) {
        List<User> users = userService.findAll();
        model.addAttribute("users", users);
        model.addAttribute("message", "User List");
        return "user-list";
    }
}
```

### 3. ModelAndView

ModelAndView 是一个类，用于同时存储模型数据和视图信息。

#### 主要方法

- **setViewName(String viewName)**：设置视图名称
- **setView(View view)**：设置视图对象
- **addObject(String attributeName, Object attributeValue)**：添加模型属性
- **addObject(Object attributeValue)**：添加模型属性，使用对象的类名作为属性名
- **addAllObjects(Map<String, ?> modelMap)**：添加多个模型属性
- **getModel()**：获取模型数据
- **getViewName()**：获取视图名称
- **getView()**：获取视图对象

#### 示例

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public ModelAndView listUsers() {
        ModelAndView mav = new ModelAndView("user-list");
        mav.addObject("users", userService.findAll());
        mav.addObject("message", "User List");
        return mav;
    }
}
```

### 4. Map

Map 是 Java 中的接口，也可以用作模型。当控制器方法参数为 Map 时，Spring MVC 会自动创建一个 Map 对象并传递给方法。

#### 示例

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Map<String, Object> model) {
        List<User> users = userService.findAll();
        model.put("users", users);
        model.put("message", "User List");
        return "user-list";
    }
}
```

## 模型的使用

### 1. 在控制器中使用模型

在控制器方法中，通过参数注入模型对象，然后添加模型属性。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;
    
    @GetMapping
    public String listUsers(Model model) {
        List<User> users = userService.findAll();
        model.addAttribute("users", users);
        model.addAttribute("message", "User List");
        return "user-list";
    }
    
    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = userService.findById(id);
        model.addAttribute("user", user);
        model.addAttribute("message", "User Detail");
        return "user-detail";
    }
}
```

### 2. 在视图中使用模型

在视图中，通过表达式语言（如 JSP EL、Thymeleaf 表达式等）访问模型属性。

#### JSP 示例

```jsp
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>${message}</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        <c:forEach items="${users}" var="user">
            <tr>
                <td>${user.id}</td>
                <td>${user.firstName}</td>
                <td>${user.lastName}</td>
            </tr>
        </c:forEach>
    </table>
</body>
</html>
```

#### Thymeleaf 示例

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>User List</title>
</head>
<body>
    <h1 th:text="${message}"></h1>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        <tr th:each="user : ${users}">
            <td th:text="${user.id}"></td>
            <td th:text="${user.firstName}"></td>
            <td th:text="${user.lastName}"></td>
        </tr>
    </table>
</body>
</html>
```

### 3. 模型数据绑定

Spring MVC 支持将请求参数绑定到模型对象。

#### 基本数据类型绑定

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping("/search")
    public String searchUsers(@RequestParam("name") String name, Model model) {
        List<User> users = userService.findByName(name);
        model.addAttribute("users", users);
        model.addAttribute("name", name);
        return "user-list";
    }
}
```

#### 对象绑定

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @PostMapping
    public String createUser(User user, Model model) {
        userService.save(user);
        model.addAttribute("message", "User created successfully");
        return "redirect:/users";
    }
}
```

#### 嵌套对象绑定

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

@Controller
@RequestMapping("/users")
public class UserController {
    @PostMapping
    public String createUser(User user, Model model) {
        userService.save(user);
        model.addAttribute("message", "User created successfully");
        return "redirect:/users";
    }
}
```

#### 集合绑定

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @PostMapping("/batch-delete")
    public String batchDelete(@RequestParam("ids") List<Long> ids, Model model) {
        userService.deleteByIds(ids);
        model.addAttribute("message", "Users deleted successfully");
        return "redirect:/users";
    }
}
```

## 模型的最佳实践

### 1. 保持模型简洁

模型应该只包含必要的数据，避免存储过多的信息。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        // 只添加必要的数据
        model.addAttribute("users", userService.findAll());
        return "user-list";
    }
}
```

### 2. 使用 DTO 模式

使用 DTO（Data Transfer Object）模式，避免直接使用实体类作为模型。

```java
class UserDTO {
    private Long id;
    private String firstName;
    private String lastName;
    // getters and setters
}

@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        List<User> users = userService.findAll();
        List<UserDTO> userDTOs = users.stream()
                .map(user -> new UserDTO(user.getId(), user.getFirstName(), user.getLastName()))
                .collect(Collectors.toList());
        model.addAttribute("users", userDTOs);
        return "user-list";
    }
}
```

### 3. 使用模型属性名常量

使用常量定义模型属性名，避免硬编码。

```java
public class ModelAttributeNames {
    public static final String USERS = "users";
    public static final String USER = "user";
    public static final String MESSAGE = "message";
}

@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        model.addAttribute(ModelAttributeNames.USERS, userService.findAll());
        model.addAttribute(ModelAttributeNames.MESSAGE, "User List");
        return "user-list";
    }
}
```

### 4. 合理使用 ModelAndView

当需要同时设置模型数据和视图信息时，使用 ModelAndView。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public ModelAndView listUsers() {
        ModelAndView mav = new ModelAndView("user-list");
        mav.addObject(ModelAttributeNames.USERS, userService.findAll());
        mav.addObject(ModelAttributeNames.MESSAGE, "User List");
        return mav;
    }
}
```

### 5. 避免在模型中存储敏感信息

避免在模型中存储敏感信息，如密码、令牌等。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = userService.findById(id);
        // 不存储密码等敏感信息
        model.addAttribute(ModelAttributeNames.USER, user);
        return "user-detail";
    }
}
```

## 总结

模型是 Spring MVC 中的重要组件，用于存储和传递数据。Spring MVC 提供了多种模型类型，包括 Model、ModelMap、ModelAndView 和 Map。本章节详细介绍了 Spring MVC 模型的使用方法，包括模型的类型、使用和最佳实践。通过本章节的学习，您应该了解如何在控制器中使用模型，如何在视图中访问模型属性，以及如何遵循模型的最佳实践，构建高效、可维护的 Web 应用程序。