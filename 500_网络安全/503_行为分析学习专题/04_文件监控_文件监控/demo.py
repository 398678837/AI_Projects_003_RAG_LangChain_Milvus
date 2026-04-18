#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件监控示例
演示如何使用Python进行文件监控、文件分析和文件行为检测
"""

import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileModifiedEvent, FileDeletedEvent, FileMovedEvent


class FileMonitorEventHandler(FileSystemEventHandler):
    """文件系统事件处理器"""
    
    def __init__(self, callback=None):
        self.callback = callback
    
    def on_created(self, event):
        """文件创建事件"""
        if not event.is_directory:
            self._handle_event('created', event.src_path)
    
    def on_modified(self, event):
        """文件修改事件"""
        if not event.is_directory:
            self._handle_event('modified', event.src_path)
    
    def on_deleted(self, event):
        """文件删除事件"""
        if not event.is_directory:
            self._handle_event('deleted', event.src_path)
    
    def on_moved(self, event):
        """文件移动事件"""
        if not event.is_directory:
            self._handle_event('moved', event.src_path, event.dest_path)
    
    def _handle_event(self, event_type, src_path, dest_path=None):
        """处理事件"""
        event_info = {
            'type': event_type,
            'src_path': src_path,
            'dest_path': dest_path,
            'timestamp': time.time()
        }
        
        if self.callback:
            self.callback(event_info)
        else:
            print(f"[{event_type.upper()}] {src_path}")
            if dest_path:
                print(f"  -> {dest_path}")


class FileMonitor:
    """文件监控器"""
    
    def __init__(self):
        self.observer = Observer()
        self.event_handler = FileMonitorEventHandler(self._on_event)
        self.monitored_paths = []
        self.events = []
    
    def _on_event(self, event_info):
        """事件回调"""
        self.events.append(event_info)
        self._analyze_event(event_info)
    
    def _analyze_event(self, event_info):
        """分析文件事件"""
        event_type = event_info['type']
        path = event_info['src_path']
        
        # 检测可疑文件类型
        suspicious_extensions = ['.exe', '.dll', '.bat', '.cmd', '.ps1', '.vbs']
        ext = os.path.splitext(path)[1].lower()
        if ext in suspicious_extensions:
            print(f"[!] 可疑文件类型: {path} (类型: {ext})")
        
        # 检测系统目录修改
        system_directories = ['C:\\Windows', 'C:\\Program Files', 'C:\\Program Files (x86)']
        if any(path.startswith(dir) for dir in system_directories):
            print(f"[!] 系统目录修改: {path}")
        
        # 检测临时目录活动
        temp_directories = ['C:\\Temp', 'C:\\Windows\\Temp', os.environ.get('TEMP', '')]
        if any(path.startswith(dir) for dir in temp_directories):
            print(f"[!] 临时目录活动: {path}")
    
    def add_path(self, path):
        """添加监控路径"""
        if os.path.exists(path):
            self.monitored_paths.append(path)
            self.observer.schedule(self.event_handler, path, recursive=True)
            print(f"[+] 监控路径: {path}")
        else:
            print(f"[-] 路径不存在: {path}")
    
    def start(self):
        """启动监控"""
        if self.monitored_paths:
            self.observer.start()
            print("\n[*] 文件监控已启动")
        else:
            print("[-] 没有监控路径")
    
    def stop(self):
        """停止监控"""
        self.observer.stop()
        self.observer.join()
        print("\n[*] 文件监控已停止")
    
    def get_events(self, event_type=None):
        """获取事件列表"""
        if event_type:
            return [e for e in self.events if e['type'] == event_type]
        return self.events


def analyze_file_hiding():
    """检测文件隐藏技术"""
    print("\n--- 文件隐藏技术分析 ---")
    
    # 检测隐藏属性
    test_dir = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 检查文件属性
                attrs = os.stat(file_path)
                # 检测隐藏属性
                if attrs.st_file_attributes & 0x02:  # FILE_ATTRIBUTE_HIDDEN
                    print(f"[!] 隐藏文件: {file_path}")
                # 检测系统属性
                if attrs.st_file_attributes & 0x04:  # FILE_ATTRIBUTE_SYSTEM
                    print(f"[!] 系统文件: {file_path}")
            except:
                pass


def main():
    """主函数"""
    print("=== 文件监控示例 ===")
    
    # 初始化监控器
    monitor = FileMonitor()
    
    # 添加监控路径
    monitor.add_path(os.path.dirname(os.path.abspath(__file__)))
    
    # 启动监控
    monitor.start()
    
    # 运行5秒
    print("\n[*] 监控中... (按Ctrl+C停止)")
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    
    # 停止监控
    monitor.stop()
    
    # 显示监控结果
    print(f"\n[*] 监控到的事件数量: {len(monitor.get_events())}")
    
    # 分析隐藏文件
    analyze_file_hiding()


if __name__ == "__main__":
    main()
