package com.example.spring.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.stereotype.Component;

/**
 * Spring AOP 示例
 */
public class AOPDemo {
    
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AOPConfig.class);
        
        UserService userService = context.getBean(UserService.class);
        
        try {
            userService.addUser("Alice");
            System.out.println();
            userService.getUser(1);
            System.out.println();
            userService.deleteUser(1);
        } catch (Exception e) {
            System.out.println("Main caught exception: " + e.getMessage());
        }
        
        context.close();
    }
}

/**
 * AOP配置类
 */
@Configuration
@ComponentScan("com.example.spring.aop")
@EnableAspectJAutoProxy
class AOPConfig {
}

/**
 * 用户服务
 */
@Component
class UserService {
    
    public void addUser(String name) {
        System.out.println("Adding user: " + name);
    }
    
    public String getUser(int id) {
        System.out.println("Getting user with id: " + id);
        return "User " + id;
    }
    
    public void deleteUser(int id) {
        System.out.println("Deleting user with id: " + id);
        throw new RuntimeException("Delete failed");
    }
}

/**
 * 日志切面
 */
@Aspect
@Component
class LoggingAspect {
    
    // 定义切点
    @Pointcut("execution(* com.example.spring.aop.UserService.*(..))")
    private void userServiceMethods() {}
    
    // 前置通知
    @Before("userServiceMethods()")
    public void beforeAdvice(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        Object[] args = joinPoint.getArgs();
        System.out.println("[Before] Method: " + methodName + ", Args: " + java.util.Arrays.toString(args));
    }
    
    // 后置通知
    @After("userServiceMethods()")
    public void afterAdvice(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("[After] Method: " + methodName);
    }
    
    // 返回通知
    @AfterReturning(pointcut = "userServiceMethods()", returning = "result")
    public void afterReturningAdvice(JoinPoint joinPoint, Object result) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("[AfterReturning] Method: " + methodName + ", Result: " + result);
    }
    
    // 异常通知
    @AfterThrowing(pointcut = "userServiceMethods()", throwing = "ex")
    public void afterThrowingAdvice(JoinPoint joinPoint, Exception ex) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("[AfterThrowing] Method: " + methodName + ", Exception: " + ex.getMessage());
    }
    
    // 环绕通知
    @Around("userServiceMethods()")
    public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();
        Object[] args = joinPoint.getArgs();
        
        System.out.println("[Around] Before method: " + methodName + ", Args: " + java.util.Arrays.toString(args));
        
        Object result = null;
        try {
            result = joinPoint.proceed(); // 执行目标方法
            System.out.println("[Around] After returning: " + methodName + ", Result: " + result);
        } catch (Exception e) {
            System.out.println("[Around] After throwing: " + methodName + ", Exception: " + e.getMessage());
            throw e;
        } finally {
            System.out.println("[Around] Finally: " + methodName);
        }
        
        return result;
    }
}

/**
 * 性能监控切面
 */
@Aspect
@Component
class PerformanceAspect {
    
    @Around("execution(* com.example.spring.aop.UserService.*(..))")
    public Object performanceAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        
        Object result = joinPoint.proceed();
        
        long endTime = System.currentTimeMillis();
        long duration = endTime - startTime;
        
        String methodName = joinPoint.getSignature().getName();
        System.out.println("[Performance] Method: " + methodName + " took " + duration + "ms");
        
        return result;
    }
}

/**
 * 安全切面
 */
@Aspect
@Component
class SecurityAspect {
    
    @Before("execution(* com.example.spring.aop.UserService.*(..))")
    public void securityAdvice(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        System.out.println("[Security] Checking permissions for method: " + methodName);
        // 这里可以添加实际的权限检查逻辑
    }
}

/**
 * 事务切面
 */
@Aspect
@Component
class TransactionAspect {
    
    @Around("execution(* com.example.spring.aop.UserService.*(..))")
    public Object transactionAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();
        
        System.out.println("[Transaction] Starting transaction for method: " + methodName);
        
        Object result = null;
        try {
            result = joinPoint.proceed();
            System.out.println("[Transaction] Committing transaction for method: " + methodName);
        } catch (Exception e) {
            System.out.println("[Transaction] Rolling back transaction for method: " + methodName);
            throw e;
        }
        
        return result;
    }
}

/**
 * 自定义注解切面
 */
@Aspect
@Component
class CustomAnnotationAspect {
    
    @Around("@annotation(com.example.spring.aop.Loggable)")
    public Object loggableAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();
        
        System.out.println("[CustomAnnotation] Logging method: " + methodName);
        
        Object result = joinPoint.proceed();
        
        System.out.println("[CustomAnnotation] Logged method: " + methodName);
        
        return result;
    }
}

/**
 * 自定义注解
 */
@interface Loggable {
}

/**
 * 使用自定义注解的服务
 */
@Component
class LoggableService {
    
    @Loggable
    public void doSomething() {
        System.out.println("Doing something...");
    }
}

/**
 * 自定义注解切面测试
 */
class CustomAnnotationTest {
    
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AOPConfig.class);
        
        LoggableService loggableService = context.getBean(LoggableService.class);
        loggableService.doSomething();
        
        context.close();
    }
}

/**
 * 切点表达式示例
 */
@Aspect
@Component
class PointcutExamples {
    
    // 匹配所有公共方法
    @Pointcut("execution(public * *(..))")
    public void publicMethods() {}
    
    // 匹配UserService类的所有方法
    @Pointcut("execution(* com.example.spring.aop.UserService.*(..))")
    public void userServiceMethods() {}
    
    // 匹配以add开头的方法
    @Pointcut("execution(* add*(..))")
    public void addMethods() {}
    
    // 匹配有一个参数的方法
    @Pointcut("execution(* *(*))")
    public void methodsWithOneParam() {}
    
    // 匹配抛出异常的方法
    @Pointcut("execution(* *(*) throws Exception)")
    public void methodsThrowingException() {}
}
