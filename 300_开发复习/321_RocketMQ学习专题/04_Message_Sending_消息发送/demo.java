package com.example.rocketmq.sending;

import org.apache.rocketmq.client.producer.*;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;

public class MessageSendingDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RocketMQ消息发送示例 ===");

        try {
            syncSendDemo();
            asyncSendDemo();
            onewaySendDemo();
            messageConfigDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void syncSendDemo() throws Exception {
        System.out.println("\n--- 1. 同步发送 ---");
        DefaultMQProducer producer = new DefaultMQProducer("sync_producer_group");
        producer.setNamesrvAddr("localhost:9876");
        producer.start();

        Message msg = new Message("TopicTest", "TagA", "Hello RocketMQ".getBytes(RemotingHelper.DEFAULT_CHARSET));
        SendResult sendResult = producer.send(msg);
        System.out.println("发送结果: " + sendResult);
        producer.shutdown();
    }

    private static void asyncSendDemo() throws Exception {
        System.out.println("\n--- 2. 异步发送 ---");
        DefaultMQProducer producer = new DefaultMQProducer("async_producer_group");
        producer.setNamesrvAddr("localhost:9876");
        producer.start();

        Message msg = new Message("TopicTest", "TagA", "Hello RocketMQ Async".getBytes(RemotingHelper.DEFAULT_CHARSET));
        producer.send(msg, new SendCallback() {
            @Override
            public void onSuccess(SendResult sendResult) {
                System.out.println("发送成功: " + sendResult);
            }
            @Override
            public void onException(Throwable e) {
                System.out.println("发送失败: " + e);
            }
        });

        Thread.sleep(10000);
        producer.shutdown();
    }

    private static void onewaySendDemo() throws Exception {
        System.out.println("\n--- 3. Oneway发送 ---");
        DefaultMQProducer producer = new DefaultMQProducer("oneway_producer_group");
        producer.setNamesrvAddr("localhost:9876");
        producer.start();

        Message msg = new Message("TopicTest", "TagA", "Hello RocketMQ Oneway".getBytes(RemotingHelper.DEFAULT_CHARSET));
        producer.sendOneway(msg);
        System.out.println("Oneway发送完成");
        producer.shutdown();
    }

    private static void messageConfigDemo() {
        System.out.println("\n--- 4. 消息发送配置 ---");
        System.out.println("重试次数: producer.setRetryTimesWhenSendFailed(3);");
        System.out.println("超时时间: producer.setSendMsgTimeout(3000);");
        System.out.println("异步重试: producer.setRetryTimesWhenSendAsyncFailed(2);");
    }
}
