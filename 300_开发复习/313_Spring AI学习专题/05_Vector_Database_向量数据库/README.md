# Spring AI 向量数据库

## 1. 向量数据库概述

向量数据库是一种专门用于存储和检索向量数据的数据库，在 Spring AI 中，向量数据库主要用于存储文本的向量表示，支持语义搜索和 RAG（检索增强生成）系统。

### 1.1 向量数据库的作用

- **语义搜索**：基于向量相似度进行搜索，能够理解文本的语义含义
- **RAG 支持**：为检索增强生成系统提供高效的向量检索能力
- **相似度计算**：快速计算向量之间的相似度
- **大规模数据处理**：高效处理和索引大规模向量数据

## 2. 支持的向量数据库

Spring AI 支持多种向量数据库，包括：

### 2.1 PostgreSQL with pgvector

PostgreSQL 是一个功能强大的开源关系型数据库，通过 pgvector 扩展支持向量存储和检索。

**特点**：
- 成熟的关系型数据库，支持 SQL
- 可扩展性好
- 适合中小型应用

### 2.2 Milvus

Milvus 是一个专门为向量检索设计的开源数据库。

**特点**：
- 高性能向量检索
- 支持多种索引类型
- 适合大规模向量数据

### 2.3 Chroma

Chroma 是一个轻量级的向量数据库，专为 AI 应用设计。

**特点**：
- 易于使用
- 适合开发和测试
- 内存存储，速度快

### 2.4 FAISS

FAISS 是 Facebook AI 开发的向量搜索库。

**特点**：
- 高性能
- 适合内存中的向量搜索
- 支持多种索引类型

### 2.5 Pinecone

Pinecone 是一个托管的向量数据库服务。

**特点**：
- 完全托管
- 高可扩展性
- 适合生产环境

## 3. 向量数据库集成

### 3.1 PostgreSQL with pgvector

#### 3.1.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-pgvector-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.3</version>
</dependency>
```

#### 3.1.2 应用配置

```properties
# PostgreSQL 连接配置
spring.ai.vectorstore.pgvector.connection-string=jdbc:postgresql://localhost:5432/vector_db
spring.ai.vectorstore.pgvector.username=postgres
spring.ai.vectorstore.pgvector.password=postgres

# 表配置
spring.ai.vectorstore.pgvector.table-name=vector_store
spring.ai.vectorstore.pgvector.dimension=1536
```

### 3.2 Milvus

#### 3.2.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-milvus-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.2.2 应用配置

```properties
# Milvus 连接配置
spring.ai.vectorstore.milvus.host=localhost
spring.ai.vectorstore.milvus.port=19530
spring.ai.vectorstore.milvus.collection-name=vector_store
spring.ai.vectorstore.milvus.dimension=1536
```

### 3.3 Chroma

#### 3.3.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-chroma-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.3.2 应用配置

```properties
# Chroma 配置
spring.ai.vectorstore.chroma.collection-name=vector_store
spring.ai.vectorstore.chroma.embedding-dimension=1536
```

### 3.4 FAISS

#### 3.4.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-faiss-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.4.2 应用配置

```properties
# FAISS 配置
spring.ai.vectorstore.faiss.index-path=faiss_index
spring.ai.vectorstore.faiss.dimension=1536
```

## 4. 向量数据库使用

### 4.1 基本操作

#### 4.1.1 添加文档

```java
@Autowired
private VectorStore vectorStore;

public void addDocument(String content, Map<String, Object> metadata) {
    Document document = new Document(content, metadata);
    vectorStore.add(List.of(document));
}
```

#### 4.1.2 搜索文档

```java
public List<Document> search(String query, int k) {
    return vectorStore.search(query, k);
}
```

#### 4.1.3 删除文档

```java
public void deleteDocuments(List<String> ids) {
    vectorStore.delete(ids);
}
```

### 4.2 高级操作

#### 4.2.1 带过滤条件的搜索

```java
public List<Document> searchWithFilter(String query, int k, Map<String, Object> filter) {
    // 实现带过滤条件的搜索
    return vectorStore.search(query, k);
}
```

#### 4.2.2 批量操作

```java
public void batchAdd(List<Document> documents) {
    vectorStore.add(documents);
}
```

#### 4.2.3 索引管理

```java
public void createIndex() {
    // 实现索引创建
}

public void updateIndex() {
    // 实现索引更新
}
```

## 5. 向量存储最佳实践

### 5.1 文档处理

#### 5.1.1 文本分块

- **分块策略**：根据文本长度和语义进行分块
- **块大小**：一般为 500-1000  tokens
- **重叠**：相邻块之间保留 10-20% 的重叠，确保上下文连续性

#### 5.1.2 元数据管理

- **丰富的元数据**：添加文档来源、类型、创建时间等元数据
- **结构化元数据**：使用结构化的元数据格式，便于过滤和检索
- **元数据索引**：为常用的元数据字段创建索引

### 5.2 向量存储优化

#### 5.2.1 索引选择

- **HNSW**：适合高维向量，查询速度快
- **IVF**：适合大规模数据集
- **FLAT**：适合小数据集，精度高

#### 5.2.2 批量处理

- **批量添加**：使用批量添加减少 API 调用次数
- **批量搜索**：批量处理多个查询
- **批量删除**：批量删除文档

#### 5.2.3 缓存策略

- **查询缓存**：缓存频繁的查询结果
- **向量缓存**：缓存热点向量
- **索引缓存**：缓存索引结构

### 5.3 性能优化

#### 5.3.1 硬件优化

- **内存**：确保足够的内存用于索引和缓存
- **CPU**：使用多核 CPU 加速向量计算
- **存储**：使用 SSD 存储提高 I/O 性能

#### 5.3.2 配置优化

- **批量大小**：根据硬件配置调整批量大小
- **索引参数**：根据数据特点调整索引参数
- **并发度**：合理设置并发查询数

#### 5.3.3 查询优化

- **查询向量优化**：使用高质量的查询向量
- **结果过滤**：在应用层对结果进行过滤
- **分页查询**：使用分页减少返回数据量

## 6. 向量数据库与 RAG 集成

### 6.1 RAG 流程

1. **文档加载**：从各种源加载文档
2. **文本分块**：将文档分割成小块
3. **向量化**：使用嵌入模型将文本转换为向量
4. **存储向量**：将向量存储到向量数据库
5. **检索**：根据查询向量检索相关文档
6. **生成**：结合检索结果生成回答

### 6.2 实现示例

```java
@RestController
public class RAGController {
    
    private final VectorStore vectorStore;
    private final ChatClient chatClient;
    private final EmbeddingClient embeddingClient;
    
    @Autowired
    public RAGController(VectorStore vectorStore, 
                        ChatClient chatClient, 
                        EmbeddingClient embeddingClient) {
        this.vectorStore = vectorStore;
        this.chatClient = chatClient;
        this.embeddingClient = embeddingClient;
    }
    
    @PostMapping("/rag")
    public String rag(@RequestParam String question) {
        // 1. 检索相关文档
        List<Document> documents = vectorStore.search(question, 3);
        
        // 2. 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 3. 构建提示
        String prompt = String.format("基于以下上下文回答问题：\n\n%s\n\n问题：%s", 
                                    context.toString(), question);
        
        // 4. 调用模型
        return chatClient.call(prompt);
    }
}
```

## 7. 常见问题及解决方案

### 7.1 向量维度不匹配

**问题**：嵌入模型的向量维度与向量数据库配置的维度不匹配
**解决方案**：确保嵌入模型的向量维度与向量数据库配置的维度一致

### 7.2 检索结果质量差

**问题**：检索到的文档与查询相关性低
**解决方案**：
- 优化文本分块策略
- 使用更高质量的嵌入模型
- 调整检索参数
- 增加检索结果数量

### 7.3 性能问题

**问题**：向量数据库查询速度慢
**解决方案**：
- 使用合适的索引类型
- 优化硬件配置
- 增加缓存
- 批量处理查询

### 7.4 内存使用过高

**问题**：向量数据库内存使用过高
**解决方案**：
- 使用磁盘索引
- 调整批量大小
- 优化缓存策略
- 使用更高效的索引算法

## 8. 总结

向量数据库是 Spring AI 中实现语义搜索和 RAG 系统的关键组件。通过选择合适的向量数据库，优化配置和使用策略，可以构建高性能、高质量的 AI 应用。

在实际开发中，应根据应用场景和数据规模选择合适的向量数据库，遵循最佳实践，不断优化系统性能和检索质量。随着 AI 技术的发展，向量数据库也在不断演进，为开发者提供更多强大的功能和更好的性能。