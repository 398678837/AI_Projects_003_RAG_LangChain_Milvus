// TypeScript 类示例

// 1. 基本类
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): string {
    return `Hello, my name is ${this.name} and I'm ${this.age} years old.`;
  }
}

const person1 = new Person("John", 30);
console.log(person1.greet());

// 2. 访问修饰符
class Employee {
  public name: string;      // 公共属性，默认
  private salary: number;    // 私有属性，只能在类内部访问
  protected department: string; // 受保护属性，可以在类和子类中访问

  constructor(name: string, salary: number, department: string) {
    this.name = name;
    this.salary = salary;
    this.department = department;
  }

  getSalary(): number {
    return this.salary;
  }

  protected getDepartment(): string {
    return this.department;
  }
}

const employee1 = new Employee("Jane", 50000, "Engineering");
console.log(employee1.name); // 可以访问
// console.log(employee1.salary); // 错误，私有属性
// console.log(employee1.department); // 错误，受保护属性
console.log(employee1.getSalary()); // 可以通过方法访问

// 3. 继承
class Manager extends Employee {
  private employees: Employee[] = [];

  constructor(name: string, salary: number, department: string) {
    super(name, salary, department);
  }

  addEmployee(employee: Employee): void {
    this.employees.push(employee);
  }

  getDepartment(): string {
    return `Manager of ${super.getDepartment()}`;
  }

  getEmployeesCount(): number {
    return this.employees.length;
  }
}

const manager = new Manager("John", 80000, "Engineering");
manager.addEmployee(employee1);
console.log(manager.getDepartment());
console.log(manager.getEmployeesCount());

// 4. 只读属性
class Product {
  readonly id: number;
  name: string;
  price: number;

  constructor(id: number, name: string, price: number) {
    this.id = id;
    this.name = name;
    this.price = price;
  }
}

const product1 = new Product(1, "Laptop", 999.99);
// product1.id = 2; // 错误，只读属性

// 5. 静态属性和方法
class MathUtil {
  static PI: number = 3.14159;

  static add(a: number, b: number): number {
    return a + b;
  }

  static multiply(a: number, b: number): number {
    return a * b;
  }
}

console.log(MathUtil.PI);
console.log(MathUtil.add(5, 3));
console.log(MathUtil.multiply(5, 3));

// 6. 抽象类
abstract class Shape {
  abstract area(): number;
  abstract perimeter(): number;

  describe(): string {
    return `This is a shape with area ${this.area()} and perimeter ${this.perimeter()}.`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }

  area(): number {
    return Math.PI * this.radius * this.radius;
  }

  perimeter(): number {
    return 2 * Math.PI * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {
    super();
  }

  area(): number {
    return this.width * this.height;
  }

  perimeter(): number {
    return 2 * (this.width + this.height);
  }
}

const circle1 = new Circle(5);
console.log(circle1.describe());

const rectangle1 = new Rectangle(10, 5);
console.log(rectangle1.describe());

// 7. 接口实现
interface Printable {
  print(): void;
}

class MyDocument implements Printable {
  constructor(private content: string) {}

  print(): void {
    console.log(this.content);
  }
}

const myDocument = new MyDocument("Hello, World!");
myDocument.print();

// 8. 构造函数简写
class User {
  constructor(
    public id: number,
    public name: string,
    public email: string
  ) {}
}

const user1 = new User(1, "John", "john@example.com");
console.log(user1.id, user1.name, user1.email);

// 9. Getter 和 Setter
class BankAccount {
  private _balance: number = 0;

  get balance(): number {
    return this._balance;
  }

  set balance(amount: number) {
    if (amount < 0) {
      throw new Error("Balance cannot be negative");
    }
    this._balance = amount;
  }

  deposit(amount: number): void {
    if (amount < 0) {
      throw new Error("Deposit amount cannot be negative");
    }
    this._balance += amount;
  }

  withdraw(amount: number): void {
    if (amount < 0) {
      throw new Error("Withdraw amount cannot be negative");
    }
    if (amount > this._balance) {
      throw new Error("Insufficient funds");
    }
    this._balance -= amount;
  }
}

const account = new BankAccount();
account.deposit(1000);
console.log(account.balance);
account.withdraw(500);
console.log(account.balance);

// 10. 类表达式
const PersonClass1 = class {
  constructor(private name: string) {}

  greet() {
    return `Hello, ${this.name}!`;
  }
};

const person3 = new PersonClass1("Jane");
console.log(person3.greet());

// 11. 泛型类
class Box<T> {
  constructor(private value: T) {}

  getValue(): T {
    return this.value;
  }

  setValue(value: T): void {
    this.value = value;
  }
}

const numberBox = new Box<number>(42);
const stringBox = new Box<string>("Hello");

// 12. 类的类型
let personType: Person;
personType = new Person("John", 30);

// 13. 类的实例类型
function createPerson(): Person {
  return new Person("John", 30);
}

// 14. 类的继承与多态
function printShape(shape: Shape): void {
  console.log(shape.describe());
}

printShape(circle1);
printShape(rectangle1);

// 15. 类的私有方法
class Calculator {
  private add(a: number, b: number): number {
    return a + b;
  }

  private subtract(a: number, b: number): number {
    return a - b;
  }

  calculate(operation: string, a: number, b: number): number {
    switch (operation) {
      case "add":
        return this.add(a, b);
      case "subtract":
        return this.subtract(a, b);
      default:
        throw new Error("Invalid operation");
    }
  }
}

const calculator = new Calculator();
console.log(calculator.calculate("add", 5, 3));
console.log(calculator.calculate("subtract", 5, 3));

// 16. 类的静态块
class Configuration {
  static readonly API_URL: string = "https://api.example.com";
  static readonly API_KEY: string = "default-api-key";
}

console.log(Configuration.API_URL);
console.log(Configuration.API_KEY);

// 17. 类的装饰器 (暂时注释掉，避免编译错误)
/*
function sealed(constructor: any) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
  return constructor;
}

@sealed
class SealedClass {
  constructor(public name: string) {}
}

// 18. 类的方法装饰器
function configurable(value: boolean) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.configurable = value;
  };
}

class DecoratedClass {
  @configurable(false)
  greet() {
    return "Hello!";
  }
}

// 19. 类的方法装饰器
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with args: ${args}`);
    const result = originalMethod.apply(this, args);
    console.log(`Called ${propertyKey} with result: ${result}`);
    return result;
  };
}

class LoggedClass {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

const logged = new LoggedClass();
logged.add(5, 3);
*/

// 20. 类的参数装饰器 (暂时注释掉，避免编译错误)
/*
function required(target: any, propertyKey: string, parameterIndex: number) {
  console.log(`Required parameter at index ${parameterIndex} in ${propertyKey}`);
}

class RequiredClass {
  greet(name: string) {
    return `Hello, ${name}!`;
  }
}

const requiredClass = new RequiredClass();
requiredClass.greet("John");
*/
