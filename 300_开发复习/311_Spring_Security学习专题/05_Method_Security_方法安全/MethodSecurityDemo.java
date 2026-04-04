import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.access.prepost.PostAuthorize;
import org.springframework.security.access.prepost.PreFilter;
import org.springframework.security.access.prepost.PostFilter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
public class MethodSecurityDemo {
    public static void main(String[] args) {
        SpringApplication.run(MethodSecurityDemo.class, args);
    }
}

// 控制器
@RestController
@RequestMapping("/api")
class HelloController {
    @Autowired
    private UserService userService;
    
    @GetMapping("/public")
    public String publicEndpoint() {
        return "Public endpoint - no authorization required";
    }
    
    @GetMapping("/user")
    @PreAuthorize("hasRole('USER')")
    public String userEndpoint() {
        return "User endpoint - requires USER role";
    }
    
    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public String adminEndpoint() {
        return "Admin endpoint - requires ADMIN role";
    }
    
    @GetMapping("/user/{username}")
    @PreAuthorize("hasRole('USER') and #username == principal.username")
    public String userSpecificEndpoint(@PathVariable String username) {
        return "User specific endpoint - requires USER role and matching username";
    }
    
    @GetMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public List<User> getUsers() {
        return userService.getUsers();
    }
    
    @PostMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }
    
    @DeleteMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUsers(@RequestBody List<User> users) {
        userService.deleteUsers(users);
    }
}

// 服务
@Service
class UserService {
    private List<User> users = new ArrayList<>();
    private Long nextId = 1L;
    
    public UserService() {
        // 初始化一些测试数据
        users.add(new User(nextId++, "user", "user@example.com", "USER"));
        users.add(new User(nextId++, "admin", "admin@example.com", "ADMIN"));
    }
    
    @PostAuthorize("returnObject.username == principal.username or hasRole('ADMIN')")
    public User getUser(Long id) {
        return users.stream()
                .filter(user -> user.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
    
    @PostFilter("hasRole('ADMIN') or filterObject.username == principal.username")
    public List<User> getUsers() {
        return users;
    }
    
    @PreAuthorize("hasRole('ADMIN')")
    public User createUser(User user) {
        user.setId(nextId++);
        users.add(user);
        return user;
    }
    
    @PreAuthorize("hasRole('ADMIN')")
    @PreFilter("hasRole('ADMIN')")
    public void deleteUsers(List<User> users) {
        this.users.removeAll(users);
    }
}

// 实体类
class User {
    private Long id;
    private String username;
    private String email;
    private String role;
    
    public User() {
    }
    
    public User(Long id, String username, String email, String role) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.role = role;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getUsername() {
        return username;
    }
    
    public void setUsername(String username) {
        this.username = username;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getRole() {
        return role;
    }
    
    public void setRole(String role) {
        this.role = role;
    }
}

// 安全配置
@Configuration
@EnableWebSecurity
class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Bean
    public UserDetailsService userDetailsService() {
        UserDetails user = User.withUsername("user")
            .password(passwordEncoder().encode("password"))
            .roles("USER")
            .build();
        
        UserDetails admin = User.withUsername("admin")
            .password(passwordEncoder().encode("password"))
            .roles("ADMIN")
            .build();
        
        return new InMemoryUserDetailsManager(user, admin);
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService()).passwordEncoder(passwordEncoder());
    }
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/api/public").permitAll()
                .anyRequest().authenticated()
            .and()
            .formLogin()
                .permitAll()
            .and()
            .logout()
                .permitAll();
    }
}

// 方法安全配置
@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
class MethodSecurityConfig {
}