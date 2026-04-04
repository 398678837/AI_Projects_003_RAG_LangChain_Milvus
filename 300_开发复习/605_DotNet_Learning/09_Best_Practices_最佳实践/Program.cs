using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace BestPractices
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("=== 最佳实践 ===");
            
            // 代码规范
            Console.WriteLine("\n1. 代码规范:");
            CodeConventions();
            
            // 性能优化
            Console.WriteLine("\n2. 性能优化:");
            PerformanceOptimization();
            
            // 安全性
            Console.WriteLine("\n3. 安全性:");
            Security();
            
            // 异常处理
            Console.WriteLine("\n4. 异常处理:");
            ExceptionHandling();
            
            // 异步编程
            Console.WriteLine("\n5. 异步编程:");
            await AsyncProgramming();
            
            // 设计模式
            Console.WriteLine("\n6. 设计模式:");
            DesignPatterns();
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 代码规范
        static void CodeConventions()
        {
            // 命名规范
            int employeeId = 1001; // 驼峰命名法
            string employeeName = "张三"; // 驼峰命名法
            
            // 常量
            const int MaxRetries = 3; // 帕斯卡命名法
            
            // 类名
            Person person = new Person { Name = "李四", Age = 30 };
            
            Console.WriteLine($"员工ID: {employeeId}, 员工姓名: {employeeName}");
            Console.WriteLine($"最大重试次数: {MaxRetries}");
            Console.WriteLine($"人员信息: {person.Name}, {person.Age}");
        }
        
        // 性能优化
        static void PerformanceOptimization()
        {
            // 字符串拼接
            string result = string.Empty;
            
            // 不推荐的方式
            for (int i = 0; i < 1000; i++)
            {
                result += i.ToString();
            }
            
            // 推荐的方式
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 1000; i++)
            {
                sb.Append(i.ToString());
            }
            string optimizedResult = sb.ToString();
            
            Console.WriteLine("字符串拼接优化完成");
            
            // 集合初始化
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
            Console.WriteLine($"集合初始化: {string.Join(", ", numbers)}");
        }
        
        // 安全性
        static void Security()
        {
            // 输入验证
            string userInput = "test"; // 模拟用户输入
            if (string.IsNullOrEmpty(userInput))
            {
                Console.WriteLine("输入不能为空");
                return;
            }
            
            // 防止SQL注入
            string username = "admin"; // 模拟用户名
            string query = $"SELECT * FROM Users WHERE Username = @Username";
            Console.WriteLine($"安全的SQL查询: {query}");
            
            // 密码处理
            string password = "SecurePassword123";
            // 实际应用中应使用密码哈希
            Console.WriteLine("密码处理示例");
        }
        
        // 异常处理
        static void ExceptionHandling()
        {
            try
            {
                int result = Divide(10, 0);
                Console.WriteLine($"结果: {result}");
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"除零错误: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"其他错误: {ex.Message}");
            }
        }
        
        static int Divide(int a, int b)
        {
            if (b == 0)
            {
                throw new DivideByZeroException("除数不能为零");
            }
            return a / b;
        }
        
        // 异步编程
        static async Task AsyncProgramming()
        {
            // 异步方法
            string result = await GetDataAsync();
            Console.WriteLine($"异步操作结果: {result}");
        }
        
        static async Task<string> GetDataAsync()
        {
            await Task.Delay(1000); // 模拟异步操作
            return "异步数据";
        }
        
        // 设计模式
        static void DesignPatterns()
        {
            // 单例模式
            Singleton singleton = Singleton.Instance;
            singleton.DoSomething();
            
            // 工厂模式
            IProduct product = ProductFactory.CreateProduct(ProductType.A);
            product.DoWork();
            
            // 策略模式
            ISortStrategy sortStrategy = new BubbleSortStrategy();
            int[] numbers = { 5, 2, 8, 1, 9 };
            sortStrategy.Sort(numbers);
            Console.WriteLine($"排序结果: {string.Join(", ", numbers)}");
        }
    }
    
    // 代码规范示例
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }
    
    // 单例模式
    class Singleton
    {
        private static Singleton instance;
        private static readonly object lockObject = new object();
        
        private Singleton() { }
        
        public static Singleton Instance
        {
            get
            {
                if (instance == null)
                {
                    lock (lockObject)
                    {
                        if (instance == null)
                        {
                            instance = new Singleton();
                        }
                    }
                }
                return instance;
            }
        }
        
        public void DoSomething()
        {
            Console.WriteLine("单例模式执行操作");
        }
    }
    
    // 工厂模式
    enum ProductType
    {
        A,
        B
    }
    
    interface IProduct
    {
        void DoWork();
    }
    
    class ProductA : IProduct
    {
        public void DoWork()
        {
            Console.WriteLine("产品A执行工作");
        }
    }
    
    class ProductB : IProduct
    {
        public void DoWork()
        {
            Console.WriteLine("产品B执行工作");
        }
    }
    
    class ProductFactory
    {
        public static IProduct CreateProduct(ProductType type)
        {
            switch (type)
            {
                case ProductType.A:
                    return new ProductA();
                case ProductType.B:
                    return new ProductB();
                default:
                    throw new ArgumentException("无效的产品类型");
            }
        }
    }
    
    // 策略模式
    interface ISortStrategy
    {
        void Sort(int[] numbers);
    }
    
    class BubbleSortStrategy : ISortStrategy
    {
        public void Sort(int[] numbers)
        {
            int n = numbers.Length;
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (numbers[j] > numbers[j + 1])
                    {
                        int temp = numbers[j];
                        numbers[j] = numbers[j + 1];
                        numbers[j + 1] = temp;
                    }
                }
            }
        }
    }
    
    class QuickSortStrategy : ISortStrategy
    {
        public void Sort(int[] numbers)
        {
            QuickSort(numbers, 0, numbers.Length - 1);
        }
        
        private void QuickSort(int[] numbers, int low, int high)
        {
            if (low < high)
            {
                int pivot = Partition(numbers, low, high);
                QuickSort(numbers, low, pivot - 1);
                QuickSort(numbers, pivot + 1, high);
            }
        }
        
        private int Partition(int[] numbers, int low, int high)
        {
            int pivot = numbers[high];
            int i = low - 1;
            for (int j = low; j < high; j++)
            {
                if (numbers[j] < pivot)
                {
                    i++;
                    int temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                }
            }
            int temp1 = numbers[i + 1];
            numbers[i + 1] = numbers[high];
            numbers[high] = temp1;
            return i + 1;
        }
    }
}