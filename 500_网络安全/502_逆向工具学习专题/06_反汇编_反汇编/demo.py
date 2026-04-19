#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
反汇编示例
演示反汇编基础、x86/x64汇编、反汇编技巧和分析
"""

from datetime import datetime

class DisassemblyDemo:
    """反汇编示例类"""
    
    def __init__(self):
        """初始化反汇编示例"""
        print("=== 反汇编示例 ===")
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def disassembly_basics(self):
        """反汇编基础"""
        print("\n--- 1. 反汇编基础 ---")
        
        print("反汇编概念:")
        print("  - 机器码到汇编: 将二进制机器码转换为人类可读的汇编语言")
        print("  - 二进制到文本: 将二进制数据转换为文本形式的汇编指令")
        print("  - 指令解析: 解析机器码的操作码和操作数")
        print("  - 指令集架构: 不同CPU架构有不同的指令集")
        
        print("\n反汇编原理:")
        print("  - 指令解码: 识别机器码对应的指令")
        print("  - 操作码解析: 确定指令的操作类型")
        print("  - 操作数解析: 确定指令的操作对象")
        print("  - 指令长度: 不同指令有不同的长度")
        
        print("\n反汇编工具:")
        print("  - IDA Pro: 专业的反汇编工具，功能强大")
        print("  - Ghidra: 开源的反汇编工具，由NSA开发")
        print("  - Radare2: 命令行反汇编工具，跨平台")
        print("  - objdump: GNU工具链中的反汇编工具")
        print("  - x64dbg: 调试器内置的反汇编功能")
        
        print("\n反汇编流程:")
        print("  - 加载文件: 读取可执行文件或内存镜像")
        print("  - 分析代码: 识别代码段和数据段")
        print("  - 指令解码: 将机器码转换为汇编指令")
        print("  - 生成汇编: 输出汇编代码")
        print("  - 分析优化: 识别函数、变量和控制流")
    
    def x86_assembly(self):
        """x86汇编"""
        print("\n--- 2. x86汇编 ---")
        
        print("32位寄存器:")
        print("  - EAX: 累加器，用于算术运算和返回值")
        print("  - EBX: 基址寄存器，用于内存寻址")
        print("  - ECX: 计数器，用于循环和移位操作")
        print("  - EDX: 数据寄存器，用于乘法和除法")
        print("  - ESP: 栈指针，指向栈顶")
        print("  - EBP: 基址指针，指向当前栈帧")
        print("  - ESI: 源变址寄存器，用于字符串操作")
        print("  - EDI: 目的变址寄存器，用于字符串操作")
        print("  - EIP: 指令指针，指向下一条要执行的指令")
        
        print("\n常用指令:")
        print("  - 数据传送: MOV, XCHG, PUSH, POP, LEA")
        print("  - 算术运算: ADD, SUB, MUL, DIV, INC, DEC, NEG")
        print("  - 逻辑运算: AND, OR, XOR, NOT, TEST, SHL, SHR")
        print("  - 控制转移: JMP, JZ, JNZ, JE, JNE, JL, JG, CALL, RET")
        print("  - 栈操作: PUSH, POP, PUSHF, POPF")
        print("  - 字符串操作: MOVS, CMPS, SCAS, LODS, STOS")
        
        print("\n寻址方式:")
        print("  - 立即数寻址: MOV EAX, 123")
        print("  - 寄存器寻址: MOV EAX, EBX")
        print("  - 直接寻址: MOV EAX, [0x12345678]")
        print("  - 寄存器间接寻址: MOV EAX, [EBX]")
        print("  - 基址+偏移寻址: MOV EAX, [EBX+8]")
        print("  - 基址+变址+偏移寻址: MOV EAX, [EBX+ECX*4+8]")
        
        print("\n栈操作:")
        print("  - PUSH: 将数据压入栈，ESP减小")
        print("  - POP: 从栈中弹出数据，ESP增大")
        print("  - 栈帧: 每个函数都有自己的栈帧")
        print("  - 函数调用: PUSH返回地址，CALL函数")
        
        print("\n调用约定:")
        print("  - cdecl: 参数从右到左压栈，调用者清理栈")
        print("  - stdcall: 参数从右到左压栈，被调用者清理栈")
        print("  - fastcall: 前两个参数用ECX和EDX传递，其余压栈")
    
    def x64_assembly(self):
        """x64汇编"""
        print("\n--- 3. x64汇编 ---")
        
        print("64位寄存器:")
        print("  - RAX: 64位累加器")
        print("  - RBX: 64位基址寄存器")
        print("  - RCX: 64位计数器")
        print("  - RDX: 64位数据寄存器")
        print("  - RSP: 64位栈指针")
        print("  - RBP: 64位基址指针")
        print("  - RSI: 64位源变址寄存器")
        print("  - RDI: 64位目的变址寄存器")
        print("  - RIP: 64位指令指针")
        print("  - R8-R15: 额外的通用寄存器")
        
        print("\n64位指令特点:")
        print("  - 64位操作数: 支持64位整数操作")
        print("  - RIP相对寻址: 相对于RIP的地址计算")
        print("  - 扩展指令集: SSE, AVX等SIMD指令")
        print("  - 指令长度: 可变长度，1-15字节")
        
        print("\n调用约定:")
        print("  - Windows x64调用约定:")
        print("    - RCX: 参数1")
        print("    - RDX: 参数2")
        print("    - R8: 参数3")
        print("    - R9: 参数4")
        print("    - 其余参数: 从右到左压栈")
        print("    - 返回值: RAX")
        print("  - Linux x64 (System V)调用约定:")
        print("    - RDI: 参数1")
        print("    - RSI: 参数2")
        print("    - RDX: 参数3")
        print("    - RCX: 参数4")
        print("    - R8: 参数5")
        print("    - R9: 参数6")
        print("    - 其余参数: 从右到左压栈")
        print("    - 返回值: RAX")
        
        print("\n64位寻址方式:")
        print("  - RIP相对寻址: MOV RAX, [RIP+offset]")
        print("  - 64位绝对寻址: MOV RAX, [0x123456789ABCDEF0]")
        print("  - 基址+变址寻址: MOV RAX, [RBX+RCX*8]")
        print("  - 基址+变址+偏移: MOV RAX, [RBX+RCX*8+0x10]")
    
    def disassembly_techniques(self):
        """反汇编技巧"""
        print("\n--- 4. 反汇编技巧 ---")
        
        print("函数识别:")
        print("  - 函数序言: 识别函数开始的指令序列")
        print("    - x86: PUSH EBP, MOV EBP, ESP")
        print("    - x64: PUSH RBP, MOV RBP, RSP")
        print("  - 函数尾声: 识别函数结束的指令序列")
        print("    - x86: MOV ESP, EBP, POP EBP, RET")
        print("    - x64: MOV RSP, RBP, POP RBP, RET")
        print("  - 调用约定: 根据参数传递方式识别调用约定")
        print("  - 函数签名: 分析函数参数和返回值")
        
        print("\n控制流分析:")
        print("  - 条件分支: 分析if-else结构")
        print("  - 循环结构: 识别for、while、do-while循环")
        print("  - 开关语句: 识别switch-case结构")
        print("  - 异常处理: 识别try-catch结构")
        print("  - 函数调用图: 分析函数之间的调用关系")
        
        print("\n数据流分析:")
        print("  - 数据来源: 跟踪数据的初始来源")
        print("  - 数据去向: 跟踪数据的最终去向")
        print("  - 数据转换: 分析数据的转换过程")
        print("  - 变量识别: 识别程序中的变量")
        print("  - 常量识别: 识别程序中的常量")
        
        print("\n字符串分析:")
        print("  - 字符串引用: 识别程序中引用的字符串")
        print("  - 字符串处理: 分析字符串操作函数")
        print("  - 字符串加密: 识别加密的字符串")
        print("  - 字符串解密: 分析字符串解密逻辑")
        
        print("\n反汇编技巧:")
        print("  - 交叉引用: 分析代码和数据的引用关系")
        print("  - 注释添加: 为反汇编代码添加注释")
        print("  - 函数重命名: 为函数添加有意义的名称")
        print("  - 变量重命名: 为变量添加有意义的名称")
        print("  - 结构识别: 识别程序中的数据结构")
    
    def disassembly_analysis(self):
        """反汇编分析"""
        print("\n--- 5. 反汇编分析 ---")
        
        print("代码分析:")
        print("  - 代码逻辑: 分析程序的执行逻辑")
        print("  - 代码结构: 分析程序的结构组织")
        print("  - 代码优化: 识别编译器优化和手动优化")
        print("  - 代码质量: 评估代码的质量和可靠性")
        
        print("\n逻辑分析:")
        print("  - 业务逻辑: 分析程序的业务功能")
        print("  - 控制逻辑: 分析程序的控制流程")
        print("  - 数据逻辑: 分析程序的数据处理")
        print("  - 错误处理: 分析程序的错误处理机制")
        
        print("\n算法分析:")
        print("  - 加密算法: 识别和分析加密算法")
        print("  - 哈希算法: 识别和分析哈希算法")
        print("  - 压缩算法: 识别和分析压缩算法")
        print("  - 排序算法: 识别和分析排序算法")
        print("  - 搜索算法: 识别和分析搜索算法")
        
        print("\n漏洞分析:")
        print("  - 缓冲区溢出: 识别缓冲区溢出漏洞")
        print("  - 格式化字符串: 识别格式化字符串漏洞")
        print("  - 整数溢出: 识别整数溢出漏洞")
        print("  - 内存泄漏: 识别内存泄漏问题")
        print("  - 逻辑漏洞: 识别业务逻辑漏洞")
        
        print("\n恶意代码分析:")
        print("  - 行为分析: 分析恶意代码的行为")
        print("  - 网络通信: 分析恶意代码的网络通信")
        print("  - 文件操作: 分析恶意代码的文件操作")
        print("  - 注册表操作: 分析恶意代码的注册表操作")
        print("  - 自启动项: 分析恶意代码的自启动机制")
    
    def advanced_disassembly(self):
        """高级反汇编技术"""
        print("\n--- 6. 高级反汇编技术 ---")
        
        print("反混淆技术:")
        print("  - 控制流混淆: 识别和还原被混淆的控制流")
        print("  - 数据混淆: 识别和还原被混淆的数据")
        print("  - 字符串混淆: 识别和还原被混淆的字符串")
        print("  - 代码虚拟化: 识别和分析虚拟机保护")
        
        print("\n反调试技术:")
        print("  - 调试器检测: 识别调试器检测代码")
        print("  - 时间检测: 识别时间检测代码")
        print("  - 异常检测: 识别异常检测代码")
        print("  - 虚拟机检测: 识别虚拟机检测代码")
        
        print("\n反编译技术:")
        print("  - 伪代码生成: 将汇编代码转换为伪代码")
        print("  - 变量恢复: 恢复被优化掉的变量")
        print("  - 类型推断: 推断变量和函数的类型")
        print("  - 结构恢复: 恢复程序中的数据结构")
        
        print("\n动态反汇编:")
        print("  - 运行时分析: 在程序运行时进行分析")
        print("  - 内存转储: 分析内存中的代码")
        print("  - 执行跟踪: 跟踪程序的执行流程")
        print("  - 动态插桩: 在运行时插入代码进行分析")
    
    def practical_tools(self):
        """实用工具"""
        print("\n--- 7. 实用工具 ---")
        
        print("反汇编工具:")
        print("  - IDA Pro: https://www.hex-rays.com/products/ida/")
        print("  - Ghidra: https://ghidra-sre.org/")
        print("  - Radare2: https://rada.re/r/")
        print("  - objdump: 包含在GNU binutils中")
        print("  - x64dbg: https://x64dbg.com/")
        
        print("\n辅助工具:")
        print("  - Capstone: 多架构反汇编库")
        print("  - Keystone: 多架构汇编库")
        print("  - Unicorn: CPU模拟器")
        print("  - Z3: 定理证明器，用于符号执行")
        print("  - angr: 符号执行框架")
        
        print("\n学习资源:")
        print("  - 《汇编语言程序设计》")
        print("  - 《逆向工程核心原理》")
        print("  - 《恶意代码分析实战》")
        print("  - 《加密与解密》")
        print("  - 各种安全会议的演讲和教程")
    
    def run_demo(self):
        """运行演示"""
        try:
            self.disassembly_basics()
            self.x86_assembly()
            self.x64_assembly()
            self.disassembly_techniques()
            self.disassembly_analysis()
            self.advanced_disassembly()
            self.practical_tools()
            
            print("\n" + "=" * 80)
            print("反汇编示例演示完成！")
            print("通过本演示，您了解了反汇编的基本概念、x86/x64汇编、反汇编技巧和分析方法等内容。")
            print("反汇编是逆向工程的基础技能，掌握它将帮助您更有效地分析程序的内部工作原理。")
            
        except Exception as e:
            print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    demo = DisassemblyDemo()
    demo.run_demo()

