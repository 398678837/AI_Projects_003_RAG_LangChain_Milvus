package com.example.spring.eventdriven;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEvent;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.ApplicationEventPublisherAware;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAsync;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;

/**
 * Spring 事件驱动示例
 */
public class EventDrivenDemo {
    
    public static void main(String[] args) throws InterruptedException {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(EventConfig.class);
        
        // 测试自定义事件
        System.out.println("=== 测试自定义事件 ===");
        EventPublisher eventPublisher = context.getBean(EventPublisher.class);
        eventPublisher.publishCustomEvent("Hello, Spring Event!");
        
        // 测试任意对象事件
        System.out.println("\n=== 测试任意对象事件 ===");
        ObjectEventPublisher objectEventPublisher = context.getBean(ObjectEventPublisher.class);
        objectEventPublisher.publishStringEvent("Hello, Object Event!");
        
        // 测试异步事件
        System.out.println("\n=== 测试异步事件 ===");
        AsyncEventPublisher asyncEventPublisher = context.getBean(AsyncEventPublisher.class);
        CountDownLatch latch = new CountDownLatch(1);
        asyncEventPublisher.publishAsyncEvent("Hello, Async Event!", latch);
        
        // 等待异步事件处理完成
        latch.await(5, TimeUnit.SECONDS);
        
        // 测试事件顺序
        System.out.println("\n=== 测试事件顺序 ===");
        eventPublisher.publishOrderEvent("Hello, Ordered Event!");
        
        // 测试条件事件
        System.out.println("\n=== 测试条件事件 ===");
        eventPublisher.publishConditionalEvent("important");
        eventPublisher.publishConditionalEvent("normal");
        
        // 关闭上下文
        context.close();
    }
}

/**
 * 事件配置类
 */
@Configuration
@ComponentScan("com.example.spring.eventdriven")
@EnableAsync
class EventConfig {
}

/**
 * 自定义事件
 */
class CustomEvent extends ApplicationEvent {
    private String message;
    
    public CustomEvent(Object source, String message) {
        super(source);
        this.message = message;
    }
    
    public String getMessage() {
        return message;
    }
}

/**
 * 订单事件
 */
class OrderEvent extends ApplicationEvent {
    private String message;
    
    public OrderEvent(Object source, String message) {
        super(source);
        this.message = message;
    }
    
    public String getMessage() {
        return message;
    }
}

/**
 * 事件发布者
 */
@Component
class EventPublisher implements ApplicationEventPublisherAware {
    
    private ApplicationEventPublisher publisher;
    
    @Override
    public void setApplicationEventPublisher(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }
    
    public void publishCustomEvent(String message) {
        CustomEvent event = new CustomEvent(this, message);
        publisher.publishEvent(event);
    }
    
    public void publishOrderEvent(String message) {
        OrderEvent event = new OrderEvent(this, message);
        publisher.publishEvent(event);
    }
    
    public void publishConditionalEvent(String message) {
        CustomEvent event = new CustomEvent(this, message);
        publisher.publishEvent(event);
    }
}

/**
 * 对象事件发布者
 */
@Component
class ObjectEventPublisher {
    
    private final ApplicationEventPublisher publisher;
    
    @Autowired
    public ObjectEventPublisher(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }
    
    public void publishStringEvent(String message) {
        // 直接发布字符串作为事件
        publisher.publishEvent(message);
    }
    
    public void publishObjectEvent(Object object) {
        // 直接发布对象作为事件
        publisher.publishEvent(object);
    }
}

/**
 * 异步事件发布者
 */
@Component
class AsyncEventPublisher {
    
    private final ApplicationEventPublisher publisher;
    
    @Autowired
    public AsyncEventPublisher(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }
    
    public void publishAsyncEvent(String message, CountDownLatch latch) {
        AsyncEvent event = new AsyncEvent(this, message, latch);
        publisher.publishEvent(event);
    }
}

/**
 * 异步事件
 */
class AsyncEvent extends ApplicationEvent {
    private String message;
    private CountDownLatch latch;
    
    public AsyncEvent(Object source, String message, CountDownLatch latch) {
        super(source);
        this.message = message;
        this.latch = latch;
    }
    
    public String getMessage() {
        return message;
    }
    
    public CountDownLatch getLatch() {
        return latch;
    }
}

/**
 * 自定义事件监听器
 */
@Component
class CustomEventListener {
    
    @org.springframework.context.event.EventListener
    public void handleCustomEvent(CustomEvent event) {
        System.out.println("CustomEventListener: Received event - " + event.getMessage());
    }
}

/**
 * 字符串事件监听器
 */
@Component
class StringEventListener {
    
    @org.springframework.context.event.EventListener
    public void handleStringEvent(String message) {
        System.out.println("StringEventListener: Received string event - " + message);
    }
}

/**
 * 异步事件监听器
 */
@Component
class AsyncEventListener {
    
    @org.springframework.context.event.EventListener
    @Async
    public void handleAsyncEvent(AsyncEvent event) {
        System.out.println("AsyncEventListener: Received event - " + event.getMessage());
        System.out.println("AsyncEventListener: Thread - " + Thread.currentThread().getName());
        
        // 模拟耗时操作
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        System.out.println("AsyncEventListener: Processing completed");
        event.getLatch().countDown();
    }
}

/**
 * 顺序监听器1
 */
@Component
@Order(Ordered.HIGHEST_PRECEDENCE)
class FirstOrderEventListener {
    
    @org.springframework.context.event.EventListener
    public void handleOrderEvent(OrderEvent event) {
        System.out.println("FirstOrderEventListener: Received event - " + event.getMessage());
    }
}

/**
 * 顺序监听器2
 */
@Component
@Order(Ordered.LOWEST_PRECEDENCE)
class SecondOrderEventListener {
    
    @org.springframework.context.event.EventListener
    public void handleOrderEvent(OrderEvent event) {
        System.out.println("SecondOrderEventListener: Received event - " + event.getMessage());
    }
}

/**
 * 条件事件监听器
 */
@Component
class ConditionalEventListener {
    
    @org.springframework.context.event.EventListener(condition = "#event.message == 'important'")
    public void handleImportantEvent(CustomEvent event) {
        System.out.println("ConditionalEventListener: Received important event - " + event.getMessage());
    }
}

/**
 * 多事件监听器
 */
@Component
class MultiEventListener {
    
    @org.springframework.context.event.EventListener({CustomEvent.class, OrderEvent.class})
    public void handleMultipleEvents(ApplicationEvent event) {
        if (event instanceof CustomEvent) {
            System.out.println("MultiEventListener: Received CustomEvent - " + ((CustomEvent) event).getMessage());
        } else if (event instanceof OrderEvent) {
            System.out.println("MultiEventListener: Received OrderEvent - " + ((OrderEvent) event).getMessage());
        }
    }
}

/**
 * 标准事件监听器
 */
@Component
class StandardEventListener {
    
    @org.springframework.context.event.EventListener
    public void handleContextRefreshedEvent(org.springframework.context.event.ContextRefreshedEvent event) {
        System.out.println("StandardEventListener: Context refreshed");
    }
    
    @org.springframework.context.event.EventListener
    public void handleContextClosedEvent(org.springframework.context.event.ContextClosedEvent event) {
        System.out.println("StandardEventListener: Context closed");
    }
}
