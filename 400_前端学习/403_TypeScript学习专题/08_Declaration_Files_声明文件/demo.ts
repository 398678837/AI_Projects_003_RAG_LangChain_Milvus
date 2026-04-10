// TypeScript 声明文件示例

// 1. 声明全局变量
// globals.d.ts
declare var process: {
  env: {
    NODE_ENV: string;
    [key: string]: string | undefined;
  };
};

// 2. 声明全局函数
// globals.d.ts
declare function alert(message: string): void;
declare function prompt(message: string, defaultValue?: string): string | null;

// 3. 声明全局类型
// globals.d.ts
declare interface Window {
  __REDUX_DEVTOOLS_EXTENSION__?: any;
  ga?: (command: string, ...args: any[]) => void;
}

// 4. 声明模块
// lodash.d.ts
declare module 'lodash' {
  export function debounce<T extends (...args: any[]) => any>(
    func: T,
    wait: number,
    options?: {
      leading?: boolean;
      trailing?: boolean;
      maxWait?: number;
    }
  ): (...args: Parameters<T>) => void;

  export function throttle<T extends (...args: any[]) => any>(
    func: T,
    wait: number,
    options?: {
      leading?: boolean;
      trailing?: boolean;
    }
  ): (...args: Parameters<T>) => void;

  export function cloneDeep<T>(value: T): T;
}

// 5. 声明命名空间
// jquery.d.ts
declare namespace $ {
  interface JQuery {
    fadeIn(duration?: number, callback?: () => void): JQuery;
    fadeOut(duration?: number, callback?: () => void): JQuery;
    on(event: string, handler: (event: Event) => void): JQuery;
  }
}

declare function $(selector: string): $.JQuery;

// 6. 声明类
// moment.d.ts
declare class Moment {
  format(format: string): string;
  add(amount: number, unit: string): Moment;
  subtract(amount: number, unit: string): Moment;
  isBefore(date: Moment | Date): boolean;
  isAfter(date: Moment | Date): boolean;
}

declare function moment(date?: string | Date): Moment;

declare namespace moment {
  function utc(date?: string | Date): Moment;
  function unix(timestamp: number): Moment;
}

// 7. 声明枚举
// colors.d.ts
declare enum Colors {
  Red = "red",
  Green = "green",
  Blue = "blue",
}

// 8. 声明接口
// user.d.ts
declare interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

// 9. 声明类型别名
// types.d.ts
declare type StringOrNumber = string | number;
declare type Callback<T> = (error: Error | null, result: T) => void;

// 10. 声明模块增强
// express.d.ts
declare module 'express' {
  interface Request {
    user?: User;
  }
  
  interface Response {
    success(data: any): void;
    error(message: string, statusCode?: number): void;
  }
}

// 11. 声明环境模块
// ambient.d.ts
declare module '*.css' {
  const content: Record<string, string>;
  export default content;
}

declare module '*.scss' {
  const content: Record<string, string>;
  export default content;
}

declare module '*.jpg' {
  const value: string;
  export default value;
}

declare module '*.png' {
  const value: string;
  export default value;
}

// 12. 声明合并
// merged.d.ts
declare interface Person {
  name: string;
  age: number;
}

declare interface Person {
  email: string;
  address?: string;
}

// 13. 声明泛型
// generic.d.ts
declare function create<T>(value: T): T;
declare class Container<T> {
  constructor(value: T);
  get(): T;
  set(value: T): void;
}

// 14. 声明函数重载
// overloaded.d.ts
declare function process(value: string): string;
declare function process(value: number): number;
declare function process(value: boolean): boolean;

// 15. 声明可选参数和默认参数
// parameters.d.ts
declare function greet(name: string, age?: number): string;
declare function calculate(a: number, b: number, c: number = 1): number;

// 16. 声明剩余参数
// rest.d.ts
declare function sum(...numbers: number[]): number;
declare function concatenate(...strings: string[]): string;

// 17. 声明异步函数
// async.d.ts
declare function fetchData(url: string): Promise<any>;
declare async function processData(data: any): Promise<string>;

// 18. 声明生成器函数
// generator.d.ts
declare function* generateNumbers(): Generator<number, void, unknown>;

// 19. 声明装饰器
// decorator.d.ts
declare function log(target: any, propertyKey: string, descriptor: PropertyDescriptor): void;
declare function sealed(constructor: Function): void;

// 20. 声明模块导出
// module.d.ts
declare module 'my-module' {
  export const version: string;
  export function greet(name: string): string;
  export class User {
    constructor(name: string);
    getName(): string;
  }
  export default function main(): void;
}
