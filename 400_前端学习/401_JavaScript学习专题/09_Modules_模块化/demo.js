// 模块化示例

// 1. ES6 模块导出
// 导出单个变量
export const PI = 3.14;

// 导出函数
export function calculateArea(radius) {
    return PI * radius * radius;
}

// 导出多个变量
const name = "JavaScript";
const version = "ES6+";
export { name, version };

// 导出默认值
export default {
    greet: function(name) {
        return `Hello, ${name}!`;
    },
    farewell: function(name) {
        return `Goodbye, ${name}!`;
    }
};

// 2. 模块导入
// 导入单个变量
// import { PI, calculateArea } from './math.js';

// 导入多个变量
// import { name, version } from './config.js';

// 导入默认值
// import utils from './utils.js';

// 导入所有内容
// import * as math from './math.js';

// 3. CommonJS 模块（Node.js）
// 导出
// module.exports = {
//     PI: 3.14,
//     calculateArea: function(radius) {
//         return this.PI * radius * radius;
//     }
// };

// 导入
// const math = require('./math.js');

// 4. AMD 模块（RequireJS）
// 定义模块
// define(['dependency1', 'dependency2'], function(dep1, dep2) {
//     return {
//         method1: function() {
//             // 实现
//         },
//         method2: function() {
//             // 实现
//         }
//     };
// });

// 加载模块
// require(['module1', 'module2'], function(mod1, mod2) {
//     // 使用模块
// });

// 5. UMD 模块（通用模块定义）
// (function (root, factory) {
//     if (typeof define === 'function' && define.amd) {
//         // AMD
//         define(['jquery'], factory);
//     } else if (typeof module === 'object' && module.exports) {
//         // CommonJS
//         module.exports = factory(require('jquery'));
//     } else {
//         // 全局变量
//         root.myModule = factory(root.jQuery);
//     }
// }(typeof self !== 'undefined' ? self : this, function($) {
//     // 模块实现
//     return {
//         method1: function() {
//             // 实现
//         },
//         method2: function() {
//             // 实现
//         }
//     };
// }));

// 6. 模块的好处
// - 代码组织：将代码分割成多个文件
// - 命名空间：避免全局变量污染
// - 依赖管理：明确模块间的依赖关系
// - 代码复用：方便在不同项目中复用代码
// - 维护性：更容易维护和测试

// 7. 模块系统对比
// | 特性 | ES6 Modules | CommonJS | AMD |
// |------|------------|----------|-----|
// | 加载方式 | 静态（编译时） | 动态（运行时） | 动态（运行时） |
// | 适用环境 | 浏览器和Node.js | Node.js | 浏览器 |
// | 导出方式 | export, export default | module.exports | define |
// | 导入方式 | import | require | require |
// | 异步加载 | 支持 | 不支持 | 支持 |
