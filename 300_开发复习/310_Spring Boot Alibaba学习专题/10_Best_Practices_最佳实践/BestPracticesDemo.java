import com.alibaba.csp.sentinel.annotation.SentinelResource;
import io.seata.spring.annotation.GlobalTransactional;
import org.apache.dubbo.config.annotation.DubboReference;
import org.apache.dubbo.config.annotation.DubboService;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.context.annotation.Bean;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

// 服务接口
interface UserService {
    User getUserById(Long id);
    List<User> getUsers();
}

// 服务实现
@DubboService
class UserServiceImpl implements UserService {
    @Override
    public User getUserById(Long id) {
        return new User(id, "张三", "zhangsan@example.com");
    }
    
    @Override
    public List<User> getUsers() {
        List<User> users = new ArrayList<>();
        users.add(new User(1L, "张三", "zhangsan@example.com"));
        users.add(new User(2L, "李四", "lisi@example.com"));
        users.add(new User(3L, "王五", "wangwu@example.com"));
        return users;
    }
}

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class BestPracticesDemo {
    public static void main(String[] args) {
        SpringApplication.run(BestPracticesDemo.class, args);
    }
    
    // 配置线程池
    @Bean
    public ExecutorService executorService() {
        return new ThreadPoolExecutor(
            10, // 核心线程数
            20, // 最大线程数
            60L, // 线程空闲时间
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(100), // 阻塞队列
            new ThreadPoolExecutor.CallerRunsPolicy() // 拒绝策略
        );
    }
    
    // 配置 RedisTemplate
    @Bean
    public RedisTemplate<String, Object> redisTemplate(org.springframework.data.redis.connection.RedisConnectionFactory factory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new StringRedisSerializer());
        return template;
    }
}

// 用户控制器
@RestController
@RequestMapping("/api/users")
@RefreshScope
class UserController {
    @Value("${spring.datasource.url}")
    private String datasourceUrl;
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    @SentinelResource(value = "getUserById", fallback = "getUserByIdFallback")
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        // 尝试从缓存获取
        String key = "user:" + id;
        User user = (User) redisTemplate.opsForValue().get(key);
        if (user != null) {
            return user;
        }
        
        // 从数据库获取
        user = new User(id, "张三", "zhangsan@example.com");
        
        // 存入缓存
        redisTemplate.opsForValue().set(key, user, 30, TimeUnit.MINUTES);
        
        return user;
    }
    
    public User getUserByIdFallback(Long id) {
        return new User(id, "默认用户", "default@example.com");
    }
    
    @GetMapping("/config")
    public String getConfig() {
        return "Datasource URL: " + datasourceUrl;
    }
}

// 订单控制器
@RestController
@RequestMapping("/api/orders")
class OrderController {
    private final List<Order> orders = new ArrayList<>();
    private Long nextOrderId = 1L;
    
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
    
    @Autowired
    private ExecutorService executorService;
    
    @DubboReference
    private UserService userService;
    
    @GlobalTransactional
    @PostMapping
    public Order createOrder(@RequestBody Order order) {
        order.setId(nextOrderId++);
        orders.add(order);
        
        // 异步发送消息
        executorService.submit(() -> {
            Message<Order> message = MessageBuilder.withPayload(order).build();
            rocketMQTemplate.syncSend("order-topic", message);
        });
        
        // 调用用户服务
        User user = userService.getUserById(order.getUserId());
        System.out.println("User: " + user.getName());
        
        return order;
    }
    
    @GetMapping
    public List<Order> getOrders() {
        return orders;
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
    private String productId;
    private int count;
    private int status;
    
    public Order() {
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
    
    public String getProductId() {
        return productId;
    }
    
    public void setProductId(String productId) {
        this.productId = productId;
    }
    
    public int getCount() {
        return count;
    }
    
    public void setCount(int count) {
        this.count = count;
    }
    
    public int getStatus() {
        return status;
    }
    
    public void setStatus(int status) {
        this.status = status;
    }
}