import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

// 主应用类
@SpringBootApplication
public class ModelsDemo {
    public static void main(String[] args) {
        SpringApplication.run(ModelsDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/models")
class ModelsController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public ModelsController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
        users.add(new User(nextId++, "Bob", "Johnson"));
    }
    
    @GetMapping("/model")
    public String modelExample(Model model) {
        model.addAttribute("message", "Hello from Model!");
        model.addAttribute("users", users);
        return "model-example";
    }
    
    @GetMapping("/modelmap")
    public String modelMapExample(ModelMap model) {
        model.addAttribute("message", "Hello from ModelMap!");
        model.addAttribute("users", users);
        return "model-example";
    }
    
    @GetMapping("/map")
    public String mapExample(Map<String, Object> model) {
        model.put("message", "Hello from Map!");
        model.put("users", users);
        return "model-example";
    }
    
    @GetMapping("/modelandview")
    public ModelAndView modelAndViewExample() {
        ModelAndView mav = new ModelAndView("model-example");
        mav.addObject("message", "Hello from ModelAndView!");
        mav.addObject("users", users);
        return mav;
    }
    
    @GetMapping("/form")
    public String formExample(Model model) {
        model.addAttribute("user", new User());
        return "user-form";
    }
    
    @PostMapping("/submit")
    public String submitForm(User user, Model model) {
        user.setId(nextId++);
        users.add(user);
        model.addAttribute("message", "User created successfully!");
        model.addAttribute("users", users);
        return "model-example";
    }
    
    @GetMapping("/search")
    public String searchExample(@RequestParam("name") String name, Model model) {
        List<User> filteredUsers = users.stream()
                .filter(user -> user.getFirstName().contains(name) || user.getLastName().contains(name))
                .collect(java.util.stream.Collectors.toList());
        model.addAttribute("message", "Search results for: " + name);
        model.addAttribute("users", filteredUsers);
        return "model-example";
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
// model-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Model Example</title>
</head>
<body>
    <h1>${message}</h1>
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
    <a href="/models/form">Add User</a>
    <form action="/models/search" method="get">
        <input type="text" name="name" placeholder="Search by name">
        <button type="submit">Search</button>
    </form>
</body>
</html>

// user-form.jsp
<!DOCTYPE html>
<html>
<head>
    <title>User Form</title>
</head>
<body>
    <h1>Add User</h1>
    <form action="/models/submit" method="post">
        <div>
            <label>First Name:</label>
            <input type="text" name="firstName" required>
        </div>
        <div>
            <label>Last Name:</label>
            <input type="text" name="lastName" required>
        </div>
        <button type="submit">Save</button>
    </form>
    <a href="/models/model">Back to List</a>
</body>
</html>
*/