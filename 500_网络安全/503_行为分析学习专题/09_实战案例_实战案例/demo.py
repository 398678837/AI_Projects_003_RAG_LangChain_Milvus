import psutil
import os
import hashlib
import json
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import scapy.all as scapy
import winreg
import threading

class MaliciousActivityDetector:
    def __init__(self):
        self.suspicious_processes = []
        self.suspicious_files = []
        self.suspicious_network = []
        self.suspicious_registry = []
        self.alerts = []
        self.monitoring = False
    
    def calculate_file_hash(self, file_path):
        """计算文件哈希值"""
        try:
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def monitor_processes(self, duration=60):
        """监控进程活动"""
        print("\n--- 监控进程活动 ---")
        start_time = time.time()
        
        while time.time() - start_time < duration and self.monitoring:
            for proc in psutil.process_iter(['pid', 'name', 'ppid', 'exe', 'cmdline']):
                try:
                    proc_info = proc.info
                    pid = proc_info['pid']
                    name = proc_info['name']
                    exe = proc_info.get('exe', 'N/A')
                    cmdline = proc_info.get('cmdline', [])
                    
                    # 检测可疑进程特征
                    suspicious_indicators = [
                        'cmd.exe /c',
                        'powershell.exe -EncodedCommand',
                        'regsvr32.exe /s',
                        'wscript.exe',
                        'cscript.exe'
                    ]
                    
                    cmdline_str = ' '.join(cmdline) if cmdline else ''
                    
                    for indicator in suspicious_indicators:
                        if indicator in cmdline_str:
                            alert = {
                                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                'type': 'Process',
                                'message': f'可疑进程: {name} (PID: {pid})',
                                'details': f'命令行: {cmdline_str}',
                                'severity': 'High'
                            }
                            if alert not in self.alerts:
                                self.alerts.append(alert)
                                self.suspicious_processes.append(proc_info)
                                print(f"[ALERT] {alert['message']} - {alert['details']}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            time.sleep(2)
    
    def monitor_files(self, directories=None, duration=60):
        """监控文件系统活动"""
        print("\n--- 监控文件系统活动 ---")
        
        if directories is None:
            directories = [
                os.path.expanduser('~\\AppData\\Local\\Temp'),
                os.path.expanduser('~\\AppData\\Roaming'),
                'C:\\Windows\\Temp'
            ]
        
        class FileChangeHandler(FileSystemEventHandler):
            def __init__(self, detector):
                self.detector = detector
            
            def on_modified(self, event):
                if not event.is_directory:
                    self.check_file(event.src_path)
            
            def on_created(self, event):
                if not event.is_directory:
                    self.check_file(event.src_path)
            
            def check_file(self, file_path):
                # 检测可疑文件类型
                suspicious_extensions = ['.exe', '.dll', '.sys', '.bat', '.cmd', '.ps1', '.vbs', '.js']
                file_ext = os.path.splitext(file_path)[1].lower()
                
                if file_ext in suspicious_extensions:
                    alert = {
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'type': 'File',
                        'message': f'可疑文件操作: {file_path}',
                        'details': f'文件类型: {file_ext}',
                        'severity': 'Medium'
                    }
                    if alert not in self.detector.alerts:
                        self.detector.alerts.append(alert)
                        self.detector.suspicious_files.append({'path': file_path, 'extension': file_ext})
                        print(f"[ALERT] {alert['message']}")
        
        observer = Observer()
        handler = FileChangeHandler(self)
        
        for directory in directories:
            if os.path.exists(directory):
                observer.schedule(handler, directory, recursive=True)
        
        observer.start()
        
        start_time = time.time()
        while time.time() - start_time < duration and self.monitoring:
            time.sleep(1)
        
        observer.stop()
        observer.join()
    
    def monitor_network(self, duration=60):
        """监控网络活动"""
        print("\n--- 监控网络活动 ---")
        
        def packet_handler(packet):
            if packet.haslayer(scapy.IP):
                src_ip = packet[scapy.IP].src
                dst_ip = packet[scapy.IP].dst
                
                # 检测可疑端口
                suspicious_ports = [22, 443, 8080, 9000, 3389]
                
                if packet.haslayer(scapy.TCP):
                    dst_port = packet[scapy.TCP].dport
                    if dst_port in suspicious_ports:
                        alert = {
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'type': 'Network',
                            'message': f'可疑网络连接: {src_ip} -> {dst_ip}:{dst_port}',
                            'details': f'TCP连接到可疑端口',
                            'severity': 'Medium'
                        }
                        if alert not in self.alerts:
                            self.alerts.append(alert)
                            self.suspicious_network.append({'src_ip': src_ip, 'dst_ip': dst_ip, 'port': dst_port})
                            print(f"[ALERT] {alert['message']}")
        
        # 启动网络监控线程
        def start_sniffing():
            scapy.sniff(prn=packet_handler, timeout=duration)
        
        sniff_thread = threading.Thread(target=start_sniffing)
        sniff_thread.daemon = True
        sniff_thread.start()
        
        sniff_thread.join()
    
    def monitor_registry(self, duration=60):
        """监控注册表活动"""
        print("\n--- 监控注册表活动 ---")
        
        # 检查常见的启动项位置
        startup_locations = [
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce',
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run',
            r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run'
        ]
        
        start_time = time.time()
        while time.time() - start_time < duration and self.monitoring:
            for location in startup_locations:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, location, 0, winreg.KEY_READ)
                    try:
                        i = 0
                        while True:
                            try:
                                value_name, value_data, value_type = winreg.EnumValue(key, i)
                                # 检测可疑的启动项
                                suspicious_names = ['svchost', 'system32', 'winlogon', 'explorer']
                                for name in suspicious_names:
                                    if name.lower() in value_name.lower() or name.lower() in str(value_data).lower():
                                        alert = {
                                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                            'type': 'Registry',
                                            'message': f'可疑注册表项: {location}\\{value_name}',
                                            'details': f'值: {value_data}',
                                            'severity': 'High'
                                        }
                                        if alert not in self.alerts:
                                            self.alerts.append(alert)
                                            self.suspicious_registry.append({'location': location, 'name': value_name, 'data': value_data})
                                            print(f"[ALERT] {alert['message']}")
                                i += 1
                            except OSError:
                                break
                    finally:
                        winreg.CloseKey(key)
                except Exception as e:
                    pass
            time.sleep(5)
    
    def run_comprehensive_analysis(self, duration=120):
        """运行综合分析"""
        print("=== 开始综合行为分析 ===")
        self.monitoring = True
        
        # 启动各个监控线程
        threads = []
        
        # 进程监控线程
        process_thread = threading.Thread(target=self.monitor_processes, args=(duration,))
        threads.append(process_thread)
        
        # 文件监控线程
        file_thread = threading.Thread(target=self.monitor_files, args=(None, duration))
        threads.append(file_thread)
        
        # 网络监控线程
        network_thread = threading.Thread(target=self.monitor_network, args=(duration,))
        threads.append(network_thread)
        
        # 注册表监控线程
        registry_thread = threading.Thread(target=self.monitor_registry, args=(duration,))
        threads.append(registry_thread)
        
        # 启动所有线程
        for thread in threads:
            thread.daemon = True
            thread.start()
        
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        
        self.monitoring = False
        self.generate_analysis_report()
    
    def generate_analysis_report(self):
        """生成分析报告"""
        print("\n=== 行为分析报告 ===")
        
        report = {
            "analysis_summary": {
                "total_alerts": len(self.alerts),
                "suspicious_processes": len(self.suspicious_processes),
                "suspicious_files": len(self.suspicious_files),
                "suspicious_network": len(self.suspicious_network),
                "suspicious_registry": len(self.suspicious_registry),
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            "alerts": self.alerts,
            "suspicious_activities": {
                "processes": self.suspicious_processes,
                "files": self.suspicious_files,
                "network": self.suspicious_network,
                "registry": self.suspicious_registry
            },
            "recommendations": [
                "对可疑进程进行深入分析",
                "检查可疑文件的哈希值是否在威胁情报库中",
                "阻止可疑的网络连接",
                "删除可疑的注册表项",
                "运行完整的系统扫描"
            ]
        }
        
        # 保存报告到文件
        report_file = f"behavior_analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"报告已保存到: {report_file}")
        print(f"\n总警报数: {len(self.alerts)}")
        print(f"可疑进程: {len(self.suspicious_processes)}")
        print(f"可疑文件: {len(self.suspicious_files)}")
        print(f"可疑网络活动: {len(self.suspicious_network)}")
        print(f"可疑注册表项: {len(self.suspicious_registry)}")

if __name__ == "__main__":
    detector = MaliciousActivityDetector()
    print("行为分析实战案例 - 综合检测系统")
    print("==================================")
    print("该系统将监控以下活动:")
    print("1. 进程创建和执行")
    print("2. 文件系统修改")
    print("3. 网络连接")
    print("4. 注册表修改")
    print("\n开始监控... (持续2分钟)")
    
    try:
        detector.run_comprehensive_analysis(duration=120)
    except KeyboardInterrupt:
        detector.monitoring = False
        print("\n监控已手动停止")
    
    print("\n分析完成!")