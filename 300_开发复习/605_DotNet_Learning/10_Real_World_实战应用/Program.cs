using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
using System.Configuration;
using Newtonsoft.Json;

namespace RealWorld
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("=== 实战应用 ===");
            
            // 控制台应用
            Console.WriteLine("\n1. 控制台应用:");
            ConsoleAppDemo();
            
            // 文件处理
            Console.WriteLine("\n2. 文件处理:");
            await FileProcessingDemo();
            
            // 网络请求
            Console.WriteLine("\n3. 网络请求:");
            await NetworkRequestDemo();
            
            // 数据处理
            Console.WriteLine("\n4. 数据处理:");
            DataProcessingDemo();
            
            // 配置管理
            Console.WriteLine("\n5. 配置管理:");
            ConfigurationDemo();
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        // 控制台应用
        static void ConsoleAppDemo()
        {
            Console.WriteLine("欢迎使用控制台应用");
            Console.Write("请输入您的姓名: ");
            string name = Console.ReadLine();
            Console.Write("请输入您的年龄: ");
            int age = int.Parse(Console.ReadLine());
            
            Console.WriteLine($"您好，{name}！您今年{age}岁。");
        }
        
        // 文件处理
        static async Task FileProcessingDemo()
        {
            string fileName = "data.txt";
            
            // 写入文件
            await File.WriteAllTextAsync(fileName, "Hello, File!\nThis is a test.");
            Console.WriteLine("文件写入完成");
            
            // 读取文件
            string content = await File.ReadAllTextAsync(fileName);
            Console.WriteLine("文件内容:");
            Console.WriteLine(content);
            
            // 追加内容
            await File.AppendAllTextAsync(fileName, "\n追加的内容");
            Console.WriteLine("内容追加完成");
            
            // 再次读取
            content = await File.ReadAllTextAsync(fileName);
            Console.WriteLine("追加后的内容:");
            Console.WriteLine(content);
            
            // 删除文件
            File.Delete(fileName);
            Console.WriteLine("文件已删除");
        }
        
        // 网络请求
        static async Task NetworkRequestDemo()
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    // 设置超时
                    client.Timeout = TimeSpan.FromSeconds(10);
                    
                    // 发送GET请求
                    HttpResponseMessage response = await client.GetAsync("https://jsonplaceholder.typicode.com/posts/1");
                    
                    // 检查响应状态
                    if (response.IsSuccessStatusCode)
                    {
                        // 读取响应内容
                        string content = await response.Content.ReadAsStringAsync();
                        
                        // 解析JSON
                        Post post = JsonConvert.DeserializeObject<Post>(content);
                        Console.WriteLine("网络请求结果:");
                        Console.WriteLine($"ID: {post.Id}");
                        Console.WriteLine($"标题: {post.Title}");
                        Console.WriteLine($"内容: {post.Body}");
                    }
                    else
                    {
                        Console.WriteLine($"请求失败: {response.StatusCode}");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"网络请求异常: {ex.Message}");
            }
        }
        
        // 数据处理
        static void DataProcessingDemo()
        {
            // 模拟数据
            List<Employee> employees = new List<Employee>
            {
                new Employee { Id = 1, Name = "张三", Department = "技术部", Salary = 8000 },
                new Employee { Id = 2, Name = "李四", Department = "市场部", Salary = 6000 },
                new Employee { Id = 3, Name = "王五", Department = "技术部", Salary = 9000 },
                new Employee { Id = 4, Name = "赵六", Department = "财务部", Salary = 7000 },
                new Employee { Id = 5, Name = "钱七", Department = "技术部", Salary = 8500 }
            };
            
            // 数据过滤
            var techEmployees = employees.Where(e => e.Department == "技术部");
            Console.WriteLine("技术部员工:");
            foreach (var emp in techEmployees)
            {
                Console.WriteLine($"{emp.Name} - {emp.Salary}");
            }
            
            // 数据排序
            var sortedBySalary = employees.OrderByDescending(e => e.Salary);
            Console.WriteLine("\n按工资降序排序:");
            foreach (var emp in sortedBySalary)
            {
                Console.WriteLine($"{emp.Name} - {emp.Salary}");
            }
            
            // 数据聚合
            double averageSalary = employees.Average(e => e.Salary);
            Console.WriteLine($"\n平均工资: {averageSalary}");
        }
        
        // 配置管理
        static void ConfigurationDemo()
        {
            // 读取配置文件
            var appSettings = ConfigurationManager.AppSettings;
            
            // 输出配置项
            Console.WriteLine("配置项:");
            foreach (var key in appSettings.AllKeys)
            {
                Console.WriteLine($"{key}: {appSettings[key]}");
            }
            
            // 模拟配置使用
            string connectionString = appSettings["ConnectionString"] ?? "默认连接字符串";
            Console.WriteLine($"\n连接字符串: {connectionString}");
        }
    }
    
    // 网络请求模型
    class Post
    {
        public int UserId { get; set; }
        public int Id { get; set; }
        public string Title { get; set; }
        public string Body { get; set; }
    }
    
    // 数据处理模型
    class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Department { get; set; }
        public decimal Salary { get; set; }
    }
}