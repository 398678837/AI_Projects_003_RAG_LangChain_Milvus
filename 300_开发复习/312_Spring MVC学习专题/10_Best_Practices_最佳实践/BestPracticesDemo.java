package com.example.bestpractices;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import java.util.List;
import java.util.Optional;

/**
 * Spring MVC 最佳实践示例
 */
@Controller
@RequestMapping("/best-practices")
@Validated
public class BestPracticesDemo {
    
    private final UserService userService;
    
    // 构造函数注入，推荐使用
    @Autowired
    public BestPracticesDemo(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * RESTful API 示例 - 获取所有用户
     */
    @GetMapping("/users")
    public ResponseEntity<List<UserDTO>> getUsers() {
        List<UserDTO> users = userService.findAll();
        return ResponseEntity.ok(users);
    }
    
    /**
     * RESTful API 示例 - 根据ID获取用户
     */
    @GetMapping("/users/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable @Min(1) Long id) {
        Optional<UserDTO> user = userService.findById(id);
        return user.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
    
    /**
     * RESTful API 示例 - 创建用户
     */
    @PostMapping("/users")
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody UserCreateDTO userCreateDTO) {
        UserDTO createdUser = userService.create(userCreateDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdUser);
    }
    
    /**
     * RESTful API 示例 - 更新用户
     */
    @PutMapping("/users/{id}")
    public ResponseEntity<UserDTO> updateUser(@PathVariable @Min(1) Long id, 
                                            @Valid @RequestBody UserUpdateDTO userUpdateDTO) {
        Optional<UserDTO> updatedUser = userService.update(id, userUpdateDTO);
        return updatedUser.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
    
    /**
     * RESTful API 示例 - 删除用户
     */
    @DeleteMapping("/users/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable @Min(1) Long id) {
        boolean deleted = userService.delete(id);
        return deleted ? ResponseEntity.noContent().build() : ResponseEntity.notFound().build();
    }
    
    /**
     * 传统 MVC 示例 - 显示用户列表页面
     */
    @GetMapping("/users/page")
    public String getUserPage(Model model) {
        List<UserDTO> users = userService.findAll();
        model.addAttribute("users", users);
        return "users/list";
    }
    
    /**
     * 传统 MVC 示例 - 显示用户详情页面
     */
    @GetMapping("/users/page/{id}")
    public String getUserDetailPage(@PathVariable @Min(1) Long id, Model model) {
        Optional<UserDTO> user = userService.findById(id);
        if (user.isPresent()) {
            model.addAttribute("user", user.get());
            return "users/detail";
        } else {
            model.addAttribute("error", "用户不存在");
            return "error/not-found";
        }
    }
    
    /**
     * 传统 MVC 示例 - 显示创建用户表单
     */
    @GetMapping("/users/page/create")
    public String showCreateForm(Model model) {
        model.addAttribute("userCreateDTO", new UserCreateDTO());
        return "users/create";
    }
    
    /**
     * 传统 MVC 示例 - 处理创建用户表单提交
     */
    @PostMapping("/users/page/create")
    public String processCreateForm(@Valid UserCreateDTO userCreateDTO, Model model) {
        UserDTO createdUser = userService.create(userCreateDTO);
        model.addAttribute("message", "用户创建成功");
        return "redirect:/best-practices/users/page";
    }
}

/**
 * 用户服务接口
 */
interface UserService {
    List<UserDTO> findAll();
    Optional<UserDTO> findById(Long id);
    UserDTO create(UserCreateDTO userCreateDTO);
    Optional<UserDTO> update(Long id, UserUpdateDTO userUpdateDTO);
    boolean delete(Long id);
}

/**
 * 用户数据传输对象
 */
class UserDTO {
    private Long id;
    private String name;
    private String email;
    private int age;
    
    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

/**
 * 创建用户数据传输对象
 */
class UserCreateDTO {
    @NotBlank(message = "姓名不能为空")
    private String name;
    
    @NotBlank(message = "邮箱不能为空")
    private String email;
    
    @Min(value = 18, message = "年龄必须大于等于18")
    private int age;
    
    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

/**
 * 更新用户数据传输对象
 */
class UserUpdateDTO {
    private String name;
    private String email;
    private Integer age;
    
    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
}

/**
 * 全局异常处理器
 */
@RestControllerAdvice
class GlobalExceptionHandler {
    
    @ExceptionHandler(javax.validation.ConstraintViolationException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(javax.validation.ConstraintViolationException ex) {
        String message = ex.getConstraintViolations().stream()
                .map(violation -> violation.getMessage())
                .findFirst()
                .orElse("参数验证失败");
        ErrorResponse error = new ErrorResponse("400", message);
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception ex) {
        ErrorResponse error = new ErrorResponse("500", "系统内部错误");
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}

/**
 * 错误响应类
 */
class ErrorResponse {
    private String code;
    private String message;
    
    public ErrorResponse(String code, String message) {
        this.code = code;
        this.message = message;
    }
    
    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
}
