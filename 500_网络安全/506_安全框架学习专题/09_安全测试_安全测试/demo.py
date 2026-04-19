import os
import sys
import json
import time
import re
from datetime import datetime

class SecurityTestingDemo:
    def __init__(self):
        # 安全测试类型
        self.test_types = {
            "静态代码分析": "分析源代码，发现安全漏洞",
            "动态应用安全测试": "在运行时测试应用程序的安全性",
            "依赖项扫描": "扫描依赖项的安全漏洞",
            "渗透测试": "模拟攻击者的行为，测试系统的安全性",
            "安全配置测试": "测试系统的安全配置",
            "网络安全测试": "测试网络的安全性",
            "移动应用安全测试": "测试移动应用的安全性",
            "云安全测试": "测试云环境的安全性"
        }
        
        # 安全测试工具
        self.test_tools = {
            "OWASP ZAP": "开源的Web应用安全测试工具",
            "Nmap": "网络扫描工具",
            "Burp Suite": "Web应用安全测试工具",
            "SonarQube": "静态代码分析工具",
            "Dependency-Check": "依赖项扫描工具",
            "Metasploit": "渗透测试框架",
            "Nikto": "Web服务器扫描工具",
            "OpenVAS": "漏洞扫描工具"
        }
        
        # 安全测试日志
        self.test_logs = []
    
    def run_static_code_analysis(self, code):
        """运行静态代码分析"""
        print("\n--- 运行静态代码分析 ---")
        print(f"代码: {code}")
        
        # 模拟静态代码分析
        vulnerabilities = []
        
        # 检查硬编码凭证
        if re.search(r'password\s*=\s*["\'][^"\']*["\']', code, re.IGNORECASE):
            vulnerabilities.append("硬编码凭证")
        
        # 检查SQL注入
        if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE)\b.*\bWHERE\b.*\s+\w+\s*=\s*["\']\s*\+\s*\w+\s*\+\s*["\']', code, re.IGNORECASE):
            vulnerabilities.append("SQL注入")
        
        # 检查XSS
        if re.search(r'echo\s+\$_(GET|POST|REQUEST)\[', code, re.IGNORECASE):
            vulnerabilities.append("XSS攻击")
        
        if vulnerabilities:
            print(f"发现漏洞: {', '.join(vulnerabilities)}")
            self.log_test_event("静态代码分析", "完成", f"发现 {len(vulnerabilities)} 个漏洞: {', '.join(vulnerabilities)}")
            return vulnerabilities
        else:
            print("未发现漏洞")
            self.log_test_event("静态代码分析", "完成", "未发现漏洞")
            return []
    
    def run_dynamic_security_test(self, url):
        """运行动态应用安全测试"""
        print("\n--- 运行动态应用安全测试 ---")
        print(f"URL: {url}")
        
        # 模拟动态应用安全测试
        vulnerabilities = []
        
        # 检查SQL注入
        if "test" in url:
            vulnerabilities.append("SQL注入")
        
        # 检查XSS
        if "search" in url:
            vulnerabilities.append("XSS攻击")
        
        # 检查CSRF
        if "form" in url:
            vulnerabilities.append("CSRF攻击")
        
        if vulnerabilities:
            print(f"发现漏洞: {', '.join(vulnerabilities)}")
            self.log_test_event("动态应用安全测试", "完成", f"发现 {len(vulnerabilities)} 个漏洞: {', '.join(vulnerabilities)}")
            return vulnerabilities
        else:
            print("未发现漏洞")
            self.log_test_event("动态应用安全测试", "完成", "未发现漏洞")
            return []
    
    def run_dependency_scan(self, dependencies):
        """运行依赖项扫描"""
        print("\n--- 运行依赖项扫描 ---")
        print(f"依赖项: {dependencies}")
        
        # 模拟依赖项扫描
        vulnerable_dependencies = []
        
        # 检查存在安全漏洞的依赖项
        for dep in dependencies:
            if any(vuln in dep for vuln in ["jquery@1.12.0", "lodash@4.17.0", "express@4.16.0"]):
                vulnerable_dependencies.append(dep)
        
        if vulnerable_dependencies:
            print(f"发现存在安全漏洞的依赖项: {', '.join(vulnerable_dependencies)}")
            self.log_test_event("依赖项扫描", "完成", f"发现 {len(vulnerable_dependencies)} 个存在安全漏洞的依赖项: {', '.join(vulnerable_dependencies)}")
            return vulnerable_dependencies
        else:
            print("未发现存在安全漏洞的依赖项")
            self.log_test_event("依赖项扫描", "完成", "未发现存在安全漏洞的依赖项")
            return []
    
    def run_network_security_test(self, network):
        """运行网络安全测试"""
        print("\n--- 运行网络安全测试 ---")
        print(f"网络: {network}")
        
        # 模拟网络安全测试
        vulnerabilities = []
        
        # 检查开放端口
        if "192.168.1.1" in network:
            vulnerabilities.append("开放端口")
        
        # 检查弱密码
        if "test" in network:
            vulnerabilities.append("弱密码")
        
        # 检查不安全的协议
        if "http://" in network:
            vulnerabilities.append("不安全的协议")
        
        if vulnerabilities:
            print(f"发现漏洞: {', '.join(vulnerabilities)}")
            self.log_test_event("网络安全测试", "完成", f"发现 {len(vulnerabilities)} 个漏洞: {', '.join(vulnerabilities)}")
            return vulnerabilities
        else:
            print("未发现漏洞")
            self.log_test_event("网络安全测试", "完成", "未发现漏洞")
            return []
    
    def log_test_event(self, test_type, status, message):
        """记录测试事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "test_type": test_type,
            "status": status,
            "message": message
        }
        self.test_logs.append(log_entry)
    
    def show_test_types(self):
        """显示安全测试类型"""
        print("\n--- 安全测试类型 ---")
        for test_type, description in self.test_types.items():
            print(f"- {test_type}: {description}")
    
    def show_test_tools(self):
        """显示安全测试工具"""
        print("\n--- 安全测试工具 ---")
        for tool, description in self.test_tools.items():
            print(f"- {tool}: {description}")
    
    def show_test_logs(self):
        """显示测试日志"""
        print("\n--- 测试日志 ---")
        for log in self.test_logs:
            print(f"[{log['timestamp']}] {log['test_type']} - {log['status']}: {log['message']}")
    
    def generate_test_report(self):
        """生成测试报告"""
        print("\n--- 生成测试报告 ---")
        
        # 统计测试事件
        total_tests = len(self.test_logs)
        completed_tests = sum(1 for log in self.test_logs if log["status"] == "完成")
        
        # 统计漏洞
        total_vulnerabilities = 0
        for log in self.test_logs:
            if "发现" in log["message"] and "漏洞" in log["message"]:
                # 提取漏洞数量
                match = re.search(r'发现\s+(\d+)\s+个', log["message"])
                if match:
                    total_vulnerabilities += int(match.group(1))
        
        report = {
            "report_info": {
                "title": "安全测试报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "SecurityTestingDemo"
            },
            "test_summary": {
                "total_tests": total_tests,
                "completed_tests": completed_tests,
                "total_vulnerabilities": total_vulnerabilities
            },
            "test_types": self.test_types,
            "test_tools": self.test_tools,
            "test_logs": self.test_logs,
            "recommendations": [
                "修复发现的安全漏洞",
                "定期进行安全测试",
                "使用安全测试工具",
                "对开发人员进行安全培训",
                "建立安全测试流程"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_security_testing(self):
        """演示安全测试"""
        print("=== 安全测试演示 ===")
        print("====================")
        
        # 1. 显示安全测试类型
        print("\n1. 安全测试类型:")
        self.show_test_types()
        
        # 2. 显示安全测试工具
        print("\n2. 安全测试工具:")
        self.show_test_tools()
        
        # 3. 运行静态代码分析
        print("\n3. 运行静态代码分析:")
        code = "password = 'secret123'; $query = 'SELECT * FROM users WHERE id = ' . $_GET['id']; echo $_GET['name'];"
        self.run_static_code_analysis(code)
        
        # 4. 运行动态应用安全测试
        print("\n4. 运行动态应用安全测试:")
        url = "http://example.com/test.php?id=1&search=test&form=submit"
        self.run_dynamic_security_test(url)
        
        # 5. 运行依赖项扫描
        print("\n5. 运行依赖项扫描:")
        dependencies = ["jquery@1.12.0", "react@18.0.0", "lodash@4.17.0", "express@4.16.0"]
        self.run_dependency_scan(dependencies)
        
        # 6. 运行网络安全测试
        print("\n6. 运行网络安全测试:")
        network = "192.168.1.1/test http://example.com"
        self.run_network_security_test(network)
        
        # 7. 显示测试日志
        print("\n7. 测试日志:")
        self.show_test_logs()
        
        # 8. 生成测试报告
        print("\n8. 生成测试报告:")
        self.generate_test_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了安全测试的基本概念和常见测试方法。")
        print("安全测试是安全框架的重要组成部分，用于发现和修复安全漏洞。")

if __name__ == "__main__":
    security_testing_demo = SecurityTestingDemo()
    security_testing_demo.demonstrate_security_testing()