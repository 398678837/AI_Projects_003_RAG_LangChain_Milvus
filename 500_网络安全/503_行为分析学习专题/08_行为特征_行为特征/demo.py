#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行为特征示例
演示如何使用Python进行行为特征提取、行为特征分析和行为特征检测
"""

import os
import time
import hashlib
import psutil
from collections import defaultdict


class BehaviorFeatureExtractor:
    """行为特征提取器"""
    
    def __init__(self):
        self.features = defaultdict(list)
    
    def extract_file_features(self, file_path):
        """提取文件特征"""
        features = {}
        
        try:
            # 文件基本信息
            stat = os.stat(file_path)
            features['size'] = stat.st_size
            features['create_time'] = stat.st_ctime
            features['modify_time'] = stat.st_mtime
            features['access_time'] = stat.st_atime
            
            # 文件Hash
            with open(file_path, 'rb') as f:
                data = f.read()
                features['md5'] = hashlib.md5(data).hexdigest()
                features['sha1'] = hashlib.sha1(data).hexdigest()
                features['sha256'] = hashlib.sha256(data).hexdigest()
            
            # 文件类型
            ext = os.path.splitext(file_path)[1].lower()
            features['extension'] = ext
            
            return features
            
        except Exception as e:
            print(f"提取文件特征失败: {e}")
            return None
    
    def extract_process_features(self, pid):
        """提取进程特征"""
        features = {}
        
        try:
            p = psutil.Process(pid)
            
            # 进程基本信息
            features['pid'] = pid
            features['name'] = p.name()
            features['exe'] = p.exe()
            features['cmdline'] = ' '.join(p.cmdline())
            features['create_time'] = p.create_time()
            features['status'] = p.status()
            features['username'] = p.username()
            
            # 资源使用
            features['cpu_percent'] = p.cpu_percent(interval=0.1)
            features['memory_percent'] = p.memory_percent()
            features['memory_rss'] = p.memory_info().rss
            features['memory_vms'] = p.memory_info().vms
            
            # 线程和连接
            features['threads'] = p.num_threads()
            features['open_files'] = len(p.open_files())
            features['connections'] = len(p.connections())
            
            return features
            
        except psutil.NoSuchProcess:
            print(f"进程 {pid} 不存在")
            return None
        except psutil.AccessDenied:
            print(f"访问进程 {pid} 被拒绝")
            return None
    
    def extract_network_features(self):
        """提取网络特征"""
        features = {}
        
        # 网络连接
        connections = []
        for conn in psutil.net_connections(kind='inet'):
            connections.append({
                'laddr': f"{conn.laddr.ip}:{conn.laddr.port}",
                'raddr': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None,
                'status': conn.status,
                'pid': conn.pid
            })
        features['connections'] = connections
        
        # 网络接口
        interfaces = []
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                interfaces.append({
                    'interface': iface,
                    'address': addr.address,
                    'netmask': addr.netmask,
                    'broadcast': addr.broadcast
                })
        features['interfaces'] = interfaces
        
        # 网络统计
        stats = psutil.net_io_counters()
        features['bytes_sent'] = stats.bytes_sent
        features['bytes_recv'] = stats.bytes_recv
        features['packets_sent'] = stats.packets_sent
        features['packets_recv'] = stats.packets_recv
        
        return features


class BehaviorFeatureAnalyzer:
    """行为特征分析器"""
    
    def __init__(self):
        self.extractor = BehaviorFeatureExtractor()
    
    def analyze_malicious_process(self, pid):
        """分析恶意进程"""
        features = self.extractor.extract_process_features(pid)
        if not features:
            return None
        
        analysis = {
            'pid': pid,
            'name': features['name'],
            'suspicious': False,
            'reasons': []
        }
        
        # 检测可疑进程名
        suspicious_names = ['cmd.exe', 'powershell.exe', 'regsvr32.exe', 'rundll32.exe', 'wscript.exe']
        if features['name'].lower() in suspicious_names:
            analysis['suspicious'] = True
            analysis['reasons'].append(f"可疑进程名: {features['name']}")
        
        # 检测命令行参数
        if 'cmdline' in features:
            cmdline = features['cmdline'].lower()
            suspicious_args = ['/c', '/k', '-encodedcommand', '-w', 'hidden', 'rundll32']
            if any(arg in cmdline for arg in suspicious_args):
                analysis['suspicious'] = True
                analysis['reasons'].append(f"可疑命令行参数: {cmdline}")
        
        # 检测内存占用
        if features['memory_percent'] > 50:
            analysis['suspicious'] = True
            analysis['reasons'].append(f"内存占用过高: {features['memory_percent']}%")
        
        # 检测网络连接
        if features['connections'] > 10:
            analysis['suspicious'] = True
            analysis['reasons'].append(f"网络连接过多: {features['connections']}")
        
        return analysis


def main():
    """主函数"""
    print("=== 行为特征示例 ===")
    
    # 初始化提取器和分析器
    extractor = BehaviorFeatureExtractor()
    analyzer = BehaviorFeatureAnalyzer()
    
    # 提取进程特征
    print("\n--- 提取进程特征 ---")
    pid = os.getpid()
    process_features = extractor.extract_process_features(pid)
    if process_features:
        print(f"PID: {process_features['pid']}")
        print(f"进程名: {process_features['name']}")
        print(f"CPU使用率: {process_features['cpu_percent']}%")
        print(f"内存使用率: {process_features['memory_percent']}%")
    
    # 分析恶意进程
    print("\n--- 分析恶意进程 ---")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            
            # 只分析前10个进程
            if pid > 10:
                break
            
            analysis = analyzer.analyze_malicious_process(pid)
            if analysis:
                print(f"PID: {analysis['pid']}, 进程名: {analysis['name']}, 可疑: {analysis['suspicious']}")
                if analysis['reasons']:
                    for reason in analysis['reasons']:
                        print(f"  原因: {reason}")
                        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


if __name__ == "__main__":
    main()
