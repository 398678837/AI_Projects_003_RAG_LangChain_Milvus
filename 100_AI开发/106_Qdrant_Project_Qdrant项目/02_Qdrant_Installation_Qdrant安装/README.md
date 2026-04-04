# Qdrant安装

## 什么是Qdrant？

Qdrant是一个轻量级、高性能的向量数据库，专门用于存储和检索向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 安装Qdrant

### 1. 安装Qdrant客户端

使用pip安装Qdrant客户端：

```bash
pip install qdrant-client
```

### 2. 安装Qdrant服务器

#### 方式1：使用Docker安装

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

#### 方式2：使用二进制安装

从Qdrant官网下载二进制文件：

```bash
wget https://github.com/qdrant/qdrant/releases/latest/download/qdrant-x86_64-unknown-linux-gnu.tar.gz
tar -xzf qdrant-x86_64-unknown-linux-gnu.tar.gz
./qdrant
```

### 3. 验证安装

导入Qdrant客户端并创建实例：

```python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
```

## 安装完成

安装完成后，您可以开始使用Qdrant进行向量数据的存储和检索。

## 总结

Qdrant是一个轻量级、高性能的向量数据库，安装简单，易于使用。本目录提供了Qdrant的安装方法，帮助您快速掌握Qdrant的安装技术。
