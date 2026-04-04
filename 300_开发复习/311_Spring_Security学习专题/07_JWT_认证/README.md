# Spring Security JWT 认证

## JWT 概述

JWT（JSON Web Token）是一种基于 JSON 的开放标准，用于在各方之间安全地传输信息。JWT 由三部分组成：头部、载荷和签名。Spring Security 提供了对 JWT 的支持，通过集成第三方库（如 jjwt）来实现 JWT 认证。本章节将详细介绍 Spring Security JWT 认证的实现，帮助开发者了解如何使用 JWT 进行认证。

## JWT 的核心概念

### 1. JWT 结构

JWT 由三部分组成，用点（.）分隔：

- **头部（Header）**：包含令牌类型和签名算法
- **载荷（Payload）**：包含声明，如用户信息、过期时间等
- **签名（Signature）**：使用密钥对头部和载荷进行签名，确保令牌的完整性

### 2. 声明类型

JWT 载荷中可以包含以下类型的声明：

- **标准声明**：如 iss（签发者）、sub（主题）、exp（过期时间）、iat（签发时间）等
- **自定义声明**：如用户 ID、角色等

### 3. 认证流程

JWT 认证流程如下：

1. **用户登录**：用户提供用户名和密码
2. **生成 JWT**：服务器验证用户凭证，生成 JWT 并返回给客户端
3. **客户端存储 JWT**：客户端存储 JWT，通常在 localStorage 或 cookie 中
4. **请求资源**：客户端在请求头中携带 JWT
5. **验证 JWT**：服务器验证 JWT 的有效性，如签名、过期时间等
6. **授权访问**：验证通过后，服务器授权用户访问资源

## JWT 的配置

### 1. 添加依赖

**Maven**：

```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```

**Gradle**：

```gradle
implementation 'io.jsonwebtoken:jjwt:0.9.1'
```

### 2. JWT 工具类

```java
@Component
public class JwtUtils {
    private String secret = "secret";
    private long expiration = 3600000; // 1小时
    
    public String generateToken(String username) {
        Date now = new Date();
        Date expiryDate = new Date(now.getTime() + expiration);
        
        return Jwts.builder()
                .setSubject(username)
                .setIssuedAt(now)
                .setExpiration(expiryDate)
                .signWith(SignatureAlgorithm.HS512, secret)
                .compact();
    }
    
    public String getUsernameFromToken(String token) {
        Claims claims = Jwts.parser()
                .setSigningKey(secret)
                .parseClaimsJws(token)
                .getBody();
        
        return claims.getSubject();
    }
    
    public boolean validateToken(String token) {
        try {
            Jwts.parser().setSigningKey(secret).parseClaimsJws(token);
            return true;
        } catch (SignatureException e) {
            System.out.println("Invalid JWT signature: " + e.getMessage());
        } catch (MalformedJwtException e) {
            System.out.println("Invalid JWT token: " + e.getMessage());
        } catch (ExpiredJwtException e) {
            System.out.println("JWT token expired: " + e.getMessage());
        } catch (UnsupportedJwtException e) {
            System.out.println("JWT token is unsupported: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("JWT claims string is empty: " + e.getMessage());
        }
        return false;
    }
}
```

### 3. JWT 过滤器

```java
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    @Autowired
    private JwtUtils jwtUtils;
    
    @Autowired
    private UserDetailsService userDetailsService;
    
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws ServletException, IOException {
        try {
            String jwt = getJwtFromRequest(request);
            if (jwt != null && jwtUtils.validateToken(jwt)) {
                String username = jwtUtils.getUsernameFromToken(jwt);
                UserDetails userDetails = userDetailsService.loadUserByUsername(username);
                UsernamePasswordAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(
                        userDetails, null, userDetails.getAuthorities());
                authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authentication);
            }
        } catch (Exception e) {
            System.out.println("Cannot set user authentication: " + e.getMessage());
        }
        chain.doFilter(request, response);
    }
    
    private String getJwtFromRequest(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (StringUtils.hasText(bearerToken) && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }
}
```

### 4. 安全配置

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Autowired
    private UserDetailsService userDetailsService;
    
    @Autowired
    private JwtAuthenticationFilter jwtAuthenticationFilter;
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService).passwordEncoder(passwordEncoder());
    }
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS);
        
        http.addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class);
    }
    
    @Bean
    @Override
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }
}
```

### 5. 认证控制器

```java
@RestController
@RequestMapping("/api/auth")
public class AuthController {
    @Autowired
    private AuthenticationManager authenticationManager;
    
    @Autowired
    private JwtUtils jwtUtils;
    
    @Autowired
    private UserDetailsService userDetailsService;
    
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest loginRequest) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword()));
        
        SecurityContextHolder.getContext().setAuthentication(authentication);
        String jwt = jwtUtils.generateToken(loginRequest.getUsername());
        
        return ResponseEntity.ok(new JwtResponse(jwt));
    }
    
    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest registerRequest) {
        if (userDetailsService.loadUserByUsername(registerRequest.getUsername()) != null) {
            return ResponseEntity.badRequest().body("Username is already taken");
        }
        
        UserDetails userDetails = User.withUsername(registerRequest.getUsername())
                .password(passwordEncoder().encode(registerRequest.getPassword()))
                .roles("USER")
                .build();
        
        // 保存用户到数据库
        
        return ResponseEntity.ok("User registered successfully");
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

class LoginRequest {
    private String username;
    private String password;
    // getters and setters
}

class RegisterRequest {
    private String username;
    private String password;
    // getters and setters
}

class JwtResponse {
    private String token;
    // getters and setters
}
```

## JWT 的最佳实践

### 1. 使用安全的签名算法

使用安全的签名算法，如 HS256 或 RS256：

```java
// HS256
return Jwts.builder()
        .setSubject(username)
        .setIssuedAt(now)
        .setExpiration(expiryDate)
        .signWith(SignatureAlgorithm.HS256, secret)
        .compact();

// RS256
PrivateKey privateKey = // 加载私钥
return Jwts.builder()
        .setSubject(username)
        .setIssuedAt(now)
        .setExpiration(expiryDate)
        .signWith(privateKey)
        .compact();
```

### 2. 设置合理的过期时间

设置合理的过期时间，避免令牌长期有效：

```java
private long expiration = 3600000; // 1小时
```

### 3. 使用 HTTPS

使用 HTTPS 加密传输 JWT，提高安全性：

```java
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .requiresChannel()
                .anyRequest().requiresSecure();
    }
}
```

### 4. 实现令牌刷新

实现令牌刷新机制，避免用户频繁登录：

```java
@PostMapping("/refresh")
public ResponseEntity<?> refreshToken(@RequestHeader("Authorization") String token) {
    String jwt = token.substring(7);
    if (jwtUtils.validateToken(jwt)) {
        String username = jwtUtils.getUsernameFromToken(jwt);
        String newJwt = jwtUtils.generateToken(username);
        return ResponseEntity.ok(new JwtResponse(newJwt));
    }
    return ResponseEntity.badRequest().body("Invalid token");
}
```

### 5. 实现令牌撤销

实现令牌撤销机制，提高安全性：

```java
@Component
public class JwtUtils {
    private Set<String> revokedTokens = new HashSet<>();
    
    public void revokeToken(String token) {
        revokedTokens.add(token);
    }
    
    public boolean isTokenRevoked(String token) {
        return revokedTokens.contains(token);
    }
    
    public boolean validateToken(String token) {
        if (isTokenRevoked(token)) {
            return false;
        }
        // 其他验证逻辑
        return true;
    }
}

@PostMapping("/logout")
public ResponseEntity<?> logout(@RequestHeader("Authorization") String token) {
    String jwt = token.substring(7);
    jwtUtils.revokeToken(jwt);
    return ResponseEntity.ok("Token revoked successfully");
}
```

## JWT 的常见问题

### 1. 令牌过期

- **原因**：令牌过期
- **解决方案**：实现令牌刷新机制

### 2. 令牌被篡改

- **原因**：令牌被篡改
- **解决方案**：使用安全的签名算法，验证签名

### 3. 令牌泄露

- **原因**：令牌泄露
- **解决方案**：使用 HTTPS，设置合理的过期时间，实现令牌撤销

### 4. 性能问题

- **原因**：JWT 验证频繁，影响性能
- **解决方案**：使用缓存减少 JWT 验证的频率

### 5. 跨域请求被拒绝

- **原因**：跨域请求被拒绝
- **解决方案**：配置 CORS 支持

## 总结

Spring Security 提供了对 JWT 的支持，通过集成第三方库（如 jjwt）来实现 JWT 认证。本章节详细介绍了 Spring Security JWT 认证的实现，包括 JWT 的核心概念、配置、认证流程和最佳实践。通过本章节的学习，您应该了解如何使用 JWT 进行认证，如何配置 JWT 工具类和过滤器，以及如何实现令牌刷新和撤销。在实际开发中，应该根据项目的具体需求，选择合适的 JWT 配置，并遵循最佳实践，确保 JWT 认证的安全性和可靠性。