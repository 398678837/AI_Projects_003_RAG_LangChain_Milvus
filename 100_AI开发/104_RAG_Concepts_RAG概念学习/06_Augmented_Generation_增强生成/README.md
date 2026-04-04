# 增强生成

## 什么是增强生成？

增强生成（Augmented Generation）是RAG流程的最后一步，它将检索到的相关文本块与用户查询一起输入到语言模型中，生成基于文档的回答。增强生成的目标是利用检索到的信息，使语言模型生成更准确、更相关的回答，同时避免幻觉。

## 增强生成的原理

1. **检索结果处理**：收集和整理检索到的相关文本块
2. **提示构建**：将检索结果和用户查询构建成提示
3. **模型推理**：将提示输入到语言模型中
4. **结果生成**：语言模型基于提示生成回答
5. **后处理**：对生成的回答进行后处理（如引用来源）

## 提示模板

### 基础提示模板

```python
from langchain.prompts import PromptTemplate

prompt_template = """
你是一个基于文档的问答助手，请根据以下文档内容回答用户问题。
如果你不知道答案，直接说"根据提供的文档，我无法回答这个问题"，不要尝试编造答案。

文档内容:
{context}

问题:
{question}

回答:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)
```

### 高级提示模板

```python
prompt_template = """
你是一个专业的问答助手，任务是基于提供的文档回答用户问题。

请遵循以下规则：
1. 仔细阅读并理解提供的文档内容
2. 基于文档内容回答问题，不要添加文档中没有的信息
3. 如果文档中没有相关信息，直接说"根据提供的文档，我无法回答这个问题"
4. 回答要清晰、准确、简洁
5. 可以引用文档中的内容，但要确保引用准确

文档内容:
{context}

问题:
{question}

回答:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)
```

## 语言模型选择

### 开源模型

| 模型 | 描述 | 适用场景 |
|------|------|----------|
| Qwen | 阿里云开发的大语言模型 | 中文场景，需要本地化部署 |
| Llama 2 | Meta开发的开源大语言模型 | 英文场景，需要本地化部署 |
| ChatGLM | 智谱AI开发的中文大语言模型 | 中文场景，需要本地化部署 |
| Mistral | 轻量级开源大语言模型 | 英文场景，适合边缘设备 |

### API模型

| 模型 | 描述 | 适用场景 |
|------|------|----------|
| GPT-3.5-turbo | OpenAI的轻量级模型 | 通用场景，需要API访问 |
| GPT-4 | OpenAI的高级模型 | 复杂场景，需要API访问 |
| Claude | Anthropic开发的大语言模型 | 长文本处理，需要API访问 |
| 通义千问 | 阿里云开发的大语言模型 | 中文场景，需要API访问 |

## 问答链（QA Chain）

### 1. RetrievalQA

```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

result = qa_chain.run("什么是RAG？")
print(result)
```

### 2. ConversationalRetrievalChain

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(),
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": PROMPT}
)

result = qa_chain("什么是RAG？")
print(result["answer"])

# 多轮对话
result = qa_chain("它有什么优势？")
print(result["answer"])
```

### 3. 自定义问答链

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# 构建提示模板
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    基于以下文档回答问题：
    {context}
    
    问题：{question}
    
    回答：
    """
)

# 创建LLM链
llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt
)

# 检索相关文档
relevant_docs = retriever.get_relevant_documents("什么是RAG？")
context = "\n".join([doc.page_content for doc in relevant_docs])

# 生成回答
result = llm_chain.run(context=context, question="什么是RAG？")
print(result)
```

## 链类型（Chain Type）

### 1. stuff

**特点**：将所有检索到的文档内容填充到提示中

**优点**：简单直接，上下文信息完整
**缺点**：受限于语言模型的上下文窗口大小

**适用场景**：检索结果较少，文档较短的场景

### 2. map_reduce

**特点**：先为每个文档生成回答，然后汇总这些回答

**优点**：可以处理大量文档，不受上下文窗口限制
**缺点**：生成过程复杂，可能导致信息丢失

**适用场景**：检索结果较多，文档较长的场景

### 3. refine

**特点**：迭代式地基于前一个回答和新文档生成更完善的回答

**优点**：能够生成更连贯、更全面的回答
**缺点**：生成过程较慢，计算成本高

**适用场景**：需要深度理解文档内容的场景

### 4. map_rerank

**特点**：为每个文档生成回答和评分，然后选择评分最高的回答

**优点**：可以选择最相关的回答
**缺点**：可能忽略其他文档的重要信息

**适用场景**：需要快速生成准确回答的场景

## 最佳实践

1. **选择合适的语言模型**：
   - 开发测试：使用轻量级开源模型
   - 生产环境：根据性能和精度需求选择合适的模型

2. **优化提示模板**：
   - 明确任务要求
   - 提供清晰的指导
   - 限制幻觉

3. **选择合适的链类型**：
   - 少量文档：使用stuff
   - 大量文档：使用map_reduce或refine
   - 需要快速回答：使用map_rerank

4. **上下文管理**：
   - 控制上下文长度
   - 优先选择最相关的文档
   - 避免重复信息

5. **后处理**：
   - 检查回答是否基于文档
   - 添加引用来源
   - 格式化回答

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 回答不准确 | 检索结果不相关或提示模板不当 | 优化检索参数或提示模板 |
| 回答包含幻觉 | 语言模型编造信息 | 加强提示中的约束，限制模型自由发挥 |
| 回答不完整 | 上下文信息不足 | 增加检索结果数量或使用更适合的链类型 |
| 生成速度慢 | 语言模型推理速度慢 | 使用更轻量级的模型或优化链类型 |
| 上下文窗口不足 | 检索结果过多 | 减少检索结果数量或使用map_reduce链类型 |
