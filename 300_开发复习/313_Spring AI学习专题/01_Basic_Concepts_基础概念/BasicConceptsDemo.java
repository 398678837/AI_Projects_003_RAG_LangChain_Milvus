package com.example.springai.basic;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.embedding.EmbeddingResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * Spring AI 基础概念示例
 */
@RestController
@RequestMapping("/basic")
public class BasicConceptsDemo {
    
    private final ChatClient chatClient;
    private final EmbeddingClient embeddingClient;
    
    @Autowired
    public BasicConceptsDemo(ChatClient chatClient, EmbeddingClient embeddingClient) {
        this.chatClient = chatClient;
        this.embeddingClient = embeddingClient;
    }
    
    /**
     * 简单聊天示例
     */
    @GetMapping("/chat/simple")
    public String simpleChat(@RequestParam String message) {
        return chatClient.call(message);
    }
    
    /**
     * 高级聊天示例
     */
    @PostMapping("/chat/advanced")
    public ChatResponse advancedChat(@RequestBody List<Message> messages) {
        return chatClient.chat(messages);
    }
    
    /**
     * 提示模板示例
     */
    @GetMapping("/prompt/template")
    public String promptTemplate(@RequestParam String topic) {
        String template = "请生成一篇关于 {topic} 的短文，长度约200字。";
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String prompt = promptTemplate.render(Map.of("topic", topic));
        return chatClient.call(prompt);
    }
    
    /**
     * 嵌入示例
     */
    @GetMapping("/embed")
    public EmbeddingResponse embed(@RequestParam String text) {
        return embeddingClient.embed(text);
    }
    
    /**
     * 批量嵌入示例
     */
    @PostMapping("/embed/batch")
    public EmbeddingResponse batchEmbed(@RequestBody List<String> texts) {
        return embeddingClient.embed(texts);
    }
    
    /**
     * 对话历史示例
     */
    @PostMapping("/chat/history")
    public ChatResponse chatWithHistory(@RequestBody List<Message> messages) {
        // 消息列表包含系统消息、用户消息和助手消息
        return chatClient.chat(messages);
    }
    
    /**
     * 简单的 RAG 示例（概念演示）
     */
    @GetMapping("/rag/simple")
    public String simpleRag(@RequestParam String question) {
        // 这里只是一个概念演示，实际 RAG 会涉及文档加载、向量存储等
        String context = "Spring AI 是 Spring 生态系统中的一个新框架，旨在简化人工智能应用的开发。"
                      + "它提供了一套统一的 API 和抽象，使开发者能够轻松集成各种 AI 模型和服务到 Spring 应用中。";
        
        String prompt = String.format("基于以下上下文回答问题：\n%s\n\n问题：%s", context, question);
        return chatClient.call(prompt);
    }
}

/**
 * 消息请求类
 */
class ChatRequest {
    private List<Message> messages;
    
    public List<Message> getMessages() {
        return messages;
    }
    
    public void setMessages(List<Message> messages) {
        this.messages = messages;
    }
}

/**
 * 应用配置类
 */
// @Configuration
// class AppConfig {
//     
//     @Bean
//     public ChatClient chatClient(OpenAiChatModel openAiChatModel) {
//         return new ChatClient(openAiChatModel);
//     }
//     
//     @Bean
//     public EmbeddingClient embeddingClient(OpenAiEmbeddingModel openAiEmbeddingModel) {
//         return new EmbeddingClient(openAiEmbeddingModel);
//     }
// }
