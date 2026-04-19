# 04_文件监控_文件监控

## 学习目标
- 理解文件系统的基本概念和结构
- 掌握文件监控的原理和方法
- 熟悉常用的文件监控工具
- 能够分析文件行为并识别异常
- 了解文件隐藏技术和检测方法
- 能够使用Python进行文件监控和分析

## 关键要点

### 1. 文件监控基础

#### 1.1 文件系统概念
- **文件系统**：操作系统用于管理和存储文件的方法
- **文件**：存储数据的基本单位
- **目录**：组织文件的容器
- **路径**：文件或目录的位置标识符

#### 1.2 文件类型
- **可执行文件**：.exe, .dll, .bat, .cmd, .ps1
- **文档文件**：.txt, .doc, .pdf, .xls
- **系统文件**：.sys, .dat, .ini, .config
- **数据文件**：.csv, .json, .xml, .sqlite

#### 1.3 文件操作
- **创建**：创建新文件
- **读取**：读取文件内容
- **写入**：修改文件内容
- **删除**：删除文件
- **移动**：移动或重命名文件
- **复制**：复制文件

#### 1.4 文件权限
- **读取权限**：允许读取文件内容
- **写入权限**：允许修改文件内容
- **执行权限**：允许执行文件（仅适用于可执行文件）
- **删除权限**：允许删除文件

### 2. 文件监控工具

#### 2.1 Process Monitor
- **特点**：实时监控文件系统、注册表和网络操作
- **功能**：详细的文件操作记录、过滤和搜索
- **优势**：实时性强，信息全面
- **应用**：详细的文件行为分析

#### 2.2 FileMon
- **特点**：专门的文件系统监控工具
- **功能**：监控文件的读写操作
- **优势**：轻量级，专注于文件操作
- **应用**：简单的文件监控

#### 2.3 Windows Event Log
- **特点**：Windows内置的事件日志系统
- **功能**：记录系统事件，包括文件操作
- **优势**：系统集成，无需额外安装
- **应用**：系统级文件操作监控

#### 2.4 Python监控脚本
- **特点**：使用Python编写的自定义监控脚本
- **功能**：可根据需要定制监控逻辑
- **优势**：灵活可定制，适合特定场景
- **应用**：自动化文件监控和分析

### 3. 文件监控流程

#### 3.1 文件创建
- **监控目标**：监控新文件的创建
- **监控内容**：文件路径、创建时间、创建进程
- **分析重点**：可疑位置的文件创建、异常文件类型的创建

#### 3.2 文件修改
- **监控目标**：监控文件内容的修改
- **监控内容**：文件路径、修改时间、修改进程
- **分析重点**：系统文件的修改、配置文件的修改

#### 3.3 文件删除
- **监控目标**：监控文件的删除
- **监控内容**：文件路径、删除时间、删除进程
- **分析重点**：关键文件的删除、日志文件的删除

#### 3.4 文件移动
- **监控目标**：监控文件的移动和重命名
- **监控内容**：源路径、目标路径、移动时间、移动进程
- **分析重点**：可疑的文件移动、敏感文件的重命名

### 4. 文件行为分析

#### 4.1 文件创建分析
- **正常创建**：用户通过应用程序创建文件
- **异常创建**：恶意程序在系统目录创建文件
- **创建模式**：分析文件创建的时间、位置和类型

#### 4.2 文件修改分析
- **正常修改**：用户编辑文件内容
- **异常修改**：恶意程序修改系统文件
- **修改模式**：分析文件修改的频率、内容变化

#### 4.3 文件删除分析
- **正常删除**：用户删除不需要的文件
- **异常删除**：恶意程序删除日志文件或安全文件
- **删除模式**：分析文件删除的时间、类型

#### 4.4 文件移动分析
- **正常移动**：用户组织文件
- **异常移动**：恶意程序隐藏文件或逃避检测
- **移动模式**：分析文件移动的源路径和目标路径

### 5. 文件隐藏技术

#### 5.1 隐藏属性
- **文件属性**：设置文件为隐藏属性
- **检测方法**：显示隐藏文件，检查文件属性
- **防御措施**：定期扫描隐藏文件

#### 5.2 系统属性
- **系统属性**：设置文件为系统属性
- **检测方法**：显示系统文件，检查文件属性
- **防御措施**：定期扫描系统文件

#### 5.3 ADS流
- **ADS流**：使用NTFS文件系统的备用数据流
- **检测方法**：使用命令行工具或专用工具检测
- **防御措施**：定期扫描ADS流

#### 5.4 加密隐藏
- **加密隐藏**：使用加密软件隐藏文件
- **检测方法**：使用专用工具检测加密文件
- **防御措施**：定期扫描加密文件

### 6. 文件监控示例

#### 6.1 基本文件监控
```python
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"文件创建: {event.src_path}")
    
    def on_modified(self, event):
        if not event.is_directory:
            print(f"文件修改: {event.src_path}")
    
    def on_deleted(self, event):
        if not event.is_directory:
            print(f"文件删除: {event.src_path}")
    
    def on_moved(self, event):
        if not event.is_directory:
            print(f"文件移动: {event.src_path} -> {event.dest_path}")

def monitor_files(path):
    """监控文件"""
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    print(f"开始监控目录: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# 测试
if __name__ == "__main__":
    monitor_files(".")
```

#### 6.2 可疑文件检测
```python
import os
import hashlib

def calculate_file_hash(file_path):
    """计算文件哈希"""
    hashes = {}
    algorithms = ['md5', 'sha1', 'sha256']
    
    for algo in algorithms:
        hash_obj = hashlib.new(algo)
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                hash_obj.update(data)
        hashes[algo] = hash_obj.hexdigest()
    
    return hashes

def detect_suspicious_files(directory):
    """检测可疑文件"""
    print(f"检测目录: {directory}")
    
    # 可疑文件扩展名
    suspicious_extensions = ['.exe', '.dll', '.bat', '.cmd', '.ps1', '.vbs']
    
    # 系统敏感目录
    sensitive_directories = ['C:\Windows', 'C:\Program Files', 'C:\Program Files (x86)']
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 检测可疑文件扩展名
            ext = os.path.splitext(file)[1].lower()
            if ext in suspicious_extensions:
                print(f"[!] 可疑文件: {file_path} (扩展名: {ext})")
                
                # 计算文件哈希
                try:
                    hashes = calculate_file_hash(file_path)
                    print(f"    MD5: {hashes['md5']}")
                    print(f"    SHA1: {hashes['sha1']}")
                    print(f"    SHA256: {hashes['sha256']}")
                except:
                    pass
            
            # 检测系统目录中的文件
            if any(root.startswith(dir) for dir in sensitive_directories):
                print(f"[!] 系统目录文件: {file_path}")

# 测试
if __name__ == "__main__":
    detect_suspicious_files(".")
```

## 实践任务

### 1. 文件监控工具使用
- 安装和使用Process Monitor，熟悉其功能
- 使用FileMon监控文件系统操作
- 查看Windows Event Log中的文件操作事件

### 2. 文件监控脚本开发
- 使用Python和watchdog库开发文件监控脚本
- 实现文件创建、修改、删除和移动的监控
- 实现可疑文件的自动检测

### 3. 可疑文件检测
- 开发可疑文件检测脚本
- 检测系统目录中的异常文件
- 检测具有可疑扩展名的文件

### 4. 文件行为分析
- 分析正常文件的行为模式
- 分析恶意文件的行为特征
- 建立文件行为基线，检测异常

### 5. 文件隐藏技术研究
- 研究常见的文件隐藏技术
- 开发文件隐藏检测工具
- 测试不同文件隐藏技术的检测效果

### 6. 文件监控系统集成
- 将文件监控集成到安全运营系统
- 开发文件监控告警机制
- 实现文件监控数据的可视化

## 参考资料

### 书籍
- 《Windows Internals》（Mark Russinovich）：深入了解Windows系统内部机制
- 《恶意代码分析实战》（Michael Sikorski）：详细介绍恶意代码分析的方法和工具
- 《文件系统原理》（Remzi H. Arpaci-Dusseau）：详细介绍文件系统的原理

### 在线资源
- Process Monitor文档：https://docs.microsoft.com/en-us/sysinternals/downloads/procmon（微软官方文档）
- watchdog库文档：https://python-watchdog.readthedocs.io/（Python文件系统监控库文档）
- NTFS文件系统文档：https://docs.microsoft.com/en-us/windows/win32/fileio/ntfs-file-system（微软官方文档）
- MITRE ATT&CK框架：https://attack.mitre.org/（提供攻击行为的分类和描述）

### 工具下载
- Process Monitor：https://docs.microsoft.com/en-us/sysinternals/downloads/procmon（文件系统监控工具）
- FileMon：https://docs.microsoft.com/en-us/sysinternals/downloads/filemon（文件系统监控工具）
- Python watchdog库：通过pip install watchdog安装（Python文件系统监控库）
- Sysinternals Suite：https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite（系统工具套件）

### 视频教程
- SANS安全培训：包含文件监控和分析相关的培训课程
- 安全会议演讲：BlackHat、DEF CON等会议的文件分析相关演讲
- YouTube教程：文件监控工具使用和文件分析的视频教程

## 总结

本章节介绍了文件监控的基本概念、工具、流程和分析方法。通过本章节的学习，您应该已经掌握了文件监控的核心概念和基本方法，能够使用各种工具和Python脚本进行文件监控和分析。

文件监控是行为分析的重要组成部分，通过监控文件的创建、修改、删除和移动，以及文件的行为特征，可以识别潜在的安全威胁。在学习过程中，您应该注重实践，通过实际操作来加深对文件监控的理解。同时，您还应该了解文件隐藏技术和检测方法，以便能够检测和应对高级威胁。

希望本章节的内容对您有所帮助，祝您在文件监控的学习和实践中取得成功！
