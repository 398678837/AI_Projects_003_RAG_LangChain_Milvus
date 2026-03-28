# Milvus安装

## 什么是Milvus？

Milvus是一个开源的向量数据库，专门用于存储和检索大规模的向量数据。它支持近似最近邻检索（ANN），可以高效地处理大规模的向量数据。

## 安装Milvus

### 1. 安装Milvus客户端

使用pip安装Milvus客户端：

```bash
pip install pymilvus
```

### 2. 安装Milvus服务器

#### 方式1：使用Docker安装

```bash
docker pull milvusdb/milvus:v2.3.0
docker run -d --name milvus -p 19530:19530 milvusdb/milvus:v2.3.0
```

#### 方式2：使用二进制安装

从Milvus官网下载二进制文件：

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.3.0/milvus-2.3.0-linux-amd64.tar.gz
tar -xzf milvus-2.3.0-linux-amd64.tar.gz
cd milvus-2.3.0-linux-amd64
./bin/milvus run standalone
```

### 3. 验证安装

导入Milvus客户端并连接到服务器：

```python
from pymilvus import connections

connections.connect("default", host="localhost", port="19530")
```

## 安装完成

安装完成后，您可以开始使用Milvus进行向量数据的存储和检索。

## 总结

Milvus是一个开源的向量数据库，安装简单，易于使用。本目录提供了Milvus的安装方法，帮助您快速掌握Milvus的安装技术。
