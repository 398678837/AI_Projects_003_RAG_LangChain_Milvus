#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱嵌入
展示知识图谱嵌入的基本方法
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 1. 构建示例知识图谱
print("=== 构建示例知识图谱 ===")

# 创建知识图谱
G = nx.DiGraph()

# 添加节点（实体）
G.add_node("Alice", age=30, gender="女", occupation="设计师")
G.add_node("Bob", age=25, gender="男", occupation="教师")
G.add_node("Charlie", age=35, gender="男", occupation="工程师")
G.add_node("David", age=40, gender="男", occupation="医生")
G.add_node("Eve", age=28, gender="女", occupation="护士")
G.add_node("公司A", industry="科技", founded=2000)
G.add_node("公司B", industry="金融", founded=1995)
G.add_node("公司C", industry="医疗", founded=2010)

# 添加边（关系）
G.add_edge("Alice", "公司A", relation="雇佣", since=2018)
G.add_edge("Bob", "公司B", relation="雇佣", since=2020)
G.add_edge("Charlie", "公司A", relation="雇佣", since=2019)
G.add_edge("David", "公司C", relation="雇佣", since=2015)
G.add_edge("Eve", "公司C", relation="雇佣", since=2017)
G.add_edge("Alice", "Bob", relation="朋友", since=2015)
G.add_edge("Bob", "Charlie", relation="同事", since=2019)
G.add_edge("Charlie", "David", relation="朋友", since=2016)
G.add_edge("David", "Eve", relation="同事", since=2015)

# 可视化知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("示例知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("example_knowledge_graph.png")
print("示例知识图谱已保存为 example_knowledge_graph.png")

# 2. 基于邻接矩阵的嵌入
print("\n=== 基于邻接矩阵的嵌入 ===")

# 构建邻接矩阵
adj_matrix = nx.adjacency_matrix(G).todense()
print("邻接矩阵:")
print(adj_matrix)

# 计算节点度
node_degree = np.sum(adj_matrix, axis=1)
print("\n节点度:")
for i, node in enumerate(G.nodes()):
    print(f"{node}: {node_degree[i, 0]}")

# 3. 基于拉普拉斯矩阵的嵌入
print("\n=== 基于拉普拉斯矩阵的嵌入 ===")

# 计算拉普拉斯矩阵
laplacian_matrix = nx.laplacian_matrix(G).todense()
print("拉普拉斯矩阵:")
print(laplacian_matrix)

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)
print("\n前5个特征值:")
print(eigenvalues[:5])

# 4. 基于DeepWalk的嵌入
print("\n=== 基于DeepWalk的嵌入 ===")

def deepwalk_embedding(graph, walk_length=5, num_walks=10, embedding_dim=2):
    """简单实现DeepWalk算法"""
    import random
    
    # 构建词汇表
    nodes = list(graph.nodes())
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    
    # 生成随机游走
    walks = []
    for _ in range(num_walks):
        for node in nodes:
            walk = [node]
            current_node = node
            for _ in range(walk_length - 1):
                neighbors = list(graph.neighbors(current_node))
                if neighbors:
                    current_node = random.choice(neighbors)
                    walk.append(current_node)
                else:
                    break
            walks.append(walk)
    
    # 构建共现矩阵
    vocab_size = len(nodes)
    co_occurrence_matrix = np.zeros((vocab_size, vocab_size))
    
    for walk in walks:
        for i, node in enumerate(walk):
            for j, context_node in enumerate(walk):
                if i != j:
                    co_occurrence_matrix[node_to_idx[node], node_to_idx[context_node]] += 1
    
    # 使用SVD进行降维
    u, s, vh = np.linalg.svd(co_occurrence_matrix)
    embedding = u[:, :embedding_dim]
    
    return embedding, node_to_idx

# 生成DeepWalk嵌入
embedding, node_to_idx = deepwalk_embedding(G, walk_length=5, num_walks=10, embedding_dim=2)
print("DeepWalk嵌入结果:")
for node, idx in node_to_idx.items():
    print(f"{node}: {embedding[idx]}")

# 5. 嵌入可视化
print("\n=== 嵌入可视化 ===")

# 使用PCA降维到2维
if embedding.shape[1] > 2:
    pca = PCA(n_components=2)
    embedding_2d = pca.fit_transform(embedding)
else:
    embedding_2d = embedding

# 可视化嵌入
plt.figure(figsize=(12, 8))
for node, idx in node_to_idx.items():
    x, y = embedding_2d[idx]
    plt.scatter(x, y, s=100, color="blue")
    plt.text(x + 0.01, y + 0.01, node, fontsize=12, fontweight="bold")

plt.title("DeepWalk嵌入可视化")
plt.xlabel("维度1")
plt.ylabel("维度2")
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_embedding.png")
print("图谱嵌入可视化已保存为 graph_embedding.png")

# 6. 基于节点属性的嵌入
print("\n=== 基于节点属性的嵌入 ===")

# 提取节点属性
node_attributes = []
nodes = list(G.nodes())
for node in nodes:
    attrs = G.nodes[node]
    # 将属性转换为数值
    attr_vector = []
    if "age" in attrs:
        attr_vector.append(attrs["age"])
    else:
        attr_vector.append(0)
    if "gender" in attrs:
        attr_vector.append(1 if attrs["gender"] == "男" else 0)
    else:
        attr_vector.append(0)
    if "industry" in attrs:
        # 简单的行业编码
        industry_map = {"科技": 0, "金融": 1, "医疗": 2}
        attr_vector.append(industry_map.get(attrs["industry"], 0))
    else:
        attr_vector.append(0)
    if "founded" in attrs:
        attr_vector.append(attrs["founded"])
    else:
        attr_vector.append(0)
    node_attributes.append(attr_vector)

node_attributes = np.array(node_attributes)
print("节点属性矩阵:")
print(node_attributes)

# 7. 组合结构和属性的嵌入
print("\n=== 组合结构和属性的嵌入 ===")

# 归一化属性
normalized_attributes = (node_attributes - node_attributes.mean(axis=0)) / (node_attributes.std(axis=0) + 1e-8)

# 组合结构嵌入和属性嵌入
combined_embedding = np.hstack((embedding, normalized_attributes))
print("组合嵌入形状:", combined_embedding.shape)

# 可视化组合嵌入
pca = PCA(n_components=2)
combined_embedding_2d = pca.fit_transform(combined_embedding)

plt.figure(figsize=(12, 8))
for i, node in enumerate(nodes):
    x, y = combined_embedding_2d[i]
    plt.scatter(x, y, s=100, color="green")
    plt.text(x + 0.01, y + 0.01, node, fontsize=12, fontweight="bold")

plt.title("组合嵌入可视化")
plt.xlabel("维度1")
plt.ylabel("维度2")
plt.grid(True)
plt.tight_layout()
plt.savefig("combined_embedding.png")
print("组合嵌入可视化已保存为 combined_embedding.png")

# 8. 嵌入的应用
print("\n=== 嵌入的应用 ===")

# 计算节点相似度
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 计算Alice与其他节点的相似度
print("Alice与其他节点的相似度:")
alice_idx = node_to_idx["Alice"]
alice_embedding = embedding[alice_idx]
for node, idx in node_to_idx.items():
    if node != "Alice":
        similarity = cosine_similarity(alice_embedding, embedding[idx])
        print(f"Alice与{node}的相似度: {similarity:.4f}")

# 9. 图谱嵌入的评估
print("\n=== 图谱嵌入的评估 ===")

# 评估嵌入质量 - 计算邻居保留率
def evaluate_embedding(graph, embedding, node_to_idx, top_k=2):
    """评估嵌入质量，计算邻居保留率"""
    nodes = list(graph.nodes())
    correct = 0
    total = 0
    
    for node in nodes:
        # 获取真实邻居
        real_neighbors = set(graph.neighbors(node))
        if not real_neighbors:
            continue
        
        # 计算与其他节点的相似度
        node_idx = node_to_idx[node]
        node_emb = embedding[node_idx]
        similarities = []
        
        for other_node in nodes:
            if other_node != node:
                other_idx = node_to_idx[other_node]
                other_emb = embedding[other_idx]
                sim = cosine_similarity(node_emb, other_emb)
                similarities.append((other_node, sim))
        
        # 排序并取前k个
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_k_nodes = [x[0] for x in similarities[:top_k]]
        
        # 计算正确预测的邻居数
        for neighbor in top_k_nodes:
            if neighbor in real_neighbors:
                correct += 1
        total += top_k
    
    # 计算准确率
    accuracy = correct / total if total > 0 else 0
    return accuracy

accuracy = evaluate_embedding(G, embedding, node_to_idx, top_k=2)
print(f"嵌入评估准确率: {accuracy:.4f}")

# 10. 图谱嵌入的挑战与解决方案
print("\n=== 图谱嵌入的挑战与解决方案 ===")
print("图谱嵌入面临的主要挑战:")
print(1. 大规模图谱: 处理大型知识图谱的计算复杂度问题")
print(2. 动态图谱: 处理图谱结构变化的问题")
print(3. 多关系处理: 处理复杂关系类型的问题")
print(4. 冷启动问题: 处理新加入节点的嵌入问题")
print(5. 评估困难: 缺乏统一的评估标准")

print("\n解决方案:")
print(1. 采用高效的嵌入算法，如Node2Vec、GraphSAGE等")
print(2. 增量学习方法，适应图谱结构变化")
print(3. 关系感知的嵌入模型，如TransE、DistMult等")
print(4. 基于属性的嵌入初始化方法")
print(5. 建立多维度的评估体系)

# 11. 图谱嵌入的应用场景
print("\n=== 图谱嵌入的应用场景 ===")
print("1. 节点分类: 基于嵌入进行节点分类")
print("2. 链接预测: 预测节点之间的潜在连接")
print("3. 推荐系统: 基于实体嵌入进行推荐")
print("4. 知识图谱补全: 补全知识图谱中的缺失信息")
print("5. 异常检测: 基于嵌入识别异常节点或边")
print("6. 聚类分析: 基于嵌入对节点进行聚类")
print("7. 可视化: 低维嵌入用于图谱可视化")

print("\n知识图谱嵌入示例完成！")
