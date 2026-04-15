package com.example.elasticsearch.installation;

import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.*;

public class InstallationDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch安装配置示例 ===");

        try {
            directoryStructureDemo();
            configFileDemo();
            startStopDemo();
            healthCheckDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void directoryStructureDemo() {
        System.out.println("\n--- 1. 目录结构演示 ---");

        System.out.println("Elasticsearch目录结构:");
        System.out.println("  elasticsearch/");
        System.out.println("  ├── bin/              # 可执行文件");
        System.out.println("  │   ├── elasticsearch");
        System.out.println("  │   ├── elasticsearch.bat");
        System.out.println("  │   ├── elasticsearch-plugin");
        System.out.println("  │   └── elasticsearch-plugin.bat");
        System.out.println("  ├── config/           # 配置文件");
        System.out.println("  │   ├── elasticsearch.yml");
        System.out.println("  │   ├── jvm.options");
        System.out.println("  │   └── log4j2.properties");
        System.out.println("  ├── lib/              # 库文件");
        System.out.println("  ├── modules/          # 模块");
        System.out.println("  ├── plugins/          # 插件");
        System.out.println("  ├── data/             # 数据目录（默认）");
        System.out.println("  └── logs/             # 日志目录（默认）");
    }

    private static void configFileDemo() {
        System.out.println("\n--- 2. 配置文件演示 ---");

        System.out.println("elasticsearch.yml 基本配置:");
        String elasticsearchYml = "cluster.name: my-application\n" +
                "node.name: node-1\n" +
                "node.master: true\n" +
                "node.data: true\n" +
                "network.host: 0.0.0.0\n" +
                "http.port: 9200\n" +
                "transport.port: 9300\n" +
                "discovery.seed_hosts: [\"127.0.0.1\"]\n" +
                "cluster.initial_master_nodes: [\"node-1\"]\n" +
                "path.data: /path/to/data\n" +
                "path.logs: /path/to/logs\n" +
                "http.cors.enabled: true\n" +
                "http.cors.allow-origin: \"*\"";
        System.out.println(elasticsearchYml);

        System.out.println("\njvm.options 内存配置:");
        String jvmOptions = "-Xms2g\n" +
                "-Xmx2g\n" +
                "-XX:+UseConcMarkSweepGC\n" +
                "-XX:CMSInitiatingOccupancyFraction=75\n" +
                "-XX:+UseCMSInitiatingOccupancyOnly\n" +
                "-XX:+HeapDumpOnOutOfMemoryError\n" +
                "-XX:HeapDumpPath=data\n" +
                "-XX:ErrorFile=logs/hs_err_pid%p.log";
        System.out.println(jvmOptions);
    }

    private static void startStopDemo() {
        System.out.println("\n--- 3. 启动停止演示 ---");

        System.out.println("Linux/Mac 启动命令:");
        System.out.println("  ./bin/elasticsearch");
        System.out.println("  ./bin/elasticsearch -d  # 后台启动");
        System.out.println();

        System.out.println("Windows 启动命令:");
        System.out.println("  bin\\elasticsearch.bat");
        System.out.println();

        System.out.println("停止服务:");
        System.out.println("  # 找到进程ID");
        System.out.println("  jps | grep Elasticsearch");
        System.out.println("  # 或");
        System.out.println("  ps aux | grep elasticsearch");
        System.out.println("  # 然后kill进程");
        System.out.println("  kill <pid>");
        System.out.println();

        System.out.println("使用systemd管理:");
        System.out.println("  sudo systemctl start elasticsearch");
        System.out.println("  sudo systemctl stop elasticsearch");
        System.out.println("  sudo systemctl restart elasticsearch");
        System.out.println("  sudo systemctl status elasticsearch");
        System.out.println("  sudo systemctl enable elasticsearch");
    }

    private static void healthCheckDemo() {
        System.out.println("\n--- 4. 健康检查演示 ---");

        System.out.println("检查Elasticsearch是否运行:");
        System.out.println("  curl http://localhost:9200");
        System.out.println();

        System.out.println("预期响应:");
        String response = "{\n" +
                "  \"name\": \"node-1\",\n" +
                "  \"cluster_name\": \"my-application\",\n" +
                "  \"cluster_uuid\": \"abc123...\",\n" +
                "  \"version\": {\n" +
                "    \"number\": \"8.12.0\",\n" +
                "    \"build_flavor\": \"default\",\n" +
                "    \"build_type\": \"zip\",\n" +
                "    \"build_hash\": \"...\",\n" +
                "    \"build_date\": \"2024-01-01T00:00:00.000Z\",\n" +
                "    \"build_snapshot\": false,\n" +
                "    \"lucene_version\": \"9.8.0\",\n" +
                "    \"minimum_wire_compatibility_version\": \"7.17.0\",\n" +
                "    \"minimum_index_compatibility_version\": \"7.0.0\"\n" +
                "  },\n" +
                "  \"tagline\": \"You Know, for Search\"\n" +
                "}";
        System.out.println(response);

        System.out.println("\n集群健康检查:");
        System.out.println("  curl http://localhost:9200/_cluster/health");
        System.out.println();

        System.out.println("健康状态:");
        System.out.println("  green: 所有主分片和副分片都正常");
        System.out.println("  yellow: 所有主分片正常，部分副分片异常");
        System.out.println("  red: 部分主分片异常");

        System.out.println("\n查看节点信息:");
        System.out.println("  curl http://localhost:9200/_cat/nodes?v");

        System.out.println("\n查看索引列表:");
        System.out.println("  curl http://localhost:9200/_cat/indices?v");

        System.out.println("\n查看集群状态:");
        System.out.println("  curl http://localhost:9200/_cluster/state");
    }
}
