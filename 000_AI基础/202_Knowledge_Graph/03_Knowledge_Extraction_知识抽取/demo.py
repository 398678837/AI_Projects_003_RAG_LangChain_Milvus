#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识抽取
展示知识抽取的基本方法
"""

import re
import spacy
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt

# 1. 基础知识抽取
print("=== 基础知识抽取 ===")

# 示例文本
text = """
苹果公司是一家美国跨国科技公司，总部位于加利福尼亚州库比蒂诺。
史蒂夫·乔布斯是苹果公司的联合创始人之一。
苹果公司主要生产iPhone、iPad和Mac等产品。
2023年，苹果公司的市值超过3万亿美元。
"""

print("原始文本:")
print(text)

# 2. 基于规则的知识抽取
print("\n=== 基于规则的知识抽取 ===")

# 定义规则
entity_patterns = [
    (r"[\u4e00-\u9fa5]+公司", "组织"),
    (r"[\u4e00-\u9fa5]+州", "地点"),
    (r"[\u4e00-\u9fa5]+市", "地点"),
    (r"[\u4e00-\u9fa5]{2,4}", "人物"),
    (r"iPhone|iPad|Mac", "产品"),
    (r"\d+年", "时间"),
    (r"\d+万亿[美元]", "数值")
]

# 提取实体
extracted_entities = []
for pattern, label in entity_patterns:
    matches = re.finditer(pattern, text)
    for match in matches:
        entity = match.group(0)
        extracted_entities.append((entity, label))

print("基于规则抽取的实体:")
for entity, label in extracted_entities:
    print(f"{entity}: {label}")

# 3. 使用NLP工具进行知识抽取
print("\n=== 使用NLP工具进行知识抽取 ===")

try:
    # 加载中文NLP模型
    nlp = spacy.load("zh_core_web_sm")
    print("成功加载中文NLP模型")
    
    # 处理文本
    doc = nlp(text)
    
    # 提取实体
    print("使用Spacy抽取的实体:")
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")
    
    # 保存实体可视化
    html = displacy.render(doc, style="ent")
    with open("entity_visualization.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("实体可视化已保存为 entity_visualization.html")
    
except Exception as e:
    print(f"加载NLP模型失败: {e}")
    print("使用模拟数据进行演示")
    # 模拟NLP实体抽取结果
    simulated_entities = [
        ("苹果公司", "ORG"),
        ("美国", "GPE"),
        ("加利福尼亚州", "GPE"),
        ("库比蒂诺", "GPE"),
        ("史蒂夫·乔布斯", "PERSON"),
        ("苹果公司", "ORG"),
        ("苹果公司", "ORG"),
        ("iPhone", "PRODUCT"),
        ("iPad", "PRODUCT"),
        ("Mac", "PRODUCT"),
        ("2023年", "DATE"),
        ("苹果公司", "ORG"),
        ("3万亿美元", "MONEY")
    ]
    print("模拟抽取的实体:")
    for entity, label in simulated_entities:
        print(f"{entity}: {label}")

# 4. 关系抽取
print("\n=== 关系抽取 ===")

# 示例文本
relation_text = """
比尔·盖茨是微软公司的创始人。
微软公司开发了Windows操作系统。
比尔·盖茨出生于1955年。
微软公司总部位于华盛顿州。
"""

print("关系抽取文本:")
print(relation_text)

# 基于规则的关系抽取
sentences = relation_text.split('\n')
extracted_relations = []

for sentence in sentences:
    if not sentence.strip():
        continue
    
    # 抽取主谓宾关系
    # 简单规则示例
    patterns = [
        (r"(.*)是(.*)的创始人", "创始人"),
        (r"(.*)开发了(.*)", "开发"),
        (r"(.*)出生于(.*)", "出生于"),
        (r"(.*)总部位于(.*)", "总部位于")
    ]
    
    for pattern, relation in patterns:
        match = re.match(pattern, sentence)
        if match:
            subject = match.group(1).strip()
            object_ = match.group(2).strip()
            extracted_relations.append((subject, relation, object_))

print("基于规则抽取的关系:")
for subject, relation, object_ in extracted_relations:
    print(f"{subject} - {relation} -> {object_}")

# 5. 构建知识图谱
print("\n=== 从抽取的知识构建图谱 ===")

# 创建知识图谱
G = nx.DiGraph()

# 添加节点和边
for subject, relation, object_ in extracted_relations:
    # 添加节点
    if subject not in G:
        G.add_node(subject)
    if object_ not in G:
        G.add_node(object_)
    # 添加边
    G.add_edge(subject, object_, relation=relation)

# 可视化知识图谱
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrows=True, arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
edge_labels = {(u, v): d["relation"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("从抽取的知识构建的图谱")
plt.axis("off")
plt.tight_layout()
plt.savefig("extracted_knowledge_graph.png")
print("从抽取的知识构建的图谱已保存为 extracted_knowledge_graph.png")

# 6. 知识抽取的挑战与解决方案
print("\n=== 知识抽取的挑战与解决方案 ===")
print("知识抽取面临的主要挑战:")
print("1. 实体识别准确性: 实体边界识别困难，尤其是命名实体变体")
print("2. 关系抽取复杂性: 关系类型多样，上下文依赖强")
print("3. 知识图谱质量: 抽取的知识可能存在错误或冗余")
print("4. 大规模知识抽取: 处理海量文本的效率问题")

print("\n解决方案:")
print("1. 结合规则和机器学习方法提高实体识别准确性")
print("2. 使用深度学习模型（如BERT）进行关系抽取")
print("3. 建立知识图谱质量评估机制，定期更新和维护")
print("4. 采用分布式计算和流式处理技术处理大规模文本")

# 7. 知识抽取的应用示例
print("\n=== 知识抽取的应用示例 ===")
print("1. 智能问答系统: 从文本中抽取知识，构建问答知识库")
print("2. 信息检索: 提高搜索结果的相关性和准确性")
print("3. 知识图谱构建: 自动从文本中构建和更新知识图谱")
print("4. 文本摘要: 提取文本中的关键信息，生成摘要")
print("5. 情感分析: 抽取情感实体和情感关系")
print("6. 事件抽取: 从文本中抽取事件信息，如时间、地点、参与者等")

print("\n知识抽取示例完成！")
