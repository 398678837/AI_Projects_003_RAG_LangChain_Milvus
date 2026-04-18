#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
内存分析示例
演示如何使用Python进行内存分析、内存取证和内存行为检测
"""

import psutil
import time
import threading
import os
from datetime import datetime


class MemoryAnalyzer:
    """内存分析器"""
    
    def __init__(self):
        self.processes = {}
        self.memory_snapshots = []
    
    def get_process_memory_info(self, pid):
        """获取进程内存信息"""
        try:
            p = psutil.Process(pid)
            mem_info = p.memory_info()
            return {
                'pid': pid,
                'name': p.name(),
                'exe': p.exe(),
                'memory_rss': mem_info.rss,
                'memory_vms': mem_info.vms,
                'memory_percent': p.memory_percent(),
                'threads': p.num_threads(),
                'open_files': [f.path for f in p.open_files()],
                'connections': [conn._asdict() for conn in p.connections()]
            }
        except psutil.NoSuchProcess:
            return None
        except psutil.AccessDenied:
            return None
    
    def analyze_process_memory(self):
        """分析进程内存"""
        print("\n--- 进程内存分析 ---")
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                mem_info = proc.info['memory_info']
                
                if mem_info and mem_info.rss > 100 * 1024 * 1024:  # 超过100MB
                    print(f"进程 {name} (PID {pid}) 内存占用: {mem_info.rss / 1024 / 1024:.2f} MB")
                    
                # 检测可疑进程
                if name.lower() in ['cmd.exe', 'powershell.exe', 'regsvr32.exe']:
                    print(f"可疑进程 {name} (PID {pid})")
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    def analyze_system_memory(self):
        """分析系统内存"""
        print("\n--- 系统内存分析 ---")
        
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        print(f"总内存: {mem.total / 1024 / 1024 / 1024:.2f} GB")
        print(f"可用内存: {mem.available / 1024 / 1024 / 1024:.2f} GB")
        print(f"已用内存: {mem.used / 1024 / 1024 / 1024:.2f} GB")
        print(f"内存使用率: {mem.percent}%")
        print(f"\n交换分区: {swap.total / 1024 / 1024 / 1024:.2f} GB")
        print(f"已用交换分区: {swap.used / 1024 / 1024 / 1024:.2f} GB")
        print(f"交换分区使用率: {swap.percent}%")
    
    def detect_memory_injection(self):
        """检测内存注入"""
        print("\n--- 内存注入检测 ---")
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                
                # 检测线程数量异常
                if proc.num_threads() > 50:
                    print(f"进程 {name} (PID {pid}) 线程数量异常: {proc.num_threads()}")
                
                # 检测内存占用异常
                mem_percent = proc.memory_percent()
                if mem_percent > 50:
                    print(f"进程 {name} (PID {pid}) 内存占用异常: {mem_percent}%")
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    def create_memory_snapshot(self):
        """创建内存快照"""
        snapshot = {
            'timestamp': time.time(),
            'system_memory': psutil.virtual_memory()._asdict(),
            'swap_memory': psutil.swap_memory()._asdict(),
            'processes': []
        }
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                mem_info = proc.info['memory_info']
                
                if mem_info:
                    snapshot['processes'].append({
                        'pid': pid,
                        'name': name,
                        'memory_rss': mem_info.rss,
                        'memory_vms': mem_info.vms
                    })
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        self.memory_snapshots.append(snapshot)
        print(f"\n[+] 内存快照已创建 (ID: {len(self.memory_snapshots)})")


def main():
    """主函数"""
    print("=== 内存分析示例 ===")
    
    # 初始化分析器
    analyzer = MemoryAnalyzer()
    
    # 分析系统内存
    analyzer.analyze_system_memory()
    
    # 分析进程内存
    analyzer.analyze_process_memory()
    
    # 检测内存注入
    analyzer.detect_memory_injection()
    
    # 创建内存快照
    analyzer.create_memory_snapshot()


if __name__ == "__main__":
    main()
