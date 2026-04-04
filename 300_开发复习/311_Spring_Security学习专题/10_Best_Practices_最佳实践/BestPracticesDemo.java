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
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 主应用类
@SpringBootApplication
public class BestPracticesDemo {
    public static void main(String[] args) {
        SpringApplication.run(BestPracticesDemo.class, args);
    }
}

// 控制器
@RestController
@RequestMapping("/api")
class HelloController {
    @GetMapping("/public")
    public String publicEndpoint() {
        return "Public endpoint - no authentication required";
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
    
    @GetMapping("/read")
    @PreAuthorize("hasAuthority('READ')")
    public String readEndpoint() {
        return "Read endpoint - requires READ authority";
    }
    
    @GetMapping("/write")
    @PreAuthorize("hasAuthority('WRITE')")
    public String writeEndpoint() {
        return "Write endpoint - requires WRITE authority";
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
            .authorities("READ")
            .build();
        
        UserDetails admin = User.withUsername("admin")
            .password(passwordEncoder().encode("password"))
            .roles("ADMIN")
            .authorities("READ", "WRITE")
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
                .permitAll()
            .and()
            .csrf()
                .disable()
            .headers()
                .contentTypeOptions()
                .xssProtection()
                .cacheControl()
                .httpStrictTransportSecurity()
                .frameOptions();
    }
}

// 方法安全配置
@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
class MethodSecurityConfig {
}