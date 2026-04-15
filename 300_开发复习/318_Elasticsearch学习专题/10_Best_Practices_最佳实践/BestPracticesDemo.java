package com.example.elasticsearch.bestpractices;

import java.util.*;

public class BestPracticesDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch最佳实践示例 ===");

        try {
            indexDesignDemo();
            queryBestPracticesDemo();
            clusterBestPracticesDemo();
            securityBestPracticesDemo();
            operationsBestPracticesDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void indexDesignDemo() {
        System.out.println("\n--- 1. 索引设计最佳实践 ---");

        System.out.println("按时间分索引（日志场景）:");
        String timeBasedIndex = "PUT /logs-2024.01.01\n" +
                "{\n" +
                "  \"settings\": {\n" +
                "    \"number_of_shards\": 3,\n" +
                "    \"number_of_replicas\": 1\n" +
                "  }\n" +
                "}";
        System.out.println(timeBasedIndex);

        System.out.println("\n使用索引模板:");
        String indexTemplate = "PUT /_index_template/logs_template\n" +
                "{\n" +
                "  \"index_patterns\": [\"logs-*\"],\n" +
                "  \"template\": {\n" +
                "    \"settings\": {\n" +
                "      \"number_of_shards\": 3,\n" +
                "      \"number_of_replicas\": 1,\n" +
                "      \"refresh_interval\": \"30s\"\n" +
                "    },\n" +
                "    \"mappings\": {\n" +
                "      \"properties\": {\n" +
                "        \"@timestamp\": { \"type\": \"date\" },\n" +
                "        \"message\": { \"type\": \"text\" },\n" +
                "        \"level\": { \"type\": \"keyword\" },\n" +
                "        \"service\": { \"type\": \"keyword\" }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(indexTemplate);

        System.out.println("\n使用索引别名:");
        String indexAlias = "POST /_aliases\n" +
                "{\n" +
                "  \"actions\": [\n" +
                "    { \"add\": { \"index\": \"logs-2024.01.01\", \"alias\": \"logs_write\" } },\n" +
                "    { \"add\": { \"index\": \"logs-2024.01.01\", \"alias\": \"logs_search\" } },\n" +
                "    { \"add\": { \"index\": \"logs-2024.01.02\", \"alias\": \"logs_search\" } }\n" +
                "  ]\n" +
                "}";
        System.out.println(indexAlias);

        System.out.println("\n索引生命周期管理:");
        String ilmPolicy = "PUT /_ilm/policy/logs_policy\n" +
                "{\n" +
                "  \"policy\": {\n" +
                "    \"phases\": {\n" +
                "      \"hot\": {\n" +
                "        \"actions\": {\n" +
                "          \"rollover\": {\n" +
                "            \"max_size\": \"50gb\",\n" +
                "            \"max_age\": \"7d\"\n" +
                "          }\n" +
                "        }\n" +
                "      },\n" +
                "      \"warm\": {\n" +
                "        \"min_age\": \"30d\",\n" +
                "        \"actions\": {\n" +
                "          \"allocate\": { \"number_of_replicas\": 1 },\n" +
                "          \"forcemerge\": { \"max_num_segments\": 1 }\n" +
                "        }\n" +
                "      },\n" +
                "      \"cold\": {\n" +
                "        \"min_age\": \"90d\",\n" +
                "        \"actions\": {\n" +
                "          \"allocate\": { \"number_of_replicas\": 0 }\n" +
                "        }\n" +
                "      },\n" +
                "      \"delete\": {\n" +
                "        \"min_age\": \"365d\",\n" +
                "        \"actions\": { \"delete\": {} }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(ilmPolicy);
    }

    private static void queryBestPracticesDemo() {
        System.out.println("\n--- 2. 查询最佳实践 ---");

        System.out.println("使用filter而不是query进行过滤:");
        String filterQuery = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"bool\": {\n" +
                "      \"must\": [\n" +
                "        { \"match\": { \"name\": \"iPhone\" } }\n" +
                "      ],\n" +
                "      \"filter\": [\n" +
                "        { \"range\": { \"price\": { \"gte\": 5000 } } },\n" +
                "        { \"term\": { \"category\": \"手机\" } }\n" +
                "      ]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(filterQuery);

        System.out.println("\n避免使用通配符开头:");
        System.out.println("  # 不好:");
        System.out.println("  { \"wildcard\": { \"name\": \"*phone\" } }");
        System.out.println("  # 好:");
        System.out.println("  { \"wildcard\": { \"name\": \"phone*\" } }");

        System.out.println("\n避免使用脚本查询:");
        System.out.println("  # 尽量避免:");
        System.out.println("  { \"script\": { \"source\": \"doc['price'].value > 5000\" } }");
        System.out.println("  # 改为:");
        System.out.println("  { \"range\": { \"price\": { \"gt\": 5000 } } }");

        System.out.println("\n使用bool查询组合多个条件:");
        String boolQuery = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"bool\": {\n" +
                "      \"must\": [\n" +
                "        { \"match\": { \"name\": \"iPhone\" } }\n" +
                "      ],\n" +
                "      \"filter\": [\n" +
                "        { \"term\": { \"category\": \"手机\" } }\n" +
                "      ],\n" +
                "      \"should\": [\n" +
                "        { \"match\": { \"description\": \"新品\" } }\n" +
                "      ],\n" +
                "      \"must_not\": [\n" +
                "        { \"term\": { \"status\": \"下架\" } }\n" +
                "      ]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(boolQuery);

        System.out.println("\n限制返回的字段:");
        String sourceFilter = "GET /products/_search\n" +
                "{\n" +
                "  \"_source\": [\"name\", \"price\", \"category\"],\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(sourceFilter);
    }

    private static void clusterBestPracticesDemo() {
        System.out.println("\n--- 3. 集群管理最佳实践 ---");

        System.out.println("节点角色分离（生产环境）:");
        System.out.println("  - 3个Master节点");
        System.out.println("  - 多个Data节点");
        System.out.println("  - 可选的Ingest节点");
        System.out.println("  - 可选的Coordinating节点");
        System.out.println("  - 可选的ML节点");

        System.out.println("\n分片数量规划:");
        System.out.println("  - 每个分片大小: 20-40GB");
        System.out.println("  - 分片数 <= 节点数 × 10");
        System.out.println("  - 避免过多小分片");
        System.out.println("  - 避免过大的分片");

        System.out.println("\n副本配置:");
        System.out.println("  - 生产环境: 至少1个副本");
        System.out.println("  - 高可用: 2个副本");
        System.out.println("  - 读多写少: 可以增加副本");

        System.out.println("\n集群设置（elasticsearch.yml）:");
        String clusterSettings = "cluster.name: my-production-cluster\n" +
                "node.name: node-1\n" +
                "node.master: true\n" +
                "node.data: true\n" +
                "network.host: 0.0.0.0\n" +
                "discovery.seed_hosts: [\"192.168.1.10\", \"192.168.1.11\", \"192.168.1.12\"]\n" +
                "cluster.initial_master_nodes: [\"node-1\", \"node-2\", \"node-3\"]\n" +
                "bootstrap.memory_lock: true\n" +
                "action.destructive_requires_name: true";
        System.out.println(clusterSettings);
    }

    private static void securityBestPracticesDemo() {
        System.out.println("\n--- 4. 安全最佳实践 ---");

        System.out.println("启用安全:");
        System.out.println("  xpack.security.enabled: true");
        System.out.println("  xpack.security.transport.ssl.enabled: true");
        System.out.println("  xpack.security.http.ssl.enabled: true");

        System.out.println("\n设置密码:");
        System.out.println("  bin/elasticsearch-setup-passwords auto");
        System.out.println("  bin/elasticsearch-setup-passwords interactive");

        System.out.println("\n角色和权限:");
        String role = "PUT /_security/role/read_only\n" +
                "{\n" +
                "  \"cluster\": [\"monitor\"],\n" +
                "  \"indices\": [\n" +
                "    {\n" +
                "      \"names\": [\"products\", \"orders\"],\n" +
                "      \"privileges\": [\"read\"]\n" +
                "    }\n" +
                "  ]\n" +
                "}";
        System.out.println(role);

        System.out.println("\n创建用户:");
        String user = "PUT /_security/user/john\n" +
                "{\n" +
                "  \"password\": \"secure-password-123\",\n" +
                "  \"roles\": [\"read_only\"]\n" +
                "}";
        System.out.println(user);

        System.out.println("\n网络安全:");
        System.out.println("  - 绑定到内网IP");
        System.out.println("  - 使用防火墙");
        System.out.println("  - 启用TLS/SSL");
        System.out.println("  - 使用VPN");
    }

    private static void operationsBestPracticesDemo() {
        System.out.println("\n--- 5. 运维最佳实践 ---");

        System.out.println("快照和恢复:");
        String snapshotRepo = "PUT /_snapshot/backup_repo\n" +
                "{\n" +
                "  \"type\": \"fs\",\n" +
                "  \"settings\": {\n" +
                "    \"location\": \"/mnt/elasticsearch/backup\"\n" +
                "  }\n" +
                "}";
        System.out.println(snapshotRepo);

        System.out.println("\n创建快照:");
        String createSnapshot = "PUT /_snapshot/backup_repo/snapshot_2024_01_01?wait_for_completion=true\n" +
                "{\n" +
                "  \"indices\": \"products,orders\",\n" +
                "  \"ignore_unavailable\": true,\n" +
                "  \"include_global_state\": false\n" +
                "}";
        System.out.println(createSnapshot);

        System.out.println("\n恢复快照:");
        String restoreSnapshot = "POST /_snapshot/backup_repo/snapshot_2024_01_01/_restore\n" +
                "{\n" +
                "  \"indices\": \"products\",\n" +
                "  \"ignore_unavailable\": true\n" +
                "}";
        System.out.println(restoreSnapshot);

        System.out.println("\n监控和告警:");
        System.out.println("  - 集群健康状态");
        System.out.println("  - JVM堆内存");
        System.out.println("  - CPU使用率");
        System.out.println("  - 磁盘空间");
        System.out.println("  - 搜索延迟");
        System.out.println("  - 索引延迟");
        System.out.println("  - 节点状态");

        System.out.println("\n常见问题排查:");
        System.out.println("  - 集群Yellow: 检查副本分配");
        System.out.println("  - 集群Red: 检查主分片");
        System.out.println("  - OOM: 调整JVM内存");
        System.out.println("  - 高CPU: 检查慢查询");
        System.out.println("  - 高磁盘: 清理旧索引");
    }
}
