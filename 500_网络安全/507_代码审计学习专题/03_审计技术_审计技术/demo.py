import os
import sys
import json
import re
import time
from datetime import datetime

class CodeAuditTechniquesDemo:
    def __init__(self):
        # 代码审计技术分类
        self.technique_categories = {
            "静态审计技术": "不运行代码，通过分析源代码来发现安全漏洞",
            "动态审计技术": "在运行时测试代码，发现运行时的安全漏洞",
            "手动审计技术": "由安全专家手动审查代码，发现安全漏洞",
            "混合审计技术": "结合多种审计技术，提高审计效果"
        }
        
        # 静态审计技术
        self.static_techniques = {
            "词法分析": "分析源代码的词法结构，发现语法错误和潜在问题",
            "语法分析": "分析源代码的语法结构，发现语法错误和潜在问题",
            "语义分析": "分析源代码的语义，发现逻辑错误和潜在问题",
            "数据流分析": "分析数据在代码中的流动，发现数据处理错误和潜在问题",
            "控制流分析": "分析代码的控制流，发现逻辑错误和潜在问题"
        }
        
        # 动态审计技术
        self.dynamic_techniques = {
            "黑盒测试": "不了解代码结构，通过输入输出测试发现安全漏洞",
            "白盒测试": "了解代码结构，通过有针对性的测试发现安全漏洞",
            "灰盒测试": "部分了解代码结构，结合黑盒和白盒测试发现安全漏洞",
            "模糊测试": "使用随机或半随机输入测试代码，发现边界情况的安全漏洞",
            "性能测试": "测试代码的性能，发现性能问题和潜在的安全漏洞"
        }
        
        # 手动审计技术
        self.manual_techniques = {
            "代码审查": "手动审查代码，发现安全漏洞和质量问题",
            "安全设计审查": "审查系统的安全设计，发现设计层面的安全问题",
            "威胁建模": "识别系统的威胁，发现潜在的安全漏洞",
            "代码走查": "团队成员共同审查代码，发现安全漏洞和质量问题"
        }
        
        # 审计技术日志
        self.technique_logs = []
    
    def show_technique_categories(self):
        """显示代码审计技术分类"""
        print("\n--- 代码审计技术分类 ---")
        for category, description in self.technique_categories.items():
            print(f"- {category}: {description}")
        
        self.log_technique_event("技术分类", "查看", "查看了代码审计技术分类")
    
    def show_static_techniques(self):
        """显示静态审计技术"""
        print("\n--- 静态审计技术 ---")
        for technique, description in self.static_techniques.items():
            print(f"- {technique}: {description}")
        
        self.log_technique_event("静态技术", "查看", "查看了静态审计技术")
    
    def show_dynamic_techniques(self):
        """显示动态审计技术"""
        print("\n--- 动态审计技术 ---")
        for technique, description in self.dynamic_techniques.items():
            print(f"- {technique}: {description}")
        
        self.log_technique_event("动态技术", "查看", "查看了动态审计技术")
    
    def show_manual_techniques(self):
        """显示手动审计技术"""
        print("\n--- 手动审计技术 ---")
        for technique, description in self.manual_techniques.items():
            print(f"- {technique}: {description}")
        
        self.log_technique_event("手动技术", "查看", "查看了手动审计技术")
    
    def detect_sql_injection(self, code):
        """检测SQL注入漏洞"""
        print("\n--- 检测SQL注入漏洞 ---")
        print(f"代码: {code}")
        
        # SQL注入模式
        sql_injection_patterns = [
            r'\bSELECT.*FROM.*WHERE.*\b.*\$',
            r'\bINSERT.*INTO.*VALUES.*\$',
            r'\bUPDATE.*SET.*WHERE.*\$',
            r'\bDELETE.*FROM.*WHERE.*\$'
        ]
        
        # 检测SQL注入
        for pattern in sql_injection_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                if not re.search(r'\?|prepare|bind', code, re.IGNORECASE):
                    print("检测到SQL注入漏洞")
                    self.log_technique_event("SQL注入检测", "完成", "检测到SQL注入漏洞")
                    return True
        
        print("未检测到SQL注入漏洞")
        self.log_technique_event("SQL注入检测", "完成", "未检测到SQL注入漏洞")
        return False
    
    def detect_xss(self, code):
        """检测XSS漏洞"""
        print("\n--- 检测XSS漏洞 ---")
        print(f"代码: {code}")
        
        # XSS模式
        xss_patterns = [
            r'echo.*\$',
            r'print.*\$',
            r'\bresponse\.write\(.*\$',
            r'\bdocument\.write\(.*\$'
        ]
        
        # 检测XSS
        for pattern in xss_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                if not re.search(r'htmlspecialchars|escape|sanitize', code, re.IGNORECASE):
                    print("检测到XSS漏洞")
                    self.log_technique_event("XSS检测", "完成", "检测到XSS漏洞")
                    return True
        
        print("未检测到XSS漏洞")
        self.log_technique_event("XSS检测", "完成", "未检测到XSS漏洞")
        return False
    
    def detect_csrf(self, code):
        """检测CSRF漏洞"""
        print("\n--- 检测CSRF漏洞 ---")
        print(f"代码: {code}")
        
        # CSRF模式
        csrf_patterns = [
            r'\bPOST\b.*\bform\b',
            r'\bform.*\bmethod="POST"',
            r'\bform.*\baction='
        ]
        
        # 检测CSRF
        for pattern in csrf_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                if not re.search(r'csrf|token|nonce', code, re.IGNORECASE):
                    print("检测到CSRF漏洞")
                    self.log_technique_event("CSRF检测", "完成", "检测到CSRF漏洞")
                    return True
        
        print("未检测到CSRF漏洞")
        self.log_technique_event("CSRF检测", "完成", "未检测到CSRF漏洞")
        return False
    
    def simulate_audit_techniques(self):
        """模拟审计技术的使用"""
        print("\n--- 模拟审计技术的使用 ---")
        
        # 1. 静态审计技术
        print("1. 静态审计技术:")
        print("   - 使用词法分析分析代码语法")
        print("   - 使用语义分析分析代码逻辑")
        print("   - 使用数据流分析分析数据流动")
        time.sleep(1)
        
        # 2. 动态审计技术
        print("\n2. 动态审计技术:")
        print("   - 使用黑盒测试测试输入输出")
        print("   - 使用白盒测试测试代码逻辑")
        print("   - 使用模糊测试测试边界情况")
        time.sleep(1)
        
        # 3. 手动审计技术
        print("\n3. 手动审计技术:")
        print("   - 手动审查代码，发现安全漏洞")
        print("   - 审查安全设计，发现设计层面的问题")
        print("   - 进行威胁建模，识别潜在威胁")
        time.sleep(1)
        
        # 4. 混合审计技术
        print("\n4. 混合审计技术:")
        print("   - 结合静态和动态审计技术")
        print("   - 结合自动化和手动审计技术")
        print("   - 综合分析审计结果")
        time.sleep(1)
        
        print("\n审计技术使用模拟完成！")
        self.log_technique_event("审计技术", "模拟", "完成了审计技术使用模拟")
    
    def log_technique_event(self, activity, action, message):
        """记录技术事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "action": action,
            "message": message
        }
        self.technique_logs.append(log_entry)
    
    def show_technique_logs(self):
        """显示技术日志"""
        print("\n--- 技术日志 ---")
        for log in self.technique_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['action']}: {log['message']}")
    
    def generate_technique_report(self):
        """生成技术报告"""
        print("\n--- 生成技术报告 ---")
        
        report = {
            "report_info": {
                "title": "代码审计技术报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "CodeAuditTechniquesDemo"
            },
            "technique_categories": self.technique_categories,
            "static_techniques": self.static_techniques,
            "dynamic_techniques": self.dynamic_techniques,
            "manual_techniques": self.manual_techniques,
            "logs": self.technique_logs,
            "recommendations": [
                "根据项目的需求选择合适的审计技术",
                "结合多种审计技术，提高审计效果",
                "使用自动化工具辅助审计技术的实施",
                "定期更新审计技术，适应新的安全威胁",
                "对审计人员进行技术培训，提高审计能力"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_code_audit_techniques(self):
        """演示代码审计技术"""
        print("=== 代码审计技术演示 ===")
        print("==================")
        
        # 1. 显示代码审计技术分类
        print("\n1. 代码审计技术分类:")
        self.show_technique_categories()
        
        # 2. 显示静态审计技术
        print("\n2. 静态审计技术:")
        self.show_static_techniques()
        
        # 3. 显示动态审计技术
        print("\n3. 动态审计技术:")
        self.show_dynamic_techniques()
        
        # 4. 显示手动审计技术
        print("\n4. 手动审计技术:")
        self.show_manual_techniques()
        
        # 5. 检测SQL注入漏洞
        print("\n5. 检测SQL注入漏洞:")
        self.detect_sql_injection("query = 'SELECT * FROM users WHERE id = ' + user_id")
        self.detect_sql_injection("query = 'SELECT * FROM users WHERE id = ?'")
        
        # 6. 检测XSS漏洞
        print("\n6. 检测XSS漏洞:")
        self.detect_xss("echo $user_input")
        self.detect_xss("echo htmlspecialchars($user_input)")
        
        # 7. 检测CSRF漏洞
        print("\n7. 检测CSRF漏洞:")
        self.detect_csrf('<form method="POST" action="/submit">')
        self.detect_csrf('<form method="POST" action="/submit"><input type="hidden" name="csrf_token" value="...">')
        
        # 8. 模拟审计技术的使用
        print("\n8. 模拟审计技术的使用:")
        self.simulate_audit_techniques()
        
        # 9. 显示技术日志
        print("\n9. 技术日志:")
        self.show_technique_logs()
        
        # 10. 生成技术报告
        print("\n10. 生成技术报告:")
        self.generate_technique_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了代码审计的技术和方法。")
        print("选择合适的审计技术是提高代码审计效率和效果的关键。")

if __name__ == "__main__":
    code_audit_techniques_demo = CodeAuditTechniquesDemo()
    code_audit_techniques_demo.demonstrate_code_audit_techniques()