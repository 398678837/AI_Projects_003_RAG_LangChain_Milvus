# Spring AI 提示工程

## 1. 提示工程概述

提示工程是设计和优化提示（Prompt）的过程，以获得模型的最佳响应。在 Spring AI 中，提示工程是构建有效 AI 应用的关键部分。

### 1.1 提示工程的重要性

- **提高模型性能**：精心设计的提示可以显著提高模型的输出质量
- **减少错误**：清晰的提示可以减少模型产生错误或不相关内容的可能性
- **控制输出**：通过提示可以控制模型输出的格式、风格和内容
- **节省成本**：优化的提示可以减少模型调用次数，降低成本

## 2. 提示的基本结构

一个有效的提示通常包含以下部分：

### 2.1 指令（Instruction）

指令告诉模型要做什么，应该清晰、具体。

**示例**：
- "请总结以下文本"
- "请将以下内容翻译成英语"
- "请回答以下问题"

### 2.2 上下文（Context）

上下文提供模型需要的背景信息，帮助模型理解问题。

**示例**：
- 文档内容
- 对话历史
- 相关事实

### 2.3 问题（Question）

问题是用户想要模型回答的具体问题。

**示例**：
- "Spring AI 是什么？"
- "如何使用 Spring AI 构建 RAG 系统？"

### 2.4 格式（Format）

格式指定模型输出的期望格式。

**示例**：
- "请以 JSON 格式输出"
- "请分点回答"
- "请用中文回答"

## 3. Spring AI 中的提示工程

### 3.1 PromptTemplate

`PromptTemplate` 是 Spring AI 中用于创建结构化提示的核心类。

#### 3.1.1 基本用法

```java
// 创建提示模板
String template = "请生成一篇关于 {topic} 的短文，长度约200字。";
PromptTemplate promptTemplate = PromptTemplate.create(template);

// 渲染提示
String prompt = promptTemplate.render(Map.of("topic", "Spring AI"));
```

#### 3.1.2 高级用法

```java
// 创建带系统消息的提示模板
String systemTemplate = "你是一个专业的 {role}。";
String userTemplate = "请生成关于 {topic} 的内容。";

PromptTemplate systemPromptTemplate = PromptTemplate.create(systemTemplate);
PromptTemplate userPromptTemplate = PromptTemplate.create(userTemplate);

String systemPrompt = systemPromptTemplate.render(Map.of("role", "技术作家"));
String userPrompt = userPromptTemplate.render(Map.of("topic", "Spring AI"));

List<Message> messages = List.of(
    new SystemMessage(systemPrompt),
    new UserMessage(userPrompt)
);
```

### 3.2 提示链

提示链是多个提示的组合，形成复杂的对话流程。

```java
// 第一步：获取用户问题
String userQuestion = "Spring AI 是什么？";

// 第二步：生成相关问题
String followUpTemplate = "基于用户问题 \"{question}\"，生成3个相关问题。";
PromptTemplate followUpPromptTemplate = PromptTemplate.create(followUpTemplate);
String followUpPrompt = followUpPromptTemplate.render(Map.of("question", userQuestion));
String followUpQuestions = chatClient.call(followUpPrompt);

// 第三步：结合相关问题生成最终回答
String finalTemplate = "用户问：{question}\n相关问题：{followUpQuestions}\n请提供详细回答。";
PromptTemplate finalPromptTemplate = PromptTemplate.create(finalTemplate);
String finalPrompt = finalPromptTemplate.render(Map.of(
    "question", userQuestion,
    "followUpQuestions", followUpQuestions
));
String finalAnswer = chatClient.call(finalPrompt);
```

### 3.3 上下文管理

上下文管理是提示工程的重要部分，特别是在对话系统中。

```java
// 管理对话历史
List<Message> conversation = new ArrayList<>();

// 添加系统消息
conversation.add(new SystemMessage("你是一个 helpful 的助手。"));

// 处理用户消息
public String handleUserMessage(String userMessage) {
    // 添加用户消息
    conversation.add(new UserMessage(userMessage));
    
    // 调用模型
    ChatResponse response = chatClient.chat(conversation);
    String assistantMessage = response.getResult().getOutput().getContent();
    
    // 添加助手消息到对话历史
    conversation.add(new AssistantMessage(assistantMessage));
    
    // 限制对话历史长度
    if (conversation.size() > 10) {
        conversation = conversation.subList(conversation.size() - 10, conversation.size());
    }
    
    return assistantMessage;
}
```

## 4. 提示工程最佳实践

### 4.1 提示设计原则

- **清晰具体**：明确告诉模型要做什么
- **提供示例**：通过示例展示期望的输出格式
- **使用系统消息**：利用系统消息设置上下文和角色
- **分割复杂任务**：将复杂任务分解为多个简单任务
- **指定输出格式**：明确要求模型以特定格式输出

### 4.2 提示优化技巧

- **迭代优化**：通过多次试验优化提示
- **使用few-shot学习**：提供少量示例帮助模型理解任务
- **调整温度参数**：根据任务调整模型的创造性
- **使用思维链**：引导模型逐步思考复杂问题
- **限制输出长度**：设置合理的最大令牌数

### 4.3 常见提示模式

#### 4.3.1 总结模式

```
请总结以下文本，保持核心信息，长度不超过200字：

{text}
```

#### 4.3.2 问答模式

```
基于以下上下文回答问题：

{context}

问题：{question}
```

#### 4.3.3 分类模式

```
请将以下文本分类到以下类别之一：技术、娱乐、体育、政治、其他

文本：{text}

分类：
```

#### 4.3.4 翻译模式

```
请将以下{source_language}文本翻译成{target_language}：

{text}
```

#### 4.3.5 创意写作模式

```
请以{genre}风格写一篇关于{topic}的{length}字文章：

要求：
1. {requirement1}
2. {requirement2}
3. {requirement3}
```

## 5. 提示工程工具

### 5.1 提示模板库

创建和管理提示模板的库，方便复用和维护。

```java
public class PromptTemplateLibrary {
    
    private static final Map<String, String> templates = new HashMap<>();
    
    static {
        templates.put("summary", "请总结以下文本，保持核心信息，长度不超过{length}字：\n\n{text}");
        templates.put("qa", "基于以下上下文回答问题：\n\n{context}\n\n问题：{question}");
        templates.put("classification", "请将以下文本分类到以下类别之一：{categories}\n\n文本：{text}\n\n分类：");
    }
    
    public static PromptTemplate getTemplate(String name) {
        String template = templates.get(name);
        if (template == null) {
            throw new IllegalArgumentException("Template not found: " + name);
        }
        return PromptTemplate.create(template);
    }
}
```

### 5.2 提示评估工具

评估提示质量的工具，帮助选择最佳提示。

```java
public class PromptEvaluator {
    
    private final ChatClient chatClient;
    
    public PromptEvaluator(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    public double evaluate(String prompt, String expectedOutput) {
        String actualOutput = chatClient.call(prompt);
        // 计算相似度或其他评估指标
        return calculateScore(actualOutput, expectedOutput);
    }
    
    private double calculateScore(String actual, String expected) {
        // 实现评估逻辑
        return 0.0;
    }
}
```

## 6. 提示工程案例

### 6.1 智能客服

**提示设计**：
```
你是一个专业的客服代表，负责回答用户关于产品的问题。

产品信息：
{product_info}

用户问题：{user_question}

请以友好、专业的语气回答用户问题，提供具体的解决方案。
```

**应用**：
- 处理用户咨询
- 提供产品信息
- 解决常见问题

### 6.2 内容生成

**提示设计**：
```
你是一个专业的内容创作者，擅长写技术博客。

主题：{topic}

要求：
1. 内容结构清晰，有标题和小标题
2. 包含具体的代码示例
3. 解释技术原理
4. 长度约1000字
5. 适合开发者阅读

请生成一篇高质量的技术博客。
```

**应用**：
- 生成技术文档
- 撰写博客文章
- 创建教程内容

### 6.3 代码辅助

**提示设计**：
```
你是一个专业的程序员，擅长{language}编程。

请为以下需求编写代码：
{requirement}

要求：
1. 代码结构清晰，有注释
2. 处理边界情况
3. 遵循最佳实践
4. 提供测试用例

请生成完整的代码。
```

**应用**：
- 代码生成
- 代码优化
- 代码解释

## 7. 常见问题及解决方案

### 7.1 模型输出不相关

**问题**：模型输出与问题不相关
**解决方案**：
- 明确指令
- 提供更多上下文
- 使用系统消息设置角色
- 限制输出范围

### 7.2 模型输出格式错误

**问题**：模型输出格式不符合要求
**解决方案**：
- 明确指定输出格式
- 提供格式示例
- 使用结构化提示
- 验证输出格式

### 7.3 模型输出质量不稳定

**问题**：模型输出质量时好时坏
**解决方案**：
- 优化提示结构
- 调整温度参数
- 使用few-shot学习
- 实现输出验证和重试机制

### 7.4 提示过长

**问题**：提示长度超过模型限制
**解决方案**：
- 精简提示内容
- 使用摘要技术
- 分割复杂任务
- 利用向量存储和 RAG

## 8. 总结

提示工程是 Spring AI 应用开发的关键部分，通过精心设计和优化提示，可以显著提高模型的输出质量和应用的整体性能。

在实际开发中，应根据具体任务和模型特点，设计合适的提示策略，不断迭代优化，以获得最佳效果。随着 AI 技术的不断发展，提示工程也在不断演进，为开发者提供更多可能性。