package com.example.rabbitmq.ack;

import com.rabbitmq.client.*;

public class AckDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RabbitMQ确认机制示例 ===");

        try {
            manualAckDemo();
            nackDemo();
            deadLetterDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void manualAckDemo() throws Exception {
        System.out.println("\n--- 1. 手动确认 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        
        String QUEUE_NAME = "ack_queue";
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
        
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
            channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
            System.out.println(" [x] Acknowledged");
        };
        
        boolean autoAck = false;
        channel.basicConsume(QUEUE_NAME, autoAck, deliverCallback, consumerTag -> { });
    }

    private static void nackDemo() throws Exception {
        System.out.println("\n--- 2. Nack ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        
        String QUEUE_NAME = "nack_queue";
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
        
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
            boolean requeue = true;
            channel.basicNack(delivery.getEnvelope().getDeliveryTag(), false, requeue);
            System.out.println(" [x] Nacked, requeued");
        };
        
        boolean autoAck = false;
        channel.basicConsume(QUEUE_NAME, autoAck, deliverCallback, consumerTag -> { });
    }

    private static void deadLetterDemo() throws Exception {
        System.out.println("\n--- 3. 死信队列 ---");
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            
            String DLX_EXCHANGE = "dlx_exchange";
            String DLX_QUEUE = "dlx_queue";
            String QUEUE_NAME = "with_dlx_queue";
            
            channel.exchangeDeclare(DLX_EXCHANGE, "direct");
            channel.queueDeclare(DLX_QUEUE, false, false, false, null);
            channel.queueBind(DLX_QUEUE, DLX_EXCHANGE, "");
            
            java.util.Map<String, Object> args = new java.util.HashMap<>();
            args.put("x-dead-letter-exchange", DLX_EXCHANGE);
            args.put("x-dead-letter-routing-key", "");
            channel.queueDeclare(QUEUE_NAME, false, false, false, args);
            
            System.out.println("Queue with DLX declared");
        }
    }
}
