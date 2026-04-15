package com.example.rabbitmq.exchange;

import com.rabbitmq.client.*;

public class ExchangeDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RabbitMQ交换机示例 ===");

        try {
            directExchangeDemo();
            topicExchangeDemo();
            fanoutExchangeDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void directExchangeDemo() throws Exception {
        System.out.println("\n--- 1. Direct交换机 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "direct_logs";
            channel.exchangeDeclare(EXCHANGE_NAME, "direct");
            
            String severity = "info";
            String message = "This is an info message";
            channel.basicPublish(EXCHANGE_NAME, severity, null, message.getBytes("UTF-8"));
            System.out.println(" [x] Sent '" + severity + "':'" + message + "'");
        }
    }

    private static void topicExchangeDemo() throws Exception {
        System.out.println("\n--- 2. Topic交换机 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "topic_logs";
            channel.exchangeDeclare(EXCHANGE_NAME, "topic");
            
            String routingKey = "kern.critical";
            String message = "A critical kernel error";
            channel.basicPublish(EXCHANGE_NAME, routingKey, null, message.getBytes("UTF-8"));
            System.out.println(" [x] Sent '" + routingKey + "':'" + message + "'");
        }
    }

    private static void fanoutExchangeDemo() throws Exception {
        System.out.println("\n--- 3. Fanout交换机 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String EXCHANGE_NAME = "logs";
            channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
            
            String message = "Hello World!";
            channel.basicPublish(EXCHANGE_NAME, "", null, message.getBytes("UTF-8"));
            System.out.println(" [x] Sent '" + message + "'");
        }
    }
}
