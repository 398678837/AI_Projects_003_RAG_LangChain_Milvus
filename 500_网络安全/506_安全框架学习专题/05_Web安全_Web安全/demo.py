import os
import sys
import json
import time
import re
from datetime import datetime
import urllib.parse

class WebSecurityDemo:
    def __init__(self):
        # Web安全漏洞类型
        self.vulnerabilities = {
            "XSS": "跨站脚本攻击",
            "SQL注入": "SQL注入攻击",
            "CSRF": "跨站请求伪造",
            "命令注入": "命令注入攻击",
            "敏感信息泄露": "敏感信息泄露",
            "权限绕过": "权限绕过攻击",
            "不安全的直接对象引用": "不安全的直接对象引用",
            "安全配置错误": "安全配置错误"
        }
        
        # 安全防护措施
        self.security_measures = {
            "输入验证": "验证所有用户输入",
            "输出编码": "对输出进行编码",
            "参数化查询": "使用参数化查询防止SQL注入",
            "CSRF令牌": "使用CSRF令牌防止CSRF攻击",
            "访问控制": "实施严格的访问控制",
            "安全配置": "正确配置安全设置",
            "加密": "使用加密保护敏感数据",
            "安全审计": "定期进行安全审计"
        }
        
        # Web安全日志
        self.security_logs = []
    
    def detect_xss(self, input_data):
        """检测XSS攻击"""
        print("\n--- 检测XSS攻击 ---")
        print(f"输入数据: {input_data}")
        
        # XSS攻击模式
        xss_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:',
            r'on\w+\s*=\s*["\'].*?["\']',
            r'<iframe[^>]*>.*?</iframe>',
            r'<img[^>]*onerror[^>]*>'
        ]
        
        # 检测XSS攻击
        for pattern in xss_patterns:
            if re.search(pattern, input_data, re.IGNORECASE):
                print("检测到XSS攻击")
                self.log_security_event("XSS", "检测", True, f"检测到XSS攻击: {input_data}")
                return True
        
        print("未检测到XSS攻击")
        self.log_security_event("XSS", "检测", False, f"未检测到XSS攻击: {input_data}")
        return False
    
    def detect_sql_injection(self, input_data):
        """检测SQL注入攻击"""
        print("\n--- 检测SQL注入攻击 ---")
        print(f"输入数据: {input_data}")
        
        # SQL注入攻击模式
        sql_patterns = [
            r'\b(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|EXEC)\b',
            r'\b(OR|AND|NOT)\b\s+\d+\s*=\s*\d+',
            r'\bUNION\b\s+SELECT',
            r'\bFROM\b\s+information_schema\.',
            r'--',
            r';',
            r'\bWAITFOR\b\s+DELAY'
        ]
        
        # 检测SQL注入攻击
        for pattern in sql_patterns:
            if re.search(pattern, input_data, re.IGNORECASE):
                print("检测到SQL注入攻击")
                self.log_security_event("SQL注入", "检测", True, f"检测到SQL注入攻击: {input_data}")
                return True
        
        print("未检测到SQL注入攻击")
        self.log_security_event("SQL注入", "检测", False, f"未检测到SQL注入攻击: {input_data}")
        return False
    
    def detect_csrf(self, request_data):
        """检测CSRF攻击"""
        print("\n--- 检测CSRF攻击 ---")
        print(f"请求数据: {request_data}")
        
        # 检查是否包含CSRF令牌
        if "csrf_token" not in request_data:
            print("检测到CSRF攻击: 缺少CSRF令牌")
            self.log_security_event("CSRF", "检测", True, f"检测到CSRF攻击: 缺少CSRF令牌")
            return True
        
        # 检查CSRF令牌是否有效（模拟）
        if request_data["csrf_token"] != "valid_token":
            print("检测到CSRF攻击: 无效的CSRF令牌")
            self.log_security_event("CSRF", "检测", True, f"检测到CSRF攻击: 无效的CSRF令牌")
            return True
        
        print("未检测到CSRF攻击")
        self.log_security_event("CSRF", "检测", False, f"未检测到CSRF攻击: {request_data}")
        return False
    
    def detect_command_injection(self, input_data):
        """检测命令注入攻击"""
        print("\n--- 检测命令注入攻击 ---")
        print(f"输入数据: {input_data}")
        
        # 命令注入攻击模式
        command_patterns = [
            r'\|',
            r';',
            r'&&',
            r'\&',
            r'\|\|',
            r'\<',
            r'\>',
            r'\$\(',
            r'`',
            r'\b(echo|cat|ls|pwd|whoami|ifconfig|ipconfig)\b'
        ]
        
        # 检测命令注入攻击
        for pattern in command_patterns:
            if re.search(pattern, input_data):
                print("检测到命令注入攻击")
                self.log_security_event("命令注入", "检测", True, f"检测到命令注入攻击: {input_data}")
                return True
        
        print("未检测到命令注入攻击")
        self.log_security_event("命令注入", "检测", False, f"未检测到命令注入攻击: {input_data}")
        return False
    
    def sanitize_input(self, input_data):
        """输入 sanitization"""
        print("\n--- 输入 sanitization ---")
        print(f"原始输入: {input_data}")
        
        # 移除HTML标签
        sanitized = re.sub(r'<[^>]*>', '', input_data)
        
        # URL编码
        sanitized = urllib.parse.quote(sanitized)
        
        print(f"Sanitized输入: {sanitized}")
        self.log_security_event("输入验证", "Sanitization", True, f"Sanitized输入: {sanitized}")
        return sanitized
    
    def log_security_event(self, vulnerability, action, detected, message):
        """记录安全事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "vulnerability": vulnerability,
            "action": action,
            "detected": detected,
            "message": message
        }
        self.security_logs.append(log_entry)
    
    def show_vulnerabilities(self):
        """显示Web安全漏洞类型"""
        print("\n--- Web安全漏洞类型 ---")
        for vuln, description in self.vulnerabilities.items():
            print(f"- {vuln}: {description}")
    
    def show_security_measures(self):
        """显示安全防护措施"""
        print("\n--- 安全防护措施 ---")
        for measure, description in self.security_measures.items():
            print(f"- {measure}: {description}")
    
    def show_security_logs(self):
        """显示安全日志"""
        print("\n--- 安全日志 ---")
        for log in self.security_logs:
            status = "检测到" if log["detected"] else "未检测到"
            print(f"[{log['timestamp']}] {log['vulnerability']} - {log['action']} - {status}: {log['message']}")
    
    def generate_security_report(self):
        """生成安全报告"""
        print("\n--- 生成安全报告 ---")
        
        # 统计安全事件
        total_events = len(self.security_logs)
        detected_events = sum(1 for log in self.security_logs if log["detected"])
        undetected_events = total_events - detected_events
        
        # 统计漏洞类型
        vulnerability_stats = {}
        for log in self.security_logs:
            vuln = log["vulnerability"]
            if vuln not in vulnerability_stats:
                vulnerability_stats[vuln] = {"total": 0, "detected": 0}
            vulnerability_stats[vuln]["total"] += 1
            if log["detected"]:
                vulnerability_stats[vuln]["detected"] += 1
        
        report = {
            "report_info": {
                "title": "Web安全报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "WebSecurityDemo"
            },
            "security_summary": {
                "total_events": total_events,
                "detected_events": detected_events,
                "undetected_events": undetected_events,
                "detection_rate": detected_events / total_events if total_events > 0 else 0
            },
            "vulnerability_stats": vulnerability_stats,
            "vulnerabilities": self.vulnerabilities,
            "security_measures": self.security_measures,
            "recommendations": [
                "实施输入验证",
                "使用参数化查询",
                "实施CSRF保护",
                "定期进行安全扫描",
                "保持系统和依赖项更新"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_web_security(self):
        """演示Web安全"""
        print("=== Web安全演示 ===")
        print("====================")
        
        # 1. 显示Web安全漏洞类型
        print("\n1. Web安全漏洞类型:")
        self.show_vulnerabilities()
        
        # 2. 显示安全防护措施
        print("\n2. 安全防护措施:")
        self.show_security_measures()
        
        # 3. 测试XSS检测
        print("\n3. 测试XSS检测:")
        self.detect_xss("<script>alert('XSS')</script>")
        self.detect_xss("正常输入")
        
        # 4. 测试SQL注入检测
        print("\n4. 测试SQL注入检测:")
        self.detect_sql_injection("1' OR 1=1 --")
        self.detect_sql_injection("正常输入")
        
        # 5. 测试CSRF检测
        print("\n5. 测试CSRF检测:")
        self.detect_csrf({"action": "delete", "id": "1"})
        self.detect_csrf({"action": "delete", "id": "1", "csrf_token": "valid_token"})
        
        # 6. 测试命令注入检测
        print("\n6. 测试命令注入检测:")
        self.detect_command_injection("file.txt; ls")
        self.detect_command_injection("正常输入")
        
        # 7. 测试输入sanitization
        print("\n7. 测试输入sanitization:")
        self.sanitize_input("<script>alert('XSS')</script>")
        
        # 8. 显示安全日志
        print("\n8. 安全日志:")
        self.show_security_logs()
        
        # 9. 生成安全报告
        print("\n9. 生成安全报告:")
        self.generate_security_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了Web安全的基本概念和常见漏洞。")
        print("Web安全是安全框架的重要组成部分，用于保护Web应用程序免受攻击。")

if __name__ == "__main__":
    web_security_demo = WebSecurityDemo()
    web_security_demo.demonstrate_web_security()