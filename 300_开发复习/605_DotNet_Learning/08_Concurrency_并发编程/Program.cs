using System;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Concurrent;
using System.Linq;
using System.Diagnostics;

namespace Concurrency
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 并发编程 ===");
            
            // 线程
            Console.WriteLine("\n1. 线程:");
            ThreadDemo();
            
            // 线程池
            Console.WriteLine("\n2. 线程池:");
            ThreadPoolDemo();
            
            // 任务并行库
            Console.WriteLine("\n3. 任务并行库:");
            TaskDemo();
            
            // 异步编程
            Console.WriteLine("\n4. 异步编程:");
            AsyncDemo().Wait();
            
            // 线程同步
            Console.WriteLine("\n5. 线程同步:");
            ThreadSynchronizationDemo();
            
            // 并发集合
            Console.WriteLine("\n6. 并发集合:");
            ConcurrentCollectionsDemo();
            
            // 并行LINQ
            Console.WriteLine("\n7. 并行LINQ:");
            ParallelLinqDemo();
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 线程
        static void ThreadDemo()
        {
            Thread t1 = new Thread(() =>
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.WriteLine($"线程1: {i}");
                    Thread.Sleep(100);
                }
            });
            
            Thread t2 = new Thread(() =>
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.WriteLine($"线程2: {i}");
                    Thread.Sleep(100);
                }
            });
            
            t1.Start();
            t2.Start();
            
            t1.Join();
            t2.Join();
        }
        
        // 线程池
        static void ThreadPoolDemo()
        {
            for (int i = 0; i < 5; i++)
            {
                int taskId = i;
                ThreadPool.QueueUserWorkItem((state) =>
                {
                    Console.WriteLine($"线程池任务 {taskId} 执行");
                    Thread.Sleep(100);
                });
            }
            
            Thread.Sleep(1000); // 等待线程池任务完成
        }
        
        // 任务并行库
        static void TaskDemo()
        {
            Task[] tasks = new Task[5];
            
            for (int i = 0; i < 5; i++)
            {
                int taskId = i;
                tasks[i] = Task.Run(() =>
                {
                    Console.WriteLine($"任务 {taskId} 执行");
                    Thread.Sleep(100);
                });
            }
            
            Task.WaitAll(tasks);
        }
        
        // 异步编程
        static async Task AsyncDemo()
        {
            Console.WriteLine("开始异步操作");
            
            string result1 = await DoAsyncOperation(1, 1000);
            Console.WriteLine($"操作1结果: {result1}");
            
            string result2 = await DoAsyncOperation(2, 500);
            Console.WriteLine($"操作2结果: {result2}");
            
            // 并行执行
            Task<string> task3 = DoAsyncOperation(3, 800);
            Task<string> task4 = DoAsyncOperation(4, 600);
            
            await Task.WhenAll(task3, task4);
            Console.WriteLine($"操作3结果: {task3.Result}");
            Console.WriteLine($"操作4结果: {task4.Result}");
        }
        
        static async Task<string> DoAsyncOperation(int id, int delay)
        {
            await Task.Delay(delay);
            return $"操作 {id} 完成";
        }
        
        // 线程同步
        static void ThreadSynchronizationDemo()
        {
            int sharedCounter = 0;
            object lockObject = new object();
            
            Thread[] threads = new Thread[5];
            for (int i = 0; i < 5; i++)
            {
                threads[i] = new Thread(() =>
                {
                    for (int j = 0; j < 1000; j++)
                    {
                        lock (lockObject)
                        {
                            sharedCounter++;
                        }
                    }
                });
                threads[i].Start();
            }
            
            foreach (var thread in threads)
            {
                thread.Join();
            }
            
            Console.WriteLine($"共享计数器值: {sharedCounter}");
        }
        
        // 并发集合
        static void ConcurrentCollectionsDemo()
        {
            ConcurrentQueue<int> queue = new ConcurrentQueue<int>();
            
            // 生产者
            Thread producer = new Thread(() =>
            {
                for (int i = 0; i < 10; i++)
                {
                    queue.Enqueue(i);
                    Console.WriteLine($"生产: {i}");
                    Thread.Sleep(100);
                }
            });
            
            // 消费者
            Thread consumer = new Thread(() =>
            {
                for (int i = 0; i < 10; i++)
                {
                    while (!queue.TryDequeue(out int item))
                    {
                        Thread.Sleep(50);
                    }
                    Console.WriteLine($"消费: {item}");
                    Thread.Sleep(150);
                }
            });
            
            producer.Start();
            consumer.Start();
            
            producer.Join();
            consumer.Join();
        }
        
        // 并行LINQ
        static void ParallelLinqDemo()
        {
            int[] numbers = Enumerable.Range(1, 1000000).ToArray();
            
            // 顺序LINQ
            Stopwatch stopwatch = Stopwatch.StartNew();
            int evenCount = numbers.Count(n => n % 2 == 0);
            stopwatch.Stop();
            Console.WriteLine($"顺序LINQ: 偶数数量 = {evenCount}, 耗时 = {stopwatch.ElapsedMilliseconds}ms");
            
            // 并行LINQ
            stopwatch.Restart();
            int parallelEvenCount = numbers.AsParallel().Count(n => n % 2 == 0);
            stopwatch.Stop();
            Console.WriteLine($"并行LINQ: 偶数数量 = {parallelEvenCount}, 耗时 = {stopwatch.ElapsedMilliseconds}ms");
        }
    }
}