# Spring AI 核心组件

## 1. 核心组件概述

Spring AI 提供了一系列核心组件，用于构建 AI 应用。这些组件相互协作，形成了一个完整的 AI 应用开发框架。

## 2. 核心组件详解

### 2.1 模型（Model）

模型是 Spring AI 的核心抽象，代表一个 AI 模型的能力。

#### 2.1.1 ChatModel

`ChatModel` 接口定义了与大语言模型交互的方法：

```java
public interface ChatModel {
    ChatResponse call(ChatRequest request);
}
```

**实现类**：
- `OpenAiChatModel`：OpenAI 模型实现
- `HuggingFaceChatModel`：Hugging Face 模型实现
- `AzureOpenAiChatModel`：Azure OpenAI 模型实现

#### 2.1.2 EmbeddingModel

`EmbeddingModel` 接口定义了文本向量化的方法：

```java
public interface EmbeddingModel {
    EmbeddingResponse embed(EmbeddingRequest request);
}
```

**实现类**：
- `OpenAiEmbeddingModel`：OpenAI 嵌入模型实现
- `HuggingFaceEmbeddingModel`：Hugging Face 嵌入模型实现
- `AzureOpenAiEmbeddingModel`：Azure OpenAI 嵌入模型实现

### 2.2 客户端（Client）

客户端提供了与模型交互的高级接口，简化了模型调用。

#### 2.2.1 ChatClient

`ChatClient` 是与大语言模型交互的主要接口：

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

**主要方法**：
- `call(String)`：发送简单文本消息并返回响应
- `chat(List<Message>)`：发送消息列表（包含系统消息、用户消息等）
- `chat(List<Message>, ChatOptions)`：带选项的消息发送

#### 2.2.2 EmbeddingClient

`EmbeddingClient` 用于文本向量化：

```java
public interface EmbeddingClient {
    // 嵌入单个文本
    EmbeddingResponse embed(String text);
    
    // 嵌入多个文本
    EmbeddingResponse embed(List<String> texts);
}
```

**主要方法**：
- `embed(String)`：嵌入单个文本
- `embed(List<String>)`：批量嵌入多个文本

### 2.3 消息（Message）

消息是与模型交互的基本单位，有多种类型。

#### 2.3.1 消息类型

- `UserMessage`：用户发送的消息
- `AssistantMessage`：助手（模型）的响应
- `SystemMessage`：系统消息，用于设置上下文和指令
- `ToolMessage`：工具调用的消息

#### 2.3.2 消息构建

```java
// 创建用户消息
Message userMessage = new UserMessage("你好，Spring AI！");

// 创建系统消息
Message systemMessage = new SystemMessage("你是一个 helpful 的助手。");

// 创建助手消息
Message assistantMessage = new AssistantMessage("你好！我是基于 Spring AI 的助手。");
```

### 2.4 提示（Prompt）

提示是发送给模型的输入，包含指令、上下文和问题。

#### 2.4.1 PromptTemplate

`PromptTemplate` 用于创建结构化的提示：

```java
// 创建提示模板
String template = "请生成一篇关于 {topic} 的短文，长度约200字。";
PromptTemplate promptTemplate = PromptTemplate.create(template);

// 渲染提示
String prompt = promptTemplate.render(Map.of("topic", "Spring AI"));
```

#### 2.4.2 Prompt

`Prompt` 类包含完整的提示信息：

```java
// 创建提示
Prompt prompt = new Prompt(
    "请生成一篇关于 Spring AI 的短文",
    List.of(new SystemMessage("你是一个专业的技术作家。"))
);
```

### 2.5 响应（Response）

响应是模型的输出，包含生成的内容。

#### 2.5.1 ChatResponse

`ChatResponse` 包含大语言模型的响应：

```java
// 获取响应
ChatResponse response = chatClient.chat(messages);

// 获取生成的消息
Message generatedMessage = response.getResult().getOutput();

// 获取生成的文本
String text = generatedMessage.getContent();
```

#### 2.5.2 EmbeddingResponse

`EmbeddingResponse` 包含嵌入模型的响应：

```java
// 获取响应
EmbeddingResponse response = embeddingClient.embed("Spring AI");

// 获取向量
List<Double> embedding = response.getEmbedding();
```

### 2.6 向量存储（Vector Store）

向量存储用于存储和检索文本的向量表示。

#### 2.6.1 VectorStore

`VectorStore` 接口定义了向量存储的基本操作：

```java
public interface VectorStore {
    // 添加文档
    void add(List<Document> documents);
    
    // 搜索
    List<Document> search(String query, int k);
    
    // 删除
    void delete(List<String> ids);
}
```

**实现类**：
- `PgVectorStore`：PostgreSQL 向量存储
- `MilvusVectorStore`：Milvus 向量存储
- `ChromaVectorStore`：Chroma 向量存储
- `FAISSVectorStore`：FAISS 向量存储

### 2.7 文档（Document）

文档是 RAG 系统中的基本单位，包含文本内容和元数据。

```java
// 创建文档
Document document = new Document(
    "Spring AI 是 Spring 生态系统中的一个新框架...",
    Map.of("source", "spring.io", "category", "technology")
);
```

### 2.8 检索器（Retriever）

检索器用于从向量存储中检索相关文档。

```java
// 创建检索器
VectorStoreRetriever retriever = new VectorStoreRetriever(vectorStore, 5);

// 检索相关文档
List<Document> documents = retriever.retrieve("Spring AI 是什么？");
```

### 2.9 工具（Tool）

工具允许模型调用外部功能，如查询数据库、调用 API 等。

```java
// 创建工具
Tool tool = new Tool(
    "weather",
    "获取指定城市的天气信息",
    Map.of("city", "城市名称"),
    parameters -> {
        String city = parameters.get("city").toString();
        return "北京市的天气：晴，25°C";
    }
);

// 将工具添加到聊天选项
ChatOptions options = ChatOptions.builder()
    .tools(List.of(tool))
    .build();
```

## 3. 组件协作

### 3.1 聊天流程

1. **创建消息**：构建用户消息、系统消息等
2. **调用模型**：通过 ChatClient 调用模型
3. **处理响应**：处理模型返回的响应
4. **返回结果**：将结果返回给用户

### 3.2 RAG 流程

1. **文档加载**：从各种源加载文档
2. **文本分块**：将文档分割成小块
3. **向量化**：使用 EmbeddingClient 将文本转换为向量
4. **存储向量**：将向量存储到 VectorStore
5. **检索**：根据查询向量检索相关文档
6. **生成**：结合检索结果生成回答

## 4. 配置和使用

### 4.1 依赖配置

```xml
<!-- 核心依赖 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-core</artifactId>
    <version>0.8.1</version>
</dependency>

<!-- OpenAI 集成 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>

<!-- 向量存储集成 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-pgvector-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

### 4.2 应用配置

```properties
# OpenAI 配置
spring.ai.openai.api-key=your-api-key
spring.ai.openai.chat.model=gpt-3.5-turbo
spring.ai.openai.chat.temperature=0.7
spring.ai.openai.embedding.model=text-embedding-ada-002

# 向量存储配置
spring.ai.vectorstore.pgvector.connection-string=jdbc:postgresql://localhost:5432/vector_db
spring.ai.vectorstore.pgvector.username=postgres
spring.ai.vectorstore.pgvector.password=postgres
```

### 4.3 组件注入

```java
@RestController
public class AIController {
    
    private final ChatClient chatClient;
    private final EmbeddingClient embeddingClient;
    private final VectorStore vectorStore;
    
    @Autowired
    public AIController(ChatClient chatClient, 
                       EmbeddingClient embeddingClient, 
                       VectorStore vectorStore) {
        this.chatClient = chatClient;
        this.embeddingClient = embeddingClient;
        this.vectorStore = vectorStore;
    }
    
    // 控制器方法
}
```

## 5. 最佳实践

### 5.1 组件使用建议

- **ChatClient**：用于与大语言模型交互，处理对话、问答等任务
- **EmbeddingClient**：用于文本向量化，支持语义搜索、相似度计算等
- **VectorStore**：用于存储向量，支持 RAG 系统
- **PromptTemplate**：用于创建结构化提示，提高模型输出质量

### 5.2 性能优化

- **批量处理**：使用批量方法减少 API 调用次数
- **缓存**：缓存频繁使用的响应和向量
- **异步处理**：使用异步方法处理长时间运行的任务
- **适当的批大小**：根据模型和任务选择合适的批大小

### 5.3 错误处理

- **异常捕获**：捕获模型调用可能的异常
- **重试机制**：对临时错误实现重试机制
- **降级策略**：当模型不可用时提供降级方案

## 6. 总结

Spring AI 的核心组件提供了构建 AI 应用的基础功能，包括模型交互、文本向量化、向量存储等。通过这些组件，开发者可以轻松构建各种 AI 应用，如智能客服、内容生成、知识库系统等。

了解这些核心组件的功能和使用方法，是掌握 Spring AI 的关键。在实际开发中，应根据具体需求选择合适的组件，并遵循最佳实践，构建高质量的 AI 应用。