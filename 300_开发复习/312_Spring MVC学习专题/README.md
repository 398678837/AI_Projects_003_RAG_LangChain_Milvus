# Spring MVC 学习专题

## Spring MVC 概述

Spring MVC 是 Spring 框架的一个模块，用于构建 Web 应用程序。它基于 MVC（Model-View-Controller）设计模式，提供了一种清晰的方式来组织 Web 应用的代码结构。Spring MVC 具有以下特点：

- **灵活性**：Spring MVC 提供了灵活的配置选项，可以根据项目需求进行定制
- **可扩展性**：Spring MVC 易于扩展，可以集成各种视图技术和其他框架
- **测试友好**：Spring MVC 支持单元测试和集成测试
- **与 Spring 生态系统集成**：Spring MVC 与 Spring 框架的其他模块无缝集成

## 目录结构

```
312_Spring MVC学习专题/
├── 01_Basic_Concepts_基础概念/        # 基础概念
├── 02_Core_Components_核心组件/       # 核心组件
├── 03_Controllers_控制器/             # 控制器
├── 04_Views_视图/                     # 视图
├── 05_Models_模型/                    # 模型
├── 06_Request_Handling_请求处理/      # 请求处理
├── 07_Response_Handling_响应处理/     # 响应处理
├── 08_Validation_验证/               # 验证
├── 09_Exception_Handling_异常处理/    # 异常处理
├── 10_Best_Practices_最佳实践/         # 最佳实践
└── README.md                           # 本文件
```

## 核心功能

1. **控制器**：处理用户请求，返回响应
2. **视图解析**：将模型数据渲染为视图
3. **数据绑定**：将请求参数绑定到模型对象
4. **验证**：验证用户输入数据
5. **异常处理**：处理应用程序中的异常
6. **国际化**：支持多语言
7. **文件上传**：支持文件上传功能

## 快速入门

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

**Java 配置**：

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

### 3. 创建控制器

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

## 学习路径

1. **基础概念**：了解 Spring MVC 的基本概念和工作原理
2. **核心组件**：学习 Spring MVC 的核心组件，如 DispatcherServlet、HandlerMapping 等
3. **控制器**：掌握控制器的编写和使用
4. **视图**：学习视图技术和视图解析
5. **模型**：了解模型的使用和数据绑定
6. **请求处理**：学习请求处理的各种方式
7. **响应处理**：掌握响应处理的方法
8. **验证**：学习数据验证的实现
9. **异常处理**：了解异常处理的机制
10. **最佳实践**：掌握 Spring MVC 的最佳实践

通过本专题的学习，您将能够构建功能强大、结构清晰的 Web 应用程序。