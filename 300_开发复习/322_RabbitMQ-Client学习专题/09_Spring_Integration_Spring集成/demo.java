package com.example.rabbitmq.spring;

public class SpringIntegrationDemo {

    public static void main(String[] args) {
        System.out.println("=== RabbitMQ Spring集成示例 ===");

        try {
            configDemo();
            rabbitTemplateDemo();
            rabbitListenerDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void configDemo() {
        System.out.println("\n--- 1. 配置示例 ---");
        System.out.println("application.properties:");
        System.out.println("  spring.rabbitmq.host=localhost");
        System.out.println("  spring.rabbitmq.port=5672");
        System.out.println("  spring.rabbitmq.username=guest");
        System.out.println("  spring.rabbitmq.password=guest");
    }

    private static void rabbitTemplateDemo() {
        System.out.println("\n--- 2. RabbitTemplate ---");
        System.out.println("发送消息:");
        System.out.println("  rabbitTemplate.convertAndSend(\"exchange\", \"routingKey\", message);");
        System.out.println();
        System.out.println("接收消息:");
        System.out.println("  Object message = rabbitTemplate.receiveAndConvert(\"queue\");");
    }

    private static void rabbitListenerDemo() {
        System.out.println("\n--- 3. @RabbitListener ---");
        System.out.println("@RabbitListener(queues = \"myQueue\")");
        System.out.println("public void handleMessage(String message) {");
        System.out.println("    System.out.println(\"Received: \" + message);");
        System.out.println("}");
    }
}
