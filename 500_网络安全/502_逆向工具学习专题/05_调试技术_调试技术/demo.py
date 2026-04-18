#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试技术示例
演示断点技术、单步执行、内存调试、API调试和反调试绕过
"""


def breakpoint_techniques():
    """断点技术"""
    print("\n--- 1. 断点技术 ---")
    
    print("软件断点:")
    print("  - INT 3指令 (0xCC)")
    print("  - 无限数量")
    print("  - 修改代码")
    
    print("\n硬件断点:")
    print("  - DR0-DR7调试寄存器")
    print("  - 最多4个断点")
    print("  - 不修改代码")
    
    print("\n内存断点:")
    print("  - 内存访问断点")
    print("  - 内存写入断点")
    print("  - 内存执行断点")
    
    print("\n条件断点:")
    print("  - 条件触发")
    print("  - 计数断点")
    print("  - 日志断点")


def single_step_execution():
    """单步执行"""
    print("\n--- 2. 单步执行 ---")
    
    print("Step Into (F7):")
    print("  - 进入函数")
    print("  - 深入分析")
    print("  - 详细跟踪")
    
    print("\nStep Over (F8):")
    print("  - 跳过函数")
    print("  - 快速执行")
    print("  - 函数返回")
    
    print("\nStep Out (Ctrl+F9):")
    print("  - 执行到返回")
    print("  - 跳出函数")
    print("  - 查看返回值")
    
    print("\nRun to Cursor:")
    print("  - 执行到光标")
    print("  - 快速定位")
    print("  - 临时断点")


def memory_debugging():
    """内存调试"""
    print("\n--- 3. 内存调试 ---")
    
    print("内存查看:")
    print("  - 内存Dump")
    print("  - 内存查看器")
    print("  - 内存分析")
    
    print("\n内存搜索:")
    print("  - 字符串搜索")
    print("  - 特征码搜索")
    print("  - 模式搜索")
    
    print("\n内存修改:")
    print("  - 变量修改")
    print("  - 代码修改")
    print("  - 标志修改")
    
    print("\n内存断点:")
    print("  - 访问断点")
    print("  - 写入断点")
    print("  - 执行断点")


def api_debugging():
    """API调试"""
    print("\n--- 4. API调试 ---")
    
    print("API断点:")
    print("  - 导入函数断点")
    print("  - 系统DLL断点")
    print("  - 自定义DLL断点")
    
    print("\nAPI参数:")
    print("  - 栈参数")
    print("  - 寄存器参数")
    print("  - 结构体参数")
    
    print("\nAPI返回值:")
    print("  - EAX返回值")
    print("  - 成功/失败")
    print("  - 错误码")
    
    print("\nAPI Hook:")
    print("  - IAT Hook")
    print("  - Inline Hook")
    print("  - EAT Hook")


def anti_debug_bypass():
    """反调试绕过"""
    print("\n--- 5. 反调试绕过 ---")
    
    print("调试器检测:")
    print("  - IsDebuggerPresent")
    print("  - CheckRemoteDebuggerPresent")
    print("  - NtQueryInformationProcess")
    
    print("\n时间检测:")
    print("  - GetTickCount")
    print("  - QueryPerformanceCounter")
    print("  - RDTSC指令")
    
    print("\n异常检测:")
    print("  - SEH检测")
    print("  - 异常处理")
    print("  - 异常利用")
    
    print("\n虚拟机检测:")
    print("  - 进程名检测")
    print("  - 注册表检测")
    print("  - 硬件检测")


if __name__ == "__main__":
    print("=== 调试技术示例 ===")
    
    breakpoint_techniques()
    single_step_execution()
    memory_debugging()
    api_debugging()
    anti_debug_bypass()
