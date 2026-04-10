// TypeScript 类型系统示例

// 1. 基本类型
let str1: string = "Hello";
let num1: number = 42;
let bool: boolean = true;
let undef: undefined = undefined;
let nul: null = null;
let sym: symbol = Symbol("unique");
// let bigInt: bigint = 100n; // BigInt requires ES2020+

// 2. 数组类型
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// 3. 元组类型
let tuple: [string, number, boolean] = ["Hello", 42, true];

// 4. 枚举类型
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

let dir: Direction = Direction.Up;

// 5. 字面量类型
type Color = "red" | "green" | "blue";
let color: Color = "red";

type Size = 1 | 2 | 3 | 4 | 5;
let size: Size = 3;

// 6. 联合类型
let value: string | number | boolean = "Hello";
value = 42;
value = true;

// 7. 交叉类型
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

// 8. 类型别名
type StringOrNumber = string | number;
let sn: StringOrNumber = "Hello";
sn = 42;

type User = {
  id: number;
  name: string;
  email: string;
};

let user: User = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// 9. 类型断言
let someValue: unknown = "Hello";
let strLength: number = (someValue as string).length;
let strLength2: number = (<string>someValue).length;

// 10. 类型守卫
function isString(value: any): value is string {
  return typeof value === "string";
}

function isNumber(value: any): value is number {
  return typeof value === "number";
}

function processValue(value: string | number) {
  if (isString(value)) {
    return value.toUpperCase();
  } else if (isNumber(value)) {
    return value * 2;
  }
  return value;
}

// 11. 类型保护
function getLength1(value: string | number): number {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value.toString().length;
  }
}

// 12. 类型推断
let inferredString = "Hello";
// inferredString = 42; // 错误，类型推断为string

let inferredNumber = 42;
// inferredNumber = "Hello"; // 错误，类型推断为number

// 13. 类型兼容性
interface Shape {
  name: string;
}

interface Circle extends Shape {
  radius: number;
}

let shape: Shape = {
  name: "Shape",
};

let circle: Circle = {
  name: "Circle",
  radius: 5,
};

shape = circle; // 兼容，Circle 是 Shape 的子类型

// 14. 类型收窄
function narrowType(value: string | number | null) {
  if (value === null) {
    return "Value is null";
  }
  
  if (typeof value === "string") {
    return `String length: ${value.length}`;
  }
  
  return `Number value: ${value}`;
}

// 15. 类型谓词
interface Dog {
  bark(): void;
}

interface Cat {
  meow(): void;
}

function isDog(animal: Dog | Cat): animal is Dog {
  return (animal as Dog).bark !== undefined;
}

function makeSound(animal: Dog | Cat) {
  if (isDog(animal)) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// 16. 索引签名
interface StringMap {
  [key: string]: string;
}

let map: StringMap = {
  a: "Hello",
  b: "World",
};

// 17. 函数重载
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any): any {
  return a + b;
}

const sum = add(1, 2); // 类型为number
const concatenated = add("Hello", "World"); // 类型为string

// 18. 泛型函数
function identity<T>(value: T): T {
  return value;
}

const num2 = identity<number>(42);
const str2 = identity<string>("Hello");

// 19. 泛型约束
interface Lengthy {
  length: number;
}

function getLength<T extends Lengthy>(value: T): number {
  return value.length;
}

const arrLength = getLength([1, 2, 3]);
const strLength3 = getLength("Hello");

// 20. 类型参数推断
function createPair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

const pair = createPair(1, "Hello"); // 类型为 [number, string]
