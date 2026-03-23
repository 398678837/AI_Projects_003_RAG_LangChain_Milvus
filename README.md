# LangChain + LangGraph + Matplotlib + Seaborn + Scikit-learn + Keras + FastAPI 入门学习项目

本项目包含LangChain、LangGraph、Matplotlib、Seaborn、Scikit-learn、Keras和FastAPI的入门示例，帮助开发者快速上手这些强大的AI开发、数据可视化、机器学习和Web框架。

## 项目结构

```
├── README.md              # 项目说明文档
├── requirements.txt       # 依赖包配置文件
├── 001_Matplotlib/        # Matplotlib学习主文件夹
│   ├── 01_Basic_Concepts_基础概念与环境/     # 基础概念和环境设置
│   ├── 02_Basic_Plots_基本图形绘制/           # 基本图形绘制
│   ├── 03_Styling_图形美化与定制/             # 图形美化与定制
│   ├── 04_Subplots_多子图布局/                # 多子图布局
│   ├── 05_3D_Plots_三维图形/                 # 三维图形
│   ├── 06_Interactive_Plots_交互式图形/       # 交互式图形
│   ├── 07_Data_Visualization_数据可视化实战/   # 数据可视化实战
│   └── 08_Best_Practices_常见问题与最佳实践/  # 常见问题与最佳实践
├── 002_Seaborn/           # Seaborn学习主文件夹
│   ├── 01_Basic_Concepts_基础概念与环境/     # 基础概念和环境设置
│   ├── 02_Basic_Plots_基本图形绘制/           # 基本图形绘制
│   ├── 03_Statistical_Plots_统计图形/         # 统计图形
│   ├── 04_Categorical_Plots_分类数据图形/     # 分类数据图形
│   ├── 05_Distribution_Plots_分布图形/        # 分布图形
│   ├── 06_Regression_Plots_回归图形/         # 回归图形
│   ├── 07_Heatmaps_热力图/                  # 热力图
│   └── 08_Real_World_实战应用/             # 实战应用
├── 003_Scikit-learn/      # Scikit-learn学习主文件夹
│   ├── 01_Basic_Concepts_基础概念与环境/     # 基础概念和环境设置
│   ├── 02_Data_Preprocessing_数据预处理/       # 数据预处理
│   ├── 03_Supervised_Learning_监督学习/       # 监督学习
│   ├── 04_Unsupervised_Learning_无监督学习/   # 无监督学习
│   ├── 05_Model_Evaluation_模型评估/          # 模型评估
│   ├── 06_Feature_Engineering_特征工程/       # 特征工程
│   ├── 07_Model_Selection_模型选择/           # 模型选择
│   └── 08_Real_World_实战应用/             # 实战应用
├── 004_Keras/             # Keras学习主文件夹
│   ├── 01_Basic_Concepts_基础概念与环境/     # 基础概念和环境设置
│   ├── 02_Model_Basics_模型基础/             # 模型基础
│   ├── 03_Sequential_Models_序列模型/        # 序列模型
│   ├── 04_Functional_API_函数式API/          # 函数式API
│   ├── 05_CNN_卷积神经网络/                 # 卷积神经网络
│   ├── 06_RNN_循环神经网络/                 # 循环神经网络
│   ├── 07_Transfer_Learning_迁移学习/        # 迁移学习
│   └── 08_Real_World_实战应用/             # 实战应用
├── 005_FastAPI/           # FastAPI学习主文件夹
│   ├── 01_Basic_Concepts_基础概念与环境/     # 基础概念和环境设置
│   ├── 02_RESTful_API_RESTful风格API/       # RESTful风格API
│   ├── 03_Routing_路由/                     # 路由
│   ├── 04_Request_Handling_请求处理/         # 请求处理
│   ├── 05_Response_Handling_响应处理/        # 响应处理
│   ├── 06_Data_Validation_数据验证/         # 数据验证
│   ├── 07_Dependency_Injection_依赖注入/    # 依赖注入
│   └── 08_Real_World_实战应用/             # 实战应用
├── 101_Langchian/         # LangChain学习主文件夹
│   ├── 01_Basic_Chain_基础问答链/            # 基础PromptTemplate+LLM链式调用
│   ├── 02_Advanced_Chain_进阶链结构/         # 更复杂的链结构示例
│   ├── 03_Tools_集成外部工具/                # 集成外部工具的示例
│   ├── 04_RAG_检索增强生成/                  # 检索增强生成示例
│   ├── 05_Agents_智能代理/                  # 智能代理示例
│   ├── 06_Memory_记忆管理/                  # 记忆管理示例
│   ├── 07_Evaluation_评估与优化/            # 评估与优化示例
│   └── 08_Real_World_实战应用/             # 实战应用示例
└── 102_Langgraph/         # LangGraph学习主文件夹
    ├── 01_Basic_Flow_基础流程/             # 基础2节点+条件边示例
    ├── 02_Advanced_Flow_复杂流程/          # 更复杂的流程示例
    ├── 03_State_Management_状态管理/       # 状态管理示例
    └── 04_Real_World_实战应用/            # 实战应用示例
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

### Matplotlib学习路径
1. **01_Basic_Concepts_基础概念与环境**：学习Matplotlib的基本概念和环境配置
2. **02_Basic_Plots_基本图形绘制**：学习基本图形的绘制方法
3. **03_Styling_图形美化与定制**：学习如何美化和定制图形
4. **04_Subplots_多子图布局**：学习如何创建多子图布局
5. **05_3D_Plots_三维图形**：学习如何绘制三维图形
6. **06_Interactive_Plots_交互式图形**：学习如何创建交互式图形
7. **07_Data_Visualization_数据可视化实战**：学习数据可视化的实际应用
8. **08_Best_Practices_常见问题与最佳实践**：学习常见问题的解决方案和最佳实践

### Seaborn学习路径
1. **01_Basic_Concepts_基础概念与环境**：学习Seaborn的基本概念和环境配置
2. **02_Basic_Plots_基本图形绘制**：学习Seaborn的基本图形绘制
3. **03_Statistical_Plots_统计图形**：学习Seaborn的统计图形
4. **04_Categorical_Plots_分类数据图形**：学习Seaborn的分类数据图形
5. **05_Distribution_Plots_分布图形**：学习Seaborn的分布图形
6. **06_Regression_Plots_回归图形**：学习Seaborn的回归图形
7. **07_Heatmaps_热力图**：学习Seaborn的热力图
8. **08_Real_World_实战应用**：学习Seaborn的实战应用

### Scikit-learn学习路径
1. **01_Basic_Concepts_基础概念与环境**：学习Scikit-learn的基本概念和环境配置
2. **02_Data_Preprocessing_数据预处理**：学习数据预处理方法
3. **03_Supervised_Learning_监督学习**：学习监督学习算法
4. **04_Unsupervised_Learning_无监督学习**：学习无监督学习算法
5. **05_Model_Evaluation_模型评估**：学习模型评估方法
6. **06_Feature_Engineering_特征工程**：学习特征工程技术
7. **07_Model_Selection_模型选择**：学习模型选择和调优
8. **08_Real_World_实战应用**：学习Scikit-learn的实战应用

### Keras学习路径
1. **01_Basic_Concepts_基础概念与环境**：学习Keras的基本概念和环境配置
2. **02_Model_Basics_模型基础**：学习Keras的模型基础操作
3. **03_Sequential_Models_序列模型**：学习序列模型的使用
4. **04_Functional_API_函数式API**：学习函数式API的使用
5. **05_CNN_卷积神经网络**：学习卷积神经网络的使用
6. **06_RNN_循环神经网络**：学习循环神经网络的使用
7. **07_Transfer_Learning_迁移学习**：学习迁移学习的使用
8. **08_Real_World_实战应用**：学习Keras的实战应用

### FastAPI学习路径
1. **01_Basic_Concepts_基础概念与环境**：学习FastAPI的基本概念和环境配置
2. **02_RESTful_API_RESTful风格API**：学习如何创建RESTful风格的API
3. **03_Routing_路由**：学习FastAPI的路由功能
4. **04_Request_Handling_请求处理**：学习如何处理请求
5. **05_Response_Handling_响应处理**：学习如何处理响应
6. **06_Data_Validation_数据验证**：学习数据验证功能
7. **07_Dependency_Injection_依赖注入**：学习依赖注入功能
8. **08_Real_World_实战应用**：学习FastAPI的实战应用

### LangChain学习路径
1. **01_Basic_Chain_基础问答链**：学习基本的PromptTemplate和LLM调用
2. **02_Advanced_Chain_进阶链结构**：学习更复杂的链组合，如SequentialChain
3. **03_Tools_集成外部工具**：学习如何与外部系统交互
4. **04_RAG_检索增强生成**：学习检索增强生成技术
5. **05_Agents_智能代理**：学习智能代理的创建和使用
6. **06_Memory_记忆管理**：学习如何管理对话记忆
7. **07_Evaluation_评估与优化**：学习如何评估和优化LangChain应用
8. **08_Real_World_实战应用**：学习完整的应用开发

### LangGraph学习路径
1. **01_Basic_Flow_基础流程**：学习基本的节点和条件边
2. **02_Advanced_Flow_复杂流程**：学习更复杂的流程设计
3. **03_State_Management_状态管理**：学习如何管理流程状态
4. **04_Real_World_实战应用**：学习完整的流程应用开发

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