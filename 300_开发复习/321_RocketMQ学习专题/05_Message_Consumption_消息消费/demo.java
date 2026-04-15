package com.example.rocketmq.consumption;

import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
import org.apache.rocketmq.common.message.MessageExt;

import java.util.List;

public class MessageConsumptionDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RocketMQ消息消费示例 ===");

        try {
            pushConsumerDemo();
            pullConsumerDemo();
            consumptionModeDemo();
            retryMechanismDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void pushConsumerDemo() throws Exception {
        System.out.println("\n--- 1. Push消费 ---");
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("push_consumer_group");
        consumer.setNamesrvAddr("localhost:9876");
        consumer.subscribe("TopicTest", "*");
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            @Override
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs, ConsumeConcurrentlyContext context) {
                System.out.println("收到消息: " + msgs);
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
        consumer.start();
        System.out.println("Push Consumer启动成功");
    }

    private static void pullConsumerDemo() {
        System.out.println("\n--- 2. Pull消费 ---");
        System.out.println("使用DefaultMQPullConsumer手动拉取消息");
        System.out.println("更灵活的消费控制");
    }

    private static void consumptionModeDemo() {
        System.out.println("\n--- 3. 消费模式 ---");
        System.out.println("集群消费: MessageModel.CLUSTERING");
        System.out.println("  - 一条消息只被一个Consumer消费");
        System.out.println("  - 负载均衡");
        System.out.println();
        System.out.println("广播消费: MessageModel.BROADCASTING");
        System.out.println("  - 一条消息被所有Consumer消费");
        System.out.println("  - 通知场景");
    }

    private static void retryMechanismDemo() {
        System.out.println("\n--- 4. 重试机制 ---");
        System.out.println("消费重试:");
        System.out.println("  - 返回RECONSUME_LATER重试");
        System.out.println("  - 重试间隔递增");
        System.out.println("  - 最大重试次数");
        System.out.println();
        System.out.println("死信队列:");
        System.out.println("  - 超过重试次数");
        System.out.println("  - 进入死信队列");
        System.out.println("  - Topic: %DLQ%consumerGroup");
    }
}
