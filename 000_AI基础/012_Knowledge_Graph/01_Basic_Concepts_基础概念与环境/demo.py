#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱基础概念与环境
展示知识图谱的基础概念和环境设置
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 1. 基础概念介绍
print("=== 知识图谱基础概念 ===")
print("知识图谱是一种以图形结构表示知识的方法，由节点（实体）和边（关系）组成。")
print("核心概念包括：")
print("- 实体：现实世界中的对象，如人物、组织、地点等")
print("- 关系：实体之间的联系，如父子、雇佣、位于等")
print("- 属性：实体的特征，如年龄、性别、地址等")
print("- 三元组：知识的基本表示形式，如 (主语, 谓语, 宾语)")

# 2. 环境检查
print("\n=== 环境检查 ===")
try:
    import networkx
    print(f"NetworkX版本: {networkx.__version__}")
except ImportError:
    print("NetworkX未安装")

try:
    import matplotlib
    print(f"Matplotlib版本: {matplotlib.__version__}")
except ImportError:
    print("Matplotlib未安装")

try:
    import numpy
    print(f"NumPy版本: {numpy.__version__}")
except ImportError:
    print("NumPy未安装")

# 3. 简单知识图谱创建
print("\n=== 简单知识图谱创建 ===")

# 创建一个无向图
G = nx.Graph()

# 添加节点（实体）
G.add_node("Alice", age=30, gender="女")
G.add_node("Bob", age=25, gender="男")
G.add_node("Charlie", age=35, gender="男")
G.add_node("公司A", industry="科技")
G.add_node("公司B", industry="金融")

# 添加边（关系）
G.add_edge("Alice", "Bob", relation="朋友")
G.add_edge("Alice", "公司A", relation="雇佣")
G.add_edge("Bob", "公司B", relation="雇佣")
G.add_edge("Charlie", "公司A", relation="雇佣")
G.add_edge("Charlie", "Bob", relation="同事")

# 打印图谱信息
print(f"节点数量: {G.number_of_nodes()}")
print(f"边数量: {G.number_of_edges()}")
print("\n节点属性:")
for node, attrs in G.nodes(data=True):
    print(f"{node}: {attrs}")

print("\n边属性:")
for u, v, attrs in G.edges(data=True):
    print(f"{u} - {v}: {attrs}")

# 4. 图谱可视化
print("\n=== 图谱可视化 ===")

# 设置节点位置
pos = nx.spring_layout(G, seed=42)

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="lightblue")

# 绘制边
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")

# 绘制节点标签
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

# 绘制边标签
edge_labels = {(u, v): d["relation"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# 设置图形大小和标题
plt.figure(figsize=(12, 8))
plt.title("简单知识图谱示例")
plt.axis("off")
plt.tight_layout()

# 保存图谱
plt.savefig("knowledge_graph.png")
print("知识图谱已保存为 knowledge_graph.png")

# 5. 有向图示例
print("\n=== 有向图示例 ===")

# 创建有向图
DG = nx.DiGraph()

# 添加节点
DG.add_node("北京", population=2154)
DG.add_node("上海", population=2424)
DG.add_node("广州", population=1530)
DG.add_node("深圳", population=1343)

# 添加有向边
DG.add_edge("北京", "上海", distance=1318)
DG.add_edge("上海", "广州", distance=1430)
DG.add_edge("广州", "深圳", distance=147)
DG.add_edge("北京", "广州", distance=2100)

# 可视化有向图
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(DG, seed=42)
nx.draw_networkx_nodes(DG, pos, node_size=1000, node_color="lightgreen")
nx.draw_networkx_edges(DG, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(DG, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): f"距离: {d['distance']}km" for u, v, d in DG.edges(data=True)}
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, font_size=10)
plt.title("中国城市关系有向图")
plt.axis("off")
plt.tight_layout()
plt.savefig("directed_knowledge_graph.png")
print("有向知识图谱已保存为 directed_knowledge_graph.png")

# 6. 知识图谱的基本操作
print("\n=== 知识图谱的基本操作 ===")

# 节点操作
print("\n节点操作:")
print(f"所有节点: {list(G.nodes())}")
print(f"包含Alice节点: {'Alice' in G}")
print(f"Alice的邻居: {list(G.neighbors('Alice'))}")

# 边操作
print("\n边操作:")
print(f"所有边: {list(G.edges())}")
print(f"Alice和Bob之间有边: {'Alice' in G and 'Bob' in G and G.has_edge('Alice', 'Bob')}")
print(f"Alice和Bob之间的关系: {G['Alice']['Bob']['relation']}")

# 路径查询
print("\n路径查询:")
try:
    path = nx.shortest_path(G, "Alice", "Charlie")
    print(f"Alice到Charlie的最短路径: {' -> '.join(path)}")
except nx.NetworkXNoPath:
    print("Alice和Charlie之间没有路径")

# 度分析
print("\n度分析:")
print("节点度:")
for node in G.nodes():
    print(f"{node}: {G.degree(node)}")

# 7. 知识图谱的存储与加载
print("\n=== 知识图谱的存储与加载 ===")

# 保存图谱
nx.write_graphml(G, "knowledge_graph.graphml")
print("知识图谱已保存为 knowledge_graph.graphml")

# 加载图谱
loaded_graph = nx.read_graphml("knowledge_graph.graphml")
print(f"加载的图谱节点数量: {loaded_graph.number_of_nodes()}")
print(f"加载的图谱边数量: {loaded_graph.number_of_edges()}")

# 8. 知识图谱的应用场景
print("\n=== 知识图谱的应用场景 ===")
print("知识图谱在以下领域有广泛应用:")
print("1. 智能问答系统: 基于知识图谱的问答可以提供更准确的答案")
print("2. 推荐系统: 利用实体之间的关系进行更精准的推荐")
print("3. 信息检索: 提高搜索结果的相关性和准确性")
print("4. 金融风控: 识别欺诈行为和风险关联")
print("5. 医疗健康: 整合医疗知识，辅助诊断和治疗")
print("6. 供应链管理: 优化供应链流程，识别风险")
print("7. 语义理解: 增强自然语言处理能力")

print("\n知识图谱基础概念与环境设置示例完成！")
