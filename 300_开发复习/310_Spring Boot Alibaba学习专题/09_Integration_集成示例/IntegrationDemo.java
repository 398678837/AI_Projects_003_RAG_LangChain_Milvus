import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import io.seata.spring.annotation.GlobalTransactional;
import org.apache.dubbo.config.annotation.DubboReference;
import org.apache.dubbo.config.annotation.DubboService;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

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

// 消息消费者
@RocketMQMessageListener(topic = "order-topic", consumerGroup = "order-consumer-group")
class OrderConsumer implements RocketMQListener<Order> {
    @Override
    public void onMessage(Order order) {
        System.out.println("Received order: " + order);
    }
}

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class IntegrationDemo {
    public static void main(String[] args) {
        SpringApplication.run(IntegrationDemo.class, args);
    }
}

// 用户控制器
@RestController
@RequestMapping("/api/users")
@RefreshScope
class UserController {
    @Value("${spring.datasource.url}")
    private String datasourceUrl;
    
    @SentinelResource(value = "getUserById", fallback = "getUserByIdFallback")
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return new User(id, "张三", "zhangsan@example.com");
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
    
    @DubboReference
    private UserService userService;
    
    @GlobalTransactional
    @PostMapping
    public Order createOrder(@RequestBody Order order) {
        order.setId(nextOrderId++);
        orders.add(order);
        
        // 发送消息
        Message<Order> message = MessageBuilder.withPayload(order).build();
        rocketMQTemplate.syncSend("order-topic", message);
        
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

// 文件控制器
@RestController
@RequestMapping("/api/files")
class FileController {
    private final OSS ossClient;
    private final String bucketName = "your-bucket-name";
    
    public FileController() {
        // 初始化 OSS 客户端
        String endpoint = "oss-cn-hangzhou.aliyuncs.com";
        String accessKeyId = "your-access-key-id";
        String accessKeySecret = "your-access-key-secret";
        this.ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);
    }
    
    @PostMapping("/upload")
    public String upload(@RequestParam("file") MultipartFile file) throws IOException {
        // 生成文件名
        String originalFilename = file.getOriginalFilename();
        String extension = originalFilename.substring(originalFilename.lastIndexOf("."));
        String fileName = UUID.randomUUID().toString() + extension;
        
        // 上传文件
        try (InputStream inputStream = file.getInputStream()) {
            ossClient.putObject(bucketName, fileName, inputStream);
        }
        
        // 生成访问 URL
        return "https://" + bucketName + ".oss-cn-hangzhou.aliyuncs.com/" + fileName;
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
    
    @Override
    public String toString() {
        return "Order{" +
                "id=" + id +
                ", userId=" + userId +
                ", productId='" + productId + '\'' +
                ", count=" + count +
                ", status=" + status +
                '}';
    }
}