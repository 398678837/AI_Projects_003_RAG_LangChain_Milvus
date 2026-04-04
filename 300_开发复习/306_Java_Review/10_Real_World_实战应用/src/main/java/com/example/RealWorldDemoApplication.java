package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

// 1. Spring Boot应用
@SpringBootApplication
@RestController
@RequestMapping("/api")
public class RealWorldDemoApplication {
    
    // 模拟数据库
    private List<User> users = new ArrayList<>();
    private AtomicLong nextId = new AtomicLong(1);
    
    // 构造方法，初始化数据
    public RealWorldDemoApplication() {
        User user1 = new User();
        user1.setId(nextId.getAndIncrement());
        user1.setUsername("张三");
        user1.setPassword("123456");
        user1.setEmail("zhangsan@example.com");
        user1.setPhone("13800138000");
        user1.setCreateTime(new Date());
        user1.setUpdateTime(new Date());
        users.add(user1);
        
        User user2 = new User();
        user2.setId(nextId.getAndIncrement());
        user2.setUsername("李四");
        user2.setPassword("123456");
        user2.setEmail("lisi@example.com");
        user2.setPhone("13900139000");
        user2.setCreateTime(new Date());
        user2.setUpdateTime(new Date());
        users.add(user2);
    }
    
    // 获取用户列表
    @GetMapping("/user")
    public List<User> getUsers() {
        return users;
    }
    
    // 根据ID获取用户
    @GetMapping("/user/{id}")
    public User getUserById(@PathVariable Long id) {
        for (User user : users) {
            if (user.getId().equals(id)) {
                return user;
            }
        }
        return null;
    }
    
    // 创建用户
    @PostMapping("/user")
    public User createUser(@RequestBody User user) {
        user.setId(nextId.getAndIncrement());
        user.setCreateTime(new Date());
        user.setUpdateTime(new Date());
        users.add(user);
        return user;
    }
    
    // 更新用户
    @PutMapping("/user/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        for (int i = 0; i < users.size(); i++) {
            if (users.get(i).getId().equals(id)) {
                User existingUser = users.get(i);
                existingUser.setUsername(user.getUsername());
                existingUser.setPassword(user.getPassword());
                existingUser.setEmail(user.getEmail());
                existingUser.setPhone(user.getPhone());
                existingUser.setUpdateTime(new Date());
                return existingUser;
            }
        }
        return null;
    }
    
    // 删除用户
    @DeleteMapping("/user/{id}")
    public void deleteUser(@PathVariable Long id) {
        users.removeIf(user -> user.getId().equals(id));
    }
    
    // 主方法
    public static void main(String[] args) {
        SpringApplication.run(RealWorldDemoApplication.class, args);
    }
}

// 2. 用户实体类
class User {
    private Long id;
    private String username;
    private String password;
    private String email;
    private String phone;
    private Date createTime;
    private Date updateTime;
    
    // getter和setter
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
    
    public String getPassword() {
        return password;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
    }
    
    public Date getCreateTime() {
        return createTime;
    }
    
    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }
    
    public Date getUpdateTime() {
        return updateTime;
    }
    
    public void setUpdateTime(Date updateTime) {
        this.updateTime = updateTime;
    }
}