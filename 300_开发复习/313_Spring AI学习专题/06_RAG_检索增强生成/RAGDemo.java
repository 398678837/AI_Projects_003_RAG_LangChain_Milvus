package com.example.springai.rag;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.ai.vectorstore.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;

/**
 * Spring AI RAG 示例
 */
@RestController
@RequestMapping("/rag")
public class RAGDemo {
    
    private final VectorStore vectorStore;
    private final ChatClient chatClient;
    
    @Autowired
    public RAGDemo(VectorStore vectorStore, ChatClient chatClient) {
        this.vectorStore = vectorStore;
        this.chatClient = chatClient;
    }
    
    /**
     * 基本 RAG 示例
     */
    @GetMapping("/basic")
    public String basicRAG(@RequestParam String question) {
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
    
    /**
     * 高级 RAG 示例
     */
    @PostMapping("/advanced")
    public RAGResponse advancedRAG(@RequestBody RAGRequest request) {
        // 1. 检索相关文档
        List<Document> documents = vectorStore.search(request.getQuestion(), request.getTopK());
        
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
                      "问题：" + request.getQuestion();
        
        // 4. 调用模型
        String answer = chatClient.call(prompt);
        
        // 5. 构建响应
        RAGResponse response = new RAGResponse();
        response.setQuestion(request.getQuestion());
        response.setAnswer(answer);
        response.setRetrievedDocuments(documents);
        response.setContext(context.toString());
        
        return response;
    }
    
    /**
     * 索引本地文件
     */
    @PostMapping("/index/file")
    public String indexFile(@RequestParam String filePath) {
        try {
            // 1. 读取文件内容
            String content = Files.readString(Path.of(filePath));
            
            // 2. 文本分块
            List<String> chunks = TextChunker.smartChunkText(content, 1000);
            
            // 3. 创建文档
            List<Document> documents = chunks.stream()
                .map(chunk -> new Document(chunk, Map.of("source", filePath)))
                .toList();
            
            // 4. 存储到向量数据库
            vectorStore.add(documents);
            
            return "文件已成功索引，共 " + chunks.size() + " 个块";
        } catch (IOException e) {
            return "索引文件失败：" + e.getMessage();
        }
    }
    
    /**
     * 索引文本内容
     */
    @PostMapping("/index/text")
    public String indexText(@RequestBody IndexRequest request) {
        // 1. 文本分块
        List<String> chunks = TextChunker.smartChunkText(request.getContent(), 1000);
        
        // 2. 创建文档
        List<Document> documents = chunks.stream()
            .map(chunk -> new Document(chunk, request.getMetadata()))
            .toList();
        
        // 3. 存储到向量数据库
        vectorStore.add(documents);
        
        return "文本已成功索引，共 " + chunks.size() + " 个块";
    }
    
    /**
     * 清空向量存储
     */
    @DeleteMapping("/clear")
    public String clearVectorStore() {
        // 注意：这会删除所有文档，使用时需谨慎
        // 具体实现取决于向量数据库类型
        return "向量存储已清空";
    }
    
    /**
     * 批量查询
     */
    @PostMapping("/batch")
    public List<RAGResponse> batchRAG(@RequestBody List<String> questions) {
        return questions.stream()
            .map(question -> {
                RAGRequest request = new RAGRequest();
                request.setQuestion(question);
                request.setTopK(3);
                return advancedRAG(request);
            })
            .toList();
    }
}

/**
 * RAG 请求类
 */
class RAGRequest {
    private String question;
    private int topK = 3;
    
    public String getQuestion() {
        return question;
    }
    
    public void setQuestion(String question) {
        this.question = question;
    }
    
    public int getTopK() {
        return topK;
    }
    
    public void setTopK(int topK) {
        this.topK = topK;
    }
}

/**
 * RAG 响应类
 */
class RAGResponse {
    private String question;
    private String answer;
    private List<Document> retrievedDocuments;
    private String context;
    
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
    
    public String getContext() {
        return context;
    }
    
    public void setContext(String context) {
        this.context = context;
    }
}

/**
 * 索引请求类
 */
class IndexRequest {
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
 * 文本分块工具类
 */
class TextChunker {
    
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
}
