import os
import sys
import json
import time
from datetime import datetime

class ThreatModelingDemo:
    def __init__(self):
        # 威胁建模方法
        self.threat_modeling_methods = {
            "STRIDE": "微软提出的威胁建模方法",
            "DREAD": "威胁评估方法",
            "CVSS": "通用漏洞评分系统",
            "PASTA": "基于过程的威胁建模方法",
            "VAST": "可视化、自动化、简单的威胁建模方法"
        }
        
        # 威胁类型
        self.threat_types = {
            "Spoofing": "伪装攻击",
            "Tampering": "篡改攻击",
            "Repudiation": "否认攻击",
            "Information Disclosure": "信息泄露",
            "Denial of Service": "拒绝服务",
            "Elevation of Privilege": "权限提升"
        }
        
        # 资产
        self.assets = [
            {"id": "A1", "name": "用户数据", "value": "高", "description": "用户的个人信息和敏感数据"},
            {"id": "A2", "name": "系统配置", "value": "中", "description": "系统的配置信息"},
            {"id": "A3", "name": "网络连接", "value": "中", "description": "系统的网络连接"},
            {"id": "A4", "name": "应用程序代码", "value": "高", "description": "应用程序的源代码"}
        ]
        
        # 威胁
        self.threats = []
        
        # 威胁建模日志
        self.threat_modeling_logs = []
    
    def identify_assets(self):
        """识别资产"""
        print("\n--- 识别资产 ---")
        for asset in self.assets:
            print(f"- 资产ID: {asset['id']}")
            print(f"  名称: {asset['name']}")
            print(f"  价值: {asset['value']}")
            print(f"  描述: {asset['description']}")
        
        self.log_threat_modeling_event("资产识别", "完成", f"识别了 {len(self.assets)} 个资产")
    
    def identify_threats(self):
        """识别威胁"""
        print("\n--- 识别威胁 ---")
        
        # 基于STRIDE方法识别威胁
        stride_threats = [
            {
                "id": "T1",
                "type": "Spoofing",
                "asset": "A1",
                "description": "攻击者伪装成合法用户",
                "severity": "高",
                "likelihood": "中"
            },
            {
                "id": "T2",
                "type": "Tampering",
                "asset": "A1",
                "description": "攻击者篡改用户数据",
                "severity": "高",
                "likelihood": "中"
            },
            {
                "id": "T3",
                "type": "Information Disclosure",
                "asset": "A1",
                "description": "攻击者获取用户敏感数据",
                "severity": "高",
                "likelihood": "高"
            },
            {
                "id": "T4",
                "type": "Denial of Service",
                "asset": "A3",
                "description": "攻击者使网络连接不可用",
                "severity": "中",
                "likelihood": "中"
            },
            {
                "id": "T5",
                "type": "Elevation of Privilege",
                "asset": "A4",
                "description": "攻击者获取应用程序的高级权限",
                "severity": "高",
                "likelihood": "低"
            }
        ]
        
        self.threats.extend(stride_threats)
        
        for threat in stride_threats:
            print(f"- 威胁ID: {threat['id']}")
            print(f"  类型: {threat['type']}")
            print(f"  资产: {threat['asset']}")
            print(f"  描述: {threat['description']}")
            print(f"  严重程度: {threat['severity']}")
            print(f"  可能性: {threat['likelihood']}")
        
        self.log_threat_modeling_event("威胁识别", "完成", f"识别了 {len(stride_threats)} 个威胁")
    
    def assess_threats(self):
        """评估威胁"""
        print("\n--- 评估威胁 ---")
        
        for threat in self.threats:
            # 计算风险分数（基于严重程度和可能性）
            severity_score = {
                "高": 3,
                "中": 2,
                "低": 1
            }[threat['severity']]
            
            likelihood_score = {
                "高": 3,
                "中": 2,
                "低": 1
            }[threat['likelihood']]
            
            risk_score = severity_score * likelihood_score
            threat['risk_score'] = risk_score
            
            # 确定风险等级
            if risk_score >= 7:
                threat['risk_level'] = "高"
            elif risk_score >= 4:
                threat['risk_level'] = "中"
            else:
                threat['risk_level'] = "低"
            
            print(f"- 威胁ID: {threat['id']}")
            print(f"  类型: {threat['type']}")
            print(f"  严重程度: {threat['severity']}")
            print(f"  可能性: {threat['likelihood']}")
            print(f"  风险分数: {threat['risk_score']}")
            print(f"  风险等级: {threat['risk_level']}")
        
        self.log_threat_modeling_event("威胁评估", "完成", f"评估了 {len(self.threats)} 个威胁")
    
    def mitigate_threats(self):
        """缓解威胁"""
        print("\n--- 缓解威胁 ---")
        
        # 为每个威胁制定缓解措施
        mitigation_measures = {
            "T1": ["实施强密码策略", "使用双因素认证", "监控异常登录行为"],
            "T2": ["使用加密保护数据", "实施访问控制", "监控数据修改行为"],
            "T3": ["使用加密传输", "实施数据访问控制", "定期审计数据访问"],
            "T4": ["使用DDoS防护", "实施速率限制", "使用负载均衡"],
            "T5": ["实施最小权限原则", "定期权限审查", "监控权限变更"]
        }
        
        for threat in self.threats:
            measures = mitigation_measures.get(threat['id'], ["无特定缓解措施"])
            threat['mitigation_measures'] = measures
            
            print(f"- 威胁ID: {threat['id']}")
            print(f"  类型: {threat['type']}")
            print(f"  缓解措施:")
            for measure in measures:
                print(f"    - {measure}")
        
        self.log_threat_modeling_event("威胁缓解", "完成", f"为 {len(self.threats)} 个威胁制定了缓解措施")
    
    def log_threat_modeling_event(self, activity, status, message):
        """记录威胁建模事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "status": status,
            "message": message
        }
        self.threat_modeling_logs.append(log_entry)
    
    def show_threat_modeling_methods(self):
        """显示威胁建模方法"""
        print("\n--- 威胁建模方法 ---")
        for method, description in self.threat_modeling_methods.items():
            print(f"- {method}: {description}")
    
    def show_threat_types(self):
        """显示威胁类型"""
        print("\n--- 威胁类型 ---")
        for threat_type, description in self.threat_types.items():
            print(f"- {threat_type}: {description}")
    
    def show_threat_modeling_logs(self):
        """显示威胁建模日志"""
        print("\n--- 威胁建模日志 ---")
        for log in self.threat_modeling_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['status']}: {log['message']}")
    
    def generate_threat_modeling_report(self):
        """生成威胁建模报告"""
        print("\n--- 生成威胁建模报告 ---")
        
        # 统计威胁
        total_threats = len(self.threats)
        high_risk_threats = sum(1 for threat in self.threats if threat.get('risk_level') == "高")
        medium_risk_threats = sum(1 for threat in self.threats if threat.get('risk_level') == "中")
        low_risk_threats = sum(1 for threat in self.threats if threat.get('risk_level') == "低")
        
        # 统计资产
        total_assets = len(self.assets)
        high_value_assets = sum(1 for asset in self.assets if asset['value'] == "高")
        medium_value_assets = sum(1 for asset in self.assets if asset['value'] == "中")
        low_value_assets = sum(1 for asset in self.assets if asset['value'] == "低")
        
        report = {
            "report_info": {
                "title": "威胁建模报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "ThreatModelingDemo"
            },
            "threat_summary": {
                "total_threats": total_threats,
                "high_risk_threats": high_risk_threats,
                "medium_risk_threats": medium_risk_threats,
                "low_risk_threats": low_risk_threats
            },
            "asset_summary": {
                "total_assets": total_assets,
                "high_value_assets": high_value_assets,
                "medium_value_assets": medium_value_assets,
                "low_value_assets": low_value_assets
            },
            "threats": self.threats,
            "assets": self.assets,
            "recommendations": [
                "优先缓解高风险威胁",
                "定期更新威胁模型",
                "实施安全监控",
                "进行安全培训",
                "定期进行安全评估"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_threat_modeling(self):
        """演示威胁建模"""
        print("=== 威胁建模演示 ===")
        print("====================")
        
        # 1. 显示威胁建模方法
        print("\n1. 威胁建模方法:")
        self.show_threat_modeling_methods()
        
        # 2. 显示威胁类型
        print("\n2. 威胁类型:")
        self.show_threat_types()
        
        # 3. 识别资产
        print("\n3. 识别资产:")
        self.identify_assets()
        
        # 4. 识别威胁
        print("\n4. 识别威胁:")
        self.identify_threats()
        
        # 5. 评估威胁
        print("\n5. 评估威胁:")
        self.assess_threats()
        
        # 6. 缓解威胁
        print("\n6. 缓解威胁:")
        self.mitigate_threats()
        
        # 7. 显示威胁建模日志
        print("\n7. 威胁建模日志:")
        self.show_threat_modeling_logs()
        
        # 8. 生成威胁建模报告
        print("\n8. 生成威胁建模报告:")
        self.generate_threat_modeling_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了威胁建模的基本概念和实施方法。")
        print("威胁建模是安全框架的重要组成部分，用于识别和缓解安全威胁。")

if __name__ == "__main__":
    threat_modeling_demo = ThreatModelingDemo()
    threat_modeling_demo.demonstrate_threat_modeling()