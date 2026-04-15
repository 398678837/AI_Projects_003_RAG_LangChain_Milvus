# 01_Basic_Concepts_基础概念

## 学习目标
- 理解Elasticsearch的基本概念
- 掌握Elasticsearch的核心架构
- 理解索引、文档、类型、字段
- 理解倒排索引
- 掌握Elasticsearch的应用场景

## 关键要点
### 1. Elasticsearch概述
- 分布式搜索和分析引擎
- 基于Lucene
- RESTful API
- 实时搜索
- 水平扩展

### 2. 核心概念
- 索引（Index）：类似数据库
- 类型（Type）：类似表（已废弃）
- 文档（Document）：类似行
- 字段（Field）：类似列
- 映射（Mapping）：类似Schema

### 3. 倒排索引
- 索引结构
- 分词
- 词项字典
- 倒排表
- 相关性评分

### 4. 数据类型
- 字符串：text、keyword
- 数值：long、integer、short、byte、double、float
- 日期：date
- 布尔：boolean
- 二进制：binary
- 复杂类型：object、nested、array

### 5. 架构组件
- 节点（Node）：单个服务器实例
- 集群（Cluster）：多个节点组成
- 分片（Shard）：索引的一部分
- 副本（Replica）：分片的副本
- 主分片（Primary Shard）
- 副分片（Replica Shard）

### 6. 应用场景
- 全文搜索
- 日志分析
- 指标监控
- 安全分析
- 业务搜索
- 实时分析

## 实践任务
1. 理解Elasticsearch核心概念
2. 理解倒排索引原理
3. 理解集群架构
4. 理解数据类型

## 参考资料
- Elasticsearch官方文档：https://www.elastic.co/guide/en/elasticsearch/reference/
- 《Elasticsearch权威指南》
