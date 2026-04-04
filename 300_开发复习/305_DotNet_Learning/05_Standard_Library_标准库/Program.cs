using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

namespace StandardLibrary
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("=== 集合类 ===");
            
            // 列表
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
            numbers.Add(6);
            numbers.Remove(3);
            Console.WriteLine("List<int>:");
            foreach (var num in numbers)
            {
                Console.Write($"{num} ");
            }
            Console.WriteLine();
            
            // 字典
            Dictionary<string, int> ages = new Dictionary<string, int>
            {
                { "张三", 30 },
                { "李四", 25 },
                { "王五", 35 }
            };
            ages["赵六"] = 28;
            Console.WriteLine("\nDictionary<string, int>:");
            foreach (var kvp in ages)
            {
                Console.WriteLine($"{kvp.Key}: {kvp.Value}");
            }
            
            // 集合
            HashSet<string> fruits = new HashSet<string> { "苹果", "香蕉", "橙子" };
            fruits.Add("葡萄");
            fruits.Add("苹果"); // 重复元素不会添加
            Console.WriteLine("\nHashSet<string>:");
            foreach (var fruit in fruits)
            {
                Console.Write($"{fruit} ");
            }
            Console.WriteLine();
            
            // 字符串处理
            Console.WriteLine("\n=== 字符串处理 ===");
            string text = "Hello, C# World!";
            Console.WriteLine($"原始字符串: {text}");
            Console.WriteLine($"长度: {text.Length}");
            Console.WriteLine($"大写: {text.ToUpper()}");
            Console.WriteLine($"小写: {text.ToLower()}");
            Console.WriteLine($"替换'World'为'CSharp': {text.Replace("World", "CSharp")}");
            Console.WriteLine($"分割: {string.Join(", ", text.Split(' '))}");
            
            // 日期时间
            Console.WriteLine("\n=== 日期时间 ===");
            DateTime now = DateTime.Now;
            Console.WriteLine($"当前时间: {now}");
            Console.WriteLine($"日期: {now.Date}");
            Console.WriteLine($"时间: {now.TimeOfDay}");
            Console.WriteLine($"年: {now.Year}");
            Console.WriteLine($"月: {now.Month}");
            Console.WriteLine($"日: {now.Day}");
            Console.WriteLine($"格式化: {now.ToString("yyyy-MM-dd HH:mm:ss")}");
            
            // 文件操作
            Console.WriteLine("\n=== 文件操作 ===");
            string fileName = "test.txt";
            
            // 写入文件
            File.WriteAllText(fileName, "Hello, File!\nThis is a test.");
            Console.WriteLine("文件写入完成。");
            
            // 读取文件
            string content = File.ReadAllText(fileName);
            Console.WriteLine("文件内容:");
            Console.WriteLine(content);
            
            // 删除文件
            File.Delete(fileName);
            Console.WriteLine("文件已删除。");
            
            // 正则表达式
            Console.WriteLine("\n=== 正则表达式 ===");
            string input = "邮箱: test@example.com, 电话: 13812345678";
            Regex emailRegex = new Regex(@"\w+@\w+\.\w+");
            Regex phoneRegex = new Regex(@"1[3-9]\d{9}");
            
            Match emailMatch = emailRegex.Match(input);
            if (emailMatch.Success)
            {
                Console.WriteLine($"邮箱: {emailMatch.Value}");
            }
            
            Match phoneMatch = phoneRegex.Match(input);
            if (phoneMatch.Success)
            {
                Console.WriteLine($"电话: {phoneMatch.Value}");
            }
            
            // LINQ
            Console.WriteLine("\n=== LINQ ===");
            int[] linqNumbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            
            // 过滤
            var evenNumbers = from num in linqNumbers where num % 2 == 0 select num;
            Console.WriteLine("偶数:");
            foreach (var num in evenNumbers)
            {
                Console.Write($"{num} ");
            }
            Console.WriteLine();
            
            // 排序
            var sortedNumbers = from num in linqNumbers orderby num descending select num;
            Console.WriteLine("降序排序:");
            foreach (var num in sortedNumbers)
            {
                Console.Write($"{num} ");
            }
            Console.WriteLine();
            
            // 聚合
            int sum = linqNumbers.Sum();
            double average = linqNumbers.Average();
            Console.WriteLine($"总和: {sum}, 平均值: {average}");
            
            // 网络请求
            Console.WriteLine("\n=== 网络请求 ===");
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    string response = await client.GetStringAsync("https://api.github.com/users/octocat");
                    Console.WriteLine("GitHub API响应: ");
                    Console.WriteLine(response.Substring(0, Math.Min(200, response.Length)) + "...");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"网络请求失败: {ex.Message}");
            }
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
    }
}