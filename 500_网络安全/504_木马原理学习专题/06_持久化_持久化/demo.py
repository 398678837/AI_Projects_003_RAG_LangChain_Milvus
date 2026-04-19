import os
import sys
import winreg
import shutil
import subprocess
import time
from datetime import datetime

class Persistence:
    def __init__(self):
        self.persistence_methods = [
            "启动项",
            "服务",
            "计划任务",
            "WMI事件订阅",
            "DLL劫持",
            "注册表 Run 键",
            "启动文件夹",
            "引导过程"
        ]
    
    def add_to_startup(self, name, path):
        """添加到启动项"""
        print(f"\n--- 添加到启动项: {name} ---")
        
        try:
            # 添加到当前用户的启动项
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
            winreg.CloseKey(key)
            print(f"成功添加到当前用户启动项: {name}")
            
            # 尝试添加到所有用户的启动项（需要管理员权限）
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0,
                    winreg.KEY_SET_VALUE
                )
                winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
                winreg.CloseKey(key)
                print(f"成功添加到所有用户启动项: {name}")
            except Exception as e:
                print(f"添加到所有用户启动项失败（需要管理员权限）: {str(e)}")
            
            return True
        except Exception as e:
            print(f"添加到启动项失败: {str(e)}")
            return False
    
    def create_service(self, service_name, display_name, path):
        """创建服务"""
        print(f"\n--- 创建服务: {service_name} ---")
        
        try:
            # 使用sc命令创建服务
            result = subprocess.run(
                ["sc", "create", service_name, "binPath=", path, "displayName=", display_name, "start=", "auto"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"成功创建服务: {service_name}")
                
                # 启动服务
                start_result = subprocess.run(
                    ["sc", "start", service_name],
                    capture_output=True,
                    text=True
                )
                if start_result.returncode == 0:
                    print(f"成功启动服务: {service_name}")
                else:
                    print(f"启动服务失败: {start_result.stderr}")
                
                return True
            else:
                print(f"创建服务失败: {result.stderr}")
                return False
        except Exception as e:
            print(f"创建服务失败: {str(e)}")
            return False
    
    def create_scheduled_task(self, task_name, path):
        """创建计划任务"""
        print(f"\n--- 创建计划任务: {task_name} ---")
        
        try:
            # 使用schtasks命令创建计划任务
            # 每天启动时运行
            result = subprocess.run(
                ["schtasks", "/create", "/tn", task_name, "/tr", path, "/sc", "onlogon", "/f"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"成功创建计划任务: {task_name}")
                return True
            else:
                print(f"创建计划任务失败: {result.stderr}")
                return False
        except Exception as e:
            print(f"创建计划任务失败: {str(e)}")
            return False
    
    def add_to_startup_folder(self, name, path):
        """添加到启动文件夹"""
        print(f"\n--- 添加到启动文件夹: {name} ---")
        
        try:
            # 获取当前用户的启动文件夹路径
            startup_folder = os.path.join(os.environ['APPDATA'], r"Microsoft\Windows\Start Menu\Programs\Startup")
            
            # 创建快捷方式
            shortcut_path = os.path.join(startup_folder, f"{name}.lnk")
            
            # 使用powershell创建快捷方式
            powershell_command = f"$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('{shortcut_path}'); $Shortcut.TargetPath = '{path}'; $Shortcut.Save()"
            result = subprocess.run(
                ["powershell", "-Command", powershell_command],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"成功添加到启动文件夹: {name}")
                return True
            else:
                print(f"添加到启动文件夹失败: {result.stderr}")
                return False
        except Exception as e:
            print(f"添加到启动文件夹失败: {str(e)}")
            return False
    
    def copy_to_system_directory(self, source_path):
        """复制到系统目录"""
        print(f"\n--- 复制到系统目录 ---")
        
        try:
            # 获取系统目录路径
            system32 = os.environ['WINDIR'] + "\\System32"
            
            # 生成随机文件名
            random_name = f"{self._generate_random_string(8)}.exe"
            target_path = os.path.join(system32, random_name)
            
            # 复制文件
            shutil.copy2(source_path, target_path)
            print(f"成功复制到系统目录: {target_path}")
            return target_path
        except Exception as e:
            print(f"复制到系统目录失败: {str(e)}")
            return None
    
    def _generate_random_string(self, length=8):
        """生成随机字符串"""
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def check_persistence(self):
        """检查持久化项"""
        print("\n--- 检查持久化项 ---")
        
        # 检查启动项
        print("\n1. 检查启动项:")
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
                        print(f"  {value_name}: {value_data}")
                        i += 1
                    except OSError:
                        break
            finally:
                winreg.CloseKey(key)
        except Exception as e:
            print(f"  检查启动项失败: {str(e)}")
        
        # 检查服务
        print("\n2. 检查服务:")
        try:
            result = subprocess.run(
                ["sc", "query"],
                capture_output=True,
                text=True
            )
            # 只显示前20行，避免输出过多
            lines = result.stdout.split('\n')[:20]
            for line in lines:
                print(f"  {line}")
            if len(result.stdout.split('\n')) > 20:
                print("  ... (输出被截断)")
        except Exception as e:
            print(f"  检查服务失败: {str(e)}")
        
        # 检查计划任务
        print("\n3. 检查计划任务:")
        try:
            result = subprocess.run(
                ["schtasks", "/query", "/fo", "list", "/v"],
                capture_output=True,
                text=True
            )
            # 只显示前20行，避免输出过多
            lines = result.stdout.split('\n')[:20]
            for line in lines:
                print(f"  {line}")
            if len(result.stdout.split('\n')) > 20:
                print("  ... (输出被截断)")
        except Exception as e:
            print(f"  检查计划任务失败: {str(e)}")
        
        # 检查启动文件夹
        print("\n4. 检查启动文件夹:")
        try:
            startup_folder = os.path.join(os.environ['APPDATA'], r"Microsoft\Windows\Start Menu\Programs\Startup")
            if os.path.exists(startup_folder):
                files = os.listdir(startup_folder)
                for file in files:
                    print(f"  {file}")
            else:
                print("  启动文件夹不存在")
        except Exception as e:
            print(f"  检查启动文件夹失败: {str(e)}")
    
    def remove_persistence(self, name):
        """移除持久化项"""
        print(f"\n--- 移除持久化项: {name} ---")
        
        # 从启动项中移除
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE
            )
            try:
                winreg.DeleteValue(key, name)
                print(f"成功从当前用户启动项中移除: {name}")
            except FileNotFoundError:
                print(f"在当前用户启动项中未找到: {name}")
            finally:
                winreg.CloseKey(key)
        except Exception as e:
            print(f"从启动项中移除失败: {str(e)}")
        
        # 从服务中移除
        try:
            result = subprocess.run(
                ["sc", "stop", name],
                capture_output=True,
                text=True
            )
            result = subprocess.run(
                ["sc", "delete", name],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"成功删除服务: {name}")
            else:
                print(f"删除服务失败: {result.stderr}")
        except Exception as e:
            print(f"从服务中移除失败: {str(e)}")
        
        # 从计划任务中移除
        try:
            result = subprocess.run(
                ["schtasks", "/delete", "/tn", name, "/f"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"成功删除计划任务: {name}")
            else:
                print(f"删除计划任务失败: {result.stderr}")
        except Exception as e:
            print(f"从计划任务中移除失败: {str(e)}")
        
        # 从启动文件夹中移除
        try:
            startup_folder = os.path.join(os.environ['APPDATA'], r"Microsoft\Windows\Start Menu\Programs\Startup")
            shortcut_path = os.path.join(startup_folder, f"{name}.lnk")
            if os.path.exists(shortcut_path):
                os.remove(shortcut_path)
                print(f"成功从启动文件夹中移除: {name}")
            else:
                print(f"在启动文件夹中未找到: {name}")
        except Exception as e:
            print(f"从启动文件夹中移除失败: {str(e)}")
    
    def demonstrate_persistence(self):
        """演示持久化技术"""
        print("=== 持久化技术演示 ===")
        print("======================")
        
        # 1. 显示持久化技术列表
        print("\n1. 持久化技术列表:")
        for i, technique in enumerate(self.persistence_methods, 1):
            print(f"   {i}. {technique}")
        
        # 2. 创建测试可执行文件
        print("\n2. 创建测试可执行文件:")
        test_exe = "test_persistence.exe"
        
        # 创建一个简单的测试可执行文件
        with open(test_exe, 'w') as f:
            f.write('''
@echo off
echo Test persistence executed at %date% %time%
echo Test persistence executed at %date% %time% >> persistence_log.txt
timeout /t 2 >nul
''')
        
        # 将批处理文件转换为可执行文件（使用bat to exe工具，这里只是模拟）
        print(f"创建测试可执行文件: {test_exe}")
        
        # 3. 演示各种持久化方法
        print("\n3. 演示持久化方法:")
        persistence_name = "TestPersistence"
        
        # 复制到系统目录
        system_path = self.copy_to_system_directory(test_exe)
        if not system_path:
            system_path = os.path.abspath(test_exe)
        
        # 添加到启动项
        self.add_to_startup(persistence_name, system_path)
        
        # 创建计划任务
        self.create_scheduled_task(persistence_name, system_path)
        
        # 添加到启动文件夹
        self.add_to_startup_folder(persistence_name, system_path)
        
        # 4. 检查持久化项
        print("\n4. 检查持久化项:")
        self.check_persistence()
        
        # 5. 移除持久化项
        print("\n5. 移除持久化项:")
        self.remove_persistence(persistence_name)
        
        # 清理测试文件
        if os.path.exists(test_exe):
            os.remove(test_exe)
        if os.path.exists("persistence_log.txt"):
            os.remove("persistence_log.txt")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了持久化技术的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    if sys.platform != "win32":
        print("此演示仅在Windows平台上运行")
        sys.exit(1)
    
    persistence = Persistence()
    persistence.demonstrate_persistence()