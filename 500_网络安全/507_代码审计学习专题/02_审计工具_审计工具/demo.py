import os
import sys
import json
import time
from datetime import datetime

class CodeAuditToolsDemo:
    def __init__(self):
        # 代码审计工具分类
        self.tool_categories = {
            "静态代码分析工具": "不运行代码，通过分析源代码来发现安全漏洞",
            "动态代码分析工具": "在运行时测试代码，发现运行时的安全漏洞",
            "代码审查工具": "辅助手动代码审查的工具",
            "依赖项扫描工具": "扫描依赖项的安全漏洞",
            "安全配置检查工具": "检查系统和应用的安全配置"
        }
        
        # 常用的代码审计工具
        self.audit_tools = {
            "SonarQube": {
                "类型": "静态代码分析工具",
                "描述": "开源的代码质量和安全分析平台",
                "特点": ["支持多种编程语言", "提供详细的代码质量报告", "集成到CI/CD流程"],
                "使用场景": "大型项目的代码质量和安全分析"
            },
            "Checkmarx": {
                "类型": "静态代码分析工具",
                "描述": "企业级静态代码分析工具",
                "特点": ["高精度的漏洞检测", "支持多种编程语言", "提供详细的修复建议"],
                "使用场景": "企业级应用的安全审计"
            },
            "Fortify": {
                "类型": "静态代码分析工具",
                "描述": "企业级应用安全测试平台",
                "特点": ["全面的漏洞检测", "支持多种编程语言", "提供详细的安全报告"],
                "使用场景": "企业级应用的安全审计"
            },
            "OWASP ZAP": {
                "类型": "动态代码分析工具",
                "描述": "开源的Web应用安全扫描工具",
                "特点": ["自动扫描Web应用", "支持手动测试", "集成到CI/CD流程"],
                "使用场景": "Web应用的安全测试"
            },
            "Burp Suite": {
                "类型": "动态代码分析工具",
                "描述": "Web应用安全测试工具",
                "特点": ["强大的代理功能", "支持手动测试", "提供详细的安全报告"],
                "使用场景": "Web应用的安全测试"
            },
            "Pylint": {
                "类型": "静态代码分析工具",
                "描述": "Python代码分析工具",
                "特点": ["检查代码风格", "发现代码错误", "提供代码质量报告"],
                "使用场景": "Python项目的代码质量分析"
            },
            "ESLint": {
                "类型": "静态代码分析工具",
                "描述": "JavaScript代码分析工具",
                "特点": ["检查代码风格", "发现代码错误", "支持自定义规则"],
                "使用场景": "JavaScript项目的代码质量分析"
            },
            "OWASP Dependency Check": {
                "类型": "依赖项扫描工具",
                "描述": "依赖项安全漏洞扫描工具",
                "特点": ["扫描依赖项的安全漏洞", "支持多种构建系统", "提供详细的漏洞报告"],
                "使用场景": "项目依赖项的安全审计"
            }
        }
        
        # 工具使用示例
        self.tool_examples = {
            "SonarQube": "sonar-scanner -Dsonar.projectKey=myproject -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=token",
            "OWASP ZAP": "zap-cli quick-scan --self-contained --start-options '-config api.disablekey=true' https://example.com",
            "Pylint": "pylint mymodule.py",
            "ESLint": "eslint myfile.js",
            "OWASP Dependency Check": "dependency-check --project myproject --scan ."
        }
        
        # 审计工具日志
        self.tool_logs = []
    
    def show_tool_categories(self):
        """显示代码审计工具分类"""
        print("\n--- 代码审计工具分类 ---")
        for category, description in self.tool_categories.items():
            print(f"- {category}: {description}")
        
        self.log_tool_event("工具分类", "查看", "查看了代码审计工具分类")
    
    def show_audit_tools(self):
        """显示常用的代码审计工具"""
        print("\n--- 常用的代码审计工具 ---")
        for tool, info in self.audit_tools.items():
            print(f"\n{tool}:")
            print(f"  类型: {info['类型']}")
            print(f"  描述: {info['描述']}")
            print(f"  特点: {', '.join(info['特点'])}")
            print(f"  使用场景: {info['使用场景']}")
        
        self.log_tool_event("审计工具", "查看", "查看了常用的代码审计工具")
    
    def show_tool_examples(self):
        """显示工具使用示例"""
        print("\n--- 工具使用示例 ---")
        for tool, example in self.tool_examples.items():
            print(f"{tool}: {example}")
        
        self.log_tool_event("工具示例", "查看", "查看了工具使用示例")
    
    def simulate_tool_usage(self):
        """模拟工具使用"""
        print("\n--- 模拟工具使用 ---")
        
        # 1. 使用SonarQube进行静态分析
        print("1. 使用SonarQube进行静态分析:")
        print("   命令: sonar-scanner -Dsonar.projectKey=myproject -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=token")
        print("   结果: 发现了5个安全漏洞，3个代码质量问题")
        time.sleep(1)
        
        # 2. 使用OWASP ZAP进行动态分析
        print("\n2. 使用OWASP ZAP进行动态分析:")
        print("   命令: zap-cli quick-scan --self-contained --start-options '-config api.disablekey=true' https://example.com")
        print("   结果: 发现了2个XSS漏洞，1个CSRF漏洞")
        time.sleep(1)
        
        # 3. 使用Pylint进行Python代码分析
        print("\n3. 使用Pylint进行Python代码分析:")
        print("   命令: pylint mymodule.py")
        print("   结果: 发现了3个代码风格问题，1个潜在错误")
        time.sleep(1)
        
        # 4. 使用OWASP Dependency Check进行依赖项扫描
        print("\n4. 使用OWASP Dependency Check进行依赖项扫描:")
        print("   命令: dependency-check --project myproject --scan .")
        print("   结果: 发现了2个依赖项存在安全漏洞")
        time.sleep(1)
        
        print("\n工具使用模拟完成！")
        self.log_tool_event("工具使用", "模拟", "完成了工具使用模拟")
    
    def log_tool_event(self, activity, action, message):
        """记录工具事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "action": action,
            "message": message
        }
        self.tool_logs.append(log_entry)
    
    def show_tool_logs(self):
        """显示工具日志"""
        print("\n--- 工具日志 ---")
        for log in self.tool_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['action']}: {log['message']}")
    
    def generate_tool_report(self):
        """生成工具报告"""
        print("\n--- 生成工具报告 ---")
        
        report = {
            "report_info": {
                "title": "代码审计工具报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "CodeAuditToolsDemo"
            },
            "tool_categories": self.tool_categories,
            "audit_tools": self.audit_tools,
            "tool_examples": self.tool_examples,
            "logs": self.tool_logs,
            "recommendations": [
                "根据项目的需求选择合适的代码审计工具",
                "结合多种工具进行代码审计，提高审计效果",
                "将代码审计工具集成到CI/CD流程中",
                "定期更新代码审计工具，获取最新的漏洞规则",
                "对开发人员进行代码审计工具的培训"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_code_audit_tools(self):
        """演示代码审计工具"""
        print("=== 代码审计工具演示 ===")
        print("==================")
        
        # 1. 显示代码审计工具分类
        print("\n1. 代码审计工具分类:")
        self.show_tool_categories()
        
        # 2. 显示常用的代码审计工具
        print("\n2. 常用的代码审计工具:")
        self.show_audit_tools()
        
        # 3. 显示工具使用示例
        print("\n3. 工具使用示例:")
        self.show_tool_examples()
        
        # 4. 模拟工具使用
        print("\n4. 模拟工具使用:")
        self.simulate_tool_usage()
        
        # 5. 显示工具日志
        print("\n5. 工具日志:")
        self.show_tool_logs()
        
        # 6. 生成工具报告
        print("\n6. 生成工具报告:")
        self.generate_tool_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了常用的代码审计工具及其使用方法。")
        print("选择合适的代码审计工具是提高代码审计效率和效果的关键。")

if __name__ == "__main__":
    code_audit_tools_demo = CodeAuditToolsDemo()
    code_audit_tools_demo.demonstrate_code_audit_tools()