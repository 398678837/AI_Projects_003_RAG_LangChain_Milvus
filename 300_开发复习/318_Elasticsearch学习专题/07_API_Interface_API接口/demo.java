package com.example.elasticsearch.api;

import java.util.*;

public class ApiInterfaceDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch API接口示例 ===");

        try {
            indexApiDemo();
            documentApiDemo();
            searchApiDemo();
            bulkApiDemo();
            clusterApiDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void indexApiDemo() {
        System.out.println("\n--- 1. 索引API演示 ---");

        System.out.println("创建索引:");
        String createIndex = "PUT /products\n" +
                "{\n" +
                "  \"settings\": {\n" +
                "    \"number_of_shards\": 3,\n" +
                "    \"number_of_replicas\": 1\n" +
                "  },\n" +
                "  \"mappings\": {\n" +
                "    \"properties\": {\n" +
                "      \"name\": { \"type\": \"text\" },\n" +
                "      \"price\": { \"type\": \"double\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(createIndex);

        System.out.println("\n获取索引信息:");
        System.out.println("  GET /products");

        System.out.println("\n检查索引是否存在:");
        System.out.println("  HEAD /products");

        System.out.println("\n删除索引:");
        System.out.println("  DELETE /products");

        System.out.println("\n打开索引:");
        System.out.println("  POST /products/_open");

        System.out.println("\n关闭索引:");
        System.out.println("  POST /products/_close");

        System.out.println("\n刷新索引:");
        System.out.println("  POST /products/_refresh");
    }

    private static void documentApiDemo() {
        System.out.println("\n--- 2. 文档API演示 ---");

        System.out.println("创建文档（自动生成ID）:");
        String createDoc = "POST /products/_doc\n" +
                "{\n" +
                "  \"name\": \"iPhone 15\",\n" +
                "  \"price\": 7999.00,\n" +
                "  \"category\": \"手机\"\n" +
                "}";
        System.out.println(createDoc);

        System.out.println("\n创建文档（指定ID）:");
        String createDocWithId = "PUT /products/_doc/1\n" +
                "{\n" +
                "  \"name\": \"MacBook Pro\",\n" +
                "  \"price\": 14999.00,\n" +
                "  \"category\": \"笔记本\"\n" +
                "}";
        System.out.println(createDocWithId);

        System.out.println("\n获取文档:");
        System.out.println("  GET /products/_doc/1");

        System.out.println("\n检查文档是否存在:");
        System.out.println("  HEAD /products/_doc/1");

        System.out.println("\n更新文档:");
        String updateDoc = "POST /products/_update/1\n" +
                "{\n" +
                "  \"doc\": {\n" +
                "    \"price\": 13999.00\n" +
                "  }\n" +
                "}";
        System.out.println(updateDoc);

        System.out.println("\nUpsert（更新或插入）:");
        String upsertDoc = "POST /products/_update/2\n" +
                "{\n" +
                "  \"doc\": {\n" +
                "    \"name\": \"iPad Pro\",\n" +
                "    \"price\": 6999.00,\n" +
                "    \"category\": \"平板\"\n" +
                "  },\n" +
                "  \"doc_as_upsert\": true\n" +
                "}";
        System.out.println(upsertDoc);

        System.out.println("\n删除文档:");
        System.out.println("  DELETE /products/_doc/1");

        System.out.println("\n批量获取文档:");
        String mget = "GET /_mget\n" +
                "{\n" +
                "  \"docs\": [\n" +
                "    { \"_index\": \"products\", \"_id\": \"1\" },\n" +
                "    { \"_index\": \"products\", \"_id\": \"2\" }\n" +
                "  ]\n" +
                "}";
        System.out.println(mget);
    }

    private static void searchApiDemo() {
        System.out.println("\n--- 3. 搜索API演示 ---");

        System.out.println("URI搜索:");
        System.out.println("  GET /products/_search?q=name:iPhone&sort=price:asc");

        System.out.println("\nRequest Body搜索:");
        String searchQuery = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match\": { \"name\": \"iPhone\" }\n" +
                "  },\n" +
                "  \"sort\": [\n" +
                "    { \"price\": { \"order\": \"asc\" } }\n" +
                "  ]\n" +
                "}";
        System.out.println(searchQuery);

        System.out.println("\n分页搜索:");
        String pagination = "GET /products/_search\n" +
                "{\n" +
                "  \"from\": 0,\n" +
                "  \"size\": 10,\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(pagination);

        System.out.println("\n返回指定字段:");
        String sourceFilter = "GET /products/_search\n" +
                "{\n" +
                "  \"_source\": [\"name\", \"price\"],\n" +
                "  \"query\": { \"match_all\": {} }\n" +
                "}";
        System.out.println(sourceFilter);

        System.out.println("\n高亮搜索:");
        String highlight = "GET /products/_search\n" +
                "{\n" +
                "  \"query\": { \"match\": { \"name\": \"iPhone\" } },\n" +
                "  \"highlight\": {\n" +
                "    \"fields\": { \"name\": {} }\n" +
                "  }\n" +
                "}";
        System.out.println(highlight);
    }

    private static void bulkApiDemo() {
        System.out.println("\n--- 4. 批量API演示 ---");

        System.out.println("批量操作（_bulk）:");
        String bulk = "POST /_bulk\n" +
                "{ \"index\": { \"_index\": \"products\", \"_id\": \"1\" } }\n" +
                "{ \"name\": \"iPhone 15\", \"price\": 7999.00 }\n" +
                "{ \"index\": { \"_index\": \"products\", \"_id\": \"2\" } }\n" +
                "{ \"name\": \"MacBook Pro\", \"price\": 14999.00 }\n" +
                "{ \"update\": { \"_index\": \"products\", \"_id\": \"1\" } }\n" +
                "{ \"doc\": { \"price\": 7599.00 } }\n" +
                "{ \"delete\": { \"_index\": \"products\", \"_id\": \"3\" } }";
        System.out.println(bulk);

        System.out.println("\n批量索引:");
        String bulkIndex = "POST /products/_bulk\n" +
                "{ \"index\": { \"_id\": \"1\" } }\n" +
                "{ \"name\": \"iPhone 15\", \"price\": 7999.00 }\n" +
                "{ \"index\": { \"_id\": \"2\" } }\n" +
                "{ \"name\": \"MacBook Pro\", \"price\": 14999.00 }\n" +
                "{ \"index\": { \"_id\": \"3\" } }\n" +
                "{ \"name\": \"iPad Pro\", \"price\": 6999.00 }";
        System.out.println(bulkIndex);

        System.out.println("\n批量更新:");
        String bulkUpdate = "POST /products/_bulk\n" +
                "{ \"update\": { \"_id\": \"1\" } }\n" +
                "{ \"doc\": { \"price\": 7599.00 } }\n" +
                "{ \"update\": { \"_id\": \"2\" } }\n" +
                "{ \"doc\": { \"price\": 13999.00 } }";
        System.out.println(bulkUpdate);

        System.out.println("\n批量删除:");
        String bulkDelete = "POST /products/_bulk\n" +
                "{ \"delete\": { \"_id\": \"1\" } }\n" +
                "{ \"delete\": { \"_id\": \"2\" } }\n" +
                "{ \"delete\": { \"_id\": \"3\" } }";
        System.out.println(bulkDelete);
    }

    private static void clusterApiDemo() {
        System.out.println("\n--- 5. 集群API演示 ---");

        System.out.println("集群健康:");
        System.out.println("  GET /_cluster/health");

        System.out.println("\n集群状态:");
        System.out.println("  GET /_cluster/state");

        System.out.println("\n节点信息:");
        System.out.println("  GET /_nodes");

        System.out.println("\n节点统计:");
        System.out.println("  GET /_nodes/stats");

        System.out.println("\n查看索引:");
        System.out.println("  GET /_cat/indices?v");

        System.out.println("\n查看节点:");
        System.out.println("  GET /_cat/nodes?v");

        System.out.println("\n查看分片:");
        System.out.println("  GET /_cat/shards?v");

        System.out.println("\n别名操作:");
        String aliases = "POST /_aliases\n" +
                "{\n" +
                "  \"actions\": [\n" +
                "    { \"add\": { \"index\": \"products_v1\", \"alias\": \"products\" } }\n" +
                "  ]\n" +
                "}";
        System.out.println(aliases);

        System.out.println("\n重新索引:");
        String reindex = "POST /_reindex\n" +
                "{\n" +
                "  \"source\": { \"index\": \"products_v1\" },\n" +
                "  \"dest\": { \"index\": \"products_v2\" }\n" +
                "}";
        System.out.println(reindex);
    }
}
