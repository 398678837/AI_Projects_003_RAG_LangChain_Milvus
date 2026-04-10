// TypeScript 泛型示例

// 1. 泛型函数
function identity<T>(value: T): T {
  return value;
}

const num = identity<number>(42);
const str = identity<string>("Hello");
const bool = identity<boolean>(true);

// 2. 泛型函数类型推断
const inferredNum = identity(42); // 类型推断为 number
const inferredStr = identity("Hello"); // 类型推断为 string

// 3. 多个泛型参数
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

const stringNumberPair = pair("Hello", 42); // 类型为 [string, number]
const booleanArrayPair = pair(true, [1, 2, 3]); // 类型为 [boolean, number[]]

// 4. 泛型约束
interface Lengthy {
  length: number;
}

function getLength<T extends Lengthy>(value: T): number {
  return value.length;
}

const strLength = getLength("Hello"); // 5
const arrLength = getLength([1, 2, 3]); // 3
// getLength(42); // 错误，number 没有 length 属性

// 5. 泛型类
class Box<T> {
  private value: T;

  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }

  setValue(value: T): void {
    this.value = value;
  }
}

const numberBox = new Box<number>(42);
const stringBox = new Box<string>("Hello");

// 6. 泛型接口
interface Repository<T> {
  findById(id: number): T | undefined;
  save(item: T): void;
  delete(id: number): void;
}

class UserRepository implements Repository<User> {
  private users: User[] = [];

  findById(id: number): User | undefined {
    return this.users.find(user => user.id === id);
  }

  save(item: User): void {
    this.users.push(item);
  }

  delete(id: number): void {
    this.users = this.users.filter(user => user.id !== id);
  }
}

interface User {
  id: number;
  name: string;
  email: string;
}

// 7. 泛型类型别名
type Result<T> = {
  success: boolean;
  data: T;
  error?: string;
};

const successResult: Result<User> = {
  success: true,
  data: { id: 1, name: "John", email: "john@example.com" },
};

const errorResult: Result<User> = {
  success: false,
  data: undefined as any,
  error: "User not found",
};

// 8. 泛型默认类型
function createArray<T = string>(length: number, value: T): T[] {
  return Array(length).fill(value);
}

const stringArray = createArray(3, "Hello"); // string[]
const numberArray = createArray<number>(3, 42); // number[]

// 9. 泛型与映射类型
interface User2 {
  id: number;
  name: string;
  email: string;
}

type ReadonlyUser = {
  readonly [K in keyof User2]: User2[K];
};

const readonlyUser: ReadonlyUser = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// readonlyUser.name = "Jane"; // 错误，属性是只读的

// 10. 泛型与条件类型
type NonNullable<T> = T extends null | undefined ? never : T;

const nonNullableString: NonNullable<string | null | undefined> = "Hello";
// const nonNullableNull: NonNullable<string | null | undefined> = null; // 错误

// 11. 泛型与类型推断
function inferType<T>(value: T): T {
  return value;
}

const inferredType = inferType({ id: 1, name: "John" });
// 类型推断为 { id: number; name: string; }

// 12. 泛型与函数重载
function process<T>(value: T): T;
function process<T>(value: T[]): T[];
function process<T>(value: T | T[]): T | T[] {
  if (Array.isArray(value)) {
    return value.map(item => item);
  }
  return value;
}

const processedValue = process(42); // number
const processedArray = process([1, 2, 3]); // number[]

// 13. 泛型与联合类型
function union<T extends string | number>(value: T): T {
  return value;
}

const unionString = union("Hello"); // string
const unionNumber = union(42); // number
// const unionBoolean = union(true); // 错误，boolean 不是 string | number

// 14. 泛型与交叉类型
interface A {
  a: string;
}

interface B {
  b: number;
}

function combine<T extends A, U extends B>(a: T, b: U): T & U {
  return { ...a, ...b };
}

const combined = combine({ a: "Hello" }, { b: 42 }); // A & B

// 15. 泛型与索引类型
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user1 = { id: 1, name: "John", email: "john@example.com" };
const userId = getProperty(user1, "id"); // number
const userName = getProperty(user1, "name"); // string
// const userAge = getProperty(user1, "age"); // 错误，age 不是 user1 的属性

// 16. 泛型与递归类型
type TreeNode<T> = {
  value: T;
  children?: TreeNode<T>[];
};

const tree: TreeNode<number> = {
  value: 1,
  children: [
    {
      value: 2,
      children: [
        { value: 3 },
        { value: 4 },
      ],
    },
    { value: 5 },
  ],
};

// 17. 泛型与 Promise
async function fetchData<T>(url: string): Promise<T> {
  const response = await fetch(url);
  return response.json() as T;
}

// 用法：const user = await fetchData<User>("/api/user");

// 18. 泛型与工厂函数
function createInstance<T>(constructor: new () => T): T {
  return new constructor();
}

class Person {
  name = "";
  age = 0;
}

const person = createInstance(Person); // Person

// 19. 泛型与装饰器
function log<T extends { new (...args: any[]): {} }>(constructor: T) {
  return class extends constructor {
    constructor(...args: any[]) {
      super(...args);
      console.log(`Created instance of ${constructor.name}`);
    }
  };
}

@log
class UserClass {
  constructor(public name: string) {}
}

const userInstance = new UserClass("John"); // 输出: Created instance of UserClass

// 20. 泛型与模块
// module.ts
export function genericFunction<T>(value: T): T {
  return value;
}

// 使用: import { genericFunction } from './module';
// const result = genericFunction<string>("Hello");
