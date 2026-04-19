#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试技术示例
演示断点技术、单步执行、内存调试、API调试和反调试绕过
"""

from datetime import datetime

class DebuggingTechniquesDemo:
    """调试技术示例类"""
    
    def __init__(self):
        """初始化调试技术示例"""
        print("=== 调试技术示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def breakpoint_techniques(self):
        """断点技术"""
        print("\n--- 1. 断点技术 ---")
        
        print("软件断点:")
        print("  - 实现原理: 使用INT 3指令 (0xCC)替换目标地址的指令")
        print("  - 数量限制: 无数量限制，可以设置任意数量的软件断点")
        print("  - 特点: 修改代码，容易被反调试检测到")
        print("  - 设置方法: 在调试器中按F2或使用命令设置")
        print("  - 适用场景: 一般调试，不需要隐藏调试器的情况")
        
        print("\n硬件断点:")
        print("  - 实现原理: 使用CPU的DR0-DR7调试寄存器")
        print("  - 数量限制: 最多只能设置4个硬件断点")
        print("  - 特点: 不修改代码，不易被反调试检测到")
        print("  - 设置方法: 在调试器中右键选择Hardware Breakpoint")
        print("  - 适用场景: 反调试检测较严的程序，需要隐藏调试器的情况")
        
        print("\n内存断点:")
        print("  - 内存访问断点: 当内存被访问时触发")
        print("  - 内存写入断点: 当内存被写入时触发")
        print("  - 内存执行断点: 当内存被执行时触发")
        print("  - 实现原理: 通过修改内存页的保护属性实现")
        print("  - 特点: 可以监控内存区域的访问情况")
        print("  - 适用场景: 监控变量变化、跟踪内存操作等")
        
        print("\n条件断点:")
        print("  - 条件触发: 当满足特定条件时才触发断点")
        print("  - 计数断点: 当断点被命中指定次数后才触发")
        print("  - 日志断点: 记录断点命中情况但不中断执行")
        print("  - 命令断点: 命中时执行指定命令")
        print("  - 适用场景: 精确定位关键代码，减少不必要的中断")
    
    def single_step_execution(self):
        """单步执行"""
        print("\n--- 2. 单步执行 ---")
        
        print("Step Into (F7):")
        print("  - 功能: 单步进入函数，跟踪到函数内部")
        print("  - 适用场景: 需要深入分析函数内部逻辑")
        print("  - 特点: 执行速度较慢，但分析详细")
        print("  - 注意事项: 可能会进入系统库函数，需要手动跳过")
        
        print("\nStep Over (F8):")
        print("  - 功能: 单步跳过函数，不进入函数内部")
        print("  - 适用场景: 快速执行，不需要分析函数内部")
        print("  - 特点: 执行速度较快，跳过函数调用")
        print("  - 注意事项: 无法看到函数内部的执行过程")
        
        print("\nStep Out (Ctrl+F9):")
        print("  - 功能: 从当前函数中跳出，执行到函数返回")
        print("  - 适用场景: 已经分析完函数内部，需要查看函数返回值")
        print("  - 特点: 快速执行到函数结束")
        print("  - 注意事项: 会执行函数剩余的所有代码")
        
        print("\nRun to Cursor (F4):")
        print("  - 功能: 执行到光标位置，临时设置断点")
        print("  - 适用场景: 快速定位到目标代码位置")
        print("  - 特点: 执行速度快，自动清除临时断点")
        print("  - 注意事项: 光标位置必须是有效的代码地址")
        
        print("\n单步跟踪技巧:")
        print("  - 结合断点: 使用断点和单步执行相结合")
        print("  - 跳过系统库: 对系统库函数使用Step Over")
        print("  - 记录执行路径: 使用日志功能记录执行过程")
        print("  - 分析寄存器变化: 观察寄存器值的变化")
    
    def memory_debugging(self):
        """内存调试"""
        print("\n--- 3. 内存调试 ---")
        
        print("内存查看:")
        print("  - 内存Dump: 查看内存内容，支持多种格式")
        print("  - 内存查看器: 实时查看内存变化")
        print("  - 内存分析: 分析内存布局和使用情况")
        print("  - 适用场景: 分析数据结构、查找关键数据等")
        
        print("\n内存搜索:")
        print("  - 字符串搜索: 搜索ASCII或Unicode字符串")
        print("  - 特征码搜索: 搜索特定的字节序列")
        print("  - 模式搜索: 搜索符合特定模式的数据")
        print("  - 适用场景: 查找关键数据、定位代码位置等")
        
        print("\n内存修改:")
        print("  - 变量修改: 修改程序变量的值")
        print("  - 代码修改: 修改程序代码，测试不同执行路径")
        print("  - 标志修改: 修改标志位，影响程序执行")
        print("  - 适用场景: 测试程序行为、绕过验证等")
        
        print("\n内存断点:")
        print("  - 访问断点: 当内存被读取或写入时触发")
        print("  - 写入断点: 当内存被写入时触发")
        print("  - 执行断点: 当内存被执行时触发")
        print("  - 适用场景: 监控内存访问、跟踪数据变化等")
        
        print("\n内存操作技巧:")
        print("  - 内存映射: 了解内存布局，避免访问无效内存")
        print("  - 内存保护: 修改内存保护属性，测试内存访问")
        print("  - 内存复制: 备份和恢复内存内容")
        print("  - 内存填充: 用特定值填充内存区域")
    
    def api_debugging(self):
        """API调试"""
        print("\n--- 4. API调试 ---")
        
        print("API断点:")
        print("  - 导入函数断点: 在程序导入的API函数处设置断点")
        print("  - 系统DLL断点: 在系统DLL的函数处设置断点")
        print("  - 自定义DLL断点: 在自定义DLL的函数处设置断点")
        print("  - 适用场景: 跟踪程序与系统的交互，分析API调用")
        
        print("\nAPI参数分析:")
        print("  - 栈参数: 通过栈查看函数参数")
        print("  - 寄存器参数: 通过寄存器查看函数参数（如x64调用约定）")
        print("  - 结构体参数: 分析结构体参数的内容")
        print("  - 适用场景: 了解API调用的具体参数，分析程序行为")
        
        print("\nAPI返回值分析:")
        print("  - EAX返回值: 查看EAX寄存器中的返回值（x86）")
        print("  - 成功/失败: 判断API调用是否成功")
        print("  - 错误码: 分析API调用失败的原因")
        print("  - 适用场景: 了解API调用的结果，分析程序错误处理")
        
        print("\nAPI Hook:")
        print("  - IAT Hook: 修改导入地址表，拦截API调用")
        print("  - Inline Hook: 修改API函数开头，拦截API调用")
        print("  - EAT Hook: 修改导出地址表，拦截API调用")
        print("  - 适用场景: 监控API调用、修改API行为等")
        
        print("\n常用API断点:")
        print("  - 文件操作: CreateFile, ReadFile, WriteFile")
        print("  - 网络操作: socket, connect, send, recv")
        print("  - 注册表操作: RegOpenKey, RegSetValue")
        print("  - 进程操作: CreateProcess, OpenProcess")
    
    def anti_debug_bypass(self):
        """反调试绕过"""
        print("\n--- 5. 反调试绕过 ---")
        
        print("调试器检测技术:")
        print("  - IsDebuggerPresent: 检查进程是否被调试")
        print("  - CheckRemoteDebuggerPresent: 检查远程进程是否被调试")
        print("  - NtQueryInformationProcess: 查询进程信息，检测调试器")
        print("  - PEB标志检测: 检查PEB中的调试标志")
        print("  - 窗口检测: 检测调试器窗口")
        
        print("\n时间检测技术:")
        print("  - GetTickCount: 检测代码执行时间")
        print("  - QueryPerformanceCounter: 高精度时间检测")
        print("  - RDTSC指令: 读取时间戳计数器")
        print("  - 适用场景: 检测调试器导致的执行时间延长")
        
        print("\n异常检测技术:")
        print("  - SEH检测: 结构化异常处理检测")
        print("  - 异常处理: 检测异常处理是否被调试器接管")
        print("  - 异常利用: 使用异常来检测调试器")
        print("  - 适用场景: 检测调试器对异常的处理")
        
        print("\n虚拟机检测技术:")
        print("  - 进程名检测: 检测虚拟机进程")
        print("  - 注册表检测: 检测虚拟机注册表项")
        print("  - 硬件检测: 检测虚拟机硬件特征")
        print("  - 磁盘检测: 检测虚拟机磁盘特征")
        
        print("\n反调试绕过方法:")
        print("  - 补丁检测函数: 修改检测函数，使其返回false")
        print("  - 使用插件: 使用ScyllaHide等插件隐藏调试器")
        print("  - 硬件断点: 使用硬件断点避免被检测")
        print("  - 手动修改: 修改检测代码的结果")
        print("  - 模拟器: 使用模拟器运行恶意代码")
    
    def debugging_workflow(self):
        """调试工作流程"""
        print("\n--- 6. 调试工作流程 ---")
        
        print("基本调试流程:")
        print("  1. 启动调试器")
        print("  2. 加载目标程序")
        print("  3. 设置断点")
        print("  4. 运行程序")
        print("  5. 分析程序行为")
        print("  6. 修改和测试")
        print("  7. 导出分析结果")
        
        print("\n常见调试场景:")
        print("  - 破解软件: 找到注册验证代码")
        print("  - 分析恶意代码: 了解恶意行为")
        print("  - 调试漏洞: 分析漏洞触发条件")
        print("  - 学习程序: 了解程序工作原理")
        
        print("\n调试技巧:")
        print("  - 从入口点开始: 了解程序启动流程")
        print("  - 跟踪API调用: 了解程序与系统的交互")
        print("  - 分析内存操作: 了解数据处理逻辑")
        print("  - 使用条件断点: 精确定位关键代码")
        print("  - 结合静态分析: 提高分析效率")
    
    def advanced_debugging(self):
        """高级调试技术"""
        print("\n--- 7. 高级调试技术 ---")
        
        print("脚本调试:")
        print("  - 使用调试器脚本: 自动化调试操作")
        print("  - Python脚本: 使用Python进行调试自动化")
        print("  - 自定义命令: 编写自定义调试命令")
        print("  - 适用场景: 重复的调试操作，复杂的分析任务")
        
        print("\n多线程调试:")
        print("  - 线程切换: 在多线程程序中切换线程")
        print("  - 线程断点: 在特定线程上设置断点")
        print("  - 线程同步: 分析线程同步问题")
        print("  - 适用场景: 多线程程序的调试和分析")
        
        print("\n内核调试:")
        print("  - WinDbg内核调试: 调试内核模式代码")
        print("  - 驱动调试: 调试设备驱动程序")
        print("  - 系统调用: 分析系统调用")
        print("  - 适用场景: 内核级代码的调试和分析")
        
        print("\n远程调试:")
        print("  - 远程调试设置: 配置远程调试环境")
        print("  - 远程断点: 在远程进程上设置断点")
        print("  - 远程内存: 访问远程进程内存")
        print("  - 适用场景: 调试远程机器上的程序")
    
    def practical_tips(self):
        """实用技巧"""
        print("\n--- 8. 实用技巧 ---")
        
        print("调试器选择:")
        print("  - 32位程序: OllyDbg, x64dbg (32位模式)")
        print("  - 64位程序: x64dbg, WinDbg")
        print("  - 内核调试: WinDbg")
        print("  - 跨平台: GDB")
        
        print("\n调试效率提升:")
        print("  - 合理设置断点: 只设置必要的断点")
        print("  - 使用条件断点: 减少不必要的中断")
        print("  - 利用日志功能: 记录执行过程")
        print("  - 结合静态分析: 先静态分析，再动态调试")
        print("  - 使用插件: 利用插件提高效率")
        
        print("\n常见问题解决:")
        print("  - 程序崩溃: 检查异常处理设置")
        print("  - 断点不触发: 检查断点设置是否正确")
        print("  - 调试器被检测: 使用反反调试插件")
        print("  - 内存访问错误: 检查内存布局和访问权限")
        print("  - 性能问题: 减少断点数量，使用日志断点")
        
        print("\n调试安全注意事项:")
        print("  - 隔离环境: 在隔离环境中调试恶意代码")
        print("  - 备份数据: 调试前备份重要数据")
        print("  - 网络隔离: 调试恶意代码时断开网络")
        print("  - 使用虚拟机: 在虚拟机中进行调试")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.breakpoint_techniques()
            self.single_step_execution()
            self.memory_debugging()
            self.api_debugging()
            self.anti_debug_bypass()
            self.debugging_workflow()
            self.advanced_debugging()
            self.practical_tips()
            
            print("\n" + "=" * 80)
            print("调试技术示例演示完成！")
            print("通过本演示，您了解了断点技术、单步执行、内存调试、API调试和反调试绕过等内容。")
            print("这些调试技术是逆向工程和恶意代码分析的重要工具，掌握它们将帮助您更有效地分析程序。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = DebuggingTechniquesDemo()
    demo.run_demo()

