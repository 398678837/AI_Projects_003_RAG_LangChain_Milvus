# Java虚拟机

## 1. JVM概述

### 1.1 JVM的作用
- 执行Java字节码
- 提供内存管理
- 提供垃圾回收
- 提供安全机制

### 1.2 JVM的体系结构
```
JVM
├─ 类加载子系统
├─ 运行时数据区
│  ├─ 方法区
│  ├─ 堆
│  ├─ 虚拟机栈
│  ├─ 本地方法栈
│  └─ 程序计数器
├─ 执行引擎
│  ├─ 解释器
│  ├─ 即时编译器（JIT）
│  └─ 垃圾回收器
└─ 本地方法接口
```

## 2. 类加载机制

### 2.1 类加载的过程
1. **加载**：将字节码文件加载到内存
2. **验证**：验证字节码的合法性
3. **准备**：为静态变量分配内存并设置默认值
4. **解析**：将符号引用转换为直接引用
5. **初始化**：执行类构造器`<clinit>()`方法

### 2.2 类加载器
- **启动类加载器（Bootstrap ClassLoader）**：加载核心类库
- **扩展类加载器（Extension ClassLoader）**：加载扩展类库
- **应用程序类加载器（Application ClassLoader）**：加载应用程序类
- **自定义类加载器（Custom ClassLoader）**：用户自定义的类加载器

### 2.3 双亲委派模型
```
自定义类加载器 → 应用程序类加载器 → 扩展类加载器 → 启动类加载器
```

### 2.4 类加载器的代码示例
```java
ClassLoader classLoader = ClassLoader.getSystemClassLoader();
System.out.println("系统类加载器：" + classLoader);

ClassLoader parent = classLoader.getParent();
System.out.println("扩展类加载器：" + parent);

ClassLoader grandParent = parent.getParent();
System.out.println("启动类加载器：" + grandParent);
```

## 3. 运行时数据区

### 3.1 程序计数器
- 记录当前线程执行的字节码指令地址
- 线程私有
- 不会发生内存溢出

### 3.2 虚拟机栈
- 存储局部变量表、操作数栈、动态链接、方法出口
- 线程私有
- 可能发生StackOverflowError和OutOfMemoryError

### 3.3 本地方法栈
- 为本地方法服务
- 线程私有
- 可能发生StackOverflowError和OutOfMemoryError

### 3.4 堆
- 存储对象实例和数组
- 线程共享
- 可能发生OutOfMemoryError
- 垃圾回收的主要区域

### 3.5 方法区
- 存储类信息、常量、静态变量、即时编译后的代码
- 线程共享
- 可能发生OutOfMemoryError
- 在Java 8及以后，方法区被元空间（Metaspace）取代

### 3.6 运行时常量池
- 存储编译期生成的字面量和符号引用
- 方法区的一部分

## 4. 垃圾回收

### 4.1 垃圾回收的基本概念
- 自动回收不再使用的对象
- 释放内存空间
- 避免内存泄漏

### 4.2 垃圾回收的算法

#### 4.2.1 标记-清除算法
```
标记所有需要回收的对象 → 清除所有被标记的对象
```

#### 4.2.2 复制算法
```
将内存分为两块 → 一块使用，一块空闲 → 当使用的内存满了，将存活对象复制到空闲内存 → 清除使用过的内存
```

#### 4.2.3 标记-整理算法
```
标记所有需要回收的对象 → 将存活对象移动到内存的一端 → 清除边界以外的内存
```

#### 4.2.4 分代收集算法
```
根据对象的存活时间将内存分为新生代和老年代
新生代使用复制算法
老年代使用标记-清除或标记-整理算法
```

### 4.3 垃圾回收器

#### 4.3.1 串行回收器（Serial）
- 单线程回收
- 适合单CPU环境
- 新生代使用复制算法，老年代使用标记-整理算法

#### 4.3.2 并行回收器（Parallel）
- 多线程回收
- 提高吞吐量
- 新生代使用复制算法，老年代使用标记-整理算法

#### 4.3.3 CMS回收器（Concurrent Mark Sweep）
- 并发回收
- 减少停顿时间
- 老年代使用标记-清除算法

#### 4.3.4 G1回收器（Garbage-First）
- 分区回收
- 预测停顿时间
- 适合大内存环境

#### 4.3.5 ZGC回收器（Z Garbage Collector）
- 低延迟回收
- 停顿时间不超过10ms
- 适合大内存环境

### 4.4 垃圾回收的监控
```java
Runtime runtime = Runtime.getRuntime();
long maxMemory = runtime.maxMemory();
long totalMemory = runtime.totalMemory();
long freeMemory = runtime.freeMemory();

System.out.println("最大内存：" + maxMemory / 1024 / 1024 + "MB");
System.out.println("总内存：" + totalMemory / 1024 / 1024 + "MB");
System.out.println("空闲内存：" + freeMemory / 1024 / 1024 + "MB");
```

## 5. 内存模型

### 5.1 Java内存模型（JMM）
- 定义线程之间的可见性
- 定义指令重排序规则
- 保证原子性、可见性、有序性

### 5.2 原子性
- 操作不可分割
- 使用synchronized或Atomic类保证原子性

### 5.3 可见性
- 一个线程对共享变量的修改，其他线程可以立即看到
- 使用volatile或synchronized保证可见性

### 5.4 有序性
- 程序执行的顺序按照代码的先后顺序执行
- 使用volatile或synchronized保证有序性

### 5.5 volatile关键字
```java
private volatile boolean flag = false;

public void setFlag(boolean flag) {
    this.flag = flag;
}

public boolean getFlag() {
    return flag;
}
```

## 6. 字节码执行

### 6.1 字节码的结构
```
字节码文件
├─ 魔数（0xCAFEBABE）
├─ 版本号
├─ 常量池
├─ 访问标志
├─ 类索引、父类索引、接口索引集合
├─ 字段表集合
├─ 方法表集合
└─ 属性表集合
```

### 6.2 字节码指令
- `aload_0`：加载第一个局部变量到操作数栈
- `getfield`：获取对象的字段值
- `invokevirtual`：调用实例方法
- `return`：返回方法

### 6.3 字节码的执行
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

对应的字节码：
```
0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
3: ldc           #3                  // String Hello World
5: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
8: return
```

## 7. 性能优化

### 7.1 内存优化
- 减少对象的创建
- 避免内存泄漏
- 合理设置堆内存大小

### 7.2 垃圾回收优化
- 选择合适的垃圾回收器
- 合理设置新生代和老年代的比例
- 减少Full GC的次数

### 7.3 代码优化
- 避免使用finalize()方法
- 避免使用显式的System.gc()
- 合理使用缓存

### 7.4 JVM参数调优
```bash
# 设置堆内存大小
java -Xms512m -Xmx1024m -jar app.jar

# 设置新生代大小
java -Xmn256m -jar app.jar

# 设置垃圾回收器
java -XX:+UseG1GC -jar app.jar

# 设置日志
java -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -jar app.jar
```

## 8. 常见问题

### 8.1 StackOverflowError
- 栈内存溢出
- 通常由于递归调用过深导致

### 8.2 OutOfMemoryError
- 堆内存溢出
- 通常由于内存泄漏或内存不足导致

### 8.3 类加载异常
- ClassNotFoundException
- NoClassDefFoundError

### 8.4 死锁
- 多个线程相互等待对方释放锁
- 通常由于锁的顺序不当导致

## 9. 工具使用

### 9.1 jps
- 查看Java进程

```bash
jps
```

### 9.2 jstat
- 查看JVM统计信息

```bash
jstat -gc <pid>
```

### 9.3 jmap
- 查看内存映射

```bash
jmap -heap <pid>
```

### 9.4 jstack
- 查看线程栈

```bash
jstack <pid>
```

### 9.5 jconsole
- JVM监控工具

```bash
jconsole
```

### 9.6 VisualVM
- 可视化JVM监控工具

```bash
jvisualvm
```

## 10. 最佳实践

### 10.1 内存管理
- 合理设置堆内存大小
- 避免内存泄漏
- 及时释放不再使用的对象

### 10.2 垃圾回收
- 选择合适的垃圾回收器
- 减少Full GC的次数
- 避免显式调用System.gc()

### 10.3 并发编程
- 合理使用volatile关键字
- 合理使用synchronized关键字
- 避免死锁

### 10.4 性能优化
- 减少对象的创建
- 合理使用缓存
- 避免使用finalize()方法

### 10.5 监控与调优
- 定期监控JVM性能
- 根据监控结果进行调优
- 记录调优过程和结果