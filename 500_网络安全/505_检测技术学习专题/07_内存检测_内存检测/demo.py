import os
import sys
import json
import time
import psutil
from datetime import datetime
import ctypes

class MemoryDetection:
    def __init__(self):
        # 内存检测规则
        self.memory_rules = [
            {
                "name": "可疑内存注入",
                "conditions": [
                    "远程线程注入",
                    "DLL注入",
                    "代码注入"
                ],
                "severity": "高"
            },
            {
                "name": "可疑内存特征",
                "conditions": [
                    "Shellcode特征",
                    "加密代码",
                    "混淆代码"
                ],
                "severity": "高"
            },
            {
                "name": "异常内存行为",
                "conditions": [
                    "内存分配异常",
                    "内存修改异常",
                    "内存执行异常"
                ],
                "severity": "中"
            },
            {
                "name": "恶意代码特征",
                "conditions": [
                    "网络连接代码",
                    "文件操作代码",
                    "注册表操作代码"
                ],
                "severity": "中"
            }
        ]
        
        # 内存检测结果
        self.memory_results = {
            "process_memory": [],
            "suspicious_memory": []
        }
    
    def get_process_memory(self, process_id):
        """获取进程内存信息"""
        print(f"\n--- 获取进程内存信息: {process_id} ---")
        
        try:
            process = psutil.Process(process_id)
            process_name = process.name()
            
            # 获取进程内存信息
            memory_info = process.memory_info()
            memory_maps = process.memory_maps()
            
            print(f"进程名称: {process_name}")
            print(f"内存使用: {memory_info.rss / 1024 / 1024:.2f} MB")
            print(f"虚拟内存: {memory_info.vms / 1024 / 1024:.2f} MB")
            print(f"内存映射数量: {len(memory_maps)}")
            
            # 保存内存信息
            self.memory_results["process_memory"].append({
                "process_name": process_name,
                "process_id": process_id,
                "memory_info": {
                    "rss": memory_info.rss,
                    "vms": memory_info.vms,
                    "maps_count": len(memory_maps)
                }
            })
            
            # 分析内存映射
            for map in memory_maps[:5]:  # 只分析前5个内存映射
                print(f"  - {map.path}: {map.rss / 1024:.2f} KB")
            
            if len(memory_maps) > 5:
                print(f"  ... 还有 {len(memory_maps) - 5} 个内存映射")
            
        except Exception as e:
            print(f"获取进程内存信息失败: {str(e)}")
    
    def analyze_memory(self, process_id):
        """分析进程内存"""
        print(f"\n--- 分析进程内存: {process_id} ---")
        
        try:
            process = psutil.Process(process_id)
            process_name = process.name()
            
            # 模拟内存分析
            print(f"分析 {process_name} 的内存...")
            
            # 模拟发现可疑内存
            suspicious_memory = [
                {
                    "address": "0x10000000",
                    "size": "4096",
                    "protection": "PAGE_EXECUTE_READWRITE",
                    "type": "可疑内存",
                    "reason": "包含Shellcode特征"
                },
                {
                    "address": "0x20000000",
                    "size": "8192",
                    "protection": "PAGE_EXECUTE",
                    "type": "可疑内存",
                    "reason": "执行权限异常"
                }
            ]
            
            for memory in suspicious_memory:
                self.memory_results["suspicious_memory"].append({
                    "process_name": process_name,
                    "process_id": process_id,
                    "memory": memory
                })
                print(f"发现可疑内存: {memory['address']} (大小: {memory['size']} 字节, 权限: {memory['protection']}, 原因: {memory['reason']})")
            
        except Exception as e:
            print(f"分析进程内存失败: {str(e)}")
    
    def scan_processes(self):
        """扫描进程内存"""
        print("\n--- 扫描进程内存 ---")
        
        # 扫描前5个进程
        processes = list(psutil.process_iter(['pid', 'name']))[:5]
        for process in processes:
            try:
                print(f"\n扫描进程: {process.info['name']} (PID: {process.info['pid']})")
                self.get_process_memory(process.info['pid'])
                self.analyze_memory(process.info['pid'])
            except Exception as e:
                print(f"扫描进程失败: {str(e)}")
    
    def generate_memory_report(self):
        """生成内存检测报告"""
        print("\n--- 生成内存检测报告 ---")
        
        report = {
            "report_info": {
                "title": "内存检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "detector": "MemoryDetection"
            },
            "scan_summary": {
                "scanned_processes": len(self.memory_results["process_memory"]),
                "suspicious_processes": len(set([item["process_id"] for item in self.memory_results["suspicious_memory"]])),
                "suspicious_memory_count": len(self.memory_results["suspicious_memory"])
            },
            "memory_rules": self.memory_rules,
            "memory_results": self.memory_results,
            "recommendations": [
                "定期扫描进程内存",
                "监控内存注入行为",
                "使用内存保护技术",
                "结合其他检测技术提高检测准确率"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_memory_detection(self):
        """演示内存检测"""
        print("=== 内存检测演示 ===")
        print("====================")
        
        # 1. 显示内存检测规则
        print("\n1. 内存检测规则:")
        for rule in self.memory_rules:
            print(f"  - {rule['name']} (严重程度: {rule['severity']})")
            for condition in rule['conditions']:
                print(f"    - {condition}")
        
        # 2. 扫描进程内存
        print("\n2. 扫描进程内存:")
        self.scan_processes()
        
        # 3. 生成内存检测报告
        print("\n3. 生成内存检测报告:")
        self.generate_memory_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了内存检测的基本原理和实现方法。")
        print("内存检测可以检测无文件恶意代码，是高级恶意代码检测的重要手段。")

if __name__ == "__main__":
    memory_detection = MemoryDetection()
    memory_detection.demonstrate_memory_detection()