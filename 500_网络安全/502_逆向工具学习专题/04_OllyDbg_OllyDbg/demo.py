#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OllyDbg调试器使用示例
演示OllyDbg的基本使用、调试功能、插件和技巧
"""

from datetime import datetime

class OllyDbgDemo:
    """OllyDbg使用示例类"""
    
    def __init__(self):
        """初始化OllyDbg示例"""
        print("=== OllyDbg调试器使用示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def ollydbg_overview(self):
        """OllyDbg概述"""
        print("\n--- 1. OllyDbg概述 ---")
        
        print("OllyDbg介绍:")
        print("  - 32位调试器: 专注于32位程序调试的经典工具")
        print("  - 用户友好: 界面简洁直观，易于上手")
        print("  - 插件丰富: 拥有大量第三方插件，扩展功能")
        print("  - 免费使用: 免费软件，广泛应用于逆向工程")
        print("  - 历史悠久: 经典调试器，被广泛使用和研究")
        
        print("\nOllyDbg版本:")
        print("  - OllyDbg 1.10: 经典版本，最广泛使用")
        print("  - OllyDbg 2.01: 后续版本，功能更丰富")
        print("  - OllyICE: 社区修改版，增强功能")
        
        print("\nOllyDbg安装:")
        print("  - 下载安装包: 从官方网站或可信来源下载")
        print("  - 解压安装: 解压到任意目录即可使用")
        print("  - 配置环境: 无需特殊配置，直接运行ollydbg.exe")
        print("  - 插件目录: 插件放在Plugins目录中")
        
        print("\nOllyDbg界面:")
        print("  - CPU窗口: 显示反汇编代码和执行状态")
        print("  - 内存窗口: 显示程序内存内容")
        print("  - 寄存器窗口: 显示CPU寄存器状态")
        print("  - 堆栈窗口: 显示程序堆栈内容")
        print("  - 断点窗口: 显示设置的断点")
        print("  - 模块窗口: 显示加载的模块")
        print("  - 信息窗口: 显示调试信息和日志")
        
        print("\nOllyDbg配置:")
        print("  - 外观配置: 颜色、字体、布局等")
        print("  - 调试配置: 调试选项、异常处理等")
        print("  - 插件配置: 插件加载、设置等")
        print("  - 快捷键配置: 自定义快捷键")
    
    def debug_features(self):
        """调试功能"""
        print("\n--- 2. 调试功能 ---")
        
        print("加载程序:")
        print("  - 打开文件: File -> Open选择可执行文件")
        print("  - 附加进程: File -> Attach选择运行中的进程")
        print("  - 命令行参数: 设置程序启动参数")
        print("  - 环境变量: 设置程序运行环境")
        
        print("\n运行控制:")
        print("  - 运行: F9，继续执行程序")
        print("  - 暂停: F12，暂停程序执行")
        print("  - 停止: Ctrl+F2，终止程序执行")
        print("  - 重新启动: Ctrl+F2，重新加载程序")
        
        print("\n单步执行:")
        print("  - Step Into: F7，单步进入函数")
        print("  - Step Over: F8，单步跳过函数")
        print("  - Step Out: Ctrl+F9，从函数中跳出")
        print("  - Run to Cursor: F4，运行到光标位置")
        
        print("\n断点设置:")
        print("  - 软件断点: F2，在当前位置设置断点")
        print("  - 条件断点: 右键->Breakpoint->Condition设置条件")
        print("  - 内存断点: 右键->Breakpoint->Memory, on access/write")
        print("  - 硬件断点: 右键->Breakpoint->Hardware, on execution/access/write")
        
        print("\n内存操作:")
        print("  - 内存Dump: 查看内存内容")
        print("  - 内存搜索: 搜索内存中的特定值")
        print("  - 内存修改: 修改内存中的值")
        print("  - 内存复制: 复制内存内容到其他位置")
        print("  - 内存填充: 用特定值填充内存区域")
    
    def plugin_system(self):
        """插件系统"""
        print("\n--- 3. 插件系统 ---")
        
        print("插件安装:")
        print("  - 插件目录: 将插件文件放入Plugins目录")
        print("  - 重启生效: 重启OllyDbg后插件生效")
        print("  - 插件管理: 通过Plugins菜单管理插件")
        print("  - 插件顺序: 可调整插件加载顺序")
        
        print("\n常用插件:")
        print("  - OllyDump: 用于脱壳和内存转储")
        print("  - HideDebugger: 隐藏调试器，绕过反调试")
        print("  - CommandBar: 添加命令栏，方便执行命令")
        print("  - OllyScript: 支持脚本自动化操作")
        print("  - StrongOD: 增强OllyDbg功能，提供更多调试选项")
        print("  - LordPE: PE文件编辑工具")
        print("  - ImportREC: 导入表恢复工具")
        
        print("\n插件开发:")
        print("  - SDK: 使用OllyDbg SDK开发插件")
        print("  - API: 提供丰富的API接口")
        print("  - 示例代码: SDK中包含插件开发示例")
        print("  - 语言支持: 主要支持C/C++开发插件")
        
        print("\n插件配置:")
        print("  - 插件设置: 插件的具体配置选项")
        print("  - 快捷键: 插件可能添加新的快捷键")
        print("  - 自动加载: 配置插件是否自动加载")
        print("  - 插件间通信: 插件之间的通信机制")
    
    def debugging_techniques(self):
        """调试技巧"""
        print("\n--- 4. 调试技巧 ---")
        
        print("脱壳技巧:")
        print("  - ESP定律: 利用ESP寄存器定位OEP")
        print("  - 单步跟踪: 逐步跟踪脱壳过程")
        print("  - 内存断点: 在内存写入处设置断点")
        print("  - 硬件断点: 在可疑地址设置硬件执行断点")
        print("  - 段首断点: 在代码段首设置断点")
        
        print("\n爆破技巧:")
        print("  - 关键Call定位: 定位注册验证函数")
        print("  - 跳转修改: 修改条件跳转指令")
        print("  - 返回值修改: 修改函数返回值")
        print("  - 字符串搜索: 搜索错误提示字符串")
        print("  - 内存搜索: 搜索注册码相关数据")
        
        print("\n注册码分析:")
        print("  - 字符串搜索: 搜索注册码相关字符串")
        print("  - 断点设置: 在关键函数处设置断点")
        print("  - 算法分析: 分析注册码生成算法")
        print("  - 内存监控: 监控注册码验证过程")
        print("  - 反汇编分析: 分析注册码验证逻辑")
        
        print("\n反调试绕过:")
        print("  - IsDebuggerPresent: 补丁该API调用")
        print("  - NtGlobalFlag: 修改PEB中的NtGlobalFlag")
        print("  - 时间检测: 补丁时间检测代码")
        print("  - 异常检测: 处理异常检测代码")
        print("  - 硬件断点检测: 避免使用硬件断点")
    
    def advanced_usage(self):
        """高级用法"""
        print("\n--- 5. 高级用法 ---")
        
        print("脚本使用:")
        print("  - OllyScript: 使用OllyScript脚本自动化操作")
        print("  - 脚本语法: 了解OllyScript脚本语法")
        print("  - 脚本示例: 使用内置脚本示例")
        print("  - 自定义脚本: 根据需要编写自定义脚本")
        
        print("\n内存操作:")
        print("  - 内存映射: 查看内存映射情况")
        print("  - 内存保护: 修改内存保护属性")
        print("  - 内存分配: 分配新的内存区域")
        print("  - 内存释放: 释放内存区域")
        
        print("\n寄存器操作:")
        print("  - 寄存器修改: 修改寄存器值")
        print("  - 寄存器跟踪: 跟踪寄存器值变化")
        print("  - 标志位操作: 修改标志寄存器值")
        
        print("\n反汇编操作:")
        print("  - 代码分析: 分析反汇编代码")
        print("  - 代码修改: 修改反汇编代码")
        print("  - 代码注释: 添加代码注释")
        print("  - 函数识别: 识别函数边界")
    
    def limitations(self):
        """局限性"""
        print("\n--- 6. 局限性 ---")
        
        print("32位限制:")
        print("  - 仅支持32位: 不支持64位程序调试")
        print("  - 内存限制: 受32位地址空间限制")
        print("  - 需要替代方案: 64位程序需要使用其他调试器")
        
        print("\n系统兼容性:")
        print("  - Windows XP: 最佳支持")
        print("  - Windows 7: 基本兼容")
        print("  - Windows 10: 可能存在问题")
        print("  - Windows 11: 兼容性较差")
        
        print("\n功能限制:")
        print("  - 功能有限: 相比现代调试器功能较少")
        print("  - 插件依赖: 很多功能依赖插件")
        print("  - 更新停止: 官方更新已经停止")
        print("  - 界面老旧: 用户界面相对老旧")
        
        print("\n替代方案:")
        print("  - x64dbg: 支持32位和64位，开源活跃")
        print("  - WinDbg: Microsoft官方调试器，功能强大")
        print("  - IDA Pro: 集成调试器，功能全面")
        print("  - GDB: 跨平台调试器，支持多种架构")
    
    def practical_tips(self):
        """实用技巧"""
        print("\n--- 7. 实用技巧 ---")
        
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
        print("  - Ctrl+F: 文本搜索")
        print("  - Ctrl+E: 编辑当前指令")
        
        print("\n调试技巧:")
        print("  - 从入口点开始: 了解程序启动流程")
        print("  - 跟踪API调用: 了解程序与系统的交互")
        print("  - 分析内存操作: 了解数据处理逻辑")
        print("  - 使用条件断点: 精确定位关键代码")
        print("  - 结合静态分析: 提高分析效率")
        print("  - 记录执行流程: 使用日志功能记录执行过程")
        
        print("\n性能优化:")
        print("  - 减少断点数量: 过多断点会影响性能")
        print("  - 使用条件断点: 避免不必要的中断")
        print("  - 关闭不必要的窗口: 减少内存使用")
        print("  - 定期保存配置: 避免配置丢失")
        
        print("\n常见问题:")
        print("  - 程序崩溃: 检查异常处理设置")
        print("  - 断点不触发: 检查断点设置是否正确")
        print("  - 插件加载失败: 检查插件兼容性")
        print("  - 系统兼容性: 在兼容的Windows版本上运行")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.ollydbg_overview()
            self.debug_features()
            self.plugin_system()
            self.debugging_techniques()
            self.advanced_usage()
            self.limitations()
            self.practical_tips()
            
            print("\n" + "=" * 80)
            print("OllyDbg调试器使用示例演示完成！")
            print("通过本演示，您了解了OllyDbg的基本功能、调试技术、插件系统和高级用法等内容。")
            print("虽然OllyDbg有一些局限性，但它仍然是一款经典的调试器，在32位程序分析中仍然有用。")
            print("对于64位程序，建议使用x64dbg等现代调试器。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = OllyDbgDemo()
    demo.run_demo()

