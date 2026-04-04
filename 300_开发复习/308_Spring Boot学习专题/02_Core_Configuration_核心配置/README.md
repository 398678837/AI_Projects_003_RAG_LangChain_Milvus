# Spring Boot 核心配置

## 配置文件

Spring Boot 支持多种配置文件格式，默认使用 `application.properties` 或 `application.yml` 文件。这些文件通常放在 `src/main/resources` 目录下。

### 1. 配置文件格式

#### application.properties

```properties
# 服务器配置
server.port=8080
server.servlet.context-path=/api

# 数据库配置
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=password

# JPA 配置
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# 日志配置
logging.level.org.springframework=info
logging.level.com.example=debug
```

#### application.yml

```yaml
# 服务器配置
server:
  port: 8080
  servlet:
    context-path: /api

# 数据库配置
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: password
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true

# 日志配置
logging:
  level:
    org.springframework: info
    com.example: debug
```

### 2. 多环境配置

Spring Boot 支持为不同环境提供不同的配置文件：

- `application-dev.yml`：开发环境
- `application-test.yml`：测试环境
- `application-prod.yml`：生产环境

#### 激活环境配置

在 `application.yml` 中指定：

```yaml
spring:
  profiles:
    active: dev
```

或使用命令行参数：

```bash
java -jar myapp.jar --spring.profiles.active=prod
```

## 核心配置项

### 1. 服务器配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| server.port | 服务器端口 | 8080 |
| server.servlet.context-path | 应用上下文路径 | / |
| server.tomcat.uri-encoding | URI 编码 | UTF-8 |
| server.tomcat.max-threads | 最大线程数 | 200 |
| server.tomcat.connection-timeout | 连接超时时间 | 20000 |

### 2. 数据库配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| spring.datasource.url | 数据库 URL | - |
| spring.datasource.username | 数据库用户名 | - |
| spring.datasource.password | 数据库密码 | - |
| spring.datasource.driver-class-name | 数据库驱动 | 自动检测 |
| spring.datasource.hikari.maximum-pool-size | 连接池最大连接数 | 10 |
| spring.datasource.hikari.minimum-idle | 连接池最小空闲连接数 | 10 |
| spring.datasource.hikari.idle-timeout | 空闲连接超时时间 | 600000 |

### 3. JPA 配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| spring.jpa.hibernate.ddl-auto | 数据库表结构自动更新策略 | none |
| spring.jpa.show-sql | 是否显示 SQL 语句 | false |
| spring.jpa.properties.hibernate.format_sql | 是否格式化 SQL 语句 | false |
| spring.jpa.properties.hibernate.dialect | Hibernate 方言 | 自动检测 |

### 4. 日志配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| logging.level.* | 日志级别 | info |
| logging.file.name | 日志文件名称 | - |
| logging.file.path | 日志文件路径 | - |
| logging.pattern.console | 控制台日志格式 | %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n |
| logging.pattern.file | 文件日志格式 | %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n |

### 5. 安全配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| spring.security.user.name | 默认用户名 | user |
| spring.security.user.password | 默认密码 | 随机生成 |
| spring.security.user.roles | 默认角色 | USER |

## 自定义配置

### 1. 读取配置

#### 使用 @Value 注解

```java
@Component
public class AppConfig {
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.version}")
    private String appVersion;
    
    // getter 方法
}
```

#### 使用 @ConfigurationProperties 注解

```java
@Component
@ConfigurationProperties(prefix = "app")
public class AppConfig {
    private String name;
    private String version;
    private String description;
    
    // getter 和 setter 方法
}
```

### 2. 配置类

```java
@Configuration
public class DatabaseConfig {
    
    @Bean
    public DataSource dataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
        config.setUsername("root");
        config.setPassword("password");
        return new HikariDataSource(config);
    }
    
    @Bean
    public JdbcTemplate jdbcTemplate(DataSource dataSource) {
        return new JdbcTemplate(dataSource);
    }
}
```

## 外部配置

### 1. 环境变量

Spring Boot 会自动读取环境变量，环境变量名需要使用大写字母和下划线，例如：

```bash
# 设置环境变量
export SPRING_DATASOURCE_URL=jdbc:mysql://localhost:3306/mydb
export SPRING_DATASOURCE_USERNAME=root
export SPRING_DATASOURCE_PASSWORD=password

# 运行应用
java -jar myapp.jar
```

### 2. 命令行参数

```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

### 3. 配置中心

对于微服务架构，可以使用配置中心来管理配置，例如 Spring Cloud Config。

## 配置优先级

Spring Boot 的配置优先级从高到低依次为：

1. 命令行参数
2. 环境变量
3. `application-{profile}.yml` 文件
4. `application.yml` 文件
5. `application-{profile}.properties` 文件
6. `application.properties` 文件
7. 默认配置

## 示例：完整的配置文件

### application.yml

```yaml
# 应用基本配置
spring:
  application:
    name: my-spring-boot-app
  
  # 环境配置
  profiles:
    active: dev
  
  # 数据源配置
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
      idle-timeout: 30000
  
  # JPA 配置
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        dialect: org.hibernate.dialect.MySQL8Dialect
  
  # 消息队列配置
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest

# 服务器配置
server:
  port: 8080
  servlet:
    context-path: /api
  tomcat:
    max-threads: 200
    connection-timeout: 20000

# 日志配置
logging:
  level:
    root: info
    com.example: debug
  file:
    name: logs/app.log
  pattern:
    console: "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"

# 自定义配置
app:
  name: My Spring Boot App
  version: 1.0.0
  description: A simple Spring Boot application
  features:
    - feature1
    - feature2
    - feature3
```

## 最佳实践

### 1. 配置分离

- 将不同环境的配置分离到不同的配置文件中
- 使用 `application.yml` 作为主配置文件，指定激活的环境
- 敏感信息（如数据库密码）应通过环境变量或配置中心管理

### 2. 配置验证

- 使用 `@Validated` 注解和 JSR-303 验证注解验证配置
- 提供默认值，确保配置的健壮性
- 记录配置加载情况，便于排查问题

### 3. 配置管理

- 使用配置中心管理分布式系统的配置
- 实现配置的动态刷新
- 版本控制配置文件

### 4. 性能优化

- 减少配置文件的大小，只包含必要的配置
- 合理设置连接池大小，避免资源浪费
- 优化日志配置，避免过多的日志输出

## 常见问题

### 1. 配置不生效

- 检查配置文件路径是否正确
- 检查配置项名称是否正确
- 检查配置优先级，确保没有被其他配置覆盖
- 检查应用是否正确读取了配置文件

### 2. 敏感信息泄露

- 不要在配置文件中硬编码敏感信息
- 使用环境变量或配置中心管理敏感信息
- 加密敏感配置

### 3. 配置冲突

- 避免在不同的配置文件中重复定义相同的配置项
- 了解配置优先级，避免意外覆盖
- 使用统一的配置管理策略

## 总结

Spring Boot 提供了灵活而强大的配置系统，支持多种配置方式和格式。通过合理的配置管理，可以使应用程序更加灵活、可维护和安全。在实际开发中，应该根据项目的具体需求，选择合适的配置方式，并遵循最佳实践，确保配置的正确性和安全性。