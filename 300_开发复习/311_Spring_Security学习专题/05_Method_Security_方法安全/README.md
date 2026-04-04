# Spring Security 方法安全

## 方法安全概述

方法安全是 Spring Security 的核心功能之一，主要负责保护方法的调用安全，通过在方法上使用注解来实现授权控制。本章节将详细介绍 Spring Security 的方法安全功能，帮助开发者了解如何保护方法的调用安全。

## 方法安全的核心概念

### 1. 注解

Spring Security 提供了以下方法安全注解：

- **@PreAuthorize**：在方法调用前进行授权检查
- **@PostAuthorize**：在方法调用后进行授权检查
- **@PreFilter**：在方法调用前对集合参数进行过滤
- **@PostFilter**：在方法调用后对集合返回值进行过滤
- **@Secured**：指定方法需要的角色

### 2. 安全表达式

安全表达式是 Spring Security 中用于表达授权规则的表达式语言，基于 SpEL（Spring Expression Language）。

### 3. 方法安全配置

方法安全配置是 Spring Security 中用于配置方法安全的核心部分，包括启用方法安全、配置安全表达式处理等。

## 方法安全的配置

### 1. 启用方法安全

```java
@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true, securedEnabled = true, jsr250Enabled = true)
public class MethodSecurityConfig {
}
```

### 2. @PreAuthorize 注解

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/user")
    @PreAuthorize("hasRole('USER')")
    public String userEndpoint() {
        return "User endpoint";
    }
    
    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public String adminEndpoint() {
        return "Admin endpoint";
    }
    
    @GetMapping("/user/{username}")
    @PreAuthorize("hasRole('USER') and #username == principal.username")
    public String userSpecificEndpoint(@PathVariable String username) {
        return "User specific endpoint";
    }
}
```

### 3. @PostAuthorize 注解

```java
@Service
public class UserService {
    @PostAuthorize("returnObject.username == principal.username or hasRole('ADMIN')")
    public User getUser(Long id) {
        // 从数据库获取用户
        return userRepository.findById(id).orElse(null);
    }
}
```

### 4. @PreFilter 注解

```java
@Service
public class UserService {
    @PreFilter("filterObject.owner == principal.username or hasRole('ADMIN')")
    public void deleteUsers(List<User> users) {
        // 删除用户
        userRepository.deleteAll(users);
    }
}
```

### 5. @PostFilter 注解

```java
@Service
public class UserService {
    @PostFilter("filterObject.owner == principal.username or hasRole('ADMIN')")
    public List<User> getUsers() {
        // 获取所有用户
        return userRepository.findAll();
    }
}
```

### 6. @Secured 注解

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/user")
    @Secured("ROLE_USER")
    public String userEndpoint() {
        return "User endpoint";
    }
    
    @GetMapping("/admin")
    @Secured("ROLE_ADMIN")
    public String adminEndpoint() {
        return "Admin endpoint";
    }
}
```

## 安全表达式

Spring Security 提供了丰富的安全表达式，用于表达授权规则：

### 1. 常用表达式

- **hasRole([role])**：检查用户是否拥有指定角色
- **hasAnyRole([role1, role2, ...])**：检查用户是否拥有任意一个指定角色
- **hasAuthority([authority])**：检查用户是否拥有指定权限
- **hasAnyAuthority([authority1, authority2, ...])**：检查用户是否拥有任意一个指定权限
- **principal**：获取当前用户的主体
- **authentication**：获取当前用户的认证对象
- **permitAll**：允许所有用户访问
- **denyAll**：拒绝所有用户访问
- **isAnonymous()**：检查用户是否为匿名用户
- **isAuthenticated()**：检查用户是否已认证
- **isRememberMe()**：检查用户是否通过记住我功能认证
- **isFullyAuthenticated()**：检查用户是否完全认证（非匿名且非记住我）
- **returnObject**：获取方法的返回值（仅在 @PostAuthorize 和 @PostFilter 中使用）
- **filterObject**：获取集合中的元素（仅在 @PreFilter 和 @PostFilter 中使用）

### 2. 表达式示例

```java
@PreAuthorize("hasRole('USER')")
public String userEndpoint() {
    return "User endpoint";
}

@PreAuthorize("hasAnyRole('USER', 'ADMIN')")
public String userOrAdminEndpoint() {
    return "User or admin endpoint";
}

@PreAuthorize("hasAuthority('WRITE')")
public String writeEndpoint() {
    return "Write endpoint";
}

@PreAuthorize("principal.username == #username")
public String userSpecificEndpoint(@RequestParam String username) {
    return "User specific endpoint";
}

@PreAuthorize("hasRole('ADMIN') or (hasRole('USER') and principal.username == #username)")
public String adminOrUserSpecificEndpoint(@RequestParam String username) {
    return "Admin or user specific endpoint";
}

@PostAuthorize("returnObject.username == principal.username")
public User getUser(Long id) {
    return userRepository.findById(id).orElse(null);
}

@PreFilter("filterObject.owner == principal.username")
public void deleteUsers(List<User> users) {
    userRepository.deleteAll(users);
}

@PostFilter("filterObject.owner == principal.username")
public List<User> getUsers() {
    return userRepository.findAll();
}
```

## 方法安全的最佳实践

### 1. 最小权限原则

遵循最小权限原则，只授予用户必要的权限：

```java
@PreAuthorize("hasAuthority('READ')")
public String readEndpoint() {
    return "Read endpoint";
}

@PreAuthorize("hasAuthority('WRITE')")
public String writeEndpoint() {
    return "Write endpoint";
}
```

### 2. 基于角色的访问控制

使用基于角色的访问控制，简化授权管理：

```java
@PreAuthorize("hasRole('USER')")
public String userEndpoint() {
    return "User endpoint";
}

@PreAuthorize("hasRole('ADMIN')")
public String adminEndpoint() {
    return "Admin endpoint";
}
```

### 3. 基于表达式的访问控制

使用基于表达式的访问控制，实现复杂的授权规则：

```java
@PreAuthorize("hasRole('ADMIN') or (hasRole('USER') and principal.username == #username)")
public String adminOrUserSpecificEndpoint(@RequestParam String username) {
    return "Admin or user specific endpoint";
}
```

### 4. 方法安全与 Web 安全结合

将方法安全与 Web 安全结合，提高安全性：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/public/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .formLogin();
    }
}

@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class MethodSecurityConfig {
}

@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/public")
    public String publicEndpoint() {
        return "Public endpoint";
    }
    
    @GetMapping("/user")
    @PreAuthorize("hasRole('USER')")
    public String userEndpoint() {
        return "User endpoint";
    }
    
    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public String adminEndpoint() {
        return "Admin endpoint";
    }
}
```

### 5. 自定义安全表达式

实现自定义安全表达式，满足特定的授权需求：

```java
@Component("customSecurityExpression")
public class CustomSecurityExpression {
    public boolean hasPermission(Authentication authentication, String resource, String action) {
        // 自定义权限检查逻辑
        return true;
    }
}

@PreAuthorize("@customSecurityExpression.hasPermission(authentication, 'resource', 'action')")
public String customPermissionEndpoint() {
    return "Custom permission endpoint";
}
```

## 方法安全的常见问题

### 1. 方法安全注解不生效

- **原因**：没有启用全局方法安全
- **解决方案**：添加 @EnableGlobalMethodSecurity 注解

```java
@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class MethodSecurityConfig {
}
```

### 2. 安全表达式语法错误

- **原因**：安全表达式语法错误
- **解决方案**：检查安全表达式语法

### 3. 方法参数在安全表达式中不可用

- **原因**：方法参数在安全表达式中不可用
- **解决方案**：确保方法参数名称在编译时保留

### 4. 方法安全与 Web 安全的冲突

- **原因**：方法安全与 Web 安全的配置冲突
- **解决方案**：协调方法安全与 Web 安全的配置

### 5. 性能问题

- **原因**：方法安全检查可能影响性能
- **解决方案**：合理使用方法安全，避免过度使用

## 总结

Spring Security 的方法安全功能是保护方法调用安全的重要组成部分，通过在方法上使用注解来实现授权控制。本章节详细介绍了 Spring Security 的方法安全功能，包括方法安全的核心概念、配置、安全表达式和最佳实践。通过本章节的学习，您应该了解如何使用方法安全注解保护方法调用，如何使用安全表达式表达复杂的授权规则，以及如何将方法安全与 Web 安全结合。在实际开发中，应该根据项目的具体需求，选择合适的方法安全配置，并遵循最佳实践，确保方法调用的安全性。