// ES6+ 特性示例

// 1. 块级作用域
if (true) {
    let blockScoped = 'Block scoped variable';
    const constant = 'Constant value';
    console.log(blockScoped);
    console.log(constant);
}

// 2. 箭头函数
const greet = name => `Hello, ${name}!`;
const add = (a, b) => a + b;

// 3. 模板字符串
const name = "JavaScript";
const version = "ES6+";
const message = `${name} ${version} is awesome!`;

// 4. 解构赋值
const person = { name: "Alice", age: 30, address: { city: "New York" } };
const { name: personName, age, address: { city } } = person;

const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

// 5. 扩展运算符
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const combinedArray = [...array1, ...array2];

const object1 = { a: 1, b: 2 };
const object2 = { c: 3, d: 4 };
const combinedObject = { ...object1, ...object2 };

// 6. 类
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    introduce() {
        return `My name is ${this.name}, I'm ${this.age} years old.`;
    }

    static createPerson(name, age) {
        return new Person(name, age);
    }
}

// 7. 模块
// export const PI = 3.14;
// export function calculateArea(radius) {
//     return PI * radius * radius;
// }

// 8. 迭代器和生成器
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

const fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
console.log(fib.next().value); // 1

// 9. Set 和 Map
const set = new Set([1, 2, 3, 4, 5]);
set.add(6);
console.log(set.has(3)); // true

const map = new Map();
map.set('name', 'JavaScript');
map.set('version', 'ES6+');
console.log(map.get('name')); // JavaScript

// 10. 可选链和空值合并
const user = { name: 'Alice', address: { city: 'New York' } };
const zipCode = user?.address?.zipCode ?? 'Unknown';
console.log(zipCode); // Unknown
