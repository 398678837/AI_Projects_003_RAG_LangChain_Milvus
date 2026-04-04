import org.springframework.boot.SpringApplication;
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.boot.actuate.info.Info;
import org.springframework.boot.actuate.info.InfoContributor;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class ActuatorDemo {
    public static void main(String[] args) {
        SpringApplication.run(ActuatorDemo.class, args);
    }
    
    @Bean
    public HealthIndicator customHealthIndicator() {
        return () -> {
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
        };
    }
    
    @Bean
    public InfoContributor customInfoContributor() {
        return builder -> {
            Map<String, Object> details = new HashMap<>();
            details.put("app", Map.of(
                    "name", "Actuator Demo",
                    "version", "1.0.0",
                    "description", "Spring Boot Actuator Demo Application"
            ));
            details.put("system", Map.of(
                    "environment", "production",
                    "region", "Asia/Shanghai"
            ));
            builder.withDetails(details);
        };
    }
    
    private boolean checkService() {
        // 检查服务是否正常
        // 这里可以添加具体的检查逻辑
        return true;
    }
}

@RestController
@RequestMapping("/api")
class DemoController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, Actuator!";
    }
    
    @GetMapping("/health-check")
    public String healthCheck() {
        return "Service is healthy!";
    }
}

@RestController
@RequestMapping("/actuator/custom")
class CustomEndpointController {
    @GetMapping
    public Map<String, Object> customInfo() {
        Map<String, Object> info = new HashMap<>();
        info.put("status", "UP");
        info.put("message", "自定义端点运行正常");
        info.put("timestamp", System.currentTimeMillis());
        return info;
    }
}