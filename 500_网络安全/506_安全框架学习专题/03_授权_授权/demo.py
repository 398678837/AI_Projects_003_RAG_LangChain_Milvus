import os
import sys
import json
import time
from datetime import datetime

class AuthorizationDemo:
    def __init__(self):
        # 用户角色
        self.users = {
            "admin": {
                "role": "admin",
                "name": "Admin User"
            },
            "user": {
                "role": "user",
                "name": "Regular User"
            },
            "guest": {
                "role": "guest",
                "name": "Guest User"
            }
        }
        
        # 资源
        self.resources = {
            "/admin": "管理员资源",
            "/user": "用户资源",
            "/public": "公共资源"
        }
        
        # 基于角色的访问控制 (RBAC)
        self.rbac_permissions = {
            "admin": ["/admin", "/user", "/public"],
            "user": ["/user", "/public"],
            "guest": ["/public"]
        }
        
        # 基于属性的访问控制 (ABAC)
        self.abac_policies = [
            {
                "name": "管理员可以访问所有资源",
                "conditions": ["user.role == 'admin'"],
                "actions": ["allow"],
                "resources": ["*"]
            },
            {
                "name": "用户可以访问用户和公共资源",
                "conditions": ["user.role == 'user'"],
                "actions": ["allow"],
                "resources": ["/user", "/public"]
            },
            {
                "name": "访客只能访问公共资源",
                "conditions": ["user.role == 'guest'"],
                "actions": ["allow"],
                "resources": ["/public"]
            }
        ]
        
        # 授权日志
        self.authz_logs = []
    
    def check_rbac_permission(self, user, resource):
        """基于角色的访问控制"""
        print(f"\n--- 基于角色的访问控制 ---")
        print(f"用户: {user}, 角色: {self.users[user]['role']}")
        print(f"资源: {resource}")
        
        # 检查用户角色
        user_role = self.users[user]['role']
        
        # 检查权限
        if resource in self.rbac_permissions.get(user_role, []):
            print("授权成功: 用户有权访问该资源")
            self.log_authz_attempt(user, resource, "rbac", True, "授权成功")
            return True
        else:
            print("授权失败: 用户无权访问该资源")
            self.log_authz_attempt(user, resource, "rbac", False, "授权失败")
            return False
    
    def check_abac_permission(self, user, resource):
        """基于属性的访问控制"""
        print(f"\n--- 基于属性的访问控制 ---")
        print(f"用户: {user}, 角色: {self.users[user]['role']}")
        print(f"资源: {resource}")
        
        # 获取用户属性
        user_attrs = self.users[user]
        
        # 检查策略
        for policy in self.abac_policies:
            # 模拟条件评估
            conditions_met = True
            for condition in policy["conditions"]:
                # 简单的条件评估（实际应用中需要更复杂的评估）
                if "user.role == 'admin'" in condition and user_attrs["role"] != "admin":
                    conditions_met = False
                elif "user.role == 'user'" in condition and user_attrs["role"] != "user":
                    conditions_met = False
                elif "user.role == 'guest'" in condition and user_attrs["role"] != "guest":
                    conditions_met = False
            
            if conditions_met:
                # 检查资源
                if "*" in policy["resources"] or resource in policy["resources"]:
                    if "allow" in policy["actions"]:
                        print(f"授权成功: 符合策略 '{policy['name']}'")
                        self.log_authz_attempt(user, resource, "abac", True, f"符合策略 '{policy['name']}'")
                        return True
        
        print("授权失败: 不符合任何策略")
        self.log_authz_attempt(user, resource, "abac", False, "不符合任何策略")
        return False
    
    def log_authz_attempt(self, user, resource, method, success, message):
        """记录授权尝试"""
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "user": user,
            "resource": resource,
            "method": method,
            "success": success,
            "message": message
        }
        self.authz_logs.append(log_entry)
    
    def show_users(self):
        """显示用户信息"""
        print("\n--- 用户信息 ---")
        for username, info in self.users.items():
            print(f"- 用户名: {username}")
            print(f"  角色: {info['role']}")
            print(f"  姓名: {info['name']}")
    
    def show_resources(self):
        """显示资源信息"""
        print("\n--- 资源信息 ---")
        for resource, description in self.resources.items():
            print(f"- 资源: {resource}")
            print(f"  描述: {description}")
    
    def show_rbac_permissions(self):
        """显示RBAC权限"""
        print("\n--- 基于角色的访问控制权限 ---")
        for role, resources in self.rbac_permissions.items():
            print(f"- 角色: {role}")
            print(f"  可访问资源: {', '.join(resources)}")
    
    def show_abac_policies(self):
        """显示ABAC策略"""
        print("\n--- 基于属性的访问控制策略 ---")
        for policy in self.abac_policies:
            print(f"- 策略: {policy['name']}")
            print(f"  条件: {', '.join(policy['conditions'])}")
            print(f"  操作: {', '.join(policy['actions'])}")
            print(f"  资源: {', '.join(policy['resources'])}")
    
    def show_authz_logs(self):
        """显示授权日志"""
        print("\n--- 授权日志 ---")
        for log in self.authz_logs:
            status = "成功" if log["success"] else "失败"
            print(f"[{log['timestamp']}] {log['user']} 访问 {log['resource']} - {log['method']} - {status}: {log['message']}")
    
    def generate_authz_report(self):
        """生成授权报告"""
        print("\n--- 生成授权报告 ---")
        
        # 统计授权尝试
        total_attempts = len(self.authz_logs)
        successful_attempts = sum(1 for log in self.authz_logs if log["success"])
        failed_attempts = total_attempts - successful_attempts
        
        # 统计授权方法使用情况
        method_usage = {}
        for log in self.authz_logs:
            method = log["method"]
            if method not in method_usage:
                method_usage[method] = {"total": 0, "success": 0}
            method_usage[method]["total"] += 1
            if log["success"]:
                method_usage[method]["success"] += 1
        
        # 统计资源访问情况
        resource_access = {}
        for log in self.authz_logs:
            resource = log["resource"]
            if resource not in resource_access:
                resource_access[resource] = {"total": 0, "success": 0}
            resource_access[resource]["total"] += 1
            if log["success"]:
                resource_access[resource]["success"] += 1
        
        report = {
            "report_info": {
                "title": "授权系统报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "author": "AuthorizationDemo"
            },
            "authz_summary": {
                "total_attempts": total_attempts,
                "successful_attempts": successful_attempts,
                "failed_attempts": failed_attempts,
                "success_rate": successful_attempts / total_attempts if total_attempts > 0 else 0
            },
            "method_usage": method_usage,
            "resource_access": resource_access,
            "users": self.users,
            "resources": self.resources,
            "rbac_permissions": self.rbac_permissions,
            "abac_policies": self.abac_policies,
            "recommendations": [
                "定期审查授权策略",
                "实施最小权限原则",
                "定期审计授权日志",
                "根据业务需求调整授权策略"
            ]
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_authorization(self):
        """演示授权系统"""
        print("=== 授权系统演示 ===")
        print("====================")
        
        # 1. 显示用户信息
        print("\n1. 用户信息:")
        self.show_users()
        
        # 2. 显示资源信息
        print("\n2. 资源信息:")
        self.show_resources()
        
        # 3. 显示RBAC权限
        print("\n3. 基于角色的访问控制权限:")
        self.show_rbac_permissions()
        
        # 4. 显示ABAC策略
        print("\n4. 基于属性的访问控制策略:")
        self.show_abac_policies()
        
        # 5. 测试RBAC授权
        print("\n5. 测试基于角色的访问控制:")
        self.check_rbac_permission("admin", "/admin")
        self.check_rbac_permission("user", "/admin")
        self.check_rbac_permission("user", "/user")
        self.check_rbac_permission("guest", "/user")
        self.check_rbac_permission("guest", "/public")
        
        # 6. 测试ABAC授权
        print("\n6. 测试基于属性的访问控制:")
        self.check_abac_permission("admin", "/admin")
        self.check_abac_permission("user", "/admin")
        self.check_abac_permission("user", "/user")
        self.check_abac_permission("guest", "/user")
        self.check_abac_permission("guest", "/public")
        
        # 7. 显示授权日志
        print("\n7. 授权日志:")
        self.show_authz_logs()
        
        # 8. 生成授权报告
        print("\n8. 生成授权报告:")
        self.generate_authz_report()
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了授权系统的基本原理和实现方法。")
        print("授权是安全框架的重要组成部分，用于控制用户对资源的访问权限。")

if __name__ == "__main__":
    authz_demo = AuthorizationDemo()
    authz_demo.demonstrate_authorization()