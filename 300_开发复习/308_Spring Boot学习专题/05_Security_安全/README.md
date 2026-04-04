# Spring Boot 安全

## 安全概述

Spring Boot 提供了强大的安全功能，通过 Spring Security 框架实现。Spring Security 是一个功能强大且高度可定制的安全框架，用于保护应用程序免受各种安全威胁。本章节将介绍 Spring Boot 中的安全配置和最佳实践。

## Spring Security 基础

### 1. 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

### 2. 默认安全配置

Spring Boot 会自动配置 Spring Security，默认情况下：

- 所有请求都需要认证
- 生成一个默认用户，用户名为 `user`，密码在启动日志中显示
- 启用 CSRF 保护
- 启用会话固定保护
- 启用 XSS 保护
- 启用 HTTP 严格传输安全
- 启用内容安全策略

### 3. 自定义安全配置

创建一个配置类，继承 `WebSecurityConfigurerAdapter`：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/", "/home", "/public/**").permitAll()
                .antMatchers("/admin/**").hasRole("ADMIN")
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
                .withUser("user").password("password").roles("USER")
                .and()
                .withUser("admin").password("admin").roles("ADMIN");
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

## 认证

### 1. 基于内存的认证

```java
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
```

### 2. 基于数据库的认证

```java
@Service
public class UserDetailsServiceImpl implements UserDetailsService {
    
    private final UserRepository userRepository;
    
    public UserDetailsServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User not found"));
        
        return new org.springframework.security.core.userdetails.User(
                user.getUsername(),
                user.getPassword(),
                getAuthorities(user.getRoles())
        );
    }
    
    private Collection<? extends GrantedAuthority> getAuthorities(Set<Role> roles) {
        return roles.stream()
                .map(role -> new SimpleGrantedAuthority("ROLE_" + role.getName()))
                .collect(Collectors.toList());
    }
}
```

在安全配置类中使用：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    private final UserDetailsService userDetailsService;
    
    public SecurityConfig(UserDetailsService userDetailsService) {
        this.userDetailsService = userDetailsService;
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService).passwordEncoder(passwordEncoder());
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    // 其他配置...
}
```

### 3. 基于 LDAP 的认证

```java
@Override
protected void configure(AuthenticationManagerBuilder auth) throws Exception {
    auth
        .ldapAuthentication()
            .userDnPatterns("uid={0},ou=people")
            .groupSearchBase("ou=groups")
            .contextSource()
                .url("ldap://localhost:8389/dc=springframework,dc=org")
                .and()
            .passwordCompare()
                .passwordEncoder(new BCryptPasswordEncoder())
                .passwordAttribute("userPassword");
}
```

## 授权

### 1. 基于角色的访问控制

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        .authorizeRequests()
            .antMatchers("/", "/home").permitAll()
            .antMatchers("/admin/**").hasRole("ADMIN")
            .antMatchers("/user/**").hasAnyRole("USER", "ADMIN")
            .anyRequest().authenticated()
            .and()
        // 其他配置...
}
```

### 2. 基于权限的访问控制

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        .authorizeRequests()
            .antMatchers("/", "/home").permitAll()
            .antMatchers("/admin/**").hasAuthority("ADMIN")
            .antMatchers("/user/**").hasAnyAuthority("USER", "ADMIN")
            .anyRequest().authenticated()
            .and()
        // 其他配置...
}
```

### 3. 方法级安全

在主应用类上添加 `@EnableGlobalMethodSecurity` 注解：

```java
@SpringBootApplication
@EnableGlobalMethodSecurity(prePostEnabled = true, securedEnabled = true, jsr250Enabled = true)
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

在服务层方法上使用安全注解：

```java
@Service
public class UserService {
    
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) {
        // 删除用户
    }
    
    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    public User getUserById(Long id) {
        // 获取用户
    }
    
    @Secured("ROLE_ADMIN")
    public void updateUser(User user) {
        // 更新用户
    }
    
    @RolesAllowed({"USER", "ADMIN"})
    public List<User> getUsers() {
        // 获取用户列表
    }
}
```

## 表单登录

### 1. 自定义登录页面

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        .authorizeRequests()
            .antMatchers("/login", "/resources/**").permitAll()
            .anyRequest().authenticated()
            .and()
        .formLogin()
            .loginPage("/login")
            .loginProcessingUrl("/authenticate")
            .defaultSuccessUrl("/home", true)
            .failureUrl("/login?error=true")
            .usernameParameter("username")
            .passwordParameter("password")
            .and()
        // 其他配置...
}
```

### 2. 登录控制器

```java
@Controller
public class LoginController {
    
    @GetMapping("/login")
    public String login(Model model, String error, String logout) {
        if (error != null) {
            model.addAttribute("error", "用户名或密码错误");
        }
        if (logout != null) {
            model.addAttribute("message", "您已成功登出");
        }
        return "login";
    }
    
    @GetMapping("/home")
    public String home() {
        return "home";
    }
}
```

### 3. 登录页面

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>登录</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">登录</h1>
        <div class="mt-4">
            <form th:action="@{/authenticate}" method="post">
                <div class="form-group">
                    <label for="username">用户名</label>
                    <input type="text" class="form-control" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <button type="submit" class="btn btn-primary">登录</button>
            </form>
            <div th:if="${error}" class="alert alert-danger mt-3">
                <th:text="${error}"></th:text>
            </div>
            <div th:if="${message}" class="alert alert-success mt-3">
                <th:text="${message}"></th:text>
            </div>
        </div>
    </div>
</body>
</html>
```

## 退出登录

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        // 其他配置...
        .logout()
            .logoutUrl("/logout")
            .logoutSuccessUrl("/login?logout=true")
            .invalidateHttpSession(true)
            .deleteCookies("JSESSIONID")
            .and()
        // 其他配置...
}
```

## CSRF 保护

### 1. 启用 CSRF 保护

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        // 其他配置...
        .csrf()
            .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
            .and()
        // 其他配置...
}
```

### 2. 在表单中添加 CSRF 令牌

```html
<form th:action="@{/submit}" method="post">
    <input type="hidden" th:name="${_csrf.parameterName}" th:value="${_csrf.token}">
    <!-- 表单字段 -->
    <button type="submit">提交</button>
</form>
```

### 3. 在 AJAX 请求中添加 CSRF 令牌

```javascript
var token = $(meta[name="_csrf"]).attr(content);
var header = $(meta[name="_csrf_header"]).attr(content);

$.ajax({
    url: "/api/data",
    type: "POST",
    beforeSend: function(xhr) {
        xhr.setRequestHeader(header, token);
    },
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function(response) {
        // 处理响应
    }
});
```

## OAuth2 和 JWT

### 1. OAuth2 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-client</artifactId>
</dependency>
```

在 `application.yml` 中配置：

```yaml
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: your-client-id
            client-secret: your-client-secret
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
            scope:
              - email
              - profile
```

### 2. JWT 配置

在 `pom.xml` 中添加依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

在 `application.yml` 中配置：

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://example.com/oauth2/token
          jwk-set-uri: https://example.com/oauth2/jwks
```

## 安全最佳实践

### 1. 密码管理

- 使用强密码哈希算法（如 BCrypt）
- 实施密码复杂度要求
- 定期要求用户更改密码
- 限制登录尝试次数

### 2. 认证和授权

- 实施最小权限原则
- 使用基于角色的访问控制
- 对敏感操作进行额外验证
- 定期审查权限设置

### 3. 输入验证

- 验证所有用户输入
- 使用参数化查询防止 SQL 注入
- 防止 XSS 攻击
- 防止 CSRF 攻击

### 4. 会话管理

- 使用安全的会话管理
- 实施会话超时
- 防止会话固定攻击
- 使用 HTTPS 保护会话

### 5. 日志和监控

- 记录安全事件
- 监控异常登录尝试
- 定期审查安全日志
- 实施安全告警

### 6. 安全头部

- 配置适当的安全头部
- 启用 HTTP 严格传输安全 (HSTS)
- 配置内容安全策略 (CSP)
- 启用 X-XSS-Protection
- 启用 X-Content-Type-Options

## 示例：完整的安全配置

### 1. 安全配置类

```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    private final UserDetailsService userDetailsService;
    
    public SecurityConfig(UserDetailsService userDetailsService) {
        this.userDetailsService = userDetailsService;
    }
    
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
                .loginProcessingUrl("/authenticate")
                .defaultSuccessUrl("/home", true)
                .failureUrl("/login?error=true")
                .permitAll()
                .and()
            .logout()
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login?logout=true")
                .invalidateHttpSession(true)
                .deleteCookies("JSESSIONID")
                .permitAll()
                .and()
            .csrf()
                .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
                .and()
            .headers()
                .frameOptions().sameOrigin()
                .httpStrictTransportSecurity().includeSubDomains(true).maxAgeInSeconds(31536000)
                .contentSecurityPolicy("default-src 'self'; script-src 'self' https://trusted-cdn.com; style-src 'self' https://trusted-cdn.com; img-src 'self' data: https://trusted-cdn.com;");
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService).passwordEncoder(passwordEncoder());
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### 2. 用户服务

```java
@Service
public class UserService {
    
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    public List<User> getUsers() {
        return userRepository.findAll();
    }
    
    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }
    
    @PreAuthorize("hasRole('ADMIN')")
    public User createUser(User user) {
        user.setPassword(passwordEncoder().encode(user.getPassword()));
        return userRepository.save(user);
    }
    
    @PreAuthorize("hasRole('ADMIN') or #id == principal.id")
    public User updateUser(Long id, User user) {
        User existingUser = userRepository.findById(id).orElse(null);
        if (existingUser != null) {
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
            if (user.getPassword() != null && !user.getPassword().isEmpty()) {
                existingUser.setPassword(passwordEncoder().encode(user.getPassword()));
            }
            return userRepository.save(existingUser);
        }
        return null;
    }
    
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

## 常见问题

### 1. 密码加密

- 使用 `BCryptPasswordEncoder` 进行密码加密
- 不要存储明文密码
- 定期更新密码哈希算法

### 2. 权限问题

- 确保用户只能访问授权的资源
- 实施最小权限原则
- 定期审查权限设置

### 3. CSRF 保护

- 启用 CSRF 保护
- 在所有表单和 AJAX 请求中包含 CSRF 令牌
- 对敏感操作进行额外验证

### 4. 会话管理

- 配置适当的会话超时
- 防止会话固定攻击
- 使用 HTTPS 保护会话

### 5. 安全头部

- 配置适当的安全头部
- 启用 HSTS
- 配置 CSP

## 总结

Spring Boot 提供了强大的安全功能，通过 Spring Security 框架实现。本章节介绍了 Spring Boot 中的安全配置，包括认证、授权、表单登录、退出登录、CSRF 保护、OAuth2 和 JWT 等功能。通过本章节的学习，您应该了解如何在 Spring Boot 应用中实现安全保护，以及如何遵循安全最佳实践，确保应用程序的安全性。在实际开发中，应该根据项目的具体需求，配置适当的安全策略，并定期审查和更新安全配置，以应对不断变化的安全威胁。