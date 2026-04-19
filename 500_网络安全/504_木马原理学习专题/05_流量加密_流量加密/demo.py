import socket
import threading
import json
import time
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class TrafficEncryption:
    def __init__(self):
        self.key = os.urandom(32)  # 256-bit key
        self.iv = os.urandom(16)   # 128-bit IV
    
    def encrypt(self, plaintext):
        """加密数据"""
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # 将IV和密文一起编码
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
    
    def encrypt_file(self, input_file, output_file):
        """加密文件"""
        try:
            with open(input_file, 'rb') as f:
                plaintext = f.read()
            
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(plaintext) + padder.finalize()
            
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            
            with open(output_file, 'wb') as f:
                f.write(self.iv + ciphertext)
            
            print(f"文件加密成功: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"文件加密失败: {str(e)}")
            return False
    
    def decrypt_file(self, input_file, output_file):
        """解密文件"""
        try:
            with open(input_file, 'rb') as f:
                encrypted_data = f.read()
            
            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]
            
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            with open(output_file, 'wb') as f:
                f.write(plaintext)
            
            print(f"文件解密成功: {input_file} -> {output_file}")
            return True
        except Exception as e:
            print(f"文件解密失败: {str(e)}")
            return False
    
    def create_encrypted_server(self, host='0.0.0.0', port=8888):
        """创建加密服务器"""
        def handle_client(client_socket):
            try:
                while True:
                    # 接收加密数据
                    data = client_socket.recv(4096).decode('utf-8')
                    if not data:
                        break
                    
                    # 解密数据
                    decrypted_data = self.decrypt(data)
                    if decrypted_data:
                        print(f"[服务器] 收到解密后的数据: {decrypted_data}")
                        
                        # 处理命令
                        if decrypted_data == 'exit':
                            break
                        
                        # 加密响应
                        response = f"服务器收到: {decrypted_data}"
                        encrypted_response = self.encrypt(response)
                        client_socket.send(encrypted_response.encode('utf-8'))
            except Exception as e:
                print(f"[服务器] 处理客户端时出错: {str(e)}")
            finally:
                client_socket.close()
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"[服务器] 启动成功，监听端口: {port}")
        print(f"[服务器] 加密密钥: {base64.b64encode(self.key).decode('utf-8')}")
        
        try:
            while True:
                client_socket, client_address = server.accept()
                print(f"[服务器] 客户端 {client_address} 已连接")
                client_thread = threading.Thread(target=handle_client, args=(client_socket,))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("[服务器] 收到中断信号，正在停止...")
        finally:
            server.close()
    
    def create_encrypted_client(self, host='127.0.0.1', port=8888):
        """创建加密客户端"""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print(f"[客户端] 成功连接到服务器 {host}:{port}")
        print(f"[客户端] 加密密钥: {base64.b64encode(self.key).decode('utf-8')}")
        
        try:
            while True:
                # 输入命令
                command = input("[客户端] 输入命令 (输入exit退出): ")
                
                # 加密命令
                encrypted_command = self.encrypt(command)
                client.send(encrypted_command.encode('utf-8'))
                
                if command == 'exit':
                    break
                
                # 接收响应
                response = client.recv(4096).decode('utf-8')
                decrypted_response = self.decrypt(response)
                if decrypted_response:
                    print(f"[客户端] 收到解密后的响应: {decrypted_response}")
        except Exception as e:
            print(f"[客户端] 出错: {str(e)}")
        finally:
            client.close()
    
    def demonstrate_traffic_encryption(self):
        """演示流量加密"""
        print("=== 流量加密技术演示 ===")
        print("========================")
        
        # 1. 显示加密技术列表
        print("\n1. 流量加密技术列表:")
        encryption_techniques = [
            "AES加密",
            "RSA加密",
            "TLS/SSL加密",
            "混淆加密",
            "自定义协议加密"
        ]
        for i, technique in enumerate(encryption_techniques, 1):
            print(f"   {i}. {technique}")
        
        # 2. 演示数据加密解密
        print("\n2. 演示数据加密解密:")
        test_data = "这是一段测试数据，用于演示流量加密"
        print(f"原始数据: {test_data}")
        
        encrypted_data = self.encrypt(test_data)
        print(f"加密后数据: {encrypted_data}")
        
        decrypted_data = self.decrypt(encrypted_data)
        print(f"解密后数据: {decrypted_data}")
        print(f"解密是否成功: {decrypted_data == test_data}")
        
        # 3. 演示文件加密解密
        print("\n3. 演示文件加密解密:")
        test_file = "test_file.txt"
        encrypted_file = "encrypted_file.bin"
        decrypted_file = "decrypted_file.txt"
        
        # 创建测试文件
        with open(test_file, 'w') as f:
            f.write("这是测试文件的内容，用于演示文件加密")
        print(f"创建测试文件: {test_file}")
        
        # 加密文件
        self.encrypt_file(test_file, encrypted_file)
        
        # 解密文件
        self.decrypt_file(encrypted_file, decrypted_file)
        
        # 清理临时文件
        for file in [test_file, encrypted_file, decrypted_file]:
            if os.path.exists(file):
                os.remove(file)
        
        print("\n4. 演示加密通信:")
        print("请在另一个终端运行以下命令启动服务器:")
        print("python demo.py server")
        print("然后在当前终端运行以下命令启动客户端:")
        print("python demo.py client")
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了流量加密的基本原理和实现方法。")
        print("请注意：这些技术仅用于学习和防御目的，请勿用于非法活动。")

if __name__ == "__main__":
    import sys
    
    encryption = TrafficEncryption()
    
    if len(sys.argv) == 2:
        if sys.argv[1] == 'server':
            encryption.create_encrypted_server()
        elif sys.argv[1] == 'client':
            encryption.create_encrypted_client()
    else:
        encryption.demonstrate_traffic_encryption()