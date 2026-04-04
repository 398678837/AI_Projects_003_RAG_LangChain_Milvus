# Spring 核心容器

## 1. 核心容器概述

Spring核心容器是Spring框架的基础，负责创建、配置和管理Bean。它提供了控制反转（IoC）和依赖注入（DI）的核心功能，是Spring框架的核心组成部分。

### 1.1 核心容器的作用

- **Bean管理**：创建、配置和管理Bean
- **依赖注入**：自动注入Bean之间的依赖关系
- **生命周期管理**：管理Bean的完整生命周期
- **配置管理**：处理各种配置方式（XML、注解、Java配置）
- **资源管理**：提供统一的资源访问机制

### 1.2 核心容器的组成

- **BeanFactory**：最基础的容器接口
- **ApplicationContext**：BeanFactory的扩展，提供更多功能
- **BeanDefinition**：定义Bean的元数据
- **BeanPostProcessor**：Bean的后置处理器
- **PropertyResolver**：属性解析器

## 2. BeanFactory

### 2.1 BeanFactory简介

BeanFactory是Spring最基础的容器接口，它定义了获取Bean的基本方法。BeanFactory采用延迟初始化的方式，只有在获取Bean时才会创建Bean实例。

### 2.2 BeanFactory的核心方法

- `getBean(String name)`：根据名称获取Bean
- `getBean(Class<T> requiredType)`：根据类型获取Bean
- `getBean(String name, Object... args)`：获取Bean并指定构造参数
- `containsBean(String name)`：检查容器是否包含指定名称的Bean
- `isSingleton(String name)`：检查Bean是否是单例
- `isPrototype(String name)`：检查Bean是否是原型
- `getType(String name)`：获取Bean的类型

### 2.3 BeanFactory的实现类

- **DefaultListableBeanFactory**：默认的BeanFactory实现
- **XmlBeanFactory**：基于XML配置的BeanFactory（已废弃）
- **StaticListableBeanFactory**：静态的BeanFactory实现

## 3. ApplicationContext

### 3.1 ApplicationContext简介

ApplicationContext是BeanFactory的扩展，提供了更多高级功能。它在容器启动时就初始化所有单例Bean，而不是延迟初始化。

### 3.2 ApplicationContext的主要功能

- **Bean管理**：继承BeanFactory的所有功能
- **国际化支持**：提供消息源和国际化能力
- **资源访问**：统一的资源加载机制
- **事件发布**：支持事件驱动模型
- **环境配置**：访问环境变量和系统属性
- **AOP集成**：内置AOP支持

### 3.3 ApplicationContext的实现类

- **ClassPathXmlApplicationContext**：从类路径加载XML配置
- **FileSystemXmlApplicationContext**：从文件系统加载XML配置
- **AnnotationConfigApplicationContext**：基于注解配置的ApplicationContext
- **WebApplicationContext**：为Web应用提供的ApplicationContext
- **GenericApplicationContext**：通用的ApplicationContext实现

## 4. Bean的生命周期

### 4.1 Bean的生命周期概述

Spring Bean的生命周期包括以下阶段：

1. **实例化**：创建Bean实例
2. **属性赋值**：设置Bean的属性
3. **初始化前**：调用BeanPostProcessor的postProcessBeforeInitialization方法
4. **初始化**：调用Bean的初始化方法（如init-method）
5. **初始化后**：调用BeanPostProcessor的postProcessAfterInitialization方法
6. **使用**：Bean可以被应用程序使用
7. **销毁**：容器关闭时，调用Bean的销毁方法（如destroy-method）

### 4.2 生命周期回调方法

- **初始化方法**：通过init-method属性或@PostConstruct注解指定
- **销毁方法**：通过destroy-method属性或@PreDestroy注解指定
- **BeanPostProcessor**：自定义Bean的处理逻辑
- **InitializingBean**：实现该接口的afterPropertiesSet方法
- **DisposableBean**：实现该接口的destroy方法

### 4.3 生命周期管理示例

```java
public class LifecycleBean implements InitializingBean, DisposableBean {
    
    public LifecycleBean() {
        System.out.println("1. 构造方法");
    }
    
    public void setName(String name) {
        System.out.println("2. 设置属性: " + name);
    }
    
    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("4. InitializingBean.afterPropertiesSet()");
    }
    
    public void initMethod() {
        System.out.println("5. 自定义初始化方法");
    }
    
    public void doSomething() {
        System.out.println("6. 业务方法");
    }
    
    @Override
    public void destroy() throws Exception {
        System.out.println("7. DisposableBean.destroy()");
    }
    
    public void destroyMethod() {
        System.out.println("8. 自定义销毁方法");
    }
}
```

## 5. 依赖注入

### 5.1 依赖注入的概念

依赖注入是一种设计模式，它允许对象的依赖关系由外部容器来管理，而不是由对象自己创建或查找依赖。

### 5.2 依赖注入的方式

- **构造函数注入**：通过构造函数参数注入依赖
- **setter方法注入**：通过setter方法注入依赖
- **字段注入**：通过@Autowired注解直接注入字段
- **方法注入**：通过@Autowired注解注入方法参数

### 5.3 依赖注入的实现原理

1. **解析配置**：读取XML、注解或Java配置
2. **创建BeanDefinition**：为每个Bean创建定义
3. **注册BeanDefinition**：将BeanDefinition注册到容器
4. **实例化Bean**：创建Bean实例
5. **注入依赖**：解析和注入依赖关系
6. **初始化Bean**：调用初始化方法

### 5.4 依赖注入的优势

- **解耦**：减少组件之间的耦合
- **可测试性**：便于单元测试
- **可维护性**：提高代码的可维护性
- **灵活性**：便于替换实现

## 6. 容器的启动过程

### 6.1 ApplicationContext的启动过程

1. **创建ApplicationContext实例**
2. **加载配置源**（XML、注解、Java配置）
3. **解析配置**，创建BeanDefinition
4. **注册BeanDefinition到BeanFactory**
5. **初始化BeanFactoryPostProcessor**
6. **注册BeanPostProcessor**
7. **初始化事件监听器**
8. **初始化所有单例Bean**
9. **发布ContextRefreshedEvent事件**

### 6.2 容器启动的关键步骤

- **资源加载**：加载配置文件和资源
- **Bean定义解析**：将配置转换为BeanDefinition
- **BeanFactoryPostProcessor处理**：修改BeanDefinition
- **Bean实例化**：创建Bean实例
- **依赖注入**：注入Bean的依赖
- **初始化**：调用初始化方法
- **事件发布**：通知监听器容器已刷新

## 7. Bean的作用域

### 7.1 内置作用域

- **singleton**：单例，容器中只有一个实例（默认）
- **prototype**：原型，每次获取都创建新实例
- **request**：请求作用域，每个HTTP请求创建一个实例
- **session**：会话作用域，每个HTTP会话创建一个实例
- **application**：应用作用域，每个ServletContext创建一个实例
- **websocket**：WebSocket作用域，每个WebSocket会话创建一个实例

### 7.2 作用域的选择

- **singleton**：无状态的Bean，如工具类
- **prototype**：有状态的Bean，如DTO对象
- **request**：与HTTP请求相关的Bean
- **session**：与用户会话相关的Bean

## 8. 配置方式

### 8.1 XML配置

```xml
<bean id="userService" class="com.example.UserService">
    <property name="userDao" ref="userDao"/>
</bean>

<bean id="userDao" class="com.example.UserDaoImpl"/>
```

### 8.2 注解配置

```java
@Component
public class UserService {
    
    @Autowired
    private UserDao userDao;
    
    // 方法
}

@Component
public class UserDaoImpl implements UserDao {
    // 方法
}
```

### 8.3 Java配置类

```java
@Configuration
public class AppConfig {
    
    @Bean
    public UserService userService() {
        UserService userService = new UserService();
        userService.setUserDao(userDao());
        return userService;
    }
    
    @Bean
    public UserDao userDao() {
        return new UserDaoImpl();
    }
}
```

## 9. 核心容器的最佳实践

### 9.1 配置最佳实践

- **优先使用注解和Java配置**：更简洁、类型安全
- **合理组织配置**：将配置按功能模块分离
- **使用环境变量**：避免硬编码配置
- **配置外部化**：使用properties或yaml文件

### 9.2 Bean管理最佳实践

- **使用构造函数注入**：更安全，便于测试
- **避免循环依赖**：设计时注意依赖关系
- **合理使用作用域**：根据Bean的特性选择合适的作用域
- **使用@Qualifier**：解决依赖注入的歧义

### 9.3 性能优化

- **延迟初始化**：对于大型应用，考虑使用延迟初始化
- **Bean生命周期管理**：合理管理Bean的创建和销毁
- **资源关闭**：确保资源在容器关闭时正确释放
- **避免不必要的Bean**：只创建必要的Bean

## 10. 总结

Spring核心容器是Spring框架的基础，它提供了IoC和DI的核心功能，负责Bean的创建、配置和管理。理解核心容器的工作原理，对于掌握Spring框架的使用至关重要。

本章节介绍了BeanFactory、ApplicationContext、Bean生命周期、依赖注入等核心概念，以及容器的启动过程和最佳实践。通过学习这些知识，开发者可以更有效地使用Spring核心容器，构建高质量的Spring应用。