import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

// 主应用类
@SpringBootApplication
public class RequestHandlingDemo {
    public static void main(String[] args) {
        SpringApplication.run(RequestHandlingDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/request")
class RequestHandlingController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public RequestHandlingController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
        users.add(new User(nextId++, "Bob", "Johnson"));
    }
    
    @GetMapping("/get")
    public String getExample(@RequestParam("name") String name, Model model) {
        model.addAttribute("message", "Hello, " + name + "!");
        return "request-example";
    }
    
    @PostMapping("/post")
    public String postExample(@RequestParam("firstName") String firstName, @RequestParam("lastName") String lastName, Model model) {
        User user = new User(nextId++, firstName, lastName);
        users.add(user);
        model.addAttribute("message", "User created: " + firstName + " " + lastName);
        model.addAttribute("users", users);
        return "request-example";
    }
    
    @GetMapping("/path/{id}")
    public String pathVariableExample(@PathVariable Long id, Model model) {
        User user = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (user != null) {
            model.addAttribute("message", "User found: " + user.getFirstName() + " " + user.getLastName());
        } else {
            model.addAttribute("message", "User not found");
        }
        return "request-example";
    }
    
    @PostMapping("/object")
    public String objectExample(User user, Model model) {
        user.setId(nextId++);
        users.add(user);
        model.addAttribute("message", "User created: " + user.getFirstName() + " " + user.getLastName());
        model.addAttribute("users", users);
        return "request-example";
    }
    
    @PostMapping("/upload")
    public String uploadExample(@RequestParam("file") MultipartFile file, Model model) {
        if (!file.isEmpty()) {
            model.addAttribute("message", "File uploaded: " + file.getOriginalFilename());
        } else {
            model.addAttribute("message", "No file uploaded");
        }
        return "request-example";
    }
    
    @GetMapping("/header")
    public String headerExample(@RequestHeader("User-Agent") String userAgent, Model model) {
        model.addAttribute("message", "User Agent: " + userAgent);
        return "request-example";
    }
    
    @GetMapping("/cookie")
    public String cookieExample(@CookieValue(value = "sessionId", defaultValue = "unknown") String sessionId, Model model) {
        model.addAttribute("message", "Session ID: " + sessionId);
        return "request-example";
    }
}

// REST 控制器
@RestController
@RequestMapping("/api/request")
class ApiRequestHandlingController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public ApiRequestHandlingController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
        users.add(new User(nextId++, "Bob", "Johnson"));
    }
    
    @GetMapping
    public ResponseEntity<List<User>> getUsers() {
        return ResponseEntity.ok(users);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        User user = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
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
        if (existingUser == null) {
            return ResponseEntity.notFound().build();
        }
        existingUser.setFirstName(user.getFirstName());
        existingUser.setLastName(user.getLastName());
        return ResponseEntity.ok(existingUser);
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        boolean removed = users.removeIf(u -> u.getId().equals(id));
        if (!removed) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.noContent().build();
    }
    
    @PatchMapping("/{id}")
    public ResponseEntity<User> patchUser(@PathVariable Long id, @RequestBody Map<String, Object> updates) {
        User existingUser = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (existingUser == null) {
            return ResponseEntity.notFound().build();
        }
        if (updates.containsKey("firstName")) {
            existingUser.setFirstName((String) updates.get("firstName"));
        }
        if (updates.containsKey("lastName")) {
            existingUser.setLastName((String) updates.get("lastName"));
        }
        return ResponseEntity.ok(existingUser);
    }
}

// 用户类
class User {
    private Long id;
    private String firstName;
    private String lastName;
    
    public User() {
    }
    
    public User(Long id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getFirstName() {
        return firstName;
    }
    
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    
    public String getLastName() {
        return lastName;
    }
    
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}

// 视图文件 (模拟)
/*
// request-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Request Handling Example</title>
</head>
<body>
    <h1>${message}</h1>
    <c:if test="${not empty users}">
        <h2>User List</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
            </tr>
            <c:forEach items="${users}" var="user">
                <tr>
                    <td>${user.id}</td>
                    <td>${user.firstName}</td>
                    <td>${user.lastName}</td>
                </tr>
            </c:forEach>
        </table>
    </c:if>
    <h2>GET Request Example</h2>
    <form action="/request/get" method="get">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    <h2>POST Request Example</h2>
    <form action="/request/post" method="post">
        <input type="text" name="firstName" placeholder="First Name">
        <input type="text" name="lastName" placeholder="Last Name">
        <button type="submit">Submit</button>
    </form>
    <h2>Path Variable Example</h2>
    <form action="/request/path/1" method="get">
        <button type="submit">Get User with ID 1</button>
    </form>
    <h2>Object Example</h2>
    <form action="/request/object" method="post">
        <input type="text" name="firstName" placeholder="First Name">
        <input type="text" name="lastName" placeholder="Last Name">
        <button type="submit">Submit</button>
    </form>
    <h2>File Upload Example</h2>
    <form action="/request/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    <h2>Header Example</h2>
    <form action="/request/header" method="get">
        <button type="submit">Get User Agent</button>
    </form>
    <h2>Cookie Example</h2>
    <form action="/request/cookie" method="get">
        <button type="submit">Get Session ID</button>
    </form>
</body>
</html>
*/