package com.example.rocketmq.installation;

import java.util.*;

public class InstallationDemo {

    public static void main(String[] args) {
        System.out.println("=== RocketMQ安装配置示例 ===");

        try {
            directoryStructureDemo();
            configFileDemo();
            startStopDemo();
            healthCheckDemo();
            clusterConfigDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void directoryStructureDemo() {
        System.out.println("\n--- 1. 目录结构演示 ---");

        System.out.println("RocketMQ目录结构:");
        System.out.println("  rocketmq/");
        System.out.println("  ├── bin/              # 可执行文件");
        System.out.println("  │   ├── mqnamesrv");
        System.out.println("  │   ├── mqnamesrv.cmd");
        System.out.println("  │   ├── mqbroker");
        System.out.println("  │   ├── mqbroker.cmd");
        System.out.println("  │   ├── tools.sh");
        System.out.println("  │   └── tools.cmd");
        System.out.println("  ├── conf/             # 配置文件");
        System.out.println("  │   ├── broker.conf");
        System.out.println("  │   ├── namesrv.conf");
        System.out.println("  │   └── logback_*.xml");
        System.out.println("  ├── lib/              # 库文件");
        System.out.println("  ├── store/            # 存储目录（默认）");
        System.out.println("  │   ├── commitlog/");
        System.out.println("  │   ├── consumequeue/");
        System.out.println("  │   └── index/");
        System.out.println("  └── logs/             # 日志目录（默认）");
    }

    private static void configFileDemo() {
        System.out.println("\n--- 2. 配置文件演示 ---");

        System.out.println("namesrv.conf 基本配置:");
        String namesrvConf = "listenPort=9876\n" +
                "kvConfigPath=/path/to/kvConfig.json\n" +
                "serverWorkerThreads=8\n" +
                "serverCallbackExecutorThreads=8\n" +
                "serverSelectorThreads=3";
        System.out.println(namesrvConf);

        System.out.println("\nbroker.conf 基本配置:");
        String brokerConf = "brokerClusterName=DefaultCluster\n" +
                "brokerName=broker-a\n" +
                "brokerId=0\n" +
                "deleteWhen=04\n" +
                "fileReservedTime=48\n" +
                "brokerRole=ASYNC_MASTER\n" +
                "flushDiskType=ASYNC_FLUSH\n" +
                "namesrvAddr=127.0.0.1:9876\n" +
                "listenPort=10911\n" +
                "storePathRootDir=/path/to/store\n" +
                "storePathCommitLog=/path/to/store/commitlog\n" +
                "autoCreateTopicEnable=true\n" +
                "autoCreateSubscriptionGroup=true";
        System.out.println(brokerConf);

        System.out.println("\nJVM参数配置（runserver.sh）:");
        String jvmOptions = "JAVA_OPT=\"${JAVA_OPT} -server -Xms4g -Xmx4g -Xmn2g -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=320m\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=70\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -XX:+CMSParallelRemarkEnabled -XX:SoftRefLRUPolicyMSPerMB=0 -XX:+CMSClassUnloadingEnabled\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -XX:-OmitStackTraceInFastThrow\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -verbose:gc -Xloggc:/dev/shm/rmq_srv_gc.log -XX:+PrintGCDetails\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -XX:-UseLargePages\"\n" +
                "JAVA_OPT=\"${JAVA_OPT} -Djava.ext.dirs=${JAVA_HOME}/jre/lib/ext:${BASE_DIR}/lib\"";
        System.out.println(jvmOptions);
    }

    private static void startStopDemo() {
        System.out.println("\n--- 3. 启动停止演示 ---");

        System.out.println("Linux/Mac 启动NameServer:");
        System.out.println("  nohup sh bin/mqnamesrv &");
        System.out.println("  tail -f ~/logs/rocketmqlogs/namesrv.log");

        System.out.println("\nLinux/Mac 启动Broker:");
        System.out.println("  nohup sh bin/mqbroker -n localhost:9876 &");
        System.out.println("  tail -f ~/logs/rocketmqlogs/broker.log");

        System.out.println("\nWindows 启动NameServer:");
        System.out.println("  start bin/mqnamesrv.cmd");

        System.out.println("\nWindows 启动Broker:");
        System.out.println("  start bin/mqbroker.cmd -n localhost:9876");

        System.out.println("\n停止服务:");
        System.out.println("  sh bin/mqshutdown namesrv");
        System.out.println("  sh bin/mqshutdown broker");

        System.out.println("\nWindows停止:");
        System.out.println("  bin/mqshutdown.cmd namesrv");
        System.out.println("  bin/mqshutdown.cmd broker");
    }

    private static void healthCheckDemo() {
        System.out.println("\n--- 4. 健康检查演示 ---");

        System.out.println("检查NameServer:");
        System.out.println("  # 查看端口是否监听");
        System.out.println("  netstat -an | grep 9876");
        System.out.println();
        System.out.println("  # 查看进程");
        System.out.println("  jps | grep NamesrvStartup");

        System.out.println("\n检查Broker:");
        System.out.println("  # 查看端口是否监听");
        System.out.println("  netstat -an | grep 10911");
        System.out.println();
        System.out.println("  # 查看进程");
        System.out.println("  jps | grep BrokerStartup");

        System.out.println("\n使用管理工具检查:");
        System.out.println("  # 查看Topic列表");
        System.out.println("  sh bin/mqadmin topicList -n localhost:9876");
        System.out.println();
        System.out.println("  # 查看集群状态");
        System.out.println("  sh bin/mqadmin clusterList -n localhost:9876");
        System.out.println();
        System.out.println("  # 查看Broker状态");
        System.out.println("  sh bin/mqadmin brokerStatus -n localhost:9876 -b broker-a");

        System.out.println("\n查看日志:");
        System.out.println("  # NameServer日志");
        System.out.println("  tail -f ~/logs/rocketmqlogs/namesrv.log");
        System.out.println();
        System.out.println("  # Broker日志");
        System.out.println("  tail -f ~/logs/rocketmqlogs/broker.log");
    }

    private static void clusterConfigDemo() {
        System.out.println("\n--- 5. 集群配置演示 ---");

        System.out.println("多NameServer配置:");
        System.out.println("  # Broker配置");
        System.out.println("  namesrvAddr=192.168.1.10:9876;192.168.1.11:9876;192.168.1.12:9876");
        System.out.println();
        System.out.println("  # 生产者配置");
        System.out.println("  producer.setNamesrvAddr(\"192.168.1.10:9876;192.168.1.11:9876;192.168.1.12:9876\");");

        System.out.println("\nBroker主从配置 - Master:");
        String masterConfig = "brokerClusterName=MyCluster\n" +
                "brokerName=broker-a\n" +
                "brokerId=0\n" +
                "brokerRole=SYNC_MASTER\n" +
                "flushDiskType=ASYNC_FLUSH\n" +
                "namesrvAddr=192.168.1.10:9876;192.168.1.11:9876\n" +
                "listenPort=10911\n" +
                "haListenPort=10912";
        System.out.println(masterConfig);

        System.out.println("\nBroker主从配置 - Slave:");
        String slaveConfig = "brokerClusterName=MyCluster\n" +
                "brokerName=broker-a\n" +
                "brokerId=1\n" +
                "brokerRole=SLAVE\n" +
                "namesrvAddr=192.168.1.10:9876;192.168.1.11:9876\n" +
                "listenPort=10911\n" +
                "haListenPort=10912";
        System.out.println(slaveConfig);

        System.out.println("\nBroker角色:");
        System.out.println("  - ASYNC_MASTER: 异步复制Master");
        System.out.println("  - SYNC_MASTER: 同步复制Master");
        System.out.println("  - SLAVE: 从节点");
        System.out.println();
        System.out.println("刷盘策略:");
        System.out.println("  - ASYNC_FLUSH: 异步刷盘");
        System.out.println("  - SYNC_FLUSH: 同步刷盘");

        System.out.println("\n集群架构:");
        System.out.println("  NameServer1  NameServer2  NameServer3");
        System.out.println("       │            │            │");
        System.out.println("       └────────────┼────────────┘");
        System.out.println("                    │");
        System.out.println("       ┌────────────┼────────────┐");
        System.out.println("       │            │            │");
        System.out.println("  Broker-a-M  Broker-b-M  Broker-c-M");
        System.out.println("       │            │            │");
        System.out.println("  Broker-a-S  Broker-b-S  Broker-c-S");
        System.out.println("  (M=Master, S=Slave)");
    }
}
