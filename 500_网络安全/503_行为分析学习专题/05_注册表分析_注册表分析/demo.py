#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注册表分析示例
演示如何使用Python进行注册表监控、注册表分析和注册表行为检测
"""

import winreg
import time
import threading
from datetime import datetime


class RegistryMonitor:
    """注册表监控器"""
    
    def __init__(self):
        self.monitoring = False
        self.lock = threading.Lock()
        self.changes = []
    
    def get_registry_value(self, hkey, subkey, value_name):
        """获取注册表值"""
        try:
            with winreg.OpenKey(hkey, subkey, 0, winreg.KEY_READ) as key:
                value, value_type = winreg.QueryValueEx(key, value_name)
                return {
                    'hkey': hkey,
                    'subkey': subkey,
                    'value_name': value_name,
                    'value': value,
                    'value_type': value_type
                }
        except FileNotFoundError:
            return None
        except PermissionError:
            return None
    
    def get_registry_keys(self, hkey, subkey):
        """获取注册表键"""
        try:
            with winreg.OpenKey(hkey, subkey, 0, winreg.KEY_READ) as key:
                keys = []
                i = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        keys.append(subkey_name)
                        i += 1
                    except OSError:
                        break
                return keys
        except FileNotFoundError:
            return None
        except PermissionError:
            return None
    
    def monitor_startup_items(self):
        """监控启动项"""
        startup_locations = [
            (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
            (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
            (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
            (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce")
        ]
        
        print("\n--- 启动项分析 ---")
        for hkey, subkey in startup_locations:
            keys = self.get_registry_keys(hkey, subkey)
            if keys:
                print(f"\n{winreg.HKEY_TO_HKEY_NAME[hkey]}\\{subkey}:")
                for key in keys:
                    value_info = self.get_registry_value(hkey, subkey, key)
                    if value_info:
                        print(f"  {key}: {value_info['value']}")
    
    def monitor_malware_registry(self):
        """监控恶意代码注册表痕迹"""
        malware_locations = [
            (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"),
            (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"),
            (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_CURRENT_USER, r"Software")
        ]
        
        print("\n--- 恶意代码注册表痕迹分析 ---")
        for hkey, subkey in malware_locations:
            keys = self.get_registry_keys(hkey, subkey)
            if keys:
                print(f"\n{winreg.HKEY_TO_HKEY_NAME[hkey]}\\{subkey}:")
                for key in keys[:10]:  # 只显示前10个
                    print(f"  {key}")
    
    def analyze_registry_permissions(self):
        """分析注册表权限"""
        print("\n--- 注册表权限分析 ---")
        # 这里可以添加权限分析代码
        pass


def main():
    """主函数"""
    print("=== 注册表分析示例 ===")
    
    # 初始化监控器
    monitor = RegistryMonitor()
    
    # 监控启动项
    monitor.monitor_startup_items()
    
    # 监控恶意代码注册表痕迹
    monitor.monitor_malware_registry()
    
    # 分析注册表权限
    monitor.analyze_registry_permissions()


if __name__ == "__main__":
    main()
