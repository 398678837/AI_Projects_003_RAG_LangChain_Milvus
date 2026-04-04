# Spring Boot Actuator 监控

## Actuator 概述

Spring Boot Actuator 是 Spring Boot 提供的一个监控和管理生产环境应用的功能模块。它提供了一系列端点（endpoints），用于监控应用的运行状态、健康状况、性能指标等。通过 Actuator，开发者可以实时了解应用的运行情况，及时发现和解决问题。

## 核心功能

- **健康检查**：监控应用的健康状况
- **信息端点**：提供应用的基本信息
- **指标监控**：收集应用的性能指标
- **环境变量**：查看应用的环境变量
- **配置属性**：查看应用的配置属性
- **日志管理**：查看和修改应用的日志级别
- **线程转储**：查看应用的线程状态
- **堆转储**：生成应用的堆转储文件
- **HTTP 跟踪**：跟踪 HTTP 请求
- **审计事件**：记录审计事件

## 配置

### 1. 添加依赖

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

### 2. 基本配置

在 `application.yml` 中配置：

```yaml
management:
  endpoints:
    web:
      exposure:
        include: "*"  # 暴露所有端点
  endpoint:
    health:
      show-details: always  # 显示健康检查的详细信息
```

## 常用端点

### 1. 健康检查端点 (`/actuator/health`)

用于检查应用的健康状况，返回应用的健康状态和详细信息。

**响应示例**：

```json
{
  "status": "UP",
  "components": {
    "db": {
      "status": "UP",
      "details": {
        "database": "MySQL",
        "validationQuery": "isValid()"
      }
    },
    "diskSpace": {
      "status": "UP",
      "details": {
        "total": 107374182400,
        "free": 53687091200,
        "threshold": 10485760
      }
    },
    "ping": {
      "status": "UP"
    }
  }
}
```

### 2. 信息端点 (`/actuator/info`)

提供应用的基本信息，如版本、描述等。

**配置示例**：

```yaml
info:
  app:
    name: "My Spring Boot App"
    version: "1.0.0"
    description: "A simple Spring Boot application"
  build:
    artifact: "my-app"
    name: "My App"
    version: "1.0.0"
    group: "com.example"
```

**响应示例**：

```json
{
  "app": {
    "name": "My Spring Boot App",
    "version": "1.0.0",
    "description": "A simple Spring Boot application"
  },
  "build": {
    "artifact": "my-app",
    "name": "My App",
    "version": "1.0.0",
    "group": "com.example"
  }
}
```

### 3. 指标端点 (`/actuator/metrics`)

收集应用的性能指标，如内存使用情况、CPU 使用率、HTTP 请求数等。

**响应示例**：

```json
{
  "names": [
    "jvm.memory.used",
    "jvm.memory.committed",
    "jvm.memory.max",
    "jvm.threads.count",
    "jvm.threads.peak",
    "process.cpu.usage",
    "process.uptime",
    "http.server.requests",
    "tomcat.sessions.active.current",
    "tomcat.sessions.active.max"
  ]
}
```

查看具体指标：`/actuator/metrics/jvm.memory.used`

### 4. 环境变量端点 (`/actuator/env`)

查看应用的环境变量和系统属性。

**响应示例**：

```json
{
  "activeProfiles": [],
  "propertySources": [
    {
      "name": "server.ports",
      "properties": {
        "local.server.port": {
          "value": 8080
        }
      }
    },
    {
      "name": "systemProperties",
      "properties": {
        "java.version": {
          "value": "11.0.12"
        },
        "java.home": {
          "value": "/usr/lib/jvm/java-11-openjdk-amd64"
        }
      }
    }
  ]
}
```

### 5. 配置属性端点 (`/actuator/configprops`)

查看应用的配置属性。

**响应示例**：

```json
{
  "contexts": {
    "application": {
      "beans": {
        "serverProperties": {
          "prefix": "server",
          "properties": {
            "port": 8080,
            "servlet": {
              "contextPath": "/"
            }
          }
        }
      }
    }
  }
}
```

### 6. 日志管理端点 (`/actuator/loggers`)

查看和修改应用的日志级别。

**查看日志级别**：`/actuator/loggers`

**修改日志级别**：发送 POST 请求到 `/actuator/loggers/{name}`

```json
{
  "configuredLevel": "DEBUG"
}
```

### 7. 线程转储端点 (`/actuator/threaddump`)

查看应用的线程状态，用于排查线程问题。

### 8. 堆转储端点 (`/actuator/heapdump`)

生成应用的堆转储文件，用于分析内存问题。

### 9. HTTP 跟踪端点 (`/actuator/httptrace`)

跟踪 HTTP 请求，记录请求和响应的详细信息。

### 10. 审计事件端点 (`/actuator/auditevents`)

记录审计事件，如用户登录、权限变更等。

## 自定义健康检查

### 1. 实现 HealthIndicator 接口

```java
@Component
public class CustomHealthIndicator implements HealthIndicator {
    
    @Override
    public Health health() {
        // 检查自定义服务的健康状态
        boolean serviceUp = checkService();
        
        if (serviceUp) {
            return Health.up()
                    .withDetail("service", "自定义服务运行正常")
                    .withDetail("version", "1.0.0")
                    .build();
        } else {
            return Health.down()
                    .withDetail("service", "自定义服务运行异常")
                    .withDetail("error", "连接超时")
                    .build();
        }
    }
    
    private boolean checkService() {
        // 检查服务是否正常
        // 这里可以添加具体的检查逻辑
        return true;
    }
}
```

### 2. 配置健康检查

在 `application.yml` 中配置：

```yaml
management:
  endpoint:
    health:
      show-details: always
      probes:
        enabled: true
```

## 自定义端点

### 1. 实现 Endpoint 接口

```java
@Component
@Endpoint(id = "custom")
public class CustomEndpoint {
    
    @ReadOperation
    public Map<String, Object> customInfo() {
        Map<String, Object> info = new HashMap<>();
        info.put("status", "UP");
        info.put("message", "自定义端点运行正常");
        info.put("timestamp", LocalDateTime.now());
        return info;
    }
    
    @WriteOperation
    public void updateCustomInfo(@Selector String name, String value) {
        // 更新自定义信息
        System.out.println("更新 " + name + " 为 " + value);
    }
}
```

### 2. 暴露自定义端点

在 `application.yml` 中配置：

```yaml
management:
  endpoints:
    web:
      exposure:
        include: "custom,health,info"
```

## 安全配置

### 1. 基本安全配置

在 `application.yml` 中配置：

```yaml
management:
  endpoints:
    web:
      exposure:
        include: "health,info"
  endpoint:
    health:
      show-details: when_authorized
      roles: ADMIN

spring:
  security:
    user:
      name: admin
      password: admin
      roles: ADMIN
```

### 2. 自定义安全配置

```java
@Configuration
public class ActuatorSecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/actuator/health", "/actuator/info").permitAll()
                .antMatchers("/actuator/**").hasRole("ADMIN")
                .anyRequest().authenticated()
                .and()
            .httpBasic();
    }
}
```

## 监控集成

### 1. 与 Prometheus 集成

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

在 `application.yml` 中配置：

```yaml
management:
  endpoints:
    web:
      exposure:
        include: "prometheus,health,info"
  metrics:
    export:
      prometheus:
        enabled: true
```

访问 `http://localhost:8080/actuator/prometheus` 获取 Prometheus 格式的指标数据。

### 2. 与 Grafana 集成

1. 安装并启动 Prometheus 和 Grafana
2. 配置 Prometheus 抓取 Spring Boot 应用的指标
3. 在 Grafana 中添加 Prometheus 数据源
4. 导入或创建仪表板查看指标

### 3. 与 Spring Boot Admin 集成

Spring Boot Admin 是一个用于管理和监控 Spring Boot 应用的工具。

**服务端配置**：

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-server</artifactId>
    <version>2.7.10</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

在主应用类上添加 `@EnableAdminServer` 注解：

```java
@SpringBootApplication
@EnableAdminServer
public class AdminServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(AdminServerApplication.class, args);
    }
}
```

**客户端配置**：

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-client</artifactId>
    <version>2.7.10</version>
</dependency>
```

在 `application.yml` 中配置：

```yaml
spring:
  boot:
    admin:
      client:
        url: http://localhost:8080

management:
  endpoints:
    web:
      exposure:
        include: "*"
```

## 最佳实践

### 1. 生产环境配置

- 只暴露必要的端点
- 启用安全保护
- 配置健康检查详情级别
- 集成监控系统

### 2. 性能优化

- 配置指标采集频率
- 限制日志级别
- 合理设置线程池大小
- 监控内存使用情况

### 3. 安全措施

- 限制 Actuator 端点的访问
- 使用 HTTPS 保护端点
- 实施认证和授权
- 定期审查访问日志

### 4. 监控策略

- 建立监控仪表板
- 设置合理的告警阈值
- 定期分析监控数据
- 持续优化应用性能

## 示例：完整的监控配置

### 1. 依赖配置

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-registry-prometheus</artifactId>
    </dependency>
</dependencies>
```

### 2. 应用配置

```yaml
spring:
  application:
    name: my-application
  security:
    user:
      name: admin
      password: admin
      roles: ADMIN

management:
  endpoints:
    web:
      exposure:
        include: "health,info,metrics,prometheus"
  endpoint:
    health:
      show-details: when_authorized
      roles: ADMIN
  metrics:
    export:
      prometheus:
        enabled: true

server:
  port: 8080

info:
  app:
    name: "My Application"
    version: "1.0.0"
    description: "A Spring Boot application with Actuator"
```

### 3. 安全配置

```java
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/").permitAll()
                .antMatchers("/actuator/health", "/actuator/info").permitAll()
                .antMatchers("/actuator/**").hasRole("ADMIN")
                .anyRequest().authenticated()
                .and()
            .httpBasic()
                .and()
            .csrf().disable();
    }
}
```

### 4. 自定义健康检查

```java
@Component
public class DatabaseHealthIndicator implements HealthIndicator {
    
    private final DataSource dataSource;
    
    public DatabaseHealthIndicator(DataSource dataSource) {
        this.dataSource = dataSource;
    }
    
    @Override
    public Health health() {
        try (Connection connection = dataSource.getConnection()) {
            if (connection.isValid(1000)) {
                return Health.up()
                        .withDetail("database", "连接正常")
                        .withDetail("url", dataSource.getConnection().getMetaData().getURL())
                        .build();
            } else {
                return Health.down()
                        .withDetail("database", "连接异常")
                        .build();
            }
        } catch (Exception e) {
            return Health.down()
                    .withDetail("database", "连接失败")
                    .withDetail("error", e.getMessage())
                    .build();
        }
    }
}
```

## 常见问题

### 1. 端点访问问题

- 检查端点是否正确暴露
- 检查安全配置是否允许访问
- 检查应用是否正常运行

### 2. 健康检查失败

- 检查依赖服务是否正常
- 检查数据库连接是否正常
- 检查网络连接是否正常

### 3. 指标数据异常

- 检查指标采集配置是否正确
- 检查应用是否存在性能问题
- 检查监控系统是否正常

### 4. 安全配置问题

- 确保 Actuator 端点受到保护
- 使用 HTTPS 保护端点
- 定期更新密码和权限

## 总结

Spring Boot Actuator 是一个强大的监控和管理工具，它提供了一系列端点，用于监控应用的运行状态、健康状况、性能指标等。通过本章节的学习，您应该了解如何配置和使用 Actuator，如何自定义健康检查和端点，以及如何与监控系统集成。在实际开发中，应该根据项目的具体需求，配置适当的 Actuator 端点，并与监控系统集成，确保应用的可靠性和性能。同时，应该注意安全配置，保护 Actuator 端点免受未授权访问。