package com.example.spring.conditional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Condition;
import org.springframework.context.annotation.ConditionContext;
import org.springframework.context.annotation.Conditional;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.AliasFor;
import org.springframework.core.type.AnnotatedTypeMetadata;

import java.lang.annotation.*;
import java.util.Map;

/**
 * Spring 条件注解示例
 */
public class ConditionalAnnotationsDemo {
    
    public static void main(String[] args) {
        // 测试基本条件注解
        System.out.println("=== 测试基本条件注解 ===");
        AnnotationConfigApplicationContext context1 = new AnnotationConfigApplicationContext(BaseConfig.class);
        System.out.println("Bean 'myBean' exists: " + context1.containsBean("myBean"));
        context1.close();
        
        // 测试属性条件注解
        System.out.println("\n=== 测试属性条件注解 ===");
        System.setProperty("feature.enabled", "true");
        AnnotationConfigApplicationContext context2 = new AnnotationConfigApplicationContext(PropertyConfig.class);
        System.out.println("Bean 'featureBean' exists: " + context2.containsBean("featureBean"));
        context2.close();
        
        // 测试类条件注解
        System.out.println("\n=== 测试类条件注解 ===");
        AnnotationConfigApplicationContext context3 = new AnnotationConfigApplicationContext(ClassConfig.class);
        System.out.println("Bean 'jdbcBean' exists: " + context3.containsBean("jdbcBean"));
        System.out.println("Bean 'mongoBean' exists: " + context3.containsBean("mongoBean"));
        context3.close();
        
        // 测试Bean条件注解
        System.out.println("\n=== 测试Bean条件注解 ===");
        AnnotationConfigApplicationContext context4 = new AnnotationConfigApplicationContext(BeanConfig.class);
        System.out.println("Bean 'dependentBean' exists: " + context4.containsBean("dependentBean"));
        context4.close();
        
        // 测试自定义条件注解
        System.out.println("\n=== 测试自定义条件注解 ===");
        System.setProperty("database.type", "mysql");
        AnnotationConfigApplicationContext context5 = new AnnotationConfigApplicationContext(CustomConfig.class);
        System.out.println("Bean 'mysqlDataSource' exists: " + context5.containsBean("mysqlDataSource"));
        System.out.println("Bean 'postgresDataSource' exists: " + context5.containsBean("postgresDataSource"));
        context5.close();
    }
}

/**
 * 基本配置类
 */
@Configuration
class BaseConfig {
    
    @Bean
    @Conditional(MyCondition.class)
    public MyBean myBean() {
        return new MyBean();
    }
}

/**
 * 自定义条件类
 */
class MyCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        // 检查系统属性
        String property = System.getProperty("my.condition");
        return "true".equals(property);
    }
}

/**
 * 测试Bean
 */
class MyBean {
    public MyBean() {
        System.out.println("MyBean created");
    }
}

/**
 * 属性配置类
 */
@Configuration
class PropertyConfig {
    
    @Bean
    @ConditionalOnProperty(name = "feature.enabled", havingValue = "true")
    public FeatureBean featureBean() {
        return new FeatureBean();
    }
}

/**
 * 特性Bean
 */
class FeatureBean {
    public FeatureBean() {
        System.out.println("FeatureBean created");
    }
}

/**
 * 类配置类
 */
@Configuration
class ClassConfig {
    
    @Bean
    @ConditionalOnClass(name = "org.springframework.jdbc.core.JdbcTemplate")
    public JdbcBean jdbcBean() {
        return new JdbcBean();
    }
    
    @Bean
    @ConditionalOnClass(name = "org.springframework.data.mongodb.core.MongoTemplate")
    public MongoBean mongoBean() {
        return new MongoBean();
    }
}

/**
 * JDBC Bean
 */
class JdbcBean {
    public JdbcBean() {
        System.out.println("JdbcBean created");
    }
}

/**
 * MongoDB Bean
 */
class MongoBean {
    public MongoBean() {
        System.out.println("MongoBean created");
    }
}

/**
 * Bean配置类
 */
@Configuration
class BeanConfig {
    
    @Bean
    public DependencyBean dependencyBean() {
        return new DependencyBean();
    }
    
    @Bean
    @ConditionalOnMissingBean(name = "anotherBean")
    public DependentBean dependentBean() {
        return new DependentBean();
    }
}

/**
 * 依赖Bean
 */
class DependencyBean {
    public DependencyBean() {
        System.out.println("DependencyBean created");
    }
}

/**
 * 依赖于其他Bean的Bean
 */
class DependentBean {
    public DependentBean() {
        System.out.println("DependentBean created");
    }
}

/**
 * 自定义条件注解
 */
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Conditional(DatabaseTypeCondition.class)
@interface ConditionalOnDatabaseType {
    @AliasFor(annotation = Conditional.class)
    Class<? extends Condition>[] value() default {};
    
    String type();
}

/**
 * 数据库类型条件类
 */
class DatabaseTypeCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        Map<String, Object> attributes = metadata.getAnnotationAttributes(ConditionalOnDatabaseType.class.getName());
        if (attributes != null) {
            String expectedType = (String) attributes.get("type");
            String actualType = context.getEnvironment().getProperty("database.type");
            return expectedType.equals(actualType);
        }
        return false;
    }
}

/**
 * 自定义配置类
 */
@Configuration
class CustomConfig {
    
    @Bean
    @ConditionalOnDatabaseType(type = "mysql")
    public DataSource mysqlDataSource() {
        return new MysqlDataSource();
    }
    
    @Bean
    @ConditionalOnDatabaseType(type = "postgres")
    public DataSource postgresDataSource() {
        return new PostgresDataSource();
    }
}

/**
 * 数据源接口
 */
interface DataSource {
}

/**
 * MySQL数据源
 */
class MysqlDataSource implements DataSource {
    public MysqlDataSource() {
        System.out.println("MysqlDataSource created");
    }
}

/**
 * PostgreSQL数据源
 */
class PostgresDataSource implements DataSource {
    public PostgresDataSource() {
        System.out.println("PostgresDataSource created");
    }
}

/**
 * 多条件示例
 */
@Configuration
class MultiConditionConfig {
    
    @Bean
    @ConditionalOnProperty(name = "feature.enabled", havingValue = "true")
    @ConditionalOnClass(name = "com.example.FeatureClass")
    public MultiConditionBean multiConditionBean() {
        return new MultiConditionBean();
    }
}

/**
 * 多条件Bean
 */
class MultiConditionBean {
    public MultiConditionBean() {
        System.out.println("MultiConditionBean created");
    }
}
