# Spring MVC 异常处理

## 1. 异常处理概述

Spring MVC 提供了多种异常处理机制，用于统一处理应用程序中的异常，确保系统的稳定性和可靠性，同时提供友好的错误提示给用户。

### 1.1 异常处理的重要性

- **系统稳定性**：防止未捕获的异常导致应用崩溃
- **用户体验**：提供清晰、友好的错误信息
- **日志记录**：统一记录异常信息，便于问题排查
- **代码整洁**：将异常处理逻辑与业务逻辑分离，提高代码可维护性

## 2. 异常处理方式

### 2.1 控制器级异常处理

在控制器类中使用 `@ExceptionHandler` 注解处理特定类型的异常：

```java
@Controller
public class UserController {
    
    @ExceptionHandler(UserNotFoundException.class)
    public String handleUserNotFound(UserNotFoundException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "error/user-not-found";
    }
    
    // 其他控制器方法
}
```

### 2.2 全局异常处理

使用 `@ControllerAdvice` 注解创建全局异常处理器，处理应用程序中的所有异常：

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    public String handleException(Exception ex, Model model) {
        model.addAttribute("error", "系统内部错误");
        return "error/500";
    }
    
    @ExceptionHandler(NotFoundException.class)
    public String handleNotFound(NotFoundException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "error/404";
    }
}
```

### 2.3  ResponseEntity 处理异常

对于 REST API，可以使用 `ResponseEntity` 返回包含错误信息的 HTTP 响应：

```java
@RestControllerAdvice
public class RestExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception ex) {
        ErrorResponse error = new ErrorResponse("500", "系统内部错误");
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```

### 2.4 自定义异常类

创建自定义异常类，用于表示特定业务场景的异常：

```java
public class BusinessException extends RuntimeException {
    private String errorCode;
    private String errorMessage;
    
    public BusinessException(String errorCode, String errorMessage) {
        super(errorMessage);
        this.errorCode = errorCode;
        this.errorMessage = errorMessage;
    }
    
    // Getters
}
```

## 3. 异常处理流程

### 3.1 异常处理的执行顺序

1. **控制器级异常处理器**：先查找控制器中是否有对应的 `@ExceptionHandler`
2. **全局异常处理器**：如果控制器中没有处理，则查找 `@ControllerAdvice` 中的处理器
3. **默认异常处理器**：如果以上都没有处理，则使用 Spring MVC 的默认异常处理器

### 3.2 异常响应状态码

根据异常类型返回适当的 HTTP 状态码：

| 异常类型 | 状态码 | 描述 |
|---------|--------|------|
| `NotFoundException` | 404 | 资源不存在 |
| `BadRequestException` | 400 | 请求参数错误 |
| `UnauthorizedException` | 401 | 未授权 |
| `ForbiddenException` | 403 | 禁止访问 |
| `InternalServerErrorException` | 500 | 服务器内部错误 |

## 4. 异常处理最佳实践

### 4.1 异常分类

- **业务异常**：由业务逻辑引起的异常，如用户不存在、余额不足等
- **系统异常**：由系统故障引起的异常，如数据库连接失败、网络错误等
- **参数异常**：由用户输入参数错误引起的异常，如格式不正确、缺少必填项等

### 4.2 异常信息国际化

使用国际化资源文件存储异常信息，支持多语言环境：

```properties
# messages.properties
exception.user.notfound=用户不存在
exception.invalid.parameter=参数无效
exception.system.error=系统内部错误
```

### 4.3 异常日志记录

在异常处理器中记录详细的异常信息，便于问题排查：

```java
@ExceptionHandler(Exception.class)
public String handleException(Exception ex, Model model) {
    logger.error("系统异常", ex);
    model.addAttribute("error", "系统内部错误");
    return "error/500";
}
```

### 4.4 异常信息安全

- **生产环境**：不向用户暴露详细的异常信息，只返回友好的错误提示
- **开发环境**：可以返回详细的异常信息，便于开发调试

## 5. 异常处理示例

### 5.1 传统 MVC 应用异常处理

适用于服务器端渲染的应用，返回错误页面：

```java
@ControllerAdvice
public class MvcExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    public ModelAndView handleException(Exception ex) {
        ModelAndView mav = new ModelAndView("error/500");
        mav.addObject("error", "系统内部错误");
        return mav;
    }
    
    @ExceptionHandler(NotFoundException.class)
    public ModelAndView handleNotFound(NotFoundException ex) {
        ModelAndView mav = new ModelAndView("error/404");
        mav.addObject("error", ex.getMessage());
        return mav;
    }
}
```

### 5.2 REST API 异常处理

适用于 RESTful 接口，返回 JSON 格式的错误信息：

```java
@RestControllerAdvice
public class RestExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception ex) {
        ErrorResponse error = new ErrorResponse("500", "系统内部错误");
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
    
    @ExceptionHandler(ValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidation(ValidationException ex) {
        ErrorResponse error = new ErrorResponse("400", ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }
}

public class ErrorResponse {
    private String code;
    private String message;
    
    // Constructors, getters and setters
}
```

### 5.3 自定义业务异常处理

处理特定业务场景的异常：

```java
public class OrderException extends RuntimeException {
    private String orderId;
    private String errorCode;
    
    public OrderException(String orderId, String errorCode, String message) {
        super(message);
        this.orderId = orderId;
        this.errorCode = errorCode;
    }
    
    // Getters
}

@ControllerAdvice
public class OrderExceptionHandler {
    
    @ExceptionHandler(OrderException.class)
    public String handleOrderException(OrderException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        model.addAttribute("orderId", ex.getOrderId());
        return "error/order-error";
    }
}
```

## 6. 异常处理的性能考虑

- **异常捕获开销**：异常处理会产生一定的性能开销，避免在正常业务流程中使用异常控制流程
- **异常粒度**：合理设计异常粒度，避免过于细粒度的异常导致代码复杂度增加
- **异常传递**：避免异常在系统中过多传递，及时处理异常

## 7. 常见异常处理场景

### 7.1 表单提交异常

处理用户表单提交时的验证错误和业务异常：

```java
@PostMapping("/submit")
public String submitForm(@Valid Form form, BindingResult result) {
    if (result.hasErrors()) {
        return "form";
    }
    try {
        // 处理业务逻辑
    } catch (BusinessException e) {
        result.reject("error.business", e.getMessage());
        return "form";
    }
    return "success";
}
```

### 7.2 文件上传异常

处理文件上传时的异常：

```java
@ExceptionHandler(MultipartException.class)
public String handleFileUploadError(MultipartException ex, Model model) {
    model.addAttribute("error", "文件上传失败：" + ex.getMessage());
    return "upload-form";
}
```

### 7.3 数据库异常

处理数据库操作时的异常：

```java
@ExceptionHandler(DataAccessException.class)
public String handleDatabaseError(DataAccessException ex, Model model) {
    logger.error("数据库操作异常", ex);
    model.addAttribute("error", "数据库操作失败，请稍后重试");
    return "error/database-error";
}
```

## 8. 总结

Spring MVC 的异常处理机制提供了灵活、强大的方式来处理应用程序中的异常，确保系统的稳定性和可靠性。通过合理使用控制器级异常处理、全局异常处理和自定义异常类，可以构建更加健壮的应用程序。

在实际开发中，应根据具体业务需求选择合适的异常处理策略，平衡异常处理的全面性和代码的简洁性，确保应用程序的稳定性和用户体验。