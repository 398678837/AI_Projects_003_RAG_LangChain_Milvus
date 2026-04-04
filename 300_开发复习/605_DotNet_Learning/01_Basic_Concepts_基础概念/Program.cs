using System;

namespace BasicConcepts
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 基本数据类型 ===");
            
            // 基本数据类型
            bool b = true;
            char c = 'A';
            int i = 10;
            float f = 3.14f;
            double d = 3.14159;
            string s = "Hello, C#!";
            
            Console.WriteLine($"bool: {b}");
            Console.WriteLine($"char: {c}");
            Console.WriteLine($"int: {i}");
            Console.WriteLine($"float: {f}");
            Console.WriteLine($"double: {d}");
            Console.WriteLine($"string: {s}");
            
            Console.WriteLine("\n=== 变量和常量 ===");
            
            // 变量和常量
            int age = 25;
            const double PI = 3.14159;
            
            Console.WriteLine($"age: {age}");
            Console.WriteLine($"PI: {PI}");
            
            Console.WriteLine("\n=== 运算符 ===");
            
            // 运算符
            int a = 10, e = 3;
            Console.WriteLine($"a + e: {a + e}");
            Console.WriteLine($"a - e: {a - e}");
            Console.WriteLine($"a * e: {a * e}");
            Console.WriteLine($"a / e: {a / e}");
            Console.WriteLine($"a % e: {a % e}");
            
            Console.WriteLine("\n=== 输入输出 ===");
            
            // 输入输出
            Console.Write("请输入一个数字: ");
            string input = Console.ReadLine();
            if (int.TryParse(input, out int num))
            {
                Console.WriteLine($"你输入的数字是: {num}");
            }
            else
            {
                Console.WriteLine("输入无效，请输入一个数字。");
            }
            
            Console.WriteLine("\n=== 类型转换 ===");
            
            // 类型转换
            int intValue = 100;
            double doubleValue = intValue; // 隐式转换
            intValue = (int)doubleValue; // 显式转换
            
            Console.WriteLine($"intValue: {intValue}");
            Console.WriteLine($"doubleValue: {doubleValue}");
            
            Console.WriteLine("\n=== 字符串操作 ===");
            
            // 字符串操作
            string str1 = "Hello";
            string str2 = "World";
            string str3 = str1 + " " + str2;
            
            Console.WriteLine($"str3: {str3}");
            Console.WriteLine($"str3.Length: {str3.Length}");
            Console.WriteLine($"str3.Substring(0, 5): {str3.Substring(0, 5)}");
            Console.WriteLine($"str3.ToUpper(): {str3.ToUpper()}");
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
    }
}