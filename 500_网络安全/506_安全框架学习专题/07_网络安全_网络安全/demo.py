import os
import sys
import json
import time
import re
from datetime import datetime

class NetworkSecurityDemo:
    def __init__(self):
        # 网络安全漏洞类型
        self.vulnerabilities = {
            "DDoS攻击": "分布式拒绝服务攻击",
            "ARP欺骗": "地址解析协议欺骗",
            "DNS劫持": "域名系统劫持",
            "中间人攻击": "中间人攻击",
            "端口扫描": "端口扫描攻击",
            "网络嗅探": "网络数据包嗅探",
            "SQL注入": "SQL注入攻击",
            "XSS攻击": "跨站脚本攻击"
        }
        
        # 网络安全防护措施
        self.security_measures = {
            "防火墙": "使用防火墙过滤网络流量",
            "入侵检测系统": "使用入侵检测系统检测攻击",
            "入侵防御系统": "使用入侵防御系统防止攻击",
            "VPN": "使用虚拟专用网络加密通信",
            "SSL/TLS": "使用SSL/TLS加密传输",
            "网络分段": "将网络分为不同的网段",
            "访问控制": "实施网络访问控制",
            "安全监控": "监控网络安全状态"
        }
        
        # 网络安全日志
        self.security_logs = []
    
    def detect_ddos_attack(self, traffic_data):
        """检测DDoS攻击"""
        print("\n--- 检测DDoS攻击 ---")
        print(f"流量数据: {traffic_data}")
        
        # DDoS攻击特征
        if traffic_data.get("request_rate", 0) > 1000:
            print("检测到DDoS攻击")
            self.log_security_event("DDoS攻击", "检测", True, f"检测到DDoS攻击，请求速率: {traffic_data['request_rate']}")
            return True
        else:
            print("未检测到DDoS攻击")
            self.log_security_event("DDoS攻击", "检测", False, "未检测到DDoS攻击")
            return False
    
    def detect_arp_spoofing(self, arp_data):
        """检测ARP欺骗"""
        print("\n--- 检测ARP欺骗 ---")
        print(f"ARP数据: {arp_data}")
        
        # ARP欺骗特征
        if arp_data.get("duplicate_ips", False):
            print("检测到ARP欺骗")
            self.log_security_event("ARP欺骗", "检测", True, "检测到ARP欺骗")
            return True
        else:
            print("未检测到ARP欺骗")
            self.log_security_event("ARP欺骗", "检测", False, "未检测到ARP欺骗")
            return False
    
    def detect_dns_hijacking(self, dns_data):
        """检测DNS劫持"""
        print("\n--- 检测DNS劫持 ---")
        print(f"DNS数据: {dns_data}")
        
        # DNS劫持特征
        if dns_data.get("unauthorized_servers", True):
            print("检测到DNS劫持")
            self.log_security_event("DNS劫持", "检测", True, "检测到DNS劫持")
            return True
        else:
            print("未检测到DNS劫持")
            self.log_security_event("DNS劫持", "检测", False, "未检测到DNS劫持")
            return False
    
    def detect_port_scan(self, scan_data):
        """检测端口扫描"""
        print("\n--- 检测端口扫描 ---")
        print(f"扫描数据: {scan_data}")
        
        # 端口扫描特征
        if scan_data.get("port_scan_count", 0) > 100:
            print("检测到端口扫描")
            self.log_security_event("端口扫描", "检测", True, f"检测到端口扫描，扫描端口数: {scan_data['port_scan_count']}")
            return True
        else:
            print("未检测到端口扫描")
            self.log_security_event("端口扫描", "检测", False, "未检测到端口扫描")
            return False
    
    def log_security_event(self, vulnerability, action, detected, message):
        """记录安全事件"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "vulnerability": vulnerability,
            "action": action,
            "detected": detected,
            "message": message
        }
        self.security_logs.append(log_entry)
    
    def show_vulnerabilities(self):
        """显示网络安全漏洞类型"""
        print("\n--- 网络安全漏洞类型 ---")
        for vuln, description in self.vulnerabilities.items():
            print(f"- {vuln}: {description}")
    
    def show_security_measures(self):
        """显示网络安全防护措施"""
        print("\n--- 网络安全防护措施 ---")
        for measure, description in self.security_measures.items():
            print(f"- {measure}: {description}")
    
    def show_security_logs(self):
        """显示安全日志"""
        print("\n--- 安全日志 ---")
        for log in self.security_logs:
            status = "检测到" if log["detected"] else "未检测到"
            print(f"[{log['timestamp']}] {log['vulnerability']} - {log['action']} - {status}: {log['message']}")
    
    def generate_security_report(self):
        """生成安全报告"""
        print("\n--- 生成安全报告 ---")
        
        # 统计安全事件
        total_events = len(self.security_logs)
        detected_events = sum(1 for log in self.security_logs if log["detected"])
        undetected_events = total_events - detected_events
        
        # 统计漏洞类型
        vulnerability_stats = {}
        for log in self.security_logs:
            vuln = log["vulnerability"]
            if vuln not in vulnerability_stats:
                vulnerability_stats[vuln] = {"total": 0, "detected": 0}
            vulnerability_stats[vuln]["total"] += 1
            if log["detected"]:
                vulnerability_stats[vuln]["detected"] += 1
        
        report = {
            "report_info": {
                "title": "网络安全报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "NetworkSecurityDemo"
            },
            "security_summary": {
                "total_events": total_events,
                "detected_events": detected_events,
                "undetected_events": undetected_events,
                "detection_rate": detected_events / total_events if total_events > 0 else 0
            },
            "vulnerability_stats": vulnerability_stats,
            "vulnerabilities": self.vulnerabilities,
            "security_measures": self.security_measures,
            "recommendations": [
                "使用防火墙过滤网络流量",
                "部署入侵检测系统",
                "使用SSL/TLS加密传输",
                "实施网络分段",
                "定期进行网络安全扫描"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_network_security(self):
        """演示网络安全"""
        print("=== 网络安全演示 ===")
        print("====================")
        
        # 1. 显示网络安全漏洞类型
        print("\n1. 网络安全漏洞类型:")
        self.show_vulnerabilities()
        
        # 2. 显示网络安全防护措施
        print("\n2. 网络安全防护措施:")
        self.show_security_measures()
        
        # 3. 测试DDoS攻击检测
        print("\n3. 测试DDoS攻击检测:")
        ddos_traffic = {"request_rate": 1500}
        normal_traffic = {"request_rate": 500}
        self.detect_ddos_attack(ddos_traffic)
        self.detect_ddos_attack(normal_traffic)
        
        # 4. 测试ARP欺骗检测
        print("\n4. 测试ARP欺骗检测:")
        arp_spoofing = {"duplicate_ips": True}
        normal_arp = {"duplicate_ips": False}
        self.detect_arp_spoofing(arp_spoofing)
        self.detect_arp_spoofing(normal_arp)
        
        # 5. 测试DNS劫持检测
        print("\n5. 测试DNS劫持检测:")
        dns_hijacking = {"unauthorized_servers": True}
        normal_dns = {"unauthorized_servers": False}
        self.detect_dns_hijacking(dns_hijacking)
        self.detect_dns_hijacking(normal_dns)
        
        # 6. 测试端口扫描检测
        print("\n6. 测试端口扫描检测:")
        port_scan = {"port_scan_count": 200}
        normal_scan = {"port_scan_count": 50}
        self.detect_port_scan(port_scan)
        self.detect_port_scan(normal_scan)
        
        # 7. 显示安全日志
        print("\n7. 安全日志:")
        self.show_security_logs()
        
        # 8. 生成安全报告
        print("\n8. 生成安全报告:")
        self.generate_security_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了网络安全的基本概念和常见漏洞。")
        print("网络安全是安全框架的重要组成部分，用于保护网络免受攻击。")

if __name__ == "__main__":
    network_security_demo = NetworkSecurityDemo()
    network_security_demo.demonstrate_network_security()