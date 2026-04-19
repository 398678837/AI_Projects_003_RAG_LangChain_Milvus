import os
import json
import hashlib
import time
from datetime import datetime

class TrojanBasics:
    def __init__(self):
        self.trojan_types = {
            "远程控制型": ["灰鸽子", "冰河", "TeamViewer"],
            "数据窃取型": ["键盘记录器", "密码窃取器", "Cookie窃取器"],
            "破坏型": ["勒索软件", "DDoS木马", "删除型木马"],
            "代理型": ["肉鸡木马", "代理服务器木马"],
            "下载型": ["下载器", "多态木马"]
        }
        
        self.trojan_structure = {
            "客户端": ["命令控制界面", "数据显示", "配置管理"],
            "服务端": ["启动模块", "通信模块", "功能模块", "持久化模块"],
            "通信协议": ["TCP", "UDP", "HTTP", "HTTPS", "自定义协议"]
        }
    
    def get_trojan_types(self):
        """获取木马类型"""
        print("\n--- 木马类型 ---\n")
        for trojan_type, examples in self.trojan_types.items():
            print(f"{trojan_type}:")
            for example in examples:
                print(f"  - {example}")
    
    def get_trojan_structure(self):
        """获取木马结构"""
        print("\n--- 木马结构 ---\n")
        for component, parts in self.trojan_structure.items():
            print(f"{component}:")
            for part in parts:
                print(f"  - {part}")
    
    def simulate_trojan_communication(self):
        """模拟木马通信过程"""
        print("\n--- 模拟木马通信过程 ---\n")
        
        # 模拟服务端启动
        print("[服务端] 启动并监听端口...")
        time.sleep(1)
        
        # 模拟客户端连接
        print("[客户端] 连接到服务端...")
        time.sleep(1)
        
        # 模拟认证过程
        print("[客户端] 发送认证信息...")
        time.sleep(1)
        print("[服务端] 验证认证信息...")
        time.sleep(1)
        print("[服务端] 认证成功，建立连接...")
        time.sleep(1)
        
        # 模拟命令执行
        print("[客户端] 发送命令: 获取系统信息")
        time.sleep(1)
        print("[服务端] 执行命令...")
        time.sleep(1)
        print("[服务端] 返回系统信息...")
        time.sleep(1)
        print("[客户端] 接收并显示系统信息...")
        time.sleep(1)
        
        # 模拟断开连接
        print("[客户端] 发送断开连接命令...")
        time.sleep(1)
        print("[服务端] 断开连接...")
    
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
    
    def generate_trojan_report(self):
        """生成木马分析报告"""
        print("\n--- 生成木马分析报告 ---\n")
        
        report = {
            "report_info": {
                "title": "木马原理分析报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "analyst": "Security Researcher"
            },
            "trojan_types": self.trojan_types,
            "trojan_structure": self.trojan_structure,
            "communication_process": [
                "服务端启动并监听端口",
                "客户端连接到服务端",
                "客户端发送认证信息",
                "服务端验证认证信息",
                "认证成功，建立连接",
                "客户端发送命令",
                "服务端执行命令并返回结果",
                "客户端接收并显示结果",
                "断开连接"
            ],
            "security_recommendations": [
                "安装并更新杀毒软件",
                "启用防火墙",
                "定期更新系统和应用程序",
                "不随意下载和运行未知文件",
                "使用强密码并定期更换",
                "定期备份重要数据"
            ]
        }
        
        report_file = f"trojan_analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"报告已保存到: {report_file}")
        return report
    
    def demonstrate_trojan_basics(self):
        """演示木马基础概念"""
        print("=== 木马原理基础概念演示 ===")
        print("============================")
        
        # 展示木马类型
        self.get_trojan_types()
        
        # 展示木马结构
        self.get_trojan_structure()
        
        # 模拟木马通信
        self.simulate_trojan_communication()
        
        # 生成分析报告
        self.generate_trojan_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了木马的基本类型、结构和通信过程。")
        print("请继续学习后续章节，深入了解木马的高级技术。")

if __name__ == "__main__":
    trojan_basics = TrojanBasics()
    trojan_basics.demonstrate_trojan_basics()