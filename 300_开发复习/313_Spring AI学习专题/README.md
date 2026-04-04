# Spring AI 学习专题

## 1. Spring AI 概述

Spring AI 是 Spring 生态系统中的一个新框架，旨在简化人工智能（AI）应用的开发。它提供了一套统一的 API 和抽象，使开发者能够轻松集成各种 AI 模型和服务到 Spring 应用中。

### 1.1 Spring AI 的核心价值

- **统一抽象**：为不同的 AI 模型和服务提供统一的接口
- **简化集成**：减少集成 AI 服务的样板代码
- **生态系统集成**：与 Spring Boot、Spring Cloud 等 Spring 生态系统无缝集成
- **可扩展性**：支持多种 AI 模型和服务提供商
- **生产就绪**：提供监控、容错、安全等企业级特性

## 2. 目录结构

```
313_Spring AI学习专题/
├── 01_Basic_Concepts_基础概念/        # 基础概念
├── 02_Core_Components_核心组件/       # 核心组件
├── 03_Model_Integration_模型集成/     # 模型集成
├── 04_Prompt_Engineering_提示工程/    # 提示工程
├── 05_Vector_Database_向量数据库/     # 向量数据库
├── 06_RAG_检索增强生成/              # 检索增强生成
├── 07_Fine_Tuning_模型微调/          # 模型微调
├── 08_Evaluation_模型评估/           # 模型评估
├── 09_Best_Practices_最佳实践/         # 最佳实践
├── 10_Real_World_实战应用/           # 实战应用
└── README.md                           # 本文件
```

## 3. 核心特性

### 3.1 模型集成

- **大语言模型（LLM）**：集成 OpenAI、Azure OpenAI、Hugging Face 等模型
- **嵌入模型**：支持文本向量化，用于语义搜索和 RAG
- **多模态模型**：支持处理文本、图像等多种数据类型

### 3.2 提示工程

- **提示模板**：支持结构化的提示模板
- **提示链**：支持复杂的提示流程
- **上下文管理**：管理对话历史和上下文信息

### 3.3 检索增强生成（RAG）

- **文档加载**：支持从多种源加载文档
- **文本分块**：智能分块策略
- **向量存储**：集成多种向量数据库
- **检索策略**：支持多种检索算法

### 3.4 评估

- **模型评估**：评估模型性能
- **提示评估**：评估提示质量
- **RAG 评估**：评估 RAG 系统性能

## 4. 快速开始

### 4.1 依赖配置

在 Maven 项目中添加 Spring AI 依赖：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    <version>0.8.1</version>
</dependency>
```

### 4.2 配置示例

在 `application.properties` 中配置 AI 模型：

```properties
# OpenAI 配置
spring.ai.openai.api-key=your-api-key
spring.ai.openai.chat.model=gpt-3.5-turbo
spring.ai.openai.chat.temperature=0.7
```

### 4.3 基本使用

```java
@RestController
public class AIController {
    
    private final ChatClient chatClient;
    
    public AIController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    @GetMapping("/chat")
    public String chat(@RequestParam String message) {
        return chatClient.call(message);
    }
}
```

## 5. 学习路径

1. **基础概念**：了解 Spring AI 的核心概念和架构
2. **核心组件**：学习 Spring AI 的核心组件和 API
3. **模型集成**：掌握如何集成不同的 AI 模型
4. **提示工程**：学习如何设计有效的提示
5. **向量数据库**：了解向量数据库的使用
6. **RAG**：掌握检索增强生成技术
7. **模型微调**：学习如何微调模型
8. **评估**：了解如何评估模型和系统性能
9. **最佳实践**：学习 Spring AI 的最佳实践
10. **实战应用**：通过实际项目应用 Spring AI

## 6. 适用场景

- **智能客服**：构建基于 LLM 的客服系统
- **内容生成**：自动生成文章、报告等内容
- **知识管理**：构建基于 RAG 的知识库系统
- **语义搜索**：实现基于向量的语义搜索
- **代码辅助**：辅助开发人员编写代码
- **数据分析**：分析和处理结构化、非结构化数据

## 7. 总结

Spring AI 为 Spring 开发者提供了一种简单、统一的方式来集成 AI 能力到应用中。通过本学习专题，你将了解 Spring AI 的核心概念、组件和最佳实践，掌握如何构建基于 AI 的应用系统。

随着 AI 技术的不断发展，Spring AI 也在持续演进，为开发者提供更多强大的功能和更好的开发体验。