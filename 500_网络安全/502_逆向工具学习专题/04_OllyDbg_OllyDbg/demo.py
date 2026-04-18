#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OllyDbg调试器使用示例
演示OllyDbg的基本使用、调试功能、插件和技巧
"""


def ollydbg_overview():
    """OllyDbg概述"""
    print("\n--- 1. OllyDbg概述 ---")
    
    print("OllyDbg介绍:")
    print("  - 32位调试器")
    print("  - 用户友好")
    print("  - 插件丰富")
    
    print("\nOllyDbg安装:")
    print("  - 下载安装包")
    print("  - 解压安装")
    print("  - 配置环境")
    
    print("\nOllyDbg界面:")
    print("  - CPU窗口")
    print("  - 内存窗口")
    print("  - 寄存器窗口")
    
    print("\nOllyDbg配置:")
    print("  - 外观配置")
    print("  - 调试配置")
    print("  - 插件配置")


def debug_features():
    """调试功能"""
    print("\n--- 2. 调试功能 ---")
    
    print("加载程序:")
    print("  - 打开文件")
    print("  - 附加进程")
    print("  - 命令行参数")
    
    print("\n运行控制:")
    print("  - 运行: F9")
    print("  - 暂停: F12")
    print("  - 停止: Ctrl+F2")
    
    print("\n断点设置:")
    print("  - 软件断点: F2")
    print("  - 条件断点")
    print("  - 内存断点")
    
    print("\n内存查看:")
    print("  - 内存Dump")
    print("  - 内存搜索")
    print("  - 内存修改")


def plugin_system():
    """插件系统"""
    print("\n--- 3. 插件系统 ---")
    
    print("插件安装:")
    print("  - OllyDir目录")
    print("  - 重启生效")
    print("  - 插件管理")
    
    print("\n常用插件:")
    print("  - OllyDump: 脱壳")
    print("  - HideDebugger: 隐藏")
    print("  - CommandBar: 命令栏")
    
    print("\n插件开发:")
    print("  - SDK")
    print("  - API")
    print("  - 示例代码")
    
    print("\n插件配置:")
    print("  - 插件设置")
    print("  - 快捷键")
    print("  - 自动加载")


def debugging_techniques():
    """调试技巧"""
    print("\n--- 4. 调试技巧 ---")
    
    print("脱壳技巧:")
    print("  - ESP定律")
    print("  - 单步跟踪")
    print("  - 内存断点")
    
    print("\n爆破技巧:")
    print("  - 关键Call定位")
    print("  - 跳转修改")
    print("  - 返回值修改")
    
    print("\n注册码分析:")
    print("  - 字符串搜索")
    print("  - 断点设置")
    print("  - 算法分析")
    
    print("\n反调试绕过:")
    print("  - IsDebuggerPresent")
    print("  - NtGlobalFlag")
    print("  - 时间检测")


def limitations():
    """局限性"""
    print("\n--- 5. 局限性 ---")
    
    print("32位限制:")
    print("  - 仅支持32位")
    print("  - 不支持64位")
    print("  - 需要替代方案")
    
    print("\n系统兼容:")
    print("  - Windows XP最佳")
    print("  - Windows 7兼容")
    print("  - Windows 10问题")
    
    print("\n功能限制:")
    print("  - 功能有限")
    print("  - 插件依赖")
    print("  - 更新停止")
    
    print("\n替代方案:")
    print("  - x64dbg")
    print("  - WinDbg")
    print("  - IDA调试")


if __name__ == "__main__":
    print("=== OllyDbg调试器使用示例 ===")
    
    ollydbg_overview()
    debug_features()
    plugin_system()
    debugging_techniques()
    limitations()
