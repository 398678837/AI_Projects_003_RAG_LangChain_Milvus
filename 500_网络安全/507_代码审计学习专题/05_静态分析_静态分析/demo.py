import os
import sys
import json
import re
import time
from datetime import datetime

class StaticAnalysisDemo:
    def __init__(self):
        # 静态分析技术
        self.static_analysis_techniques = {
            "词法分析": "分析源代码的词法结构，发现语法错误和潜在问题",
            "语法分析": "分析源代码的语法结构，发现语法错误和潜在问题",
            "语义分析": "分析源代码的语义，发现逻辑错误和潜在问题",
            "数据流分析": "分析数据在代码中的流动，发现数据处理错误和潜在问题",
            "控制流分析": "分析代码的控制流，发现逻辑错误和潜在问题",
            "类型检查": "检查代码的类型系统，发现类型错误和潜在问题",
            "复杂度分析": "分析代码的复杂度，发现复杂度过高的代码",
            "代码风格检查": "检查代码的风格，确保代码符合编码规范"
        }
        
        # 静态分析工具
        self.static_analysis_tools = {
            "SonarQube": {
                "描述": "开源的代码质量和安全分析平台",
                "支持的语言": ["Java", "C/C++", "C#", "Python", "JavaScript"],
                "特点": ["支持多种编程语言", "提供详细的代码质量报告", "集成到CI/CD流程"],
                "使用场景": "大型项目的代码质量和安全分析"
            },
            "Checkmarx": {
                "描述": "企业级静态代码分析工具",
                "支持的语言": ["Java", "C/C++", "C#", "Python", "JavaScript"],
                "特点": ["高精度的漏洞检测", "支持多种编程语言", "提供详细的修复建议"],
                "使用场景": "企业级应用的安全审计"
            },
            "Fortify": {
                "描述": "企业级应用安全测试平台",
                "支持的语言": ["Java", "C/C++", "C#", "Python", "JavaScript"],
                "特点": ["全面的漏洞检测", "支持多种编程语言", "提供详细的安全报告"],
                "使用场景": "企业级应用的安全审计"
            },
            "Pylint": {
                "描述": "Python代码分析工具",
                "支持的语言": ["Python"],
                "特点": ["检查代码风格", "发现代码错误", "提供代码质量报告"],
                "使用场景": "Python项目的代码质量分析"
            },
            "ESLint": {
                "描述": "JavaScript代码分析工具",
                "支持的语言": ["JavaScript", "TypeScript"],
                "特点": ["检查代码风格", "发现代码错误", "支持自定义规则"],
                "使用场景": "JavaScript项目的代码质量分析"
            },
            "CheckStyle": {
                "描述": "Java代码分析工具",
                "支持的语言": ["Java"],
                "特点": ["检查代码风格", "发现代码错误", "支持自定义规则"],
                "使用场景": "Java项目的代码质量分析"
            }
        }
        
        # 静态分析规则
        self.static_analysis_rules = {
            "代码风格": [
                "缩进使用4个空格",
                "行长度不超过100个字符",
                "变量名使用驼峰命名法",
                "函数名使用驼峰命名法",
                "类名使用帕斯卡命名法"
            ],
            "安全漏洞": [
                "避免SQL注入",
                "避免XSS攻击",
                "避免CSRF攻击",
                "避免敏感数据泄露",
                "避免认证绕过"
            ],
            "代码质量": [
                "避免重复代码",
                "避免复杂度过高的函数",
                "避免未使用的变量",
                "避免未使用的导入",
                "避免硬编码的常量"
            ]
        }
        
        # 静态分析日志
        self.static_analysis_logs = []
    
    def show_static_analysis_techniques(self):
        """显示静态分析技术"""
        print("\n--- 静态分析技术 ---")
        for technique, description in self.static_analysis_techniques.items():
            print(f"- {technique}: {description}")
        
        self.log_static_analysis_event("静态分析技术", "查看", "查看了静态分析技术")
    
    def show_static_analysis_tools(self):
        """显示静态分析工具"""
        print("\n--- 静态分析工具 ---")
        for tool, info in self.static_analysis_tools.items():
            print(f"\n{tool}:")
            print(f"  描述: {info['描述']}")
            print(f"  支持的语言: {', '.join(info['支持的语言'])}")
            print(f"  特点: {', '.join(info['特点'])}")
            print(f"  使用场景: {info['使用场景']}")
        
        self.log_static_analysis_event("静态分析工具", "查看", "查看了静态分析工具")
    
    def show_static_analysis_rules(self):
        """显示静态分析规则"""
        print("\n--- 静态分析规则 ---")
        for category, rules in self.static_analysis_rules.items():
            print(f"\n{category}:")
            for rule in rules:
                print(f"  - {rule}")
        
        self.log_static_analysis_event("静态分析规则", "查看", "查看了静态分析规则")
    
    def analyze_code_style(self, code):
        """分析代码风格"""
        print("\n--- 分析代码风格 ---")
        print(f"代码: {code}")
        
        issues = []
        
        # 检查缩进
        if '\t' in code:
            issues.append("使用了制表符缩进，应该使用空格")
        
        # 检查行长度
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if len(line) > 100:
                issues.append(f"第{i+1}行长度超过100个字符")
        
        # 检查变量名
        variable_pattern = r'\b[a-z_][a-z0-9_]*\b'
        variables = re.findall(variable_pattern, code)
        for var in variables:
            if '_' in var and any(c.isupper() for c in var):
                issues.append(f"变量名{var}使用了混合命名风格")
        
        if issues:
            print("发现的问题:")
            for issue in issues:
                print(f"  - {issue}")
            self.log_static_analysis_event("代码风格分析", "完成", f"发现了{len(issues)}个代码风格问题")
            return issues
        else:
            print("未发现代码风格问题")
            self.log_static_analysis_event("代码风格分析", "完成", "未发现代码风格问题")
            return []
    
    def analyze_security_vulnerabilities(self, code):
        """分析安全漏洞"""
        print("\n--- 分析安全漏洞 ---")
        print(f"代码: {code}")
        
        vulnerabilities = []
        
        # 检查SQL注入
        if re.search(r'\bSELECT.*FROM.*WHERE.*\b.*\$', code, re.IGNORECASE):
            if not re.search(r'\?|prepare|bind', code, re.IGNORECASE):
                vulnerabilities.append("可能存在SQL注入漏洞")
        
        # 检查XSS
        if re.search(r'echo.*\$|print.*\$|\bresponse\.write\(.*\$|\bdocument\.write\(.*\$', code, re.IGNORECASE):
            if not re.search(r'htmlspecialchars|escape|sanitize', code, re.IGNORECASE):
                vulnerabilities.append("可能存在XSS漏洞")
        
        # 检查敏感数据泄露
        if re.search(r'echo.*password.*\$|print.*password.*\$|echo.*secret.*\$|print.*secret.*\$', code, re.IGNORECASE):
            vulnerabilities.append("可能存在敏感数据泄露")
        
        if vulnerabilities:
            print("发现的安全漏洞:")
            for vuln in vulnerabilities:
                print(f"  - {vuln}")
            self.log_static_analysis_event("安全漏洞分析", "完成", f"发现了{len(vulnerabilities)}个安全漏洞")
            return vulnerabilities
        else:
            print("未发现安全漏洞")
            self.log_static_analysis_event("安全漏洞分析", "完成", "未发现安全漏洞")
            return []
    
    def analyze_code_quality(self, code):
        """分析代码质量"""
        print("\n--- 分析代码质量 ---")
        print(f"代码: {code}")
        
        issues = []
        
        # 检查未使用的变量
        if re.search(r'\b\w+\s*=\s*[^;]+;', code):
            # 简单的未使用变量检测
            variables = re.findall(r'\b(\w+)\s*=\s*[^;]+;', code)
            for var in variables:
                if code.count(var) == 1:
                    issues.append(f"变量{var}可能未使用")
        
        # 检查复杂度过高的函数
        if code.count('if') > 3 or code.count('for') > 3 or code.count('while') > 3:
            issues.append("函数复杂度可能过高")
        
        # 检查硬编码的常量
        if re.search(r'\b\d+\b', code):
            issues.append("可能存在硬编码的常量")
        
        if issues:
            print("发现的代码质量问题:")
            for issue in issues:
                print(f"  - {issue}")
            self.log_static_analysis_event("代码质量分析", "完成", f"发现了{len(issues)}个代码质量问题")
            return issues
        else:
            print("未发现代码质量问题")
            self.log_static_analysis_event("代码质量分析", "完成", "未发现代码质量问题")
            return []
    
    def simulate_static_analysis(self):
        """模拟静态分析过程"""
        print("\n--- 模拟静态分析过程 ---")
        
        # 1. 词法分析
        print("1. 词法分析:")
        print("   - 分析源代码的词法结构")
        print("   - 发现词法错误")
        time.sleep(1)
        
        # 2. 语法分析
        print("\n2. 语法分析:")
        print("   - 分析源代码的语法结构")
        print("   - 发现语法错误")
        time.sleep(1)
        
        # 3. 语义分析
        print("\n3. 语义分析:")
        print("   - 分析源代码的语义")
        print("   - 发现逻辑错误")
        time.sleep(1)
        
        # 4. 数据流分析
        print("\n4. 数据流分析:")
        print("   - 分析数据在代码中的流动")
        print("   - 发现数据处理错误")
        time.sleep(1)
        
        # 5. 控制流分析
        print("\n5. 控制流分析:")
        print("   - 分析代码的控制流")
        print("   - 发现逻辑错误")
        time.sleep(1)
        
        # 6. 生成分析报告
        print("\n6. 生成分析报告:")
        print("   - 汇总分析结果")
        print("   - 提供修复建议")
        time.sleep(1)
        
        print("\n静态分析过程模拟完成！")
        self.log_static_analysis_event("静态分析过程", "模拟", "完成了静态分析过程模拟")
    
    def log_static_analysis_event(self, activity, action, message):
        """记录静态分析事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "activity": activity,
            "action": action,
            "message": message
        }
        self.static_analysis_logs.append(log_entry)
    
    def show_static_analysis_logs(self):
        """显示静态分析日志"""
        print("\n--- 静态分析日志 ---")
        for log in self.static_analysis_logs:
            print(f"[{log['timestamp']}] {log['activity']} - {log['action']}: {log['message']}")
    
    def generate_static_analysis_report(self):
        """生成静态分析报告"""
        print("\n--- 生成静态分析报告 ---")
        
        report = {
            "report_info": {
                "title": "静态分析报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "StaticAnalysisDemo"
            },
            "static_analysis_techniques": self.static_analysis_techniques,
            "static_analysis_tools": self.static_analysis_tools,
            "static_analysis_rules": self.static_analysis_rules,
            "logs": self.static_analysis_logs,
            "recommendations": [
                "使用静态分析工具进行代码质量和安全分析",
                "将静态分析集成到CI/CD流程中",
                "定期进行静态分析，发现和修复问题",
                "对开发人员进行静态分析工具使用培训",
                "根据项目需求，配置合适的静态分析规则"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_static_analysis(self):
        """演示静态分析"""
        print("=== 静态分析演示 ===")
        print("==================")
        
        # 1. 显示静态分析技术
        print("\n1. 静态分析技术:")
        self.show_static_analysis_techniques()
        
        # 2. 显示静态分析工具
        print("\n2. 静态分析工具:")
        self.show_static_analysis_tools()
        
        # 3. 显示静态分析规则
        print("\n3. 静态分析规则:")
        self.show_static_analysis_rules()
        
        # 4. 分析代码风格
        print("\n4. 分析代码风格:")
        self.analyze_code_style("def bad_function():\n\tprint('Hello')\n    x=1\n    return x")
        
        # 5. 分析安全漏洞
        print("\n5. 分析安全漏洞:")
        self.analyze_security_vulnerabilities("query = 'SELECT * FROM users WHERE id = ' + user_id")
        
        # 6. 分析代码质量
        print("\n6. 分析代码质量:")
        self.analyze_code_quality("def complex_function():\n    x = 1\n    if x > 0:\n        for i in range(10):\n            if i % 2 == 0:\n                while i < 5:\n                    print(i)\n                    i += 1\n    return x")
        
        # 7. 模拟静态分析过程
        print("\n7. 模拟静态分析过程:")
        self.simulate_static_analysis()
        
        # 8. 显示静态分析日志
        print("\n8. 静态分析日志:")
        self.show_static_analysis_logs()
        
        # 9. 生成静态分析报告
        print("\n9. 生成静态分析报告:")
        self.generate_static_analysis_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了静态分析的技术、工具和方法。")
        print("静态分析是发现代码质量和安全问题的重要手段。")

if __name__ == "__main__":
    static_analysis_demo = StaticAnalysisDemo()
    static_analysis_demo.demonstrate_static_analysis()