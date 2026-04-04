# Spring AI 基础概念

## 1. Spring AI 简介

Spring AI 是 Spring 生态系统中的一个新框架，旨在简化人工智能（AI）应用的开发。它提供了一套统一的 API 和抽象，使开发者能够轻松集成各种 AI 模型和服务到 Spring 应用中。

### 1.1 Spring AI 的设计理念

- **统一抽象**：为不同的 AI 模型和服务提供统一的接口，减少学习成本
- **简化集成**：提供简洁的 API，减少样板代码
- **生态系统集成**：与 Spring Boot、Spring Cloud 等 Spring 生态系统无缝集成
- **可扩展性**：支持多种 AI 模型和服务提供商
- **生产就绪**：提供监控、容错、安全等企业级特性

## 2. 核心概念

### 2.1 模型（Model）

模型是 Spring AI 的核心概念，代表一个 AI 模型，如大语言模型（LLM）、嵌入模型等。

- **大语言模型（LLM）**：如 GPT-3.5、GPT-4、Llama 等，用于生成文本、回答问题等
- **嵌入模型**：用于将文本转换为向量表示，用于语义搜索、相似度计算等
- **多模态模型**：支持处理文本、图像等多种数据类型

### 2.2 客户端（Client）

客户端是与 AI 模型交互的接口，提供了调用模型的方法。

- **ChatClient**：用于与大语言模型进行对话
- **EmbeddingClient**：用于文本向量化
- **ImageClient**：用于处理图像

### 2.3 提示（Prompt）

提示是发送给 AI 模型的输入，包含指令、上下文和问题。

- **提示模板**：结构化的提示格式，支持变量替换
- **提示链**：多个提示的组合，形成复杂的对话流程
- **上下文管理**：管理对话历史和上下文信息

### 2.4 响应（Response）

响应是 AI 模型的输出，包含生成的文本、向量等。

- **ChatResponse**：大语言模型的响应
- **EmbeddingResponse**：嵌入模型的响应
- **ImageResponse**：图像模型的响应

### 2.5 检索增强生成（RAG）

RAG 是一种结合检索和生成的技术，用于增强大语言模型的知识和准确性。

- **文档加载**：从多种源加载文档
- **文本分块**：将文档分割成小块
- **向量存储**：存储文本的向量表示
- **检索**：根据查询检索相关文本
- **生成**：结合检索结果生成回答

## 3. Spring AI 架构

### 3.1 分层架构

Spring AI 采用分层架构，从上到下依次为：

1. **应用层**：用户应用代码
2. **客户端层**：ChatClient、EmbeddingClient 等客户端
3. **模型层**：各种 AI 模型的实现
4. **底层服务**：与 AI 服务提供商的集成

### 3.2 核心组件

- **Model**：模型接口，定义了模型的基本操作
- **Client**：客户端接口，提供了与模型交互的方法
- **Prompt**：提示相关的类和接口
- **Response**：响应相关的类和接口
- **RAG**：检索增强生成相关的组件

## 4. 快速开始

### 4.1 依赖配置

在 Maven 项目中添加 Spring AI 依赖：

```xml
<!-- OpenAI 集成 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>

<!-- Hugging Face 集成 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-huggingface-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>

<!-- 向量数据库集成 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-pgvector-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

### 4.2 配置示例

在 `application.properties` 中配置 AI 模型：

```properties
# OpenAI 配置
spring.ai.openai.api-key=your-api-key
spring.ai.openai.chat.model=gpt-3.5-turbo
spring.ai.openai.chat.temperature=0.7

# Hugging Face 配置
spring.ai.huggingface.api-key=your-api-key
spring.ai.huggingface.chat.model=mistralai/Mixtral-8x7B-Instruct-v0.1

# 向量数据库配置
spring.ai.vectorstore.pgvector.connection-string=jdbc:postgresql://localhost:5432/vector_db
spring.ai.vectorstore.pgvector.username=postgres
spring.ai.vectorstore.pgvector.password=postgres
```

### 4.3 基本使用

#### 4.3.1 聊天客户端

```java
@RestController
public class ChatController {
    
    private final ChatClient chatClient;
    
    public ChatController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    @GetMapping("/chat")
    public String chat(@RequestParam String message) {
        return chatClient.call(message);
    }
    
    @PostMapping("/chat")
    public ChatResponse chat(@RequestBody ChatRequest request) {
        return chatClient.chat(request.getMessages());
    }
}
```

#### 4.3.2 嵌入客户端

```java
@RestController
public class EmbeddingController {
    
    private final EmbeddingClient embeddingClient;
    
    public EmbeddingController(EmbeddingClient embeddingClient) {
        this.embeddingClient = embeddingClient;
    }
    
    @GetMapping("/embed")
    public List<Double> embed(@RequestParam String text) {
        EmbeddingResponse response = embeddingClient.embed(text);
        return response.getEmbedding();
    }
}
```

## 5. 核心 API

### 5.1 ChatClient

```java
public interface ChatClient {
    // 简单调用
    String call(String message);
    
    // 带消息列表的调用
    ChatResponse chat(List<Message> messages);
    
    // 带选项的调用
    ChatResponse chat(List<Message> messages, ChatOptions options);
}
```

### 5.2 EmbeddingClient

```java
public interface EmbeddingClient {
    // 嵌入单个文本
    EmbeddingResponse embed(String text);
    
    // 嵌入多个文本
    EmbeddingResponse embed(List<String> texts);
}
```

### 5.3 PromptTemplate

```java
public class PromptTemplate {
    // 创建提示模板
    public static PromptTemplate create(String template);
    
    // 渲染提示
    public String render(Map<String, Object> variables);
}
```

## 6. 工作原理

### 6.1 模型调用流程

1. **创建提示**：构建发送给模型的提示
2. **模型调用**：通过客户端调用 AI 模型
3. **处理响应**：处理模型返回的响应
4. **返回结果**：将结果返回给用户

### 6.2 RAG 流程

1. **文档加载**：从各种源加载文档
2. **文本分块**：将文档分割成小块
3. **向量化**：使用嵌入模型将文本转换为向量
4. **存储向量**：将向量存储到向量数据库
5. **检索**：根据查询向量检索相关文本
6. **生成**：结合检索结果生成回答

## 7. 常见问题

### 7.1 模型选择

- **大语言模型**：选择适合任务的模型，如 GPT-3.5 适合一般任务，GPT-4 适合复杂任务
- **嵌入模型**：选择与大语言模型配套的嵌入模型，确保向量空间一致

### 7.2 性能优化

- **批处理**：批量处理多个请求，减少 API 调用次数
- **缓存**：缓存频繁使用的响应
- **异步处理**：使用异步方法处理长时间运行的任务

### 7.3 成本控制

- **令牌管理**：监控和控制令牌使用量
- **模型选择**：根据任务选择合适的模型，平衡成本和性能
- **提示优化**：优化提示，减少不必要的令牌使用

## 8. 总结

Spring AI 的基础概念包括模型、客户端、提示、响应和 RAG 等核心组件。通过这些概念，开发者可以轻松集成 AI 能力到 Spring 应用中，构建智能应用系统。

了解这些基础概念是使用 Spring AI 的第一步，后续章节将深入探讨各个组件的详细用法和最佳实践。