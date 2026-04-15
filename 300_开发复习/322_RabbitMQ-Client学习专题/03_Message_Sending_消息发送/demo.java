package com.example.rabbitmq.sending;

import com.rabbitmq.client.*;

public class MessageSendingDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RabbitMQ消息发送示例 ===");

        try {
            basicSendDemo();
            publishConfirmDemo();
            messagePropertiesDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void basicSendDemo() throws Exception {
        System.out.println("\n--- 1. 基本发送 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "hello";
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            String message = "Hello World!";
            channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
            System.out.println(" [x] Sent '" + message + "'");
        }
    }

    private static void publishConfirmDemo() throws Exception {
        System.out.println("\n--- 2. 发布确认 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            channel.confirmSelect();
            String QUEUE_NAME = "confirm_queue";
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            String message = "Confirm message";
            channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
            
            if (channel.waitForConfirms()) {
                System.out.println(" [x] Message confirmed");
            } else {
                System.out.println(" [x] Message not confirmed");
            }
        }
    }

    private static void messagePropertiesDemo() throws Exception {
        System.out.println("\n--- 3. 消息属性 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String QUEUE_NAME = "props_queue";
            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            
            AMQP.BasicProperties props = new AMQP.BasicProperties.Builder()
                    .contentType("text/plain")
                    .deliveryMode(2)
                    .priority(1)
                    .userId("guest")
                    .build();
            
            String message = "Message with properties";
            channel.basicPublish("", QUEUE_NAME, props, message.getBytes());
            System.out.println(" [x] Sent message with properties");
        }
    }
}
