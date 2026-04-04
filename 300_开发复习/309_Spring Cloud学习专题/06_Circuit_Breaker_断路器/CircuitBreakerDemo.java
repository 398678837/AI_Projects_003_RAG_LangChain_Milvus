import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;

// 服务提供者示例
@SpringBootApplication
@EnableDiscoveryClient
class UserServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }
}

@RestController
@RequestMapping("/api/users")
class UserController {
    private final List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public UserController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "张三", "zhangsan@example.com"));
        users.add(new User(nextId++, "李四", "lisi@example.com"));
        users.add(new User(nextId++, "王五", "wangwu@example.com"));
    }
    
    @GetMapping
    public List<User> getUsers() {
        return users;
    }
    
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        // 模拟服务故障
        if (id == 999) {
            throw new RuntimeException("Service unavailable");
        }
        return users.stream()
                .filter(user -> user.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}

// 服务消费者示例 (使用 Hystrix)
@SpringBootApplication
@EnableDiscoveryClient
@EnableCircuitBreaker
class OrderServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderServiceApplication.class, args);
    }
    
    @Bean
    @LoadBalanced
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}

@RestController
@RequestMapping("/api/orders")
class OrderController {
    private final List<Order> orders = new ArrayList<>();
    private Long nextId = 1L;
    private final UserService userService;
    
    public OrderController(UserService userService) {
        this.userService = userService;
        // 初始化一些测试数据
        orders.add(new Order(nextId++, 1L, "Order 1", 100.0));
        orders.add(new Order(nextId++, 2L, "Order 2", 200.0));
        orders.add(new Order(nextId++, 1L, "Order 3", 150.0));
    }
    
    @GetMapping
    public List<Order> getOrders() {
        return orders;
    }
    
    @GetMapping("/{id}")
    public Order getOrderById(@PathVariable Long id) {
        return orders.stream()
                .filter(order -> order.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
    
    @GetMapping("/user/{userId}")
    public List<Order> getOrdersByUserId(@PathVariable Long userId) {
        // 调用用户服务获取用户信息
        User user = userService.getUserById(userId);
        System.out.println("User: " + user.getName());
        
        return orders.stream()
                .filter(order -> order.getUserId().equals(userId))
                .collect(java.util.stream.Collectors.toList());
    }
}

// 服务消费者示例 (使用 Hystrix)
@org.springframework.stereotype.Service
class UserService {
    private final RestTemplate restTemplate;
    
    public UserService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
    
    // @HystrixCommand(fallbackMethod = "getUserByIdFallback")
    public User getUserById(Long id) {
        return restTemplate.getForObject("http://user-service/api/users/{id}", User.class, id);
    }
    
    public User getUserByIdFallback(Long id) {
        return new User(id, "默认用户", "default@example.com");
    }
}

// 实体类
class User {
    private Long id;
    private String name;
    private String email;
    
    public User() {
    }
    
    public User(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
}

class Order {
    private Long id;
    private Long userId;
    private String description;
    private double amount;
    
    public Order() {
    }
    
    public Order(Long id, Long userId, String description, double amount) {
        this.id = id;
        this.userId = userId;
        this.description = description;
        this.amount = amount;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public Long getUserId() {
        return userId;
    }
    
    public void setUserId(Long userId) {
        this.userId = userId;
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
    }
    
    public double getAmount() {
        return amount;
    }
    
    public void setAmount(double amount) {
        this.amount = amount;
    }
}

// 主应用类
@SpringBootApplication
public class CircuitBreakerDemo {
    public static void main(String[] args) {
        SpringApplication.run(CircuitBreakerDemo.class, args);
    }
}