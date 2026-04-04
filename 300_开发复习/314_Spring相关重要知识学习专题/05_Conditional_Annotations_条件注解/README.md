# Spring 条件注解

## 1. 条件注解概述

条件注解是Spring框架中的一个重要特性，它允许开发者根据特定条件来决定是否创建和注册Bean。条件注解在Spring 4.0中引入，为Spring应用提供了更灵活的配置方式。

### 1.1 条件注解的作用

- **根据环境条件创建Bean**：根据不同的环境（开发、测试、生产）创建不同的Bean
- **根据系统属性创建Bean**：根据系统属性或环境变量决定是否创建Bean
- **根据依赖存在性创建Bean**：根据特定依赖是否存在决定是否创建Bean
- **根据自定义条件创建Bean**：根据自定义的条件逻辑决定是否创建Bean

### 1.2 条件注解的核心概念

- **@Conditional**：核心条件注解，用于指定条件类
- **Condition**：条件接口，定义了条件判断的方法
- **ConditionContext**：条件上下文，提供访问Spring环境的方法
- **AnnotatedTypeMetadata**：注解元数据，提供访问注解信息的方法

## 2. @Conditional注解

### 2.1 @Conditional注解的使用

@Conditional注解可以应用于类和方法上，用于指定一个或多个条件类：

```java
@Configuration
public class AppConfig {
    
    @Bean
    @Conditional(MyCondition.class)
    public MyBean myBean() {
        return new MyBean();
    }
}
```

### 2.2 条件类的实现

条件类需要实现Condition接口：

```java
public class MyCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        // 条件判断逻辑
        return true; // 返回true表示条件满足
    }
}
```

## 3. 内置条件注解

Spring框架提供了一些内置的条件注解，用于常见的条件判断场景：

### 3.1 @ConditionalOnProperty

根据配置属性的值决定是否创建Bean：

```java
@Bean
@ConditionalOnProperty(name = "myapp.feature.enabled", havingValue = "true")
public MyFeature myFeature() {
    return new MyFeature();
}
```

### 3.2 @ConditionalOnClass

根据特定类是否存在决定是否创建Bean：

```java
@Bean
@ConditionalOnClass(name = "com.example.SomeClass")
public MyBean myBean() {
    return new MyBean();
}
```

### 3.3 @ConditionalOnMissingClass

根据特定类是否不存在决定是否创建Bean：

```java
@Bean
@ConditionalOnMissingClass("com.example.SomeClass")
public MyBean myBean() {
    return new MyBean();
}
```

### 3.4 @ConditionalOnBean

根据特定Bean是否存在决定是否创建Bean：

```java
@Bean
@ConditionalOnBean(MyDependency.class)
public MyBean myBean(MyDependency dependency) {
    return new MyBean(dependency);
}
```

### 3.5 @ConditionalOnMissingBean

根据特定Bean是否不存在决定是否创建Bean：

```java
@Bean
@ConditionalOnMissingBean(MyBean.class)
public MyBean myBean() {
    return new MyBean();
}
```

### 3.6 @ConditionalOnWebApplication

根据应用是否是Web应用决定是否创建Bean：

```java
@Bean
@ConditionalOnWebApplication
public WebBean webBean() {
    return new WebBean();
}
```

### 3.7 @ConditionalOnNotWebApplication

根据应用是否不是Web应用决定是否创建Bean：

```java
@Bean
@ConditionalOnNotWebApplication
public NonWebBean nonWebBean() {
    return new NonWebBean();
}
```

### 3.8 @ConditionalOnExpression

根据SpEL表达式的结果决定是否创建Bean：

```java
@Bean
@ConditionalOnExpression("${myapp.feature.enabled} and ${myapp.feature.version} >= 2")
public MyFeature myFeature() {
    return new MyFeature();
}
```

## 4. 自定义条件注解

### 4.1 创建自定义条件类

```java
public class DatabaseTypeCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        String databaseType = context.getEnvironment().getProperty("database.type");
        return "mysql".equals(databaseType);
    }
}
```

### 4.2 创建自定义条件注解

```java
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Conditional(DatabaseTypeCondition.class)
public @interface ConditionalOnMysql {
}
```

### 4.3 使用自定义条件注解

```java
@Configuration
public class DatabaseConfig {
    
    @Bean
    @ConditionalOnMysql
    public DataSource mysqlDataSource() {
        // 配置MySQL数据源
        return new MysqlDataSource();
    }
    
    @Bean
    @ConditionalOnPostgres
    public DataSource postgresDataSource() {
        // 配置PostgreSQL数据源
        return new PostgresDataSource();
    }
}
```

## 5. 条件上下文（ConditionContext）

ConditionContext提供了访问Spring环境的方法：

- **getBeanFactory()**：获取BeanFactory
- **getEnvironment()**：获取Environment
- **getClassLoader()**：获取ClassLoader
- **getResourceLoader()**：获取ResourceLoader
- **getRegistry()**：获取BeanDefinitionRegistry

### 5.1 使用ConditionContext

```java
public class MyCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        // 获取环境属性
        String property = context.getEnvironment().getProperty("myapp.feature.enabled");
        
        // 检查Bean是否存在
        boolean beanExists = context.getBeanFactory().containsBean("myDependency");
        
        // 检查类是否存在
        ClassLoader classLoader = context.getClassLoader();
        try {
            classLoader.loadClass("com.example.SomeClass");
            return true;
        } catch (ClassNotFoundException e) {
            return false;
        }
    }
}
```

## 6. 注解元数据（AnnotatedTypeMetadata）

AnnotatedTypeMetadata提供了访问注解信息的方法：

- **isAnnotated(String annotationName)**：检查是否有特定注解
- **getAnnotationAttributes(String annotationName)**：获取注解属性
- **getAllAnnotationAttributes(String annotationName)**：获取所有注解属性

### 6.1 使用AnnotatedTypeMetadata

```java
public class MyCondition implements Condition {
    
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        // 检查是否有特定注解
        boolean hasAnnotation = metadata.isAnnotated("org.springframework.stereotype.Component");
        
        // 获取注解属性
        Map<String, Object> attributes = metadata.getAnnotationAttributes("com.example.MyAnnotation");
        if (attributes != null) {
            String value = (String) attributes.get("value");
            return "test".equals(value);
        }
        
        return false;
    }
}
```

## 7. 条件注解的应用场景

### 7.1 环境特定配置

```java
@Configuration
public class EnvironmentConfig {
    
    @Bean
    @Profile("development")
    @ConditionalOnProperty(name = "dev.mode", havingValue = "true")
    public DevelopmentBean developmentBean() {
        return new DevelopmentBean();
    }
    
    @Bean
    @Profile("production")
    public ProductionBean productionBean() {
        return new ProductionBean();
    }
}
```

### 7.2 依赖特定配置

```java
@Configuration
public class DependencyConfig {
    
    @Bean
    @ConditionalOnClass(name = "org.springframework.data.mongodb.core.MongoTemplate")
    public MongoRepository mongoRepository() {
        return new MongoRepository();
    }
    
    @Bean
    @ConditionalOnClass(name = "org.springframework.jdbc.core.JdbcTemplate")
    public JdbcRepository jdbcRepository() {
        return new JdbcRepository();
    }
}
```

### 7.3 特性开关

```java
@Configuration
public class FeatureConfig {
    
    @Bean
    @ConditionalOnProperty(name = "feature.a.enabled", havingValue = "true")
    public FeatureA featureA() {
        return new FeatureA();
    }
    
    @Bean
    @ConditionalOnProperty(name = "feature.b.enabled", havingValue = "true")
    public FeatureB featureB() {
        return new FeatureB();
    }
}
```

## 8. 条件注解的最佳实践

### 8.1 条件设计

- **单一职责**：每个条件类只负责一个条件判断
- **清晰命名**：条件类和条件注解的命名应清晰表达其用途
- **文档化**：为条件注解添加详细的文档说明
- **可测试性**：设计可测试的条件类

### 8.2 条件组合

- **使用多个条件注解**：可以在一个Bean上使用多个条件注解
- **使用逻辑运算符**：在@ConditionalOnExpression中使用逻辑运算符
- **自定义复合条件**：创建包含多个条件判断的复合条件类

### 8.3 性能考虑

- **条件判断轻量**：条件判断应尽可能轻量，避免耗时操作
- **缓存条件结果**：对于复杂的条件判断，考虑缓存结果
- **避免循环依赖**：条件判断中避免创建Bean，可能导致循环依赖

### 8.4 测试

- **测试不同条件**：测试条件为true和false的情况
- **模拟环境**：使用@ActiveProfiles和@TestPropertySource模拟不同环境
- **验证Bean创建**：验证Bean是否按预期创建或不创建

## 9. 常见问题

### 9.1 条件判断顺序

当多个条件注解应用于同一个Bean时，条件判断的顺序可能会影响结果。建议：

- 先判断最基本的条件（如类是否存在）
- 再判断更具体的条件（如属性值）
- 使用@Order注解控制条件判断的顺序

### 9.2 条件依赖

条件判断中应避免依赖其他Bean的创建，可能导致循环依赖。建议：

- 使用context.getEnvironment()获取配置
- 使用context.getClassLoader()检查类是否存在
- 避免在条件判断中调用context.getBean()

### 9.3 条件注解与Profile

@Profile注解也是一种条件注解，它基于激活的配置文件进行条件判断。建议：

- 对于环境相关的配置，使用@Profile
- 对于更复杂的条件，使用@Conditional或自定义条件注解

## 10. 总结

Spring的条件注解是一种强大的特性，它允许开发者根据特定条件来决定是否创建和注册Bean。通过使用条件注解，开发者可以创建更灵活、更适应不同环境的Spring应用。

本章节介绍了条件注解的核心概念、内置条件注解、自定义条件注解、条件上下文和注解元数据等内容，以及条件注解的应用场景和最佳实践。通过学习这些知识，开发者可以更有效地使用条件注解，构建高质量的Spring应用。