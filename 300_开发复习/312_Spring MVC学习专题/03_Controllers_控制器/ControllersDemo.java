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

import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
public class ControllersDemo {
    public static void main(String[] args) {
        SpringApplication.run(ControllersDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/users")
class UserController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public UserController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
    }
    
    @GetMapping
    public String listUsers(Model model) {
        model.addAttribute("users", users);
        return "user-list";
    }
    
    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (user == null) {
            model.addAttribute("error", "User not found");
            return "error";
        }
        model.addAttribute("user", user);
        return "user-detail";
    }
    
    @GetMapping("/add")
    public String addUserForm(Model model) {
        model.addAttribute("user", new User());
        return "user-form";
    }
    
    @PostMapping
    public String createUser(User user) {
        user.setId(nextId++);
        users.add(user);
        return "redirect:/users";
    }
    
    @GetMapping("/edit/{id}")
    public String editUserForm(@PathVariable Long id, Model model) {
        User user = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (user == null) {
            model.addAttribute("error", "User not found");
            return "error";
        }
        model.addAttribute("user", user);
        return "user-form";
    }
    
    @PostMapping("/update/{id}")
    public String updateUser(@PathVariable Long id, User user) {
        User existingUser = users.stream()
                .filter(u -> u.getId().equals(id))
                .findFirst()
                .orElse(null);
        if (existingUser != null) {
            existingUser.setFirstName(user.getFirstName());
            existingUser.setLastName(user.getLastName());
        }
        return "redirect:/users";
    }
    
    @PostMapping("/delete/{id}")
    public String deleteUser(@PathVariable Long id) {
        users.removeIf(u -> u.getId().equals(id));
        return "redirect:/users";
    }
}

// REST 控制器
@RestController
@RequestMapping("/api/users")
class ApiUserController {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public ApiUserController() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "John", "Doe"));
        users.add(new User(nextId++, "Jane", "Smith"));
    }
    
    @GetMapping
    public ResponseEntity<List<User>> listUsers() {
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

// 视图类 (模拟JSP视图)
/*
// user-list.jsp
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <a href="/users/add">Add User</a>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Actions</th>
        </tr>
        <c:forEach items="${users}" var="user">
            <tr>
                <td>${user.id}</td>
                <td>${user.firstName}</td>
                <td>${user.lastName}</td>
                <td>
                    <a href="/users/${user.id}">View</a>
                    <a href="/users/edit/${user.id}">Edit</a>
                    <form action="/users/delete/${user.id}" method="post">
                        <button type="submit">Delete</button>
                    </form>
                </td>
            </tr>
        </c:forEach>
    </table>
</body>
</html>

// user-detail.jsp
<!DOCTYPE html>
<html>
<head>
    <title>User Detail</title>
</head>
<body>
    <h1>User Detail</h1>
    <p>ID: ${user.id}</p>
    <p>First Name: ${user.firstName}</p>
    <p>Last Name: ${user.lastName}</p>
    <a href="/users">Back to List</a>
</body>
</html>

// user-form.jsp
<!DOCTYPE html>
<html>
<head>
    <title>User Form</title>
</head>
<body>
    <h1>${user.id == null ? 'Add User' : 'Edit User'}</h1>
    <form action="${user.id == null ? '/users' : '/users/update/' + user.id}" method="post">
        <input type="hidden" name="id" value="${user.id}">
        <div>
            <label>First Name:</label>
            <input type="text" name="firstName" value="${user.firstName}" required>
        </div>
        <div>
            <label>Last Name:</label>
            <input type="text" name="lastName" value="${user.lastName}" required>
        </div>
        <button type="submit">Save</button>
    </form>
    <a href="/users">Back to List</a>
</body>
</html>

// error.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>${error}</p>
    <a href="/users">Back to List</a>
</body>
</html>
*/