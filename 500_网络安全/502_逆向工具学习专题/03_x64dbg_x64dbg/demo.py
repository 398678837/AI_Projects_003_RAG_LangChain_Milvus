#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
x64dbg调试器使用示例
演示x64dbg的基本使用、调试功能、断点和插件
"""


def x64dbg_overview():
    """x64dbg概述"""
    print("\n--- 1. x64dbg概述 ---")
    
    print("x64dbg介绍:")
    print("  - 开源调试器")
    print("  - 32/64位支持")
    print("  - 活跃开发")
    
    print("\nx64dbg安装:")
    print("  - 下载安装包")
    print("  - 解压安装")
    print("  - 配置环境")
    
    print("\nx64dbg界面:")
    print("  - CPU窗口")
    print("  - 内存窗口")
    print("  - 寄存器窗口")
    
    print("\nx64dbg配置:")
    print("  - 外观配置")
    print("  - 调试配置")
    print("  - 插件配置")


def debug_features():
    """调试功能"""
    print("\n--- 2. 调试功能 ---")
    
    print("附加进程:")
    print("  - 附加运行进程")
    print("  - 暂停进程")
    print("  - 分离进程")
    
    print("\n运行控制:")
    print("  - 运行: F9")
    print("  - 暂停: F12")
    print("  - 停止: Shift+F2")
    
    print("\n单步执行:")
    print("  - Step Into: F7")
    print("  - Step Over: F8")
    print("  - Step Out: Ctrl+F9")
    
    print("\n内存查看:")
    print("  - 内存Dump")
    print("  - 内存搜索")
    print("  - 内存修改")


def breakpoint_features():
    """断点功能"""
    print("\n--- 3. 断点功能 ---")
    
    print("软件断点:")
    print("  - INT 3指令")
    print("  - 无限数量")
    print("  - F2设置")
    
    print("\n硬件断点:")
    print("  - DR0-DR7寄存器")
    print("  - 最多4个")
    print("  - 执行/读写断点")
    
    print("\n内存断点:")
    print("  - 内存访问断点")
    print("  - 内存写入断点")
    print("  - 内存执行断点")
    
    print("\n条件断点:")
    print("  - 条件触发")
    print("  - 计数断点")
    print("  - 日志断点")


def plugin_system():
    """插件系统"""
    print("\n--- 4. 插件系统 ---")
    
    print("插件安装:")
    print("  - plugins目录")
    print("  - 重启生效")
    print("  - 插件管理")
    
    print("\n插件开发:")
    print("  - SDK")
    print("  - API")
    print("  - 示例代码")
    
    print("\n常用插件:")
    print("  - x64dbgpy: Python脚本")
    print("  - ScyllaHide: 反反调试")
    print("  - TitanHide: 隐藏调试器")
    
    print("\n插件配置:")
    print("  - 插件设置")
    print("  - 快捷键")
    print("  - 自动加载")


def advanced_features():
    """高级功能"""
    print("\n--- 5. 高级功能 ---")
    
    print("脚本支持:")
    print("  - x64dbg脚本")
    print("  - 自动化操作")
    print("  - 批处理")
    
    print("\n主题定制:")
    print("  - 主题切换")
    print("  - 颜色配置")
    print("  - 字体配置")
    
    print("\n快捷键:")
    print("  - 默认快捷键")
    print("  - 自定义快捷键")
    print("  - 快捷键冲突")
    
    print("\n导出功能:")
    print("  - 导出Dump")
    print("  - 导出日志")
    print("  - 导出配置")


if __name__ == "__main__":
    print("=== x64dbg调试器使用示例 ===")
    
    x64dbg_overview()
    debug_features()
    breakpoint_features()
    plugin_system()
    advanced_features()
