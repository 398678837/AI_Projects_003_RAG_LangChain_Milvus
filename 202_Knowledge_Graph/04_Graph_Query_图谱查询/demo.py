#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱查询
展示知识图谱的查询方法
"""

import networkx as nx
import matplotlib.pyplot as plt

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

# 2. 基础查询操作
print("\n=== 基础查询操作 ===")

# 查询所有节点
print("所有节点:")
for node in G.nodes():
    print(f"- {node}")

# 查询所有边
print("\n所有边:")
for u, v, d in G.edges(data=True):
    print(f"- {u} -> {v} ({d['relation']})")

# 查询节点属性
print("\n节点属性:")
for node, attrs in G.nodes(data=True):
    print(f"- {node}: {attrs}")

# 查询边属性
print("\n边属性:")
for u, v, attrs in G.edges(data=True):
    print(f"- {u} -> {v}: {attrs}")

# 3. 基于节点的查询
print("\n=== 基于节点的查询 ===")

# 查询特定节点
node = "Alice"
print(f"{node}的属性:")
if node in G:
    print(G.nodes[node])
else:
    print(f"节点{node}不存在")

# 查询节点的邻居
print(f"\n{node}的邻居:")
if node in G:
    neighbors = list(G.neighbors(node))
    print(neighbors)
else:
    print(f"节点{node}不存在")

# 查询节点的入边和出边
print(f"\n{node}的出边:")
if node in G:
    out_edges = list(G.out_edges(node, data=True))
    for u, v, d in out_edges:
        print(f"- {u} -> {v} ({d['relation']})")
else:
    print(f"节点{node}不存在")

print(f"\n{node}的入边:")
if node in G:
    in_edges = list(G.in_edges(node, data=True))
    for u, v, d in in_edges:
        print(f"- {u} -> {v} ({d['relation']})")
else:
    print(f"节点{node}不存在")

# 4. 基于关系的查询
print("\n=== 基于关系的查询 ===")

# 查询特定关系的边
relation = "雇佣"
print(f"关系为'{relation}'的边:")
for u, v, d in G.edges(data=True):
    if d.get("relation") == relation:
        print(f"- {u} -> {v}")

# 查询特定节点的特定关系
node = "Alice"
relation = "朋友"
print(f"\n{node}的'{relation}'关系:")
if node in G:
    for u, v, d in G.out_edges(node, data=True):
        if d.get("relation") == relation:
            print(f"- {u} -> {v}")
else:
    print(f"节点{node}不存在")

# 5. 路径查询
print("\n=== 路径查询 ===")

# 查询两个节点之间的最短路径
start_node = "Alice"
end_node = "David"
print(f"{start_node}到{end_node}的最短路径:")
try:
    path = nx.shortest_path(G, start_node, end_node)
    print(" -> ".join(path))
except nx.NetworkXNoPath:
    print(f"{start_node}和{end_node}之间没有路径")

# 查询两个节点之间的所有简单路径
print(f"\n{start_node}到{end_node}的所有简单路径:")
try:
    paths = list(nx.all_simple_paths(G, start_node, end_node, cutoff=3))
    for i, path in enumerate(paths):
        print(f"路径{i+1}: {' -> '.join(path)}")
except nx.NetworkXNoPath:
    print(f"{start_node}和{end_node}之间没有路径")

# 6. 模式匹配查询
print("\n=== 模式匹配查询 ===")

# 查询所有被公司雇佣的人
print("所有被公司雇佣的人:")
for u, v, d in G.edges(data=True):
    if d.get("relation") == "雇佣" and "公司" in v:
        print(f"- {u} 被 {v} 雇佣")

# 查询所有同事关系
print("\n所有同事关系:")
for u, v, d in G.edges(data=True):
    if d.get("relation") == "同事":
        print(f"- {u} 和 {v} 是同事")

# 7. 属性过滤查询
print("\n=== 属性过滤查询 ===")

# 查询年龄大于30的人
print("年龄大于30的人:")
for node, attrs in G.nodes(data=True):
    if "age" in attrs and attrs["age"] > 30:
        print(f"- {node}: {attrs['age']}岁")

# 查询科技行业的公司
print("\n科技行业的公司:")
for node, attrs in G.nodes(data=True):
    if "industry" in attrs and attrs["industry"] == "科技":
        print(f"- {node}")

# 查询2018年及以后雇佣的关系
print("\n2018年及以后雇佣的关系:")
for u, v, d in G.edges(data=True):
    if d.get("relation") == "雇佣" and d.get("since") >= 2018:
        print(f"- {u} 从 {d['since']} 年开始被 {v} 雇佣")

# 8. 复杂查询示例
print("\n=== 复杂查询示例 ===")

# 查询Alice的朋友的雇主
print("Alice的朋友的雇主:")
alice_friends = []
for u, v, d in G.edges(data=True):
    if u == "Alice" and d.get("relation") == "朋友":
        alice_friends.append(v)

for friend in alice_friends:
    for u, v, d in G.edges(data=True):
        if u == friend and d.get("relation") == "雇佣":
            print(f"- {friend} 的雇主是 {v}")

# 查询在同一家公司工作的人
print("\n在同一家公司工作的人:")
companies = {}
for u, v, d in G.edges(data=True):
    if d.get("relation") == "雇佣":
        if v not in companies:
            companies[v] = []
        companies[v].append(u)

for company, employees in companies.items():
    if len(employees) > 1:
        print(f"- {company} 的员工: {', '.join(employees)}")

# 9. 子图查询
print("\n=== 子图查询 ===")

# 创建公司相关的子图
company_nodes = [node for node in G.nodes() if "公司" in node]
person_nodes = [node for node in G.nodes() if "公司" not in node]

# 创建公司和人员的子图
company_subgraph = G.subgraph(company_nodes + person_nodes)

# 可视化子图
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(company_subgraph, seed=42)
nx.draw_networkx_nodes(company_subgraph, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(company_subgraph, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(company_subgraph, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in company_subgraph.edges(data=True)}
nx.draw_networkx_edge_labels(company_subgraph, pos, edge_labels=edge_labels, font_size=10)
plt.title("公司相关子图")
plt.axis("off")
plt.tight_layout()
plt.savefig("company_subgraph.png")
print("公司相关子图已保存为 company_subgraph.png")

# 10. 知识图谱查询的应用
print("\n=== 知识图谱查询的应用 ===")
print("知识图谱查询在以下场景中有广泛应用:")
print("1. 智能问答系统: 基于知识图谱的查询回答用户问题")
print("2. 信息检索: 提高搜索结果的相关性和准确性")
print("3. 推荐系统: 基于实体关系进行精准推荐")
print("4. 风险评估: 分析实体之间的关联风险")
print("5. 决策支持: 基于知识图谱的分析辅助决策")
print("6. 数据集成: 整合不同来源的数据")
print("7. 知识发现: 发现实体之间的潜在关系")

print("\n知识图谱查询示例完成！")
