package com.example.spring.testing;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;

/**
 * Spring 测试示例
 */
public class TestingDemo {
    
    // 单元测试示例
    @ExtendWith(MockitoExtension.class)
    static class UnitTestExample {
        
        @Mock
        private UserDao userDao;
        
        @Test
        void testGetUser() {
            // 模拟UserDao的行为
            when(userDao.findById(1)).thenReturn(new User(1, "Alice"));
            
            // 创建UserService并注入模拟的UserDao
            UserService userService = new UserService(userDao);
            
            // 测试getUser方法
            User user = userService.getUser(1);
            assertEquals("Alice", user.getName());
        }
    }
    
    // 集成测试示例
    @ExtendWith(SpringExtension.class)
    @SpringBootTest
    static class IntegrationTestExample {
        
        @Autowired
        private UserService userService;
        
        @Test
        void testGetUser() {
            User user = userService.getUser(1);
            assertEquals("Alice", user.getName());
        }
    }
    
    // Web测试示例
    @WebMvcTest(UserController.class)
    static class WebTestExample {
        
        @Autowired
        private MockMvc mockMvc;
        
        @MockBean
        private UserService userService;
        
        @Test
        void testGetUser() throws Exception {
            // 模拟UserService的行为
            when(userService.getUser(1)).thenReturn(new User(1, "Alice"));
            
            // 执行HTTP请求并验证结果
            mockMvc.perform(get("/users/1"))
                .andExpect(status().isOk())
                .andExpect(content().json("{\"id\":1,\"name\":\"Alice\"}"));
        }
    }
}

/**
 * 用户类
 */
class User {
    private int id;
    private String name;
    
    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}

/**
 * 用户DAO接口
 */
interface UserDao {
    User findById(int id);
}

/**
 * 用户DAO实现
 */
class UserDaoImpl implements UserDao {
    @Override
    public User findById(int id) {
        // 实际实现
        return new User(id, "Alice");
    }
}

/**
 * 用户服务
 */
class UserService {
    private final UserDao userDao;
    
    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }
    
    public User getUser(int id) {
        return userDao.findById(id);
    }
}

/**
 * 用户控制器
 */
class UserController {
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    // 实际的控制器方法
    // @GetMapping("/users/{id}")
    public User getUser(int id) {
        return userService.getUser(id);
    }
}

/**
 * 计算器类
 */
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int subtract(int a, int b) {
        return a - b;
    }
    
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public int divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Division by zero");
        }
        return a / b;
    }
}

/**
 * 计算器测试
 */
class CalculatorTest {
    
    @Test
    void testAdd() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }
    
    @Test
    void testSubtract() {
        Calculator calculator = new Calculator();
        int result = calculator.subtract(5, 3);
        assertEquals(2, result);
    }
    
    @Test
    void testMultiply() {
        Calculator calculator = new Calculator();
        int result = calculator.multiply(2, 3);
        assertEquals(6, result);
    }
    
    @Test
    void testDivide() {
        Calculator calculator = new Calculator();
        int result = calculator.divide(6, 3);
        assertEquals(2, result);
    }
    
    @Test
    void testDivideByZero() {
        Calculator calculator = new Calculator();
        try {
            calculator.divide(6, 0);
        } catch (IllegalArgumentException e) {
            assertEquals("Division by zero", e.getMessage());
        }
    }
}
