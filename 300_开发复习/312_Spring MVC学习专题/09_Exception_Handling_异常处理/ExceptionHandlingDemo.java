package com.example.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * Spring MVC 异常处理示例
 */
@Controller
@RequestMapping("/exception")
public class ExceptionHandlingDemo {
    
    private static final Logger logger = LoggerFactory.getLogger(ExceptionHandlingDemo.class);
    
    /**
     * 测试控制器级异常处理
     */
    @GetMapping("/controller/{id}")
    public String testControllerException(@PathVariable Long id, Model model) {
        if (id == null || id <= 0) {
            throw new IllegalArgumentException("无效的ID参数");
        }
        if (id == 100) {
            throw new ResourceNotFoundException("资源不存在：" + id);
        }
        model.addAttribute("message", "操作成功，ID: " + id);
        return "success";
    }
    
    /**
     * 测试全局异常处理
     */
    @GetMapping("/global/{id}")
    public String testGlobalException(@PathVariable Long id, Model model) {
        if (id == 999) {
            throw new BusinessException("业务逻辑异常：" + id);
        }
        if (id == 888) {
            // 模拟系统异常
            int result = 10 / 0;
        }
        model.addAttribute("message", "操作成功，ID: " + id);
        return "success";
    }
    
    /**
     * 测试表单提交异常
     */
    @PostMapping("/form")
    public String testFormException(String name, Integer age, Model model) {
        if (name == null || name.isEmpty()) {
            throw new ValidationException("姓名不能为空");
        }
        if (age == null || age < 18) {
            throw new ValidationException("年龄必须大于等于18");
        }
        model.addAttribute("message", "表单提交成功");
        return "success";
    }
    
    /**
     * 控制器级异常处理器
     */
    @ExceptionHandler(IllegalArgumentException.class)
    public String handleIllegalArgument(IllegalArgumentException ex, Model model) {
        logger.warn("参数异常: {}", ex.getMessage());
        model.addAttribute("error", ex.getMessage());
        return "error/bad-request";
    }
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public String handleResourceNotFound(ResourceNotFoundException ex, Model model) {
        logger.warn("资源不存在: {}", ex.getMessage());
        model.addAttribute("error", ex.getMessage());
        return "error/not-found";
    }
}

/**
 * 全局异常处理器
 */
@ControllerAdvice
class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(BusinessException.class)
    public String handleBusinessException(BusinessException ex, Model model) {
        logger.error("业务异常: {}", ex.getMessage());
        model.addAttribute("error", ex.getMessage());
        return "error/business-error";
    }
    
    @ExceptionHandler(ValidationException.class)
    public String handleValidationException(ValidationException ex, Model model) {
        logger.warn("验证异常: {}", ex.getMessage());
        model.addAttribute("error", ex.getMessage());
        return "error/validation-error";
    }
    
    @ExceptionHandler(Exception.class)
    public String handleException(Exception ex, Model model) {
        logger.error("系统异常", ex);
        model.addAttribute("error", "系统内部错误，请稍后重试");
        return "error/internal-error";
    }
}

/**
 * REST API 异常处理器
 */
@RestControllerAdvice
class RestExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(RestExceptionHandler.class);
    
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ErrorResponse> handleBusinessException(BusinessException ex) {
        logger.error("业务异常: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse("400", ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(ResourceNotFoundException ex) {
        logger.warn("资源不存在: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse("404", ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception ex) {
        logger.error("系统异常", ex);
        ErrorResponse error = new ErrorResponse("500", "系统内部错误，请稍后重试");
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}

/**
 * 自定义异常类
 */
class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}

class BusinessException extends RuntimeException {
    public BusinessException(String message) {
        super(message);
    }
}

class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
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
    
    public String getCode() {
        return code;
    }
    
    public void setCode(String code) {
        this.code = code;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
}
