# Spring Boot 部署

## 部署概述

部署是将应用程序从开发环境转移到生产环境的过程。Spring Boot 提供了多种部署方式，包括传统的 WAR 包部署、可执行 JAR 包部署、容器化部署等。本章节将介绍 Spring Boot 应用的各种部署方式和最佳实践。

## 部署方式

### 1. 可执行 JAR 包部署

Spring Boot 应用默认打包为可执行 JAR 包，这是最常用的部署方式。

#### 构建 JAR 包

```bash
# 使用 Maven 构建
mvn clean package

# 使用 Gradle 构建
gradle clean build
```

#### 运行 JAR 包

```bash
java -jar my-application.jar
```

#### 配置启动参数

```bash
# 指定端口
java -jar my-application.jar --server.port=8081

# 指定环境
java -jar my-application.jar --spring.profiles.active=prod

# 指定配置文件
java -jar my-application.jar --spring.config.location=file:/path/to/application.yml
```

### 2. WAR 包部署

如果需要将 Spring Boot 应用部署到传统的 Servlet 容器中，可以打包为 WAR 包。

#### 配置 POM.xml

```xml
<packaging>war</packaging>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-tomcat</artifactId>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

#### 配置主类

```java
@SpringBootApplication
public class MyApplication extends SpringBootServletInitializer {
    
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
    
    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(MyApplication.class);
    }
}
```

#### 构建 WAR 包

```bash
# 使用 Maven 构建
mvn clean package

# 使用 Gradle 构建
gradle clean build
```

#### 部署到 Servlet 容器

将生成的 WAR 包复制到 Servlet 容器的 `webapps` 目录中。

### 3. 容器化部署

使用 Docker 容器化 Spring Boot 应用，便于在不同环境中一致部署。

#### 创建 Dockerfile

```dockerfile
FROM openjdk:11-jdk-slim

WORKDIR /app

COPY target/my-application.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

#### 构建 Docker 镜像

```bash
docker build -t my-application:1.0 .
```

#### 运行 Docker 容器

```bash
docker run -d -p 8080:8080 --name my-app my-application:1.0
```

#### 使用 Docker Compose

创建 `docker-compose.yml` 文件：

```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=prod
    depends_on:
      - db
  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=myapp
    ports:
      - "3306:3306"
```

启动容器：

```bash
docker-compose up -d
```

### 4. 云平台部署

#### AWS

- **EC2**：在 EC2 实例上部署可执行 JAR 包
- **Elastic Beanstalk**：使用 Elastic Beanstalk 自动部署和扩展应用
- **Lambda**：将 Spring Boot 应用部署为 Lambda 函数

#### Azure

- **App Service**：在 Azure App Service 上部署 Spring Boot 应用
- **Azure Kubernetes Service (AKS)**：在 AKS 上部署容器化的 Spring Boot 应用

#### Google Cloud

- **App Engine**：在 App Engine 上部署 Spring Boot 应用
- **Google Kubernetes Engine (GKE)**：在 GKE 上部署容器化的 Spring Boot 应用

## 部署配置

### 1. 环境配置

为不同环境提供不同的配置文件：

- `application-dev.yml`：开发环境
- `application-test.yml`：测试环境
- `application-prod.yml`：生产环境

### 2. 外部配置

使用外部配置文件覆盖默认配置：

```bash
java -jar my-application.jar --spring.config.location=file:/path/to/application.yml
```

### 3. 环境变量

使用环境变量配置应用：

```bash
export SPRING_DATASOURCE_URL=jdbc:mysql://localhost:3306/mydb
export SPRING_DATASOURCE_USERNAME=root
export SPRING_DATASOURCE_PASSWORD=password
java -jar my-application.jar
```

### 4. 配置中心

使用 Spring Cloud Config 作为配置中心：

```yaml
spring:
  cloud:
    config:
      uri: http://config-server:8888
      profile: prod
      label: master
```

## 部署最佳实践

### 1. 构建优化

- 使用 Maven 或 Gradle 的构建缓存
- 配置构建参数，减少构建时间
- 使用多阶段构建减少 Docker 镜像大小

### 2. 环境管理

- 使用环境变量管理敏感配置
- 使用配置中心集中管理配置
- 为不同环境使用不同的配置文件

### 3. 监控和日志

- 配置应用日志输出到标准输出
- 集成 ELK 或 EFK 栈收集和分析日志
- 使用 Prometheus 和 Grafana 监控应用性能

### 4. 高可用性

- 部署多个应用实例
- 使用负载均衡器分发流量
- 配置健康检查和自动重启

### 5. 安全措施

- 使用 HTTPS 保护应用
- 配置防火墙规则
- 定期更新依赖，修复安全漏洞
- 实施访问控制和认证

### 6. 持续集成和持续部署

- 使用 CI/CD 工具（如 Jenkins、GitHub Actions、GitLab CI）自动化构建和部署
- 配置自动化测试，确保部署的应用质量
- 实施蓝绿部署或金丝雀发布，减少部署风险

## 示例：完整的部署配置

### 1. Docker 部署

**Dockerfile**：

```dockerfile
FROM openjdk:11-jdk-slim as build
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests

FROM openjdk:11-jre-slim
WORKDIR /app
COPY --from=build /app/target/my-application.jar app.jar
EXPOSE 8080
ENV SPRING_PROFILES_ACTIVE=prod
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**docker-compose.yml**：

```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/myapp
      - SPRING_DATASOURCE_USERNAME=root
      - SPRING_DATASOURCE_PASSWORD=root
    depends_on:
      - db
    restart: always
  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=myapp
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql
    restart: always
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    restart: always

volumes:
  mysql-data:
```

**nginx.conf**：

```nginx
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name example.com;
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name example.com;

        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;

        location / {
            proxy_pass http://app:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

### 2. Kubernetes 部署

**deployment.yaml**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-application
  labels:
    app: my-application
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-application
  template:
    metadata:
      labels:
        app: my-application
    spec:
      containers:
      - name: my-application
        image: my-application:1.0
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "prod"
        - name: SPRING_DATASOURCE_URL
          value: "jdbc:mysql://mysql:3306/myapp"
        - name: SPRING_DATASOURCE_USERNAME
          value: "root"
        - name: SPRING_DATASOURCE_PASSWORD
          value: "root"
        readinessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 30
```

**service.yaml**：

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-application
  labels:
    app: my-application
spec:
  selector:
    app: my-application
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

**ingress.yaml**：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-application
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - example.com
    secretName: example-tls
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-application
            port:
              number: 80
```

## 常见问题

### 1. 端口冲突

- 检查应用是否使用了正确的端口
- 检查容器端口映射是否正确
- 检查防火墙规则是否允许端口访问

### 2. 数据库连接问题

- 检查数据库连接字符串是否正确
- 检查数据库服务是否运行
- 检查数据库用户权限是否正确

### 3. 应用启动失败

- 检查应用日志，查找错误信息
- 检查环境变量是否正确设置
- 检查配置文件是否正确

### 4. 性能问题

- 检查应用内存配置是否合理
- 检查数据库查询是否优化
- 检查应用是否存在内存泄漏

### 5. 安全问题

- 检查应用是否使用 HTTPS
- 检查敏感信息是否泄露
- 检查依赖是否存在安全漏洞

## 总结

Spring Boot 提供了多种部署方式，包括可执行 JAR 包部署、WAR 包部署、容器化部署和云平台部署。本章节介绍了 Spring Boot 应用的各种部署方式和最佳实践，包括构建优化、环境管理、监控和日志、高可用性、安全措施以及持续集成和持续部署。通过本章节的学习，您应该了解如何选择合适的部署方式，如何配置部署环境，以及如何遵循部署最佳实践，确保应用的可靠性、安全性和性能。在实际开发中，应该根据项目的具体需求，选择合适的部署方式，并结合 CI/CD 工具，实现自动化部署，提高开发效率和部署质量。