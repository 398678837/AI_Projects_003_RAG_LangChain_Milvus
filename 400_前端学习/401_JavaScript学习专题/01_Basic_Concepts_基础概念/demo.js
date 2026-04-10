// JavaScript 基础概念示例

// 变量声明
let name = "JavaScript";
const version = "ES6+";
var author = "ECMA International";

// 数据类型
const number = 42;
const string = "Hello World";
const boolean = true;
const nullValue = null;
const undefinedValue = undefined;
const object = { key: "value" };
const array = [1, 2, 3];

// 运算符
const sum = 10 + 5;
const difference = 10 - 5;
const product = 10 * 5;
const quotient = 10 / 5;
const remainder = 10 % 3;

// 控制流
if (sum > 10) {
    console.log("Sum is greater than 10");
} else {
    console.log("Sum is not greater than 10");
}

// 循环
for (let i = 0; i < 5; i++) {
    console.log(`Loop iteration: ${i}`);
}

// 函数
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("JavaScript"));
