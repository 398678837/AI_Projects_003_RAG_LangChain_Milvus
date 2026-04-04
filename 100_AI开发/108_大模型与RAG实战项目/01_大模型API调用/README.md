# 大模型API调用

## 项目简介

本目录包含了各种大模型API的调用示例，帮助开发者快速上手大模型应用开发。

## 目录结构

```
01_大模型API调用/
├── 01_OpenAI_API调用示例.py          # OpenAI GPT模型调用
├── 02_百度文心一言API调用示例.py      # 百度文心一言模型调用
└── README.md                         # 本文件
```

## 环境配置

### 安装依赖
```bash
pip install openai python-dotenv requests
```

### 配置API密钥
创建`.env`文件，添加以下内容：
```env
# OpenAI API配置
OPENAI_API_KEY=your_openai_api_key

# 百度文心一言API配置
BAIDU_API_KEY=your_baidu_api_key
BAIDU_SECRET_KEY=your_baidu_secret_key
```

## 使用说明

### OpenAI API调用
```bash
python 01_OpenAI_API调用示例.py
```

### 百度文心一言API调用
```bash
python 02_百度文心一言API调用示例.py
```

## 常见问题

### API密钥获取
- **OpenAI API**: 访问 https://platform.openai.com/ 获取API密钥
- **百度文心一言API**: 访问 https://ai.baidu.com/ 获取API密钥

### 调用限制
- 不同模型有不同的调用频率限制
- 注意API调用费用
- 建议设置合理的超时时间

## 扩展建议

1. **添加错误处理** - 完善API调用的错误处理机制
2. **支持更多模型** - 添加其他大模型的API调用示例
3. **批量处理** - 实现批量文本生成功能
4. **结果缓存** - 缓存API调用结果，减少重复调用
5. **性能优化** - 异步调用多个API提高效率