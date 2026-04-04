package com.example.spring.basic;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Spring 基础概念示例
 */
public class BasicConceptsDemo {
    
    public static void main(String[] args) {
        // 创建应用上下文
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        
        // 获取Bean
        MessageService messageService = context.getBean(MessageService.class);
        
        // 使用Bean
        System.out.println(messageService.getMessage());
        
        // 关闭上下文
        context.close();
    }
}

/**
 * 配置类
 */
@Configuration
class AppConfig {
    
    @Bean
    public MessageService messageService() {
        return new MessageServiceImpl();
    }
    
    @Bean
    public GreetingService greetingService() {
        return new GreetingServiceImpl(messageService());
    }
}

/**
 * 消息服务接口
 */
interface MessageService {
    String getMessage();
}

/**
 * 消息服务实现
 */
class MessageServiceImpl implements MessageService {
    @Override
    public String getMessage() {
        return "Hello, Spring!";
    }
}

/**
 * 问候服务接口
 */
interface GreetingService {
    String getGreeting();
}

/**
 * 问候服务实现
 */
class GreetingServiceImpl implements GreetingService {
    
    private final MessageService messageService;
    
    // 构造函数注入
    public GreetingServiceImpl(MessageService messageService) {
        this.messageService = messageService;
    }
    
    @Override
    public String getGreeting() {
        return "Greeting: " + messageService.getMessage();
    }
}

/**
 * 演示依赖注入的类
 */
class DependencyInjectionDemo {
    
    private final MessageService messageService;
    
    // 构造函数注入
    @Autowired
    public DependencyInjectionDemo(MessageService messageService) {
        this.messageService = messageService;
    }
    
    public void showMessage() {
        System.out.println("Dependency Injection Demo: " + messageService.getMessage());
    }
}

/**
 * 演示Bean生命周期的类
 */
class BeanLifecycleDemo {
    
    public BeanLifecycleDemo() {
        System.out.println("BeanLifecycleDemo: 构造方法");
    }
    
    public void init() {
        System.out.println("BeanLifecycleDemo: 初始化方法");
    }
    
    public void destroy() {
        System.out.println("BeanLifecycleDemo: 销毁方法");
    }
    
    public void doSomething() {
        System.out.println("BeanLifecycleDemo: 执行方法");
    }
}

/**
 * 生命周期配置类
 */
@Configuration
class LifecycleConfig {
    
    @Bean(initMethod = "init", destroyMethod = "destroy")
    public BeanLifecycleDemo beanLifecycleDemo() {
        return new BeanLifecycleDemo();
    }
}

/**
 * 演示不同作用域的类
 */
class ScopeDemo {
    private int count = 0;
    
    public ScopeDemo() {
        System.out.println("ScopeDemo: 构造方法");
    }
    
    public int getCount() {
        return count++;
    }
}

/**
 * 作用域配置类
 */
@Configuration
class ScopeConfig {
    
    @Bean
    public ScopeDemo singletonBean() {
        return new ScopeDemo();
    }
    
    @Bean
    @org.springframework.context.annotation.Scope("prototype")
    public ScopeDemo prototypeBean() {
        return new ScopeDemo();
    }
}

/**
 * 作用域演示类
 */
class ScopeDemoTest {
    
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(ScopeConfig.class);
        
        // 测试单例作用域
        System.out.println("=== 测试单例作用域 ===");
        ScopeDemo singleton1 = context.getBean("singletonBean", ScopeDemo.class);
        System.out.println("singleton1.count: " + singleton1.getCount());
        
        ScopeDemo singleton2 = context.getBean("singletonBean", ScopeDemo.class);
        System.out.println("singleton2.count: " + singleton2.getCount());
        
        System.out.println("singleton1 == singleton2: " + (singleton1 == singleton2));
        
        // 测试原型作用域
        System.out.println("\n=== 测试原型作用域 ===");
        ScopeDemo prototype1 = context.getBean("prototypeBean", ScopeDemo.class);
        System.out.println("prototype1.count: " + prototype1.getCount());
        
        ScopeDemo prototype2 = context.getBean("prototypeBean", ScopeDemo.class);
        System.out.println("prototype2.count: " + prototype2.getCount());
        
        System.out.println("prototype1 == prototype2: " + (prototype1 == prototype2));
        
        context.close();
    }
}
