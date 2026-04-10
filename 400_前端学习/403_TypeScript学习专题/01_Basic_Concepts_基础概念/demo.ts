// TypeScript 基础概念示例

// 1. 类型注解
let name: string = "TypeScript";
let age: number = 5;
let isActive: boolean = true;

// 2. 变量声明
const PI: number = 3.14;
let message: string = "Hello, TypeScript!";

// 3. 函数类型
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const add = (a: number, b: number): number => {
  return a + b;
};

// 4. 数组类型
let numbers: number[] = [1, 2, 3, 4, 5];
let fruits: string[] = ["apple", "banana", "orange"];

// 5. 元组类型
let person: [string, number] = ["John", 30];

// 6. 枚举类型
enum Color {
  Red,
  Green,
  Blue,
}

let favoriteColor: Color = Color.Blue;

// 7. 任意类型
let anyValue: any = "Hello";
anyValue = 42;
anyValue = true;

// 8. 空类型
function logMessage(message: string): void {
  console.log(message);
}

// 9. 类型断言
let someValue: unknown = "Hello";
let strLength: number = (someValue as string).length;

// 10. 接口
interface User {
  id: number;
  name: string;
  email: string;
  age?: number; // 可选属性
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// 11. 类
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

// 12. 泛型
function identity<T>(value: T): T {
  return value;
}

const num = identity<number>(42);
const str = identity<string>("Hello");

// 13. 类型守卫
function isNumber(value: any): value is number {
  return typeof value === "number";
}

function processValue(value: number | string) {
  if (isNumber(value)) {
    return value * 2;
  } else {
    return value.toUpperCase();
  }
}

// 14. 联合类型
let result: number | string = 42;
result = "Hello";

// 15. 交叉类型
interface A {
  a: string;
}

interface B {
  b: number;
}

let ab: A & B = {
  a: "Hello",
  b: 42,
};

// 16. 类型别名
type StringOrNumber = string | number;

let value: StringOrNumber = "Hello";
value = 42;

// 17. 字面量类型
type Direction = "up" | "down" | "left" | "right";

let direction: Direction = "up";

// 18. 非空断言
let nullableValue: string | null = "Hello";
let length: number = nullableValue!.length;

// 19. 可选链
interface IPerson {
  name: string;
  address?: {
    street: string;
    city: string;
  };
}

const person2: IPerson = { name: "John" };
const city = person2.address?.city;

// 20. 空值合并运算符
let username: string | null = null;
let displayName = username ?? "Guest";
