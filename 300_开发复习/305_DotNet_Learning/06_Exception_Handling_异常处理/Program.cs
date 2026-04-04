using System;
using System.IO;

namespace ExceptionHandling
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 异常处理 ===");
            
            // 基本异常处理
            Console.WriteLine("\n1. 基本异常处理:");
            try
            {
                int[] numbers = { 1, 2, 3 };
                Console.WriteLine(numbers[5]); // 索引越界异常
            }
            catch (IndexOutOfRangeException ex)
            {
                Console.WriteLine($"捕获到异常: {ex.Message}");
            }
            finally
            {
                Console.WriteLine("finally块执行");
            }
            
            // 多个异常处理
            Console.WriteLine("\n2. 多个异常处理:");
            try
            {
                Console.Write("请输入一个数字: ");
                string input = Console.ReadLine();
                int number = int.Parse(input);
                int result = 100 / number;
                Console.WriteLine($"100 / {number} = {result}");
            }
            catch (FormatException ex)
            {
                Console.WriteLine($"格式错误: {ex.Message}");
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"除零错误: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"其他异常: {ex.Message}");
            }
            
            // 抛出异常
            Console.WriteLine("\n3. 抛出异常:");
            try
            {
                ValidateAge(-5);
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"捕获到异常: {ex.Message}");
            }
            
            // 自定义异常
            Console.WriteLine("\n4. 自定义异常:");
            try
            {
                ProcessFile("nonexistent.txt");
            }
            catch (FileProcessingException ex)
            {
                Console.WriteLine($"文件处理异常: {ex.Message}");
                Console.WriteLine($"错误代码: {ex.ErrorCode}");
            }
            
            // 异常处理最佳实践
            Console.WriteLine("\n5. 异常处理最佳实践:");
            try
            {
                using (StreamReader reader = new StreamReader("test.txt"))
                {
                    string content = reader.ReadToEnd();
                    Console.WriteLine("文件读取成功");
                }
            }
            catch (FileNotFoundException ex)
            {
                Console.WriteLine($"文件不存在: {ex.Message}");
            }
            catch (IOException ex)
            {
                Console.WriteLine($"IO错误: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"其他错误: {ex.Message}");
            }
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 抛出异常的方法
        static void ValidateAge(int age)
        {
            if (age < 0)
            {
                throw new ArgumentException("年龄不能为负数");
            }
            Console.WriteLine($"年龄: {age}");
        }
        
        // 自定义异常
        static void ProcessFile(string filePath)
        {
            if (!File.Exists(filePath))
            {
                throw new FileProcessingException("文件不存在", 404);
            }
            
            try
            {
                using (StreamReader reader = new StreamReader(filePath))
                {
                    string content = reader.ReadToEnd();
                    Console.WriteLine("文件处理成功");
                }
            }
            catch (IOException ex)
            {
                throw new FileProcessingException("文件读取错误", 500, ex);
            }
        }
    }
    
    // 自定义异常类
    class FileProcessingException : Exception
    {
        public int ErrorCode { get; }
        
        public FileProcessingException(string message, int errorCode) : base(message)
        {
            ErrorCode = errorCode;
        }
        
        public FileProcessingException(string message, int errorCode, Exception innerException) 
            : base(message, innerException)
        {
            ErrorCode = errorCode;
        }
    }
}