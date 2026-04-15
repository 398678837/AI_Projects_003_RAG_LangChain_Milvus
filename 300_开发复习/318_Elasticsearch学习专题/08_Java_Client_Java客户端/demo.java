package com.example.elasticsearch.client;

import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.CredentialsProvider;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
import org.elasticsearch.action.bulk.BulkRequest;
import org.elasticsearch.action.bulk.BulkResponse;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.delete.DeleteResponse;
import org.elasticsearch.action.get.GetRequest;
import org.elasticsearch.action.get.GetResponse;
import org.elasticsearch.action.get.MultiGetRequest;
import org.elasticsearch.action.get.MultiGetResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.support.master.AcknowledgedResponse;
import org.elasticsearch.action.update.UpdateRequest;
import org.elasticsearch.action.update.UpdateResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.client.indices.CreateIndexRequest;
import org.elasticsearch.client.indices.CreateIndexResponse;
import org.elasticsearch.client.indices.GetIndexRequest;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.unit.TimeValue;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.query.*;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.aggregations.AggregationBuilders;
import org.elasticsearch.search.aggregations.bucket.terms.Terms;
import org.elasticsearch.search.aggregations.bucket.terms.TermsAggregationBuilder;
import org.elasticsearch.search.aggregations.metrics.Avg;
import org.elasticsearch.search.aggregations.metrics.AvgAggregationBuilder;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.elasticsearch.search.sort.SortOrder;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

public class JavaClientDemo {

    private static RestHighLevelClient client;

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch Java客户端示例 ===");

        try {
            createClientDemo();
            indexOperationsDemo();
            documentOperationsDemo();
            searchOperationsDemo();
            aggregationOperationsDemo();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeClient();
        }
    }

    private static void createClientDemo() {
        System.out.println("\n--- 1. 创建客户端演示 ---");

        RestClientBuilder builder = RestClient.builder(
                new HttpHost("localhost", 9200, "http")
        );

        final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
        credentialsProvider.setCredentials(AuthScope.ANY,
                new UsernamePasswordCredentials("elastic", "password"));

        builder.setHttpClientConfigCallback(httpClientBuilder ->
                httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider));

        client = new RestHighLevelClient(builder);

        System.out.println("RestHighLevelClient创建成功");
    }

    private static void closeClient() {
        if (client != null) {
            try {
                client.close();
                System.out.println("客户端已关闭");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static void indexOperationsDemo() throws IOException {
        System.out.println("\n--- 2. 索引操作演示 ---");

        String indexName = "products";

        System.out.println("检查索引是否存在:");
        GetIndexRequest getIndexRequest = new GetIndexRequest(indexName);
        boolean exists = client.indices().exists(getIndexRequest, RequestOptions.DEFAULT);
        System.out.println("  索引存在: " + exists);

        if (exists) {
            System.out.println("删除索引:");
            DeleteIndexRequest deleteRequest = new DeleteIndexRequest(indexName);
            AcknowledgedResponse deleteResponse = client.indices().delete(deleteRequest, RequestOptions.DEFAULT);
            System.out.println("  删除成功: " + deleteResponse.isAcknowledged());
        }

        System.out.println("创建索引:");
        CreateIndexRequest createRequest = new CreateIndexRequest(indexName);
        createRequest.settings(Settings.builder()
                .put("index.number_of_shards", 3)
                .put("index.number_of_replicas", 1));

        String mapping = "{\n" +
                "  \"properties\": {\n" +
                "    \"name\": { \"type\": \"text\" },\n" +
                "    \"category\": { \"type\": \"keyword\" },\n" +
                "    \"price\": { \"type\": \"double\" },\n" +
                "    \"inStock\": { \"type\": \"boolean\" },\n" +
                "    \"created\": { \"type\": \"date\" }\n" +
                "  }\n" +
                "}";
        createRequest.mapping(mapping, XContentType.JSON);

        CreateIndexResponse createResponse = client.indices().create(createRequest, RequestOptions.DEFAULT);
        System.out.println("  创建成功: " + createResponse.isAcknowledged());
    }

    private static void documentOperationsDemo() throws IOException {
        System.out.println("\n--- 3. 文档操作演示 ---");

        String indexName = "products";

        System.out.println("索引文档:");
        Map<String, Object> product = new HashMap<>();
        product.put("name", "iPhone 15");
        product.put("category", "手机");
        product.put("price", 7999.00);
        product.put("inStock", true);
        product.put("created", "2024-01-01");

        IndexRequest indexRequest = new IndexRequest(indexName)
                .id("1")
                .source(product);

        IndexResponse indexResponse = client.index(indexRequest, RequestOptions.DEFAULT);
        System.out.println("  文档ID: " + indexResponse.getId());
        System.out.println("  版本: " + indexResponse.getVersion());

        System.out.println("\n获取文档:");
        GetRequest getRequest = new GetRequest(indexName, "1");
        GetResponse getResponse = client.get(getRequest, RequestOptions.DEFAULT);
        System.out.println("  文档存在: " + getResponse.isExists());
        if (getResponse.isExists()) {
            System.out.println("  文档内容: " + getResponse.getSourceAsString());
        }

        System.out.println("\n更新文档:");
        Map<String, Object> updateFields = new HashMap<>();
        updateFields.put("price", 7599.00);

        UpdateRequest updateRequest = new UpdateRequest(indexName, "1")
                .doc(updateFields);

        UpdateResponse updateResponse = client.update(updateRequest, RequestOptions.DEFAULT);
        System.out.println("  更新版本: " + updateResponse.getVersion());

        System.out.println("\n删除文档:");
        DeleteRequest deleteRequest = new DeleteRequest(indexName, "1");
        DeleteResponse deleteResponse = client.delete(deleteRequest, RequestOptions.DEFAULT);
        System.out.println("  删除成功: " + deleteResponse.status());

        System.out.println("\n批量操作:");
        BulkRequest bulkRequest = new BulkRequest();

        bulkRequest.add(new IndexRequest(indexName).id("1").source(
                "name", "iPhone 15", "category", "手机", "price", 7999.00));
        bulkRequest.add(new IndexRequest(indexName).id("2").source(
                "name", "MacBook Pro", "category", "笔记本", "price", 14999.00));
        bulkRequest.add(new IndexRequest(indexName).id("3").source(
                "name", "iPad Pro", "category", "平板", "price", 6999.00));

        BulkResponse bulkResponse = client.bulk(bulkRequest, RequestOptions.DEFAULT);
        System.out.println("  批量操作完成，是否有失败: " + bulkResponse.hasFailures());
    }

    private static void searchOperationsDemo() throws IOException {
        System.out.println("\n--- 4. 搜索操作演示 ---");

        String indexName = "products";

        System.out.println("搜索所有文档:");
        SearchRequest searchRequest = new SearchRequest(indexName);
        SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.query(QueryBuilders.matchAllQuery());
        searchRequest.source(sourceBuilder);

        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        System.out.println("  命中数: " + searchResponse.getHits().getTotalHits());
        for (SearchHit hit : searchResponse.getHits().getHits()) {
            System.out.println("    - " + hit.getSourceAsString());
        }

        System.out.println("\nMatch查询:");
        sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.query(QueryBuilders.matchQuery("name", "iPhone"));
        searchRequest.source(sourceBuilder);

        searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        System.out.println("  命中数: " + searchResponse.getHits().getTotalHits());

        System.out.println("\nBool查询:");
        BoolQueryBuilder boolQuery = QueryBuilders.boolQuery()
                .must(QueryBuilders.matchQuery("name", "Pro"))
                .filter(QueryBuilders.rangeQuery("price").gte(5000).lte(20000));

        sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.query(boolQuery);
        searchRequest.source(sourceBuilder);

        searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        System.out.println("  命中数: " + searchResponse.getHits().getTotalHits());

        System.out.println("\n分页和排序:");
        sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.query(QueryBuilders.matchAllQuery());
        sourceBuilder.from(0);
        sourceBuilder.size(10);
        sourceBuilder.sort("price", SortOrder.ASC);
        searchRequest.source(sourceBuilder);

        searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        System.out.println("  命中数: " + searchResponse.getHits().getTotalHits());
    }

    private static void aggregationOperationsDemo() throws IOException {
        System.out.println("\n--- 5. 聚合操作演示 ---");

        String indexName = "products";

        System.out.println("Terms聚合:");
        TermsAggregationBuilder termsAgg = AggregationBuilders
                .terms("by_category")
                .field("category")
                .size(10);

        SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.size(0);
        sourceBuilder.aggregation(termsAgg);

        SearchRequest searchRequest = new SearchRequest(indexName);
        searchRequest.source(sourceBuilder);

        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        Terms terms = searchResponse.getAggregations().get("by_category");
        for (Terms.Bucket bucket : terms.getBuckets()) {
            System.out.println("  " + bucket.getKeyAsString() + ": " + bucket.getDocCount());
        }

        System.out.println("\n嵌套聚合:");
        AvgAggregationBuilder avgPrice = AggregationBuilders.avg("avg_price").field("price");
        termsAgg = AggregationBuilders.terms("by_category").field("category").subAggregation(avgPrice);

        sourceBuilder = new SearchSourceBuilder();
        sourceBuilder.size(0);
        sourceBuilder.aggregation(termsAgg);
        searchRequest.source(sourceBuilder);

        searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        terms = searchResponse.getAggregations().get("by_category");
        for (Terms.Bucket bucket : terms.getBuckets()) {
            Avg avg = bucket.getAggregations().get("avg_price");
            System.out.println("  " + bucket.getKeyAsString() + ": " + bucket.getDocCount() +
                    " 平均价格: " + avg.getValue());
        }
    }
}
