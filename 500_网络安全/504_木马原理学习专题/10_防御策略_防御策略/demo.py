import os
import sys
import json
import time
import subprocess
import winreg
from datetime import datetime

class TrojanDefense:
    def __init__(self):
        self.defense_strategies = [
            "安装杀毒软件",
            "启用防火墙",
            "定期更新系统",
            "谨慎下载文件",
            "使用强密码",
            "定期备份数据",
            "监控系统行为",
            "安全意识培训"
        ]
    
    def check_antivirus(self):
        """检查杀毒软件"""
        print("\n--- 检查杀毒软件 ---")
        
        try:
            # 检查常见的杀毒软件
            antivirus_list = [
                "Windows Defender",
                "Avast",
                "Avira",
                "Bitdefender",
                "Kaspersky",
                "McAfee",
                "Norton",
                "ESET"
            ]
            
            installed_antivirus = []
            
            # 检查Windows Defender
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\Microsoft\Windows Defender",
                    0,
                    winreg.KEY_READ
                )
                installed_antivirus.append("Windows Defender")
                winreg.CloseKey(key)
            except Exception:
                pass
            
            # 检查其他杀毒软件
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    0,
                    winreg.KEY_READ
                )
                try:
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey = winreg.OpenKey(key, subkey_name)
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                for antivirus in antivirus_list:
                                    if antivirus in display_name:
                                        installed_antivirus.append(antivirus)
                            except Exception:
                                pass
                            winreg.CloseKey(subkey)
                            i += 1
                        except OSError:
                            break
                finally:
                    winreg.CloseKey(key)
            except Exception:
                pass
            
            if installed_antivirus:
                print("已安装的杀毒软件:")
                for antivirus in installed_antivirus:
                    print(f"  - {antivirus}")
            else:
                print("未检测到已安装的杀毒软件")
            
            return installed_antivirus
        except Exception as e:
            print(f"检查杀毒软件失败: {str(e)}")
            return []
    
    def check_firewall(self):
        """检查防火墙"""
        print("\n--- 检查防火墙 ---")
        
        try:
            # 检查Windows防火墙状态
            result = subprocess.run(
                ["netsh", "advfirewall", "show", "allprofiles"],
                capture_output=True,
                text=True
            )
            
            print("Windows防火墙状态:")
            for line in result.stdout.split('\n'):
                if "State" in line:
                    print(f"  {line}")
            
            return result.stdout
        except Exception as e:
            print(f"检查防火墙失败: {str(e)}")
            return None
    
    def check_windows_updates(self):
        """检查Windows更新"""
        print("\n--- 检查Windows更新 ---")
        
        try:
            # 检查Windows更新状态
            result = subprocess.run(
                ["powershell", "Get-WindowsUpdate"],
                capture_output=True,
                text=True
            )
            
            print("Windows更新状态:")
            if result.stdout:
                print(result.stdout)
            else:
                print("没有可用的更新")
            
            return result.stdout
        except Exception as e:
            print(f"检查Windows更新失败: {str(e)}")
            return None
    
    def check_startup_items(self):
        """检查启动项"""
        print("\n--- 检查启动项 ---")
        
        try:
            startup_items = []
            
            # 检查当前用户的启动项
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0,
                    winreg.KEY_READ
                )
                try:
                    i = 0
                    while True:
                        try:
                            value_name, value_data, value_type = winreg.EnumValue(key, i)
                            startup_items.append({"name": value_name, "path": value_data, "location": "Current User"})
                            i += 1
                        except OSError:
                            break
                finally:
                    winreg.CloseKey(key)
            except Exception:
                pass
            
            # 检查所有用户的启动项
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0,
                    winreg.KEY_READ
                )
                try:
                    i = 0
                    while True:
                        try:
                            value_name, value_data, value_type = winreg.EnumValue(key, i)
                            startup_items.append({"name": value_name, "path": value_data, "location": "All Users"})
                            i += 1
                        except OSError:
                            break
                finally:
                    winreg.CloseKey(key)
            except Exception:
                pass
            
            print("启动项:")
            for item in startup_items:
                print(f"  - {item['name']} ({item['location']}): {item['path']}")
            
            return startup_items
        except Exception as e:
            print(f"检查启动项失败: {str(e)}")
            return []
    
    def check_services(self):
        """检查服务"""
        print("\n--- 检查服务 ---")
        
        try:
            # 检查服务状态
            result = subprocess.run(
                ["sc", "query"],
                capture_output=True,
                text=True
            )
            
            # 只显示前20行，避免输出过多
            lines = result.stdout.split('\n')[:20]
            print("服务状态:")
            for line in lines:
                print(f"  {line}")
            
            if len(result.stdout.split('\n')) > 20:
                print("  ... (输出被截断)")
            
            return result.stdout
        except Exception as e:
            print(f"检查服务失败: {str(e)}")
            return None
    
    def check_scheduled_tasks(self):
        """检查计划任务"""
        print("\n--- 检查计划任务 ---")
        
        try:
            # 检查计划任务
            result = subprocess.run(
                ["schtasks", "/query", "/fo", "list", "/v"],
                capture_output=True,
                text=True
            )
            
            # 只显示前20行，避免输出过多
            lines = result.stdout.split('\n')[:20]
            print("计划任务:")
            for line in lines:
                print(f"  {line}")
            
            if len(result.stdout.split('\n')) > 20:
                print("  ... (输出被截断)")
            
            return result.stdout
        except Exception as e:
            print(f"检查计划任务失败: {str(e)}")
            return None
    
    def scan_system(self):
        """扫描系统"""
        print("\n--- 扫描系统 ---")
        
        try:
            # 使用Windows Defender扫描
            print("使用Windows Defender扫描系统...")
            result = subprocess.run(
                ["powershell", "Start-MpScan -ScanType QuickScan"],
                capture_output=True,
                text=True
            )
            
            print("扫描结果:")
            print(result.stdout)
            if result.stderr:
                print(f"错误: {result.stderr}")
            
            return result.stdout
        except Exception as e:
            print(f"扫描系统失败: {str(e)}")
            return None
    
    def generate_defense_report(self):
        """生成防御报告"""
        print("\n--- 生成防御报告 ---")
        
        try:
            report = {
                "report_info": {
                    "title": "木马防御报告",
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "system": {
                        "os": os.name,
                        "platform": sys.platform
                    }
                },
                "defense_status": {
                    "antivirus": self.check_antivirus(),
                    "firewall": self.check_firewall() is not None,
                    "windows_updates": self.check_windows_updates() is not None,
                    "startup_items": self.check_startup_items(),
                    "services": self.check_services() is not None,
                    "scheduled_tasks": self.check_scheduled_tasks() is not None
                },
                "recommendations": [
                    "安装并更新杀毒软件",
                    "启用防火墙",
                    "定期更新系统和应用程序",
                    "不随意下载和运行未知文件",
                    "使用强密码并定期更换",
                    "定期备份重要数据",
                    "监控系统行为，及时发现异常",
                    "提高安全意识，避免点击可疑链接"
                ]
            }
            
            # 保存报告到文件
            report_file = f"defense_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            print(f"防御报告已保存到: {report_file}")
            
            # 清理测试文件
            if os.path.exists(report_file):
                os.remove(report_file)
            
            return report
        except Exception as e:
            print(f"生成防御报告失败: {str(e)}")
            return None
    
    def demonstrate_defense(self):
        """演示防御策略"""
        print("=== 木马防御策略演示 ===")
        print("========================")
        
        # 1. 显示防御策略列表
        print("\n1. 木马防御策略列表:")
        for i, strategy in enumerate(self.defense_strategies, 1):
            print(f"   {i}. {strategy}")
        
        # 2. 检查系统防御状态
        print("\n2. 检查系统防御状态:")
        
        # 检查杀毒软件
        self.check_antivirus()
        
        # 检查防火墙
        self.check_firewall()
        
        # 检查Windows更新
        self.check_windows_updates()
        
        # 检查启动项
        self.check_startup_items()
        
        # 检查服务
        self.check_services()
        
        # 检查计划任务
        self.check_scheduled_tasks()
        
        # 3. 扫描系统
        print("\n3. 扫描系统:")
        self.scan_system()
        
        # 4. 生成防御报告
        print("\n4. 生成防御报告:")
        self.generate_defense_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了木马防御的基本策略和实现方法。")
        print("请根据防御报告中的建议，加强系统的安全防护。")

if __name__ == "__main__":
    defense = TrojanDefense()
    defense.demonstrate_defense()