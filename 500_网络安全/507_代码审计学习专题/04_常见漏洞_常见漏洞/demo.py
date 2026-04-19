import os
import sys
import json
import re
import time
from datetime import datetime

class CommonVulnerabilitiesDemo:
    def __init__(self):
        # 常见漏洞分类
        self.vulnerability_categories = {
            "注入漏洞": "攻击者将恶意代码注入到应用程序中，执行未授权的操作",
            "跨站脚本(XSS)": "攻击者将恶意脚本注入到网页中，在用户浏览器中执行",
            "跨站请求伪造(CSRF)": "攻击者诱导用户执行未授权的操作",
            "认证漏洞": "认证机制存在缺陷，导致未授权访问",
            "授权漏洞": "授权机制存在缺陷，导致权限提升",
            "敏感数据泄露": "敏感数据未加密或保护不足，导致数据泄露",
            "安全配置错误": "系统或应用的安全配置错误，导致安全漏洞",
            "使用有漏洞的依赖项": "使用存在安全漏洞的依赖项",
            "日志记录和监控不足": "日志记录和监控不足，导致安全事件无法及时发现",
            "服务器端请求伪造(SSRF)": "攻击者诱导服务器向内部或外部资源发送请求"
        }
        
        # 常见漏洞详情
        self.common_vulnerabilities = {
            "SQL注入": {
                "描述": "攻击者将SQL代码注入到应用程序中，执行未授权的数据库操作",
                "危害": "数据泄露、数据篡改、数据库服务器被控制",
                "示例": "SELECT * FROM users WHERE id = ' + user_id",
                "修复": "使用参数化查询、预编译语句、输入验证"
            },
            "XSS": {
                "描述": "攻击者将恶意脚本注入到网页中，在用户浏览器中执行",
                "危害": "会话劫持、数据窃取、钓鱼攻击",
                "示例": "echo $user_input",
                "修复": "输入验证、输出编码、Content-Security-Policy"
            },
            "CSRF": {
                "描述": "攻击者诱导用户执行未授权的操作",
                "危害": "未授权操作、数据篡改、权限提升",
                "示例": "<form method=\"POST\" action=\"/transfer\">",
                "修复": "CSRF token、SameSite cookie、验证Referer头"
            },
            "认证绕过": {
                "描述": "攻击者绕过认证机制，未授权访问系统",
                "危害": "未授权访问、数据泄露、系统被控制",
                "示例": "if (user_id == 1) { login(); }",
                "修复": "严格的认证验证、会话管理、权限检查"
            },
            "权限提升": {
                "描述": "攻击者利用授权漏洞，获取更高的权限",
                "危害": "权限提升、未授权操作、系统被控制",
                "示例": "if (user_role == 'user') { access_admin_panel(); }",
                "修复": "严格的权限检查、最小权限原则、权限分离"
            },
            "敏感数据泄露": {
                "描述": "敏感数据未加密或保护不足，导致数据泄露",
                "危害": "数据泄露、隐私侵犯、身份盗窃",
                "示例": "echo $password",
                "修复": "数据加密、访问控制、敏感数据处理规范"
            },
            "安全配置错误": {
                "描述": "系统或应用的安全配置错误，导致安全漏洞",
                "危害": "未授权访问、数据泄露、系统被控制",
                "示例": "DEBUG = True",
                "修复": "安全配置检查、最小权限原则、定期安全审计"
            },
            "依赖项漏洞": {
                "描述": "使用存在安全漏洞的依赖项",
                "危害": "未授权访问、数据泄露、系统被控制",
                "示例": "使用有漏洞的库版本",
                "修复": "定期更新依赖项、依赖项扫描、安全审计"
            },
            "日志记录不足": {
                "描述": "日志记录不足，导致安全事件无法及时发现",
                "危害": "安全事件无法及时发现、取证困难",
                "示例": "未记录关键操作",
                "修复": "全面的日志记录、日志分析、监控系统"
            },
            "SSRF": {
                "描述": "攻击者诱导服务器向内部或外部资源发送请求",
                "危害": "内部资源访问、数据泄露、系统被控制",
                "示例": "file_get_contents($_GET['url'])",
                "修复": "输入验证、白名单、网络隔离"
            }
        }
        
        # 漏洞检测规则
        self.vulnerability_rules = {
            "SQL注入": [
                r'\bSELECT.*FROM.*WHERE.*\b.*\$',
                r'\bINSERT.*INTO.*VALUES.*\$',
                r'\bUPDATE.*SET.*WHERE.*\$',
                r'\bDELETE.*FROM.*WHERE.*\$'
            ],
            "XSS": [
                r'echo.*\$',
                r'print.*\$',
                r'\bresponse\.write\(.*\$',
                r'\bdocument\.write\(.*\$'
            ],
            "CSRF": [
                r'\bPOST\b.*\bform\b',
                r'\bform.*\bmethod="POST"',
                r'\bform.*\baction='
            ],
            "认证绕过": [
                r'if.*==.*1.*\{.*login\(\).*\}',
                r'if.*==.*admin.*\{.*login\(\).*\}',
                r'if.*user_id.*==.*1.*\{.*login\(\).*\}'
            ],
            "权限提升": [
                r'if.*user_role.*==.*user.*\{.*access_admin.*\}',
                r'if.*role.*==.*user.*\{.*access_admin.*\}',
                r'if.*permission.*==.*user.*\{.*access_admin.*\}'
            ],
            "敏感数据泄露": [
                r'echo.*password.*\$',
                r'print.*password.*\$',
                r'echo.*secret.*\$',
                r'print.*secret.*\$'
            ],
            "安全配置错误": [
                r'DEBUG.*=.*True',
                r'DEBUG.*=.*true',
                r'ALLOWED_HOSTS.*=.*\[\'\*\'\]'
            ],
            "依赖项漏洞": [
                r'\bversion\b.*=.*\d+\.\d+\.\d+',
                r'\bdependency\b.*=.*\d+\.\d+\.\d+',
                r'\brequire\b.*=.*\d+\.\d+\.\d+'
            ],
            "日志记录不足": [
                r'\bprint\b.*\$',
                r'\becho\b.*\$',
                r'\blog\b.*\(.*\$'
            ],
            "SSRF": [
                r'file_get_contents\(.*\$',
                r'curl\(.*\$',
                r'\bhttp.*\(.*\$'
            ]
        }
        
        # 漏洞日志
        self.vulnerability_logs = []
    
    def show_vulnerability_categories(self):
        """显示常见漏洞分类"""
        print("\n--- 常见漏洞分类 ---")
        for category, description in self.vulnerability_categories.items():
            print(f"- {category}: {description}")
        
        self.log_vulnerability_event("漏洞分类", "查看", "查看了常见漏洞分类")
    
    def show_common_vulnerabilities(self):
        """显示常见漏洞详情"""
        print("\n--- 常见漏洞详情 ---")
        for vulnerability, info in self.common_vulnerabilities.items():
            print(f"\n{vulnerability}:")
            print(f"  描述: {info['描述']}")
            print(f"  危害: {info['危害']}")
            print(f"  示例: {info['示例']}")
            print(f"  修复: {info['修复']}")
        
        self.log_vulnerability_event("漏洞详情", "查看", "查看了常见漏洞详情")
    
    def detect_vulnerability(self, code, vulnerability_type):
        """检测漏洞"""
        print(f"\n--- 检测{ vulnerability_type }漏洞 ---")
        print(f"代码: {code}")
        
        if vulnerability_type in self.vulnerability_rules:
            rules = self.vulnerability_rules[vulnerability_type]
            for rule in rules:
                if re.search(rule, code, re.IGNORECASE):
                    print(f"检测到{ vulnerability_type }漏洞")
                    self.log_vulnerability_event(vulnerability_type, "检测", f"检测到{ vulnerability_type }漏洞")
                    return True
        
        print(f"未检测到{ vulnerability_type }漏洞")
        self.log_vulnerability_event(vulnerability_type, "检测", f"未检测到{ vulnerability_type }漏洞")
        return False
    
    def demonstrate_vulnerability_fix(self, vulnerability_type):
        """演示漏洞修复"""
        print(f"\n--- 演示{ vulnerability_type }漏洞修复 ---")
        
        if vulnerability_type == "SQL注入":
            print("漏洞代码: SELECT * FROM users WHERE id = ' + user_id")
            print("修复代码: SELECT * FROM users WHERE id = ?")
            print("修复方法: 使用参数化查询")
        elif vulnerability_type == "XSS":
            print("漏洞代码: echo $user_input")
            print("修复代码: echo htmlspecialchars($user_input)")
            print("修复方法: 输出编码")
        elif vulnerability_type == "CSRF":
            print("漏洞代码: <form method=\"POST\" action=\"/transfer\">")
            print("修复代码: <form method=\"POST\" action=\"/transfer\"><input type=\"hidden\" name=\"csrf_token\" value=\"...\">")
            print("修复方法: 使用CSRF token")
        elif vulnerability_type == "认证绕过":
            print("漏洞代码: if (user_id == 1) { login(); }")
            print("修复代码: if (user_id == 1 && password == 'correct_password') { login(); }")
            print("修复方法: 严格的认证验证")
        elif vulnerability_type == "权限提升":
            print("漏洞代码: if (user_role == 'user') { access_admin_panel(); }")
            print("修复代码: if (user_role == 'admin') { access_admin_panel(); }")
            print("修复方法: 严格的权限检查")
        
        self.log_vulnerability_event(vulnerability_type, "修复", f"演示了{ vulnerability_type }漏洞修复")
    
    def simulate_vulnerability_scan(self):
        """模拟漏洞扫描"""
        print("\n--- 模拟漏洞扫描 ---")
        
        # 1. 扫描SQL注入漏洞
        print("1. 扫描SQL注入漏洞:")
        self.detect_vulnerability("query = 'SELECT * FROM users WHERE id = ' + user_id", "SQL注入")
        time.sleep(1)
        
        # 2. 扫描XSS漏洞
        print("\n2. 扫描XSS漏洞:")
        self.detect_vulnerability("echo $user_input", "XSS")
        time.sleep(1)
        
        # 3. 扫描CSRF漏洞
        print("\n3. 扫描CSRF漏洞:")
        self.detect_vulnerability('<form method="POST" action="/submit">', "CSRF")
        time.sleep(1)
        
        # 4. 扫描认证绕过漏洞
        print("\n4. 扫描认证绕过漏洞:")
        self.detect_vulnerability("if (user_id == 1) { login(); }", "认证绕过")
        time.sleep(1)
        
        # 5. 扫描权限提升漏洞
        print("\n5. 扫描权限提升漏洞:")
        self.detect_vulnerability("if (user_role == 'user') { access_admin_panel(); }", "权限提升")
        time.sleep(1)
        
        print("\n漏洞扫描模拟完成！")
        self.log_vulnerability_event("漏洞扫描", "模拟", "完成了漏洞扫描模拟")
    
    def log_vulnerability_event(self, activity, action, message):
        """记录漏洞事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "action": action,
            "message": message
        }
        self.vulnerability_logs.append(log_entry)
    
    def show_vulnerability_logs(self):
        """显示漏洞日志"""
        print("\n--- 漏洞日志 ---")
        for log in self.vulnerability_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['action']}: {log['message']}")
    
    def generate_vulnerability_report(self):
        """生成漏洞报告"""
        print("\n--- 生成漏洞报告 ---")
        
        report = {
            "report_info": {
                "title": "常见漏洞报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "CommonVulnerabilitiesDemo"
            },
            "vulnerability_categories": self.vulnerability_categories,
            "common_vulnerabilities": self.common_vulnerabilities,
            "logs": self.vulnerability_logs,
            "recommendations": [
                "定期进行代码审计，发现和修复安全漏洞",
                "使用自动化工具进行漏洞扫描",
                "对开发人员进行安全编码培训",
                "建立安全编码规范，指导开发人员编写安全的代码",
                "定期更新依赖项，修复已知的安全漏洞"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_common_vulnerabilities(self):
        """演示常见漏洞"""
        print("=== 常见漏洞演示 ===")
        print("==================")
        
        # 1. 显示常见漏洞分类
        print("\n1. 常见漏洞分类:")
        self.show_vulnerability_categories()
        
        # 2. 显示常见漏洞详情
        print("\n2. 常见漏洞详情:")
        self.show_common_vulnerabilities()
        
        # 3. 检测SQL注入漏洞
        print("\n3. 检测SQL注入漏洞:")
        self.detect_vulnerability("query = 'SELECT * FROM users WHERE id = ' + user_id", "SQL注入")
        self.detect_vulnerability("query = 'SELECT * FROM users WHERE id = ?'", "SQL注入")
        
        # 4. 检测XSS漏洞
        print("\n4. 检测XSS漏洞:")
        self.detect_vulnerability("echo $user_input", "XSS")
        self.detect_vulnerability("echo htmlspecialchars($user_input)", "XSS")
        
        # 5. 检测CSRF漏洞
        print("\n5. 检测CSRF漏洞:")
        self.detect_vulnerability('<form method="POST" action="/submit">', "CSRF")
        self.detect_vulnerability('<form method="POST" action="/submit"><input type="hidden" name="csrf_token" value="...">', "CSRF")
        
        # 6. 演示漏洞修复
        print("\n6. 演示漏洞修复:")
        self.demonstrate_vulnerability_fix("SQL注入")
        self.demonstrate_vulnerability_fix("XSS")
        self.demonstrate_vulnerability_fix("CSRF")
        
        # 7. 模拟漏洞扫描
        print("\n7. 模拟漏洞扫描:")
        self.simulate_vulnerability_scan()
        
        # 8. 显示漏洞日志
        print("\n8. 漏洞日志:")
        self.show_vulnerability_logs()
        
        # 9. 生成漏洞报告
        print("\n9. 生成漏洞报告:")
        self.generate_vulnerability_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了常见的安全漏洞及其修复方法。")
        print("及时发现和修复安全漏洞是保障代码安全的关键。")

if __name__ == "__main__":
    common_vulnerabilities_demo = CommonVulnerabilitiesDemo()
    common_vulnerabilities_demo.demonstrate_common_vulnerabilities()