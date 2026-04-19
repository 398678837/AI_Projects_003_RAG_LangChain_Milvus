import os
import sys
import json
import time
from datetime import datetime

class AuditReportDemo:
    def __init__(self):
        # 审计报告结构
        self.report_structure = {
            "报告信息": "包含报告的基本信息，如标题、日期、作者等",
            "审计范围": "包含审计的范围和目标",
            "审计方法": "包含审计使用的方法和工具",
            "审计发现": "包含审计过程中发现的问题",
            "风险评估": "包含对发现问题的风险评估",
            "修复建议": "包含对发现问题的修复建议",
            "结论": "包含审计的结论和建议"
        }
        
        # 审计发现分类
        self.finding_categories = {
            "安全漏洞": "代码中存在的安全漏洞，如SQL注入、XSS等",
            "代码质量": "代码的质量问题，如重复代码、复杂度过高等",
            "性能问题": "代码的性能问题，如响应时间长、内存泄漏等",
            "合规问题": "代码不符合合规要求的问题"
        }
        
        # 风险等级
        self.risk_levels = {
            "高": "严重的安全漏洞，可能导致系统被控制或数据泄露",
            "中": "中等的安全漏洞，可能导致部分功能异常或数据泄露",
            "低": "轻微的安全漏洞，对系统影响较小"
        }
        
        # 示例审计发现
        self.sample_findings = [
            {
                "id": "F001",
                "标题": "SQL注入漏洞",
                "描述": "登录功能中使用了拼接SQL语句的方式，可能导致SQL注入攻击",
                "位置": "login.py:10",
                "分类": "安全漏洞",
                "风险等级": "高",
                "影响": "攻击者可能通过SQL注入攻击获取敏感数据或控制数据库",
                "修复建议": "使用参数化查询或预编译语句，避免拼接SQL语句"
            },
            {
                "id": "F002",
                "标题": "XSS漏洞",
                "描述": "用户输入未经过滤直接输出到网页，可能导致XSS攻击",
                "位置": "profile.py:25",
                "分类": "安全漏洞",
                "风险等级": "中",
                "影响": "攻击者可能通过XSS攻击窃取用户的会话cookie或执行恶意脚本",
                "修复建议": "对用户输入进行过滤和转义，使用Content-Security-Policy"
            },
            {
                "id": "F003",
                "标题": "CSRF漏洞",
                "描述": "表单提交未使用CSRF token，可能导致CSRF攻击",
                "位置": "transfer.py:15",
                "分类": "安全漏洞",
                "风险等级": "中",
                "影响": "攻击者可能通过CSRF攻击诱导用户执行未授权的操作",
                "修复建议": "为表单添加CSRF token，验证请求的合法性"
            },
            {
                "id": "F004",
                "标题": "重复代码",
                "描述": "多个函数中存在重复的代码，影响代码的可维护性",
                "位置": "utils.py:10-20, utils.py:30-40",
                "分类": "代码质量",
                "风险等级": "低",
                "影响": "增加代码的维护成本，可能导致不一致的行为",
                "修复建议": "提取重复代码为公共函数，提高代码的复用性"
            },
            {
                "id": "F005",
                "标题": "性能问题",
                "描述": "循环中执行数据库查询，可能导致性能问题",
                "位置": "data.py:50-60",
                "分类": "性能问题",
                "风险等级": "中",
                "影响": "当数据量较大时，可能导致响应时间过长",
                "修复建议": "使用批量查询或缓存，减少数据库查询次数"
            }
        ]
        
        # 审计报告日志
        self.report_logs = []
    
    def show_report_structure(self):
        """显示审计报告结构"""
        print("\n--- 审计报告结构 ---")
        for section, description in self.report_structure.items():
            print(f"- {section}: {description}")
        
        self.log_report_event("审计报告结构", "查看", "查看了审计报告结构")
    
    def show_finding_categories(self):
        """显示审计发现分类"""
        print("\n--- 审计发现分类 ---")
        for category, description in self.finding_categories.items():
            print(f"- {category}: {description}")
        
        self.log_report_event("审计发现分类", "查看", "查看了审计发现分类")
    
    def show_risk_levels(self):
        """显示风险等级"""
        print("\n--- 风险等级 ---")
        for level, description in self.risk_levels.items():
            print(f"- {level}: {description}")
        
        self.log_report_event("风险等级", "查看", "查看了风险等级")
    
    def show_sample_findings(self):
        """显示示例审计发现"""
        print("\n--- 示例审计发现 ---")
        for finding in self.sample_findings:
            print(f"\nID: {finding['id']}")
            print(f"标题: {finding['标题']}")
            print(f"描述: {finding['描述']}")
            print(f"位置: {finding['位置']}")
            print(f"分类: {finding['分类']}")
            print(f"风险等级: {finding['风险等级']}")
            print(f"影响: {finding['影响']}")
            print(f"修复建议: {finding['修复建议']}")
        
        self.log_report_event("示例审计发现", "查看", "查看了示例审计发现")
    
    def generate_audit_report(self):
        """生成审计报告"""
        print("\n--- 生成审计报告 ---")
        
        # 计算审计发现统计
        total_findings = len(self.sample_findings)
        findings_by_category = {}
        findings_by_risk = {}
        
        for finding in self.sample_findings:
            category = finding["分类"]
            risk = finding["风险等级"]
            
            if category not in findings_by_category:
                findings_by_category[category] = 0
            findings_by_category[category] += 1
            
            if risk not in findings_by_risk:
                findings_by_risk[risk] = 0
            findings_by_risk[risk] += 1
        
        report = {
            "报告信息": {
                "标题": "代码审计报告",
                "日期": datetime.now().strftime('%Y-%m-%d'),
                "作者": "AuditReportDemo",
                "版本": "1.0"
            },
            "审计范围": {
                "目标": "对登录、用户管理、数据处理等功能进行安全审计",
                "代码范围": "login.py, profile.py, transfer.py, utils.py, data.py",
                "审计时间": f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            },
            "审计方法": {
                "静态分析": "使用SonarQube进行静态代码分析",
                "动态分析": "使用OWASP ZAP进行动态代码分析",
                "手动审查": "对关键代码进行手动审查"
            },
            "审计发现": self.sample_findings,
            "风险评估": {
                "总体风险": "中等",
                "高风险项": findings_by_risk.get("高", 0),
                "中风险项": findings_by_risk.get("中", 0),
                "低风险项": findings_by_risk.get("低", 0)
            },
            "修复建议": [
                "优先修复高风险的安全漏洞，如SQL注入、XSS等",
                "改进代码质量问题，如重复代码、复杂度过高等",
                "优化性能问题，如数据库查询优化、缓存使用等",
                "建立代码审查机制，确保代码的质量和安全性",
                "定期进行安全审计，发现和修复安全问题"
            ],
            "结论": {
                "总体评估": "代码整体质量较好，但存在一些安全漏洞和质量问题",
                "建议": "建议按照修复建议进行修复，提高代码的安全性和可靠性",
                "后续行动": "定期进行安全审计，建立持续的安全改进机制"
            },
            "统计信息": {
                "总发现数": total_findings,
                "按分类统计": findings_by_category,
                "按风险等级统计": findings_by_risk
            }
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        self.log_report_event("审计报告", "生成", "生成了审计报告")
        return report
    
    def log_report_event(self, activity, action, message):
        """记录报告事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "action": action,
            "message": message
        }
        self.report_logs.append(log_entry)
    
    def show_report_logs(self):
        """显示报告日志"""
        print("\n--- 报告日志 ---")
        for log in self.report_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['action']}: {log['message']}")
    
    def demonstrate_audit_report(self):
        """演示审计报告"""
        print("=== 审计报告演示 ===")
        print("==================")
        
        # 1. 显示审计报告结构
        print("\n1. 审计报告结构:")
        self.show_report_structure()
        
        # 2. 显示审计发现分类
        print("\n2. 审计发现分类:")
        self.show_finding_categories()
        
        # 3. 显示风险等级
        print("\n3. 风险等级:")
        self.show_risk_levels()
        
        # 4. 显示示例审计发现
        print("\n4. 示例审计发现:")
        self.show_sample_findings()
        
        # 5. 生成审计报告
        print("\n5. 生成审计报告:")
        self.generate_audit_report()
        
        # 6. 显示报告日志
        print("\n6. 报告日志:")
        self.show_report_logs()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了审计报告的结构、内容和编写方法。")
        print("审计报告是代码审计的重要输出，用于记录和传达审计结果。")

if __name__ == "__main__":
    audit_report_demo = AuditReportDemo()
    audit_report_demo.demonstrate_audit_report()