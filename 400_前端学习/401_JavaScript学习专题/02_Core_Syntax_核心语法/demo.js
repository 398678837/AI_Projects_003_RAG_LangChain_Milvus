// JavaScript 核心语法示例

// 箭头函数
const add = (a, b) => a + b;
const multiply = (a, b) => a * b;

// 模板字符串
const name = "JavaScript";
const version = "ES6+";
const message = `${name} ${version} is awesome!`;

// 解构赋值
const person = { name: "Alice", age: 30 };
const { name: personName, age: personAge } = person;

const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

// 扩展运算符
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const combinedArray = [...array1, ...array2];

const object1 = { a: 1, b: 2 };
const object2 = { c: 3, d: 4 };
const combinedObject = { ...object1, ...object2 };

// 默认参数
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}

// 剩余参数
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4, 5));
