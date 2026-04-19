import os
import sys
import json
import time
import socket
import threading
from datetime import datetime
import scapy.all as scapy

class NetworkTrafficDetection:
    def __init__(self):
        # 网络流量规则
        self.traffic_rules = [
            {
                "name": "可疑IP地址",
                "conditions": [
                    "192.168.1.100",
                    "10.0.0.1",
                    "172.16.0.1"
                ],
                "severity": "高"
            },
            {
                "name": "可疑端口",
                "conditions": [
                    4444,  # Metasploit默认端口
                    3389,  # RDP端口
                    22,    # SSH端口
                    8080   # 常见代理端口
                ],
                "severity": "中"
            },
            {
                "name": "异常流量",
                "conditions": [
                    "大量DNS请求",
                    "大量HTTP请求",
                    "异常的数据包大小"
                ],
                "severity": "高"
            },
            {
                "name": "恶意流量模式",
                "conditions": [
                    "SQL注入攻击",
                    "XSS攻击",
                    "暴力破解"
                ],
                "severity": "高"
            }
        ]
        
        # 网络流量日志
        self.traffic_logs = []
        
        # 监控状态
        self.running = False
    
    def packet_handler(self, packet):
        """处理捕获的数据包"""
        try:
            # 提取数据包信息
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # 处理IP数据包
            if packet.haslayer(scapy.IP):
                ip_src = packet[scapy.IP].src
                ip_dst = packet[scapy.IP].dst
                protocol = packet[scapy.IP].proto
                
                # 处理TCP数据包
                if packet.haslayer(scapy.TCP):
                    sport = packet[scapy.TCP].sport
                    dport = packet[scapy.TCP].dport
                    
                    log_entry = {
                        "timestamp": timestamp,
                        "src_ip": ip_src,
                        "dst_ip": ip_dst,
                        "protocol": "TCP",
                        "src_port": sport,
                        "dst_port": dport,
                        "length": len(packet)
                    }
                    
                    self.traffic_logs.append(log_entry)
                    print(f"[TCP] {ip_src}:{sport} -> {ip_dst}:{dport} (长度: {len(packet)})")
                
                # 处理UDP数据包
                elif packet.haslayer(scapy.UDP):
                    sport = packet[scapy.UDP].sport
                    dport = packet[scapy.UDP].dport
                    
                    log_entry = {
                        "timestamp": timestamp,
                        "src_ip": ip_src,
                        "dst_ip": ip_dst,
                        "protocol": "UDP",
                        "src_port": sport,
                        "dst_port": dport,
                        "length": len(packet)
                    }
                    
                    self.traffic_logs.append(log_entry)
                    print(f"[UDP] {ip_src}:{sport} -> {ip_dst}:{dport} (长度: {len(packet)})")
                
                # 处理ICMP数据包
                elif packet.haslayer(scapy.ICMP):
                    log_entry = {
                        "timestamp": timestamp,
                        "src_ip": ip_src,
                        "dst_ip": ip_dst,
                        "protocol": "ICMP",
                        "length": len(packet)
                    }
                    
                    self.traffic_logs.append(log_entry)
                    print(f"[ICMP] {ip_src} -> {ip_dst} (长度: {len(packet)})")
        except Exception as e:
            print(f"处理数据包失败: {str(e)}")
    
    def start_sniffing(self, interface=None):
        """开始网络流量捕获"""
        print("\n--- 开始网络流量捕获 ---")
        self.running = True
        
        try:
            # 开始捕获数据包
            scapy.sniff(iface=interface, prn=self.packet_handler, store=False, stop_filter=lambda x: not self.running)
        except Exception as e:
            print(f"捕获数据包失败: {str(e)}")
    
    def analyze_traffic(self):
        """分析网络流量"""
        print("\n--- 分析网络流量 ---")
        
        # 分析流量日志
        suspicious_traffic = []
        
        for log in self.traffic_logs:
            # 检查可疑IP地址
            for rule in self.traffic_rules:
                if rule["name"] == "可疑IP地址":
                    for ip in rule["conditions"]:
                        if log.get("src_ip") == ip or log.get("dst_ip") == ip:
                            suspicious_traffic.append({
                                "log": log,
                                "rule": rule
                            })
                
                # 检查可疑端口
                elif rule["name"] == "可疑端口":
                    for port in rule["conditions"]:
                        if log.get("src_port") == port or log.get("dst_port") == port:
                            suspicious_traffic.append({
                                "log": log,
                                "rule": rule
                            })
                
                # 检查异常流量
                elif rule["name"] == "异常流量":
                    if log.get("length") > 10000:
                        suspicious_traffic.append({
                            "log": log,
                            "rule": rule
                        })
        
        if suspicious_traffic:
            print("检测到以下可疑流量:")
            for traffic in suspicious_traffic:
                log = traffic["log"]
                rule = traffic["rule"]
                print(f"  - {rule['name']}: {log['src_ip']}:{log.get('src_port', '-')} -> {log['dst_ip']}:{log.get('dst_port', '-')} (严重程度: {rule['severity']})")
        else:
            print("未检测到可疑流量")
        
        return suspicious_traffic
    
    def generate_traffic_report(self):
        """生成网络流量检测报告"""
        print("\n--- 生成网络流量检测报告 ---")
        
        # 统计流量信息
        protocol_stats = {}
        for log in self.traffic_logs:
            protocol = log["protocol"]
            if protocol not in protocol_stats:
                protocol_stats[protocol] = 0
            protocol_stats[protocol] += 1
        
        # 统计IP地址
        ip_stats = {}
        for log in self.traffic_logs:
            src_ip = log["src_ip"]
            if src_ip not in ip_stats:
                ip_stats[src_ip] = 0
            ip_stats[src_ip] += 1
        
        report = {
            "report_info": {
                "title": "网络流量检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "detector": "NetworkTrafficDetection"
            },
            "traffic_summary": {
                "total_packets": len(self.traffic_logs),
                "protocol_stats": protocol_stats,
                "top_ips": sorted(ip_stats.items(), key=lambda x: x[1], reverse=True)[:5]
            },
            "suspicious_traffic": self.analyze_traffic(),
            "traffic_rules": self.traffic_rules,
            "recommendations": [
                "定期监控网络流量",
                "设置流量阈值，及时发现异常流量",
                "使用防火墙过滤可疑IP和端口",
                "结合其他检测技术提高检测准确率"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def simulate_malicious_traffic(self):
        """模拟恶意流量"""
        print("\n--- 模拟恶意流量 ---")
        
        # 模拟TCP连接
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(("127.0.0.1", 8080))
            s.send(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
            s.close()
            print("模拟TCP连接成功")
        except Exception as e:
            print(f"模拟TCP连接失败: {str(e)}")
        
        # 模拟UDP数据包
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"Hello", ("127.0.0.1", 53))
            s.close()
            print("模拟UDP数据包成功")
        except Exception as e:
            print(f"模拟UDP数据包失败: {str(e)}")
    
    def demonstrate_network_detection(self):
        """演示网络流量检测"""
        print("=== 网络流量检测演示 ===")
        print("========================")
        
        # 1. 显示流量规则
        print("\n1. 网络流量规则:")
        for rule in self.traffic_rules:
            print(f"  - {rule['name']} (严重程度: {rule['severity']})")
            for condition in rule['conditions']:
                print(f"    - {condition}")
        
        # 2. 开始捕获流量
        print("\n2. 开始捕获网络流量:")
        print("捕获5秒的网络流量...")
        
        # 启动捕获线程
        sniff_thread = threading.Thread(target=self.start_sniffing)
        sniff_thread.daemon = True
        sniff_thread.start()
        
        # 模拟恶意流量
        self.simulate_malicious_traffic()
        
        # 等待5秒
        time.sleep(5)
        
        # 停止捕获
        self.running = False
        time.sleep(1)  # 等待线程结束
        
        # 3. 分析流量
        print("\n3. 分析网络流量:")
        self.analyze_traffic()
        
        # 4. 生成流量报告
        print("\n4. 生成网络流量检测报告:")
        self.generate_traffic_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了网络流量检测的基本原理和实现方法。")
        print("网络流量检测可以实时监控网络活动，及时发现可疑的网络行为。")

if __name__ == "__main__":
    network_detection = NetworkTrafficDetection()
    network_detection.demonstrate_network_detection()