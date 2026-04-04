import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

// 主应用类
class TestingDemo {
    public static void main(String[] args) {
        // 应用入口
    }
}

// 实体类
class User {
    private Long id;
    private String name;
    private String email;
    
    public User() {
    }
    
    public User(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
}

// 仓库接口
interface UserRepository {
    List<User> findAll();
    Optional<User> findById(Long id);
    User save(User user);
    void deleteById(Long id);
}

// 服务类
class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public List<User> getUsers() {
        return userRepository.findAll();
    }
    
    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }
    
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    public User updateUser(Long id, User user) {
        User existingUser = userRepository.findById(id).orElse(null);
        if (existingUser != null) {
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
            return userRepository.save(existingUser);
        }
        return null;
    }
    
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}

// 控制器
class UserController {
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    public List<User> getUsers() {
        return userService.getUsers();
    }
    
    public User getUserById(Long id) {
        return userService.getUserById(id);
    }
    
    public User createUser(User user) {
        return userService.createUser(user);
    }
    
    public User updateUser(Long id, User user) {
        return userService.updateUser(id, user);
    }
    
    public void deleteUser(Long id) {
        userService.deleteUser(id);
    }
}

// 单元测试 - UserService
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testGetUserById() {
        // 准备数据
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        
        // 测试方法
        User result = userService.getUserById(1L);
        
        // 验证结果
        assertEquals("张三", result.getName());
        assertEquals("zhangsan@example.com", result.getEmail());
        
        // 验证方法调用
        verify(userRepository, times(1)).findById(1L);
    }
    
    @Test
    void testGetUsers() {
        // 准备数据
        List<User> users = new ArrayList<>();
        users.add(new User(1L, "张三", "zhangsan@example.com"));
        users.add(new User(2L, "李四", "lisi@example.com"));
        when(userRepository.findAll()).thenReturn(users);
        
        // 测试方法
        List<User> result = userService.getUsers();
        
        // 验证结果
        assertEquals(2, result.size());
        assertEquals("张三", result.get(0).getName());
        assertEquals("李四", result.get(1).getName());
        
        // 验证方法调用
        verify(userRepository, times(1)).findAll();
    }
}

// 集成测试 - UserController
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testGetUserById() throws Exception {
        // 准备数据
        User user = new User(1L, "张三", "zhangsan@example.com");
        when(userService.getUserById(1L)).thenReturn(user);
        
        // 执行请求
        mockMvc.perform(get("/api/users/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("张三"))
                .andExpect(jsonPath("$.email").value("zhangsan@example.com"));
    }
}