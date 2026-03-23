# LangChain基础问答链

本示例展示了如何使用LangChain创建一个基础的问答链，使用PromptTemplate和LLM链式调用。

## 功能说明

- 使用PromptTemplate创建提示模板
- 使用LLMChain构建链式调用
- 适配Qwen等通用大模型
- 支持批量问答和交互式问答

## 代码结构

```python
# 1. 配置API密钥
# 2. 配置大模型
# 3. 创建Prompt模板
# 4. 创建LLM链
# 5. 测试问答
```

## 配置说明

1. **API密钥配置**：
   - 在环境变量中设置 `API_KEY`
   - 或直接在代码中修改 `api_key` 变量

2. **大模型配置**：
   - 默认使用Qwen模型的API地址
   - 可以根据需要修改 `base_url`

## 运行示例

1. 安装依赖：
   ```bash
   pip install -r ../../requirements.txt
   ```

2. 运行示例：
   ```bash
   python demo.py
   ```

3. 交互模式：
   - 输入问题，按回车获取回答
   - 输入'quit'退出

## 学习要点

- **PromptTemplate**：用于创建结构化的提示模板
- **LLMChain**：用于将提示模板和LLM连接起来
- **ChatOpenAI**：用于调用大模型API，支持OpenAI兼容接口
- **环境变量配置**：用于安全管理API密钥

## 扩展建议

- 尝试修改Prompt模板，优化回答质量
- 集成其他大模型，如Claude、Gemini等
- 添加更多输入变量，构建更复杂的提示模板