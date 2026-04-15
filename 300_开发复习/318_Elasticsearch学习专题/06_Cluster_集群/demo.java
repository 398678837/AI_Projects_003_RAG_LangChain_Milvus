package com.example.elasticsearch.cluster;

import java.util.*;

public class ClusterDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch集群示例 ===");

        try {
            nodeTypesDemo();
            shardReplicaDemo();
            clusterDiscoveryDemo();
            clusterManagementDemo();
            highAvailabilityDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void nodeTypesDemo() {
        System.out.println("\n--- 1. 节点类型演示 ---");

        System.out.println("Master节点配置:");
        String masterConfig = "node.master: true\n" +
                "node.data: false\n" +
                "node.ingest: false";
        System.out.println(masterConfig);

        System.out.println("\nData节点配置:");
        String dataConfig = "node.master: false\n" +
                "node.data: true\n" +
                "node.ingest: false";
        System.out.println(dataConfig);

        System.out.println("\nIngest节点配置:");
        String ingestConfig = "node.master: false\n" +
                "node.data: false\n" +
                "node.ingest: true";
        System.out.println(ingestConfig);

        System.out.println("\nCoordinating节点配置:");
        String coordinatingConfig = "node.master: false\n" +
                "node.data: false\n" +
                "node.ingest: false";
        System.out.println(coordinatingConfig);

        System.out.println("\n混合节点配置（开发环境）:");
        String hybridConfig = "node.master: true\n" +
                "node.data: true\n" +
                "node.ingest: true";
        System.out.println(hybridConfig);
    }

    private static void shardReplicaDemo() {
        System.out.println("\n--- 2. 分片和副本演示 ---");

        System.out.println("创建索引时指定分片和副本:");
        String createIndex = "PUT /products\n" +
                "{\n" +
                "  \"settings\": {\n" +
                "    \"number_of_shards\": 3,\n" +
                "    \"number_of_replicas\": 2\n" +
                "  }\n" +
                "}";
        System.out.println(createIndex);

        System.out.println("\n分片分配示例（3节点集群）:");
        System.out.println("  节点1: [P0, R1, R2]");
        System.out.println("  节点2: [P1, R0, R2]");
        System.out.println("  节点3: [P2, R0, R1]");
        System.out.println("  (P=主分片, R=副分片)");

        System.out.println("\n动态调整副本数:");
        String updateReplicas = "PUT /products/_settings\n" +
                "{\n" +
                "  \"index\": {\n" +
                "    \"number_of_replicas\": 1\n" +
                "  }\n" +
                "}";
        System.out.println(updateReplicas);

        System.out.println("\n查看分片信息:");
        System.out.println("  GET /_cat/shards?v");
        System.out.println("  GET /products/_shard_stores");
    }

    private static void clusterDiscoveryDemo() {
        System.out.println("\n--- 3. 集群发现演示 ---");

        System.out.println("单播发现配置:");
        String unicastConfig = "discovery.seed_hosts:\n" +
                "  - \"192.168.1.10:9300\"\n" +
                "  - \"192.168.1.11:9300\"\n" +
                "  - \"192.168.1.12:9300\"\n" +
                "\n" +
                "cluster.initial_master_nodes:\n" +
                "  - \"node-1\"\n" +
                "  - \"node-2\"\n" +
                "  - \"node-3\"";
        System.out.println(unicastConfig);

        System.out.println("\n集群配置示例（3节点）:");
        System.out.println("节点1 elasticsearch.yml:");
        String node1Config = "cluster.name: my-cluster\n" +
                "node.name: node-1\n" +
                "node.master: true\n" +
                "node.data: true\n" +
                "network.host: 192.168.1.10\n" +
                "discovery.seed_hosts: [\"192.168.1.10\", \"192.168.1.11\", \"192.168.1.12\"]\n" +
                "cluster.initial_master_nodes: [\"node-1\", \"node-2\", \"node-3\"]";
        System.out.println(node1Config);

        System.out.println("\n节点2 elasticsearch.yml:");
        String node2Config = "cluster.name: my-cluster\n" +
                "node.name: node-2\n" +
                "node.master: true\n" +
                "node.data: true\n" +
                "network.host: 192.168.1.11\n" +
                "discovery.seed_hosts: [\"192.168.1.10\", \"192.168.1.11\", \"192.168.1.12\"]\n" +
                "cluster.initial_master_nodes: [\"node-1\", \"node-2\", \"node-3\"]";
        System.out.println(node2Config);

        System.out.println("\n节点3 elasticsearch.yml:");
        String node3Config = "cluster.name: my-cluster\n" +
                "node.name: node-3\n" +
                "node.master: true\n" +
                "node.data: true\n" +
                "network.host: 192.168.1.12\n" +
                "discovery.seed_hosts: [\"192.168.1.10\", \"192.168.1.11\", \"192.168.1.12\"]\n" +
                "cluster.initial_master_nodes: [\"node-1\", \"node-2\", \"node-3\"]";
        System.out.println(node3Config);
    }

    private static void clusterManagementDemo() {
        System.out.println("\n--- 4. 集群管理演示 ---");

        System.out.println("集群健康检查:");
        System.out.println("  GET /_cluster/health");
        System.out.println("  GET /_cluster/health?level=indices");
        System.out.println("  GET /_cluster/health?level=shards");

        System.out.println("\n健康状态说明:");
        System.out.println("  green: 所有主分片和副分片都正常");
        System.out.println("  yellow: 所有主分片正常，部分副分片异常");
        System.out.println("  red: 部分主分片异常");

        System.out.println("\n查看节点信息:");
        System.out.println("  GET /_cat/nodes?v");
        System.out.println("  GET /_nodes");
        System.out.println("  GET /_nodes/stats");

        System.out.println("\n查看集群状态:");
        System.out.println("  GET /_cluster/state");

        System.out.println("\n查看索引:");
        System.out.println("  GET /_cat/indices?v");

        System.out.println("\n查看分片:");
        System.out.println("  GET /_cat/shards?v");

        System.out.println("\n集群设置:");
        String clusterSettings = "PUT /_cluster/settings\n" +
                "{\n" +
                "  \"persistent\": {\n" +
                "    \"indices.recovery.max_bytes_per_sec\": \"50mb\"\n" +
                "  },\n" +
                "  \"transient\": {\n" +
                "    \"indices.recovery.max_bytes_per_sec\": \"100mb\"\n" +
                "  }\n" +
                "}";
        System.out.println(clusterSettings);
    }

    private static void highAvailabilityDemo() {
        System.out.println("\n--- 5. 高可用演示 ---");

        System.out.println("节点故障场景:");
        System.out.println("  1. 节点3故障");
        System.out.println("  2. 集群检测到节点3离线");
        System.out.println("  3. 节点3上的P2主分片丢失");
        System.out.println("  4. 节点1和2上的R2副本提升为新的P2主分片");
        System.out.println("  5. 在其他节点上创建新的R2副本");
        System.out.println("  6. 集群恢复green状态");

        System.out.println("\n分片分配策略:");
        System.out.println("  - 主分片和副本不在同一节点");
        System.out.println("  - 副本分散在不同节点");
        System.out.println("  - 负载均衡");
        System.out.println("  - 节点离开时自动重新分配");

        System.out.println("\n分片分配设置:");
        String allocationSettings = "PUT /_cluster/settings\n" +
                "{\n" +
                "  \"persistent\": {\n" +
                "    \"cluster.routing.allocation.enable\": \"all\",\n" +
                "    \"cluster.routing.allocation.node_concurrent_recoveries\": 2,\n" +
                "    \"cluster.routing.allocation.cluster_concurrent_rebalance\": 2\n" +
                "  }\n" +
                "}";
        System.out.println(allocationSettings);

        System.out.println("\n禁用分片分配（滚动升级）:");
        String disableAllocation = "PUT /_cluster/settings\n" +
                "{\n" +
                "  \"persistent\": {\n" +
                "    \"cluster.routing.allocation.enable\": \"primaries\"\n" +
                "  }\n" +
                "}";
        System.out.println(disableAllocation);
    }
}
