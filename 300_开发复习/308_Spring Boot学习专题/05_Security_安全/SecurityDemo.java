import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class SecurityDemo {
    public static void main(String[] args) {
        SpringApplication.run(SecurityDemo.class, args);
    }
}

@Configuration
@EnableWebSecurity
class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/", "/home", "/public/**").permitAll()
                .antMatchers("/admin/**").hasRole("ADMIN")
                .antMatchers("/user/**").hasAnyRole("USER", "ADMIN")
                .anyRequest().authenticated()
                .and()
            .formLogin()
                .loginPage("/login")
                .permitAll()
                .and()
            .logout()
                .permitAll();
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth
            .inMemoryAuthentication()
                .withUser("user").password(passwordEncoder().encode("password")).roles("USER")
                .and()
                .withUser("admin").password(passwordEncoder().encode("admin")).roles("ADMIN");
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Bean
    @Override
    public UserDetailsService userDetailsService() {
        UserDetails user = User.builder()
                .username("user")
                .password(passwordEncoder().encode("password"))
                .roles("USER")
                .build();
        
        UserDetails admin = User.builder()
                .username("admin")
                .password(passwordEncoder().encode("admin"))
                .roles("ADMIN")
                .build();
        
        return new InMemoryUserDetailsManager(user, admin);
    }
}

@RestController
class HomeController {
    @GetMapping("/")
    public String home() {
        return "Welcome to the home page!";
    }
    
    @GetMapping("/home")
    public String homePage() {
        return "This is the home page!";
    }
    
    @GetMapping("/public/test")
    public String publicTest() {
        return "This is a public test page!";
    }
    
    @GetMapping("/user/dashboard")
    public String userDashboard() {
        return "Welcome to the user dashboard!";
    }
    
    @GetMapping("/admin/dashboard")
    public String adminDashboard() {
        return "Welcome to the admin dashboard!";
    }
    
    @GetMapping("/login")
    public String login() {
        return "Please login: <form action='/login' method='post'>" +
               "<div><label>Username: <input type='text' name='username'/></label></div>" +
               "<div><label>Password: <input type='password' name='password'/></label></div>" +
               "<div><input type='submit' value='Login'/></div>" +
               "</form>";
    }
}

@RestController
@RequestMapping("/api")
class ApiController {
    @GetMapping("/public")
    public String publicApi() {
        return "This is a public API!";
    }
    
    @GetMapping("/private")
    public String privateApi() {
        return "This is a private API!";
    }
}