import socket
import threading
import json
import os
import time
from datetime import datetime

class RemoteControlServer:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.client_address = None
        self.running = False
        self.command_handlers = {
            'get_system_info': self.get_system_info,
            'list_files': self.list_files,
            'execute_command': self.execute_command,
            'upload_file': self.upload_file,
            'download_file': self.download_file,
            'screenshot': self.screenshot
        }
    
    def start(self):
        """启动服务器"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            print(f"[服务器] 启动成功，监听端口: {self.port}")
            
            # 接受客户端连接
            while self.running:
                try:
                    self.client_socket, self.client_address = self.server_socket.accept()
                    print(f"[服务器] 客户端 {self.client_address} 已连接")
                    
                    # 处理客户端请求
                    self.handle_client()
                except Exception as e:
                    if not self.running:
                        break
                    print(f"[服务器] 接受连接时出错: {str(e)}")
        except Exception as e:
            print(f"[服务器] 启动失败: {str(e)}")
        finally:
            self.stop()
    
    def stop(self):
        """停止服务器"""
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        print("[服务器] 已停止")
    
    def handle_client(self):
        """处理客户端请求"""
        try:
            while self.running:
                # 接收命令
                data = self.client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                # 解析命令
                try:
                    command_data = json.loads(data)
                    command = command_data.get('command')
                    params = command_data.get('params', {})
                    
                    print(f"[服务器] 接收到命令: {command}")
                    
                    # 执行命令
                    if command in self.command_handlers:
                        result = self.command_handlers[command](**params)
                    else:
                        result = {'status': 'error', 'message': 'Unknown command'}
                    
                    # 发送结果
                    response = json.dumps(result)
                    self.client_socket.send(response.encode('utf-8'))
                except json.JSONDecodeError:
                    error_response = json.dumps({'status': 'error', 'message': 'Invalid JSON'})
                    self.client_socket.send(error_response.encode('utf-8'))
                except Exception as e:
                    error_response = json.dumps({'status': 'error', 'message': str(e)})
                    self.client_socket.send(error_response.encode('utf-8'))
        except Exception as e:
            print(f"[服务器] 处理客户端请求时出错: {str(e)}")
        finally:
            if self.client_socket:
                try:
                    self.client_socket.close()
                except:
                    pass
            print(f"[服务器] 客户端 {self.client_address} 已断开连接")
    
    def get_system_info(self):
        """获取系统信息"""
        import platform
        import psutil
        
        try:
            system_info = {
                'system': platform.system(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor(),
                'username': os.getlogin(),
                'pid': os.getpid(),
                'memory': {
                    'total': psutil.virtual_memory().total,
                    'available': psutil.virtual_memory().available
                },
                'cpu': {
                    'count': psutil.cpu_count(),
                    'usage': psutil.cpu_percent(interval=1)
                }
            }
            return {'status': 'success', 'data': system_info}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def list_files(self, path='.'):
        """列出文件"""
        try:
            files = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path):
                    files.append({
                        'name': item,
                        'type': 'file',
                        'size': os.path.getsize(item_path),
                        'mtime': os.path.getmtime(item_path)
                    })
                elif os.path.isdir(item_path):
                    files.append({
                        'name': item,
                        'type': 'directory'
                    })
            return {'status': 'success', 'data': files}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def execute_command(self, command):
        """执行命令"""
        try:
            import subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {
                'status': 'success',
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def upload_file(self, filename, content):
        """上传文件"""
        try:
            with open(filename, 'wb') as f:
                f.write(content.encode('utf-8'))
            return {'status': 'success', 'message': f'File {filename} uploaded successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def download_file(self, filename):
        """下载文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return {'status': 'success', 'content': content}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def screenshot(self):
        """获取屏幕截图"""
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            screenshot_path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(screenshot_path)
            return {'status': 'success', 'message': f'Screenshot saved to {screenshot_path}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

class RemoteControlClient:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        """连接到服务器"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"[客户端] 成功连接到服务器 {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"[客户端] 连接失败: {str(e)}")
            return False
    
    def send_command(self, command, params=None):
        """发送命令"""
        if not self.socket:
            print("[客户端] 未连接到服务器")
            return None
        
        try:
            command_data = {'command': command, 'params': params or {}}
            data = json.dumps(command_data)
            self.socket.send(data.encode('utf-8'))
            
            # 接收响应
            response = self.socket.recv(4096).decode('utf-8')
            return json.loads(response)
        except Exception as e:
            print(f"[客户端] 发送命令时出错: {str(e)}")
            return None
    
    def disconnect(self):
        """断开连接"""
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            print("[客户端] 已断开连接")
    
    def demonstrate_remote_control(self):
        """演示远程控制功能"""
        if not self.connect():
            return
        
        print("\n--- 演示远程控制功能 ---")
        
        # 获取系统信息
        print("\n1. 获取系统信息:")
        result = self.send_command('get_system_info')
        if result and result['status'] == 'success':
            print(f"系统: {result['data']['system']} {result['data']['release']}")
            print(f"处理器: {result['data']['processor']}")
            print(f"内存: {result['data']['memory']['total'] // (1024*1024)}MB 总, {result['data']['memory']['available'] // (1024*1024)}MB 可用")
        
        # 列出文件
        print("\n2. 列出当前目录文件:")
        result = self.send_command('list_files')
        if result and result['status'] == 'success':
            for item in result['data']:
                if item['type'] == 'file':
                    print(f"文件: {item['name']} ({item['size']} bytes)")
                else:
                    print(f"目录: {item['name']}")
        
        # 执行命令
        print("\n3. 执行命令:")
        result = self.send_command('execute_command', {'command': 'dir' if os.name == 'nt' else 'ls -la'})
        if result and result['status'] == 'success':
            print("命令输出:")
            print(result['stdout'])
            if result['stderr']:
                print("错误输出:")
                print(result['stderr'])
        
        # 上传文件
        print("\n4. 上传文件:")
        test_content = "This is a test file uploaded by remote control client"
        result = self.send_command('upload_file', {'filename': 'test_upload.txt', 'content': test_content})
        if result and result['status'] == 'success':
            print(result['message'])
        
        # 下载文件
        print("\n5. 下载文件:")
        result = self.send_command('download_file', {'filename': 'test_upload.txt'})
        if result and result['status'] == 'success':
            print("文件内容:")
            print(result['content'])
        
        # 断开连接
        self.disconnect()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        # 启动服务器
        server = RemoteControlServer()
        try:
            server.start()
        except KeyboardInterrupt:
            print("\n[服务器] 收到中断信号，正在停止...")
            server.stop()
    else:
        # 启动客户端
        client = RemoteControlClient()
        client.demonstrate_remote_control()