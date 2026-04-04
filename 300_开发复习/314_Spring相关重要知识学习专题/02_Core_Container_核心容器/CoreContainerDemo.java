package com.example.spring.corecontainer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

/**
 * Spring 核心容器示例
 */
public class CoreContainerDemo {
    
    public static void main(String[] args) {
        // 创建应用上下文
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        
        // 获取Bean
        UserService userService = context.getBean(UserService.class);
        UserService userService2 = context.getBean(UserService.class);
        
        // 测试单例
        System.out.println("userService == userService2: " + (userService == userService2));
        
        // 使用Bean
        userService.sayHello();
        
        // 测试原型作用域
        System.out.println("\n=== 测试原型作用域 ===");
        User user1 = context.getBean(User.class);
        User user2 = context.getBean(User.class);
        System.out.println("user1 == user2: " + (user1 == user2));
        
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
    public UserService userService() {
        return new UserService(userDao());
    }
    
    @Bean
    public UserDao userDao() {
        return new UserDaoImpl();
    }
    
    @Bean
    @Scope("prototype")
    public User user() {
        return new User();
    }
    
    @Bean
    public LifecycleBean lifecycleBean() {
        return new LifecycleBean();
    }
    
    @Bean
    public CustomBeanPostProcessor customBeanPostProcessor() {
        return new CustomBeanPostProcessor();
    }
}

/**
 * 用户服务
 */
class UserService {
    
    private final UserDao userDao;
    
    // 构造函数注入
    @Autowired
    public UserService(UserDao userDao) {
        this.userDao = userDao;
        System.out.println("UserService: 构造函数");
    }
    
    public void sayHello() {
        System.out.println("UserService: Hello! " + userDao.getMessage());
    }
}

/**
 * 用户DAO接口
 */
interface UserDao {
    String getMessage();
}

/**
 * 用户DAO实现
 */
class UserDaoImpl implements UserDao {
    
    public UserDaoImpl() {
        System.out.println("UserDaoImpl: 构造函数");
    }
    
    @Override
    public String getMessage() {
        return "UserDaoImpl message";
    }
}

/**
 * 用户类
 */
class User {
    
    public User() {
        System.out.println("User: 构造函数");
    }
}

/**
 * 生命周期Bean
 */
class LifecycleBean {
    
    public LifecycleBean() {
        System.out.println("LifecycleBean: 构造函数");
    }
    
    @PostConstruct
    public void init() {
        System.out.println("LifecycleBean: @PostConstruct 初始化方法");
    }
    
    public void customInit() {
        System.out.println("LifecycleBean: 自定义初始化方法");
    }
    
    public void doSomething() {
        System.out.println("LifecycleBean: 业务方法");
    }
    
    @PreDestroy
    public void destroy() {
        System.out.println("LifecycleBean: @PreDestroy 销毁方法");
    }
    
    public void customDestroy() {
        System.out.println("LifecycleBean: 自定义销毁方法");
    }
}

/**
 * 自定义BeanPostProcessor
 */
class CustomBeanPostProcessor implements BeanPostProcessor {
    
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) {
        System.out.println("CustomBeanPostProcessor: postProcessBeforeInitialization - " + beanName);
        return bean;
    }
    
    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) {
        System.out.println("CustomBeanPostProcessor: postProcessAfterInitialization - " + beanName);
        return bean;
    }
}

/**
 * BeanFactory演示
 */
class BeanFactoryDemo {
    
    public static void main(String[] args) {
        // 创建DefaultListableBeanFactory
        org.springframework.beans.factory.support.DefaultListableBeanFactory beanFactory = 
            new org.springframework.beans.factory.support.DefaultListableBeanFactory();
        
        // 注册BeanDefinition
        org.springframework.beans.factory.support.BeanDefinitionBuilder builder = 
            org.springframework.beans.factory.support.BeanDefinitionBuilder.genericBeanDefinition(UserService.class);
        builder.addConstructorArgReference("userDao");
        beanFactory.registerBeanDefinition("userService", builder.build());
        
        builder = org.springframework.beans.factory.support.BeanDefinitionBuilder.genericBeanDefinition(UserDaoImpl.class);
        beanFactory.registerBeanDefinition("userDao", builder.build());
        
        // 获取Bean
        UserService userService = beanFactory.getBean(UserService.class);
        userService.sayHello();
    }
}

/**
 * ApplicationContext演示
 */
class ApplicationContextDemo {
    
    public static void main(String[] args) {
        // 创建AnnotationConfigApplicationContext
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        
        // 获取Bean
        UserService userService = context.getBean(UserService.class);
        userService.sayHello();
        
        // 测试环境属性
        System.out.println("Environment property: java.version = " + 
            context.getEnvironment().getProperty("java.version"));
        
        // 测试资源加载
        org.springframework.core.io.Resource resource = context.getResource("classpath:application.properties");
        System.out.println("Resource exists: " + resource.exists());
        
        // 关闭上下文
        context.close();
    }
}

/**
 * 依赖注入演示
 */
class DependencyInjectionDemo {
    
    @Configuration
    static class DIConfig {
        
        @Bean
        public ServiceA serviceA() {
            return new ServiceA(serviceB());
        }
        
        @Bean
        public ServiceB serviceB() {
            return new ServiceB();
        }
    }
    
    static class ServiceA {
        private final ServiceB serviceB;
        
        // 构造函数注入
        public ServiceA(ServiceB serviceB) {
            this.serviceB = serviceB;
            System.out.println("ServiceA: 构造函数注入 ServiceB");
        }
        
        public void doSomething() {
            System.out.println("ServiceA: doSomething");
            serviceB.doSomething();
        }
    }
    
    static class ServiceB {
        public void doSomething() {
            System.out.println("ServiceB: doSomething");
        }
    }
    
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(DIConfig.class);
        ServiceA serviceA = context.getBean(ServiceA.class);
        serviceA.doSomething();
        context.close();
    }
}
