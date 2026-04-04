import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class DeploymentDemo {
    public static void main(String[] args) {
        SpringApplication.run(DeploymentDemo.class, args);
    }
}

@RestController
@RequestMapping("/api")
class DeploymentController {
    @GetMapping("/info")
    public Map<String, String> getInfo() {
        Map<String, String> info = new HashMap<>();
        info.put("appName", "Deployment Demo");
        info.put("version", "1.0.0");
        info.put("environment", System.getenv().getOrDefault("SPRING_PROFILES_ACTIVE", "default"));
        info.put("message", "Hello from Spring Boot application!");
        return info;
    }
    
    @GetMapping("/health")
    public Map<String, String> getHealth() {
        Map<String, String> health = new HashMap<>();
        health.put("status", "UP");
        health.put("message", "Application is running successfully!");
        return health;
    }
    
    @GetMapping("/env")
    public Map<String, String> getEnv() {
        Map<String, String> env = new HashMap<>();
        env.put("JAVA_HOME", System.getenv().getOrDefault("JAVA_HOME", "Not set"));
        env.put("SERVER_PORT", System.getenv().getOrDefault("SERVER_PORT", "8080"));
        env.put("DB_URL", System.getenv().getOrDefault("DB_URL", "Not set"));
        return env;
    }
}

// Dockerfile 示例
/*
FROM openjdk:11-jdk-slim

WORKDIR /app

COPY target/deployment-demo.jar app.jar

EXPOSE 8080

ENV SPRING_PROFILES_ACTIVE=prod

ENTRYPOINT ["java", "-jar", "app.jar"]
*/

// docker-compose.yml 示例
/*
version: '3'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - DB_URL=jdbc:mysql://db:3306/mydb
      - DB_USERNAME=root
      - DB_PASSWORD=root
    depends_on:
      - db
  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=mydb
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:
*/

// Kubernetes deployment.yaml 示例
/*
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-demo
  labels:
    app: deployment-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: deployment-demo
  template:
    metadata:
      labels:
        app: deployment-demo
    spec:
      containers:
      - name: deployment-demo
        image: deployment-demo:1.0
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "prod"
        - name: DB_URL
          value: "jdbc:mysql://mysql:3306/mydb"
        - name: DB_USERNAME
          value: "root"
        - name: DB_PASSWORD
          value: "root"
        readinessProbe:
          httpGet:
            path: /api/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /api/health
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 30
*/