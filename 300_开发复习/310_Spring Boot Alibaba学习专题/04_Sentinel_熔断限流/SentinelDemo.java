import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class SentinelDemo {
    public static void main(String[] args) {
        SpringApplication.run(SentinelDemo.class, args);
    }
}

// 控制器
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
    
    @SentinelResource(value = "getUsers", fallback = "getUsersFallback")
    @GetMapping
    public List<User> getUsers() {
        // 模拟高流量场景
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return users;
    }
    
    public List<User> getUsersFallback() {
        return new ArrayList<>();
    }
    
    @SentinelResource(value = "getUserById", fallback = "getUserByIdFallback", blockHandler = "getUserByIdBlockHandler")
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
    
    public User getUserByIdFallback(Long id) {
        return new User(id, "默认用户", "default@example.com");
    }
    
    public User getUserByIdBlockHandler(Long id, BlockException ex) {
        return new User(id, "限流用户", "blocked@example.com");
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