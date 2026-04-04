package com.example.springai.core;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.options.ChatOptions;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.embedding.EmbeddingResponse;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.ai.vectorstore.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * Spring AI 核心组件示例
 */
@RestController
@RequestMapping("/core")
public class CoreComponentsDemo {
    
    private final ChatClient chatClient;
    private final EmbeddingClient embeddingClient;
    private final VectorStore vectorStore;
    
    @Autowired
    public CoreComponentsDemo(ChatClient chatClient, 
                             EmbeddingClient embeddingClient, 
                             VectorStore vectorStore) {
        this.chatClient = chatClient;
        this.embeddingClient = embeddingClient;
        this.vectorStore = vectorStore;
    }
    
    /**
     * 消息类型示例
     */
    @PostMapping("/messages")
    public ChatResponse messagesDemo(@RequestBody List<Message> messages) {
        return chatClient.chat(messages);
    }
    
    /**
     * 系统消息示例
     */
    @GetMapping("/system-message")
    public String systemMessageDemo(@RequestParam String query) {
        List<Message> messages = List.of(
            new SystemMessage("你是一个专业的 Java 开发者，擅长解答 Spring 相关问题。"),
            new UserMessage(query)
        );
        return chatClient.chat(messages).getResult().getOutput().getContent();
    }
    
    /**
     * 提示模板示例
     */
    @PostMapping("/prompt-template")
    public String promptTemplateDemo(@RequestBody Map<String, Object> variables) {
        String template = "请生成一个关于 {topic} 的 {format}，长度约 {length} 字。";
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String promptText = promptTemplate.render(variables);
        
        List<Message> messages = List.of(
            new SystemMessage("你是一个专业的内容创作者。"),
            new UserMessage(promptText)
        );
        
        return chatClient.chat(messages).getResult().getOutput().getContent();
    }
    
    /**
     * 聊天选项示例
     */
    @GetMapping("/chat-options")
    public String chatOptionsDemo(@RequestParam String message) {
        ChatOptions options = ChatOptions.builder()
            .temperature(0.3)  // 降低随机性
            .maxTokens(500)     // 限制响应长度
            .build();
        
        List<Message> messages = List.of(new UserMessage(message));
        return chatClient.chat(messages, options).getResult().getOutput().getContent();
    }
    
    /**
     * 向量存储示例
     */
    @PostMapping("/vector-store/add")
    public String addToVectorStore(@RequestBody List<Document> documents) {
        vectorStore.add(documents);
        return "文档已添加到向量存储";
    }
    
    /**
     * 向量存储搜索示例
     */
    @GetMapping("/vector-store/search")
    public List<Document> searchVectorStore(@RequestParam String query, 
                                          @RequestParam(defaultValue = "5") int k) {
        return vectorStore.search(query, k);
    }
    
    /**
     * 完整的 RAG 流程示例
     */
    @GetMapping("/rag")
    public String ragDemo(@RequestParam String question) {
        // 1. 从向量存储中检索相关文档
        List<Document> documents = vectorStore.search(question, 3);
        
        // 2. 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 3. 构建提示
        String promptTemplate = "基于以下上下文回答问题：\n\n%s\n\n问题：%s";
        String prompt = String.format(promptTemplate, context.toString(), question);
        
        // 4. 调用模型
        List<Message> messages = List.of(
            new SystemMessage("你是一个专业的助手，基于提供的上下文回答问题。"),
            new UserMessage(prompt)
        );
        
        return chatClient.chat(messages).getResult().getOutput().getContent();
    }
    
    /**
     * 嵌入模型使用示例
     */
    @PostMapping("/embedding")
    public List<EmbeddingResponse> embeddingDemo(@RequestBody List<String> texts) {
        return texts.stream()
            .map(embeddingClient::embed)
            .toList();
    }
    
    /**
     * 文档创建示例
     */
    @PostMapping("/document/create")
    public Document createDocument(@RequestBody Map<String, Object> data) {
        String content = (String) data.get("content");
        Map<String, Object> metadata = (Map<String, Object>) data.get("metadata");
        
        Document document = new Document(content, metadata);
        vectorStore.add(List.of(document));
        
        return document;
    }
}

/**
 * 文档请求类
 */
class DocumentRequest {
    private String content;
    private Map<String, Object> metadata;
    
    public String getContent() {
        return content;
    }
    
    public void setContent(String content) {
        this.content = content;
    }
    
    public Map<String, Object> getMetadata() {
        return metadata;
    }
    
    public void setMetadata(Map<String, Object> metadata) {
        this.metadata = metadata;
    }
}
