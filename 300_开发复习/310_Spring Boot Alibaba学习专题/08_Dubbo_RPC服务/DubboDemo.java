import org.apache.dubbo.config.annotation.DubboReference;
import org.apache.dubbo.config.annotation.DubboService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

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
public class DubboDemo {
    public static void main(String[] args) {
        SpringApplication.run(DubboDemo.class, args);
    }
}

// 控制器
@RestController
@RequestMapping("/api/users")
class UserController {
    @DubboReference
    private UserService userService;
    
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }
    
    @GetMapping
    public List<User> getUsers() {
        return userService.getUsers();
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