package com.example.spring.configuration;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.core.env.Environment;

/**
 * Spring 配置类示例
 */
public class ConfigurationDemo {
    
    public static void main(String[] args) {
        // 测试基本配置类
        System.out.println("=== 测试基本配置类 ===");
        AnnotationConfigApplicationContext context1 = new AnnotationConfigApplicationContext(AppConfig.class);
        UserService userService1 = context1.getBean(UserService.class);
        userService1.sayHello();
        context1.close();
        
        // 测试组件扫描
        System.out.println("\n=== 测试组件扫描 ===");
        AnnotationConfigApplicationContext context2 = new AnnotationConfigApplicationContext(ComponentScanConfig.class);
        UserController userController = context2.getBean(UserController.class);
        userController.sayHello();
        context2.close();
        
        // 测试导入配置
        System.out.println("\n=== 测试导入配置 ===");
        AnnotationConfigApplicationContext context3 = new AnnotationConfigApplicationContext(MainConfig.class);
        UserService userService3 = context3.getBean(UserService.class);
        OrderService orderService = context3.getBean(OrderService.class);
        userService3.sayHello();
        orderService.sayHello();
        context3.close();
        
        // 测试属性配置
        System.out.println("\n=== 测试属性配置 ===");
        AnnotationConfigApplicationContext context4 = new AnnotationConfigApplicationContext(PropertyConfig.class);
        DatabaseService databaseService = context4.getBean(DatabaseService.class);
        databaseService.connect();
        context4.close();
        
        // 测试条件配置
        System.out.println("\n=== 测试条件配置 ===");
        System.setProperty("env", "development");
        AnnotationConfigApplicationContext context5 = new AnnotationConfigApplicationContext(ConditionalConfig.class);
        EnvironmentService environmentService = context5.getBean(EnvironmentService.class);
        environmentService.printEnvironment();
        context5.close();
    }
}

/**
 * 应用配置类
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
}

/**
 * 用户服务
 */
class UserService {
    private final UserDao userDao;
    
    public UserService(UserDao userDao) {
        this.userDao = userDao;
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
    @Override
    public String getMessage() {
        return "UserDaoImpl message";
    }
}

/**
 * 组件扫描配置
 */
@Configuration
@ComponentScan("com.example.spring.configuration")
class ComponentScanConfig {
}

/**
 * 用户控制器
 */
@Component
class UserController {
    
    @Autowired
    private UserService userService;
    
    public void sayHello() {
        System.out.println("UserController: Hello!");
        userService.sayHello();
    }
}

/**
 * 数据库配置
 */
@Configuration
class DatabaseConfig {
    
    @Bean
    public DatabaseService databaseService() {
        return new DatabaseService();
    }
}

/**
 * 订单配置
 */
@Configuration
class OrderConfig {
    
    @Bean
    public OrderService orderService() {
        return new OrderService();
    }
}

/**
 * 主配置
 */
@Configuration
@Import({DatabaseConfig.class, OrderConfig.class, AppConfig.class})
class MainConfig {
}

/**
 * 订单服务
 */
class OrderService {
    public void sayHello() {
        System.out.println("OrderService: Hello!");
    }
}

/**
 * 数据库服务
 */
class DatabaseService {
    
    @Value("${database.url:jdbc:mysql://localhost:3306/test}")
    private String url;
    
    @Value("${database.username:root}")
    private String username;
    
    @Value("${database.password:123456}")
    private String password;
    
    public void connect() {
        System.out.println("DatabaseService: Connecting to " + url);
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
    }
}

/**
 * 属性配置
 */
@Configuration
@PropertySource("classpath:application.properties")
class PropertyConfig {
    
    @Autowired
    private Environment environment;
    
    @Bean
    public DatabaseService databaseService() {
        DatabaseService service = new DatabaseService();
        // 可以通过Environment获取属性
        System.out.println("Environment property: database.url = " + environment.getProperty("database.url"));
        return service;
    }
}

/**
 * 条件配置
 */
@Configuration
class ConditionalConfig {
    
    @Bean
    @Conditional(DevelopmentCondition.class)
    public EnvironmentService developmentEnvironmentService() {
        return new DevelopmentEnvironmentService();
    }
    
    @Bean
    @Conditional(ProductionCondition.class)
    public EnvironmentService productionEnvironmentService() {
        return new ProductionEnvironmentService();
    }
}

/**
 * 环境服务接口
 */
interface EnvironmentService {
    void printEnvironment();
}

/**
 * 开发环境服务
 */
class DevelopmentEnvironmentService implements EnvironmentService {
    @Override
    public void printEnvironment() {
        System.out.println("EnvironmentService: Development environment");
    }
}

/**
 * 生产环境服务
 */
class ProductionEnvironmentService implements EnvironmentService {
    @Override
    public void printEnvironment() {
        System.out.println("EnvironmentService: Production environment");
    }
}

/**
 * 开发环境条件
 */
class DevelopmentCondition implements Condition {
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        String env = System.getProperty("env");
        return "development".equals(env);
    }
}

/**
 * 生产环境条件
 */
class ProductionCondition implements Condition {
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        String env = System.getProperty("env");
        return "production".equals(env);
    }
}

/**
 * 配置属性绑定
 */
@Configuration
@ConfigurationProperties(prefix = "app")
class AppProperties {
    private String name;
    private String version;
    private Server server;
    
    public static class Server {
        private int port;
        private String host;
        
        // getters and setters
        public int getPort() { return port; }
        public void setPort(int port) { this.port = port; }
        public String getHost() { return host; }
        public void setHost(String host) { this.host = host; }
    }
    
    // getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getVersion() { return version; }
    public void setVersion(String version) { this.version = version; }
    public Server getServer() { return server; }
    public void setServer(Server server) { this.server = server; }
}

/**
 * 配置属性配置
 */
@Configuration
@EnableConfigurationProperties(AppProperties.class)
class AppConfigProperties {
    
    @Bean
    public AppInfo appInfo(AppProperties properties) {
        return new AppInfo(properties);
    }
}

/**
 * 应用信息
 */
class AppInfo {
    private final AppProperties properties;
    
    public AppInfo(AppProperties properties) {
        this.properties = properties;
    }
    
    public void printInfo() {
        System.out.println("App name: " + properties.getName());
        System.out.println("App version: " + properties.getVersion());
        System.out.println("Server host: " + properties.getServer().getHost());
        System.out.println("Server port: " + properties.getServer().getPort());
    }
}
