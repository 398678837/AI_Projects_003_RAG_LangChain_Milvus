package com.example.validation;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.validation.constraints.Email;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;

/**
 * Spring MVC 验证示例
 */
@Controller
@RequestMapping("/validation")
public class ValidationDemo {
    
    /**
     * 显示注册表单
     */
    @GetMapping("/register")
    public String showRegisterForm(Model model) {
        model.addAttribute("user", new User());
        return "register-form";
    }
    
    /**
     * 处理注册请求，使用 @Validated 进行验证
     */
    @PostMapping("/register")
    public String processRegister(@Validated User user, BindingResult result, Model model) {
        if (result.hasErrors()) {
            // 验证失败，返回表单页面
            return "register-form";
        }
        // 验证成功，处理业务逻辑
        model.addAttribute("message", "注册成功！");
        return "success";
    }
    
    /**
     * 显示登录表单
     */
    @GetMapping("/login")
    public String showLoginForm(Model model) {
        model.addAttribute("loginForm", new LoginForm());
        return "login-form";
    }
    
    /**
     * 处理登录请求
     */
    @PostMapping("/login")
    public String processLogin(@Validated LoginForm loginForm, BindingResult result, Model model) {
        if (result.hasErrors()) {
            return "login-form";
        }
        // 验证成功，处理登录逻辑
        model.addAttribute("message", "登录成功！");
        return "success";
    }
    
    /**
     * 显示订单表单
     */
    @GetMapping("/order")
    public String showOrderForm(Model model) {
        Order order = new Order();
        order.setCustomer(new Customer());
        model.addAttribute("order", order);
        return "order-form";
    }
    
    /**
     * 处理订单提交，展示级联验证
     */
    @PostMapping("/order")
    public String processOrder(@Validated Order order, BindingResult result, Model model) {
        if (result.hasErrors()) {
            return "order-form";
        }
        model.addAttribute("message", "订单提交成功！");
        return "success";
    }
    
    /**
     * 用户实体类，包含验证注解
     */
    public static class User {
        
        @NotBlank(message = "用户名不能为空")
        @Size(min = 3, max = 20, message = "用户名长度必须在3-20之间")
        private String username;
        
        @NotBlank(message = "密码不能为空")
        @Size(min = 6, max = 20, message = "密码长度必须在6-20之间")
        private String password;
        
        @NotBlank(message = "邮箱不能为空")
        @Email(message = "邮箱格式不正确")
        private String email;
        
        @Min(value = 18, message = "年龄必须大于等于18")
        private int age;
        
        // Getters and setters
        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getPassword() { return password; }
        public void setPassword(String password) { this.password = password; }
        public String getEmail() { return email; }
        public void setEmail(String email) { this.email = email; }
        public int getAge() { return age; }
        public void setAge(int age) { this.age = age; }
    }
    
    /**
     * 登录表单类
     */
    public static class LoginForm {
        
        @NotBlank(message = "用户名不能为空")
        private String username;
        
        @NotBlank(message = "密码不能为空")
        private String password;
        
        // Getters and setters
        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getPassword() { return password; }
        public void setPassword(String password) { this.password = password; }
    }
    
    /**
     * 订单类，展示级联验证
     */
    public static class Order {
        
        @NotBlank(message = "订单号不能为空")
        private String orderId;
        
        @Min(value = 1, message = "订单金额必须大于0")
        private double amount;
        
        @Validated
        private Customer customer;
        
        // Getters and setters
        public String getOrderId() { return orderId; }
        public void setOrderId(String orderId) { this.orderId = orderId; }
        public double getAmount() { return amount; }
        public void setAmount(double amount) { this.amount = amount; }
        public Customer getCustomer() { return customer; }
        public void setCustomer(Customer customer) { this.customer = customer; }
    }
    
    /**
     * 客户类，作为订单的嵌套对象
     */
    public static class Customer {
        
        @NotBlank(message = "客户姓名不能为空")
        private String name;
        
        @NotBlank(message = "联系电话不能为空")
        private String phone;
        
        @NotBlank(message = "地址不能为空")
        private String address;
        
        // Getters and setters
        public String getName() { return name; }
        public void setName(String name) { this.name = name; }
        public String getPhone() { return phone; }
        public void setPhone(String phone) { this.phone = phone; }
        public String getAddress() { return address; }
        public void setAddress(String address) { this.address = address; }
    }
}
