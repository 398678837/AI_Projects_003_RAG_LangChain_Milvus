package com.example.rocketmq.transaction;

import org.apache.rocketmq.client.producer.LocalTransactionState;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.client.producer.TransactionListener;
import org.apache.rocketmq.client.producer.TransactionMQProducer;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.remoting.common.RemotingHelper;

import java.util.concurrent.*;

public class TransactionMessageDemo {

    public static void main(String[] args) throws Exception {
        System.out.println("=== RocketMQ事务消息示例 ===");

        try {
            transactionProducerDemo();
            transactionListenerDemo();
            transactionStatusDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void transactionProducerDemo() throws Exception {
        System.out.println("\n--- 1. 事务消息生产者 ---");
        TransactionListener transactionListener = new TransactionListener() {
            @Override
            public LocalTransactionState executeLocalTransaction(Message msg, Object arg) {
                System.out.println("执行本地事务: " + new String(msg.getBody()));
                return LocalTransactionState.COMMIT_MESSAGE;
            }
            @Override
            public LocalTransactionState checkLocalTransaction(MessageExt msg) {
                System.out.println("检查本地事务: " + new String(msg.getBody()));
                return LocalTransactionState.COMMIT_MESSAGE;
            }
        };

        TransactionMQProducer producer = new TransactionMQProducer("tx_producer_group");
        producer.setNamesrvAddr("localhost:9876");
        ExecutorService executorService = new ThreadPoolExecutor(2, 5, 100, TimeUnit.SECONDS, new ArrayBlockingQueue<>(2000), r -> {
            Thread thread = new Thread(r);
            thread.setName("transaction-check-thread");
            return thread;
        });
        producer.setExecutorService(executorService);
        producer.setTransactionListener(transactionListener);
        producer.start();

        Message msg = new Message("TransactionTopic", "TagA", "Hello Transaction".getBytes(RemotingHelper.DEFAULT_CHARSET));
        SendResult sendResult = producer.sendMessageInTransaction(msg, null);
        System.out.println("事务消息发送结果: " + sendResult);

        Thread.sleep(10000);
        producer.shutdown();
    }

    private static void transactionListenerDemo() {
        System.out.println("\n--- 2. 事务监听器 ---");
        System.out.println("TransactionListener接口:");
        System.out.println("  - executeLocalTransaction: 执行本地事务");
        System.out.println("  - checkLocalTransaction: 检查本地事务");
    }

    private static void transactionStatusDemo() {
        System.out.println("\n--- 3. 事务状态 ---");
        System.out.println("LocalTransactionState.COMMIT_MESSAGE: 提交");
        System.out.println("LocalTransactionState.ROLLBACK_MESSAGE: 回滚");
        System.out.println("LocalTransactionState.UNKNOWN: 未知，等待回查");
    }
}
