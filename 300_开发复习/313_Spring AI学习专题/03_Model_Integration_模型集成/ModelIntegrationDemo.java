package com.example.springai.model;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.embedding.EmbeddingResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Spring AI 模型集成示例
 */
@RestController
@RequestMapping("/model")
public class ModelIntegrationDemo {
    
    // 默认聊天客户端
    private final ChatClient defaultChatClient;
    
    // OpenAI 聊天客户端（如果配置）
    @Autowired(required = false)
    @Qualifier("openaiChatClient")
    private ChatClient openaiChatClient;
    
    // Hugging Face 聊天客户端（如果配置）
    @Autowired(required = false)
    @Qualifier("huggingFaceChatClient")
    private ChatClient huggingFaceChatClient;
    
    // 默认嵌入客户端
    private final EmbeddingClient defaultEmbeddingClient;
    
    @Autowired
    public ModelIntegrationDemo(ChatClient defaultChatClient, 
                               EmbeddingClient defaultEmbeddingClient) {
        this.defaultChatClient = defaultChatClient;
        this.defaultEmbeddingClient = defaultEmbeddingClient;
    }
    
    /**
     * 使用默认模型聊天
     */
    @GetMapping("/chat/default")
    public String defaultChat(@RequestParam String message) {
        return defaultChatClient.call(message);
    }
    
    /**
     * 使用 OpenAI 模型聊天（如果配置）
     */
    @GetMapping("/chat/openai")
    public String openaiChat(@RequestParam String message) {
        if (openaiChatClient != null) {
            return openaiChatClient.call(message);
        } else {
            return "OpenAI 模型未配置";
        }
    }
    
    /**
     * 使用 Hugging Face 模型聊天（如果配置）
     */
    @GetMapping("/chat/huggingface")
    public String huggingFaceChat(@RequestParam String message) {
        if (huggingFaceChatClient != null) {
            return huggingFaceChatClient.call(message);
        } else {
            return "Hugging Face 模型未配置";
        }
    }
    
    /**
     * 模型比较
     */
    @PostMapping("/chat/compare")
    public ModelComparisonResult compareModels(@RequestParam String message) {
        ModelComparisonResult result = new ModelComparisonResult();
        result.setMessage(message);
        
        // 使用默认模型
        result.setDefaultResponse(defaultChatClient.call(message));
        
        // 使用 OpenAI 模型（如果配置）
        if (openaiChatClient != null) {
            result.setOpenaiResponse(openaiChatClient.call(message));
        }
        
        // 使用 Hugging Face 模型（如果配置）
        if (huggingFaceChatClient != null) {
            result.setHuggingFaceResponse(huggingFaceChatClient.call(message));
        }
        
        return result;
    }
    
    /**
     * 使用默认嵌入模型
     */
    @GetMapping("/embed/default")
    public EmbeddingResponse defaultEmbed(@RequestParam String text) {
        return defaultEmbeddingClient.embed(text);
    }
    
    /**
     * 批量嵌入
     */
    @PostMapping("/embed/batch")
    public List<EmbeddingResponse> batchEmbed(@RequestBody List<String> texts) {
        return texts.stream()
            .map(defaultEmbeddingClient::embed)
            .toList();
    }
    
    /**
     * 高级聊天示例
     */
    @PostMapping("/chat/advanced")
    public ChatResponse advancedChat(@RequestBody List<Message> messages) {
        return defaultChatClient.chat(messages);
    }
}

/**
 * 模型比较结果类
 */
class ModelComparisonResult {
    private String message;
    private String defaultResponse;
    private String openaiResponse;
    private String huggingFaceResponse;
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public String getDefaultResponse() {
        return defaultResponse;
    }
    
    public void setDefaultResponse(String defaultResponse) {
        this.defaultResponse = defaultResponse;
    }
    
    public String getOpenaiResponse() {
        return openaiResponse;
    }
    
    public void setOpenaiResponse(String openaiResponse) {
        this.openaiResponse = openaiResponse;
    }
    
    public String getHuggingFaceResponse() {
        return huggingFaceResponse;
    }
    
    public void setHuggingFaceResponse(String huggingFaceResponse) {
        this.huggingFaceResponse = huggingFaceResponse;
    }
}

/**
 * 模型配置类
 */
// @Configuration
// public class ModelConfig {
//     
//     @Bean("openaiChatClient")
//     public ChatClient openaiChatClient(OpenAiChatModel openAiChatModel) {
//         return new ChatClient(openAiChatModel);
//     }
//     
//     @Bean("huggingFaceChatClient")
//     public ChatClient huggingFaceChatClient(HuggingFaceChatModel huggingFaceChatModel) {
//         return new ChatClient(huggingFaceChatModel);
//     }
//     
//     @Bean("openaiEmbeddingClient")
//     public EmbeddingClient openaiEmbeddingClient(OpenAiEmbeddingModel openAiEmbeddingModel) {
//         return new EmbeddingClient(openAiEmbeddingModel);
//     }
//     
//     @Bean("huggingFaceEmbeddingClient")
//     public EmbeddingClient huggingFaceEmbeddingClient(HuggingFaceEmbeddingModel huggingFaceEmbeddingModel) {
//         return new EmbeddingClient(huggingFaceEmbeddingModel);
//     }
// }
