#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行为分析基础概念示例
演示行为分析的基本概念、目的、流程、工具和应用
"""

import os
import time
import psutil
from datetime import datetime

class BehaviorAnalysisBasics:
    """行为分析基础概念类"""
    
    def __init__(self):
        """初始化行为分析基础示例"""
        print("=== 行为分析基础概念示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def behavior_analysis_overview(self):
        """行为分析概述"""
        print("\n--- 1. 行为分析概述 ---")
        
        print("行为分析定义:")
        print("  - 分析程序运行时的行为")
        print("  - 监控系统状态变化")
        print("  - 识别恶意活动")
        
        print("\n行为分析目的:")
        print("  - 检测恶意代码")
        print("  - 发现异常行为")
        print("  - 分析攻击路径")
        
        print("\n行为分析历史:")
        print("  - 早期: 人工分析")
        print("  - 中期: 自动化工具")
        print("  - 现代: AI驱动")
        
        print("\n行为分析应用:")
        print("  - 恶意代码分析")
        print("  - 威胁狩猎")
        print("  - 安全运营")
    
    def behavior_analysis_purpose(self):
        """行为分析目的"""
        print("\n--- 2. 行为分析目的 ---")
        
        print("恶意代码检测:")
        print("  - 基于行为的检测")
        print("  - 未知恶意代码检测")
        print("  - 零日漏洞利用检测")
        
        print("\n威胁狩猎:")
        print("  - 主动发现威胁")
        print("  - 内部威胁检测")
        print("  - 高级威胁检测")
        
        print("\n异常检测:")
        print("  - 基线建立")
        print("  - 异常识别")
        print("  - 告警处理")
        
        print("\n行为画像:")
        print("  - 用户行为画像")
        print("  - 程序行为画像")
        print("  - 攻击行为画像")
    
    def behavior_analysis_process(self):
        """行为分析流程"""
        print("\n--- 3. 行为分析流程 ---")
        
        print("环境准备:")
        print("  - 沙箱环境")
        print("  - 监控工具")
        print("  - 日志收集")
        
        print("\n样本运行:")
        print("  - 样本执行")
        print("  - 行为记录")
        print("  - 数据收集")
        
        print("\n行为监控:")
        print("  - 进程监控")
        print("  - 文件监控")
        print("  - 网络监控")
        
        print("\n数据分析:")
        print("  - 行为特征提取")
        print("  - 异常检测")
        print("  - 威胁识别")
        
        print("\n报告编写:")
        print("  - 行为描述")
        print("  - 技术分析")
        print("  - 防御建议")
    
    def behavior_analysis_tools(self):
        """行为分析工具"""
        print("\n--- 4. 行为分析工具 ---")
        
        print("沙箱工具:")
        print("  - Cuckoo Sandbox")
        print("  - Joe Sandbox")
        print("  - Any.Run")
        
        print("\n监控工具:")
        print("  - Process Monitor")
        print("  - Process Explorer")
        print("  - Wireshark")
        
        print("\n分析工具:")
        print("  - Volatility")
        print("  - Rekall")
        print("  - Redline")
        
        print("\n可视化工具:")
        print("  - Graphviz")
        print("  - Gephi")
        print("  - Maltego")
    
    def behavior_analysis_applications(self):
        """行为分析应用"""
        print("\n--- 5. 行为分析应用 ---")
        
        print("安全运营:")
        print("  - 安全监控")
        print("  - 告警分析")
        print("  - 事件响应")
        
        print("\n威胁情报:")
        print("  - IOC提取")
        print("  - 威胁狩猎")
        print("  - 情报共享")
        
        print("\n应急响应:")
        print("  - 事件调查")
        print("  - 取证分析")
        print("  - 恢复重建")
        
        print("\n取证分析:")
        print("  - 内存取证")
        print("  - 磁盘取证")
        print("  - 网络取证")
    
    def simple_process_monitor(self, duration=5):
        """简单的进程监控示例"""
        print("\n--- 6. 简单进程监控示例 ---")
        print(f"监控进程 {duration} 秒...")
        
        processes = {}
        start_time = time.time()
        
        while time.time() - start_time < duration:
            for proc in psutil.process_iter(['pid', 'name', 'ppid']):
                try:
                    proc_info = proc.info
                    pid = proc_info['pid']
                    if pid not in processes:
                        processes[pid] = {
                            'name': proc_info['name'],
                            'ppid': proc_info['ppid'],
                            'start_time': datetime.now().strftime('%H:%M:%S')
                        }
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            time.sleep(1)
        
        print(f"\n监控到 {len(processes)} 个进程:")
        for pid, info in list(processes.items())[:10]:  # 只显示前10个进程
            print(f"  PID: {pid}, Name: {info['name']}, PPID: {info['ppid']}, Start: {info['start_time']}")
        
        if len(processes) > 10:
            print(f"  ... 还有 {len(processes) - 10} 个进程未显示")
    
    def file_operation_monitor(self):
        """文件操作监控示例"""
        print("\n--- 7. 文件操作监控示例 ---")
        
        test_file = "test_behavior_analysis.txt"
        
        print(f"创建测试文件: {test_file}")
        with open(test_file, 'w') as f:
            f.write("Behavior analysis test file")
        
        print(f"读取测试文件")
        with open(test_file, 'r') as f:
            content = f.read()
            print(f"  文件内容: {content}")
        
        print(f"修改测试文件")
        with open(test_file, 'a') as f:
            f.write("\nModified content")
        
        print(f"删除测试文件")
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"  文件已删除: {test_file}")
        
        print("文件操作监控完成")
    
    def behavior_baseline_demo(self):
        """行为基线演示"""
        print("\n--- 8. 行为基线演示 ---")
        
        print("建立系统行为基线:")
        print("  1. 收集正常系统行为数据")
        print("  2. 分析行为模式")
        print("  3. 建立基线模型")
        print("  4. 检测异常行为")
        
        # 模拟基线数据
        baseline_cpu = 10.0  # 正常CPU使用率
        baseline_memory = 30.0  # 正常内存使用率
        
        print(f"\n模拟系统行为基线:")
        print(f"  正常CPU使用率: {baseline_cpu}%")
        print(f"  正常内存使用率: {baseline_memory}%")
        
        # 模拟当前系统状态
        current_cpu = psutil.cpu_percent(interval=1)
        current_memory = psutil.virtual_memory().percent
        
        print(f"\n当前系统状态:")
        print(f"  当前CPU使用率: {current_cpu}%")
        print(f"  当前内存使用率: {current_memory}%")
        
        # 检测异常
        if current_cpu > baseline_cpu * 2:
            print("  警告: CPU使用率异常")
        if current_memory > baseline_memory * 2:
            print("  警告: 内存使用率异常")
        
        print("行为基线演示完成")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.behavior_analysis_overview()
            self.behavior_analysis_purpose()
            self.behavior_analysis_process()
            self.behavior_analysis_tools()
            self.behavior_analysis_applications()
            self.simple_process_monitor()
            self.file_operation_monitor()
            self.behavior_baseline_demo()
            
            print("\n" + "=" * 80)
            print("行为分析基础概念示例演示完成！")
            print("通过本演示，您了解了行为分析的基本概念、目的、流程、工具和应用。")
            print("行为分析是网络安全领域的重要技术，通过监控和分析系统、应用程序和网络的行为，识别潜在的安全威胁。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = BehaviorAnalysisBasics()
    demo.run_demo()
