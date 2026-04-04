import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.config.server.EnableConfigServer;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

// Config Server 示例
@SpringBootApplication
@EnableConfigServer
@EnableDiscoveryClient
class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}

// Config Client 示例
@SpringBootApplication
@EnableDiscoveryClient
class ConfigClientApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigClientApplication.class, args);
    }
    
    @Bean
    @ConfigurationProperties(prefix = "app")
    public AppConfig appConfig() {
        return new AppConfig();
    }
}

// 配置类
class AppConfig {
    private String name;
    private String version;
    private String description;
    private Database database;
    
    // getter 和 setter 方法
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getVersion() {
        return version;
    }
    
    public void setVersion(String version) {
        this.version = version;
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
    }
    
    public Database getDatabase() {
        return database;
    }
    
    public void setDatabase(Database database) {
        this.database = database;
    }
}

class Database {
    private String url;
    private String username;
    private String password;
    
    // getter 和 setter 方法
    public String getUrl() {
        return url;
    }
    
    public void setUrl(String url) {
        this.url = url;
    }
    
    public String getUsername() {
        return username;
    }
    
    public void setUsername(String username) {
        this.username = username;
    }
    
    public String getPassword() {
        return password;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }
}

// 控制器
@RestController
@RequestMapping("/api/config")
class ConfigController {
    private final AppConfig appConfig;
    
    public ConfigController(AppConfig appConfig) {
        this.appConfig = appConfig;
    }
    
    @GetMapping
    public Map<String, Object> getConfig() {
        Map<String, Object> config = new HashMap<>();
        config.put("app", Map.of(
                "name", appConfig.getName(),
                "version", appConfig.getVersion(),
                "description", appConfig.getDescription()
        ));
        config.put("database", Map.of(
                "url", appConfig.getDatabase().getUrl(),
                "username", appConfig.getDatabase().getUsername()
                // 密码不返回
        ));
        return config;
    }
}

// 主应用类
@SpringBootApplication
public class ConfigCenterDemo {
    public static void main(String[] args) {
        SpringApplication.run(ConfigCenterDemo.class, args);
    }
}