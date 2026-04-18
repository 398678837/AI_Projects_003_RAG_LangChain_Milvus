#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
进程监控示例
演示如何使用Python进行进程监控、进程分析和进程行为检测
"""

import psutil
import time
import threading
from datetime import datetime


class ProcessMonitor:
    """进程监控器类"""
    
    def __init__(self):
        self.processes = {}
        self.monitoring = False
        self.lock = threading.Lock()
    
    def get_process_info(self, pid):
        """获取进程详细信息"""
        try:
            p = psutil.Process(pid)
            return {
                'pid': pid,
                'name': p.name(),
                'exe': p.exe(),
                'cmdline': p.cmdline(),
                'create_time': datetime.fromtimestamp(p.create_time()).strftime('%Y-%m-%d %H:%M:%S'),
                'status': p.status(),
                'username': p.username(),
                'cpu_percent': p.cpu_percent(interval=0.1),
                'memory_percent': p.memory_percent(),
                'memory_info': p.memory_info()._asdict(),
                'threads': p.num_threads(),
                'open_files': [f.path for f in p.open_files()],
                'connections': [conn._asdict() for conn in p.connections()]
            }
        except psutil.NoSuchProcess:
            return None
        except psutil.AccessDenied:
            return None
    
    def monitor_processes(self, interval=1):
        """监控所有进程"""
        self.monitoring = True
        
        while self.monitoring:
            with self.lock:
                current_pids = psutil.pids()
                
                # 新增进程
                for pid in current_pids:
                    if pid not in self.processes:
                        process_info = self.get_process_info(pid)
                        if process_info:
                            self.processes[pid] = process_info
                            print(f"[+] 进程创建: PID={pid}, Name={process_info['name']}")
                
                # 已终止进程
                for pid in list(self.processes.keys()):
                    if pid not in current_pids:
                        print(f"[-] 进程终止: PID={pid}, Name={self.processes[pid]['name']}")
                        del self.processes[pid]
            
            time.sleep(interval)
    
    def start_monitoring(self, interval=1):
        """启动监控线程"""
        thread = threading.Thread(target=self.monitor_processes, args=(interval,))
        thread.daemon = True
        thread.start()
    
    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False
    
    def find_suspicious_processes(self):
        """查找可疑进程"""
        suspicious = []
        
        with self.lock:
            for pid, process in self.processes.items():
                # 检测可疑进程名
                suspicious_names = ['cmd.exe', 'powershell.exe', 'regsvr32.exe', 'rundll32.exe']
                if process['name'].lower() in suspicious_names:
                    suspicious.append((pid, process, '可疑进程名'))
                
                # 检测命令行参数
                if process['cmdline']:
                    cmdline = ' '.join(process['cmdline'])
                    suspicious_args = ['/c', '/k', '-EncodedCommand', '-w', 'hidden']
                    if any(arg in cmdline for arg in suspicious_args):
                        suspicious.append((pid, process, '可疑命令行参数'))
                
                # 检测内存占用过高
                if process['memory_percent'] > 50:
                    suspicious.append((pid, process, '内存占用过高'))
                
                # 检测网络连接
                if len(process['connections']) > 10:
                    suspicious.append((pid, process, '网络连接过多'))
        
        return suspicious


def analyze_process_injection():
    """检测进程注入"""
    print("\n--- 进程注入分析 ---")
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # 检测可疑内存区域
            mem_info = proc.memory_info()
            if mem_info.rss > 100 * 1024 * 1024:  # 超过100MB
                print(f"进程 {proc.name()} (PID {proc.pid}) 内存占用: {mem_info.rss / 1024 / 1024:.2f} MB")
            
            # 检测线程数量异常
            if proc.num_threads() > 50:
                print(f"进程 {proc.name()} (PID {proc.pid}) 线程数量异常: {proc.num_threads()}")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


def main():
    """主函数"""
    print("=== 进程监控示例 ===")
    
    # 初始化监控器
    monitor = ProcessMonitor()
    
    # 启动监控
    print("\n[*] 启动进程监控...")
    monitor.start_monitoring(interval=1)
    
    # 运行5秒
    print("\n[*] 监控中... (按Ctrl+C停止)")
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    
    # 停止监控
    monitor.stop_monitoring()
    print("\n[*] 停止进程监控")
    
    # 显示监控结果
    print(f"\n[*] 监控到的进程数量: {len(monitor.processes)}")
    
    # 查找可疑进程
    suspicious = monitor.find_suspicious_processes()
    if suspicious:
        print("\n[!] 发现可疑进程:")
        for pid, process, reason in suspicious:
            print(f"  PID: {pid}, 名称: {process['name']}, 原因: {reason}")
    
    # 进程注入分析
    analyze_process_injection()


if __name__ == "__main__":
    main()
