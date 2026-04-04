# Spring MVC 核心组件

## 核心组件概述

Spring MVC 由多个核心组件组成，这些组件共同协作，处理 HTTP 请求并生成响应。本章节将详细介绍 Spring MVC 的核心组件，帮助开发者了解 Spring MVC 的内部工作原理。

## 核心组件详解

### 1. DispatcherServlet

DispatcherServlet 是 Spring MVC 的核心组件，负责处理所有的 HTTP 请求。它是整个 Spring MVC 框架的中央调度器，协调其他组件的工作。

#### 主要职责

- **接收请求**：接收客户端发送的 HTTP 请求
- **请求映射**：将请求映射到相应的处理器（控制器方法）
- **参数解析**：解析请求参数
- **调用处理器**：调用相应的处理器方法
- **视图解析**：将逻辑视图名解析为实际的视图
- **异常处理**：处理请求处理过程中的异常
- **返回响应**：将响应返回给客户端

#### 配置方式

**XML 配置**：

```xml
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
```

**Java 配置**：

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

### 2. HandlerMapping

HandlerMapping 负责将 HTTP 请求映射到相应的处理器（控制器方法）。它根据请求的 URL、HTTP 方法等信息，找到对应的处理器。

#### 主要实现

- **RequestMappingHandlerMapping**：基于 @RequestMapping 注解的映射，是 Spring MVC 中最常用的 HandlerMapping
- **SimpleUrlHandlerMapping**：基于 URL 模式的映射
- **BeanNameUrlHandlerMapping**：基于 bean 名称的映射
- **RouterFunctionMapping**：基于函数式路由的映射（Spring 5+）

#### 工作原理

1. **初始化**：HandlerMapping 在应用启动时初始化，扫描并注册所有的处理器
2. **请求映射**：当请求到达时，HandlerMapping 根据请求信息查找对应的处理器
3. **返回处理器**：返回处理器和处理器拦截器

### 3. HandlerAdapter

HandlerAdapter 负责调用处理器（控制器方法）。由于处理器的类型可能不同，HandlerAdapter 提供了统一的接口来调用不同类型的处理器。

#### 主要实现

- **RequestMappingHandlerAdapter**：处理基于 @RequestMapping 注解的控制器方法
- **HttpRequestHandlerAdapter**：处理实现 HttpRequestHandler 接口的处理器
- **SimpleControllerHandlerAdapter**：处理实现 Controller 接口的控制器
- **HandlerFunctionAdapter**：处理函数式处理器（Spring 5+）

#### 工作原理

1. **参数解析**：解析请求参数，包括路径变量、请求参数、请求体等
2. **调用处理器**：调用处理器方法，传入解析后的参数
3. **返回结果**：返回处理器的执行结果，通常是 ModelAndView 对象

### 4. ViewResolver

ViewResolver 负责将逻辑视图名解析为实际的视图。它根据逻辑视图名和配置，找到对应的视图实现。

#### 主要实现

- **InternalResourceViewResolver**：解析 JSP 视图
- **FreeMarkerViewResolver**：解析 FreeMarker 视图
- **ThymeleafViewResolver**：解析 Thymeleaf 视图
- **VelocityViewResolver**：解析 Velocity 视图
- **ContentNegotiatingViewResolver**：根据请求的内容类型选择合适的视图解析器

#### 工作原理

1. **解析视图名**：根据逻辑视图名和配置，找到对应的视图实现
2. **创建视图**：创建视图对象
3. **返回视图**：返回视图对象

### 5. View

View 负责将模型数据渲染为响应。它根据模型数据和视图模板，生成 HTML、JSON 等响应。

#### 主要实现

- **InternalResourceView**：JSP 视图
- **FreeMarkerView**：FreeMarker 视图
- **ThymeleafView**：Thymeleaf 视图
- **JsonView**：JSON 视图
- **RedirectView**：重定向视图

#### 工作原理

1. **准备数据**：准备模型数据
2. **渲染视图**：根据视图模板和模型数据，渲染响应
3. **返回响应**：将渲染后的响应返回给客户端

### 6. Model

Model 是一个接口，用于存储模型数据。它在控制器和视图之间传递数据。

#### 主要方法

- **addAttribute(String attributeName, Object attributeValue)**：添加模型属性
- **addAttribute(Object attributeValue)**：添加模型属性，使用对象的类名作为属性名
- **addAllAttributes(Collection<?> attributes)**：添加多个模型属性
- **addAllAttributes(Map<String, ?> attributes)**：添加多个模型属性
- **getAttribute(String attributeName)**：获取模型属性
- **containsAttribute(String attributeName)**：检查模型是否包含指定属性
- **asMap()**：将模型转换为 Map

### 7. ModelAndView

ModelAndView 是一个类，用于同时存储模型数据和视图信息。它是控制器方法的常见返回类型。

#### 主要方法

- **setViewName(String viewName)**：设置视图名称
- **setView(View view)**：设置视图对象
- **addObject(String attributeName, Object attributeValue)**：添加模型属性
- **addObject(Object attributeValue)**：添加模型属性，使用对象的类名作为属性名
- **addAllObjects(Map<String, ?> modelMap)**：添加多个模型属性
- **getModel()**：获取模型数据
- **getViewName()**：获取视图名称
- **getView()**：获取视图对象

### 8. HandlerInterceptor

HandlerInterceptor 是一个接口，用于在请求处理的不同阶段进行拦截和处理。它可以用于实现日志记录、权限检查、事务管理等功能。

#### 主要方法

- **preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)**：在处理器方法执行前调用
- **postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView)**：在处理器方法执行后、视图渲染前调用
- **afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)**：在整个请求处理完成后调用

### 9. WebResolver

WebResolver 是一个接口，用于解析 Web 相关的对象，如主题、区域设置等。

#### 主要实现

- **LocaleResolver**：解析区域设置
- **ThemeResolver**：解析主题
- **RequestToViewNameTranslator**：将请求转换为视图名称
- **FlashMapManager**：管理 FlashMap，用于在重定向时传递数据

### 10. ExceptionHandler

ExceptionHandler 负责处理请求处理过程中的异常。它可以用于统一处理异常，返回友好的错误信息。

#### 主要实现

- **SimpleMappingExceptionResolver**：将异常映射到视图
- **DefaultHandlerExceptionResolver**：处理 Spring MVC 内置的异常
- **ResponseStatusExceptionResolver**：处理带有 @ResponseStatus 注解的异常
- **ExceptionHandlerExceptionResolver**：处理带有 @ExceptionHandler 注解的方法

## 核心组件的工作流程

1. **用户发送请求**：用户通过浏览器向服务器发送 HTTP 请求
2. **DispatcherServlet 接收请求**：DispatcherServlet 接收请求并开始处理
3. **HandlerMapping 解析请求**：HandlerMapping 将请求映射到相应的处理器
4. **HandlerInterceptor 预处理**：HandlerInterceptor 的 preHandle 方法被调用
5. **HandlerAdapter 调用处理器**：HandlerAdapter 调用处理器方法，处理业务逻辑
6. **HandlerInterceptor 后处理**：HandlerInterceptor 的 postHandle 方法被调用
7. **ViewResolver 解析视图**：ViewResolver 将逻辑视图名解析为实际的视图
8. **View 渲染响应**：View 将模型数据渲染为 HTML 响应
9. **HandlerInterceptor 完成处理**：HandlerInterceptor 的 afterCompletion 方法被调用
10. **DispatcherServlet 返回响应**：DispatcherServlet 将响应返回给浏览器

## 核心组件的配置

### 1. 配置 DispatcherServlet

**XML 配置**：

```xml
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
```

**Java 配置**：

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

### 2. 配置 HandlerMapping

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
        configurer.enable();
    }
}
```

### 3. 配置 HandlerAdapter

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Bean
    public RequestMappingHandlerAdapter requestMappingHandlerAdapter() {
        RequestMappingHandlerAdapter adapter = new RequestMappingHandlerAdapter();
        // 配置适配器
        return adapter;
    }
}
```

### 4. 配置 ViewResolver

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

### 5. 配置 HandlerInterceptor

**Java 配置**：

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LoggingInterceptor())
                .addPathPatterns("/**")
                .excludePathPatterns("/static/**");
    }
}

public class LoggingInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("Pre-handle: " + request.getRequestURI());
        return true;
    }
    
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("Post-handle: " + request.getRequestURI());
    }
    
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("After completion: " + request.getRequestURI());
    }
}
```

## 核心组件的最佳实践

### 1. 合理配置 DispatcherServlet

- **URL 映射**：使用 "/" 作为 URL 映射，处理所有请求
- **加载顺序**：设置 load-on-startup 为 1，在应用启动时加载
- **配置文件**：使用 Java 配置或 XML 配置，根据项目需求选择

### 2. 选择合适的 HandlerMapping

- **RequestMappingHandlerMapping**：推荐使用，基于 @RequestMapping 注解，灵活方便
- **SimpleUrlHandlerMapping**：适用于简单的 URL 映射
- **BeanNameUrlHandlerMapping**：适用于基于 bean 名称的映射

### 3. 选择合适的 ViewResolver

- **InternalResourceViewResolver**：适用于 JSP 视图
- **ThymeleafViewResolver**：适用于 Thymeleaf 视图，推荐使用
- **FreeMarkerViewResolver**：适用于 FreeMarker 视图

### 4. 使用 HandlerInterceptor

- **日志记录**：记录请求和响应信息
- **权限检查**：检查用户权限
- **事务管理**：管理事务
- **性能监控**：监控请求处理时间

### 5. 合理使用 Model 和 ModelAndView

- **Model**：用于存储模型数据，传递给视图
- **ModelAndView**：同时存储模型数据和视图信息，适用于需要指定视图的场景

## 总结

Spring MVC 的核心组件包括 DispatcherServlet、HandlerMapping、HandlerAdapter、ViewResolver、View、Model、ModelAndView、HandlerInterceptor、WebResolver 和 ExceptionHandler 等。这些组件共同协作，处理 HTTP 请求并生成响应。本章节详细介绍了 Spring MVC 的核心组件，包括它们的职责、实现和配置方式。通过本章节的学习，您应该了解 Spring MVC 的内部工作原理，掌握核心组件的使用方法，为构建高效、可维护的 Web 应用程序打下基础。