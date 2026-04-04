import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// 主应用类
@SpringBootApplication
public class CoreComponentsDemo {
    public static void main(String[] args) {
        SpringApplication.run(CoreComponentsDemo.class, args);
    }
}

// 配置类
@Configuration
@EnableWebMvc
class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LoggingInterceptor())
                .addPathPatterns("/**");
    }
}

// 拦截器
class LoggingInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("Pre-handle: " + request.getRequestURI());
        return true;
    }
    
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("Post-handle: " + request.getRequestURI());
    }
    
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("After completion: " + request.getRequestURI());
    }
}

// 控制器
@Controller
@RequestMapping("/core")
class CoreController {
    @GetMapping("/model")
    public String modelExample(Model model) {
        model.addAttribute("message", "Hello from Model!");
        model.addAttribute("user", new User("John", "Doe"));
        return "model-example";
    }
    
    @GetMapping("/modelandview")
    public ModelAndView modelAndViewExample() {
        ModelAndView mav = new ModelAndView("modelandview-example");
        mav.addObject("message", "Hello from ModelAndView!");
        mav.addObject("user", new User("Jane", "Smith"));
        return mav;
    }
    
    @GetMapping("/interceptor")
    public String interceptorExample(Model model) {
        model.addAttribute("message", "Hello from Interceptor Example!");
        return "interceptor-example";
    }
}

// 用户类
class User {
    private String firstName;
    private String lastName;
    
    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
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
// model-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Model Example</title>
</head>
<body>
    <h1>${message}</h1>
    <p>User: ${user.firstName} ${user.lastName}</p>
</body>
</html>

// modelandview-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>ModelAndView Example</title>
</head>
<body>
    <h1>${message}</h1>
    <p>User: ${user.firstName} ${user.lastName}</p>
</body>
</html>

// interceptor-example.jsp
<!DOCTYPE html>
<html>
<head>
    <title>Interceptor Example</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
*/