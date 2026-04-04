import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class CoreConfigurationDemo {
    public static void main(String[] args) {
        SpringApplication.run(CoreConfigurationDemo.class, args);
    }
}

@RestController
@RequestMapping("/api/config")
class ConfigController {
    
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.version}")
    private String appVersion;
    
    private final AppConfig appConfig;
    
    public ConfigController(AppConfig appConfig) {
        this.appConfig = appConfig;
    }
    
    @GetMapping("/basic")
    public ConfigResponse getBasicConfig() {
        ConfigResponse response = new ConfigResponse();
        response.setAppName(appName);
        response.setAppVersion(appVersion);
        return response;
    }
    
    @GetMapping("/advanced")
    public AppConfig getAdvancedConfig() {
        return appConfig;
    }
}

@ConfigurationProperties(prefix = "app")
class AppConfig {
    private String name;
    private String version;
    private String description;
    private Features features;
    
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
    
    public Features getFeatures() {
        return features;
    }
    
    public void setFeatures(Features features) {
        this.features = features;
    }
}

class Features {
    private boolean enableSecurity;
    private boolean enableCache;
    private boolean enableMonitoring;
    
    // getter 和 setter 方法
    public boolean isEnableSecurity() {
        return enableSecurity;
    }
    
    public void setEnableSecurity(boolean enableSecurity) {
        this.enableSecurity = enableSecurity;
    }
    
    public boolean isEnableCache() {
        return enableCache;
    }
    
    public void setEnableCache(boolean enableCache) {
        this.enableCache = enableCache;
    }
    
    public boolean isEnableMonitoring() {
        return enableMonitoring;
    }
    
    public void setEnableMonitoring(boolean enableMonitoring) {
        this.enableMonitoring = enableMonitoring;
    }
}

class ConfigResponse {
    private String appName;
    private String appVersion;
    
    // getter 和 setter 方法
    public String getAppName() {
        return appName;
    }
    
    public void setAppName(String appName) {
        this.appName = appName;
    }
    
    public String getAppVersion() {
        return appVersion;
    }
    
    public void setAppVersion(String appVersion) {
        this.appVersion = appVersion;
    }
}

class AppConfigBeans {
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}