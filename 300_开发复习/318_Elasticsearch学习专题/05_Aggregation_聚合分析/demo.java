package com.example.elasticsearch.aggregation;

import java.util.*;

public class AggregationDemo {

    public static void main(String[] args) {
        System.out.println("=== Elasticsearch聚合分析示例 ===");

        try {
            metricAggregationDemo();
            bucketAggregationDemo();
            nestedAggregationDemo();
            pipelineAggregationDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void metricAggregationDemo() {
        System.out.println("\n--- 1. Metric聚合演示 ---");

        System.out.println("基本统计聚合:");
        String basicStats = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"avg_price\": { \"avg\": { \"field\": \"price\" } },\n" +
                "    \"sum_price\": { \"sum\": { \"field\": \"price\" } },\n" +
                "    \"min_price\": { \"min\": { \"field\": \"price\" } },\n" +
                "    \"max_price\": { \"max\": { \"field\": \"price\" } },\n" +
                "    \"count_products\": { \"value_count\": { \"field\": \"price\" } }\n" +
                "  }\n" +
                "}";
        System.out.println(basicStats);

        System.out.println("\nstats聚合:");
        String statsAgg = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"price_stats\": { \"stats\": { \"field\": \"price\" } }\n" +
                "  }\n" +
                "}";
        System.out.println(statsAgg);

        System.out.println("\ncardinality聚合:");
        String cardinality = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"unique_categories\": { \"cardinality\": { \"field\": \"category\" } }\n" +
                "  }\n" +
                "}";
        System.out.println(cardinality);

        System.out.println("\npercentiles聚合:");
        String percentiles = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"price_percentiles\": { \"percentiles\": { \"field\": \"price\" } }\n" +
                "  }\n" +
                "}";
        System.out.println(percentiles);

        System.out.println("\ntop_hits聚合:");
        String topHits = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"top_products\": {\n" +
                "      \"top_hits\": {\n" +
                "        \"size\": 3,\n" +
                "        \"sort\": [{ \"price\": { \"order\": \"desc\" } }]\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(topHits);
    }

    private static void bucketAggregationDemo() {
        System.out.println("\n--- 2. Bucket聚合演示 ---");

        System.out.println("terms聚合:");
        String termsAgg = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"by_category\": {\n" +
                "      \"terms\": { \"field\": \"category\", \"size\": 10 }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(termsAgg);

        System.out.println("\nrange聚合:");
        String rangeAgg = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"price_ranges\": {\n" +
                "      \"range\": {\n" +
                "        \"field\": \"price\",\n" +
                "        \"ranges\": [\n" +
                "          { \"to\": 50 },\n" +
                "          { \"from\": 50, \"to\": 100 },\n" +
                "          { \"from\": 100 }\n" +
                "        ]\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(rangeAgg);

        System.out.println("\ndate_histogram聚合:");
        String dateHistogram = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\",\n" +
                "        \"format\": \"yyyy-MM\"\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(dateHistogram);

        System.out.println("\nhistogram聚合:");
        String histogram = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"price_histogram\": {\n" +
                "      \"histogram\": {\n" +
                "        \"field\": \"price\",\n" +
                "        \"interval\": 50\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(histogram);

        System.out.println("\nfilter聚合:");
        String filterAgg = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"expensive_products\": {\n" +
                "      \"filter\": { \"range\": { \"price\": { \"gte\": 100 } } },\n" +
                "      \"aggs\": { \"avg_price\": { \"avg\": { \"field\": \"price\" } } }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(filterAgg);
    }

    private static void nestedAggregationDemo() {
        System.out.println("\n--- 3. 嵌套聚合演示 ---");

        System.out.println("嵌套聚合 - terms中嵌套metric:");
        String nested1 = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"by_category\": {\n" +
                "      \"terms\": { \"field\": \"category\" },\n" +
                "      \"aggs\": {\n" +
                "        \"avg_price\": { \"avg\": { \"field\": \"price\" } },\n" +
                "        \"max_price\": { \"max\": { \"field\": \"price\" } }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(nested1);

        System.out.println("\n多层嵌套:");
        String nested2 = "GET /products/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"by_category\": {\n" +
                "      \"terms\": { \"field\": \"category\" },\n" +
                "      \"aggs\": {\n" +
                "        \"by_brand\": {\n" +
                "          \"terms\": { \"field\": \"brand\" },\n" +
                "          \"aggs\": {\n" +
                "            \"price_stats\": { \"stats\": { \"field\": \"price\" } }\n" +
                "          }\n" +
                "        }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(nested2);

        System.out.println("\ndate_histogram嵌套:");
        String nested3 = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\"\n" +
                "      },\n" +
                "      \"aggs\": {\n" +
                "        \"total_sales\": { \"sum\": { \"field\": \"amount\" } },\n" +
                "        \"avg_order\": { \"avg\": { \"field\": \"amount\" } }\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(nested3);
    }

    private static void pipelineAggregationDemo() {
        System.out.println("\n--- 4. Pipeline聚合演示 ---");

        System.out.println("avg_bucket聚合:");
        String avgBucket = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\"\n" +
                "      },\n" +
                "      \"aggs\": {\n" +
                "        \"monthly_sales\": { \"sum\": { \"field\": \"amount\" } }\n" +
                "      }\n" +
                "    },\n" +
                "    \"avg_monthly_sales\": {\n" +
                "      \"avg_bucket\": { \"buckets_path\": \"sales_by_month>monthly_sales\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(avgBucket);

        System.out.println("\nderivative聚合:");
        String derivative = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\"\n" +
                "      },\n" +
                "      \"aggs\": {\n" +
                "        \"monthly_sales\": { \"sum\": { \"field\": \"amount\" } }\n" +
                "      }\n" +
                "    },\n" +
                "    \"sales_diff\": {\n" +
                "      \"derivative\": { \"buckets_path\": \"sales_by_month>monthly_sales\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(derivative);

        System.out.println("\ncumulative_sum聚合:");
        String cumulativeSum = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\"\n" +
                "      },\n" +
                "      \"aggs\": {\n" +
                "        \"monthly_sales\": { \"sum\": { \"field\": \"amount\" } }\n" +
                "      }\n" +
                "    },\n" +
                "    \"total_sales\": {\n" +
                "      \"cumulative_sum\": { \"buckets_path\": \"sales_by_month>monthly_sales\" }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(cumulativeSum);

        System.out.println("\nmoving_avg聚合:");
        String movingAvg = "GET /orders/_search\n" +
                "{\n" +
                "  \"size\": 0,\n" +
                "  \"aggs\": {\n" +
                "    \"sales_by_month\": {\n" +
                "      \"date_histogram\": {\n" +
                "        \"field\": \"orderDate\",\n" +
                "        \"interval\": \"month\"\n" +
                "      },\n" +
                "      \"aggs\": {\n" +
                "        \"monthly_sales\": { \"sum\": { \"field\": \"amount\" } }\n" +
                "      }\n" +
                "    },\n" +
                "    \"moving_avg_sales\": {\n" +
                "      \"moving_avg\": {\n" +
                "        \"buckets_path\": \"sales_by_month>monthly_sales\",\n" +
                "        \"window\": 3\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}";
        System.out.println(movingAvg);
    }
}
