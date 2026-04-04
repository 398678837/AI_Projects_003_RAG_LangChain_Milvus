# Spring MVC 视图

## 视图概述

视图是 Spring MVC 中的重要组件，负责将模型数据渲染为响应。Spring MVC 支持多种视图技术，包括 JSP、Thymeleaf、FreeMarker 等。本章节将详细介绍 Spring MVC 视图的使用方法，帮助开发者掌握视图的配置和使用。

## 视图技术

### 1. JSP

JSP（JavaServer Pages）是一种传统的视图技术，使用 Java 代码和 HTML 标签混合编写。

#### 配置

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Bean
    public InternalResourceViewResolver viewResolver() {
        InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
        viewResolver.setPrefix("/WEB-INF/views/");
        viewResolver.setSuffix(".jsp");
        return viewResolver;
    }
}
```

#### 示例

**/WEB-INF/views/hello.jsp**：

```jsp
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
```

### 2. Thymeleaf

Thymeleaf 是一种现代的服务器端 Java 模板引擎，支持 HTML5，易于集成到 Spring 应用中。

#### 依赖

**Maven**：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

**Gradle**：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
```

#### 配置

**application.properties**：

```properties
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html
spring.thymeleaf.mode=HTML5
spring.thymeleaf.encoding=UTF-8
spring.thymeleaf.cache=false
```

#### 示例

**/src/main/resources/templates/hello.html**：

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
</head>
<body>
    <h1 th:text="${message}"></h1>
</body>
</html>
```

### 3. FreeMarker

FreeMarker 是一种模板引擎，使用模板文件生成文本输出。

#### 依赖

**Maven**：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```

**Gradle**：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-freemarker'
```

#### 配置

**application.properties**：

```properties
spring.freemarker.template-loader-path=classpath:/templates/
spring.freemarker.suffix=.ftl
spring.freemarker.charset=UTF-8
spring.freemarker.cache=false
```

#### 示例

**/src/main/resources/templates/hello.ftl**：

```ftl
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
```

### 4. Velocity

Velocity 是一种模板引擎，使用模板文件生成文本输出。

#### 依赖

**Maven**：

```xml
<dependency>
    <groupId>org.apache.velocity</groupId>
    <artifactId>velocity</artifactId>
    <version>1.7</version>
</dependency>
<dependency>
    <groupId>org.apache.velocity</groupId>
    <artifactId>velocity-tools</artifactId>
    <version>2.0</version>
</dependency>
```

**Gradle**：

```gradle
implementation 'org.apache.velocity:velocity:1.7'
implementation 'org.apache.velocity:velocity-tools:2.0'
```

#### 配置

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Bean
    public VelocityViewResolver viewResolver() {
        VelocityViewResolver viewResolver = new VelocityViewResolver();
        viewResolver.setPrefix("/WEB-INF/views/");
        viewResolver.setSuffix(".vm");
        return viewResolver;
    }
}
```

#### 示例

**/WEB-INF/views/hello.vm**：

```vm
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>$message</h1>
</body>
</html>
```

## 视图解析器

### 1. InternalResourceViewResolver

InternalResourceViewResolver 用于解析 JSP 视图。

```java
@Bean
public InternalResourceViewResolver viewResolver() {
    InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
    viewResolver.setPrefix("/WEB-INF/views/");
    viewResolver.setSuffix(".jsp");
    return viewResolver;
}
```

### 2. ThymeleafViewResolver

ThymeleafViewResolver 用于解析 Thymeleaf 视图。

```java
@Bean
public ThymeleafViewResolver viewResolver() {
    ThymeleafViewResolver viewResolver = new ThymeleafViewResolver();
    viewResolver.setTemplateEngine(templateEngine());
    viewResolver.setCharacterEncoding("UTF-8");
    return viewResolver;
}

@Bean
public SpringTemplateEngine templateEngine() {
    SpringTemplateEngine templateEngine = new SpringTemplateEngine();
    templateEngine.setTemplateResolver(templateResolver());
    return templateEngine;
}

@Bean
public ITemplateResolver templateResolver() {
    SpringResourceTemplateResolver templateResolver = new SpringResourceTemplateResolver();
    templateResolver.setPrefix("classpath:/templates/");
    templateResolver.setSuffix(".html");
    templateResolver.setTemplateMode(TemplateMode.HTML);
    templateResolver.setCharacterEncoding("UTF-8");
    return templateResolver;
}
```

### 3. FreeMarkerViewResolver

FreeMarkerViewResolver 用于解析 FreeMarker 视图。

```java
@Bean
public FreeMarkerViewResolver viewResolver() {
    FreeMarkerViewResolver viewResolver = new FreeMarkerViewResolver();
    viewResolver.setPrefix("");
    viewResolver.setSuffix(".ftl");
    viewResolver.setContentType("text/html;charset=UTF-8");
    return viewResolver;
}

@Bean
public FreeMarkerConfigurer freeMarkerConfigurer() {
    FreeMarkerConfigurer configurer = new FreeMarkerConfigurer();
    configurer.setTemplateLoaderPath("classpath:/templates/");
    return configurer;
}
```

### 4. ContentNegotiatingViewResolver

ContentNegotiatingViewResolver 根据请求的内容类型选择合适的视图解析器。

```java
@Bean
public ContentNegotiatingViewResolver viewResolver() {
    ContentNegotiatingViewResolver viewResolver = new ContentNegotiatingViewResolver();
    viewResolver.setViewResolvers(Arrays.asList(
            internalResourceViewResolver(),
            thymeleafViewResolver()
    ));
    return viewResolver;
}

@Bean
public InternalResourceViewResolver internalResourceViewResolver() {
    InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
    viewResolver.setPrefix("/WEB-INF/views/");
    viewResolver.setSuffix(".jsp");
    return viewResolver;
}

@Bean
public ThymeleafViewResolver thymeleafViewResolver() {
    ThymeleafViewResolver viewResolver = new ThymeleafViewResolver();
    viewResolver.setTemplateEngine(templateEngine());
    viewResolver.setCharacterEncoding("UTF-8");
    return viewResolver;
}
```

## 视图的使用

### 1. 基本使用

在控制器中返回视图名称，Spring MVC 会根据视图解析器解析为实际的视图。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @GetMapping
    public String hello(Model model) {
        model.addAttribute("message", "Hello, Spring MVC!");
        return "hello";
    }
}
```

### 2. 模型数据

在控制器中使用 Model 对象存储模型数据，视图可以访问这些数据。

```java
@Controller
@RequestMapping("/users")
public class UserController {
    @GetMapping
    public String listUsers(Model model) {
        List<User> users = userService.findAll();
        model.addAttribute("users", users);
        return "user-list";
    }
}
```

### 3. 视图参数

在控制器中使用 ModelAndView 对象设置视图参数。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @GetMapping
    public ModelAndView hello() {
        ModelAndView mav = new ModelAndView("hello");
        mav.addObject("message", "Hello, Spring MVC!");
        return mav;
    }
}
```

### 4. 重定向

使用 `redirect:` 前缀重定向到其他 URL。

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

### 5. 转发

使用 `forward:` 前缀转发到其他控制器方法。

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

## 视图的最佳实践

### 1. 选择合适的视图技术

根据项目需求选择合适的视图技术：

- **JSP**：传统的视图技术，适用于遗留项目
- **Thymeleaf**：现代的视图技术，支持 HTML5，推荐使用
- **FreeMarker**：模板引擎，适用于复杂的模板需求
- **Velocity**：模板引擎，适用于简单的模板需求

### 2. 合理组织视图文件

合理组织视图文件，按照功能模块分类：

```
templates/
├── user/
│   ├── user-list.html
│   ├── user-detail.html
│   └── user-form.html
├── product/
│   ├── product-list.html
│   ├── product-detail.html
│   └── product-form.html
└── common/
    ├── header.html
    └── footer.html
```

### 3. 使用模板继承

使用模板继承，减少重复代码：

**Thymeleaf 示例**：

**/src/main/resources/templates/layouts/main.html**：

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title th:text="${title}"></title>
</head>
<body>
    <header>
        <h1>My Application</h1>
    </header>
    <main>
        <div th:fragment="content"></div>
    </main>
    <footer>
        <p>© 2024 My Application</p>
    </footer>
</body>
</html>
```

**/src/main/resources/templates/hello.html**：

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org" th:replace="layouts/main :: html">
<head>
    <title>Hello</title>
</head>
<body>
    <div th:fragment="content">
        <h1 th:text="${message}"></h1>
    </div>
</body>
</html>
```

### 4. 使用片段

使用片段，复用视图代码：

**Thymeleaf 示例**：

**/src/main/resources/templates/common/header.html**：

```html
<header th:fragment="header">
    <h1>My Application</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/products">Products</a></li>
        </ul>
    </nav>
</header>
```

**/src/main/resources/templates/hello.html**：

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
</head>
<body>
    <div th:replace="common/header :: header"></div>
    <h1 th:text="${message}"></h1>
</body>
</html>
```

### 5. 避免在视图中编写业务逻辑

视图应该只负责展示数据，避免在视图中编写业务逻辑。

**不好的示例**：

```jsp
<% 
    List<User> users = userService.findAll();
    for (User user : users) {
        out.println(user.getFirstName() + " " + user.getLastName());
    }
%>
```

**好的示例**：

```jsp
<c:forEach items="${users}" var="user">
    <tr>
        <td>${user.firstName}</td>
        <td>${user.lastName}</td>
    </tr>
</c:forEach>
```

### 6. 使用国际化

使用国际化，支持多语言：

**Thymeleaf 示例**：

**/src/main/resources/messages.properties**：

```properties
welcome.message=Hello, {0}!
```

**/src/main/resources/messages_zh_CN.properties**：

```properties
welcome.message=你好, {0}!
```

**/src/main/resources/templates/hello.html**：

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
</head>
<body>
    <h1 th:text="#{welcome.message(${name})}"></h1>
</body>
</html>
```

## 总结

视图是 Spring MVC 中的重要组件，负责将模型数据渲染为响应。Spring MVC 支持多种视图技术，包括 JSP、Thymeleaf、FreeMarker 等。本章节详细介绍了 Spring MVC 视图的使用方法，包括视图技术、视图解析器、视图的使用和最佳实践。通过本章节的学习，您应该了解如何选择和配置视图技术，如何在控制器中使用视图，以及如何遵循视图的最佳实践，构建美观、可维护的 Web 应用程序。