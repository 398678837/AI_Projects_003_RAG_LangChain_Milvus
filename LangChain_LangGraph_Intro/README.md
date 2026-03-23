# LangChain + LangGraph 入门学习项目

本项目包含LangChain和LangGraph的入门示例，帮助开发者快速上手这两个强大的AI开发框架。

## 项目结构

```
LangChain_LangGraph_Intro/
├── README.md              # 项目说明文档
├── requirements.txt       # 依赖包配置文件
├── 101langchian/          # LangChain学习主文件夹
│   ├── 01基础问答链/       # 基础PromptTemplate+LLM链式调用
│   ├── 02进阶链结构/       # 更复杂的链结构示例
│   ├── 03集成外部工具/     # 集成外部工具的示例
│   └── 04实战应用/         # 实战应用示例
└── 102langgraph/          # LangGraph学习主文件夹
    ├── 01基础流程/         # 基础2节点+条件边示例
    ├── 02复杂流程/         # 更复杂的流程示例
    ├── 03状态管理/         # 状态管理示例
    └── 04实战应用/         # 实战应用示例
```

## 环境准备

1. 克隆本项目
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 配置环境变量：
   - 设置 `API_KEY` 环境变量，用于调用大模型API

## 学习路径

### LangChain学习路径
1. **01基础问答链**：学习基本的PromptTemplate和LLM调用
2. **02进阶链结构**：学习更复杂的链组合，如SequentialChain、RouterChain等
3. **03集成外部工具**：学习如何与外部系统交互
4. **04实战应用**：学习完整的应用开发

### LangGraph学习路径
1. **01基础流程**：学习基本的节点和条件边
2. **02复杂流程**：学习更复杂的流程设计
3. **03状态管理**：学习如何管理流程状态
4. **04实战应用**：学习完整的流程应用开发

## 运行示例

进入对应目录，运行示例代码：

```bash
python demo.py
```

## 注意事项

- 本项目使用Qwen等通用大模型，需要配置相应的API密钥
- 示例代码已做极简设计，便于理解和学习
- 每个示例都包含详细的注释和学习文档

## 贡献

欢迎提交Issue和Pull Request，共同完善本学习项目。