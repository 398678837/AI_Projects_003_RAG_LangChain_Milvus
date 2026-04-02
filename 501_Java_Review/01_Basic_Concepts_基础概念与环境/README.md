# Java基础概念与环境

## 1. Java语言概述

### 1.1 Java的发展历程
- 1995年Sun Microsystems发布Java 1.0
- 2009年Oracle收购Sun Microsystems
- 2014年Java 8发布（里程碑版本）
- 2018年开始每6个月发布一次新版本

### 1.2 Java的三大平台
- **Java SE** (Standard Edition)：标准版，用于桌面应用开发
- **Java EE** (Enterprise Edition)：企业版，用于服务器端应用开发
- **Java ME** (Micro Edition)：微型版，用于嵌入式设备开发

### 1.3 Java的核心特性
- **跨平台性**：一次编写，到处运行（Write Once, Run Anywhere）
- **面向对象**：封装、继承、多态
- **垃圾回收**：自动内存管理
- **安全性**：沙箱机制
- **高性能**：即时编译（JIT）

## 2. Java开发环境搭建

### 2.1 JDK、JRE、JVM的区别
- **JVM** (Java Virtual Machine)：Java虚拟机，负责执行Java字节码
- **JRE** (Java Runtime Environment)：Java运行环境，包含JVM和核心类库
- **JDK** (Java Development Kit)：Java开发工具包，包含JRE和开发工具（编译器、调试器等）

### 2.2 安装JDK
1. 下载JDK安装包（Oracle官网或OpenJDK）
2. 配置环境变量：
   - `JAVA_HOME`：JDK安装目录
   - `PATH`：添加`%JAVA_HOME%/bin`
   - `CLASSPATH`：指定类库路径

### 2.3 常用开发工具
- **Eclipse**：开源IDE
- **IntelliJ IDEA**：JetBrains出品的商业IDE
- **NetBeans**：Oracle出品的开源IDE
- **VS Code**：轻量级编辑器，通过插件支持Java开发

## 3. 第一个Java程序

### 3.1 HelloWorld示例
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 3.2 编译与运行
1. 编译：`javac HelloWorld.java`
2. 运行：`java HelloWorld`

### 3.3 程序结构解析
- **类声明**：`public class HelloWorld`
- **主方法**：`public static void main(String[] args)`
- **输出语句**：`System.out.println("Hello, World!")`

## 4. Java程序的执行流程
1. 编写Java源文件（.java）
2. 编译器（javac）将源文件编译为字节码文件（.class）
3. JVM加载字节码文件
4. JVM解释执行字节码（或通过JIT编译为本地机器码）

## 5. Java的命名规范
- **包名**：全小写，使用域名反转（com.example.project）
- **类名**：大驼峰式（HelloWorld）
- **方法名**：小驼峰式（getUserInfo）
- **变量名**：小驼峰式（userName）
- **常量名**：全大写，下划线分隔（MAX_VALUE）