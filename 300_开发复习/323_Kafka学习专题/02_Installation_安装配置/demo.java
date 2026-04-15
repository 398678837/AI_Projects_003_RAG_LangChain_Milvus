package com.example.kafka.installation;

import java.util.*;

public class InstallationDemo {

    public static void main(String[] args) {
        System.out.println("=== Kafka安装配置示例 ===");

        try {
            directoryStructureDemo();
            configFileDemo();
            startStopDemo();
            healthCheckDemo();
            basicConfigDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void directoryStructureDemo() {
        System.out.println("\n--- 1. 目录结构 ---");

        System.out.println("Kafka目录结构:");
        System.out.println("  kafka/");
        System.out.println("  ├── bin/              # 可执行文件");
        System.out.println("  │   ├── kafka-server-start.sh");
        System.out.println("  │   ├── kafka-server-stop.sh");
        System.out.println("  │   ├── zookeeper-server-start.sh");
        System.out.println("  │   ├── kafka-topics.sh");
        System.out.println("  │   ├── kafka-console-producer.sh");
        System.out.println("  │   └── kafka-console-consumer.sh");
        System.out.println("  ├── config/           # 配置文件");
        System.out.println("  │   ├── server.properties");
        System.out.println("  │   ├── zookeeper.properties");
        System.out.println("  │   ├── producer.properties");
        System.out.println("  │   └── consumer.properties");
        System.out.println("  ├── libs/             # 库文件");
        System.out.println("  ├── logs/             # 日志目录");
        System.out.println("  └── data/             # 数据目录");
    }

    private static void configFileDemo() {
        System.out.println("\n--- 2. 配置文件 ---");

        System.out.println("server.properties:");
        String serverProps = "broker.id=0\n" +
                "listeners=PLAINTEXT://:9092\n" +
                "num.network.threads=3\n" +
                "num.io.threads=8\n" +
                "socket.send.buffer.bytes=102400\n" +
                "socket.receive.buffer.bytes=102400\n" +
                "socket.request.max.bytes=104857600\n" +
                "log.dirs=/tmp/kafka-logs\n" +
                "num.partitions=1\n" +
                "num.recovery.threads.per.data.dir=1\n" +
                "offsets.topic.replication.factor=1\n" +
                "transaction.state.log.replication.factor=1\n" +
                "transaction.state.log.min.isr=1\n" +
                "log.retention.hours=168\n" +
                "log.segment.bytes=1073741824\n" +
                "log.retention.check.interval.ms=300000\n" +
                "zookeeper.connect=localhost:2181\n" +
                "zookeeper.connection.timeout.ms=18000";
        System.out.println(serverProps);

        System.out.println("\nzookeeper.properties:");
        String zkProps = "dataDir=/tmp/zookeeper\n" +
                "clientPort=2181\n" +
                "maxClientCnxns=0";
        System.out.println(zkProps);
    }

    private static void startStopDemo() {
        System.out.println("\n--- 3. 启动停止 ---");

        System.out.println("启动ZooKeeper:");
        System.out.println("  bin/zookeeper-server-start.sh config/zookeeper.properties");

        System.out.println("\n启动Kafka:");
        System.out.println("  bin/kafka-server-start.sh config/server.properties");

        System.out.println("\n停止Kafka:");
        System.out.println("  bin/kafka-server-stop.sh");

        System.out.println("\n停止ZooKeeper:");
        System.out.println("  bin/zookeeper-server-stop.sh");
    }

    private static void healthCheckDemo() {
        System.out.println("\n--- 4. 健康检查 ---");

        System.out.println("创建Topic:");
        System.out.println("  bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1");

        System.out.println("\n查看Topic列表:");
        System.out.println("  bin/kafka-topics.sh --list --bootstrap-server localhost:9092");

        System.out.println("\n发送消息:");
        System.out.println("  bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092");

        System.out.println("\n消费消息:");
        System.out.println("  bin/kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092");
    }

    private static void basicConfigDemo() {
        System.out.println("\n--- 5. 基本配置 ---");

        System.out.println("Broker配置:");
        System.out.println("  broker.id: Broker唯一标识");
        System.out.println("  listeners: 监听地址");
        System.out.println("  log.dirs: 日志目录");
        System.out.println("  zookeeper.connect: ZooKeeper连接");

        System.out.println("\nTopic配置:");
        System.out.println("  num.partitions: 默认分区数");
        System.out.println("  default.replication.factor: 默认副本数");

        System.out.println("\n日志配置:");
        System.out.println("  log.retention.hours: 日志保留时间");
        System.out.println("  log.segment.bytes: 日志分段大小");
    }
}
