import os
import sys
import json
import time
import hashlib
from datetime import datetime

class AuthenticationDemo:
    def __init__(self):
        # 用户数据库
        self.users = {
            "admin": {
                "password": "5f4dcc3b5aa765d61d8327deb882cf99",  # 密码: password
                "full_name": "Admin User",
                "role": "admin",
                "last_login": None
            },
            "user": {
                "password": "5f4dcc3b5aa765d61d8327deb882cf99",  # 密码: password
                "full_name": "Regular User",
                "role": "user",
                "last_login": None
            }
        }
        
        # 认证方法
        self.auth_methods = {
            "password": "基于密码的认证",
            "token": "基于令牌的认证",
            "biometric": "基于生物特征的认证",
            "multi_factor": "多因素认证"
        }
        
        # 认证日志
        self.auth_logs = []
    
    def hash_password(self, password):
        """哈希密码"""
        return hashlib.md5(password.encode()).hexdigest()
    
    def authenticate_password(self, username, password):
        """基于密码的认证"""
        print(f"\n--- 基于密码的认证 ---")
        print(f"用户名: {username}")
        
        # 检查用户是否存在
        if username not in self.users:
            print("认证失败: 用户不存在")
            self.log_auth_attempt(username, "password", False, "用户不存在")
            return False
        
        # 检查密码
        hashed_password = self.hash_password(password)
        if hashed_password != self.users[username]["password"]:
            print("认证失败: 密码错误")
            self.log_auth_attempt(username, "password", False, "密码错误")
            return False
        
        # 认证成功
        print("认证成功")
        self.users[username]["last_login"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_auth_attempt(username, "password", True, "认证成功")
        return True
    
    def generate_token(self, username):
        """生成认证令牌"""
        token = hashlib.sha256(f"{username}_{time.time()}".encode()).hexdigest()
        return token
    
    def authenticate_token(self, username, token):
        """基于令牌的认证"""
        print(f"\n--- 基于令牌的认证 ---")
        print(f"用户名: {username}")
        print(f"令牌: {token}")
        
        # 检查用户是否存在
        if username not in self.users:
            print("认证失败: 用户不存在")
            self.log_auth_attempt(username, "token", False, "用户不存在")
            return False
        
        # 模拟令牌验证（实际应用中应该有令牌存储和验证机制）
        print("认证成功")
        self.users[username]["last_login"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_auth_attempt(username, "token", True, "认证成功")
        return True
    
    def authenticate_multi_factor(self, username, password, otp):
        """多因素认证"""
        print(f"\n--- 多因素认证 ---")
        print(f"用户名: {username}")
        print(f"密码: {'*' * len(password)}")
        print(f"一次性密码: {otp}")
        
        # 检查用户是否存在
        if username not in self.users:
            print("认证失败: 用户不存在")
            self.log_auth_attempt(username, "multi_factor", False, "用户不存在")
            return False
        
        # 检查密码
        hashed_password = self.hash_password(password)
        if hashed_password != self.users[username]["password"]:
            print("认证失败: 密码错误")
            self.log_auth_attempt(username, "multi_factor", False, "密码错误")
            return False
        
        # 检查一次性密码（模拟）
        if otp != "123456":
            print("认证失败: 一次性密码错误")
            self.log_auth_attempt(username, "multi_factor", False, "一次性密码错误")
            return False
        
        # 认证成功
        print("认证成功")
        self.users[username]["last_login"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_auth_attempt(username, "multi_factor", True, "认证成功")
        return True
    
    def log_auth_attempt(self, username, method, success, message):
        """记录认证尝试"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "username": username,
            "method": method,
            "success": success,
            "message": message
        }
        self.auth_logs.append(log_entry)
    
    def show_auth_methods(self):
        """显示认证方法"""
        print("\n--- 认证方法 ---")
        for method, description in self.auth_methods.items():
            print(f"- {method}: {description}")
    
    def show_users(self):
        """显示用户信息"""
        print("\n--- 用户信息 ---")
        for username, info in self.users.items():
            print(f"- 用户名: {username}")
            print(f"  姓名: {info['full_name']}")
            print(f"  角色: {info['role']}")
            print(f"  最后登录: {info['last_login'] or '从未登录'}")
    
    def show_auth_logs(self):
        """显示认证日志"""
        print("\n--- 认证日志 ---")
        for log in self.auth_logs:
            status = "成功" if log["success"] else "失败"
            print(f"[{log['timestamp']}] {log['username']} - {log['method']} - {status}: {log['message']}")
    
    def generate_auth_report(self):
        """生成认证报告"""
        print("\n--- 生成认证报告 ---")
        
        # 统计认证尝试
        total_attempts = len(self.auth_logs)
        successful_attempts = sum(1 for log in self.auth_logs if log["success"])
        failed_attempts = total_attempts - successful_attempts
        
        # 统计认证方法使用情况
        method_usage = {}
        for log in self.auth_logs:
            method = log["method"]
            if method not in method_usage:
                method_usage[method] = {"total": 0, "success": 0}
            method_usage[method]["total"] += 1
            if log["success"]:
                method_usage[method]["success"] += 1
        
        report = {
            "report_info": {
                "title": "认证系统报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "AuthenticationDemo"
            },
            "auth_summary": {
                "total_attempts": total_attempts,
                "successful_attempts": successful_attempts,
                "failed_attempts": failed_attempts,
                "success_rate": successful_attempts / total_attempts if total_attempts > 0 else 0
            },
            "method_usage": method_usage,
            "users": self.users,
            "recommendations": [
                "使用强密码策略",
                "实施多因素认证",
                "定期审计认证日志",
                "使用安全的认证协议"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_authentication(self):
        """演示认证系统"""
        print("=== 认证系统演示 ===")
        print("====================")
        
        # 1. 显示认证方法
        print("\n1. 认证方法:")
        self.show_auth_methods()
        
        # 2. 显示用户信息
        print("\n2. 用户信息:")
        self.show_users()
        
        # 3. 测试基于密码的认证
        print("\n3. 测试基于密码的认证:")
        self.authenticate_password("admin", "password")
        self.authenticate_password("admin", "wrongpassword")
        
        # 4. 测试基于令牌的认证
        print("\n4. 测试基于令牌的认证:")
        token = self.generate_token("user")
        self.authenticate_token("user", token)
        
        # 5. 测试多因素认证
        print("\n5. 测试多因素认证:")
        self.authenticate_multi_factor("admin", "password", "123456")
        self.authenticate_multi_factor("admin", "password", "wrongotp")
        
        # 6. 显示认证日志
        print("\n6. 认证日志:")
        self.show_auth_logs()
        
        # 7. 生成认证报告
        print("\n7. 生成认证报告:")
        self.generate_auth_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了认证系统的基本原理和实现方法。")
        print("认证是安全框架的重要组成部分，用于验证用户身份。")

if __name__ == "__main__":
    auth_demo = AuthenticationDemo()
    auth_demo.demonstrate_authentication()