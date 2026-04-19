import os
import sys
import hashlib
import json
import time
from datetime import datetime

class SignatureDetection:
    def __init__(self):
        # 模拟恶意代码特征库
        self.malware_signatures = {
            "EICAR-Test-File": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",  # EICAR测试文件的SHA256
            "Malware.Sample.1": "d41d8cd98f00b204e9800998ecf8427e",  # 示例哈希值
            "Malware.Sample.2": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        }
        
        # 特征码规则
        self.signature_rules = [
            {"name": "Shellcode Pattern", "pattern": b"\x90\x90\x90\x90\x90", "description": "NOP sled pattern"},
            {"name": "Encrypted Code", "pattern": b"\x00\x01\x02\x03\x04", "description": "Potential encrypted code"},
            {"name": "Network Connection", "pattern": b"connect", "description": "Network connection attempt"},
            {"name": "File Operation", "pattern": b"CreateFile", "description": "File creation attempt"}
        ]
    
    def calculate_hash(self, file_path):
        """计算文件的哈希值"""
        try:
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            print(f"计算哈希值失败: {str(e)}")
            return None
    
    def scan_file_by_hash(self, file_path):
        """通过哈希值扫描文件"""
        print(f"\n--- 通过哈希值扫描文件: {file_path} ---")
        
        # 计算文件哈希值
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return False
        
        print(f"文件哈希值: {file_hash}")
        
        # 比对特征库
        for malware_name, signature in self.malware_signatures.items():
            if file_hash == signature:
                print(f"检测到恶意代码: {malware_name}")
                return True
        
        print("未检测到已知恶意代码")
        return False
    
    def scan_file_by_pattern(self, file_path):
        """通过特征码模式扫描文件"""
        print(f"\n--- 通过特征码模式扫描文件: {file_path} ---")
        
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            
            detected_patterns = []
            for rule in self.signature_rules:
                if rule["pattern"] in file_content:
                    detected_patterns.append(rule)
            
            if detected_patterns:
                print("检测到以下特征码模式:")
                for pattern in detected_patterns:
                    print(f"  - {pattern['name']}: {pattern['description']}")
                return True
            else:
                print("未检测到特征码模式")
                return False
        except Exception as e:
            print(f"扫描文件失败: {str(e)}")
            return False
    
    def scan_directory(self, directory_path):
        """扫描目录"""
        print(f"\n--- 扫描目录: {directory_path} ---")
        
        scan_results = {
            "scanned_files": 0,
            "detected_files": 0,
            "results": []
        }
        
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    scan_results["scanned_files"] += 1
                    
                    # 扫描文件
                    hash_detected = self.scan_file_by_hash(file_path)
                    pattern_detected = self.scan_file_by_pattern(file_path)
                    
                    if hash_detected or pattern_detected:
                        scan_results["detected_files"] += 1
                        scan_results["results"].append({
                            "file": file_path,
                            "hash_detected": hash_detected,
                            "pattern_detected": pattern_detected
                        })
            
            print(f"\n扫描完成: 扫描了 {scan_results['scanned_files']} 个文件，检测到 {scan_results['detected_files']} 个可疑文件")
            return scan_results
        except Exception as e:
            print(f"扫描目录失败: {str(e)}")
            return scan_results
    
    def create_signature(self, file_path, malware_name):
        """创建恶意代码特征"""
        print(f"\n--- 创建恶意代码特征: {malware_name} ---")
        
        # 计算文件哈希值
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return False
        
        # 添加到特征库
        self.malware_signatures[malware_name] = file_hash
        print(f"成功创建特征: {malware_name} = {file_hash}")
        return True
    
    def generate_signature_report(self, scan_results):
        """生成特征码检测报告"""
        print("\n--- 生成特征码检测报告 ---")
        
        report = {
            "report_info": {
                "title": "特征码检测报告",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "scanner": "SignatureDetection"
            },
            "scan_summary": {
                "scanned_files": scan_results.get("scanned_files", 0),
                "detected_files": scan_results.get("detected_files", 0),
                "detection_rate": f"{scan_results.get('detected_files', 0) / scan_results.get('scanned_files', 1) * 100:.2f}%"
            },
            "signature_database": {
                "total_signatures": len(self.malware_signatures),
                "signature_names": list(self.malware_signatures.keys())
            },
            "scan_results": scan_results.get("results", [])
        }
        
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return report
    
    def demonstrate_signature_detection(self):
        """演示特征码检测"""
        print("=== 特征码检测演示 ===")
        print("======================")
        
        # 1. 显示特征库
        print("\n1. 特征库信息:")
        print(f"特征库大小: {len(self.malware_signatures)} 个特征")
        for malware_name, signature in self.malware_signatures.items():
            print(f"  - {malware_name}: {signature}")
        
        # 2. 显示特征码规则
        print("\n2. 特征码规则:")
        for rule in self.signature_rules:
            print(f"  - {rule['name']}: {rule['description']}")
        
        # 3. 创建EICAR测试文件
        print("\n3. 创建EICAR测试文件:")
        eicar_file = "eicar_test.txt"
        eicar_content = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
        
        with open(eicar_file, 'w') as f:
            f.write(eicar_content)
        print(f"创建EICAR测试文件: {eicar_file}")
        
        # 4. 扫描EICAR测试文件
        print("\n4. 扫描EICAR测试文件:")
        self.scan_file_by_hash(eicar_file)
        self.scan_file_by_pattern(eicar_file)
        
        # 5. 扫描当前目录
        print("\n5. 扫描当前目录:")
        scan_results = self.scan_directory('.')
        
        # 6. 生成检测报告
        print("\n6. 生成检测报告:")
        self.generate_signature_report(scan_results)
        
        # 7. 清理测试文件
        if os.path.exists(eicar_file):
            os.remove(eicar_file)
            print(f"\n清理测试文件: {eicar_file}")
        
        print("\n=== 演示完成 ===")
        print("通过本演示，你了解了特征码检测的基本原理和实现方法。")
        print("特征码检测是一种快速、准确的检测方法，但需要定期更新特征库。")

if __name__ == "__main__":
    signature_detection = SignatureDetection()
    signature_detection.demonstrate_signature_detection()