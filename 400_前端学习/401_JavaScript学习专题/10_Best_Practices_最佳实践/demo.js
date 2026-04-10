// JavaScript 最佳实践示例

// 1. 变量声明
// 使用 const 和 let，避免 var
const PI = 3.14;
let count = 0;

// 2. 函数
// 使用箭头函数
const add = (a, b) => a + b;

// 函数参数默认值
function greet(name = 'Guest') {
    return `Hello, ${name}!`;
}

// 3. 对象
// 使用对象简写
const name = 'JavaScript';
const version = 'ES6+';
const obj = { name, version };

// 使用解构赋值
const { name: objName, version: objVersion } = obj;

// 4. 数组
// 使用扩展运算符
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const combinedArray = [...array1, ...array2];

// 使用数组方法
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
const evenNumbers = numbers.filter(num => num % 2 === 0);
const sum = numbers.reduce((acc, num) => acc + num, 0);

// 5. 错误处理
// 使用 try/catch/finally
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    } finally {
        console.log('Fetch completed');
    }
}

// 6. 代码风格
// 缩进：使用 4 个空格
// 命名：变量和函数使用驼峰命名法
// 常量：使用大写字母和下划线
// 分号：使用分号

// 7. 性能优化
// 避免频繁的 DOM 操作
function updateDOM() {
    const container = document.getElementById('container');
    const fragment = document.createDocumentFragment();
    
    for (let i = 0; i < 1000; i++) {
        const div = document.createElement('div');
        div.textContent = `Item ${i}`;
        fragment.appendChild(div);
    }
    
    container.appendChild(fragment);
}

// 避免使用 eval
// 不好的做法
// const result = eval('1 + 2');

// 好的做法
const result = 1 + 2;

// 8. 安全
// 避免 XSS 攻击
function escapeHtml(text) {
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// 9. 模块化
// 使用 ES6 模块
// export const utils = {
//     formatDate: function(date) {
//         return new Date(date).toISOString();
//     }
// };

// 10. 测试
// 使用测试框架
// describe('Utils', () => {
//     test('formatDate should format date correctly', () => {
//         const date = new Date('2023-01-01');
//         expect(utils.formatDate(date)).toBe('2023-01-01T00:00:00.000Z');
//     });
// });

// 11. 注释
// 函数注释
/**
 * Adds two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Sum of the two numbers
 */
function addNumbers(a, b) {
    return a + b;
}

// 12. 代码组织
// 按功能组织代码
// 按字母顺序排序导入
// 分离关注点

// 13. 浏览器兼容性
// 使用 Babel 转译
// 使用 polyfill
// 测试不同浏览器

// 14. 性能监控
// 使用浏览器开发者工具
// 使用 Lighthouse
// 监控页面加载时间

// 15. 版本控制
// 使用 Git
// 提交有意义的 commit 信息
// 分支管理
