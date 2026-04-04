using System;
using System.Threading;

namespace MemoryManagement
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 内存管理 ===");
            
            // 值类型和引用类型
            Console.WriteLine("\n1. 值类型和引用类型:");
            ValueTypeDemo();
            
            // 垃圾回收
            Console.WriteLine("\n2. 垃圾回收:");
            GarbageCollectionDemo();
            
            // IDisposable接口
            Console.WriteLine("\n3. IDisposable接口:");
            DisposableDemo();
            
            // 析构函数
            Console.WriteLine("\n4. 析构函数:");
            DestructorDemo();
            
            // 弱引用
            Console.WriteLine("\n5. 弱引用:");
            WeakReferenceDemo();
            
            // 内存优化
            Console.WriteLine("\n6. 内存优化:");
            MemoryOptimizationDemo();
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 值类型和引用类型
        static void ValueTypeDemo()
        {
            // 值类型
            int x = 10;
            int y = x;
            y = 20;
            Console.WriteLine($"值类型: x = {x}, y = {y}");
            
            // 引用类型
            Person person1 = new Person { Name = "张三" };
            Person person2 = person1;
            person2.Name = "李四";
            Console.WriteLine($"引用类型: person1.Name = {person1.Name}, person2.Name = {person2.Name}");
        }
        
        // 垃圾回收
        static void GarbageCollectionDemo()
        {
            Console.WriteLine($"垃圾回收前: 第0代 {GC.CollectionCount(0)}, 第1代 {GC.CollectionCount(1)}, 第2代 {GC.CollectionCount(2)}");
            
            // 创建大量对象
            for (int i = 0; i < 100000; i++)
            {
                var obj = new object();
            }
            
            // 手动触发垃圾回收
            GC.Collect();
            GC.WaitForPendingFinalizers();
            
            Console.WriteLine($"垃圾回收后: 第0代 {GC.CollectionCount(0)}, 第1代 {GC.CollectionCount(1)}, 第2代 {GC.CollectionCount(2)}");
        }
        
        // IDisposable接口
        static void DisposableDemo()
        {
            // 使用using语句
            using (var resource = new DisposableResource())
            {
                resource.DoSomething();
            } // 自动调用Dispose
            
            Console.WriteLine("资源已释放");
        }
        
        // 析构函数
        static void DestructorDemo()
        {
            { // 作用域开始
                var obj = new ClassWithDestructor();
                obj.DoSomething();
            } // 作用域结束，对象超出范围
            
            // 触发垃圾回收
            GC.Collect();
            GC.WaitForPendingFinalizers();
        }
        
        // 弱引用
        static void WeakReferenceDemo()
        {
            var obj = new LargeObject();
            WeakReference weakRef = new WeakReference(obj);
            
            Console.WriteLine($"弱引用是否存活: {weakRef.IsAlive}");
            
            // 释放强引用
            obj = null;
            
            // 触发垃圾回收
            GC.Collect();
            GC.WaitForPendingFinalizers();
            
            Console.WriteLine($"垃圾回收后弱引用是否存活: {weakRef.IsAlive}");
            
            if (weakRef.IsAlive)
            {
                var retrievedObj = (LargeObject)weakRef.Target;
                Console.WriteLine($"成功从弱引用中获取对象: {retrievedObj.Id}");
            }
            else
            {
                Console.WriteLine("对象已被垃圾回收");
            }
        }
        
        // 内存优化
        static void MemoryOptimizationDemo()
        {
            // 字符串池
            string s1 = "Hello";
            string s2 = "Hello";
            string s3 = new string("Hello".ToCharArray());
            
            Console.WriteLine($"s1 == s2: {s1 == s2}");
            Console.WriteLine($"ReferenceEquals(s1, s2): {ReferenceEquals(s1, s2)}");
            Console.WriteLine($"ReferenceEquals(s1, s3): {ReferenceEquals(s1, s3)}");
            
            // 字符串内插vs字符串拼接
            string name = "张三";
            int age = 30;
            
            string str1 = "姓名: " + name + ", 年龄: " + age;
            string str2 = $"姓名: {name}, 年龄: {age}";
            
            Console.WriteLine($"字符串拼接: {str1}");
            Console.WriteLine($"字符串内插: {str2}");
        }
    }
    
    // 引用类型
    class Person
    {
        public string Name { get; set; }
    }
    
    // 实现IDisposable接口
    class DisposableResource : IDisposable
    {
        private bool disposed = false;
        
        public void DoSomething()
        {
            Console.WriteLine("使用资源");
        }
        
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }
        
        protected virtual void Dispose(bool disposing)
        {
            if (!disposed)
            {
                if (disposing)
                {
                    // 释放托管资源
                    Console.WriteLine("释放托管资源");
                }
                
                // 释放非托管资源
                Console.WriteLine("释放非托管资源");
                
                disposed = true;
            }
        }
        
        ~DisposableResource()
        {
            Dispose(false);
        }
    }
    
    // 带有析构函数的类
    class ClassWithDestructor
    {
        public void DoSomething()
        {
            Console.WriteLine("执行操作");
        }
        
        ~ClassWithDestructor()
        {
            Console.WriteLine("析构函数被调用");
        }
    }
    
    // 大对象
    class LargeObject
    {
        public int Id { get; } = new Random().Next();
        private byte[] data = new byte[1024 * 1024]; // 1MB
    }
}