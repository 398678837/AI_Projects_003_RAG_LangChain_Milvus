import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class WebDevelopmentDemo {
    public static void main(String[] args) {
        SpringApplication.run(WebDevelopmentDemo.class, args);
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
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        User user = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (user != null) {
            return ResponseEntity.ok(user);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        user.setId(nextId++);
        users.add(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @RequestBody User user) {
        User existingUser = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (existingUser != null) {
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
            return ResponseEntity.ok(existingUser);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        boolean removed = users.removeIf(user -> user.getId().equals(id));
        if (removed) {
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}

@RestController
@RequestMapping("/api/files")
class FileController {
    @PostMapping("/upload")
    public ResponseEntity<String> uploadFile(@RequestParam("file") MultipartFile file) {
        try {
            // 保存文件
            String fileName = file.getOriginalFilename();
            file.transferTo(new File("uploads/" + fileName));
            return ResponseEntity.ok("文件上传成功：" + fileName);
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("文件上传失败：" + e.getMessage());
        }
    }
}

@Controller
class HomeController {
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("message", "欢迎来到 Spring Boot Web 应用");
        return "home";
    }
    
    @GetMapping("/users")
    public String users(Model model) {
        List<User> users = new ArrayList<>();
        users.add(new User(1L, "张三", "zhangsan@example.com"));
        users.add(new User(2L, "李四", "lisi@example.com"));
        users.add(new User(3L, "王五", "wangwu@example.com"));
        model.addAttribute("users", users);
        return "users";
    }
}

@RestControllerAdvice
class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception e) {
        ErrorResponse error = new ErrorResponse();
        error.setStatus(HttpStatus.INTERNAL_SERVER_ERROR.value());
        error.setMessage(e.getMessage());
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}

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

class ErrorResponse {
    private int status;
    private String message;
    
    public int getStatus() {
        return status;
    }
    
    public void setStatus(int status) {
        this.status = status;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
}