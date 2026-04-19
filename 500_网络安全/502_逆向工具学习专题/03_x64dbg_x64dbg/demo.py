#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
x64dbg调试器使用示例
演示x64dbg的基本使用、调试功能、断点和插件
"""

from datetime import datetime

class X64DbgDemo:
    """x64dbg使用示例类"""
    
    def __init__(self):
        """初始化x64dbg示例"""
        print("=== x64dbg调试器使用示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def x64dbg_overview(self):
        """x64dbg概述"""
        print("\n--- 1. x64dbg概述 ---")
        
        print("x64dbg介绍:")
        print("  - 开源调试器: 免费开源的Windows调试器")
        print("  - 32/64位支持: 同时支持32位和64位程序调试")
        print("  - 活跃开发: 持续更新和改进")
        print("  - 插件支持: 丰富的插件生态系统")
        print("  - 脚本支持: 支持x64dbg脚本和Python脚本")
        
        print("\nx64dbg安装:")
        print("  - 下载安装包: 从官方网站下载最新版本")
        print("  - 解压安装: 解压到任意目录即可使用")
        print("  - 配置环境: 无需特殊配置，直接运行")
        print("  - 依赖项: 可能需要安装Visual C++ Redistributable")
        
        print("\nx64dbg界面:")
        print("  - CPU窗口: 显示反汇编代码和执行状态")
        print("  - 内存窗口: 显示程序内存内容")
        print("  - 寄存器窗口: 显示CPU寄存器状态")
        print("  - 堆栈窗口: 显示程序堆栈内容")
        print("  - 断点窗口: 显示设置的断点")
        print("  - 模块窗口: 显示加载的模块")
        
        print("\nx64dbg配置:")
        print("  - 外观配置: 主题、颜色、字体等")
        print("  - 调试配置: 调试选项、异常处理等")
        print("  - 插件配置: 插件加载、设置等")
        print("  - 快捷键配置: 自定义快捷键")
    
    def debug_features(self):
        """调试功能"""
        print("\n--- 2. 调试功能 ---")
        
        print("附加进程:")
        print("  - 附加运行进程: 通过进程列表选择要附加的进程")
        print("  - 暂停进程: 暂停正在运行的进程")
        print("  - 分离进程: 与进程分离，不终止进程")
        print("  - 启动新进程: 直接启动并调试新进程")
        
        print("\n运行控制:")
        print("  - 运行: F9，继续执行程序")
        print("  - 暂停: F12，暂停程序执行")
        print("  - 停止: Shift+F2，终止程序执行")
        print("  - 重新启动: Ctrl+F2，重新启动程序")
        
        print("\n单步执行:")
        print("  - Step Into: F7，单步进入函数")
        print("  - Step Over: F8，单步跳过函数")
        print("  - Step Out: Ctrl+F9，从函数中跳出")
        print("  - Run to Cursor: F4，运行到光标位置")
        
        print("\n内存查看:")
        print("  - 内存Dump: 查看内存内容")
        print("  - 内存搜索: 搜索内存中的特定值")
        print("  - 内存修改: 修改内存中的值")
        print("  - 内存断点: 设置内存访问断点")
        print("  - 内存映射: 查看内存映射情况")
    
    def breakpoint_features(self):
        """断点功能"""
        print("\n--- 3. 断点功能 ---")
        
        print("软件断点:")
        print("  - INT 3指令: 使用INT 3指令实现")
        print("  - 无限数量: 可以设置任意数量的软件断点")
        print("  - F2设置: 按F2在当前位置设置断点")
        print("  - 容易被检测: 可能被反调试检测到")
        
        print("\n硬件断点:")
        print("  - DR0-DR7寄存器: 使用CPU的调试寄存器")
        print("  - 最多4个: 受限于CPU调试寄存器数量")
        print("  - 执行/读写断点: 可以设置执行、读取或写入断点")
        print("  - 不易被检测: 相对软件断点更难被检测")
        
        print("\n内存断点:")
        print("  - 内存访问断点: 当内存被访问时触发")
        print("  - 内存写入断点: 当内存被写入时触发")
        print("  - 内存执行断点: 当内存被执行时触发")
        print("  - 基于内存保护: 通过修改内存保护属性实现")
        
        print("\n条件断点:")
        print("  - 条件触发: 当满足特定条件时才触发")
        print("  - 计数断点: 当断点被命中指定次数后触发")
        print("  - 日志断点: 记录断点命中情况但不中断执行")
        print("  - 命令断点: 命中时执行指定命令")
    
    def plugin_system(self):
        """插件系统"""
        print("\n--- 4. 插件系统 ---")
        
        print("插件安装:")
        print("  - plugins目录: 将插件文件放入plugins目录")
        print("  - 重启生效: 重启x64dbg后插件生效")
        print("  - 插件管理: 在插件菜单中管理插件")
        print("  - 依赖项: 某些插件可能需要特定依赖项")
        
        print("\n插件开发:")
        print("  - SDK: 使用x64dbg SDK开发插件")
        print("  - API: 提供丰富的API接口")
        print("  - 示例代码: 提供插件开发示例")
        print("  - 语言支持: 支持C/C++开发插件")
        
        print("\n常用插件:")
        print("  - x64dbgpy: Python脚本支持插件")
        print("  - ScyllaHide: 反反调试插件，隐藏调试器特征")
        print("  - TitanHide: 另一个反反调试插件")
        print("  - xAnalyzer: 静态分析插件")
        print("  - MonoLoader: .NET程序调试插件")
        
        print("\n插件配置:")
        print("  - 插件设置: 插件的具体配置选项")
        print("  - 快捷键: 插件可能添加新的快捷键")
        print("  - 自动加载: 配置插件是否自动加载")
        print("  - 插件间通信: 插件之间的通信机制")
    
    def advanced_features(self):
        """高级功能"""
        print("\n--- 5. 高级功能 ---")
        
        print("脚本支持:")
        print("  - x64dbg脚本: 使用x64dbg内置脚本语言")
        print("  - 自动化操作: 自动化重复的调试操作")
        print("  - 批处理: 批量执行多个操作")
        print("  - Python脚本: 通过x64dbgpy插件支持Python脚本")
        
        print("\n主题定制:")
        print("  - 主题切换: 内置多种主题")
        print("  - 颜色配置: 自定义各种元素的颜色")
        print("  - 字体配置: 自定义字体和字号")
        print("  - 布局配置: 自定义窗口布局")
        
        print("\n快捷键:")
        print("  - 默认快捷键: 内置的默认快捷键")
        print("  - 自定义快捷键: 根据个人习惯修改")
        print("  - 快捷键冲突: 解决快捷键冲突")
        print("  - 快捷键提示: 显示快捷键提示")
        
        print("\n导出功能:")
        print("  - 导出Dump: 导出内存Dump")
        print("  - 导出日志: 导出调试日志")
        print("  - 导出配置: 导出x64dbg配置")
        print("  - 导出反汇编: 导出反汇编代码")
    
    def debugging_workflow(self):
        """调试工作流程"""
        print("\n--- 6. 调试工作流程 ---")
        
        print("基本调试流程:")
        print("  1. 启动x64dbg")
        print("  2. 打开或附加目标程序")
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
        print("  - 使用条件断点: 减少不必要的中断")
        print("  - 利用日志断点: 记录程序行为")
        print("  - 结合静态分析: 先静态分析，再动态调试")
        print("  - 使用插件: 利用插件提高效率")
    
    def anti_debugging(self):
        """反调试技术"""
        print("\n--- 7. 反调试技术 ---")
        
        print("常见反调试技术:")
        print("  - 检测调试器存在: 使用API检测调试器")
        print("  - 时间检测: 检测执行时间异常")
        print("  - 内存检测: 检测内存布局异常")
        print("  - 异常检测: 检测异常处理异常")
        
        print("\n反调试绕过:")
        print("  - 使用ScyllaHide: 自动隐藏调试器特征")
        print("  - 手动补丁: 补丁反调试代码")
        print("  - 硬件断点: 使用硬件断点避免被检测")
        print("  - 模拟器: 使用模拟器运行恶意代码")
    
    def practical_tips(self):
        """实用技巧"""
        print("\n--- 8. 实用技巧 ---")
        
        print("快捷键:")
        print("  - F2: 设置/清除断点")
        print("  - F7: 单步进入")
        print("  - F8: 单步跳过")
        print("  - F9: 运行")
        print("  - F12: 暂停")
        print("  - Ctrl+F2: 重新启动")
        print("  - Ctrl+F9: 单步跳出")
        print("  - F4: 运行到光标")
        print("  - Ctrl+G: 跳转到地址")
        print("  - Ctrl+B: 二进制搜索")
        
        print("\n调试技巧:")
        print("  - 从入口点开始: 了解程序启动流程")
        print("  - 跟踪API调用: 了解程序与系统的交互")
        print("  - 分析内存操作: 了解数据处理逻辑")
        print("  - 使用条件断点: 精确定位关键代码")
        print("  - 结合静态分析: 提高分析效率")
        
        print("\n性能优化:")
        print("  - 减少断点数量: 过多断点会影响性能")
        print("  - 使用日志断点: 避免频繁中断")
        print("  - 合理使用硬件断点: 硬件断点比软件断点快")
        print("  - 关闭不必要的窗口: 减少内存使用")
        print("  - 定期保存配置: 避免配置丢失")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.x64dbg_overview()
            self.debug_features()
            self.breakpoint_features()
            self.plugin_system()
            self.advanced_features()
            self.debugging_workflow()
            self.anti_debugging()
            self.practical_tips()
            
            print("\n" + "=" * 80)
            print("x64dbg调试器使用示例演示完成！")
            print("通过本演示，您了解了x64dbg的基本功能、调试技术、断点设置和插件系统等内容。")
            print("这些知识将帮助您更有效地使用x64dbg进行逆向工程和调试分析。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = X64DbgDemo()
    demo.run_demo()

