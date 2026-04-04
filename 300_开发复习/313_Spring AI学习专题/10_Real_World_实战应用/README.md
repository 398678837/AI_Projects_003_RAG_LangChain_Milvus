# Spring AI 实战应用

## 1. 实战应用概述

Spring AI 可以应用于各种实际场景，从智能客服到内容生成，从知识管理到语义搜索。本章将介绍几个典型的 Spring AI 实战应用案例，帮助开发者理解如何在实际项目中使用 Spring AI。

### 1.1 实战应用的重要性

- **验证理论**：将理论知识应用到实际场景中
- **解决问题**：使用 AI 技术解决实际业务问题
- **积累经验**：积累 Spring AI 开发经验
- **展示能力**：展示 Spring AI 的实际应用价值

## 2. 智能客服系统

### 2.1 系统概述

智能客服系统是 Spring AI 的典型应用场景，通过大语言模型和 RAG 技术，为用户提供智能的问答服务。

### 2.2 系统架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  用户界面   │────>│  控制器层   │────>│  服务层     │────>│  AI 组件    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │  向量存储   │
                                        └─────────────┘
```

### 2.3 核心功能

- **意图识别**：识别用户的意图和需求
- **知识库检索**：从知识库中检索相关信息
- **智能回答**：生成准确、相关的回答
- **多轮对话**：支持复杂的多轮对话
- **情感分析**：分析用户情感，提供个性化响应

### 2.4 实现示例

```java
@RestController
@RequestMapping("/chatbot")
public class ChatbotController {
    
    private final ChatbotService chatbotService;
    
    @Autowired
    public ChatbotController(ChatbotService chatbotService) {
        this.chatbotService = chatbotService;
    }
    
    @PostMapping("/chat")
    public ChatResponse chat(@RequestBody ChatRequest request) {
        return chatbotService.processMessage(request.getMessage(), request.getConversationId());
    }
    
    @PostMapping("/upload-knowledge")
    public String uploadKnowledge(@RequestParam("file") MultipartFile file) {
        return chatbotService.uploadKnowledge(file);
    }
}

@Service
public class ChatbotService {
    
    private final ChatClient chatClient;
    private final VectorStore vectorStore;
    private final Map<String, List<Message>> conversations = new ConcurrentHashMap<>();
    
    @Autowired
    public ChatbotService(ChatClient chatClient, VectorStore vectorStore) {
        this.chatClient = chatClient;
        this.vectorStore = vectorStore;
    }
    
    public ChatResponse processMessage(String message, String conversationId) {
        // 获取或创建对话历史
        List<Message> conversation = conversations.computeIfAbsent(conversationId, k -> new ArrayList<>());
        
        // 添加用户消息
        conversation.add(new UserMessage(message));
        
        // 检索相关知识
        List<Document> documents = vectorStore.search(message, 3);
        
        // 构建上下文
        StringBuilder context = new StringBuilder();
        for (Document doc : documents) {
            context.append(doc.getContent()).append("\n\n");
        }
        
        // 构建提示
        String prompt = "基于以下上下文和对话历史回答用户问题：\n\n" +
                      context.toString() + "\n" +
                      "对话历史：" + conversation.stream()
                          .map(Message::getContent)
                          .collect(Collectors.joining("\n")) + "\n" +
                      "用户问题：" + message;
        
        // 调用模型
        String response = chatClient.call(prompt);
        
        // 添加助手消息
        conversation.add(new AssistantMessage(response));
        
        // 限制对话历史长度
        if (conversation.size() > 20) {
            conversation = conversation.subList(conversation.size() - 20, conversation.size());
            conversations.put(conversationId, conversation);
        }
        
        return new ChatResponse(response);
    }
    
    public String uploadKnowledge(MultipartFile file) {
        try {
            // 读取文件内容
            String content = new String(file.getBytes());
            
            // 文本分块
            List<String> chunks = TextChunker.smartChunkText(content, 1000);
            
            // 创建文档
            List<Document> documents = chunks.stream()
                .map(chunk -> new Document(chunk, Map.of("source", file.getOriginalFilename())))
                .toList();
            
            // 存储到向量数据库
            vectorStore.add(documents);
            
            return "知识库上传成功，共 " + chunks.size() + " 个块";
        } catch (Exception e) {
            return "知识库上传失败：" + e.getMessage();
        }
    }
}
```

## 3. 内容生成系统

### 3.1 系统概述

内容生成系统利用 Spring AI 生成各种类型的内容，如文章、报告、邮件等，提高内容创作效率。

### 3.2 系统架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  用户界面   │────>│  控制器层   │────>│  服务层     │────>│  AI 组件    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### 3.3 核心功能

- **文章生成**：生成各种类型的文章
- **报告生成**：基于数据生成报告
- **邮件生成**：生成邮件内容
- **内容优化**：优化现有内容
- **多格式支持**：支持生成多种格式的内容

### 3.4 实现示例

```java
@RestController
@RequestMapping("/content")
public class ContentController {
    
    private final ContentService contentService;
    
    @Autowired
    public ContentController(ContentService contentService) {
        this.contentService = contentService;
    }
    
    @PostMapping("/generate/article")
    public String generateArticle(@RequestBody ArticleRequest request) {
        return contentService.generateArticle(request.getTopic(), request.getLength(), request.getStyle());
    }
    
    @PostMapping("/generate/report")
    public String generateReport(@RequestBody ReportRequest request) {
        return contentService.generateReport(request.getData(), request.getTemplate());
    }
    
    @PostMapping("/optimize")
    public String optimizeContent(@RequestBody OptimizeRequest request) {
        return contentService.optimizeContent(request.getContent(), request.getTargetStyle());
    }
}

@Service
public class ContentService {
    
    private final ChatClient chatClient;
    private final PromptTemplateLibrary promptTemplateLibrary;
    
    @Autowired
    public ContentService(ChatClient chatClient, PromptTemplateLibrary promptTemplateLibrary) {
        this.chatClient = chatClient;
        this.promptTemplateLibrary = promptTemplateLibrary;
    }
    
    public String generateArticle(String topic, int length, String style) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("article");
        String prompt = template.render(Map.of(
            "topic", topic,
            "length", String.valueOf(length),
            "style", style
        ));
        return chatClient.call(prompt);
    }
    
    public String generateReport(Map<String, Object> data, String template) {
        PromptTemplate promptTemplate = promptTemplateLibrary.getTemplate("report");
        String prompt = promptTemplate.render(Map.of(
            "data", data.toString(),
            "template", template
        ));
        return chatClient.call(prompt);
    }
    
    public String optimizeContent(String content, String targetStyle) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("optimize");
        String prompt = template.render(Map.of(
            "content", content,
            "targetStyle", targetStyle
        ));
        return chatClient.call(prompt);
    }
}
```

## 4. 知识库系统

### 4.1 系统概述

知识库系统利用 Spring AI 和 RAG 技术，构建智能的知识管理和检索系统，帮助用户快速获取所需信息。

### 4.2 系统架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  用户界面   │────>│  控制器层   │────>│  服务层     │────>│  RAG 系统   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │  向量存储   │
                                        └─────────────┘
```

### 4.3 核心功能

- **文档管理**：上传、管理和组织文档
- **智能检索**：基于语义的智能检索
- **问答系统**：基于知识库的问答
- **知识图谱**：构建知识之间的关联
- **版本管理**：管理知识库的版本

### 4.4 实现示例

```java
@RestController
@RequestMapping("/knowledge")
public class KnowledgeController {
    
    private final KnowledgeService knowledgeService;
    
    @Autowired
    public KnowledgeController(KnowledgeService knowledgeService) {
        this.knowledgeService = knowledgeService;
    }
    
    @PostMapping("/upload")
    public String uploadDocument(@RequestParam("file") MultipartFile file) {
        return knowledgeService.uploadDocument(file);
    }
    
    @GetMapping("/search")
    public List<Document> search(@RequestParam String query, @RequestParam(defaultValue = "5") int k) {
        return knowledgeService.search(query, k);
    }
    
    @GetMapping("/qa")
    public String askQuestion(@RequestParam String question) {
        return knowledgeService.askQuestion(question);
    }
    
    @DeleteMapping("/delete/{id}")
    public String deleteDocument(@PathVariable String id) {
        return knowledgeService.deleteDocument(id);
    }
}

@Service
public class KnowledgeService {
    
    private final VectorStore vectorStore;
    private final ChatClient chatClient;
    
    @Autowired
    public KnowledgeService(VectorStore vectorStore, ChatClient chatClient) {
        this.vectorStore = vectorStore;
        this.chatClient = chatClient;
    }
    
    public String uploadDocument(MultipartFile file) {
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
        } catch (Exception e) {
            return "文档上传失败：" + e.getMessage();
        }
    }
    
    public List<Document> search(String query, int k) {
        return vectorStore.search(query, k);
    }
    
    public String askQuestion(String question) {
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
    
    public String deleteDocument(String id) {
        try {
            vectorStore.delete(List.of(id));
            return "文档删除成功";
        } catch (Exception e) {
            return "文档删除失败：" + e.getMessage();
        }
    }
}
```

## 5. 语义搜索系统

### 5.1 系统概述

语义搜索系统利用 Spring AI 的嵌入模型和向量存储，实现基于语义的智能搜索，比传统的关键词搜索更准确、更智能。

### 5.2 系统架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  用户界面   │────>│  控制器层   │────>│  服务层     │────>│  向量存储   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │  嵌入模型   │
                                        └─────────────┘
```

### 5.3 核心功能

- **语义搜索**：基于语义的智能搜索
- **结果排序**：根据相关性排序搜索结果
- **过滤功能**：基于元数据过滤搜索结果
- **搜索建议**：提供搜索建议
- **结果高亮**：高亮显示匹配的内容

### 5.4 实现示例

```java
@RestController
@RequestMapping("/search")
public class SearchController {
    
    private final SearchService searchService;
    
    @Autowired
    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }
    
    @GetMapping("/semantic")
    public List<SearchResult> semanticSearch(@RequestParam String query, 
                                           @RequestParam(defaultValue = "10") int k) {
        return searchService.semanticSearch(query, k);
    }
    
    @GetMapping("/filtered")
    public List<SearchResult> filteredSearch(@RequestParam String query, 
                                           @RequestParam Map<String, String> filters, 
                                           @RequestParam(defaultValue = "10") int k) {
        return searchService.filteredSearch(query, filters, k);
    }
    
    @GetMapping("/suggest")
    public List<String> getSuggestions(@RequestParam String query) {
        return searchService.getSuggestions(query);
    }
}

@Service
public class SearchService {
    
    private final VectorStore vectorStore;
    private final EmbeddingClient embeddingClient;
    private final ChatClient chatClient;
    
    @Autowired
    public SearchService(VectorStore vectorStore, 
                       EmbeddingClient embeddingClient, 
                       ChatClient chatClient) {
        this.vectorStore = vectorStore;
        this.embeddingClient = embeddingClient;
        this.chatClient = chatClient;
    }
    
    public List<SearchResult> semanticSearch(String query, int k) {
        // 搜索相关文档
        List<Document> documents = vectorStore.search(query, k);
        
        // 转换为搜索结果
        return documents.stream()
            .map(doc -> {
                SearchResult result = new SearchResult();
                result.setContent(doc.getContent());
                result.setMetadata(doc.getMetadata());
                // 计算相关性得分（这里简化处理）
                result.setScore(0.0);
                return result;
            })
            .toList();
    }
    
    public List<SearchResult> filteredSearch(String query, Map<String, String> filters, int k) {
        // 这里简化处理，实际应该根据过滤器进行过滤
        List<Document> documents = vectorStore.search(query, k);
        
        // 过滤结果
        List<Document> filteredDocuments = documents.stream()
            .filter(doc -> {
                // 简单的过滤逻辑
                for (Map.Entry<String, String> entry : filters.entrySet()) {
                    Object value = doc.getMetadata().get(entry.getKey());
                    if (value == null || !value.toString().equals(entry.getValue())) {
                        return false;
                    }
                }
                return true;
            })
            .toList();
        
        // 转换为搜索结果
        return filteredDocuments.stream()
            .map(doc -> {
                SearchResult result = new SearchResult();
                result.setContent(doc.getContent());
                result.setMetadata(doc.getMetadata());
                result.setScore(0.0);
                return result;
            })
            .toList();
    }
    
    public List<String> getSuggestions(String query) {
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
}

class SearchResult {
    private String content;
    private Map<String, Object> metadata;
    private double score;
    
    // getters and setters
}
```

## 6. 代码辅助系统

### 6.1 系统概述

代码辅助系统利用 Spring AI 帮助开发者编写、优化和理解代码，提高开发效率。

### 6.2 系统架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  IDE 插件   │────>│  控制器层   │────>│  服务层     │────>│  AI 组件    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### 6.3 核心功能

- **代码生成**：根据需求生成代码
- **代码优化**：优化现有代码
- **代码解释**：解释代码的功能和逻辑
- **错误修复**：修复代码中的错误
- **文档生成**：为代码生成文档

### 6.4 实现示例

```java
@RestController
@RequestMapping("/code")
public class CodeController {
    
    private final CodeService codeService;
    
    @Autowired
    public CodeController(CodeService codeService) {
        this.codeService = codeService;
    }
    
    @PostMapping("/generate")
    public String generateCode(@RequestBody CodeRequest request) {
        return codeService.generateCode(request.getRequirement(), request.getLanguage());
    }
    
    @PostMapping("/optimize")
    public String optimizeCode(@RequestBody OptimizeCodeRequest request) {
        return codeService.optimizeCode(request.getCode(), request.getLanguage());
    }
    
    @PostMapping("/explain")
    public String explainCode(@RequestBody ExplainCodeRequest request) {
        return codeService.explainCode(request.getCode(), request.getLanguage());
    }
    
    @PostMapping("/fix")
    public String fixCode(@RequestBody FixCodeRequest request) {
        return codeService.fixCode(request.getCode(), request.getError(), request.getLanguage());
    }
    
    @PostMapping("/document")
    public String generateDocumentation(@RequestBody DocumentCodeRequest request) {
        return codeService.generateDocumentation(request.getCode(), request.getLanguage());
    }
}

@Service
public class CodeService {
    
    private final ChatClient chatClient;
    private final PromptTemplateLibrary promptTemplateLibrary;
    
    @Autowired
    public CodeService(ChatClient chatClient, PromptTemplateLibrary promptTemplateLibrary) {
        this.chatClient = chatClient;
        this.promptTemplateLibrary = promptTemplateLibrary;
    }
    
    public String generateCode(String requirement, String language) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("code");
        String prompt = template.render(Map.of(
            "requirement", requirement,
            "language", language
        ));
        return chatClient.call(prompt);
    }
    
    public String optimizeCode(String code, String language) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("optimize-code");
        String prompt = template.render(Map.of(
            "code", code,
            "language", language
        ));
        return chatClient.call(prompt);
    }
    
    public String explainCode(String code, String language) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("explain-code");
        String prompt = template.render(Map.of(
            "code", code,
            "language", language
        ));
        return chatClient.call(prompt);
    }
    
    public String fixCode(String code, String error, String language) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("fix-code");
        String prompt = template.render(Map.of(
            "code", code,
            "error", error,
            "language", language
        ));
        return chatClient.call(prompt);
    }
    
    public String generateDocumentation(String code, String language) {
        PromptTemplate template = promptTemplateLibrary.getTemplate("document-code");
        String prompt = template.render(Map.of(
            "code", code,
            "language", language
        ));
        return chatClient.call(prompt);
    }
}
```

## 7. 实战应用最佳实践

### 7.1 项目规划

- **需求分析**：明确项目需求和目标
- **技术选型**：选择合适的 AI 模型和向量存储
- **架构设计**：设计合理的系统架构
- **资源规划**：规划计算资源和存储需求

### 7.2 开发流程

- **原型开发**：快速开发原型，验证概念
- **迭代开发**：采用迭代开发方式，不断优化
- **测试**：进行充分的测试，确保系统质量
- **部署**：部署到生产环境，监控系统性能

### 7.3 性能优化

- **模型选择**：选择适合任务的模型
- **缓存策略**：合理使用缓存，提高性能
- **批处理**：批量处理请求，减少 API 调用
- **异步处理**：使用异步处理，提高系统响应速度

### 7.4 安全考虑

- **API 密钥管理**：安全管理 API 密钥
- **数据安全**：保护敏感数据
- **访问控制**：实现合理的访问控制
- **输入验证**：验证用户输入，防止注入攻击

## 8. 总结

Spring AI 可以应用于各种实际场景，从智能客服到内容生成，从知识库系统到语义搜索，从代码辅助到数据分析。通过本章的实战应用案例，开发者可以了解如何在实际项目中使用 Spring AI，构建智能、高效的应用系统。

在实际开发中，应根据具体需求和资源情况，选择合适的技术方案，遵循最佳实践，不断优化系统性能和用户体验。随着 AI 技术的不断发展，Spring AI 也在持续演进，为开发者提供更多强大的功能和更好的开发体验。