// TypeScript 模块化示例

// 1. 导出声明
// math.ts
export const PI = 3.14159;

export function add(a: number, b: number): number {
  return a + b;
}

export function subtract(a: number, b: number): number {
  return a - b;
}

export function multiply(a: number, b: number): number {
  return a * b;
}

export function divide(a: number, b: number): number {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

// 2. 导入声明
// app.ts
// import { add, subtract, multiply, divide, PI } from './math';

// console.log(add(5, 3));
// console.log(subtract(5, 3));
// console.log(multiply(5, 3));
// console.log(divide(5, 3));
// console.log(PI);

// 3. 重命名导入
// import { add as sum, subtract as diff } from './math';

// console.log(sum(5, 3));
// console.log(diff(5, 3));

// 4. 导入所有
// import * as MathUtil from './math';

// console.log(MathUtil.add(5, 3));
// console.log(MathUtil.PI);

// 5. 默认导出
// user.ts
export default class User {
  constructor(public id: number, public name: string, public email: string) {}

  greet(): string {
    return `Hello, my name is ${this.name}`;
  }
}

// app.ts
// import User from './user';

// const user = new User(1, "John", "john@example.com");
// console.log(user.greet());

// 6. 混合导出
// utils.ts
export const version = "1.0.0";

export function formatDate(date: Date): string {
  return date.toISOString();
}

export default function greet(name: string): string {
  return `Hello, ${name}!`;
}

// app.ts
// import greet, { version, formatDate } from './utils';

// console.log(greet("John"));
// console.log(version);
// console.log(formatDate(new Date()));

// 7. 重新导出
// index.ts
// export { add, subtract, multiply, divide, PI } from './math';
// export { default as User } from './user';
// export { default as greet, version, formatDate } from './utils';

// 8. 模块解析
// 相对路径导入
// import { add } from './math';

// 绝对路径导入（需要配置 tsconfig.json）
// import { add } from '@/math';

// 9. 环境模块
// 声明外部模块
// declare module 'lodash' {
//   export function debounce<T extends (...args: any[]) => any>(
//     func: T,
//     wait: number
//   ): (...args: Parameters<T>) => void;
// }

// 10. 模块增强
// 增强现有模块
// declare module 'express' {
//   interface Request {
//     user?: User;
//   }
// }

// 11. 动态导入
// async function loadModule() {
//   const math = await import('./math');
//   console.log(math.add(5, 3));
// }

// loadModule();

// 12. 条件导入
// if (process.env.NODE_ENV === 'development') {
//   import('./dev-utils').then(({ log }) => {
//     log('Development mode');
//   });
// }

// 13. 命名空间
// namespace Geometry {
//   export interface Point {
//     x: number;
//     y: number;
//   }

//   export function distance(a: Point, b: Point): number {
//     const dx = a.x - b.x;
//     const dy = a.y - b.y;
//     return Math.sqrt(dx * dx + dy * dy);
//   }
// }

// const point1: Geometry.Point = { x: 0, y: 0 };
// const point2: Geometry.Point = { x: 3, y: 4 };
// console.log(Geometry.distance(point1, point2));

// 14. 模块与命名空间的结合
// module.ts
// export namespace Utils {
//   export function greet(name: string): string {
//     return `Hello, ${name}!`;
//   }
// }

// app.ts
// import { Utils } from './module';
// console.log(Utils.greet("John"));

// 15. 循环依赖
// a.ts
// import { b } from './b';
// export const a = "a";
// console.log(b);

// b.ts
// import { a } from './a';
// export const b = "b";
// console.log(a);

// 16. 模块解析策略
// tsconfig.json
/*
{
  "compilerOptions": {
    "module": "commonjs",
    "moduleResolution": "node",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
*/

// 17. 模块类型
// package.json
/*
{
  "type": "module"
}
*/

// 18. CommonJS 模块
// math.cjs
/*
const PI = 3.14159;

function add(a, b) {
  return a + b;
}

module.exports = {
  PI,
  add
};
*/

// app.js
/*
const { PI, add } = require('./math.cjs');
console.log(add(5, 3));
console.log(PI);
*/

// 19. ES 模块
// math.mjs
/*
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}
*/

// app.mjs
/*
import { PI, add } from './math.mjs';
console.log(add(5, 3));
console.log(PI);
*/

// 20. 模块打包
// 使用 webpack、rollup 等工具打包模块

// webpack.config.js
/*
module.exports = {
  entry: './src/index.ts',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
};
*/
