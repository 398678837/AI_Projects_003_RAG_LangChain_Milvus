import os
import sys
import json
import hashlib
import psutil
import time
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('behavior_analysis_best_practices.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BehaviorAnalysisBestPractices:
    def __init__(self):
        self.analysis_environment = {
            'isolated': False,
            'tools': [],
            'baseline': None
        }
        self.analysis_results = []
    
    def setup_secure_environment(self):
        """设置安全的分析环境"""
        logger.info("=== 设置安全的分析环境 ===")
        
        # 检查是否在虚拟机中运行
        is_vm = self._check_if_vm()
        logger.info(f"运行环境: {'虚拟机' if is_vm else '物理机'}")
        
        # 检查系统状态
        system_status = self._check_system_status()
        logger.info(f"系统状态: {system_status}")
        
        # 验证必要工具是否安装
        required_tools = ['psutil', 'scapy', 'watchdog']
        installed_tools = []
        
        for tool in required_tools:
            try:
                __import__(tool)
                installed_tools.append(tool)
            except ImportError:
                logger.warning(f"工具 {tool} 未安装")
        
        self.analysis_environment['tools'] = installed_tools
        self.analysis_environment['isolated'] = is_vm
        
        logger.info(f"已安装工具: {', '.join(installed_tools)}")
        logger.info("安全环境设置完成")
    
    def _check_if_vm(self):
        """检查是否在虚拟机中运行"""
        try:
            # 检查常见的虚拟机特征
            vm_indicators = [
                'virtualbox', 'vmware', 'hyper-v', 'qemu', 'kvm',
                'parallels', 'virtual machine'
            ]
            
            # 检查系统信息
            system_info = {
                'system': platform.system(),
                'node': platform.node(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor()
            }
            
            # 检查处理器信息
            for key, value in system_info.items():
                for indicator in vm_indicators:
                    if indicator.lower() in str(value).lower():
                        return True
            
            # 检查磁盘信息
            for disk in psutil.disk_partitions():
                if 'virtual' in disk.device.lower():
                    return True
            
            return False
        except Exception as e:
            logger.error(f"检查虚拟机状态时出错: {str(e)}")
            return False
    
    def _check_system_status(self):
        """检查系统状态"""
        try:
            # 检查CPU使用率
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # 检查内存使用率
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            
            # 检查磁盘使用率
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            
            # 检查网络连接数
            net_connections = len(psutil.net_connections())
            
            status = f"CPU: {cpu_usage}%, 内存: {memory_usage}%, 磁盘: {disk_usage}%, 网络连接: {net_connections}"
            return status
        except Exception as e:
            logger.error(f"检查系统状态时出错: {str(e)}")
            return "无法获取系统状态"
    
    def create_behavior_baseline(self):
        """创建行为基线"""
        logger.info("=== 创建行为基线 ===")
        
        baseline = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'processes': [],
            'network_connections': [],
            'system_resources': {}
        }
        
        # 收集进程信息
        for proc in psutil.process_iter(['pid', 'name', 'ppid', 'exe']):
            try:
                proc_info = proc.info
                baseline['processes'].append({
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'ppid': proc_info['ppid'],
                    'exe': proc_info.get('exe', 'N/A')
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # 收集网络连接信息
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED':
                baseline['network_connections'].append({
                    'local_address': f"{conn.laddr.ip}:{conn.laddr.port}",
                    'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else 'N/A',
                    'status': conn.status,
                    'pid': conn.pid
                })
        
        # 收集系统资源信息
        baseline['system_resources'] = {
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent
        }
        
        # 保存基线到文件
        baseline_file = f"behavior_baseline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(baseline_file, 'w', encoding='utf-8') as f:
            json.dump(baseline, f, indent=2, ensure_ascii=False)
        
        self.analysis_environment['baseline'] = baseline
        logger.info(f"行为基线已创建并保存到: {baseline_file}")
        logger.info(f"基线包含 {len(baseline['processes'])} 个进程和 {len(baseline['network_connections'])} 个网络连接")
    
    def implement_analysis_workflow(self, sample_path=None):
        """实现标准的分析工作流程"""
        logger.info("=== 实现标准的分析工作流程 ===")
        
        workflow_steps = [
            "1. 静态分析",
            "2. 动态分析",
            "3. 行为分析",
            "4. IOC提取",
            "5. 报告生成"
        ]
        
        for step in workflow_steps:
            logger.info(f"执行: {step}")
            time.sleep(1)
        
        if sample_path and os.path.exists(sample_path):
            # 执行静态分析
            static_analysis = self._perform_static_analysis(sample_path)
            logger.info(f"静态分析结果: {static_analysis}")
            
            # 执行动态分析
            dynamic_analysis = self._perform_dynamic_analysis(sample_path)
            logger.info(f"动态分析结果: {dynamic_analysis}")
            
            # 提取IOC
            iocs = self._extract_iocs(sample_path)
            logger.info(f"提取的IOC: {iocs}")
            
            # 生成报告
            report = self._generate_analysis_report(static_analysis, dynamic_analysis, iocs)
            logger.info(f"分析报告已生成: {report}")
        else:
            logger.warning("未提供样本路径，跳过具体分析步骤")
    
    def _perform_static_analysis(self, file_path):
        """执行静态分析"""
        try:
            # 计算文件哈希值
            hashes = {
                'md5': self._calculate_hash(file_path, 'md5'),
                'sha1': self._calculate_hash(file_path, 'sha1'),
                'sha256': self._calculate_hash(file_path, 'sha256')
            }
            
            # 获取文件信息
            file_info = {
                'name': os.path.basename(file_path),
                'size': os.path.getsize(file_path),
                'path': file_path,
                'modification_time': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return {
                'file_info': file_info,
                'hashes': hashes
            }
        except Exception as e:
            logger.error(f"静态分析失败: {str(e)}")
            return {}
    
    def _perform_dynamic_analysis(self, file_path):
        """执行动态分析"""
        try:
            # 模拟动态分析过程
            dynamic_analysis = {
                'process_creation': True,
                'file_operations': True,
                'network_connections': True,
                'registry_modifications': True
            }
            return dynamic_analysis
        except Exception as e:
            logger.error(f"动态分析失败: {str(e)}")
            return {}
    
    def _extract_iocs(self, file_path):
        """提取IOC"""
        try:
            # 模拟IOC提取
            iocs = {
                'file_hashes': {
                    'sha256': self._calculate_hash(file_path, 'sha256')
                },
                'ip_addresses': ['192.168.1.1', '10.0.0.1'],
                'domains': ['example.com'],
                'file_paths': [file_path],
                'registry_keys': ['HKCU\Software\Test\Run']
            }
            return iocs
        except Exception as e:
            logger.error(f"IOC提取失败: {str(e)}")
            return {}
    
    def _generate_analysis_report(self, static_analysis, dynamic_analysis, iocs):
        """生成分析报告"""
        try:
            report = {
                'report_info': {
                    'title': '行为分析报告',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'analyst': 'Security Analyst'
                },
                'static_analysis': static_analysis,
                'dynamic_analysis': dynamic_analysis,
                'iocs': iocs,
                'conclusion': '基于分析结果，该样本表现出可疑行为特征',
                'recommendations': [
                    '隔离受感染系统',
                    '删除恶意文件',
                    '阻止相关IP和域名',
                    '清除恶意注册表项',
                    '进行全面系统扫描'
                ]
            }
            
            report_file = f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            return report_file
        except Exception as e:
            logger.error(f"报告生成失败: {str(e)}")
            return None
    
    def _calculate_hash(self, file_path, hash_type):
        """计算文件哈希值"""
        try:
            if hash_type == 'md5':
                hasher = hashlib.md5()
            elif hash_type == 'sha1':
                hasher = hashlib.sha1()
            elif hash_type == 'sha256':
                hasher = hashlib.sha256()
            else:
                return None
            
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            
            return hasher.hexdigest()
        except Exception as e:
            logger.error(f"计算哈希值失败: {str(e)}")
            return None
    
    def demonstrate_best_practices(self):
        """演示最佳实践"""
        logger.info("=== 演示行为分析最佳实践 ===")
        
        # 1. 设置安全环境
        self.setup_secure_environment()
        
        # 2. 创建行为基线
        self.create_behavior_baseline()
        
        # 3. 实现分析工作流程
        self.implement_analysis_workflow()
        
        # 4. 展示分析技巧
        self._show_analysis_techniques()
        
        # 5. 提供防御建议
        self._provide_defense_recommendations()
        
        logger.info("最佳实践演示完成")
    
    def _show_analysis_techniques(self):
        """展示分析技巧"""
        logger.info("=== 展示分析技巧 ===")
        
        techniques = [
            "1. 分层分析：从宏观到微观，逐步深入",
            "2. 对比分析：与基线对比，识别异常",
            "3. 关联分析：关联不同维度的行为数据",
            "4. 时间线分析：按时间顺序分析行为序列",
            "5. 沙箱分析：在隔离环境中执行样本",
            "6. 内存分析：分析进程内存中的可疑代码",
            "7. 网络流量分析：分析样本的网络通信",
            "8. 行为模式识别：识别已知的恶意行为模式"
        ]
        
        for technique in techniques:
            logger.info(technique)
    
    def _provide_defense_recommendations(self):
        """提供防御建议"""
        logger.info("=== 提供防御建议 ===")
        
        recommendations = [
            "1. 安装并更新杀毒软件",
            "2. 启用防火墙",
            "3. 定期更新系统和应用程序",
            "4. 实施应用程序白名单",
            "5. 加强用户权限管理",
            "6. 定期备份重要数据",
            "7. 实施网络分段",
            "8. 加强员工安全意识培训",
            "9. 部署行为分析系统",
            "10. 建立安全事件响应流程"
        ]
        
        for recommendation in recommendations:
            logger.info(recommendation)

if __name__ == "__main__":
    import platform
    
    best_practices = BehaviorAnalysisBestPractices()
    print("行为分析最佳实践演示")
    print("====================")
    print("本演示将展示行为分析的最佳实践，包括：")
    print("1. 设置安全的分析环境")
    print("2. 创建行为基线")
    print("3. 实现标准的分析工作流程")
    print("4. 展示分析技巧")
    print("5. 提供防御建议")
    print("\n开始演示...")
    
    try:
        best_practices.demonstrate_best_practices()
    except KeyboardInterrupt:
        print("\n演示已手动停止")
    
    print("\n演示完成！")