#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网络监控示例
演示如何使用Python进行网络监控、网络分析和网络行为检测
"""

import socket
import time
import threading
import psutil
from scapy.all import sniff, IP, TCP, UDP, ICMP


class NetworkMonitor:
    """网络监控器"""
    
    def __init__(self):
        self.monitoring = False
        self.lock = threading.Lock()
        self.connections = []
        self.packets = []
    
    def get_network_connections(self):
        """获取网络连接"""
        connections = []
        for conn in psutil.net_connections(kind='inet'):
            connections.append({
                'fd': conn.fd,
                'family': conn.family,
                'type': conn.type,
                'laddr': conn.laddr,
                'raddr': conn.raddr,
                'status': conn.status,
                'pid': conn.pid
            })
        return connections
    
    def monitor_connections(self, interval=1):
        """监控网络连接"""
        self.monitoring = True
        
        while self.monitoring:
            with self.lock:
                current_connections = self.get_network_connections()
                
                # 新增连接
                for conn in current_connections:
                    if conn not in self.connections:
                        self.connections.append(conn)
                        print(f"[+] 网络连接建立: {conn['laddr']} -> {conn['raddr']} (PID: {conn['pid']})")
                
                # 已关闭连接
                for conn in list(self.connections):
                    if conn not in current_connections:
                        print(f"[-] 网络连接关闭: {conn['laddr']} -> {conn['raddr']} (PID: {conn['pid']})")
                        self.connections.remove(conn)
            
            time.sleep(interval)
    
    def packet_callback(self, packet):
        """数据包回调"""
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto = packet[IP].proto
            
            packet_info = {
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'proto': proto,
                'length': len(packet),
                'timestamp': time.time()
            }
            
            with self.lock:
                self.packets.append(packet_info)
            
            # 检测可疑IP
            suspicious_ips = ['192.168.1.100', '10.0.0.100']  # 示例可疑IP
            if src_ip in suspicious_ips or dst_ip in suspicious_ips:
                print(f"[!] 可疑IP连接: {src_ip} -> {dst_ip}")
            
            # 检测异常端口
            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                if dst_port in [22, 80, 443, 8080]:
                    print(f"[*] 常见端口连接: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
    
    def start_packet_sniffing(self):
        """启动数据包嗅探"""
        thread = threading.Thread(target=sniff, kwargs={'prn': self.packet_callback, 'store': 0})
        thread.daemon = True
        thread.start()
    
    def start_monitoring(self, interval=1):
        """启动监控"""
        thread = threading.Thread(target=self.monitor_connections, args=(interval,))
        thread.daemon = True
        thread.start()
        self.start_packet_sniffing()
    
    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False


def main():
    """主函数"""
    print("=== 网络监控示例 ===")
    
    # 初始化监控器
    monitor = NetworkMonitor()
    
    # 启动监控
    print("\n[*] 启动网络监控...")
    monitor.start_monitoring(interval=1)
    
    # 运行5秒
    print("\n[*] 监控中... (按Ctrl+C停止)")
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    
    # 停止监控
    monitor.stop_monitoring()
    print("\n[*] 停止网络监控")
    
    # 显示监控结果
    print(f"\n[*] 监控到的网络连接数量: {len(monitor.connections)}")
    print(f"[*] 监控到的数据包数量: {len(monitor.packets)}")


if __name__ == "__main__":
    main()
