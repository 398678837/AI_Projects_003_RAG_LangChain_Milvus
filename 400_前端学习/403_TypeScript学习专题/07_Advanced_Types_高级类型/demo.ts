// TypeScript 高级类型示例

// 1. 交叉类型
interface A {
  a: string;
}

interface B {
  b: number;
}

interface C {
  c: boolean;
}

const abc: A & B & C = {
  a: "Hello",
  b: 42,
  c: true,
};

// 2. 联合类型
let value: string | number | boolean = "Hello";
value = 42;
value = true;

// 3. 类型守卫
function isString(value: any): value is string {
  return typeof value === "string";
}

function isNumber(value: any): value is number {
  return typeof value === "number";
}

function processValue(value: string | number | boolean) {
  if (isString(value)) {
    return value.toUpperCase();
  } else if (isNumber(value)) {
    return value * 2;
  } else {
    return value;
  }
}

// 4. 类型谓词
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

// 5. 类型保护
function getLength(value: string | number): number {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value.toString().length;
  }
}

// 6. 类型别名
type StringOrNumber = string | number;
type User = {
  id: number;
  name: string;
  email: string;
};

// 7. 字面量类型
type Direction = "up" | "down" | "left" | "right";
type Size = 1 | 2 | 3 | 4 | 5;

const direction: Direction = "up";
const size: Size = 3;

// 8. 映射类型
interface User {
  id: number;
  name: string;
  email: string;
}

type ReadonlyUser = {
  readonly [K in keyof User]: User[K];
};

type PartialUser = {
  [K in keyof User]?: User[K];
};

type PickUser = Pick<User, "id" | "name">;
type OmitUser = Omit<User, "email">;

// 9. 条件类型
type NonNullable<T> = T extends null | undefined ? never : T;
type Extract<T, U> = T extends U ? T : never;
type Exclude<T, U> = T extends U ? never : T;

type StringOrNumberOnly = Extract<string | number | boolean, string | number>; // string | number
type NotString = Exclude<string | number | boolean, string>; // number | boolean

// 10. 分布式条件类型
type ToArray<T> = T extends any ? T[] : never;
type StringArrayOrNumberArray = ToArray<string | number>; // string[] | number[]

// 11. 类型推断
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
type Parameters<T> = T extends (...args: infer P) => any ? P : never;

function add(a: number, b: number): number {
  return a + b;
}

type AddReturnType = ReturnType<typeof add>; // number
type AddParameters = Parameters<typeof add>; // [number, number]

// 12. 索引类型
type UserKeys = keyof User; // "id" | "name" | "email"
type UserIdType = User["id"]; // number
type UserNameType = User["name"]; // string

// 13. 模板字面量类型
type EventName<T extends string> = `${T}Changed`;
type UserEvent = EventName<"user">; // "userChanged"
type PasswordEvent = EventName<"password">; // "passwordChanged"

// 14. 递归类型
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

// 15. 条件类型与映射类型结合
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

interface Person {
  name: string;
  address: {
    street: string;
    city: string;
  };
}

type ReadonlyPerson = DeepReadonly<Person>;

// 16. 类型参数约束
type Constrained<T extends { length: number }> = T;

const constrainedString: Constrained<string> = "Hello";
const constrainedArray: Constrained<number[]> = [1, 2, 3];

// 17. 类型参数默认值
type GenericWithDefault<T = string> = T;

const defaultString: GenericWithDefault = "Hello";
const defaultNumber: GenericWithDefault<number> = 42;

// 18. 类型断言函数
function assertIsString(value: any): asserts value is string {
  if (typeof value !== "string") {
    throw new Error("Value is not a string");
  }
}

function processString(value: any) {
  assertIsString(value);
  return value.toUpperCase();
}

// 19. 可调用类型
type Func = {
  (a: number, b: number): number;
  description: string;
};

const addFunc: Func = (a, b) => a + b;
addFunc.description = "Adds two numbers";

// 20. 构造函数类型
type Constructor<T> = new (...args: any[]) => T;

class PersonClass {
  constructor(public name: string) {}
}

function createInstance<T>(ctor: Constructor<T>, ...args: any[]): T {
  return new ctor(...args);
}

const person = createInstance(PersonClass, "John");
