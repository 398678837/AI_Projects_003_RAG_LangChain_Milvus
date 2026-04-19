#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
插件开发示例
演示插件开发基础、IDA插件开发、x64dbg插件开发和API
"""

from datetime import datetime

class PluginDevDemo:
    """插件开发示例类"""
    
    def __init__(self):
        """初始化插件开发示例"""
        print("=== 插件开发示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def plugin_development_basics(self):
        """插件开发基础"""
        print("\n--- 1. 插件开发基础 ---")
        
        print("插件概念:")
        print("  - 扩展功能: 为现有工具添加新功能")
        print("  - 自定义操作: 根据需求定制特定操作")
        print("  - 自动化任务: 自动执行重复性任务")
        print("  - 集成工具: 与其他工具集成，提高工作效率")
        
        print("\n插件架构:")
        print("  - 插件接口: 定义插件与主程序的交互方式")
        print("  - 插件生命周期: 插件的加载、初始化、运行和卸载")
        print("  - 插件通信: 插件之间的通信机制")
        print("  - 插件配置: 插件的配置和设置")
        
        print("\n插件开发语言:")
        print("  - Python: 简单易用，适合快速开发")
        print("  - C/C++: 性能高，适合复杂插件")
        print("  - IDC: IDA Pro内置脚本语言")
        print("  - Lua: 轻量级脚本语言，适合简单插件")
        
        print("\n插件开发工具:")
        print("  - IDE: Visual Studio, PyCharm, VS Code等")
        print("  - SDK: 各工具提供的插件开发SDK")
        print("  - 调试工具: 用于调试插件代码")
        print("  - 版本控制: Git等版本控制工具")
    
    def ida_plugin_development(self):
        """IDA插件开发"""
        print("\n--- 2. IDA插件开发 ---")
        
        print("IDAPython:")
        print("  - Python脚本: 使用Python开发IDA插件")
        print("  - IDA API: 提供丰富的API接口")
        print("  - 易于开发: 开发效率高，适合快速原型")
        print("  - 示例: 以下是一个简单的IDAPython插件示例:")
        print("    \n"""")
        print("    # IDAPython插件示例")
        print("    import idaapi")
        print("    ")
        print("    class MyPlugin(idaapi.plugin_t):")
        print("        flags = idaapi.PLUGIN_UNL")
        print("        comment = \"My first IDA plugin\"")
        print("        help = \"This is a help string\"")
        print("        wanted_name = \"My Plugin\"")
        print("        wanted_hotkey = \"Alt-F8\"")
        print("    ")
        print("        def init(self):")
        print("            print(\"My Plugin initialized\")")
        print("            return idaapi.PLUGIN_OK")
        print("    ")
        print("        def run(self, arg):")
        print("            print(\"My Plugin run\")")
        print("    ")
        print("        def term(self):")
        print("            print(\"My Plugin terminated\")")
        print("    ")
        print("    def PLUGIN_ENTRY():")
        print("        return MyPlugin()")
        print("    """)
        
        print("\nIDC脚本:")
        print("  - IDC语言: IDA Pro内置的脚本语言")
        print("  - 内置语言: 无需额外依赖")
        print("  - 兼容性好: 适用于不同版本的IDA Pro")
        print("  - 示例: 以下是一个简单的IDC脚本示例:")
        print("    \n"""")
        print("    // IDC脚本示例")
        print("    static main() {")
        print("        Message(\"Hello from IDC script!\n\");")
        print("        auto func = GetFunctionAttr(ScreenEA(), FUNCATTR_START);")
        print("        if (func != BADADDR) {")
        print("            Message(\"Current function: %s\n\", GetFunctionName(func));")
        print("        }")
        print("    }")
        print("    """)
        
        print("\n插件框架:")
        print("  - 插件类: 继承自idaapi.plugin_t")
        print("  - 插件方法: init(), run(), term()")
        print("  - 插件注册: 通过PLUGIN_ENTRY()函数注册")
        print("  - 插件信息: flags, comment, help, wanted_name, wanted_hotkey")
        
        print("\n插件API:")
        print("  - idaapi: 核心API，提供各种功能")
        print("  - idc: 高级API，封装了常用功能")
        print("  - idautils: 实用工具函数")
        print("  - ida_bytes: 字节操作相关API")
        print("  - ida_funcs: 函数操作相关API")
        print("  - ida_ida: IDA核心功能API")
    
    def x64dbg_plugin_development(self):
        """x64dbg插件开发"""
        print("\n--- 3. x64dbg插件开发 ---")
        
        print("SDK:")
        print("  - 插件SDK: x64dbg提供的插件开发SDK")
        print("  - 头文件: plugin.h, bridge.h等")
        print("  - 库文件: x32dbg.lib/x64dbg.lib")
        print("  - 开发环境: Visual Studio")
        
        print("\nAPI:")
        print("  - 调试API: 调试相关功能")
        print("  - UI API: 界面相关功能")
        print("  - 工具API: 工具相关功能")
        print("  - 插件API: 插件管理相关功能")
        
        print("\n插件框架:")
        print("  - 插件入口: DllMain()函数")
        print("  - 插件回调: CB_INITDEBUG, CB_STOPDEBUG等")
        print("  - 插件配置: 插件的配置和设置")
        print("  - 插件导出: 导出插件信息和回调函数")
        
        print("\n插件示例:")
        print("  - 示例代码: x64dbg SDK中的示例")
        print("  - 模板项目: 用于快速开始插件开发")
        print("  - 文档: x64dbg插件开发文档")
        print("  - 示例: 以下是一个简单的x64dbg插件示例:")
        print("    \n"""")
        print("    // x64dbg插件示例")
        print("    #include <Windows.h>")
        print("    #include <plugin.h>")
        print("    ")
        print("    // 插件信息")
        print("    PLUGIN_INFO pluginInfo = {")
        print("        sizeof(PLUGIN_INFO),")
        print("        PLUGIN_NAME, // 插件名称")
        print("        PLUGIN_VERSION, // 插件版本")
        print("        PLUGIN_AUTHOR, // 插件作者")
        print("        PLUGIN_DESCRIPTION, // 插件描述")
        print("        PLUGIN_FAMILY, // 插件家族")
        print("        0 // 插件标志")
        print("    };")
        print("    ")
        print("    // 插件回调函数")
        print("    static bool cbInitDebug(PLUG_CB_INITDEBUG* cbInfo)")
        print("    {")
        print("        _plugin_logprintf(\"Plugin initialized!\\n\");")
        print("        return true;")
        print("    }")
        print("    ")
        print("    // 插件导出函数")
        print("    extern \"C\" __declspec(dllexport) void CBMENUENTRY(CBTYPE cbType, PLUG_CB* cbInfo)")
        print("    {")
        print("        switch(cbType)")
        print("        {")
        print("        case CB_INITDEBUG:")
        print("            cbInitDebug((PLUG_CB_INITDEBUG*)cbInfo);")
        print("            break;")
        print("        // 其他回调...")
        print("        }")
        print("    }")
        print("    ")
        print("    // 插件信息导出")
        print("    extern \"C\" __declspec(dllexport) PLUGIN_INFO* PLUGIN_INFOProc()")
        print("    {")
        print("        return &pluginInfo;")
        print("    }")
        print("    """)
    
    def plugin_api(self):
        """插件API"""
        print("\n--- 4. 插件API ---")
        
        print("文件操作:")
        print("  - 文件读取: 读取文件内容")
        print("  - 文件写入: 写入文件内容")
        print("  - 文件分析: 分析文件结构和内容")
        print("  - 文件保存: 保存修改后的文件")
        print("  - 示例 (IDAPython):")
        print("    \n"""")
        print("    # 读取文件")
        print("    import idaapi")
        print("    file_path = idaapi.ask_file(0, \"*.exe\", \"Select file\")")
        print("    if file_path:")
        print("        with open(file_path, 'rb') as f:")
        print("            content = f.read()")
        print("        print(f\"File size: {len(content)} bytes\")")
        print("    """)
        
        print("\n内存操作:")
        print("  - 内存读取: 读取内存内容")
        print("  - 内存写入: 写入内存内容")
        print("  - 内存搜索: 搜索内存中的特定内容")
        print("  - 内存分配: 分配新的内存")
        print("  - 示例 (IDAPython):")
        print("    \n"""")
        print("    # 读取内存")
        print("    import idaapi")
        print("    addr = 0x10000000")
        print("    size = 0x100")
        print("    data = idaapi.get_bytes(addr, size)")
        print("    print(f\"Memory content: {data.hex()}")")
        print("    """)
        
        print("\n调试操作:")
        print("  - 断点设置: 设置各种类型的断点")
        print("  - 运行控制: 控制程序的运行")
        print("  - 寄存器操作: 读取和修改寄存器值")
        print("  - 堆栈操作: 读取和修改堆栈内容")
        print("  - 示例 (IDAPython):")
        print("    \n"""")
        print("    # 设置断点")
        print("    import idaapi")
        print("    addr = 0x10000000")
        print("    bpt = idaapi.add_bpt(addr)")
        print("    print(f\"Breakpoint set at: {hex(addr)}")")
        print("    """)
        
        print("\nUI操作:")
        print("  - 窗口创建: 创建自定义窗口")
        print("  - 菜单添加: 添加菜单项")
        print("  - 消息显示: 显示消息框")
        print("  - 图标设置: 设置插件图标")
        print("  - 示例 (IDAPython):")
        print("    \n"""")
        print("    # 添加菜单项")
        print("    import idaapi")
        print("    def my_menu_callback():")
        print("        print(\"Menu item clicked!\")")
        print("    ")
        print("    # 添加菜单项")
        print("    idaapi.add_menu_item(\")")
        print("        \"Edit/Plugins/\",")
        print("        \"My Plugin\",")
        print("        None,")
        print("        0,")
        print("        my_menu_callback,")
        print("        ("))
        print("    ")
        print("    """)
    
    def plugin_release(self):
        """插件发布"""
        print("\n--- 5. 插件发布 ---")
        
        print("插件打包:")
        print("  - 文件打包: 将插件文件打包成压缩包")
        print("  - 依赖打包: 包含必要的依赖文件")
        print("  - 文档打包: 包含使用说明和API文档")
        print("  - 版本管理: 使用版本号管理插件版本")
        
        print("\n插件文档:")
        print("  - 使用说明: 详细的使用方法")
        print("  - API文档: 插件API的详细说明")
        print("  - 示例代码: 插件使用的示例代码")
        print("  - 变更日志: 记录插件的变更历史")
        
        print("\n插件测试:")
        print("  - 功能测试: 测试插件的各项功能")
        print("  - 兼容性测试: 测试插件在不同版本工具上的兼容性")
        print("  - 性能测试: 测试插件的性能影响")
        print("  - 稳定性测试: 测试插件的稳定性")
        
        print("\n插件发布:")
        print("  - GitHub发布: 在GitHub上发布插件")
        print("  - 插件市场: 在工具的插件市场发布")
        print("  - 社区分享: 在相关社区分享插件")
        print("  - 版本更新: 定期更新插件，修复问题和添加新功能")
    
    def advanced_plugin_development(self):
        """高级插件开发"""
        print("\n--- 6. 高级插件开发 ---")
        
        print("插件架构设计:")
        print("  - 模块化设计: 将插件功能分解为模块")
        print("  - 事件驱动: 基于事件的插件设计")
        print("  - 多线程: 使用多线程提高性能")
        print("  - 错误处理: 完善的错误处理机制")
        
        print("\n插件通信:")
        print("  - 进程间通信: 与其他进程通信")
        print("  - 网络通信: 通过网络与其他设备通信")
        print("  - 插件间通信: 与其他插件通信")
        print("  - 数据共享: 在插件间共享数据")
        
        print("\n插件安全:")
        print("  - 输入验证: 验证用户输入")
        print("  - 权限管理: 管理插件的权限")
        print("  - 数据安全: 保护敏感数据")
        print("  - 代码安全: 避免安全漏洞")
        
        print("\n插件性能优化:")
        print("  - 代码优化: 优化插件代码")
        print("  - 内存优化: 优化内存使用")
        print("  - 算法优化: 优化算法性能")
        print("  - 缓存使用: 使用缓存提高性能")
    
    def practical_tools(self):
        """实用工具"""
        print("\n--- 7. 实用工具 ---")
        
        print("开发工具:")
        print("  - Visual Studio: https://visualstudio.microsoft.com/（C/C++插件开发）")
        print("  - PyCharm: https://www.jetbrains.com/pycharm/（Python插件开发）")
        print("  - VS Code: https://code.visualstudio.com/（通用代码编辑器）")
        print("  - Git: https://git-scm.com/（版本控制）")
        
        print("\nSDK和文档:")
        print("  - IDA SDK: https://www.hex-rays.com/products/ida/support/sdkdoc/（IDA插件开发SDK）")
        print("  - x64dbg SDK: https://github.com/x64dbg/x64dbg/（x64dbg插件开发SDK）")
        print("  - IDAPython文档: https://www.hex-rays.com/products/ida/support/idapython_docs/（IDAPython文档）")
        print("  - x64dbg插件文档: https://x64dbg.com/blog/（x64dbg插件开发文档）")
        
        print("\n示例和模板:")
        print("  - IDA插件示例: IDA安装目录下的plugins文件夹")
        print("  - x64dbg插件示例: x64dbg SDK中的examples文件夹")
        print("  - GitHub插件仓库: 各种插件的开源代码")
        print("  - 插件模板: 用于快速开始插件开发的模板")
        
        print("\n学习资源:")
        print("  - 《IDA Pro权威指南》（Chris Eagle）：介绍IDA Pro插件开发")
        print("  - 《x64dbg插件开发指南》：x64dbg官方文档")
        print("  - 看雪论坛：https://bbs.pediy.com/（国内知名的逆向工程论坛）")
        print("  - GitHub: https://github.com/（各种插件的开源代码）")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.plugin_development_basics()
            self.ida_plugin_development()
            self.x64dbg_plugin_development()
            self.plugin_api()
            self.plugin_release()
            self.advanced_plugin_development()
            self.practical_tools()
            
            print("\n" + "=" * 80)
            print("插件开发示例演示完成！")
            print("通过本演示，您了解了插件开发的基本概念、IDA插件开发、x64dbg插件开发、插件API、插件发布、高级插件开发和实用工具等内容。")
            print("插件开发是逆向工程的重要组成部分，掌握它将帮助您更有效地扩展工具功能，提高工作效率。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = PluginDevDemo()
    demo.run_demo()

