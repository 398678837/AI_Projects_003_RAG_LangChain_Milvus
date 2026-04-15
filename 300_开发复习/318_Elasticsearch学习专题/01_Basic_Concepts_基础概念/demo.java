package com.example.elasticsearch.basic;

import java.util.*;

public class BasicConceptsDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch基础概念示例 ===");

        try {
            coreConceptsDemo();
            invertedIndexDemo();
            dataTypesDemo();
            clusterArchitectureDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void coreConceptsDemo() {
        System.out.println("\n--- 1. 核心概念演示 ---");

        System.out.println("Elasticsearch核心概念类比关系数据库:");
        System.out.println("  关系数据库      -> Elasticsearch");
        System.out.println("  Database        -> Index（索引）");
        System.out.println("  Table           -> Type（类型，已废弃）");
        System.out.println("  Row             -> Document（文档）");
        System.out.println("  Column          -> Field（字段）");
        System.out.println("  Schema          -> Mapping（映射）");
        System.out.println("  SQL             -> Query DSL");

        System.out.println("\n文档示例（JSON格式）:");
        String document = "{\n" +
                "  \"id\": 1,\n" +
                "  \"title\": \"Elasticsearch入门\",\n" +
                "  \"author\": \"张三\",\n" +
                "  \"price\": 99.00,\n" +
                "  \"publishDate\": \"2024-01-01\",\n" +
                "  \"tags\": [\"Elasticsearch\", \"搜索\", \"大数据\"]\n" +
                "}";
        System.out.println(document);
    }

    private static void invertedIndexDemo() {
        System.out.println("\n--- 2. 倒排索引演示 ---");

        List<String> documents = Arrays.asList(
                "Elasticsearch是一个分布式搜索引擎",
                "搜索引擎使用倒排索引",
                "Elasticsearch基于Lucene构建"
        );

        System.out.println("原始文档:");
        for (int i = 0; i < documents.size(); i++) {
            System.out.println("  文档" + (i + 1) + ": " + documents.get(i));
        }

        Map<String, List<Integer>> invertedIndex = buildInvertedIndex(documents);

        System.out.println("\n倒排索引:");
        for (Map.Entry<String, List<Integer>> entry : invertedIndex.entrySet()) {
            System.out.println("  \"" + entry.getKey() + "\" -> " + entry.getValue());
        }

        System.out.println("\n搜索示例:");
        String term = "Elasticsearch";
        List<Integer> result = invertedIndex.get(term);
        System.out.println("  搜索 \"" + term + "\" -> 文档" + result);
    }

    private static Map<String, List<Integer>> buildInvertedIndex(List<String> documents) {
        Map<String, List<Integer>> index = new HashMap<>();

        for (int docId = 0; docId < documents.size(); docId++) {
            String doc = documents.get(docId);
            String[] terms = doc.split("\\s+");

            for (String term : terms) {
                term = term.toLowerCase();
                index.computeIfAbsent(term, k -> new ArrayList<>()).add(docId + 1);
            }
        }

        return index;
    }

    private static void dataTypesDemo() {
        System.out.println("\n--- 3. 数据类型演示 ---");

        System.out.println("Elasticsearch常用数据类型:");
        System.out.println("  字符串类型:");
        System.out.println("    - text: 全文搜索，会分词");
        System.out.println("    - keyword: 精确匹配，不分词");
        System.out.println();

        System.out.println("  数值类型:");
        System.out.println("    - long: 长整型");
        System.out.println("    - integer: 整型");
        System.out.println("    - short: 短整型");
        System.out.println("    - byte: 字节型");
        System.out.println("    - double: 双精度浮点");
        System.out.println("    - float: 单精度浮点");
        System.out.println();

        System.out.println("  其他类型:");
        System.out.println("    - date: 日期类型");
        System.out.println("    - boolean: 布尔类型");
        System.out.println("    - binary: 二进制类型");
        System.out.println("    - object: 对象类型");
        System.out.println("    - nested: 嵌套类型");
        System.out.println("    - array: 数组类型");

        System.out.println("\n映射示例（Mapping）:");
        String mapping = "{\n" +
                "  \"properties\": {\n" +
                "    \"title\": { \"type\": \"text\" },\n" +
                "    \"author\": { \"type\": \"keyword\" },\n" +
                "    \"price\": { \"type\": \"double\" },\n" +
                "    \"publishDate\": { \"type\": \"date\" },\n" +
                "    \"inStock\": { \"type\": \"boolean\" }\n" +
                "  }\n" +
                "}";
        System.out.println(mapping);
    }

    private static void clusterArchitectureDemo() {
        System.out.println("\n--- 4. 集群架构演示 ---");

        System.out.println("Elasticsearch集群架构:");
        System.out.println("  集群（Cluster）:");
        System.out.println("    - 由多个节点组成");
        System.out.println("    - 统一的集群名称");
        System.out.println("    - 自动发现和加入");
        System.out.println();

        System.out.println("  节点（Node）:");
        System.out.println("    - Master节点: 管理集群");
        System.out.println("    - Data节点: 存储数据");
        System.out.println("    - Client节点: 路由请求");
        System.out.println("    - Ingest节点: 数据预处理");
        System.out.println();

        System.out.println("  分片（Shard）:");
        System.out.println("    - 索引的水平拆分");
        System.out.println("    - 主分片（Primary）");
        System.out.println("    - 副分片（Replica）");
        System.out.println("    - 提高并行处理能力");
        System.out.println();

        System.out.println("  副本（Replica）:");
        System.out.println("    - 分片的拷贝");
        System.out.println("    - 提高可用性");
        System.out.println("    - 提高读性能");
        System.out.println("    - 主分片故障时提升为主");

        System.out.println("\n索引分片示例:");
        System.out.println("  索引: books");
        System.out.println("  主分片数: 3");
        System.out.println("  副本数: 2");
        System.out.println("  总分片数: 3 × (1 + 2) = 9");
        System.out.println();
        System.out.println("  节点1: [P0, R1, R2]");
        System.out.println("  节点2: [P1, R0, R2]");
        System.out.println("  节点3: [P2, R0, R1]");
        System.out.println("  (P=主分片, R=副分片)");
    }
}
