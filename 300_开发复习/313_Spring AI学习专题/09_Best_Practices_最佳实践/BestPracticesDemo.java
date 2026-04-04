package com.example.springai.bestpractices;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.ai.vectorstore.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

/**
 * Spring AI 最佳实践示例
 */
@RestController
@RequestMapping("/best-practices")
public class BestPracticesDemo {
    
    private final ChatClient chatClient;
    private final EmbeddingClient embeddingClient;
    private final VectorStore vectorStore;
    private final PromptTemplateLibrary promptTemplateLibrary;
    private final RAGService ragService;
    
    @Autowired
    public BestPracticesDemo(ChatClient chatClient, 
                           EmbeddingClient embeddingClient, 
                           VectorStore vectorStore, 
                           PromptTemplateLibrary promptTemplateLibrary, 
                           RAGService ragService) {
        this.chatClient = chatClient;
        this.embeddingClient = embeddingClient;
        this.vectorStore = vectorStore;
        this.promptTemplateLibrary = promptTemplateLibrary;
        this.ragService = ragService;
    }
    
    /**
     * 异步处理示例
     */
    @GetMapping("/async")
    public CompletableFuture<String> asyncChat(@RequestParam String message) {
        return CompletableFuture.supplyAsync(() -> {
            try {
                return chatClient.call(message);
            } catch (Exception e) {
                throw new RuntimeException("Chat failed", e);
            }
        });
    }
    
    /**
     * 提示模板库示例
     */
    @GetMapping("/prompt/template")
    public String usePromptTemplate(@RequestParam String templateName, 
                                   @RequestParam Map<String, String> params) {
        PromptTemplate template = promptTemplateLibrary.getTemplate(templateName);
        String prompt = template.render(params);
        return chatClient.call(prompt);
    }
    
    /**
     * 批量处理示例
     */
    @PostMapping("/batch")
    public List<String> batchProcess(@RequestBody List<String> messages) {
        return messages.parallelStream()
            .map(chatClient::call)
            .toList();
    }
    
    /**
     * RAG 最佳实践示例
     */
    @GetMapping("/rag")
    public RAGResponse ragBestPractice(@RequestParam String question) {
        return ragService.processQuery(question);
    }
    
    /**
     * 文档索引最佳实践
     */
    @PostMapping("/document/index")
    public String indexDocument(@RequestBody DocumentRequest documentRequest) {
        // 1. 文本分块
        List<String> chunks = TextChunker.smartChunkText(documentRequest.getContent(), 1000);
        
        // 2. 创建文档
        List<Document> documents = chunks.stream()
            .map(chunk -> new Document(chunk, documentRequest.getMetadata()))
            .toList();
        
        // 3. 批量添加到向量存储
        vectorStore.add(documents);
        
        return "文档已成功索引，共 " + chunks.size() + " 个块";
    }
    
    /**
     * 错误处理示例
     */
    @GetMapping("/error-handling")
    public String errorHandling(@RequestParam String message) {
        try {
            return chatClient.call(message);
        } catch (Exception e) {
            // 记录错误
            System.err.println("Chat error: " + e.getMessage());
            // 返回友好的错误消息
            return "处理请求时出错，请稍后重试";
        }
    }
    
    /**
     * 多模型集成示例
     */
    @GetMapping("/multi-model")
    public Map<String, String> multiModel(@RequestParam String message, 
                                        @RequestParam String modelType) {
        // 根据模型类型选择不同的客户端
        ChatClient selectedClient = chatClient; // 默认客户端
        
        // 这里可以根据modelType选择不同的客户端
        // if ("openai".equals(modelType)) {
        //     selectedClient = openaiChatClient;
        // } else if ("huggingface".equals(modelType)) {
        //     selectedClient = huggingFaceChatClient;
        // }
        
        String response = selectedClient.call(message);
        return Map.of(
            "modelType", modelType,
            "response", response
        );
    }
}

/**
 * 提示模板库
 */
class PromptTemplateLibrary {
    
    private final Map<String, String> templates = Map.of(
        "summary", "请总结以下文本，保持核心信息，长度不超过{length}字：\n\n{text}",
        "qa", "基于以下上下文回答问题：\n\n{context}\n\n问题：{question}",
        "classification", "请将以下文本分类到以下类别之一：{categories}\n\n文本：{text}\n\n分类：",
        "translation", "请将以下{source_language}文本翻译成{target_language}：\n\n{text}",
        "code", "请为以下需求编写{language}代码：\n{requirement}\n\n要求：\n1. 代码结构清晰，有注释\n2. 处理边界情况\n3. 遵循最佳实践"
    );
    
    public PromptTemplate getTemplate(String name) {
        String template = templates.get(name);
        if (template == null) {
            throw new IllegalArgumentException("Template not found: " + name);
        }
        return PromptTemplate.create(template);
    }
}

/**
 * RAG 服务
 */
class RAGService {
    
    private final VectorStore vectorStore;
    private final ChatClient chatClient;
    
    public RAGService(VectorStore vectorStore, ChatClient chatClient) {
        this.vectorStore = vectorStore;
        this.chatClient = chatClient;
    }
    
    public RAGResponse processQuery(String question) {
        // 1. 检索相关文档
        List<Document> documents = vectorStore.search(question, 3);
        
        // 2. 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            if (doc.getMetadata() != null && doc.getMetadata().containsKey("source")) {
                context.append("Source: " + doc.getMetadata().get("source") + "\n");
            }
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 3. 构建提示
        String prompt = "基于以下上下文回答问题，保持回答准确、简洁：\n\n" +
                      context.toString() + "\n" +
                      "问题：" + question;
        
        // 4. 调用模型
        String answer = chatClient.call(prompt);
        
        // 5. 构建响应
        RAGResponse response = new RAGResponse();
        response.setQuestion(question);
        response.setAnswer(answer);
        response.setRetrievedDocuments(documents);
        
        return response;
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

/**
 * RAG 响应类
 */
class RAGResponse {
    private String question;
    private String answer;
    private List<Document> retrievedDocuments;
    
    public String getQuestion() {
        return question;
    }
    
    public void setQuestion(String question) {
        this.question = question;
    }
    
    public String getAnswer() {
        return answer;
    }
    
    public void setAnswer(String answer) {
        this.answer = answer;
    }
    
    public List<Document> getRetrievedDocuments() {
        return retrievedDocuments;
    }
    
    public void setRetrievedDocuments(List<Document> retrievedDocuments) {
        this.retrievedDocuments = retrievedDocuments;
    }
}

/**
 * 文本分块工具类
 */
class TextChunker {
    
    /**
     * 智能分块，基于段落
     */
    public static List<String> smartChunkText(String text, int maxChunkSize) {
        List<String> chunks = new ArrayList<>();
        String[] paragraphs = text.split("\\n\\s*\\n");
        
        StringBuilder currentChunk = new StringBuilder();
        for (String paragraph : paragraphs) {
            if (currentChunk.length() + paragraph.length() <= maxChunkSize) {
                currentChunk.append(paragraph).append("\n\n");
            } else {
                if (currentChunk.length() > 0) {
                    chunks.add(currentChunk.toString().trim());
                    currentChunk = new StringBuilder();
                }
                
                // 如果单个段落超过最大块大小，进一步分割
                if (paragraph.length() > maxChunkSize) {
                    List<String> subChunks = chunkText(paragraph, maxChunkSize, 100);
                    chunks.addAll(subChunks);
                } else {
                    currentChunk.append(paragraph).append("\n\n");
                }
            }
        }
        
        if (currentChunk.length() > 0) {
            chunks.add(currentChunk.toString().trim());
        }
        
        return chunks;
    }
    
    /**
     * 将文本分割成小块
     */
    public static List<String> chunkText(String text, int chunkSize, int overlap) {
        List<String> chunks = new ArrayList<>();
        int textLength = text.length();
        
        for (int i = 0; i < textLength; i += chunkSize - overlap) {
            int end = Math.min(i + chunkSize, textLength);
            chunks.add(text.substring(i, end));
        }
        
        return chunks;
    }
}
