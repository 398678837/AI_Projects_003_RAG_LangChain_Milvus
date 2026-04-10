// TypeScript 最佳实践示例

// 1. 使用类型别名和接口
interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

type UserId = number;
type UserName = string;

type UserWithId = User & {
  id: UserId;
};

// 2. 使用泛型
function identity<T>(value: T): T {
  return value;
}

function createArray<T>(length: number, value: T): T[] {
  return Array(length).fill(value);
}

// 3. 使用类型守卫
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

// 4. 使用可选链和空值合并
interface Person {
  name: string;
  address?: {
    street?: string;
    city?: string;
    country?: string;
  };
}

const person: Person = { name: "John" };
const city = person.address?.city ?? "Unknown";

// 5. 使用严格模式
// tsconfig.json 中设置 "strict": true

// 6. 使用 readonly 修饰符
interface ReadonlyUser {
  readonly id: number;
  readonly name: string;
  email: string;
}

const readonlyUser: ReadonlyUser = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// 7. 使用枚举类型
enum Status {
  Active = "active",
  Inactive = "inactive",
  Pending = "pending",
}

const userStatus: Status = Status.Active;

// 8. 使用接口继承
interface Shape {
  name: string;
  area(): number;
}

interface Circle extends Shape {
  radius: number;
}

interface Rectangle extends Shape {
  width: number;
  height: number;
}

// 9. 使用类型参数约束
interface Lengthy {
  length: number;
}

function getLength<T extends Lengthy>(value: T): number {
  return value.length;
}

// 10. 使用条件类型
type NonNullable<T> = T extends null | undefined ? never : T;
type Extract<T, U> = T extends U ? T : never;
type Exclude<T, U> = T extends U ? never : T;

// 11. 使用映射类型
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

type Partial<T> = {
  [P in keyof T]?: T[P];
};

type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

type Omit<T, K extends keyof T> = {
  [P in Exclude<keyof T, K>]: T[P];
};

// 12. 使用索引类型
type UserKeys = keyof User;
type UserIdType = User["id"];

// 13. 使用模板字面量类型
type EventName<T extends string> = `${T}Changed`;
type UserEvent = EventName<"user">;

// 14. 使用异步/等待
async function fetchData(url: string): Promise<any> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}

// 15. 使用 try/catch/finally
async function processData() {
  try {
    const data = await fetchData("https://api.example.com/data");
    console.log(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    console.log("Process completed");
  }
}

// 16. 使用模块化
// user.ts
export interface User {
  id: number;
  name: string;
  email: string;
}

export function createUser(id: number, name: string, email: string): User {
  return { id, name, email };
}

// 17. 使用装饰器
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with args: ${args}`);
    const result = originalMethod.apply(this, args);
    console.log(`Called ${propertyKey} with result: ${result}`);
    return result;
  };
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

// 18. 使用命名空间
namespace Utils {
  export function formatDate(date: Date): string {
    return date.toISOString();
  }

  export function formatCurrency(amount: number): string {
    return `$${amount.toFixed(2)}`;
  }
}

// 19. 使用类型断言
const anyValue: any = "Hello";
const stringValue = anyValue as string;
const length = stringValue.length;

// 20. 使用配置文件
// tsconfig.json
/*
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
*/

// 21. 使用 ESLint 和 Prettier
// .eslintrc.json
/*
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint"],
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-explicit-any": "error"
  }
}
*/

// .prettierrc
/*
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
*/

// 22. 使用 Jest 进行测试
// sum.test.ts
/*
import { sum } from './sum';

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
*/

// 23. 使用路径别名
// tsconfig.json
/*
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
*/

// 24. 使用环境变量
// .env
/*
NODE_ENV=development
API_URL=http://localhost:3000/api
*/

// 25. 使用增量编译
// tsconfig.json
/*
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": "./dist/.tsbuildinfo"
  }
}
*/
