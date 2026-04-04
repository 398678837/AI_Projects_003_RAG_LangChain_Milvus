import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

// 主应用类
@SpringBootApplication
public class BasicConceptsDemo {
    public static void main(String[] args) {
        SpringApplication.run(BasicConceptsDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
}

// 控制器
@Controller
@RequestMapping("/hello")
class HelloController {
    @GetMapping
    public String hello(Model model) {
        model.addAttribute("message", "Hello, Spring MVC!");
        return "hello";
    }
    
    @GetMapping("/api")
    @ResponseBody
    public String helloApi() {
        return "Hello, Spring MVC API!";
    }
}

// 视图类 (模拟JSP视图)
// 实际项目中，这会是一个JSP文件：/WEB-INF/views/hello.jsp
/*
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
*/