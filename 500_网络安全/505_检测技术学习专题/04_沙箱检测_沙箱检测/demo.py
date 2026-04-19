import os
import sys
import json
import time
import subprocess
import tempfile
from datetime import datetime

class SandboxDetection:
    def __init__(self):
        # 沙箱配置
        self.sandbox_config = {
            "isolation_level": "medium",
            "network_access": False,
            "file_system_access": "limited",
            "registry_access": "limited",
            "process_creation": "allowed",
            "time_limit": 60,  # 60秒
            "memory_limit": 1024  # 1024MB
        }
        
        # 行为监控点
        self.monitoring_points = [
            "file_operations",
            "network_connections",
            "process_creation",
            "registry_operations",
            "system_calls"
        ]
        
        # 沙箱分析结果
        self.analysis_results = {
            "file_operations": [],
            "network_connections": [],
            "process_creation": [],
            "registry_operations": [],
            "system_calls": []
        }
    
    def create_sandbox(self):
        """创建沙箱环境"""
        print("\n--- 创建沙箱环境 ---")
        
        # 创建临时目录作为沙箱
        sandbox_dir = tempfile.mkdtemp(prefix="sandbox_")
        print(f"创建沙箱目录: {sandbox_dir}")
        
        # 配置沙箱环境
        print("配置沙箱环境...")
        print(f"隔离级别: {self.sandbox_config['isolation_level']}")
        print(f"网络访问: {self.sandbox_config['network_access']}")
        print(f"文件系统访问: {self.sandbox_config['file_system_access']}")
        print(f"注册表访问: {self.sandbox_config['registry_access']}")
        print(f"进程创建: {self.sandbox_config['process_creation']}")
        print(f"时间限制: {self.sandbox_config['time_limit']}秒")
        print(f"内存限制: {self.sandbox_config['memory_limit']}MB")
        
        return sandbox_dir
    
    def monitor_file_operations(self, process_name):
        """监控文件操作"""
        print(f"\n--- 监控 {process_name} 的文件操作 ---")
        
        # 模拟文件操作监控
        file_operations = [
            {"action": "创建", "path": "C:\\sandbox\\test.txt", "size": 1024},
            {"action": "写入", "path": "C:\\sandbox\\test.txt", "size": 512},
            {"action": "读取", "path": "C:\\sandbox\\test.txt"},
            {"action": "删除", "path": "C:\\sandbox\\test.txt"}
        ]
        
        for operation in file_operations:
            self.analysis_results["file_operations"].append({
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "process": process_name,
                "action": operation["action"],
                "path": operation["path"],
                "size": operation.get("size", 0)
            })
            print(f"{operation['action']}文件: {operation['path']}")
    
    def monitor_network_connections(self, process_name):
        """监控网络连接"""
        print(f"\n--- 监控 {process_name} 的网络连接 ---")
        
        # 模拟网络连接监控
        network_connections = [
            {"action": "连接", "address": "192.168.1.1", "port": 80},
            {"action": "发送", "address": "192.168.1.1", "port": 80, "size": 1024},
            {"action": "接收", "address": "192.168.1.1", "port": 80, "size": 2048}
        ]
        
        for connection in network_connections:
            self.analysis_results["network_connections"].append({
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "process": process_name,
                "action": connection["action"],
                "address": connection["address"],
                "port": connection["port"],
                "size": connection.get("size", 0)
            })
            print(f"{connection['action']}: {connection['address']}:{connection['port']}")
    
    def monitor_process_creation(self, process_name):
        """监控进程创建"""
        print(f"\n--- 监控 {process_name} 的进程创建 ---")
        
        # 模拟进程创建监控
        process_creation = [
            {"action": "创建", "name": "child_process.exe", "pid": 1234},
            {"action": "退出", "name": "child_process.exe", "pid": 1234}
        ]
        
        for process in process_creation:
            self.analysis_results["process_creation"].append({
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "process": process_name,
                "action": process["action"],
                "name": process["name"],
                "pid": process["pid"]
            })
            print(f"{process['action']}进程: {process['name']} (PID: {process['pid']})")
    
    def monitor_registry_operations(self, process_name):
        """监控注册表操作"""
        print(f"\n--- 监控 {process_name} 的注册表操作 ---")
        
        # 模拟注册表操作监控
        registry_operations = [
            {"action": "读取", "key": "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows"},
            {"action": "写入", "key": "HKEY_CURRENT_USER\\Software\\Test", "value": "test"}
        ]
        
        for operation in registry_operations:
            self.analysis_results["registry_operations"].append({
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "process": process_name,
                "action": operation["action"],
                "key": operation["key"],
                "value": operation.get("value", "")
            })
            print(f"{operation['action']}注册表: {operation['key']}")
    
    def monitor_system_calls(self, process_name):
        """监控系统调用"""
        print(f"\n--- 监控 {process_name} 的系统调用 ---")
        
        # 模拟系统调用监控
        system_calls = [
            {"action": "调用", "name": "CreateFile", "arguments": "test.txt"},
            {"action": "调用", "name": "InternetConnect", "arguments": "192.168.1.1"},
            {"action": "调用", "name": "CreateProcess", "arguments": "child_process.exe"}
        ]
        
        for call in system_calls:
            self.analysis_results["system_calls"].append({
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "process": process_name,
                "action": call["action"],
                "name": call["name"],
                "arguments": call["arguments"]
            })
            print(f"{call['action']}系统调用: {call['name']} ({call['arguments']})")
    
    def analyze_behavior(self):
        """分析沙箱中的行为"""
        print("\n--- 分析沙箱中的行为 ---")
        
        # 分析行为
        suspicious_behaviors = []
        
        # 检查文件操作
        for operation in self.analysis_results["file_operations"]:
            if operation["path"].startswith("C:\\Windows") or operation["path"].startswith("C:\\System32"):
                suspicious_behaviors.append({
                    "type": "文件操作",
                    "details": f"修改系统文件: {operation['path']}",
                    "severity": "高"
                })
        
        # 检查网络连接
        for connection in self.analysis_results["network_connections"]:
            if connection["address"] in ["10.0.0.1", "192.168.1.1"]:  # 模拟可疑IP
                suspicious_behaviors.append({
                    "type": "网络连接",
                    "details": f"连接可疑IP: {connection['address']}",
                    "severity": "中"
                })
        
        # 检查进程创建
        for process in self.analysis_results["process_creation"]:
            if "cmd.exe" in process["name"] or "powershell.exe" in process["name"]:
                suspicious_behaviors.append({
                    "type": "进程创建",
                    "details": f"创建命令行进程: {process['name']}",
                    "severity": "中"
                })
        
        # 检查注册表操作
        for operation in self.analysis_results["registry_operations"]:
            if "Run" in operation["key"] or "Startup" in operation["key"]:
                suspicious_behaviors.append({
                    "type": "注册表操作",
                    "details": f"修改启动项: {operation['key']}",
                    "severity": "高"
                })
        
        # 检查系统调用
        for call in self.analysis_results["system_calls"]:
            if call["name"] in ["CreateProcess", "InternetConnect"]:
                suspicious_behaviors.append({
                    "type": "系统调用",
                    "details": f"调用敏感API: {call['name']}",
                    "severity": "中"
                })
        
        if suspicious_behaviors:
            print("检测到以下可疑行为:")
            for behavior in suspicious_behaviors:
                print(f"  - {behavior['type']}: {behavior['details']} (严重程度: {behavior['severity']})")
        else:
            print("未检测到可疑行为")
        
        return suspicious_behaviors
    
    def generate_sandbox_report(self):
        """生成沙箱检测报告"""
        print("\n--- 生成沙箱检测报告 ---")
        
        report = {
            "report_info": {
                "title": "沙箱检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "detector": "SandboxDetection"
            },
            "sandbox_config": self.sandbox_config,
            "analysis_results": self.analysis_results,
            "suspicious_behaviors": self.analyze_behavior(),
            "recommendations": [
                "定期使用沙箱分析可疑文件",
                "结合其他检测技术提高检测准确率",
                "持续更新沙箱检测规则",
                "建立沙箱分析结果数据库"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def run_in_sandbox(self, file_path):
        """在沙箱中运行文件"""
        print(f"\n--- 在沙箱中运行文件: {file_path} ---")
        
        # 创建沙箱
        sandbox_dir = self.create_sandbox()
        
        try:
            # 模拟在沙箱中运行文件
            print(f"在沙箱中运行文件: {file_path}")
            
            # 监控文件行为
            self.monitor_file_operations(os.path.basename(file_path))
            self.monitor_network_connections(os.path.basename(file_path))
            self.monitor_process_creation(os.path.basename(file_path))
            self.monitor_registry_operations(os.path.basename(file_path))
            self.monitor_system_calls(os.path.basename(file_path))
            
            # 等待一段时间
            print("\n等待文件执行...")
            time.sleep(2)
            
            # 分析行为
            self.analyze_behavior()
            
            # 生成报告
            self.generate_sandbox_report()
            
        finally:
            # 清理沙箱
            if os.path.exists(sandbox_dir):
                import shutil
                shutil.rmtree(sandbox_dir)
                print(f"\n清理沙箱目录: {sandbox_dir}")
    
    def demonstrate_sandbox_detection(self):
        """演示沙箱检测"""
        print("=== 沙箱检测演示 ===")
        print("====================")
        
        # 1. 显示沙箱配置
        print("\n1. 沙箱配置:")
        for key, value in self.sandbox_config.items():
            print(f"  - {key}: {value}")
        
        # 2. 显示监控点
        print("\n2. 监控点:")
        for point in self.monitoring_points:
            print(f"  - {point}")
        
        # 3. 创建测试文件
        print("\n3. 创建测试文件:")
        test_file = "test_file.exe"
        with open(test_file, 'w') as f:
            f.write("This is a test file.")
        print(f"创建测试文件: {test_file}")
        
        # 4. 在沙箱中运行测试文件
        print("\n4. 在沙箱中运行测试文件:")
        self.run_in_sandbox(test_file)
        
        # 5. 清理测试文件
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"\n清理测试文件: {test_file}")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了沙箱检测的基本原理和实现方法。")
        print("沙箱检测可以安全地分析程序的行为，是检测未知恶意代码的重要手段。")

if __name__ == "__main__":
    sandbox_detection = SandboxDetection()
    sandbox_detection.demonstrate_sandbox_detection()