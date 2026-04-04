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
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
public class ResponseHandlingDemo {
    public static void main(String[] args) {
        SpringApplication.run(ResponseHandlingDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/response")
class ResponseHandlingController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public ResponseHandlingController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
        users.add(new User(nextId++, "Bob", "Johnson"));
    }
    
    @GetMapping("/view")
    public String viewResponse(Model model) {
        model.addAttribute("message", "Hello from View Response!");
        model.addAttribute("users", users);
        return "response-example";
    }
    
    @GetMapping("/modelandview")
    public org.springframework.web.servlet.ModelAndView modelAndViewResponse() {
        org.springframework.web.servlet.ModelAndView mav = new org.springframework.web.servlet.ModelAndView("response-example");
        mav.addObject("message", "Hello from ModelAndView Response!");
        mav.addObject("users", users);
        return mav;
    }
    
    @PostMapping("/redirect")
    public String redirectResponse(@RequestParam("name") String name, Model model) {
        model.addAttribute("message", "Hello, " + name + "!");
        return "redirect:/response/view";
    }
    
    @GetMapping("/forward")
    public String forwardResponse() {
        return "forward:/response/view";
    }
    
    @GetMapping("/download")
    public ResponseEntity<Resource> downloadResponse() throws IOException {
        Resource resource = new ClassPathResource("example.txt");
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=example.txt");
        return ResponseEntity.ok()
                .headers(headers)
                .contentLength(resource.contentLength())
                .contentType(MediaType.APPLICATION_OCTET_STREAM)
                .body(resource);
    }
}

// REST 控制器
@RestController
@RequestMapping("/api/response")
class ApiResponseHandlingController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public ApiResponseHandlingController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
        users.add(new User(nextId++, "Bob", "Johnson"));
    }
    
    @GetMapping
    public List<User> listUsers() {
        return users;
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
    
    @GetMapping("/error")
    public ResponseEntity<ErrorResponse> errorResponse() {
        ErrorResponse error = new ErrorResponse("An error occurred");
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
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

// 错误响应类
class ErrorResponse {
    private String message;
    
    public ErrorResponse(String message) {
        this.message = message;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
}

// 视图文件 (模拟)
/*
// response-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Response Handling Example</title>
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
    <h2>Redirect Example</h2>
    <form action="/response/redirect" method="post">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    <h2>Forward Example</h2>
    <a href="/response/forward">Forward to View</a>
    <h2>Download Example</h2>
    <a href="/response/download">Download File</a>
    <h2>REST API Examples</h2>
    <ul>
        <li><a href="/api/response">Get All Users</a></li>
        <li><a href="/api/response/1">Get User with ID 1</a></li>
        <li><a href="/api/response/error">Error Example</a></li>
    </ul>
</body>
</html>
*/