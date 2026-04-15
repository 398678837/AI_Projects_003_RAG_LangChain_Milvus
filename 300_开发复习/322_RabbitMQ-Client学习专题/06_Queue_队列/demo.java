package com.example.rabbitmq.queue;

import com.rabbitmq.client.*;
import java.util.HashMap;
import java.util.Map;

public class QueueDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RabbitMQ队列示例 ===");

        try {
            basicQueueDemo();
            durableQueueDemo();
            ttlQueueDemo();
            maxLengthQueueDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void basicQueueDemo() throws Exception {
        System.out.println("\n--- 1. 基本队列 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "basic_queue";
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            System.out.println("Queue declared: " + QUEUE_NAME);
        }
    }

    private static void durableQueueDemo() throws Exception {
        System.out.println("\n--- 2. 持久化队列 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "durable_queue";
            boolean durable = true;
            channel.queueDeclare(QUEUE_NAME, durable, false, false, null);
            System.out.println("Durable queue declared: " + QUEUE_NAME);
            
            String message = "Persistent message";
            AMQP.BasicProperties props = MessageProperties.PERSISTENT_TEXT_PLAIN;
            channel.basicPublish("", QUEUE_NAME, props, message.getBytes());
            System.out.println("Persistent message sent");
        }
    }

    private static void ttlQueueDemo() throws Exception {
        System.out.println("\n--- 3. TTL队列 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "ttl_queue";
            Map<String, Object> args = new HashMap<>();
            args.put("x-message-ttl", 60000);
            channel.queueDeclare(QUEUE_NAME, false, false, false, args);
            System.out.println("TTL queue declared: " + QUEUE_NAME);
        }
    }

    private static void maxLengthQueueDemo() throws Exception {
        System.out.println("\n--- 4. 最大长度队列 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "max_length_queue";
            Map<String, Object> args = new HashMap<>();
            args.put("x-max-length", 10);
            channel.queueDeclare(QUEUE_NAME, false, false, false, args);
            System.out.println("Max length queue declared: " + QUEUE_NAME);
        }
    }
}
