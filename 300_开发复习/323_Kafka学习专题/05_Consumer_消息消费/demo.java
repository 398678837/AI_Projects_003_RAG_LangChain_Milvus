package com.example.kafka.consumer;

import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.TopicPartition;
import java.util.*;

public class ConsumerDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka Consumer示例 ===");

        try {
            autoCommitDemo();
            manualCommitDemo();
            subscribeDemo();
            configDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void autoCommitDemo() {
        System.out.println("\n--- 1. 自动提交 ---");
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "test-group");
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        Consumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("test-topic"));
        
        try {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("offset = %d, key = %s, value = %s%n",
                            record.offset(), record.key(), record.value());
                }
            }
        } finally {
            consumer.close();
        }
    }

    private static void manualCommitDemo() {
        System.out.println("\n--- 2. 手动提交 ---");
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "test-group");
        props.put("enable.auto.commit", "false");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        Consumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("test-topic"));
        
        try {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("offset = %d, key = %s, value = %s%n",
                            record.offset(), record.key(), record.value());
                }
                consumer.commitSync();
            }
        } finally {
            consumer.close();
        }
    }

    private static void subscribeDemo() {
        System.out.println("\n--- 3. 订阅 ---");
        System.out.println("订阅主题:");
        System.out.println("  consumer.subscribe(Arrays.asList(\"topic1\", \"topic2\"));");
        System.out.println();
        System.out.println("正则订阅:");
        System.out.println("  consumer.subscribe(Pattern.compile(\"test-.*\"));");
        System.out.println();
        System.out.println("指定分区:");
        System.out.println("  TopicPartition partition = new TopicPartition(\"topic\", 0);");
        System.out.println("  consumer.assign(Arrays.asList(partition));");
    }

    private static void configDemo() {
        System.out.println("\n--- 4. 配置 ---");
        System.out.println("auto.offset.reset:");
        System.out.println("  earliest: 从最早开始");
        System.out.println("  latest: 从最新开始");
        System.out.println();
        System.out.println("max.poll.records:");
        System.out.println("  每次拉取最大记录数");
    }
}
