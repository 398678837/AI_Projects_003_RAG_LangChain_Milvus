import os
import sys
import json
import time
import hashlib
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import serialization

class EncryptionDemo:
    def __init__(self):
        # 加密算法
        self.encryption_algorithms = {
            "AES": "高级加密标准",
            "RSA": "非对称加密算法",
            "SHA-256": "哈希函数",
            "HMAC": "消息认证码"
        }
        
        # 加密模式
        self.encryption_modes = {
            "ECB": "电子密码本模式",
            "CBC": "密码块链接模式",
            "CFB": "密码反馈模式",
            "OFB": "输出反馈模式",
            "CTR": "计数器模式"
        }
        
        # 加密日志
        self.encryption_logs = []
    
    def generate_aes_key(self):
        """生成AES密钥"""
        return os.urandom(32)  # 256位密钥
    
    def aes_encrypt(self, plaintext, key):
        """AES加密"""
        print("\n--- AES加密 ---")
        print(f"明文: {plaintext}")
        
        # 生成IV
        iv = os.urandom(16)  # 16字节IV
        
        # 创建加密器
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # 填充
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()
        
        # 加密
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        print(f"密文: {ciphertext.hex()}")
        print(f"IV: {iv.hex()}")
        
        self.log_encryption_operation("AES", "加密", True, f"加密成功，明文长度: {len(plaintext)}")
        return ciphertext, iv
    
    def aes_decrypt(self, ciphertext, key, iv):
        """AES解密"""
        print("\n--- AES解密 ---")
        print(f"密文: {ciphertext.hex()}")
        print(f"IV: {iv.hex()}")
        
        # 创建解密器
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # 解密
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        # 去填充
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        
        print(f"明文: {plaintext.decode()}")
        
        self.log_encryption_operation("AES", "解密", True, f"解密成功，明文: {plaintext.decode()}")
        return plaintext.decode()
    
    def generate_rsa_keys(self):
        """生成RSA密钥对"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    def rsa_encrypt(self, plaintext, public_key):
        """RSA加密"""
        print("\n--- RSA加密 ---")
        print(f"明文: {plaintext}")
        
        # 加密
        ciphertext = public_key.encrypt(
            plaintext.encode(),
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        print(f"密文: {ciphertext.hex()}")
        
        self.log_encryption_operation("RSA", "加密", True, f"加密成功，明文长度: {len(plaintext)}")
        return ciphertext
    
    def rsa_decrypt(self, ciphertext, private_key):
        """RSA解密"""
        print("\n--- RSA解密 ---")
        print(f"密文: {ciphertext.hex()}")
        
        # 解密
        plaintext = private_key.decrypt(
            ciphertext,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        print(f"明文: {plaintext.decode()}")
        
        self.log_encryption_operation("RSA", "解密", True, f"解密成功，明文: {plaintext.decode()}")
        return plaintext.decode()
    
    def hash_data(self, data):
        """哈希函数"""
        print("\n--- 哈希函数 ---")
        print(f"数据: {data}")
        
        # 计算SHA-256哈希
        sha256_hash = hashlib.sha256(data.encode()).hexdigest()
        print(f"SHA-256哈希: {sha256_hash}")
        
        # 计算MD5哈希
        md5_hash = hashlib.md5(data.encode()).hexdigest()
        print(f"MD5哈希: {md5_hash}")
        
        self.log_encryption_operation("SHA-256", "哈希", True, f"哈希成功，数据长度: {len(data)}")
        return sha256_hash, md5_hash
    
    def log_encryption_operation(self, algorithm, operation, success, message):
        """记录加密操作"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "algorithm": algorithm,
            "operation": operation,
            "success": success,
            "message": message
        }
        self.encryption_logs.append(log_entry)
    
    def show_encryption_algorithms(self):
        """显示加密算法"""
        print("\n--- 加密算法 ---")
        for algorithm, description in self.encryption_algorithms.items():
            print(f"- {algorithm}: {description}")
    
    def show_encryption_modes(self):
        """显示加密模式"""
        print("\n--- 加密模式 ---")
        for mode, description in self.encryption_modes.items():
            print(f"- {mode}: {description}")
    
    def show_encryption_logs(self):
        """显示加密日志"""
        print("\n--- 加密日志 ---")
        for log in self.encryption_logs:
            status = "成功" if log["success"] else "失败"
            print(f"[{log['timestamp']}] {log['algorithm']} - {log['operation']} - {status}: {log['message']}")
    
    def generate_encryption_report(self):
        """生成加密报告"""
        print("\n--- 生成加密报告 ---")
        
        # 统计加密操作
        total_operations = len(self.encryption_logs)
        successful_operations = sum(1 for log in self.encryption_logs if log["success"])
        failed_operations = total_operations - successful_operations
        
        # 统计算法使用情况
        algorithm_usage = {}
        for log in self.encryption_logs:
            algorithm = log["algorithm"]
            if algorithm not in algorithm_usage:
                algorithm_usage[algorithm] = {"total": 0, "success": 0}
            algorithm_usage[algorithm]["total"] += 1
            if log["success"]:
                algorithm_usage[algorithm]["success"] += 1
        
        report = {
            "report_info": {
                "title": "加密系统报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "EncryptionDemo"
            },
            "encryption_summary": {
                "total_operations": total_operations,
                "successful_operations": successful_operations,
                "failed_operations": failed_operations,
                "success_rate": successful_operations / total_operations if total_operations > 0 else 0
            },
            "algorithm_usage": algorithm_usage,
            "encryption_algorithms": self.encryption_algorithms,
            "encryption_modes": self.encryption_modes,
            "recommendations": [
                "使用强加密算法",
                "定期更换密钥",
                "保护密钥安全",
                "使用合适的加密模式"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_encryption(self):
        """演示加密系统"""
        print("=== 加密系统演示 ===")
        print("====================")
        
        # 1. 显示加密算法
        print("\n1. 加密算法:")
        self.show_encryption_algorithms()
        
        # 2. 显示加密模式
        print("\n2. 加密模式:")
        self.show_encryption_modes()
        
        # 3. 测试AES加密
        print("\n3. 测试AES加密:")
        plaintext = "Hello, World!"
        aes_key = self.generate_aes_key()
        ciphertext, iv = self.aes_encrypt(plaintext, aes_key)
        decrypted_text = self.aes_decrypt(ciphertext, aes_key, iv)
        print(f"加密前: {plaintext}")
        print(f"解密后: {decrypted_text}")
        print(f"解密结果与原明文是否相同: {plaintext == decrypted_text}")
        
        # 4. 测试RSA加密
        print("\n4. 测试RSA加密:")
        private_key, public_key = self.generate_rsa_keys()
        rsa_plaintext = "RSA Encryption Test"
        rsa_ciphertext = self.rsa_encrypt(rsa_plaintext, public_key)
        rsa_decrypted_text = self.rsa_decrypt(rsa_ciphertext, private_key)
        print(f"加密前: {rsa_plaintext}")
        print(f"解密后: {rsa_decrypted_text}")
        print(f"解密结果与原明文是否相同: {rsa_plaintext == rsa_decrypted_text}")
        
        # 5. 测试哈希函数
        print("\n5. 测试哈希函数:")
        hash_data = "Hash Function Test"
        sha256_hash, md5_hash = self.hash_data(hash_data)
        print(f"原始数据: {hash_data}")
        print(f"SHA-256哈希: {sha256_hash}")
        print(f"MD5哈希: {md5_hash}")
        
        # 6. 显示加密日志
        print("\n6. 加密日志:")
        self.show_encryption_logs()
        
        # 7. 生成加密报告
        print("\n7. 生成加密报告:")
        self.generate_encryption_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了加密系统的基本原理和实现方法。")
        print("加密是安全框架的重要组成部分，用于保护数据的机密性和完整性。")

# 导入缺失的模块
try:
    from cryptography.hazmat.primitives import hashes
except ImportError:
    print("请安装cryptography库: pip install cryptography")
    sys.exit(1)

if __name__ == "__main__":
    encryption_demo = EncryptionDemo()
    encryption_demo.demonstrate_encryption()