import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

// 主应用类
@SpringBootApplication
public class ViewsDemo {
    public static void main(String[] args) {
        SpringApplication.run(ViewsDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/views")
class ViewsController {
    @GetMapping("/thymeleaf")
    public String thymeleafExample(Model model) {
        model.addAttribute("message", "Hello from Thymeleaf!");
        model.addAttribute("users", getUsers());
        return "thymeleaf-example";
    }
    
    @GetMapping("/freemarker")
    public String freemarkerExample(Model model) {
        model.addAttribute("message", "Hello from FreeMarker!");
        model.addAttribute("users", getUsers());
        return "freemarker-example";
    }
    
    @GetMapping("/jsp")
    public ModelAndView jspExample() {
        ModelAndView mav = new ModelAndView("jsp-example");
        mav.addObject("message", "Hello from JSP!");
        mav.addObject("users", getUsers());
        return mav;
    }
    
    private java.util.List<User> getUsers() {
        java.util.List<User> users = new java.util.ArrayList<>();
        users.add(new User(1L, "John", "Doe"));
        users.add(new User(2L, "Jane", "Smith"));
        users.add(new User(3L, "Bob", "Johnson"));
        return users;
    }
}

// 用户类
class User {
    private Long id;
    private String firstName;
    private String lastName;
    
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
// Thymeleaf 视图 - thymeleaf-example.html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Thymeleaf Example</title>
</head>
<body>
    <h1 th:text="${message}"></h1>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        <tr th:each="user : ${users}">
            <td th:text="${user.id}"></td>
            <td th:text="${user.firstName}"></td>
            <td th:text="${user.lastName}"></td>
        </tr>
    </table>
</body>
</html>

// FreeMarker 视图 - freemarker-example.ftl
<!DOCTYPE html>
<html>
<head>
    <title>FreeMarker Example</title>
</head>
<body>
    <h1>${message}</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        <#list users as user>
        <tr>
            <td>${user.id}</td>
            <td>${user.firstName}</td>
            <td>${user.lastName}</td>
        </tr>
        </#list>
    </table>
</body>
</html>

// JSP 视图 - jsp-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>JSP Example</title>
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
</body>
</html>
*/