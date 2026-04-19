import os
import sys
import json
import time
import psutil
from datetime import datetime
import subprocess
import threading

class BehaviorDetection:
    def __init__(self):
        # 行为规则
        self.behavior_rules = [
            {
                "name": "可疑文件操作",
                "conditions": [
                    "创建系统目录文件",
                    "修改系统文件",
                    "删除系统文件",
                    "创建可执行文件"
                ],
                "severity": "高"
            },
            {
                "name": "可疑网络行为",
                "conditions": [
                    "连接可疑IP地址",
                    "大量网络连接",
                    "异常网络流量",
                    "连接已知恶意域名"
                ],
                "severity": "高"
            },
            {
                "name": "可疑进程行为",
                "conditions": [
                    "创建大量子进程",
                    "注入其他进程",
                    "修改其他进程内存",
                    "异常进程权限"
                ],
                "severity": "高"
            },
            {
                "name": "可疑注册表操作",
                "conditions": [
                    "修改启动项",
                    "修改系统设置",
                    "删除安全设置",
                    "添加可疑服务"
                ],
                "severity": "高"
            },
            {
                "name": "可疑系统调用",
                "conditions": [
                    "调用敏感API",
                    "执行shell命令",
                    "访问敏感资源",
                    "修改系统时间"
                ],
                "severity": "中"
            }
        ]
        
        # 监控的进程
        self.monitored_processes = []
        
        # 行为日志
        self.behavior_logs = []
        
        # 监控状态
        self.running = False
    
    def monitor_process(self, process_id):
        """监控进程行为"""
        try:
            process = psutil.Process(process_id)
            process_name = process.name()
            print(f"开始监控进程: {process_name} (PID: {process_id})")
            
            # 监控进程的文件操作
            self.monitor_file_operations(process)
            
            # 监控进程的网络连接
            self.monitor_network_connections(process)
            
            # 监控进程的子进程
            self.monitor_child_processes(process)
            
            # 监控进程的系统调用
            self.monitor_system_calls(process)
            
        except Exception as e:
            print(f"监控进程失败: {str(e)}")
    
    def monitor_file_operations(self, process):
        """监控文件操作"""
        try:
            # 模拟文件操作监控
            print(f"监控 {process.name()} 的文件操作")
            
            # 这里可以使用更高级的文件监控库，如watchdog
            # 这里仅作演示
            file_operations = [
                "读取文件: C:\\Windows\\System32\\kernel32.dll",
                "写入文件: C:\\Temp\\test.exe",
                "创建文件: C:\\Users\\User\\AppData\\Roaming\\malware.exe"
            ]
            
            for operation in file_operations:
                log_entry = {
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "process": process.name(),
                    "pid": process.pid,
                    "operation": "文件操作",
                    "details": operation,
                    "severity": "中"
                }
                self.behavior_logs.append(log_entry)
                print(f"[文件操作] {operation}")
        except Exception as e:
            print(f"监控文件操作失败: {str(e)}")
    
    def monitor_network_connections(self, process):
        """监控网络连接"""
        try:
            print(f"监控 {process.name()} 的网络连接")
            
            # 获取进程的网络连接
            connections = process.connections(kind='inet')
            for conn in connections:
                log_entry = {
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "process": process.name(),
                    "pid": process.pid,
                    "operation": "网络连接",
                    "details": f"连接到: {conn.raddr[0]}:{conn.raddr[1]}",
                    "severity": "中"
                }
                self.behavior_logs.append(log_entry)
                print(f"[网络连接] 连接到: {conn.raddr[0]}:{conn.raddr[1]}")
        except Exception as e:
            print(f"监控网络连接失败: {str(e)}")
    
    def monitor_child_processes(self, process):
        """监控子进程"""
        try:
            print(f"监控 {process.name()} 的子进程")
            
            # 获取进程的子进程
            children = process.children(recursive=True)
            for child in children:
                log_entry = {
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "process": process.name(),
                    "pid": process.pid,
                    "operation": "创建子进程",
                    "details": f"创建子进程: {child.name()} (PID: {child.pid})",
                    "severity": "中"
                }
                self.behavior_logs.append(log_entry)
                print(f"[创建子进程] {child.name()} (PID: {child.pid})")
        except Exception as e:
            print(f"监控子进程失败: {str(e)}")
    
    def monitor_system_calls(self, process):
        """监控系统调用"""
        try:
            print(f"监控 {process.name()} 的系统调用")
            
            # 模拟系统调用监控
            system_calls = [
                "调用 CreateProcess",
                "调用 RegSetValueEx",
                "调用 InternetConnect",
                "调用 ShellExecute"
            ]
            
            for call in system_calls:
                log_entry = {
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "process": process.name(),
                    "pid": process.pid,
                    "operation": "系统调用",
                    "details": call,
                    "severity": "中"
                }
                self.behavior_logs.append(log_entry)
                print(f"[系统调用] {call}")
        except Exception as e:
            print(f"监控系统调用失败: {str(e)}")
    
    def analyze_behavior(self):
        """分析行为"""
        print("\n--- 分析行为 ---")
        
        # 分析行为日志
        suspicious_behaviors = []
        
        for log in self.behavior_logs:
            # 检查是否符合行为规则
            for rule in self.behavior_rules:
                for condition in rule["conditions"]:
                    if condition in log["details"]:
                        suspicious_behaviors.append({
                            "log": log,
                            "rule": rule
                        })
                        break
        
        if suspicious_behaviors:
            print("检测到以下可疑行为:")
            for behavior in suspicious_behaviors:
                log = behavior["log"]
                rule = behavior["rule"]
                print(f"  - {log['operation']}: {log['details']} (严重程度: {rule['severity']})")
        else:
            print("未检测到可疑行为")
        
        return suspicious_behaviors
    
    def generate_behavior_report(self):
        """生成行为检测报告"""
        print("\n--- 生成行为检测报告 ---")
        
        report = {
            "report_info": {
                "title": "行为检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "detector": "BehaviorDetection"
            },
            "monitor_summary": {
                "monitored_processes": len(self.monitored_processes),
                "behavior_logs": len(self.behavior_logs)
            },
            "suspicious_behaviors": self.analyze_behavior(),
            "behavior_rules": self.behavior_rules,
            "recommendations": [
                "加强对可疑进程的监控",
                "定期分析系统行为日志",
                "使用行为分析工具进行深度检测",
                "结合其他检测技术提高检测准确率"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def start_monitoring(self):
        """开始监控"""
        print("\n--- 开始监控 ---")
        self.running = True
        
        # 监控当前进程
        current_pid = os.getpid()
        self.monitored_processes.append(current_pid)
        self.monitor_process(current_pid)
        
        # 监控其他进程
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process.info['pid'] != current_pid and process.info['name'] not in ['System', 'Idle']:
                    self.monitored_processes.append(process.info['pid'])
                    # 启动线程监控进程
                    thread = threading.Thread(target=self.monitor_process, args=(process.info['pid'],))
                    thread.daemon = True
                    thread.start()
                    # 限制监控的进程数量
                    if len(self.monitored_processes) >= 5:
                        break
            except Exception:
                pass
        
        # 等待一段时间
        time.sleep(2)
        self.running = False
        print("\n监控结束")
    
    def demonstrate_behavior_detection(self):
        """演示行为检测"""
        print("=== 行为检测演示 ===")
        print("====================")
        
        # 1. 显示行为规则
        print("\n1. 行为规则:")
        for rule in self.behavior_rules:
            print(f"  - {rule['name']} (严重程度: {rule['severity']})")
            for condition in rule['conditions']:
                print(f"    - {condition}")
        
        # 2. 开始监控
        print("\n2. 开始监控进程行为:")
        self.start_monitoring()
        
        # 3. 分析行为
        print("\n3. 分析行为:")
        self.analyze_behavior()
        
        # 4. 生成行为检测报告
        print("\n4. 生成行为检测报告:")
        self.generate_behavior_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了行为检测的基本原理和实现方法。")
        print("行为检测可以检测未知恶意代码，但需要注意误报的问题。")

if __name__ == "__main__":
    behavior_detection = BehaviorDetection()
    behavior_detection.demonstrate_behavior_detection()