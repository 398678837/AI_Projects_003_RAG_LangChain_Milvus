using System;
using System.Collections.Generic;

namespace CoreSyntax
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 控制流 ===");
            
            // 条件语句
            int score = 85;
            if (score >= 90)
            {
                Console.WriteLine("优秀");
            }
            else if (score >= 80)
            {
                Console.WriteLine("良好");
            }
            else if (score >= 60)
            {
                Console.WriteLine("及格");
            }
            else
            {
                Console.WriteLine("不及格");
            }
            
            // switch语句
            int dayOfWeek = 3;
            switch (dayOfWeek)
            {
                case 1:
                    Console.WriteLine("星期一");
                    break;
                case 2:
                    Console.WriteLine("星期二");
                    break;
                case 3:
                    Console.WriteLine("星期三");
                    break;
                case 4:
                    Console.WriteLine("星期四");
                    break;
                case 5:
                    Console.WriteLine("星期五");
                    break;
                case 6:
                    Console.WriteLine("星期六");
                    break;
                case 7:
                    Console.WriteLine("星期日");
                    break;
                default:
                    Console.WriteLine("无效的日期");
                    break;
            }
            
            // 循环语句
            Console.WriteLine("\n=== 循环语句 ===");
            
            // for循环
            Console.WriteLine("For循环:");
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine($"i = {i}");
            }
            
            // while循环
            Console.WriteLine("\nWhile循环:");
            int j = 1;
            while (j <= 5)
            {
                Console.WriteLine($"j = {j}");
                j++;
            }
            
            // do-while循环
            Console.WriteLine("\nDo-While循环:");
            int k = 1;
            do
            {
                Console.WriteLine($"k = {k}");
                k++;
            } while (k <= 5);
            
            // foreach循环
            Console.WriteLine("\nForeach循环:");
            string[] fruits = { "苹果", "香蕉", "橙子", "葡萄" };
            foreach (string fruit in fruits)
            {
                Console.WriteLine($"水果: {fruit}");
            }
            
            // 函数
            Console.WriteLine("\n=== 函数 ===");
            int result = Add(10, 20);
            Console.WriteLine($"10 + 20 = {result}");
            
            // 数组
            Console.WriteLine("\n=== 数组 ===");
            int[] numbers = { 1, 2, 3, 4, 5 };
            Console.WriteLine("数组元素:");
            for (int i = 0; i < numbers.Length; i++)
            {
                Console.WriteLine($"numbers[{i}] = {numbers[i]}");
            }
            
            // 二维数组
            int[,] matrix = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            Console.WriteLine("\n二维数组:");
            for (int i = 0; i < 3; i++)
            {
                for (int l = 0; l < 3; l++)
                {
                    Console.Write($"{matrix[i, l]} ");
                }
                Console.WriteLine();
            }
            
            // 字符串操作
            Console.WriteLine("\n=== 字符串操作 ===");
            string text = "Hello, C# World!";
            Console.WriteLine($"原始字符串: {text}");
            Console.WriteLine($"长度: {text.Length}");
            Console.WriteLine($"大写: {text.ToUpper()}");
            Console.WriteLine($"小写: {text.ToLower()}");
            Console.WriteLine($"包含'C#': {text.Contains("C#")}");
            Console.WriteLine($"替换'World'为'CSharp': {text.Replace("World", "CSharp")}");
            
            // 命名空间和类型
            Console.WriteLine("\n=== 命名空间和类型 ===");
            Person person = new Person { Name = "张三", Age = 30 };
            Console.WriteLine($"Person: {person.Name}, {person.Age}");
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 函数定义
        static int Add(int a, int b)
        {
            return a + b;
        }
    }
    
    // 类定义
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }
}