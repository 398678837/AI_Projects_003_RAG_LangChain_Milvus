#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
反汇编示例
演示反汇编基础、x86/x64汇编、反汇编技巧和分析
"""


def disassembly_basics():
    """反汇编基础"""
    print("\n--- 1. 反汇编基础 ---")
    
    print("反汇编概念:")
    print("  - 机器码到汇编")
    print("  - 二进制到文本")
    print("  - 指令解析")
    
    print("\n反汇编原理:")
    print("  - 指令解码")
    print("  - 操作码解析")
    print("  - 操作数解析")
    
    print("\n反汇编工具:")
    print("  - IDA Pro")
    print("  - Ghidra")
    print("  - Radare2")
    
    print("\n反汇编流程:")
    print("  - 加载文件")
    print("  - 分析代码")
    print("  - 生成汇编")


def x86_assembly():
    """x86汇编"""
    print("\n--- 2. x86汇编 ---")
    
    print("寄存器:")
    print("  - EAX: 累加器")
    print("  - EBX: 基址寄存器")
    print("  - ECX: 计数器")
    print("  - EDX: 数据寄存器")
    print("  - ESP: 栈指针")
    print("  - EBP: 基址指针")
    print("  - EIP: 指令指针")
    
    print("\n指令集:")
    print("  - MOV: 数据传送")
    print("  - ADD/SUB: 加减法")
    print("  - PUSH/POP: 栈操作")
    print("  - CALL/RET: 函数调用")
    print("  - JMP/JZ/JNZ: 跳转")
    
    print("\n寻址方式:")
    print("  - 立即数寻址")
    print("  - 寄存器寻址")
    print("  - 内存寻址")
    print("  - 基址+变址寻址")
    
    print("\n栈操作:")
    print("  - PUSH: 压栈")
    print("  - POP: 出栈")
    print("  - ESP: 栈指针")


def x64_assembly():
    """x64汇编"""
    print("\n--- 3. x64汇编 ---")
    
    print("64位寄存器:")
    print("  - RAX: 64位累加器")
    print("  - RBX: 64位基址")
    print("  - RCX: 64位计数器")
    print("  - RDX: 64位数据")
    print("  - RSP: 64位栈指针")
    print("  - RBP: 64位基址指针")
    print("  - RIP: 64位指令指针")
    
    print("\n64位指令:")
    print("  - 64位操作")
    print("  - RIP相对寻址")
    print("  - 扩展指令集")
    
    print("\n调用约定:")
    print("  - Windows x64:")
    print("    - RCX: 参数1")
    print("    - RDX: 参数2")
    print("    - R8: 参数3")
    print("    - R9: 参数4")
    print("  - Linux x64:")
    print("    - RDI: 参数1")
    print("    - RSI: 参数2")
    print("    - RDX: 参数3")
    
    print("\n寻址方式:")
    print("  - RIP相对寻址")
    print("  - 64位绝对寻址")
    print("  - 扩展基址寻址")


def disassembly_techniques():
    """反汇编技巧"""
    print("\n--- 4. 反汇编技巧 ---")
    
    print("函数识别:")
    print("  - 函数序言")
    print("  - 函数尾声")
    print("  - 调用约定")
    
    print("\n控制流分析:")
    print("  - 条件分支")
    print("  - 循环结构")
    print("  - 开关语句")
    
    print("\n数据流分析:")
    print("  - 数据来源")
    print("  - 数据去向")
    print("  - 数据转换")
    
    print("\n字符串分析:")
    print("  - 字符串引用")
    print("  - 字符串处理")
    print("  - 字符串加密")


def disassembly_analysis():
    """反汇编分析"""
    print("\n--- 5. 反汇编分析 ---")
    
    print("代码分析:")
    print("  - 代码逻辑")
    print("  - 代码结构")
    print("  - 代码优化")
    
    print("\n逻辑分析:")
    print("  - 业务逻辑")
    print("  - 控制逻辑")
    print("  - 数据逻辑")
    
    print("\n算法分析:")
    print("  - 加密算法")
    print("  - 哈希算法")
    print("  - 压缩算法")
    
    print("\n漏洞分析:")
    print("  - 缓冲区溢出")
    print("  - 格式化字符串")
    print("  - 整数溢出")


if __name__ == "__main__":
    print("=== 反汇编示例 ===")
    
    disassembly_basics()
    x86_assembly()
    x64_assembly()
    disassembly_techniques()
    disassembly_analysis()
