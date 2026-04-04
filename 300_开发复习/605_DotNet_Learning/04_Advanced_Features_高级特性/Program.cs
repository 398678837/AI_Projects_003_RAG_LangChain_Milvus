using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Reflection;

namespace AdvancedFeatures
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("=== 泛型 ===");
            
            // 泛型类
            GenericList<int> intList = new GenericList<int>();
            intList.Add(1);
            intList.Add(2);
            intList.Add(3);
            Console.WriteLine($"intList.Count: {intList.Count}");
            
            GenericList<string> stringList = new GenericList<string>();
            stringList.Add("Hello");
            stringList.Add("World");
            Console.WriteLine($"stringList.Count: {stringList.Count}");
            
            // 泛型方法
            int maxInt = GenericHelper.Max(10, 20);
            string maxString = GenericHelper.Max("Apple", "Banana");
            Console.WriteLine($"Max(10, 20): {maxInt}");
            Console.WriteLine($"Max(\"Apple\", \"Banana\"): {maxString}");
            
            // 委托与事件
            Console.WriteLine("\n=== 委托与事件 ===");
            Publisher publisher = new Publisher();
            Subscriber subscriber = new Subscriber();
            
            // 订阅事件
            publisher.MessagePublished += subscriber.OnMessagePublished;
            
            // 发布消息
            publisher.Publish("Hello from publisher!");
            
            // Lambda表达式
            Console.WriteLine("\n=== Lambda表达式 ===");
            Func<int, int, int> add = (a, b) => a + b;
            Console.WriteLine($"add(5, 3): {add(5, 3)}");
            
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            var evenNumbers = numbers.Where(n => n % 2 == 0);
            Console.WriteLine("偶数: ");
            foreach (var num in evenNumbers)
            {
                Console.Write($"{num} ");
            }
            Console.WriteLine();
            
            // 扩展方法
            Console.WriteLine("\n=== 扩展方法 ===");
            string text = "Hello, World!";
            Console.WriteLine($"原始字符串: {text}");
            Console.WriteLine($"反转后: {text.Reverse()}");
            Console.WriteLine($"是否包含'World': {text.ContainsIgnoreCase("world")}");
            
            // 异步编程
            Console.WriteLine("\n=== 异步编程 ===");
            Console.WriteLine("开始异步操作...");
            string result = await AsyncExample.DoAsyncOperation();
            Console.WriteLine($"异步操作结果: {result}");
            
            // 反射
            Console.WriteLine("\n=== 反射 ===");
            Person person = new Person { Name = "张三", Age = 30 };
            Type personType = person.GetType();
            Console.WriteLine($"类型名称: {personType.Name}");
            
            PropertyInfo[] properties = personType.GetProperties();
            Console.WriteLine("属性:");
            foreach (var prop in properties)
            {
                Console.WriteLine($"  {prop.Name}: {prop.GetValue(person)}");
            }
            
            // 特性
            Console.WriteLine("\n=== 特性 ===");
            Type productType = typeof(Product);
            Attribute[] attributes = Attribute.GetCustomAttributes(productType);
            Console.WriteLine("Product类的特性:");
            foreach (var attr in attributes)
            {
                if (attr is DescriptionAttribute descriptionAttr)
                {
                    Console.WriteLine($"  Description: {descriptionAttr.Description}");
                }
            }
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
    }
    
    // 泛型类
    class GenericList<T>
    {
        private List<T> items = new List<T>();
        
        public void Add(T item)
        {
            items.Add(item);
        }
        
        public int Count => items.Count;
    }
    
    // 泛型方法
    class GenericHelper
    {
        public static T Max<T>(T a, T b) where T : IComparable<T>
        {
            return a.CompareTo(b) > 0 ? a : b;
        }
    }
    
    // 委托与事件
    class Publisher
    {
        // 定义委托
        public delegate void MessageHandler(string message);
        
        // 定义事件
        public event MessageHandler MessagePublished;
        
        public void Publish(string message)
        {
            Console.WriteLine($"发布消息: {message}");
            MessagePublished?.Invoke(message);
        }
    }
    
    class Subscriber
    {
        public void OnMessagePublished(string message)
        {
            Console.WriteLine($"订阅者收到消息: {message}");
        }
    }
    
    // 扩展方法
    static class StringExtensions
    {
        public static string Reverse(this string str)
        {
            char[] chars = str.ToCharArray();
            Array.Reverse(chars);
            return new string(chars);
        }
        
        public static bool ContainsIgnoreCase(this string str, string value)
        {
            return str.ToLower().Contains(value.ToLower());
        }
    }
    
    // 异步编程
    class AsyncExample
    {
        public static async Task<string> DoAsyncOperation()
        {
            await Task.Delay(1000); // 模拟异步操作
            return "异步操作完成!";
        }
    }
    
    // 反射
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }
    
    // 特性
    [AttributeUsage(AttributeTargets.Class)]
    class DescriptionAttribute : Attribute
    {
        public string Description { get; }
        
        public DescriptionAttribute(string description)
        {
            Description = description;
        }
    }
    
    [Description("产品类")]
    class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
    }
}