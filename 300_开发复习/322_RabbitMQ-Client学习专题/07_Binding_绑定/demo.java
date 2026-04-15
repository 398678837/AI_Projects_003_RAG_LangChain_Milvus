package com.example.rabbitmq.binding;

import com.rabbitmq.client.*;
import java.util.HashMap;
import java.util.Map;

public class BindingDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RabbitMQ绑定示例 ===");

        try {
            directBindingDemo();
            topicBindingDemo();
            fanoutBindingDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void directBindingDemo() throws Exception {
        System.out.println("\n--- 1. Direct绑定 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "direct_exchange";
            String QUEUE_NAME = "direct_queue";
            
            channel.exchangeDeclare(EXCHANGE_NAME, "direct");
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            
            String routingKey = "error";
            channel.queueBind(QUEUE_NAME, EXCHANGE_NAME, routingKey);
            System.out.println("Queue bound with routing key: " + routingKey);
        }
    }

    private static void topicBindingDemo() throws Exception {
        System.out.println("\n--- 2. Topic绑定 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "topic_exchange";
            String QUEUE_NAME = "topic_queue";
            
            channel.exchangeDeclare(EXCHANGE_NAME, "topic");
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            
            String routingKey = "kern.*";
            channel.queueBind(QUEUE_NAME, EXCHANGE_NAME, routingKey);
            System.out.println("Queue bound with topic routing key: " + routingKey);
        }
    }

    private static void fanoutBindingDemo() throws Exception {
        System.out.println("\n--- 3. Fanout绑定 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "fanout_exchange";
            String QUEUE_NAME = "fanout_queue";
            
            channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            
            channel.queueBind(QUEUE_NAME, EXCHANGE_NAME, "");
            System.out.println("Queue bound to fanout exchange");
        }
    }
}
