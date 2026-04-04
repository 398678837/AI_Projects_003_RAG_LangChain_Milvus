# Spring MVC 基础概念

## 基础概念概述

Spring MVC 是 Spring 框架的一个模块，用于构建 Web 应用程序。它基于 MVC（Model-View-Controller）设计模式，提供了一种清晰的方式来组织 Web 应用的代码结构。本章节将详细介绍 Spring MVC 的基础概念，帮助开发者了解 Spring MVC 的工作原理。

## MVC 设计模式

MVC 是一种软件架构设计模式，将应用程序分为三个部分：

- **Model（模型）**：负责数据和业务逻辑
- **View（视图）**：负责展示数据
- **Controller（控制器）**：负责处理用户请求，协调模型和视图

### 工作流程

1. **用户发送请求**：用户通过浏览器向服务器发送请求
2. **控制器处理请求**：控制器接收请求，调用相应的业务逻辑
3. **模型处理业务逻辑**：模型执行业务逻辑，更新数据
4. **控制器更新视图**：控制器将模型数据传递给视图
5. **视图渲染响应**：视图将数据渲染为 HTML 响应
6. **服务器返回响应**：服务器将响应返回给浏览器

## Spring MVC 的核心概念

### 1. DispatcherServlet

DispatcherServlet 是 Spring MVC 的核心组件，负责处理所有的 HTTP 请求。它的主要职责包括：

- **请求映射**：将请求映射到相应的控制器方法
- **参数解析**：解析请求参数
- **视图解析**：将逻辑视图名解析为实际的视图
- **异常处理**：处理请求处理过程中的异常

### 2. HandlerMapping

HandlerMapping 负责将请求映射到相应的处理器（控制器方法）。Spring MVC 提供了多种 HandlerMapping 实现：

- **RequestMappingHandlerMapping**：基于 @RequestMapping 注解的映射
- **SimpleUrlHandlerMapping**：基于 URL 模式的映射
- **BeanNameUrlHandlerMapping**：基于 bean 名称的映射

### 3. HandlerAdapter

HandlerAdapter 负责调用处理器（控制器方法）。Spring MVC 提供了多种 HandlerAdapter 实现：

- **RequestMappingHandlerAdapter**：处理基于 @RequestMapping 注解的控制器方法
- **HttpRequestHandlerAdapter**：处理实现 HttpRequestHandler 接口的处理器
- **SimpleControllerHandlerAdapter**：处理实现 Controller 接口的控制器

### 4. ViewResolver

ViewResolver 负责将逻辑视图名解析为实际的视图。Spring MVC 提供了多种 ViewResolver 实现：

- **InternalResourceViewResolver**：解析 JSP 视图
- **FreeMarkerViewResolver**：解析 FreeMarker 视图
- **ThymeleafViewResolver**：解析 Thymeleaf 视图

### 5. Model

Model 是一个接口，用于存储模型数据。它的主要方法包括：

- **addAttribute(String attributeName, Object attributeValue)**：添加模型属性
- **getAttribute(String attributeName)**：获取模型属性
- **containsAttribute(String attributeName)**：检查模型是否包含指定属性

### 6. ModelAndView

ModelAndView 是一个类，用于同时存储模型数据和视图信息。它的主要方法包括：

- **setViewName(String viewName)**：设置视图名称
- **addObject(String attributeName, Object attributeValue)**：添加模型属性
- **getModel()**：获取模型数据
- **getViewName()**：获取视图名称

## Spring MVC 的工作流程

1. **用户发送请求**：用户通过浏览器向服务器发送 HTTP 请求
2. **DispatcherServlet 接收请求**：DispatcherServlet 接收请求并开始处理
3. **HandlerMapping 解析请求**：HandlerMapping 将请求映射到相应的处理器
4. **HandlerAdapter 调用处理器**：HandlerAdapter 调用处理器方法，处理业务逻辑
5. **处理器返回 ModelAndView**：处理器执行完毕后，返回 ModelAndView 对象
6. **ViewResolver 解析视图**：ViewResolver 将逻辑视图名解析为实际的视图
7. **视图渲染响应**：视图将模型数据渲染为 HTML 响应
8. **DispatcherServlet 返回响应**：DispatcherServlet 将响应返回给浏览器

## Spring MVC 的配置方式

### 1. XML 配置

**web.xml**：

```xml
<web-app>
    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

**spring-mvc.xml**：

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
                           http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context
                           http://www.springframework.org/schema/context/spring-context.xsd
                           http://www.springframework.org/schema/mvc
                           http://www.springframework.org/schema/mvc/spring-mvc.xsd">
    
    <context:component-scan base-package="com.example"/>
    <mvc:annotation-driven/>
    
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
</beans>
```

### 2. Java 配置

**WebConfig.java**：

```java
@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.example")
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

**DispatcherServletInitializer.java**：

```java
public class DispatcherServletInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {
    @Override
    protected Class<?>[] getRootConfigClasses() {
        return null;
    }
    
    @Override
    protected Class<?>[] getServletConfigClasses() {
        return new Class<?>[]{WebConfig.class};
    }
    
    @Override
    protected String[] getServletMappings() {
        return new String[]{"/"};
    }
}
```

## Spring MVC 的注解

### 1. @Controller

@Controller 注解用于标记一个类为控制器。

```java
@Controller
public class HelloController {
    // 控制器方法
}
```

### 2. @RequestMapping

@RequestMapping 注解用于映射请求路径。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @RequestMapping(method = RequestMethod.GET)
    public String hello() {
        return "hello";
    }
}
```

### 3. @GetMapping

@GetMapping 注解用于映射 HTTP GET 请求。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @GetMapping
    public String hello() {
        return "hello";
    }
}
```

### 4. @PostMapping

@PostMapping 注解用于映射 HTTP POST 请求。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @PostMapping
    public String hello() {
        return "hello";
    }
}
```

### 5. @PutMapping

@PutMapping 注解用于映射 HTTP PUT 请求。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @PutMapping
    public String hello() {
        return "hello";
    }
}
```

### 6. @DeleteMapping

@DeleteMapping 注解用于映射 HTTP DELETE 请求。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @DeleteMapping
    public String hello() {
        return "hello";
    }
}
```

### 7. @PatchMapping

@PatchMapping 注解用于映射 HTTP PATCH 请求。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @PatchMapping
    public String hello() {
        return "hello";
    }
}
```

### 8. @RequestBody

@RequestBody 注解用于绑定请求体到方法参数。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @PostMapping
    public String hello(@RequestBody User user) {
        return "hello";
    }
}
```

### 9. @ResponseBody

@ResponseBody 注解用于将方法返回值直接作为响应体。

```java
@Controller
@RequestMapping("/hello")
public class HelloController {
    @GetMapping
    @ResponseBody
    public String hello() {
        return "Hello, Spring MVC!";
    }
}
```

### 10. @RestController

@RestController 注解是 @Controller 和 @ResponseBody 的组合，用于创建 RESTful 控制器。

```java
@RestController
@RequestMapping("/hello")
public class HelloController {
    @GetMapping
    public String hello() {
        return "Hello, Spring MVC!";
    }
}
```

## 快速入门示例

### 1. 添加依赖

**Maven**：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.3.4</version>
</dependency>
```

**Gradle**：

```gradle
implementation 'org.springframework:spring-webmvc:5.3.4'
```

### 2. 配置 Spring MVC

**WebConfig.java**：

```java
@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.example")
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

**DispatcherServletInitializer.java**：

```java
public class DispatcherServletInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {
    @Override
    protected Class<?>[] getRootConfigClasses() {
        return null;
    }
    
    @Override
    protected Class<?>[] getServletConfigClasses() {
        return new Class<?>[]{WebConfig.class};
    }
    
    @Override
    protected String[] getServletMappings() {
        return new String[]{"/"};
    }
}
```

### 3. 创建控制器

**HelloController.java**：

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

### 4. 创建视图

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

### 5. 运行应用

启动应用后，访问 http://localhost:8080/hello 即可看到 "Hello, Spring MVC!" 的输出。

## 总结

Spring MVC 是一个基于 MVC 设计模式的 Web 框架，提供了清晰的代码结构和丰富的功能。本章节详细介绍了 Spring MVC 的基础概念，包括 MVC 设计模式、Spring MVC 的核心组件、工作流程、配置方式和注解。通过本章节的学习，您应该了解 Spring MVC 的基本原理和使用方法，为后续的学习打下基础。