package com.example.springai.realworld;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.ai.vectorstore.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Spring AI 实战应用示例
 */
@RestController
@RequestMapping("/real-world")
public class RealWorldDemo {
    
    private final ChatClient chatClient;
    private final VectorStore vectorStore;
    private final Map<String, List<Message>> conversations = new ConcurrentHashMap<>();
    
    @Autowired
    public RealWorldDemo(ChatClient chatClient, VectorStore vectorStore) {
        this.chatClient = chatClient;
        this.vectorStore = vectorStore;
    }
    
    // ==================== 智能客服系统 ====================
    
    /**
     * 智能客服对话
     */
    @PostMapping("/chatbot/chat")
    public ChatResponse chatbot(@RequestBody ChatRequest request) {
        // 获取或创建对话历史
        List<Message> conversation = conversations.computeIfAbsent(
            request.getConversationId(), k -> new ArrayList<>());
        
        // 添加用户消息
        conversation.add(new Message("user", request.getMessage()));
        
        // 检索相关知识
        List<Document> documents = vectorStore.search(request.getMessage(), 3);
        
        // 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 构建提示
        String prompt = "基于以下上下文和对话历史回答用户问题：\n\n" +
                      context.toString() + "\n" +
                      "对话历史：" + conversation.stream()
                          .map(m -> m.getRole() + ": " + m.getContent())
                          .collect(Collectors.joining("\n")) + "\n" +
                      "用户问题：" + request.getMessage();
        
        // 调用模型
        String response = chatClient.call(prompt);
        
        // 添加助手消息
        conversation.add(new Message("assistant", response));
        
        // 限制对话历史长度
        if (conversation.size() > 20) {
            conversation = conversation.subList(conversation.size() - 20, conversation.size());
            conversations.put(request.getConversationId(), conversation);
        }
        
        return new ChatResponse(response);
    }
    
    /**
     * 上传知识库
     */
    @PostMapping("/chatbot/upload")
    public String uploadKnowledge(@RequestParam("file") MultipartFile file) {
        try {
            // 读取文件内容
            String content = new String(file.getBytes());
            
            // 文本分块
            List<String> chunks = TextChunker.smartChunkText(content, 1000);
            
            // 创建文档
            List<Document> documents = chunks.stream()
                .map(chunk -> new Document(chunk, Map.of(
                    "source", file.getOriginalFilename(),
                    "uploadTime", LocalDateTime.now().toString()
                )))
                .toList();
            
            // 存储到向量数据库
            vectorStore.add(documents);
            
            return "知识库上传成功，共 " + chunks.size() + " 个块";
        } catch (IOException e) {
            return "知识库上传失败：" + e.getMessage();
        }
    }
    
    // ==================== 内容生成系统 ====================
    
    /**
     * 生成文章
     */
    @PostMapping("/content/generate/article")
    public String generateArticle(@RequestBody ArticleRequest request) {
        String prompt = "请生成一篇关于 \"" + request.getTopic() + "\" 的文章，" +
                      "长度约 " + request.getLength() + " 字，" +
                      "风格为 " + request.getStyle() + "。" +
                      "要求内容结构清晰，逻辑连贯，信息准确。";
        return chatClient.call(prompt);
    }
    
    /**
     * 生成报告
     */
    @PostMapping("/content/generate/report")
    public String generateReport(@RequestBody ReportRequest request) {
        String prompt = "基于以下数据生成一份报告：\n" +
                      request.getData() + "\n" +
                      "报告模板：" + request.getTemplate() + "\n" +
                      "要求报告结构清晰，数据准确，分析深入。";
        return chatClient.call(prompt);
    }
    
    /**
     * 优化内容
     */
    @PostMapping("/content/optimize")
    public String optimizeContent(@RequestBody OptimizeRequest request) {
        String prompt = "请优化以下内容，使其风格符合 \"" + request.getTargetStyle() + "\"：\n" +
                      request.getContent() + "\n" +
                      "要求保持原意，提高表达质量。";
        return chatClient.call(prompt);
    }
    
    // ==================== 知识库系统 ====================
    
    /**
     * 上传文档到知识库
     */
    @PostMapping("/knowledge/upload")
    public String uploadDocument(@RequestParam("file") MultipartFile file) {
        try {
            // 读取文件内容
            String content = new String(file.getBytes());
            
            // 文本分块
            List<String> chunks = TextChunker.smartChunkText(content, 1000);
            
            // 创建文档
            List<Document> documents = chunks.stream()
                .map(chunk -> new Document(chunk, Map.of(
                    "source", file.getOriginalFilename(),
                    "uploadTime", LocalDateTime.now().toString()
                )))
                .toList();
            
            // 存储到向量数据库
            vectorStore.add(documents);
            
            return "文档上传成功，共 " + chunks.size() + " 个块";
        } catch (IOException e) {
            return "文档上传失败：" + e.getMessage();
        }
    }
    
    /**
     * 知识库搜索
     */
    @GetMapping("/knowledge/search")
    public List<Document> searchKnowledge(@RequestParam String query, 
                                        @RequestParam(defaultValue = "5") int k) {
        return vectorStore.search(query, k);
    }
    
    /**
     * 知识库问答
     */
    @GetMapping("/knowledge/qa")
    public String askKnowledge(@RequestParam String question) {
        // 检索相关文档
        List<Document> documents = vectorStore.search(question, 3);
        
        // 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append("Source: " + doc.getMetadata().get("source") + "\n");
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 构建提示
        String prompt = "基于以下上下文回答问题，保持回答准确、简洁：\n\n" +
                      context.toString() + "\n" +
                      "问题：" + question;
        
        // 调用模型
        return chatClient.call(prompt);
    }
    
    // ==================== 语义搜索系统 ====================
    
    /**
     * 语义搜索
     */
    @GetMapping("/search/semantic")
    public List<SearchResult> semanticSearch(@RequestParam String query, 
                                           @RequestParam(defaultValue = "10") int k) {
        // 搜索相关文档
        List<Document> documents = vectorStore.search(query, k);
        
        // 转换为搜索结果
        return documents.stream()
            .map(doc -> {
                SearchResult result = new SearchResult();
                result.setContent(doc.getContent());
                result.setMetadata(doc.getMetadata());
                result.setScore(0.0); // 简化处理
                return result;
            })
            .toList();
    }
    
    /**
     * 搜索建议
     */
    @GetMapping("/search/suggest")
    public List<String> getSearchSuggestions(@RequestParam String query) {
        // 使用模型生成搜索建议
        String prompt = "基于以下查询生成5个相关的搜索建议：\n" + query;
        String response = chatClient.call(prompt);
        
        // 解析响应
        return Arrays.stream(response.split("\\n"))
            .filter(s -> !s.isEmpty())
            .map(s -> s.replaceAll("^\\d+\\.\\s*", ""))
            .limit(5)
            .toList();
    }
    
    // ==================== 代码辅助系统 ====================
    
    /**
     * 生成代码
     */
    @PostMapping("/code/generate")
    public String generateCode(@RequestBody CodeRequest request) {
        String prompt = "请为以下需求编写 " + request.getLanguage() + " 代码：\n" +
                      request.getRequirement() + "\n" +
                      "要求：\n" +
                      "1. 代码结构清晰，有注释\n" +
                      "2. 处理边界情况\n" +
                      "3. 遵循最佳实践\n" +
                      "4. 提供测试用例";
        return chatClient.call(prompt);
    }
    
    /**
     * 优化代码
     */
    @PostMapping("/code/optimize")
    public String optimizeCode(@RequestBody OptimizeCodeRequest request) {
        String prompt = "请优化以下 " + request.getLanguage() + " 代码：\n" +
                      request.getCode() + "\n" +
                      "要求：\n" +
                      "1. 提高代码性能\n" +
                      "2. 改善代码可读性\n" +
                      "3. 修复潜在问题\n" +
                      "4. 遵循最佳实践";
        return chatClient.call(prompt);
    }
    
    /**
     * 解释代码
     */
    @PostMapping("/code/explain")
    public String explainCode(@RequestBody ExplainCodeRequest request) {
        String prompt = "请解释以下 " + request.getLanguage() + " 代码的功能和逻辑：\n" +
                      request.getCode() + "\n" +
                      "要求：\n" +
                      "1. 解释代码的整体功能\n" +
                      "2. 分析关键部分的逻辑\n" +
                      "3. 说明使用的技术和设计模式\n" +
                      "4. 指出潜在的问题或改进空间";
        return chatClient.call(prompt);
    }
}

// 辅助类
class Message {
    private String role;
    private String content;
    
    public Message(String role, String content) {
        this.role = role;
        this.content = content;
    }
    
    public String getRole() {
        return role;
    }
    
    public void setRole(String role) {
        this.role = role;
    }
    
    public String getContent() {
        return content;
    }
    
    public void setContent(String content) {
        this.content = content;
    }
}

class ChatRequest {
    private String message;
    private String conversationId;
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public String getConversationId() {
        return conversationId;
    }
    
    public void setConversationId(String conversationId) {
        this.conversationId = conversationId;
    }
}

class ChatResponse {
    private String response;
    
    public ChatResponse(String response) {
        this.response = response;
    }
    
    public String getResponse() {
        return response;
    }
    
    public void setResponse(String response) {
        this.response = response;
    }
}

class ArticleRequest {
    private String topic;
    private int length;
    private String style;
    
    public String getTopic() {
        return topic;
    }
    
    public void setTopic(String topic) {
        this.topic = topic;
    }
    
    public int getLength() {
        return length;
    }
    
    public void setLength(int length) {
        this.length = length;
    }
    
    public String getStyle() {
        return style;
    }
    
    public void setStyle(String style) {
        this.style = style;
    }
}

class ReportRequest {
    private String data;
    private String template;
    
    public String getData() {
        return data;
    }
    
    public void setData(String data) {
        this.data = data;
    }
    
    public String getTemplate() {
        return template;
    }
    
    public void setTemplate(String template) {
        this.template = template;
    }
}

class OptimizeRequest {
    private String content;
    private String targetStyle;
    
    public String getContent() {
        return content;
    }
    
    public void setContent(String content) {
        this.content = content;
    }
    
    public String getTargetStyle() {
        return targetStyle;
    }
    
    public void setTargetStyle(String targetStyle) {
        this.targetStyle = targetStyle;
    }
}

class SearchResult {
    private String content;
    private Map<String, Object> metadata;
    private double score;
    
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
    
    public double getScore() {
        return score;
    }
    
    public void setScore(double score) {
        this.score = score;
    }
}

class CodeRequest {
    private String requirement;
    private String language;
    
    public String getRequirement() {
        return requirement;
    }
    
    public void setRequirement(String requirement) {
        this.requirement = requirement;
    }
    
    public String getLanguage() {
        return language;
    }
    
    public void setLanguage(String language) {
        this.language = language;
    }
}

class OptimizeCodeRequest {
    private String code;
    private String language;
    
    public String getCode() {
        return code;
    }
    
    public void setCode(String code) {
        this.code = code;
    }
    
    public String getLanguage() {
        return language;
    }
    
    public void setLanguage(String language) {
        this.language = language;
    }
}

class ExplainCodeRequest {
    private String code;
    private String language;
    
    public String getCode() {
        return code;
    }
    
    public void setCode(String code) {
        this.code = code;
    }
    
    public String getLanguage() {
        return language;
    }
    
    public void setLanguage(String language) {
        this.language = language;
    }
}

class TextChunker {
    
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
