using System;

namespace ObjectOriented
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== 面向对象编程 ===");
            
            // 创建对象
            Person person = new Person("张三", 30);
            Console.WriteLine(person.ToString());
            
            // 调用方法
            person.SayHello();
            
            // 继承
            Student student = new Student("李四", 20, "计算机科学");
            Console.WriteLine(student.ToString());
            student.SayHello();
            student.Study();
            
            // 多态
            Console.WriteLine("\n=== 多态 ===");
            Person[] people = new Person[2];
            people[0] = person;
            people[1] = student;
            
            foreach (Person p in people)
            {
                p.SayHello();
                // 类型转换
                if (p is Student)
                {
                    ((Student)p).Study();
                }
            }
            
            // 抽象类和接口
            Console.WriteLine("\n=== 抽象类和接口 ===");
            Dog dog = new Dog("旺财");
            Cat cat = new Cat("咪咪");
            
            dog.MakeSound();
            dog.Eat();
            
            cat.MakeSound();
            cat.Eat();
            
            // 封装
            Console.WriteLine("\n=== 封装 ===");
            BankAccount account = new BankAccount("123456", 1000);
            Console.WriteLine($"初始余额: {account.Balance}");
            account.Deposit(500);
            Console.WriteLine($"存款后余额: {account.Balance}");
            account.Withdraw(200);
            Console.WriteLine($"取款后余额: {account.Balance}");
            
            // 静态成员
            Console.WriteLine("\n=== 静态成员 ===");
            Console.WriteLine($"Person.Count: {Person.Count}");
            
            Console.WriteLine("\n=== 结束 ===");
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
    }
    
    // 基类
    class Person
    {
        // 静态成员
        public static int Count { get; private set; }
        
        // 属性
        public string Name { get; set; }
        public int Age { get; set; }
        
        // 构造函数
        public Person(string name, int age)
        {
            Name = name;
            Age = age;
            Count++;
        }
        
        // 方法
        public virtual void SayHello()
        {
            Console.WriteLine($"你好，我是{Name}，今年{Age}岁。");
        }
        
        // 重写ToString方法
        public override string ToString()
        {
            return $"Person: {Name}, {Age}";
        }
    }
    
    // 派生类
    class Student : Person
    {
        // 新增属性
        public string Major { get; set; }
        
        // 构造函数
        public Student(string name, int age, string major) : base(name, age)
        {
            Major = major;
        }
        
        // 重写方法
        public override void SayHello()
        {
            Console.WriteLine($"你好，我是{Name}，今年{Age}岁，专业是{Major}。");
        }
        
        // 新增方法
        public void Study()
        {
            Console.WriteLine($"{Name}正在学习{Major}。");
        }
        
        // 重写ToString方法
        public override string ToString()
        {
            return $"Student: {Name}, {Age}, {Major}";
        }
    }
    
    // 抽象类
    abstract class Animal
    {
        public string Name { get; set; }
        
        public Animal(string name)
        {
            Name = name;
        }
        
        // 抽象方法
        public abstract void MakeSound();
        
        // 非抽象方法
        public void Eat()
        {
            Console.WriteLine($"{Name}正在吃东西。");
        }
    }
    
    // 实现抽象类
    class Dog : Animal
    {
        public Dog(string name) : base(name) { }
        
        public override void MakeSound()
        {
            Console.WriteLine($"{Name}汪汪叫。");
        }
    }
    
    // 实现抽象类
    class Cat : Animal
    {
        public Cat(string name) : base(name) { }
        
        public override void MakeSound()
        {
            Console.WriteLine($"{Name}喵喵叫。");
        }
    }
    
    // 封装
    class BankAccount
    {
        // 私有字段
        private string accountNumber;
        private decimal balance;
        
        // 构造函数
        public BankAccount(string accountNumber, decimal initialBalance)
        {
            this.accountNumber = accountNumber;
            this.balance = initialBalance;
        }
        
        // 属性
        public string AccountNumber => accountNumber;
        public decimal Balance => balance;
        
        // 方法
        public void Deposit(decimal amount)
        {
            if (amount > 0)
            {
                balance += amount;
            }
        }
        
        public void Withdraw(decimal amount)
        {
            if (amount > 0 && amount <= balance)
            {
                balance -= amount;
            }
        }
    }
}