#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱实战应用
展示知识图谱在实际应用中的使用
"""

import networkx as nx
import matplotlib.pyplot as plt
import json
import csv

# 1. 智能问答系统
print("=== 智能问答系统 ===")

# 构建问答知识图谱
qa_graph = nx.DiGraph()

# 添加节点
qa_graph.add_node("人工智能", type="领域")
qa_graph.add_node("机器学习", type="学科")
qa_graph.add_node("深度学习", type="学科")
qa_graph.add_node("神经网络", type="概念")
qa_graph.add_node("卷积神经网络", type="概念")
qa_graph.add_node("循环神经网络", type="概念")
qa_graph.add_node("自然语言处理", type="应用")
qa_graph.add_node("计算机视觉", type="应用")
qa_graph.add_node("语音识别", type="应用")

# 添加边
qa_graph.add_edge("人工智能", "机器学习", relation="包含")
qa_graph.add_edge("人工智能", "深度学习", relation="包含")
qa_graph.add_edge("机器学习", "深度学习", relation="包含")
qa_graph.add_edge("深度学习", "神经网络", relation="基于")
qa_graph.add_edge("神经网络", "卷积神经网络", relation="类型")
qa_graph.add_edge("神经网络", "循环神经网络", relation="类型")
qa_graph.add_edge("深度学习", "自然语言处理", relation="应用于")
qa_graph.add_edge("深度学习", "计算机视觉", relation="应用于")
qa_graph.add_edge("深度学习", "语音识别", relation="应用于")

# 可视化问答知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(qa_graph, seed=42)
nx.draw_networkx_nodes(qa_graph, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(qa_graph, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(qa_graph, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in qa_graph.edges(data=True)}
nx.draw_networkx_edge_labels(qa_graph, pos, edge_labels=edge_labels, font_size=10)
plt.title("人工智能知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("qa_knowledge_graph.png")
print("智能问答知识图谱已保存为 qa_knowledge_graph.png")

# 实现简单的问答系统
def answer_question(graph, question):
    """基于知识图谱回答问题"""
    question = question.lower()
    
    # 简单的规则匹配
    if "什么是" in question:
        # 提取实体
        entity = question.replace("什么是", "").strip()
        if entity in graph:
            # 查找实体的类型
            entity_type = graph.nodes[entity].get("type", "实体")
            # 查找与实体相关的关系
            relations = []
            for u, v, d in graph.edges(data=True):
                if u == entity:
                    relations.append(f"{u} {d['relation']} {v}")
            for u, v, d in graph.in_edges(entity, data=True):
                relations.append(f"{u} {d['relation']} {v}")
            
            if relations:
                answer = f"{entity}是一种{entity_type}。"
                answer += "相关信息：" + "；".join(relations)
                return answer
            else:
                return f"{entity}是一种{entity_type}。"
        else:
            return "抱歉，我无法回答这个问题。"
    
    elif "包括" in question or "包含" in question:
        # 提取实体
        entity = question.split("包括")[0].strip() if "包括" in question else question.split("包含")[0].strip()
        if entity in graph:
            # 查找实体包含的内容
            includes = []
            for u, v, d in graph.edges(data=True):
                if u == entity and d['relation'] == "包含":
                    includes.append(v)
            if includes:
                return f"{entity}包括：{', '.join(includes)}。"
            else:
                return f"抱歉，我无法回答这个问题。"
    
    elif "应用" in question:
        # 提取实体
        entity = question.split("应用")[0].strip()
        if entity in graph:
            # 查找实体的应用
            applications = []
            for u, v, d in graph.edges(data=True):
                if u == entity and d['relation'] == "应用于":
                    applications.append(v)
            if applications:
                return f"{entity}应用于：{', '.join(applications)}。"
            else:
                return f"抱歉，我无法回答这个问题。"
    
    else:
        return "抱歉，我无法回答这个问题。"

# 测试问答系统
questions = [
    "什么是人工智能？",
    "机器学习包括什么？",
    "深度学习应用于什么？",
    "什么是神经网络？"
]

print("\n智能问答系统测试:")
for question in questions:
    answer = answer_question(qa_graph, question)
    print(f"Q: {question}")
    print(f"A: {answer}")
    print()

# 2. 推荐系统
print("=== 推荐系统 ===")

# 构建用户-物品知识图谱
recommendation_graph = nx.Graph()

# 添加用户节点
users = ["用户A", "用户B", "用户C", "用户D", "用户E"]
for user in users:
    recommendation_graph.add_node(user, type="用户")

# 添加物品节点
items = ["电影1", "电影2", "电影3", "电影4", "电影5", "书籍1", "书籍2", "书籍3"]
for item in items:
    recommendation_graph.add_node(item, type="物品")

# 添加类别节点
categories = ["动作片", "科幻片", "喜剧片", "悬疑片", "小说", "科普"]
for category in categories:
    recommendation_graph.add_node(category, type="类别")

# 添加用户-物品边（表示用户喜欢物品）
user_item_edges = [
    ("用户A", "电影1", 5),
    ("用户A", "电影2", 4),
    ("用户A", "书籍1", 5),
    ("用户B", "电影2", 5),
    ("用户B", "电影3", 4),
    ("用户B", "书籍2", 5),
    ("用户C", "电影3", 5),
    ("用户C", "电影4", 4),
    ("用户C", "书籍3", 5),
    ("用户D", "电影4", 5),
    ("用户D", "电影5", 4),
    ("用户E", "电影5", 5),
    ("用户E", "电影1", 4),
    ("用户E", "书籍1", 4)
]

for u, v, weight in user_item_edges:
    recommendation_graph.add_edge(u, v, relation="喜欢", weight=weight)

# 添加物品-类别边
item_category_edges = [
    ("电影1", "动作片"),
    ("电影2", "科幻片"),
    ("电影3", "悬疑片"),
    ("电影4", "科幻片"),
    ("电影5", "动作片"),
    ("书籍1", "小说"),
    ("书籍2", "科普"),
    ("书籍3", "小说")
]

for u, v in item_category_edges:
    recommendation_graph.add_edge(u, v, relation="属于")

# 可视化推荐系统知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(recommendation_graph, seed=42)

# 为不同类型的节点设置不同的颜色
node_colors = []
for node, data in recommendation_graph.nodes(data=True):
    if data.get("type") == "用户":
        node_colors.append("lightblue")
    elif data.get("type") == "物品":
        node_colors.append("lightgreen")
    elif data.get("type") == "类别":
        node_colors.append("lightcoral")
    else:
        node_colors.append("lightgray")

nx.draw_networkx_nodes(recommendation_graph, pos, node_size=1000, node_color=node_colors)
nx.draw_networkx_edges(recommendation_graph, pos, width=2, edge_color="gray")
nx.draw_networkx_labels(recommendation_graph, pos, font_size=10, font_weight="bold")
edge_labels = {(u, v): d.get("relation", "") for u, v, d in recommendation_graph.edges(data=True)}
nx.draw_networkx_edge_labels(recommendation_graph, pos, edge_labels=edge_labels, font_size=8)
plt.title("推荐系统知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("recommendation_graph.png")
print("推荐系统知识图谱已保存为 recommendation_graph.png")

# 实现基于知识图谱的推荐算法
def recommend_items(graph, user, top_k=3):
    """基于知识图谱推荐物品"""
    if user not in graph:
        return []
    
    # 获取用户喜欢的物品
    liked_items = []
    for u, v, d in graph.edges(user, data=True):
        if d.get("relation") == "喜欢":
            liked_items.append((v, d.get("weight", 0)))
    
    # 获取用户喜欢的物品的类别
    liked_categories = set()
    for item, _ in liked_items:
        for u, v, d in graph.edges(item, data=True):
            if d.get("relation") == "属于":
                liked_categories.add(v)
    
    # 查找属于这些类别的其他物品
    candidate_items = set()
    for category in liked_categories:
        for u, v, d in graph.edges(category, data=True):
            if d.get("relation") == "属于":
                candidate_items.add(v)
    
    # 过滤掉用户已经喜欢的物品
    candidate_items = [item for item in candidate_items if item not in [x[0] for x in liked_items]]
    
    # 计算物品的相似度（基于共同类别）
    item_scores = []
    for item in candidate_items:
        # 获取物品的类别
        item_categories = set()
        for u, v, d in graph.edges(item, data=True):
            if d.get("relation") == "属于":
                item_categories.add(v)
        # 计算与用户喜欢类别的交集大小
        score = len(item_categories.intersection(liked_categories))
        item_scores.append((item, score))
    
    # 按分数排序并返回前k个
    item_scores.sort(key=lambda x: x[1], reverse=True)
    return [item for item, _ in item_scores[:top_k]]

# 测试推荐系统
print("\n推荐系统测试:")
for user in users:
    recommendations = recommend_items(recommendation_graph, user)
    print(f"为{user}推荐的物品: {', '.join(recommendations)}")

# 3. 金融风控
print("\n=== 金融风控 ===")

# 构建金融风控知识图谱
risk_graph = nx.DiGraph()

# 添加节点
risk_graph.add_node("客户A", type="客户", age=35, income=10000)
risk_graph.add_node("客户B", type="客户", age=28, income=8000)
risk_graph.add_node("客户C", type="客户", age=45, income=15000)
risk_graph.add_node("客户D", type="客户", age=30, income=7000)
risk_graph.add_node("贷款1", type="贷款", amount=50000, duration=24)
risk_graph.add_node("贷款2", type="贷款", amount=30000, duration=12)
risk_graph.add_node("贷款3", type="贷款", amount=80000, duration=36)
risk_graph.add_node("贷款4", type="贷款", amount=20000, duration=6)
risk_graph.add_node("逾期1", type="逾期", days=30)
risk_graph.add_node("逾期2", type="逾期", days=60)
risk_graph.add_node("逾期3", type="逾期", days=90)
risk_graph.add_node("黑名单", type="风险", level="高")
risk_graph.add_node("灰名单", type="风险", level="中")

# 添加边
risk_graph.add_edge("客户A", "贷款1", relation="申请")
risk_graph.add_edge("客户B", "贷款2", relation="申请")
risk_graph.add_edge("客户C", "贷款3", relation="申请")
risk_graph.add_edge("客户D", "贷款4", relation="申请")
risk_graph.add_edge("贷款1", "逾期1", relation="产生")
risk_graph.add_edge("贷款2", "逾期2", relation="产生")
risk_graph.add_edge("贷款4", "逾期3", relation="产生")
risk_graph.add_edge("逾期2", "灰名单", relation="进入")
risk_graph.add_edge("逾期3", "黑名单", relation="进入")
risk_graph.add_edge("客户B", "灰名单", relation="属于")
risk_graph.add_edge("客户D", "黑名单", relation="属于")

# 可视化金融风控知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(risk_graph, seed=42)

# 为不同类型的节点设置不同的颜色
node_colors = []
for node, data in risk_graph.nodes(data=True):
    if data.get("type") == "客户":
        node_colors.append("lightblue")
    elif data.get("type") == "贷款":
        node_colors.append("lightgreen")
    elif data.get("type") == "逾期":
        node_colors.append("lightyellow")
    elif data.get("type") == "风险":
        node_colors.append("lightcoral")
    else:
        node_colors.append("lightgray")

nx.draw_networkx_nodes(risk_graph, pos, node_size=1000, node_color=node_colors)
nx.draw_networkx_edges(risk_graph, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(risk_graph, pos, font_size=10, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in risk_graph.edges(data=True)}
nx.draw_networkx_edge_labels(risk_graph, pos, edge_labels=edge_labels, font_size=8)
plt.title("金融风控知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("risk_graph.png")
print("金融风控知识图谱已保存为 risk_graph.png")

# 实现风险评估函数
def assess_risk(graph, customer):
    """基于知识图谱评估客户风险"""
    if customer not in graph:
        return "客户不存在"
    
    risk_score = 0
    risk_factors = []
    
    # 检查客户是否在黑名单或灰名单中
    for u, v, d in graph.edges(customer, data=True):
        if v == "黑名单":
            risk_score += 100
            risk_factors.append("客户在黑名单中")
        elif v == "灰名单":
            risk_score += 50
            risk_factors.append("客户在灰名单中")
    
    # 检查客户的贷款逾期情况
    for u, v, d in graph.edges(customer, data=True):
        if d.get("relation") == "申请":
            loan = v
            for u2, v2, d2 in graph.edges(loan, data=True):
                if d2.get("relation") == "产生":
                    overdue = v2
                    overdue_days = graph.nodes[overdue].get("days", 0)
                    if overdue_days > 60:
                        risk_score += 80
                        risk_factors.append(f"贷款{loan}逾期{overdue_days}天")
                    elif overdue_days > 30:
                        risk_score += 40
                        risk_factors.append(f"贷款{loan}逾期{overdue_days}天")
                    else:
                        risk_score += 20
                        risk_factors.append(f"贷款{loan}逾期{overdue_days}天")
    
    # 基于风险分数评估风险等级
    if risk_score >= 100:
        risk_level = "高风险"
    elif risk_score >= 50:
        risk_level = "中风险"
    else:
        risk_level = "低风险"
    
    return {
        "客户": customer,
        "风险分数": risk_score,
        "风险等级": risk_level,
        "风险因素": risk_factors
    }

# 测试风险评估
print("\n金融风控测试:")
for customer in ["客户A", "客户B", "客户C", "客户D"]:
    risk_assessment = assess_risk(risk_graph, customer)
    print(f"客户: {risk_assessment['客户']}")
    print(f"风险分数: {risk_assessment['风险分数']}")
    print(f"风险等级: {risk_assessment['风险等级']}")
    print(f"风险因素: {', '.join(risk_assessment['风险因素'])}")
    print()

# 4. 医疗健康
print("=== 医疗健康 ===")

# 构建医疗健康知识图谱
medical_graph = nx.DiGraph()

# 添加节点
medical_graph.add_node("感冒", type="疾病", severity="轻")
medical_graph.add_node("肺炎", type="疾病", severity="重")
medical_graph.add_node("糖尿病", type="疾病", severity="中")
medical_graph.add_node("高血压", type="疾病", severity="中")
medical_graph.add_node("发烧", type="症状")
medical_graph.add_node("咳嗽", type="症状")
medical_graph.add_node("头痛", type="症状")
medical_graph.add_node("口渴", type="症状")
medical_graph.add_node("疲劳", type="症状")
medical_graph.add_node("阿司匹林", type="药物")
medical_graph.add_node("抗生素", type="药物")
medical_graph.add_node("胰岛素", type="药物")
medical_graph.add_node("降压药", type="药物")
medical_graph.add_node("休息", type="治疗")
medical_graph.add_node("多喝水", type="治疗")

# 添加边
medical_graph.add_edge("感冒", "发烧", relation="引起")
medical_graph.add_edge("感冒", "咳嗽", relation="引起")
medical_graph.add_edge("感冒", "头痛", relation="引起")
medical_graph.add_edge("肺炎", "发烧", relation="引起")
medical_graph.add_edge("肺炎", "咳嗽", relation="引起")
medical_graph.add_edge("肺炎", "疲劳", relation="引起")
medical_graph.add_edge("糖尿病", "口渴", relation="引起")
medical_graph.add_edge("糖尿病", "疲劳", relation="引起")
medical_graph.add_edge("高血压", "头痛", relation="引起")
medical_graph.add_edge("感冒", "阿司匹林", relation="治疗药物")
medical_graph.add_edge("感冒", "休息", relation="治疗方法")
medical_graph.add_edge("感冒", "多喝水", relation="治疗方法")
medical_graph.add_edge("肺炎", "抗生素", relation="治疗药物")
medical_graph.add_edge("糖尿病", "胰岛素", relation="治疗药物")
medical_graph.add_edge("高血压", "降压药", relation="治疗药物")

# 可视化医疗健康知识图谱
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(medical_graph, seed=42)

# 为不同类型的节点设置不同的颜色
node_colors = []
for node, data in medical_graph.nodes(data=True):
    if data.get("type") == "疾病":
        node_colors.append("lightblue")
    elif data.get("type") == "症状":
        node_colors.append("lightgreen")
    elif data.get("type") == "药物":
        node_colors.append("lightcoral")
    elif data.get("type") == "治疗":
        node_colors.append("lightyellow")
    else:
        node_colors.append("lightgray")

nx.draw_networkx_nodes(medical_graph, pos, node_size=1000, node_color=node_colors)
nx.draw_networkx_edges(medical_graph, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(medical_graph, pos, font_size=10, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in medical_graph.edges(data=True)}
nx.draw_networkx_edge_labels(medical_graph, pos, edge_labels=edge_labels, font_size=8)
plt.title("医疗健康知识图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("medical_graph.png")
print("医疗健康知识图谱已保存为 medical_graph.png")

# 实现基于症状的疾病诊断
def diagnose_disease(graph, symptoms):
    """基于症状诊断疾病"""
    disease_scores = {}
    
    # 遍历所有疾病
    for node, data in graph.nodes(data=True):
        if data.get("type") == "疾病":
            # 计算疾病与症状的匹配度
            score = 0
            for symptom in symptoms:
                if graph.has_edge(node, symptom):
                    score += 1
            if score > 0:
                disease_scores[node] = score
    
    # 按匹配度排序
    sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)
    
    # 获取诊断结果
    if sorted_diseases:
        top_disease = sorted_diseases[0][0]
        # 获取治疗方法
        treatments = []
        for u, v, d in graph.edges(top_disease, data=True):
            if d.get("relation") == "治疗药物" or d.get("relation") == "治疗方法":
                treatments.append(v)
        
        return {
            "诊断结果": top_disease,
            "匹配症状数": sorted_diseases[0][1],
            "治疗方法": treatments
        }
    else:
        return {"诊断结果": "无法诊断", "匹配症状数": 0, "治疗方法": []}

# 测试疾病诊断
print("\n医疗健康测试:")
symptom_sets = [
    ["发烧", "咳嗽", "头痛"],
    ["发烧", "咳嗽", "疲劳"],
    ["口渴", "疲劳"],
    ["头痛"]
]

for symptoms in symptom_sets:
    diagnosis = diagnose_disease(medical_graph, symptoms)
    print(f"症状: {', '.join(symptoms)}")
    print(f"诊断结果: {diagnosis['诊断结果']}")
    print(f"匹配症状数: {diagnosis['匹配症状数']}")
    print(f"治疗方法: {', '.join(diagnosis['治疗方法'])}")
    print()

# 5. 知识图谱的实际应用总结
print("\n=== 知识图谱的实际应用总结 ===")
print("知识图谱在以下领域有广泛应用:")
print("1. 智能问答系统: 基于知识图谱的问答可以提供更准确的答案")
print("2. 推荐系统: 利用实体之间的关系进行更精准的推荐")
print("3. 金融风控: 识别欺诈行为和风险关联")
print("4. 医疗健康: 整合医疗知识，辅助诊断和治疗")
print("5. 信息检索: 提高搜索结果的相关性和准确性")
print("6. 供应链管理: 优化供应链流程，识别风险")
print("7. 语义理解: 增强自然语言处理能力")
print("8. 教育辅助: 构建知识体系，辅助学习")
print("9. 科研辅助: 发现研究热点和趋势")
print("10. 决策支持: 基于知识图谱的分析辅助决策")

print("\n知识图谱实战应用示例完成！")
