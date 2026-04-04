package com.example.spring.bestpractices;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Spring 最佳实践示例
 */
public class BestPracticesDemo {
    
    public static void main(String[] args) {
        // 示例代码，实际应用中会通过Spring Boot启动
        System.out.println("Spring Best Practices Demo");
    }
}

/**
 * 配置类示例
 */
@Configuration
class AppConfig {
    
    @Bean
    public UserService userService(UserRepository userRepository) {
        return new UserServiceImpl(userRepository);
    }
    
    @Bean
    public UserRepository userRepository() {
        return new InMemoryUserRepository();
    }
}

/**
 * 用户模型
 */
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
    
    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "', email='" + email + "'}";
    }
}

/**
 * 用户DTO
 */
class UserDTO {
    private String name;
    private String email;
    
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

/**
 * 用户仓库接口
 */
interface UserRepository {
    User save(User user);
    Optional<User> findById(Long id);
    List<User> findAll();
    void deleteById(Long id);
}

/**
 * 内存用户仓库实现
 */
class InMemoryUserRepository implements UserRepository {
    private final List<User> users = new ArrayList<>();
    private long nextId = 1;
    
    @Override
    public User save(User user) {
        if (user.getId() == null) {
            user.setId(nextId++);
            users.add(user);
        } else {
            users.stream()
                .filter(u -> u.getId().equals(user.getId()))
                .findFirst()
                .ifPresent(u -> {
                    u.setName(user.getName());
                    u.setEmail(user.getEmail());
                });
        }
        return user;
    }
    
    @Override
    public Optional<User> findById(Long id) {
        return users.stream()
            .filter(u -> u.getId().equals(id))
            .findFirst();
    }
    
    @Override
    public List<User> findAll() {
        return new ArrayList<>(users);
    }
    
    @Override
    public void deleteById(Long id) {
        users.removeIf(u -> u.getId().equals(id));
    }
}

/**
 * 用户服务接口
 */
interface UserService {
    User createUser(User user);
    User updateUser(Long id, User user);
    Optional<User> getUser(Long id);
    List<User> getAllUsers();
    void deleteUser(Long id);
}

/**
 * 用户服务实现
 */
@Service
class UserServiceImpl implements UserService {
    
    private final UserRepository userRepository;
    
    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Override
    public User createUser(User user) {
        // 业务逻辑
        return userRepository.save(user);
    }
    
    @Override
    public User updateUser(Long id, User user) {
        Optional<User> existingUser = userRepository.findById(id);
        if (existingUser.isPresent()) {
            user.setId(id);
            return userRepository.save(user);
        } else {
            throw new UserNotFoundException("User not found with id: " + id);
        }
    }
    
    @Override
    public Optional<User> getUser(Long id) {
        return userRepository.findById(id);
    }
    
    @Override
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    @Override
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}

/**
 * 用户控制器
 */
@RestController
@RequestMapping("/api/users")
class UserController {
    
    private final UserService userService;
    
    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody UserDTO userDTO) {
        User user = new User();
        user.setName(userDTO.getName());
        user.setEmail(userDTO.getEmail());
        User createdUser = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdUser);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        Optional<User> user = userService.getUser(id);
        return user.map(ResponseEntity::ok)
            .orElseGet(() -> ResponseEntity.notFound().build());
    }
    
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        List<User> users = userService.getAllUsers();
        return ResponseEntity.ok(users);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @Valid @RequestBody UserDTO userDTO) {
        try {
            User user = new User();
            user.setName(userDTO.getName());
            user.setEmail(userDTO.getEmail());
            User updatedUser = userService.updateUser(id, user);
            return ResponseEntity.ok(updatedUser);
        } catch (UserNotFoundException e) {
            return ResponseEntity.notFound().build();
        }
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}

/**
 * 自定义异常
 */
class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}

/**
 * 全局异常处理器
 */
@ControllerAdvice
class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<String> handleUserNotFoundException(UserNotFoundException e) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(e.getMessage());
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleException(Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Internal server error");
    }
}

/**
 * 配置属性
 */
@Configuration
class ApplicationProperties {
    
    @Value("${app.name:My Application}")
    private String appName;
    
    @Value("${app.version:1.0.0}")
    private String appVersion;
    
    @Value("${app.description:Spring Boot Application}")
    private String appDescription;
    
    public String getAppName() {
        return appName;
    }
    
    public String getAppVersion() {
        return appVersion;
    }
    
    public String getAppDescription() {
        return appDescription;
    }
}

/**
 * 工具类
 */
class StringUtil {
    
    private StringUtil() {
        // 私有构造函数，防止实例化
    }
    
    public static boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }
    
    public static String capitalize(String str) {
        if (isEmpty(str)) {
            return str;
        }
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }
}

/**
 * 异步服务
 */
@Service
class AsyncService {
    
    @org.springframework.scheduling.annotation.Async
    public void processAsyncTask(String taskName) {
        System.out.println("Processing async task: " + taskName + " in thread: " + Thread.currentThread().getName());
        // 模拟耗时操作
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Async task completed: " + taskName);
    }
}

/**
 * 缓存服务
 */
@Service
class CacheService {
    
    @org.springframework.cache.annotation.Cacheable(value = "items", key = "#id")
    public String getItem(Long id) {
        System.out.println("Getting item from database: " + id);
        // 模拟数据库查询
        return "Item " + id;
    }
    
    @org.springframework.cache.annotation.CachePut(value = "items", key = "#id")
    public String updateItem(Long id, String value) {
        System.out.println("Updating item in database: " + id);
        // 模拟数据库更新
        return value;
    }
    
    @org.springframework.cache.annotation.CacheEvict(value = "items", key = "#id")
    public void deleteItem(Long id) {
        System.out.println("Deleting item from database: " + id);
        // 模拟数据库删除
    }
}
