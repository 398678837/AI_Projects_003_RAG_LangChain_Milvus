package com.example.springai.vector;

import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.ai.vectorstore.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * Spring AI 向量数据库示例
 */
@RestController
@RequestMapping("/vector")
public class VectorDatabaseDemo {
    
    private final VectorStore vectorStore;
    
    @Autowired
    public VectorDatabaseDemo(VectorStore vectorStore) {
        this.vectorStore = vectorStore;
    }
    
    /**
     * 添加单个文档
     */
    @PostMapping("/add")
    public String addDocument(@RequestBody DocumentRequest documentRequest) {
        Document document = new Document(
            documentRequest.getContent(),
            documentRequest.getMetadata()
        );
        vectorStore.add(List.of(document));
        return "文档已添加到向量存储";
    }
    
    /**
     * 批量添加文档
     */
    @PostMapping("/add/batch")
    public String batchAddDocuments(@RequestBody List<DocumentRequest> documentRequests) {
        List<Document> documents = documentRequests.stream()
            .map(req -> new Document(req.getContent(), req.getMetadata()))
            .toList();
        vectorStore.add(documents);
        return "批量文档已添加到向量存储";
    }
    
    /**
     * 搜索文档
     */
    @GetMapping("/search")
    public List<Document> searchDocuments(@RequestParam String query, 
                                        @RequestParam(defaultValue = "5") int k) {
        return vectorStore.search(query, k);
    }
    
    /**
     * 删除文档
     */
    @DeleteMapping("/delete")
    public String deleteDocuments(@RequestBody List<String> ids) {
        vectorStore.delete(ids);
        return "文档已从向量存储中删除";
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
     * 简单的 RAG 示例
     */
    @GetMapping("/rag")
    public RAGResponse rag(@RequestParam String question) {
        // 1. 检索相关文档
        List<Document> documents = vectorStore.search(question, 3);
        
        // 2. 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 3. 这里可以调用 ChatClient 生成回答
        // 为了简化示例，我们只返回检索到的文档
        
        RAGResponse response = new RAGResponse();
        response.setQuestion(question);
        response.setRetrievedDocuments(documents);
        response.setContext(context.toString());
        
        return response;
    }
    
    /**
     * 文档统计信息
     */
    @GetMapping("/stats")
    public Map<String, Object> getStats() {
        // 注意：具体实现取决于向量数据库类型
        // 这里返回一个示例统计信息
        return Map.of(
            "vectorStoreType", vectorStore.getClass().getSimpleName(),
            "status", "active"
        );
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
    private List<Document> retrievedDocuments;
    private String context;
    private String answer;
    
    public String getQuestion() {
        return question;
    }
    
    public void setQuestion(String question) {
        this.question = question;
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
    
    public String getAnswer() {
        return answer;
    }
    
    public void setAnswer(String answer) {
        this.answer = answer;
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
