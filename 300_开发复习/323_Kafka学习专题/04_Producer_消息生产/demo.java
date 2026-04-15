package com.example.kafka.producer;

import org.apache.kafka.clients.producer.*;
import java.util.Properties;

public class ProducerDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka Producer示例 ===");

        try {
            syncSendDemo();
            asyncSendDemo();
            configDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void syncSendDemo() {
        System.out.println("\n--- 1. 同步发送 ---");
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<>(props);
        
        ProducerRecord<String, String> record = new ProducerRecord<>("test-topic", "key", "value");
        try {
            RecordMetadata metadata = producer.send(record).get();
            System.out.println("Sent to partition " + metadata.partition() + ", offset " + metadata.offset());
        } catch (Exception e) {
            e.printStackTrace();
        }
        producer.close();
    }

    private static void asyncSendDemo() {
        System.out.println("\n--- 2. 异步发送 ---");
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<>(props);
        
        ProducerRecord<String, String> record = new ProducerRecord<>("test-topic", "key", "value");
        producer.send(record, new Callback() {
            @Override
            public void onCompletion(RecordMetadata metadata, Exception exception) {
                if (exception != null) {
                    exception.printStackTrace();
                } else {
                    System.out.println("Sent to partition " + metadata.partition() + ", offset " + metadata.offset());
                }
            }
        });
        producer.close();
    }

    private static void configDemo() {
        System.out.println("\n--- 3. 配置 ---");
        System.out.println("acks配置:");
        System.out.println("  acks=0: 不等待确认");
        System.out.println("  acks=1: 等待Leader确认");
        System.out.println("  acks=all: 等待所有副本确认");
        System.out.println();
        System.out.println("retries配置:");
        System.out.println("  retries=3: 重试3次");
        System.out.println();
        System.out.println("batch.size配置:");
        System.out.println("  batch.size=16384: 16KB");
    }
}
