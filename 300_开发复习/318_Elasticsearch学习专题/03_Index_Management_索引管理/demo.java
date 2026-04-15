package com.example.elasticsearch.index;

import java.util.*;

public class IndexManagementDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch索引管理示例 ===");

        try {
            createIndexDemo();
            mappingDemo();
            indexSettingsDemo();
            indexAliasDemo();
            indexTemplateDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void createIndexDemo() {
        System.out.println("\n--- 1. 创建索引演示 ---");

        System.out.println("创建索引 - PUT /books:");
        String createIndex = "PUT /books\n" +
                "{\n" +
                "  \"settings\": {\n" +
                "    \"number_of_shards\": 3,\n" +
                "    \"number_of_replicas\": 2\n" +
                "  },\n" +
                "  \"mappings\": {\n" +
                "    \"properties\": {\n" +
                "      \"title\": { \"type\": \"text\" },\n" +
                "      \"author\": { \"type\": \"keyword\" },\n" +
                "      \"price\": { \"type\": \"double\" },\n" +
                "      \"publishDate\": { \"type\": \"date\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(createIndex);

        System.out.println("\n删除索引 - DELETE /books:");
        System.out.println("DELETE /books");

        System.out.println("\n检查索引是否存在 - HEAD /books:");
        System.out.println("HEAD /books");
        System.out.println("  200 - 存在");
        System.out.println("  404 - 不存在");

        System.out.println("\n获取索引信息 - GET /books:");
        System.out.println("GET /books");

        System.out.println("\n查看所有索引 - GET /_cat/indices?v:");
        System.out.println("GET /_cat/indices?v");
    }

    private static void mappingDemo() {
        System.out.println("\n--- 2. 映射演示 ---");

        System.out.println("显式映射:");
        String explicitMapping = "PUT /products\n" +
                "{\n" +
                "  \"mappings\": {\n" +
                "    \"properties\": {\n" +
                "      \"name\": { \"type\": \"text\" },\n" +
                "      \"category\": { \"type\": \"keyword\" },\n" +
                "      \"price\": { \"type\": \"double\" },\n" +
                "      \"inStock\": { \"type\": \"boolean\" },\n" +
                "      \"created\": { \"type\": \"date\" },\n" +
                "      \"attributes\": { \"type\": \"object\" },\n" +
                "      \"tags\": { \"type\": \"keyword\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(explicitMapping);

        System.out.println("\n字段属性:");
        String fieldProperties = "{\n" +
                "  \"properties\": {\n" +
                "    \"title\": {\n" +
                "      \"type\": \"text\",\n" +
                "      \"analyzer\": \"standard\",\n" +
                "      \"search_analyzer\": \"standard\",\n" +
                "      \"boost\": 2.0,\n" +
                "      \"index\": true,\n" +
                "      \"store\": false\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(fieldProperties);

        System.out.println("\n获取映射 - GET /products/_mapping:");
        System.out.println("GET /products/_mapping");

        System.out.println("\n添加字段 - PUT /products/_mapping:");
        String addField = "PUT /products/_mapping\n" +
                "{\n" +
                "  \"properties\": {\n" +
                "    \"description\": { \"type\": \"text\" }\n" +
                "  }\n" +
                "}";
        System.out.println(addField);
    }

    private static void indexSettingsDemo() {
        System.out.println("\n--- 3. 索引设置演示 ---");

        System.out.println("创建索引时设置:");
        String createWithSettings = "PUT /logs\n" +
                "{\n" +
                "  \"settings\": {\n" +
                "    \"number_of_shards\": 5,\n" +
                "    \"number_of_replicas\": 1,\n" +
                "    \"refresh_interval\": \"30s\",\n" +
                "    \"index.codec\": \"best_compression\"\n" +
                "  }\n" +
                "}";
        System.out.println(createWithSettings);

        System.out.println("\n获取设置 - GET /logs/_settings:");
        System.out.println("GET /logs/_settings");

        System.out.println("\n更新设置 - PUT /logs/_settings:");
        String updateSettings = "PUT /logs/_settings\n" +
                "{\n" +
                "  \"index\": {\n" +
                "    \"number_of_replicas\": 2,\n" +
                "    \"refresh_interval\": \"60s\"\n" +
                "  }\n" +
                "}";
        System.out.println(updateSettings);

        System.out.println("\n设置只读:");
        String readOnly = "PUT /logs/_settings\n" +
                "{\n" +
                "  \"index\": {\n" +
                "    \"blocks\": {\n" +
                "      \"write\": true\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(readOnly);

        System.out.println("\n打开/关闭索引:");
        System.out.println("  POST /logs/_close");
        System.out.println("  POST /logs/_open");
    }

    private static void indexAliasDemo() {
        System.out.println("\n--- 4. 索引别名演示 ---");

        System.out.println("创建别名:");
        String createAlias = "POST /_aliases\n" +
                "{\n" +
                "  \"actions\": [\n" +
                "    {\n" +
                "      \"add\": {\n" +
                "        \"index\": \"products_v1\",\n" +
                "        \"alias\": \"products\"\n" +
                "      }\n" +
                "    }\n" +
                "  ]\n" +
                "}";
        System.out.println(createAlias);

        System.out.println("\n切换别名（零停机）:");
        String swapAlias = "POST /_aliases\n" +
                "{\n" +
                "  \"actions\": [\n" +
                "    { \"remove\": { \"index\": \"products_v1\", \"alias\": \"products\" } },\n" +
                "    { \"add\": { \"index\": \"products_v2\", \"alias\": \"products\" } }\n" +
                "  ]\n" +
                "}";
        System.out.println(swapAlias);

        System.out.println("\n删除别名:");
        String deleteAlias = "POST /_aliases\n" +
                "{\n" +
                "  \"actions\": [\n" +
                "    {\n" +
                "      \"remove\": {\n" +
                "        \"index\": \"products_v2\",\n" +
                "        \"alias\": \"products\"\n" +
                "      }\n" +
                "    }\n" +
                "  ]\n" +
                "}";
        System.out.println(deleteAlias);

        System.out.println("\n查看别名:");
        System.out.println("  GET /_alias");
        System.out.println("  GET /_alias/products");
        System.out.println("  GET /products_v2/_alias/*");
    }

    private static void indexTemplateDemo() {
        System.out.println("\n--- 5. 索引模板演示 ---");

        System.out.println("创建索引模板:");
        String createTemplate = "PUT /_index_template/logs_template\n" +
                "{\n" +
                "  \"index_patterns\": [\"logs-*\"],\n" +
                "  \"priority\": 100,\n" +
                "  \"template\": {\n" +
                "    \"settings\": {\n" +
                "      \"number_of_shards\": 3,\n" +
                "      \"number_of_replicas\": 1,\n" +
                "      \"refresh_interval\": \"5s\"\n" +
                "    },\n" +
                "    \"mappings\": {\n" +
                "      \"properties\": {\n" +
                "        \"timestamp\": { \"type\": \"date\" },\n" +
                "        \"message\": { \"type\": \"text\" },\n" +
                "        \"level\": { \"type\": \"keyword\" },\n" +
                "        \"service\": { \"type\": \"keyword\" }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(createTemplate);

        System.out.println("\n查看索引模板:");
        System.out.println("  GET /_index_template");
        System.out.println("  GET /_index_template/logs_template");

        System.out.println("\n删除索引模板:");
        System.out.println("  DELETE /_index_template/logs_template");
    }
}
