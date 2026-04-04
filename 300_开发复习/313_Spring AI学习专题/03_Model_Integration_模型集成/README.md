# Spring AI 模型集成

## 1. 模型集成概述

Spring AI 支持集成多种 AI 模型和服务提供商，为开发者提供了统一的接口来使用不同的模型。本章将介绍如何集成各种 AI 模型，包括 OpenAI、Hugging Face、Azure OpenAI 等。

## 2. 支持的模型提供商

### 2.1 OpenAI

OpenAI 提供了一系列强大的大语言模型，如 GPT-3.5、GPT-4 等。

**主要模型**：
- `gpt-3.5-turbo`：适用于一般任务
- `gpt-4`：适用于复杂任务
- `gpt-4-turbo`：更强大的版本
- `text-embedding-ada-002`：用于文本向量化

### 2.2 Hugging Face

Hugging Face 提供了丰富的开源模型，包括各种语言模型、嵌入模型等。

**主要模型**：
- `mistralai/Mixtral-8x7B-Instruct-v0.1`：混合专家模型
- `meta-llama/Llama-2-7b-chat-hf`：Llama 2 模型
- `sentence-transformers/all-MiniLM-L6-v2`：轻量级嵌入模型

### 2.3 Azure OpenAI

Azure OpenAI 是 Microsoft Azure 提供的 OpenAI 模型服务。

**主要模型**：
- `gpt-35-turbo`：Azure 版本的 GPT-3.5
- `gpt-4`：Azure 版本的 GPT-4
- `text-embedding-ada-002`：Azure 版本的嵌入模型

### 2.4 其他模型提供商

Spring AI 还支持其他模型提供商，如：
- **Cohere**：提供语言模型和嵌入模型
- **Anthropic**：提供 Claude 模型
- **Google**：提供 Gemini 模型

## 3. 模型集成配置

### 3.1 OpenAI 集成

#### 3.1.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.1.2 应用配置

```properties
# OpenAI API 密钥
spring.ai.openai.api-key=your-api-key

# 聊天模型配置
spring.ai.openai.chat.model=gpt-3.5-turbo
spring.ai.openai.chat.temperature=0.7
spring.ai.openai.chat.max-tokens=1000

# 嵌入模型配置
spring.ai.openai.embedding.model=text-embedding-ada-002
spring.ai.openai.embedding.dimensions=1536
```

### 3.2 Hugging Face 集成

#### 3.2.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-huggingface-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.2.2 应用配置

```properties
# Hugging Face API 密钥
spring.ai.huggingface.api-key=your-api-key

# 聊天模型配置
spring.ai.huggingface.chat.model=mistralai/Mixtral-8x7B-Instruct-v0.1

# 嵌入模型配置
spring.ai.huggingface.embedding.model=sentence-transformers/all-MiniLM-L6-v2
```

### 3.3 Azure OpenAI 集成

#### 3.3.1 依赖配置

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-azure-openai-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

#### 3.3.2 应用配置

```properties
# Azure OpenAI 端点
spring.ai.azure.openai.endpoint=https://your-resource.openai.azure.com/

# Azure OpenAI API 密钥
spring.ai.azure.openai.api-key=your-api-key

# 部署名称
spring.ai.azure.openai.chat.deployment-name=gpt-35-turbo
spring.ai.azure.openai.embedding.deployment-name=text-embedding-ada-002

# 模型配置
spring.ai.azure.openai.chat.temperature=0.7
```

## 4. 模型使用示例

### 4.1 OpenAI 模型使用

#### 4.1.1 聊天模型

```java
@RestController
public class OpenAIController {
    
    private final ChatClient chatClient;
    
    public OpenAIController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    @GetMapping("/openai/chat")
    public String chat(@RequestParam String message) {
        return chatClient.call(message);
    }
}
```

#### 4.1.2 嵌入模型

```java
@RestController
public class OpenAIEmbeddingController {
    
    private final EmbeddingClient embeddingClient;
    
    public OpenAIEmbeddingController(EmbeddingClient embeddingClient) {
        this.embeddingClient = embeddingClient;
    }
    
    @GetMapping("/openai/embed")
    public List<Double> embed(@RequestParam String text) {
        return embeddingClient.embed(text).getEmbedding();
    }
}
```

### 4.2 Hugging Face 模型使用

#### 4.2.1 聊天模型

```java
@RestController
public class HuggingFaceController {
    
    private final ChatClient chatClient;
    
    public HuggingFaceController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    @GetMapping("/huggingface/chat")
    public String chat(@RequestParam String message) {
        return chatClient.call(message);
    }
}
```

#### 4.2.2 嵌入模型

```java
@RestController
public class HuggingFaceEmbeddingController {
    
    private final EmbeddingClient embeddingClient;
    
    public HuggingFaceEmbeddingController(EmbeddingClient embeddingClient) {
        this.embeddingClient = embeddingClient;
    }
    
    @GetMapping("/huggingface/embed")
    public List<Double> embed(@RequestParam String text) {
        return embeddingClient.embed(text).getEmbedding();
    }
}
```

### 4.3 多模型集成

Spring AI 支持在同一个应用中集成多个模型，通过命名客户端来区分。

```java
@Configuration
public class ModelConfig {
    
    @Bean("openaiChatClient")
    public ChatClient openaiChatClient(OpenAiChatModel openAiChatModel) {
        return new ChatClient(openAiChatModel);
    }
    
    @Bean("huggingFaceChatClient")
    public ChatClient huggingFaceChatClient(HuggingFaceChatModel huggingFaceChatModel) {
        return new ChatClient(huggingFaceChatModel);
    }
}

@RestController
public class MultiModelController {
    
    private final ChatClient openaiChatClient;
    private final ChatClient huggingFaceChatClient;
    
    public MultiModelController(@Qualifier("openaiChatClient") ChatClient openaiChatClient, 
                               @Qualifier("huggingFaceChatClient") ChatClient huggingFaceChatClient) {
        this.openaiChatClient = openaiChatClient;
        this.huggingFaceChatClient = huggingFaceChatClient;
    }
    
    @GetMapping("/chat/openai")
    public String chatWithOpenAI(@RequestParam String message) {
        return openaiChatClient.call(message);
    }
    
    @GetMapping("/chat/huggingface")
    public String chatWithHuggingFace(@RequestParam String message) {
        return huggingFaceChatClient.call(message);
    }
}
```

## 5. 模型选择策略

### 5.1 根据任务选择模型

- **一般对话**：GPT-3.5 Turbo、Mixtral-8x7B
- **复杂任务**：GPT-4、Claude 3
- **代码生成**：GPT-4、CodeLlama
- **文本嵌入**：text-embedding-ada-002、all-MiniLM-L6-v2

### 5.2 根据性能选择模型

- **响应速度**：较小的模型如 GPT-3.5 Turbo、Mixtral-8x7B
- **生成质量**：较大的模型如 GPT-4、Claude 3
- **成本效益**：开源模型如 Llama 2、Mixtral

### 5.3 根据部署方式选择模型

- **云服务**：OpenAI、Azure OpenAI、Google Gemini
- **本地部署**：开源模型如 Llama 2、Mixtral
- **混合部署**：关键任务使用云服务，一般任务使用本地模型

## 6. 模型集成最佳实践

### 6.1 模型配置管理

- **环境变量**：使用环境变量存储 API 密钥
- **配置文件**：使用不同环境的配置文件
- **密钥管理**：使用 Spring Cloud Config 或 Vault 管理密钥

### 6.2 模型调用优化

- **批处理**：批量处理多个请求
- **缓存**：缓存频繁使用的响应
- **异步处理**：使用异步方法处理长时间运行的任务
- **超时设置**：合理设置请求超时时间

### 6.3 错误处理

- **异常捕获**：捕获模型调用可能的异常
- **重试机制**：对临时错误实现重试机制
- **降级策略**：当模型不可用时提供降级方案
- **监控**：监控模型调用的成功率和响应时间

### 6.4 模型评估

- **性能评估**：评估模型的响应速度和生成质量
- **成本评估**：评估模型使用的成本
- **效果评估**：评估模型在特定任务上的表现

## 7. 常见问题及解决方案

### 7.1 API 密钥管理

**问题**：API 密钥泄露
**解决方案**：使用环境变量、密钥管理服务，避免硬编码 API 密钥

### 7.2 模型响应时间长

**问题**：模型响应时间过长，影响用户体验
**解决方案**：使用异步处理、设置合理的超时时间、选择响应速度快的模型

### 7.3 模型输出质量不稳定

**问题**：模型输出质量时好时坏
**解决方案**：优化提示、使用更适合任务的模型、实现输出验证

### 7.4 成本控制

**问题**：模型使用成本过高
**解决方案**：监控使用量、设置使用限额、选择成本效益高的模型

## 8. 总结

Spring AI 提供了统一的接口来集成各种 AI 模型，使开发者能够轻松使用不同的模型服务。通过合理配置和使用这些模型，可以构建各种智能应用，如智能客服、内容生成、知识库系统等。

在实际开发中，应根据具体需求选择合适的模型，遵循最佳实践，优化模型调用，确保应用的性能和可靠性。随着 AI 技术的不断发展，Spring AI 也在持续更新，支持更多的模型和功能，为开发者提供更好的开发体验。