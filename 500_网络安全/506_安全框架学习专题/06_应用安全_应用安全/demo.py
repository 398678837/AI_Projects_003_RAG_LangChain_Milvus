import os
import sys
import json
import time
import re
from datetime import datetime
import hashlib

class ApplicationSecurityDemo:
    def __init__(self):
        # 应用安全漏洞类型
        self.vulnerabilities = {
            "不安全的依赖项": "使用存在安全漏洞的依赖项",
            "硬编码凭证": "在代码中硬编码凭证",
            "不安全的随机数生成": "使用不安全的随机数生成器",
            "内存安全问题": "内存泄漏、缓冲区溢出等",
            "不安全的序列化": "不安全的对象序列化",
            "日志注入": "日志中包含敏感信息",
            "不安全的异常处理": "异常信息泄露敏感数据",
            "缺少安全头部": "缺少安全相关的HTTP头部"
        }
        
        # 应用安全防护措施
        self.security_measures = {
            "依赖项管理": "定期更新依赖项，修复安全漏洞",
            "安全编码实践": "遵循安全编码规范",
            "安全配置": "正确配置应用程序的安全设置",
            "安全测试": "定期进行安全测试",
            "安全审计": "定期进行安全审计",
            "安全监控": "监控应用程序的安全状态",
            "安全培训": "对开发人员进行安全培训"
        }
        
        # 应用安全日志
        self.security_logs = []
    
    def check_dependency_security(self, dependencies):
        """检查依赖项安全性"""
        print("\n--- 检查依赖项安全性 ---")
        print(f"依赖项: {dependencies}")
        
        # 模拟存在安全漏洞的依赖项
        vulnerable_dependencies = ["jquery@1.12.0", "lodash@4.17.0", "express@4.16.0"]
        
        # 检查依赖项
        vulnerable = []
        for dep in dependencies:
            if dep in vulnerable_dependencies:
                vulnerable.append(dep)
        
        if vulnerable:
            print(f"检测到存在安全漏洞的依赖项: {', '.join(vulnerable)}")
            self.log_security_event("依赖项安全", "检测", True, f"检测到存在安全漏洞的依赖项: {', '.join(vulnerable)}")
            return True
        else:
            print("未检测到存在安全漏洞的依赖项")
            self.log_security_event("依赖项安全", "检测", False, "未检测到存在安全漏洞的依赖项")
            return False
    
    def check_hardcoded_credentials(self, code):
        """检查硬编码凭证"""
        print("\n--- 检查硬编码凭证 ---")
        print(f"代码: {code}")
        
        # 硬编码凭证模式
        credential_patterns = [
            r'password\s*=\s*["\'][^"\']*["\']',
            r'secret\s*=\s*["\'][^"\']*["\']',
            r'api_key\s*=\s*["\'][^"\']*["\']',
            r'token\s*=\s*["\'][^"\']*["\']'
        ]
        
        # 检查硬编码凭证
        for pattern in credential_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                print("检测到硬编码凭证")
                self.log_security_event("硬编码凭证", "检测", True, f"检测到硬编码凭证: {code}")
                return True
        
        print("未检测到硬编码凭证")
        self.log_security_event("硬编码凭证", "检测", False, "未检测到硬编码凭证")
        return False
    
    def check_insecure_random(self, code):
        """检查不安全的随机数生成"""
        print("\n--- 检查不安全的随机数生成 ---")
        print(f"代码: {code}")
        
        # 不安全的随机数生成模式
        insecure_random_patterns = [
            r'Math\.random\(\)',
            r'Random\.nextInt\(\)',
            r'rand\(\)',
            r'randint\(\)'
        ]
        
        # 检查不安全的随机数生成
        for pattern in insecure_random_patterns:
            if re.search(pattern, code):
                print("检测到不安全的随机数生成")
                self.log_security_event("随机数生成", "检测", True, f"检测到不安全的随机数生成: {code}")
                return True
        
        print("未检测到不安全的随机数生成")
        self.log_security_event("随机数生成", "检测", False, "未检测到不安全的随机数生成")
        return False
    
    def check_secure_headers(self, headers):
        """检查安全头部"""
        print("\n--- 检查安全头部 ---")
        print(f"头部: {headers}")
        
        # 必需的安全头部
        required_headers = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]
        
        # 检查安全头部
        missing_headers = []
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)
        
        if missing_headers:
            print(f"缺少安全头部: {', '.join(missing_headers)}")
            self.log_security_event("安全头部", "检测", True, f"缺少安全头部: {', '.join(missing_headers)}")
            return True
        else:
            print("所有安全头部都存在")
            self.log_security_event("安全头部", "检测", False, "所有安全头部都存在")
            return False
    
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
        """显示应用安全漏洞类型"""
        print("\n--- 应用安全漏洞类型 ---")
        for vuln, description in self.vulnerabilities.items():
            print(f"- {vuln}: {description}")
    
    def show_security_measures(self):
        """显示应用安全防护措施"""
        print("\n--- 应用安全防护措施 ---")
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
                "title": "应用安全报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "ApplicationSecurityDemo"
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
                "定期更新依赖项",
                "避免硬编码凭证",
                "使用安全的随机数生成器",
                "实施安全头部",
                "定期进行安全测试"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_application_security(self):
        """演示应用安全"""
        print("=== 应用安全演示 ===")
        print("====================")
        
        # 1. 显示应用安全漏洞类型
        print("\n1. 应用安全漏洞类型:")
        self.show_vulnerabilities()
        
        # 2. 显示应用安全防护措施
        print("\n2. 应用安全防护措施:")
        self.show_security_measures()
        
        # 3. 测试依赖项安全性
        print("\n3. 测试依赖项安全性:")
        dependencies = ["jquery@1.12.0", "react@18.0.0", "vue@3.0.0"]
        self.check_dependency_security(dependencies)
        
        # 4. 测试硬编码凭证
        print("\n4. 测试硬编码凭证:")
        code_with_credentials = "password = 'secret123'; api_key = 'abc123'"
        code_without_credentials = "username = input('Enter username:')"
        self.check_hardcoded_credentials(code_with_credentials)
        self.check_hardcoded_credentials(code_without_credentials)
        
        # 5. 测试不安全的随机数生成
        print("\n5. 测试不安全的随机数生成:")
        code_with_insecure_random = "const random = Math.random();"
        code_with_secure_random = "const crypto = require('crypto'); const random = crypto.randomBytes(32);"
        self.check_insecure_random(code_with_insecure_random)
        self.check_insecure_random(code_with_secure_random)
        
        # 6. 测试安全头部
        print("\n6. 测试安全头部:")
        headers_with_missing = {"Content-Type": "text/html"}
        headers_complete = {
            "Content-Type": "text/html",
            "Content-Security-Policy": "default-src 'self'",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Strict-Transport-Security": "max-age=31536000"
        }
        self.check_secure_headers(headers_with_missing)
        self.check_secure_headers(headers_complete)
        
        # 7. 显示安全日志
        print("\n7. 安全日志:")
        self.show_security_logs()
        
        # 8. 生成安全报告
        print("\n8. 生成安全报告:")
        self.generate_security_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了应用安全的基本概念和常见漏洞。")
        print("应用安全是安全框架的重要组成部分，用于保护应用程序免受攻击。")

if __name__ == "__main__":
    app_security_demo = ApplicationSecurityDemo()
    app_security_demo.demonstrate_application_security()