package com.example.elasticsearch.performance;

import java.util.*;

public class PerformanceOptimizationDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch性能优化示例 ===");

        try {
            indexOptimizationDemo();
            searchOptimizationDemo();
            hardwareOptimizationDemo();
            clusterOptimizationDemo();
            monitoringDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void indexOptimizationDemo() {
        System.out.println("\n--- 1. 索引优化演示 ---");

        System.out.println("批量索引优化:");
        String bulkIndex = "PUT /logs/_bulk\n" +
                "{ \"index\": {}}\n" +
                "{ \"message\": \"log1\", \"timestamp\": \"2024-01-01T00:00:00\" }\n" +
                "{ \"index\": {}}\n" +
                "{ \"message\": \"log2\", \"timestamp\": \"2024-01-01T00:00:01\" }\n" +
                "{ \"index\": {}}\n" +
                "{ \"message\": \"log3\", \"timestamp\": \"2024-01-01T00:00:02\" }";
        System.out.println(bulkIndex);

        System.out.println("\n优化索引设置:");
        String indexSettings = "PUT /logs/_settings\n" +
                "{\n" +
                "  \"index\": {\n" +
                "    \"refresh_interval\": \"30s\",\n" +
                "    \"number_of_replicas\": 0,\n" +
                "    \"translog.durability\": \"async\",\n" +
                "    \"translog.sync_interval\": \"30s\"\n" +
                "  }\n" +
                "}";
        System.out.println(indexSettings);

        System.out.println("\n批量索引完成后恢复设置:");
        String restoreSettings = "PUT /logs/_settings\n" +
                "{\n" +
                "  \"index\": {\n" +
                "    \"refresh_interval\": \"1s\",\n" +
                "    \"number_of_replicas\": 1\n" +
                "  }\n" +
                "}";
        System.out.println(restoreSettings);

        System.out.println("\n禁用_source（只在不需要时）:");
        String disableSource = "PUT /logs\n" +
                "{\n" +
                "  \"mappings\": {\n" +
                "    \"_source\": { \"enabled\": false }\n" +
                "  }\n" +
                "}";
        System.out.println(disableSource);

        System.out.println("\n只索引需要的字段:");
        String indexOnly = "PUT /logs\n" +
                "{\n" +
                "  \"mappings\": {\n" +
                "    \"properties\": {\n" +
                "      \"message\": { \"type\": \"text\" },\n" +
                "      \"timestamp\": { \"type\": \"date\" },\n" +
                "      \"level\": { \"type\": \"keyword\" },\n" +
                "      \"ignore_field\": { \"type\": \"text\", \"index\": false }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(indexOnly);
    }

    private static void searchOptimizationDemo() {
        System.out.println("\n--- 2. 搜索优化演示 ---");

        System.out.println("使用过滤器:");
        String filterQuery = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"bool\": {\n" +
                "      \"must\": [\n" +
                "        { \"match\": { \"name\": \"iPhone\" } }\n" +
                "      ],\n" +
                "      \"filter\": [\n" +
                "        { \"range\": { \"price\": { \"gte\": 5000, \"lte\": 10000 } } },\n" +
                "        { \"term\": { \"category\": \"手机\" } }\n" +
                "      ]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(filterQuery);

        System.out.println("\n避免深度分页，使用search_after:");
        String searchAfter = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 10,\n" +
                "  \"search_after\": [7999.00, \"1\"],\n" +
                "  \"sort\": [\n" +
                "    { \"price\": \"asc\" },\n" +
                "    { \"_id\": \"asc\" }\n" +
                "  ],\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(searchAfter);

        System.out.println("\n使用scroll批量获取:");
        String scroll = "GET /products/_search?scroll=1m\n" +
                "{\n" +
                "  \"size\": 100,\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(scroll);

        System.out.println("\n继续scroll:");
        System.out.println("POST /_search/scroll\n" +
                "{\n" +
                "  \"scroll\": \"1m\",\n" +
                "  \"scroll_id\": \"DnF1ZXJ5VGhlbkZldGNo...\"\n" +
                "}");

        System.out.println("\n只返回需要的字段:");
        String sourceFilter = "GET /products/_search\n" +
                "{\n" +
                "  \"_source\": [\"name\", \"price\", \"category\"],\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(sourceFilter);

        System.out.println("\n禁用评分（constant_score）:");
        String constantScore = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"constant_score\": {\n" +
                "      \"filter\": {\n" +
                "        \"term\": { \"category\": \"手机\" }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(constantScore);
    }

    private static void hardwareOptimizationDemo() {
        System.out.println("\n--- 3. 硬件优化演示 ---");

        System.out.println("JVM内存设置（jvm.options）:");
        String jvmOptions = "-Xms4g\n" +
                "-Xmx4g\n" +
                "-XX:+UseG1GC\n" +
                "-XX:MaxGCPauseMillis=200\n" +
                "-XX:+HeapDumpOnOutOfMemoryError\n" +
                "-XX:HeapDumpPath=/var/log/elasticsearch";
        System.out.println(jvmOptions);

        System.out.println("\n系统配置（sysctl.conf）:");
        String sysctl = "vm.swappiness = 1\n" +
                "vm.max_map_count = 262144\n" +
                "net.core.somaxconn = 65535\n" +
                "net.core.netdev_max_backlog = 5000\n" +
                "net.ipv4.tcp_max_syn_backlog = 4096";
        System.out.println(sysctl);

        System.out.println("\n文件描述符限制（limits.conf）:");
        String limits = "elasticsearch soft nofile 65536\n" +
                "elasticsearch hard nofile 65536\n" +
                "elasticsearch soft nproc 4096\n" +
                "elasticsearch hard nproc 4096";
        System.out.println(limits);

        System.out.println("\n内存优化原则:");
        System.out.println("  - Xms和Xmx设置为相同值");
        System.out.println("  - 不超过32GB（避免指针压缩失效）");
        System.out.println("  - 预留一半内存给系统缓存");
        System.out.println("  - 监控GC和堆内存使用");
    }

    private static void clusterOptimizationDemo() {
        System.out.println("\n--- 4. 集群优化演示 ---");

        System.out.println("分片分配设置:");
        String allocationSettings = "PUT /_cluster/settings\n" +
                "{\n" +
                "  \"persistent\": {\n" +
                "    \"cluster.routing.allocation.node_concurrent_recoveries\": 2,\n" +
                "    \"cluster.routing.allocation.cluster_concurrent_rebalance\": 2,\n" +
                "    \"indices.recovery.max_bytes_per_sec\": \"50mb\"\n" +
                "  }\n" +
                "}";
        System.out.println(allocationSettings);

        System.out.println("\n线程池设置:");
        String threadPoolSettings = "PUT /_cluster/settings\n" +
                "{\n" +
                "  \"persistent\": {\n" +
                "    \"thread_pool.search.size\": 32,\n" +
                "    \"thread_pool.search.queue_size\": 1000,\n" +
                "    \"thread_pool.write.size\": 32,\n" +
                "    \"thread_pool.write.queue_size\": 1000\n" +
                "  }\n" +
                "}";
        System.out.println(threadPoolSettings);

        System.out.println("\n禁用swap:");
        System.out.println("  sudo swapoff -a");
        System.out.println("  # 或在elasticsearch.yml中设置:");
        System.out.println("  bootstrap.memory_lock: true");
    }

    private static void monitoringDemo() {
        System.out.println("\n--- 5. 监控演示 ---");

        System.out.println("集群健康:");
        System.out.println("  GET /_cluster/health");

        System.out.println("\n集群统计:");
        System.out.println("  GET /_cluster/stats");

        System.out.println("\n节点统计:");
        System.out.println("  GET /_nodes/stats");

        System.out.println("\n索引统计:");
        System.out.println("  GET /_stats");

        System.out.println("\n查看节点:");
        System.out.println("  GET /_cat/nodes?v");

        System.out.println("\n查看索引:");
        System.out.println("  GET /_cat/indices?v");

        System.out.println("\n查看分片:");
        System.out.println("  GET /_cat/shards?v");

        System.out.println("\n查看线程池:");
        System.out.println("  GET /_cat/thread_pool?v");

        System.out.println("\n慢查询日志配置:");
        String slowLog = "PUT /products/_settings\n" +
                "{\n" +
                "  \"index.search.slowlog.threshold.query.warn\": \"10s\",\n" +
                "  \"index.search.slowlog.threshold.query.info\": \"5s\",\n" +
                "  \"index.search.slowlog.threshold.query.debug\": \"2s\",\n" +
                "  \"index.search.slowlog.threshold.query.trace\": \"500ms\",\n" +
                "  \"index.search.slowlog.level\": \"info\"\n" +
                "}";
        System.out.println(slowLog);

        System.out.println("\n索引慢查询日志:");
        String indexSlowLog = "PUT /products/_settings\n" +
                "{\n" +
                "  \"index.indexing.slowlog.threshold.index.warn\": \"10s\",\n" +
                "  \"index.indexing.slowlog.threshold.index.info\": \"5s\",\n" +
                "  \"index.indexing.slowlog.threshold.index.debug\": \"2s\",\n" +
                "  \"index.indexing.slowlog.threshold.index.trace\": \"500ms\",\n" +
                "  \"index.indexing.slowlog.source\": 1000,\n" +
                "  \"index.indexing.slowlog.level\": \"info\"\n" +
                "}";
        System.out.println(indexSlowLog);
    }
}
