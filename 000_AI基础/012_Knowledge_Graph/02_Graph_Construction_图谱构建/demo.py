#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱构建
展示知识图谱的构建方法
"""

import networkx as nx
import matplotlib.pyplot as plt
import json
import csv

# 1. 从数据构建知识图谱
print("=== 从数据构建知识图谱 ===")

# 示例数据：人物关系
person_data = [
    {"name": "Alice", "age": 30, "gender": "女"},
    {"name": "Bob", "age": 25, "gender": "男"},
    {"name": "Charlie", "age": 35, "gender": "男"},
    {"name": "David", "age": 40, "gender": "男"},
    {"name": "Eve", "age": 28, "gender": "女"}
]

# 关系数据
relationship_data = [
    {"source": "Alice", "target": "Bob", "relation": "朋友", "since": 2015},
    {"source": "Alice", "target": "Charlie", "relation": "同事", "since": 2018},
    {"source": "Bob", "target": "David", "relation": "兄弟", "since": 1995},
    {"source": "Charlie", "target": "Eve", "relation": "夫妻", "since": 2020},
    {"source": "David", "target": "Eve", "relation": "朋友", "since": 2019}
]

# 创建知识图谱
G = nx.Graph()

# 添加节点
for person in person_data:
    G.add_node(person["name"], **{k: v for k, v in person.items() if k != "name"})

# 添加边
for relationship in relationship_data:
    G.add_edge(
        relationship["source"],
        relationship["target"],
        **{k: v for k, v in relationship.items() if k not in ["source", "target"]}
    )

# 打印图谱信息
print(f"节点数量: {G.number_of_nodes()}")
print(f"边数量: {G.number_of_edges()}")

# 可视化图谱
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): f"{d['relation']} ({d['since']})" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("人物关系知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("person_relationship_graph.png")
print("人物关系知识图谱已保存为 person_relationship_graph.png")

# 2. 从JSON数据构建知识图谱
print("\n=== 从JSON数据构建知识图谱 ===")

# 创建示例JSON数据
json_data = {
    "nodes": [
        {"id": "n1", "label": "电影", "name": "肖申克的救赎", "year": 1994, "rating": 9.7},
        {"id": "n2", "label": "电影", "name": "霸王别姬", "year": 1993, "rating": 9.6},
        {"id": "n3", "label": "导演", "name": "弗兰克·德拉邦特", "country": "美国"},
        {"id": "n4", "label": "导演", "name": "陈凯歌", "country": "中国"},
        {"id": "n5", "label": "演员", "name": "蒂姆·罗宾斯", "country": "美国"},
        {"id": "n6", "label": "演员", "name": "摩根·弗里曼", "country": "美国"},
        {"id": "n7", "label": "演员", "name": "张国荣", "country": "中国"},
        {"id": "n8", "label": "演员", "name": "巩俐", "country": "中国"}
    ],
    "edges": [
        {"source": "n1", "target": "n3", "label": "导演", "year": 1994},
        {"source": "n1", "target": "n5", "label": "主演", "year": 1994},
        {"source": "n1", "target": "n6", "label": "主演", "year": 1994},
        {"source": "n2", "target": "n4", "label": "导演", "year": 1993},
        {"source": "n2", "target": "n7", "label": "主演", "year": 1993},
        {"source": "n2", "target": "n8", "label": "主演", "year": 1993}
    ]
}

# 保存JSON数据
with open("movie_data.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
print("电影数据已保存为 movie_data.json")

# 从JSON数据构建图谱
movie_graph = nx.Graph()

# 添加节点
for node in json_data["nodes"]:
    node_id = node["id"]
    node_data = {k: v for k, v in node.items() if k != "id"}
    movie_graph.add_node(node_id, **node_data)

# 添加边
for edge in json_data["edges"]:
    source = edge["source"]
    target = edge["target"]
    edge_data = {k: v for k, v in edge.items() if k not in ["source", "target"]}
    movie_graph.add_edge(source, target, **edge_data)

# 可视化电影知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(movie_graph, seed=42)

# 为不同类型的节点设置不同的颜色
node_colors = []
for node, data in movie_graph.nodes(data=True):
    if data.get("label") == "电影":
        node_colors.append("lightgreen")
    elif data.get("label") == "导演":
        node_colors.append("lightblue")
    elif data.get("label") == "演员":
        node_colors.append("lightcoral")
    else:
        node_colors.append("lightgray")

# 绘制节点
nx.draw_networkx_nodes(movie_graph, pos, node_size=1000, node_color=node_colors)

# 绘制边
nx.draw_networkx_edges(movie_graph, pos, width=2, edge_color="gray")

# 绘制节点标签（使用name属性）
node_labels = {node: data.get("name", node) for node, data in movie_graph.nodes(data=True)}
nx.draw_networkx_labels(movie_graph, pos, labels=node_labels, font_size=10, font_weight="bold")

# 绘制边标签
edge_labels = {(u, v): d["label"] for u, v, d in movie_graph.edges(data=True)}
nx.draw_networkx_edge_labels(movie_graph, pos, edge_labels=edge_labels, font_size=8)

plt.title("电影知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("movie_knowledge_graph.png")
print("电影知识图谱已保存为 movie_knowledge_graph.png")

# 3. 从CSV数据构建知识图谱
print("\n=== 从CSV数据构建知识图谱 ===")

# 创建示例CSV数据
csv_data = [
    ["source", "target", "relation", "weight"],
    ["Python", "NumPy", "依赖", 10],
    ["Python", "Pandas", "依赖", 9],
    ["Python", "Matplotlib", "依赖", 8],
    ["NumPy", "Pandas", "依赖", 7],
    ["NumPy", "Matplotlib", "依赖", 6],
    ["Pandas", "Matplotlib", "依赖", 5],
    ["Python", "Scikit-learn", "依赖", 8],
    ["NumPy", "Scikit-learn", "依赖", 9],
    ["Pandas", "Scikit-learn", "依赖", 6]
]

# 保存CSV数据
with open("python_ecosystem.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print("Python生态系统数据已保存为 python_ecosystem.csv")

# 从CSV数据构建图谱
ecosystem_graph = nx.DiGraph()

# 读取CSV数据并添加边
with open("python_ecosystem.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        source = row["source"]
        target = row["target"]
        relation = row["relation"]
        weight = int(row["weight"])
        ecosystem_graph.add_edge(source, target, relation=relation, weight=weight)

# 可视化生态系统知识图谱
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(ecosystem_graph, seed=42)

# 绘制节点
nx.draw_networkx_nodes(ecosystem_graph, pos, node_size=1500, node_color="lightyellow")

# 绘制边，使用权重作为线宽
edges = ecosystem_graph.edges(data=True)
edge_weights = [d["weight"]/2 for u, v, d in edges]
nx.draw_networkx_edges(ecosystem_graph, pos, width=edge_weights, edge_color="gray", arrows=True, arrowsize=20)

# 绘制节点标签
nx.draw_networkx_labels(ecosystem_graph, pos, font_size=12, font_weight="bold")

# 绘制边标签
edge_labels = {(u, v): f"{d['relation']} ({d['weight']})" for u, v, d in edges}
nx.draw_networkx_edge_labels(ecosystem_graph, pos, edge_labels=edge_labels, font_size=8)

plt.title("Python生态系统知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("python_ecosystem_graph.png")
print("Python生态系统知识图谱已保存为 python_ecosystem_graph.png")

# 4. 知识图谱的层次结构
print("\n=== 知识图谱的层次结构 ===")

# 创建层次化知识图谱
hierarchy_graph = nx.DiGraph()

# 添加节点
levels = {
    "领域": ["计算机科学", "数学", "物理学"],
    "学科": ["人工智能", "数据结构", "代数", "几何", "力学", "光学"],
    "子学科": ["机器学习", "深度学习", "图论", "算法", "线性代数", "微积分", "经典力学", "量子力学", "几何光学", "物理光学"]
}

# 添加节点
for level, items in levels.items():
    for item in items:
        hierarchy_graph.add_node(item, level=level)

# 添加边
edges = [
    ("计算机科学", "人工智能"),
    ("计算机科学", "数据结构"),
    ("数学", "代数"),
    ("数学", "几何"),
    ("物理学", "力学"),
    ("物理学", "光学"),
    ("人工智能", "机器学习"),
    ("人工智能", "深度学习"),
    ("数据结构", "图论"),
    ("数据结构", "算法"),
    ("代数", "线性代数"),
    ("代数", "微积分"),
    ("几何", "微积分"),
    ("力学", "经典力学"),
    ("力学", "量子力学"),
    ("光学", "几何光学"),
    ("光学", "物理光学")
]

for source, target in edges:
    hierarchy_graph.add_edge(source, target, relation="包含")

# 可视化层次化知识图谱
plt.figure(figsize=(15, 10))

# 使用层次布局
pos = nx.multipartite_layout(hierarchy_graph, subset_key="level", align="vertical")

# 为不同层次的节点设置不同的颜色
node_colors = []
for node, data in hierarchy_graph.nodes(data=True):
    if data.get("level") == "领域":
        node_colors.append("lightblue")
    elif data.get("level") == "学科":
        node_colors.append("lightgreen")
    elif data.get("level") == "子学科":
        node_colors.append("lightcoral")
    else:
        node_colors.append("lightgray")

# 绘制节点
nx.draw_networkx_nodes(hierarchy_graph, pos, node_size=1000, node_color=node_colors)

# 绘制边
nx.draw_networkx_edges(hierarchy_graph, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)

# 绘制节点标签
nx.draw_networkx_labels(hierarchy_graph, pos, font_size=10, font_weight="bold")

plt.title("知识层次结构图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("hierarchy_graph.png")
print("知识层次结构图谱已保存为 hierarchy_graph.png")

# 5. 知识图谱的属性扩展
print("\n=== 知识图谱的属性扩展 ===")

# 扩展人物关系图谱
G.add_node("Frank", age=32, gender="男", occupation="工程师")
G.add_edge("Alice", "Frank", relation="同学", since=2010)
G.add_edge("Frank", "David", relation="同事", since=2021)

# 更新节点属性
G.nodes["Alice"]["occupation"] = "设计师"
G.nodes["Bob"]["occupation"] = "教师"

# 更新边属性
G["Alice"]["Bob"]["strength"] = "强"
G["Charlie"]["Eve"]["strength"] = "强"

# 可视化扩展后的图谱
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
edge_labels = {}
for u, v, d in G.edges(data=True):
    label = d.get("relation")
    if "since" in d:
        label += f" ({d['since']})"
    if "strength" in d:
        label += f" ({d['strength']})"
    edge_labels[(u, v)] = label
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("扩展后的人物关系知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("extended_person_graph.png")
print("扩展后的人物关系知识图谱已保存为 extended_person_graph.png")

print("\n知识图谱构建示例完成！")
