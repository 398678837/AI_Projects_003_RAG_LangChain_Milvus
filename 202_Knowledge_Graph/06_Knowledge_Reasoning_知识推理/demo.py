#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识推理
展示知识图谱的推理方法
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
G.add_node("北京", population=2154, country="中国")
G.add_node("上海", population=2424, country="中国")
G.add_node("纽约", population=8337, country="美国")

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
G.add_edge("Alice", "北京", relation="居住", since=2010)
G.add_edge("Bob", "上海", relation="居住", since=2018)
G.add_edge("Charlie", "北京", relation="居住", since=2015)
G.add_edge("David", "上海", relation="居住", since=2012)
G.add_edge("Eve", "北京", relation="居住", since=2014)
G.add_edge("公司A", "北京", relation="位于", since=2000)
G.add_edge("公司B", "上海", relation="位于", since=1995)
G.add_edge("公司C", "北京", relation="位于", since=2010)

# 可视化知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("示例知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("example_knowledge_graph.png")
print("示例知识图谱已保存为 example_knowledge_graph.png")

# 2. 基于规则的推理
print("\n=== 基于规则的推理 ===")

# 定义推理规则
def infer_employment_location(graph):
    """推理员工的工作地点"""
    inferences = []
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "雇佣":
            # 查找公司的位置
            for company, location, d2 in graph.edges(data=True):
                if company == v and d2.get("relation") == "位于":
                    inferences.append((u, "工作地点", location))
    return inferences

def infer_colleagues(graph):
    """推理同事关系"""
    inferences = []
    # 查找在同一家公司工作的人
    companies = {}
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "雇佣":
            if v not in companies:
                companies[v] = []
            companies[v].append(u)
    
    # 为同一家公司的人添加同事关系
    for company, employees in companies.items():
        for i in range(len(employees)):
            for j in range(i + 1, len(employees)):
                # 检查是否已经存在同事关系
                if not graph.has_edge(employees[i], employees[j]) or graph[employees[i]][employees[j]].get("relation") != "同事":
                    inferences.append((employees[i], "同事", employees[j]))
    return inferences

def infer_friend_of_friend(graph):
    """推理朋友的朋友关系"""
    inferences = []
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "朋友":
            # 查找v的朋友
            for v2, w, d2 in graph.edges(data=True):
                if v2 == v and d2.get("relation") == "朋友" and u != w:
                    # 检查是否已经存在朋友关系
                    if not graph.has_edge(u, w) or graph[u][w].get("relation") != "朋友":
                        inferences.append((u, "朋友的朋友", w))
    return inferences

# 执行推理
employment_location_inferences = infer_employment_location(G)
colleague_inferences = infer_colleagues(G)
friend_of_friend_inferences = infer_friend_of_friend(G)

print("推理结果 - 员工工作地点:")
for subject, relation, object_ in employment_location_inferences:
    print(f"{subject} - {relation} -> {object_}")

print("\n推理结果 - 同事关系:")
for subject, relation, object_ in colleague_inferences:
    print(f"{subject} - {relation} -> {object_}")

print("\n推理结果 - 朋友的朋友:")
for subject, relation, object_ in friend_of_friend_inferences:
    print(f"{subject} - {relation} -> {object_}")

# 3. 基于路径的推理
print("\n=== 基于路径的推理 ===")

def infer_connections(graph, start_node, max_depth=3):
    """基于路径推理节点之间的连接"""
    connections = {}
    for node in graph.nodes():
        if node == start_node:
            continue
        try:
            paths = list(nx.all_simple_paths(graph, start_node, node, cutoff=max_depth))
            if paths:
                connections[node] = paths
        except nx.NetworkXNoPath:
            pass
    return connections

# 推理Alice的所有连接
alice_connections = infer_connections(G, "Alice", max_depth=3)
print("Alice的连接路径:")
for node, paths in alice_connections.items():
    print(f"\nAlice到{node}的路径:")
    for path in paths:
        print(" -> ".join(path))

# 4. 基于属性的推理
print("\n=== 基于属性的推理 ===")

def infer_age_group(graph):
    """基于年龄推理年龄组"""
    inferences = []
    for node, attrs in graph.nodes(data=True):
        if "age" in attrs:
            age = attrs["age"]
            if age < 30:
                age_group = "青年"
            elif age < 40:
                age_group = "中年"
            else:
                age_group = "老年"
            inferences.append((node, "年龄组", age_group))
    return inferences

def infer_company_size(graph):
    """基于员工数量推理公司规模"""
    inferences = []
    # 统计每个公司的员工数量
    company_employees = {}
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "雇佣":
            if v not in company_employees:
                company_employees[v] = 0
            company_employees[v] += 1
    
    # 推理公司规模
    for company, count in company_employees.items():
        if count < 2:
            size = "小型公司"
        elif count < 5:
            size = "中型公司"
        else:
            size = "大型公司"
        inferences.append((company, "公司规模", size))
    return inferences

# 执行基于属性的推理
age_group_inferences = infer_age_group(G)
company_size_inferences = infer_company_size(G)

print("推理结果 - 年龄组:")
for subject, relation, object_ in age_group_inferences:
    print(f"{subject} - {relation} -> {object_}")

print("\n推理结果 - 公司规模:")
for subject, relation, object_ in company_size_inferences:
    print(f"{subject} - {relation} -> {object_}")

# 5. 知识图谱补全
print("\n=== 知识图谱补全 ===")

def predict_missing_connections(graph, relation_type, top_k=2):
    """预测缺失的连接"""
    potential_connections = []
    
    # 获取所有节点
    nodes = list(graph.nodes())
    
    # 计算节点之间的相似度（基于共同邻居）
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node1 = nodes[i]
            node2 = nodes[j]
            
            # 跳过已存在的连接
            if graph.has_edge(node1, node2) or graph.has_edge(node2, node1):
                continue
            
            # 计算共同邻居
            neighbors1 = set(graph.neighbors(node1))
            neighbors2 = set(graph.neighbors(node2))
            common_neighbors = neighbors1.intersection(neighbors2)
            similarity = len(common_neighbors)
            
            if similarity > 0:
                potential_connections.append((node1, node2, similarity))
    
    # 按相似度排序
    potential_connections.sort(key=lambda x: x[2], reverse=True)
    
    # 返回前k个潜在连接
    return potential_connections[:top_k]

# 预测缺失的朋友关系
potential_friends = predict_missing_connections(G, "朋友", top_k=3)
print("预测缺失的朋友关系:")
for node1, node2, similarity in potential_friends:
    print(f"{node1} 和 {node2} 可能是朋友（相似度: {similarity}）")

# 6. 基于逻辑的推理
print("\n=== 基于逻辑的推理 ===")

def logical_reasoning(graph):
    """基于逻辑规则的推理"""
    inferences = []
    
    # 规则1: 如果A住在X，B也住在X，那么A和B可能是邻居
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "居住":
            location = v
            # 查找其他住在同一地点的人
            for u2, v2, d2 in graph.edges(data=True):
                if d2.get("relation") == "居住" and v2 == location and u != u2:
                    # 检查是否已经存在邻居关系
                    if not graph.has_edge(u, u2) or graph[u][u2].get("relation") != "邻居":
                        inferences.append((u, "邻居", u2))
    
    # 规则2: 如果A为X工作，X位于Y，那么A可能在Y工作
    for u, v, d in graph.edges(data=True):
        if d.get("relation") == "雇佣":
            company = v
            # 查找公司的位置
            for c, l, d2 in graph.edges(data=True):
                if c == company and d2.get("relation") == "位于":
                    location = l
                    # 检查是否已经存在工作地点关系
                    found = False
                    for u3, v3, d3 in graph.edges(data=True):
                        if u3 == u and v3 == location and d3.get("relation") == "工作地点":
                            found = True
                            break
                    if not found:
                        inferences.append((u, "工作地点", location))
    
    return inferences

# 执行逻辑推理
logical_inferences = logical_reasoning(G)
print("基于逻辑的推理结果:")
for subject, relation, object_ in logical_inferences:
    print(f"{subject} - {relation} -> {object_}")

# 7. 推理结果可视化
print("\n=== 推理结果可视化 ===")

# 创建包含推理结果的新图谱
G_inferred = G.copy()

# 添加推理结果
all_inferences = employment_location_inferences + colleague_inferences + friend_of_friend_inferences + age_group_inferences + company_size_inferences + logical_inferences

for subject, relation, object_ in all_inferences:
    if not G_inferred.has_edge(subject, object_):
        G_inferred.add_edge(subject, object_, relation=relation, inferred=True)

# 可视化包含推理结果的图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G_inferred, seed=42)

# 绘制原始节点和边
nx.draw_networkx_nodes(G_inferred, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(G_inferred, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)

# 绘制推理的边
inferred_edges = [(u, v) for u, v, d in G_inferred.edges(data=True) if d.get("inferred")]
nx.draw_networkx_edges(G_inferred, pos, edgelist=inferred_edges, width=2, edge_color="red", style="dashed", arrows=True, arrowsize=20)

# 绘制标签
nx.draw_networkx_labels(G_inferred, pos, font_size=10, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in G_inferred.edges(data=True)}
nx.draw_networkx_edge_labels(G_inferred, pos, edge_labels=edge_labels, font_size=8)

plt.title("包含推理结果的知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("inferred_knowledge_graph.png")
print("包含推理结果的知识图谱已保存为 inferred_knowledge_graph.png")

# 8. 知识推理的挑战与解决方案
print("\n=== 知识推理的挑战与解决方案 ===")
print("知识推理面临的主要挑战:")
print(1. 知识图谱不完整: 知识图谱中存在缺失的实体和关系")
print(2. 知识图谱噪声: 知识图谱中存在错误的信息)
print(3. 推理复杂度: 大规模知识图谱的推理计算复杂度高)
print(4. 多源知识融合: 融合不同来源的知识进行推理)
print(5. 动态知识更新: 处理知识图谱的动态变化)

print("\n解决方案:")
print(1. 知识图谱补全技术: 预测和补全缺失的知识)
print(2. 知识图谱清洗: 识别和纠正错误信息)
print(3. 高效推理算法: 设计可扩展的推理算法)
print(4. 知识融合方法: 融合多源知识的方法)
print(5. 增量推理技术: 处理动态知识的增量推理)

# 9. 知识推理的应用场景
print("\n=== 知识推理的应用场景 ===")
print("1. 智能问答系统: 基于知识推理回答复杂问题")
print("2. 推荐系统: 基于知识推理进行个性化推荐")
print("3. 医疗诊断: 基于医学知识图谱进行辅助诊断")
print("4. 金融风控: 基于知识推理识别风险关联")
print("5. 法律辅助: 基于法律知识图谱进行案例分析")
print("6. 教育辅助: 基于知识图谱进行个性化学习路径推荐")
print("7. 科研辅助: 基于知识推理发现研究热点和趋势")

print("\n知识推理示例完成！")
