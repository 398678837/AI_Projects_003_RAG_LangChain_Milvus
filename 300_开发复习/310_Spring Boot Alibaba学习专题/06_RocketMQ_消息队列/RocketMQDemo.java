import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class RocketMQDemo {
    public static void main(String[] args) {
        SpringApplication.run(RocketMQDemo.class, args);
    }
}

// 消息控制器
@RestController
@RequestMapping("/api/messages")
class MessageController {
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
    
    @GetMapping("/sync/{content}")
    public String sendSyncMessage(@PathVariable String content) {
        Message<String> message = MessageBuilder.withPayload(content).build();
        rocketMQTemplate.syncSend("test-topic", message);
        return "Sync message sent: " + content;
    }
    
    @GetMapping("/async/{content}")
    public String sendAsyncMessage(@PathVariable String content) {
        Message<String> message = MessageBuilder.withPayload(content).build();
        rocketMQTemplate.asyncSend("test-topic", message, (result, ex) -> {
            if (ex == null) {
                System.out.println("Async message sent successfully: " + result.getMsgId());
            } else {
                System.out.println("Async message sent failed: " + ex.getMessage());
            }
        });
        return "Async message sent: " + content;
    }
    
    @GetMapping("/oneway/{content}")
    public String sendOnewayMessage(@PathVariable String content) {
        Message<String> message = MessageBuilder.withPayload(content).build();
        rocketMQTemplate.sendOneWay("test-topic", message);
        return "Oneway message sent: " + content;
    }
    
    @GetMapping("/delay/{content}")
    public String sendDelayMessage(@PathVariable String content) {
        Message<String> message = MessageBuilder.withPayload(content).build();
        // 延迟级别：1s, 5s, 10s, 30s, 1m, 2m, 3m, 4m, 5m, 6m, 7m, 8m, 9m, 10m, 20m, 30m, 1h, 2h
        rocketMQTemplate.syncSend("test-topic", message, 3000, 3);
        return "Delay message sent: " + content;
    }
}

// 消息消费者
@RocketMQMessageListener(topic = "test-topic", consumerGroup = "test-consumer-group")
class TestConsumer implements RocketMQListener<String> {
    private final List<String> messages = new ArrayList<>();
    
    @Override
    public void onMessage(String message) {
        System.out.println("Received message: " + message);
        messages.add(message);
    }
    
    public List<String> getMessages() {
        return messages;
    }
}

// 消息实体类
class Message {
    private String id;
    private String content;
    
    public Message() {
    }
    
    public Message(String id, String content) {
        this.id = id;
        this.content = content;
    }
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    public String getContent() {
        return content;
    }
    
    public void setContent(String content) {
        this.content = content;
    }
    
    @Override
    public String toString() {
        return "Message{" +
                "id='" + id + '\'' +
                ", content='" + content + '\'' +
                '}';
    }
}