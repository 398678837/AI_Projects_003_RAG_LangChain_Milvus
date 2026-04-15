package com.example.rocketmq.order;

import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.MessageQueueSelector;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.common.message.MessageQueue;
import org.apache.rocketmq.remoting.common.RemotingHelper;

import java.util.List;

public class OrderMessageDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RocketMQ顺序消息示例 ===");

        try {
            partitionOrderDemo();
            globalOrderDemo();
            orderConsumerDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void partitionOrderDemo() throws Exception {
        System.out.println("\n--- 1. 分区有序 ---");
        DefaultMQProducer producer = new DefaultMQProducer("order_producer_group");
        producer.setNamesrvAddr("localhost:9876");
        producer.start();

        String[] orderIds = {"101", "102", "103", "101", "102", "103"};
        String[] steps = {"创建", "支付", "发货", "完成", "评价", "完成"};

        for (int i = 0; i < orderIds.length; i++) {
            Message msg = new Message("OrderTopic", "Order", orderIds[i], 
                    ("Order " + orderIds[i] + " " + steps[i]).getBytes(RemotingHelper.DEFAULT_CHARSET));
            SendResult sendResult = producer.send(msg, new MessageQueueSelector() {
                @Override
                public MessageQueue select(List<MessageQueue> mqs, Message msg, Object arg) {
                    int orderId = Integer.parseInt((String) arg);
                    int index = orderId % mqs.size();
                    return mqs.get(index);
                }
            }, orderIds[i]);
            System.out.println("发送结果: " + sendResult);
        }
        producer.shutdown();
    }

    private static void globalOrderDemo() {
        System.out.println("\n--- 2. 全局有序 ---");
        System.out.println("只有一个队列");
        System.out.println("所有消息顺序发送");
        System.out.println("性能较低");
    }

    private static void orderConsumerDemo() {
        System.out.println("\n--- 3. 顺序消费 ---");
        System.out.println("使用MessageListenerOrderly");
        System.out.println("顺序消费监听器");
        System.out.println("本地锁保证顺序");
    }
}
