package com.example.elasticsearch.search;

import java.util.*;

public class SearchQueryDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch搜索查询示例 ===");

        try {
            basicSearchDemo();
            fullTextQueryDemo();
            termQueryDemo();
            compoundQueryDemo();
            searchResultsDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void basicSearchDemo() {
        System.out.println("\n--- 1. 基本搜索演示 ---");

        System.out.println("URI搜索:");
        System.out.println("  GET /books/_search?q=title:Elasticsearch");
        System.out.println("  GET /books/_search?q=author:张三&sort=price:asc");

        System.out.println("\nmatch_all查询:");
        String matchAll = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match_all\": {}\n" +
                "  }\n" +
                "}";
        System.out.println(matchAll);

        System.out.println("\nmatch查询:");
        String matchQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match\": {\n" +
                "      \"title\": \"Elasticsearch入门\"\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(matchQuery);
    }

    private static void fullTextQueryDemo() {
        System.out.println("\n--- 2. 全文查询演示 ---");

        System.out.println("match_phrase查询:");
        String matchPhrase = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match_phrase\": {\n" +
                "      \"title\": \"Elasticsearch入门\"\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(matchPhrase);

        System.out.println("\nmatch_phrase_prefix查询:");
        String matchPhrasePrefix = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match_phrase_prefix\": {\n" +
                "      \"title\": \"Elastic\"\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(matchPhrasePrefix);

        System.out.println("\nmulti_match查询:");
        String multiMatch = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"multi_match\": {\n" +
                "      \"query\": \"Elasticsearch\",\n" +
                "      \"fields\": [\"title\", \"description\"]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(multiMatch);
    }

    private static void termQueryDemo() {
        System.out.println("\n--- 3. 术语查询演示 ---");

        System.out.println("term查询:");
        String termQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"term\": {\n" +
                "      \"author\": {\n" +
                "        \"value\": \"张三\"\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(termQuery);

        System.out.println("\nterms查询:");
        String termsQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"terms\": {\n" +
                "      \"author\": [\"张三\", \"李四\", \"王五\"]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(termsQuery);

        System.out.println("\nrange查询:");
        String rangeQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"range\": {\n" +
                "      \"price\": {\n" +
                "        \"gte\": 50,\n" +
                "        \"lte\": 200\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(rangeQuery);

        System.out.println("\nexists查询:");
        String existsQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"exists\": {\n" +
                "      \"field\": \"description\"\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(existsQuery);
    }

    private static void compoundQueryDemo() {
        System.out.println("\n--- 4. 复合查询演示 ---");

        System.out.println("bool查询:");
        String boolQuery = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"bool\": {\n" +
                "      \"must\": [\n" +
                "        { \"match\": { \"title\": \"Elasticsearch\" } }\n" +
                "      ],\n" +
                "      \"filter\": [\n" +
                "        { \"range\": { \"price\": { \"gte\": 50, \"lte\": 200 } } }\n" +
                "      ],\n" +
                "      \"should\": [\n" +
                "        { \"match\": { \"description\": \"入门\" } }\n" +
                "      ],\n" +
                "      \"must_not\": [\n" +
                "        { \"term\": { \"author\": \"坏人\" } }\n" +
                "      ]\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(boolQuery);

        System.out.println("\nconstant_score查询:");
        String constantScore = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"constant_score\": {\n" +
                "      \"filter\": {\n" +
                "        \"term\": { \"category\": \"技术\" }\n" +
                "      },\n" +
                "      \"boost\": 1.2\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(constantScore);
    }

    private static void searchResultsDemo() {
        System.out.println("\n--- 5. 搜索结果演示 ---");

        System.out.println("分页:");
        String pagination = "GET /books/_search\n" +
                "{\n" +
                "  \"from\": 0,\n" +
                "  \"size\": 10,\n" +
                "  \"query\": {\n" +
                "    \"match_all\": {}\n" +
                "  }\n" +
                "}";
        System.out.println(pagination);

        System.out.println("\n排序:");
        String sorting = "GET /books/_search\n" +
                "{\n" +
                "  \"sort\": [\n" +
                "    { \"price\": { \"order\": \"asc\" } },\n" +
                "    { \"publishDate\": { \"order\": \"desc\" } }\n" +
                "  ],\n" +
                "  \"query\": {\n" +
                "    \"match_all\": {}\n" +
                "  }\n" +
                "}";
        System.out.println(sorting);

        System.out.println("\n_source过滤:");
        String sourceFilter = "GET /books/_search\n" +
                "{\n" +
                "  \"_source\": [\"title\", \"author\", \"price\"],\n" +
                "  \"query\": {\n" +
                "    \"match_all\": {}\n" +
                "  }\n" +
                "}";
        System.out.println(sourceFilter);

        System.out.println("\n高亮:");
        String highlight = "GET /books/_search\n" +
                "{\n" +
                "  \"query\": {\n" +
                "    \"match\": { \"title\": \"Elasticsearch\" }\n" +
                "  },\n" +
                "  \"highlight\": {\n" +
                "    \"fields\": {\n" +
                "      \"title\": {}\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(highlight);
    }
}
