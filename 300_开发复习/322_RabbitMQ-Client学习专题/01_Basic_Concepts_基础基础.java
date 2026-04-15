package com.example.rabbitmq.basic;

import java.util.*;

public class BasicConceptsDemo {

    public static void main(String[] args) {
        System.out.println("=== RabbitMQ基础概念示例 ===");

        try {
            rabbitMQOverviewDemo();
            coreArchitectureDemo();
            amqpProtocolDemo();
            messageModelsDemo();
            coreConceptsDemo();
            applicationScenariosDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void rabbitMQOverviewDemo() {
        System.out.println("\n--- 1. RabbitMQ概述 ---");

        System.out.println("RabbitMQ是什么?");
        System.out.println("  - 开源的消息中间件");
        System.out.println("  - 基于AMQP协议实现");
        System.out.println("  - 使用Erlang语言开发");
        System.out.println("  - 高可靠性");
        System.out.println("  - 灵活的路由");

        System.out.println("\nRabbitMQ的特点:");
        System.out.println("  - 高可靠性");
        System.out.println("  - 灵活的路由");
        System.out.println("  - 消息集群");
        System.out.println("  - 高可用性");
        System.out.println("  - 多种协议");
        System.out.println("  - 管理界面");
        System.out.println("  - 跟踪");
        System.out.println("  - 插件系统");

        System.out.println("\nRabbitMQ vs 其他MQ:");
        System.out.println("  - vs Kafka: 路由更灵活，适合复杂路由场景");
        System.out.println("  - vs RocketMQ: 生态更成熟，插件丰富");
        System.out.println("  - vs ActiveMQ: 性能更好，功能更强大");
    }

    private static void coreArchitectureDemo() {
        System.out.println("\n--- 2. 核心架构 ---");

        System.out.println("RabbitMQ核心组件:");
        System.out.println();

        System.out.println("1. Producer（生产者）:");
        System.out.println("   - 发送消息的应用");
        System.out.println("   - 创建消息");
        System.out.println("   - 发送到Exchange");
        System.out.println();

        System.out.println("2. Consumer（消费者）:");
        System.out.println("   - 接收消息的应用");
        System.out.println("   - 订阅Queue");
        System.out.println("   - 处理消息");
        System.out.println();

        System.out.println("3. Broker（消息代理）:");
        System.out.println("   - RabbitMQ服务器");
        System.out.println("   - 接收和分发消息");
        System.out.println("   - 存储消息");
        System.out.println("   - 管理连接");
        System.out.println();

        System.out.println("4. Exchange（交换机）:");
        System.out.println("   - 接收Producer的消息");
        System.out.println("   - 根据规则路由到Queue");
        System.out.println("   - 多种类型");
        System.out.println();

        System.out.println("5. Queue（队列）:");
        System.out.println("   - 存储消息");
        System.out.println("   - 等待Consumer消费");
        System.out.println("   - FIFO");
        System.out.println();

        System.out.println("6. Binding（绑定）:");
        System.out.println("   - Exchange和Queue的关联");
        System.out.println("   - 定义路由规则");
        System.out.println("   - Routing Key");
        System.out.println();

        System.out.println("7. Virtual Host（虚拟主机）:");
        System.out.println("   - 逻辑隔离");
        System.out.println("   - 独立的Exchange、Queue、Binding");
        System.out.println("   - 权限控制");

        System.out.println("\n架构关系图:");
        System.out.println("  Producer ──> Exchange ──Binding──> Queue ──> Consumer");
        System.out.println("                     │");
        System.out.println("                  Broker");
    }

    private static void amqpProtocolDemo() {
        System.out.println("\n--- 3. AMQP协议 ---");

        System.out.println("AMQP是什么?");
        System.out.println("  - Advanced Message Queuing Protocol");
        System.out.println("  - 高级消息队列协议");
        System.out.println("  - 开放的二进制协议");
        System.out.println("  - 用于消息中间件");

        System.out.println("\nAMQP的特点:");
        System.out.println("  - 二进制协议");
        System.out.println("  - 平台无关");
        System.out.println("  - 语言无关");
        System.out.println("  - 可靠的消息传递");
        System.out.println("  - 灵活的路由");
        System.out.println("  - 安全认证");

        System.out.println("\nAMQP模型:");
        System.out.println("  - Producer -> Exchange -> Queue -> Consumer");
        System.out.println("  - Exchange: 消息路由器");
        System.out.println("  - Queue: 消息存储");
        System.out.println("  - Binding: 路由规则");

        System.out.println("\nAMQP命令:");
        System.out.println("  - Connection: 建立连接");
        System.out.println("  - Channel: 建立通道");
        System.out.println("  - Exchange.Declare: 声明交换机");
        System.out.println("  - Queue.Declare: 声明队列");
        System.out.println("  - Queue.Bind: 绑定队列");
        System.out.println("  - Basic.Publish: 发布消息");
        System.out.println("  - Basic.Consume: 消费消息");
        System.out.println("  - Basic.Ack: 确认消息");
    }

    private static void messageModelsDemo() {
        System.out.println("\n--- 4. 消息模型 ---");

        System.out.println("1. 简单队列（Simple Queue）:");
        System.out.println("   - 一个Producer");
        System.out.println("   - 一个Queue");
        System.out.println("   - 一个Consumer");
        System.out.println("   Producer -> Queue -> Consumer");

        System.out.println("\n2. 工作队列（Work Queue）:");
        System.out.println("   - 一个Producer");
        System.out.println("   - 一个Queue");
        System.out.println("   - 多个Consumer");
        System.out.println("   - 负载均衡");
        System.out.println("   Producer -> Queue ─┬─> Consumer1");
        System.out.println("                     ├─> Consumer2");
        System.out.println("                     └─> Consumer3");

        System.out.println("\n3. 发布订阅（Publish/Subscribe）:");
        System.out.println("   - Fanout Exchange");
        System.out.println("   - 消息广播到所有Queue");
        System.out.println("   Producer -> Fanout Exchange ─┬─> Queue1 -> Consumer1");
        System.out.println("                                 ├─> Queue2 -> Consumer2");
        System.out.println("                                 └─> Queue3 -> Consumer3");

        System.out.println("\n4. 路由（Routing）:");
        System.out.println("   - Direct Exchange");
        System.out.println("   - 根据Routing Key精确匹配");
        System.out.println("   Producer -> Direct Exchange ──routingKey=error──> Queue1 -> Consumer1");
        System.out.println("                              └─routingKey=info──> Queue2 -> Consumer2");

        System.out.println("\n5. 主题（Topics）:");
        System.out.println("   - Topic Exchange");
        System.out.println("   - 通配符匹配");
        System.out.println("   - *: 匹配一个单词");
        System.out.println("   - #: 匹配零个或多个单词");
        System.out.println("   Producer -> Topic Exchange ──routingKey=user.created──> Queue1 -> Consumer1");
        System.out.println("                             └─routingKey=user.*──> Queue2 -> Consumer2");

        System.out.println("\n6. RPC（远程过程调用）:");
        System.out.println("   - 请求/响应模式");
        System.out.println("   - 使用Reply To和Correlation ID");
        System.out.println("   Client -> RPC Queue -> Server");
        System.out.println("   Client <-- Reply Queue <-- Server");
    }

    private static void coreConceptsDemo() {
        System.out.println("\n--- 5. 核心概念 ---");

        System.out.println("Exchange（交换机）:");
        System.out.println("  - 接收Producer的消息");
        System.out.println("  - 路由到Queue");
        System.out.println();
        System.out.println("  Exchange类型:");
        System.out.println("  - Direct: 精确匹配Routing Key");
        System.out.println("  - Topic: 通配符匹配");
        System.out.println("  - Fanout: 广播到所有Queue");
        System.out.println("  - Headers: 根据Header匹配");

        System.out.println("\nQueue（队列）:");
        System.out.println("  - 存储消息");
        System.out.println("  - FIFO");
        System.out.println("  - 可持久化");
        System.out.println("  - 可排他");
        System.out.println("  - 可自动删除");

        System.out.println("\nBinding（绑定）:");
        System.out.println("  - Exchange和Queue的关联");
        System.out.println("  - Routing Key");
        System.out.println("  - 路由规则");

        System.out.println("\nMessage（消息）:");
        System.out.println("  - Header: 元数据");
        System.out.println("  - Body: 消息内容");
        System.out.println("  - Properties: 属性");
    }

    private static void applicationScenariosDemo() {
        System.out.println("\n--- 6. 应用场景 ---");

        System.out.println("1. 异步处理:");
        System.out.println("   - 用户注册 -> MQ -> 发送邮件");
        System.out.println("   - 订单创建 -> MQ -> 扣减库存");
        System.out.println("   - 提高响应速度");
        System.out.println("   - 系统解耦");

        System.out.println("\n2. 流量削峰:");
        System.out.println("   - 秒杀请求 -> MQ -> 订单处理");
        System.out.println("   - 大促流量 -> MQ -> 业务系统");
        System.out.println("   - 保护后端系统");
        System.out.println("   - 平滑流量");

        System.out.println("\n3. 日志收集:");
        System.out.println("   - 应用日志 -> MQ -> 日志分析");
        System.out.println("   - 访问日志 -> MQ -> 监控系统");
        System.out.println("   - 统一收集");
        System.out.println("   - 实时分析");

        System.out.println("\n4. 系统解耦:");
        System.out.println("   - 系统A -> MQ -> 系统B");
        System.out.println("   - 系统A -> MQ -> 系统C");
        System.out.println("   - 降低耦合");
        System.out.println("   - 提高可扩展性");

        System.out.println("\n5. 分布式事务:");
        System.out.println("   - 最终一致性");
        System.out.println("   - 可靠消息");
        System.out.println("   - 补偿机制");
        System.out.println("   - 消息确认");

        System.out.println("\n使用RabbitMQ的知名项目:");
        System.out.println("  - OpenStack");
        System.out.println("  - Spring Cloud");
        System.out.println("  - Netflix");
        System.out.println("  - 很多互联网公司");
    }
}
