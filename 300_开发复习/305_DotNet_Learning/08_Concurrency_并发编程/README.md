# 并发编程

## 章节介绍

本章节介绍C#的并发编程特性，包括并发编程基础、多线程编程、线程同步、锁机制、线程池、任务并行库、async/await、并行LINQ、并发集合和并发编程的最佳实践等内容。

## 学习目标

- 掌握C#的多线程编程
- 学习C#的线程同步机制
- 熟悉C#的任务并行库
- 了解C#的异步编程模式
- 掌握C#的并发集合使用

## 代码示例

### Program.cs

本示例展示了C#的并发编程特性，包括：

1. **线程**：创建和管理线程
2. **线程池**：使用线程池执行任务
3. **任务并行库**：使用Task类执行并行任务
4. **异步编程**：使用async/await模式
5. **线程同步**：使用lock语句进行线程同步
6. **并发集合**：使用ConcurrentQueue进行生产者-消费者模式
7. **并行LINQ**：使用PLINQ进行并行数据处理

## 运行方法

### 使用命令行

```bash
# 编译
dotnet build

# 运行
dotnet run
```

### 使用IDE

1. **Visual Studio**：
   - 打开Visual Studio
   - 创建新项目
   - 选择"控制台应用"
   - 复制代码到Program.cs
   - 点击"运行"按钮

2. **Visual Studio Code**：
   - 打开Visual Studio Code
   - 安装C#扩展
   - 打开项目文件夹
   - 按F5运行

## 学习资源

- [C#多线程编程](https://docs.microsoft.com/dotnet/standard/threading/)
- [C#异步编程](https://docs.microsoft.com/dotnet/csharp/programming-guide/concepts/async/)
- [C#任务并行库](https://docs.microsoft.com/dotnet/standard/parallel-programming/task-parallel-library-tpl)
- [C#并发集合](https://docs.microsoft.com/dotnet/standard/collections/thread-safe)