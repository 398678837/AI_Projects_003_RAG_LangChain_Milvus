package com.example.springai.prompt;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.*;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Spring AI 提示工程示例
 */
@RestController
@RequestMapping("/prompt")
public class PromptEngineeringDemo {
    
    private final ChatClient chatClient;
    
    @Autowired
    public PromptEngineeringDemo(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    /**
     * 基本提示模板示例
     */
    @GetMapping("/template/basic")
    public String basicTemplate(@RequestParam String topic) {
        String template = "请生成一篇关于 {topic} 的短文，长度约200字。";
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String prompt = promptTemplate.render(Map.of("topic", topic));
        return chatClient.call(prompt);
    }
    
    /**
     * 带系统消息的提示模板
     */
    @PostMapping("/template/system")
    public String systemTemplate(@RequestBody Map<String, String> params) {
        String systemTemplate = "你是一个专业的 {role}。";
        String userTemplate = "请生成关于 {topic} 的内容，长度约{length}字。";
        
        PromptTemplate systemPromptTemplate = PromptTemplate.create(systemTemplate);
        PromptTemplate userPromptTemplate = PromptTemplate.create(userTemplate);
        
        String systemPrompt = systemPromptTemplate.render(Map.of("role", params.get("role")));
        String userPrompt = userPromptTemplate.render(Map.of(
            "topic", params.get("topic"),
            "length", params.get("length")
        ));
        
        List<Message> messages = List.of(
            new SystemMessage(systemPrompt),
            new UserMessage(userPrompt)
        );
        
        return chatClient.chat(messages).getResult().getOutput().getContent();
    }
    
    /**
     * 提示链示例
     */
    @GetMapping("/chain")
    public String promptChain(@RequestParam String question) {
        // 第一步：生成相关问题
        String followUpTemplate = "基于用户问题 \"{question}\"，生成3个相关问题。";
        PromptTemplate followUpPromptTemplate = PromptTemplate.create(followUpTemplate);
        String followUpPrompt = followUpPromptTemplate.render(Map.of("question", question));
        String followUpQuestions = chatClient.call(followUpPrompt);
        
        // 第二步：结合相关问题生成最终回答
        String finalTemplate = "用户问：{question}\n相关问题：{followUpQuestions}\n请提供详细回答。";
        PromptTemplate finalPromptTemplate = PromptTemplate.create(finalTemplate);
        String finalPrompt = finalPromptTemplate.render(Map.of(
            "question", question,
            "followUpQuestions", followUpQuestions
        ));
        
        return chatClient.call(finalPrompt);
    }
    
    /**
     * 对话历史管理示例
     */
    @PostMapping("/conversation")
    public String conversation(@RequestBody List<Message> messages) {
        return chatClient.chat(messages).getResult().getOutput().getContent();
    }
    
    /**
     * Few-shot 学习示例
     */
    @GetMapping("/few-shot")
    public String fewShotLearning(@RequestParam String text) {
        String template = "请将以下文本分类到以下类别之一：技术、娱乐、体育、政治、其他\n\n" +
                         "示例1：Spring AI 是一个新的框架，用于在 Spring 应用中集成 AI 能力。\n分类：技术\n\n" +
                         "示例2：世界杯足球赛正在如火如荼地进行。\n分类：体育\n\n" +
                         "示例3：最新的电影在上映，票房表现不错。\n分类：娱乐\n\n" +
                         "文本：{text}\n分类：";
        
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String prompt = promptTemplate.render(Map.of("text", text));
        return chatClient.call(prompt);
    }
    
    /**
     * 思维链示例
     */
    @GetMapping("/chain-of-thought")
    public String chainOfThought(@RequestParam String problem) {
        String template = "请解决以下问题，详细展示你的思考过程：\n\n{problem}\n\n" +
                         "思考过程：\n" +
                         "1.\n" +
                         "2.\n" +
                         "3.\n" +
                         "\n答案：";
        
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String prompt = promptTemplate.render(Map.of("problem", problem));
        return chatClient.call(prompt);
    }
    
    /**
     * 结构化输出示例
     */
    @GetMapping("/structured-output")
    public String structuredOutput(@RequestParam String text) {
        String template = "请分析以下文本，并以 JSON 格式输出分析结果：\n\n{text}\n\n" +
                         "JSON 格式：\n{\n  \"summary\": \"文本摘要\",\n  \"keywords\": [\"关键词1\", \"关键词2\"],\n  \"sentiment\": \"积极|中性|消极\"\n}";
        
        PromptTemplate promptTemplate = PromptTemplate.create(template);
        String prompt = promptTemplate.render(Map.of("text", text));
        return chatClient.call(prompt);
    }
    
    /**
     * 提示模板库示例
     */
    @GetMapping("/library/{templateName}")
    public String templateLibrary(@PathVariable String templateName, 
                                @RequestParam Map<String, String> params) {
        PromptTemplate template = PromptTemplateLibrary.getTemplate(templateName);
        String prompt = template.render(params);
        return chatClient.call(prompt);
    }
}

/**
 * 提示模板库
 */
class PromptTemplateLibrary {
    
    private static final Map<String, String> templates = Map.of(
        "summary", "请总结以下文本，保持核心信息，长度不超过{length}字：\n\n{text}",
        "qa", "基于以下上下文回答问题：\n\n{context}\n\n问题：{question}",
        "classification", "请将以下文本分类到以下类别之一：{categories}\n\n文本：{text}\n\n分类：",
        "translation", "请将以下{source_language}文本翻译成{target_language}：\n\n{text}",
        "code", "请为以下需求编写{language}代码：\n{requirement}\n\n要求：\n1. 代码结构清晰，有注释\n2. 处理边界情况\n3. 遵循最佳实践"
    );
    
    public static PromptTemplate getTemplate(String name) {
        String template = templates.get(name);
        if (template == null) {
            throw new IllegalArgumentException("Template not found: " + name);
        }
        return PromptTemplate.create(template);
    }
}

/**
 * 对话管理器
 */
class ConversationManager {
    
    private final List<Message> conversation = new ArrayList<>();
    private final int maxMessages = 20;
    
    public ConversationManager(String systemMessage) {
        conversation.add(new SystemMessage(systemMessage));
    }
    
    public String addUserMessage(String userMessage, ChatClient chatClient) {
        // 添加用户消息
        conversation.add(new UserMessage(userMessage));
        
        // 调用模型
        ChatResponse response = chatClient.chat(conversation);
        String assistantMessage = response.getResult().getOutput().getContent();
        
        // 添加助手消息
        conversation.add(new AssistantMessage(assistantMessage));
        
        // 限制对话历史长度
        if (conversation.size() > maxMessages) {
            // 保留系统消息，移除最旧的消息
            List<Message> newConversation = new ArrayList<>();
            newConversation.add(conversation.get(0)); // 保留系统消息
            newConversation.addAll(conversation.subList(conversation.size() - (maxMessages - 1), conversation.size()));
            conversation.clear();
            conversation.addAll(newConversation);
        }
        
        return assistantMessage;
    }
    
    public List<Message> getConversation() {
        return new ArrayList<>(conversation);
    }
}
