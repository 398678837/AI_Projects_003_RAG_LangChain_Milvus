// 闭包示例

// 1. 基本闭包
function outerFunction() {
    let outerVariable = 'I am outside!';

    function innerFunction() {
        console.log(outerVariable); // 可以访问外部变量
    }

    return innerFunction;
}

const closure = outerFunction();
closure(); // 输出: I am outside!

// 2. 闭包保存状态
function createCounter() {
    let count = 0;

    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.decrement()); // 1
console.log(counter.getCount()); // 1

// 3. 闭包实现私有变量
function createPerson(name) {
    let age = 0;

    return {
        getName: function() {
            return name;
        },
        getAge: function() {
            return age;
        },
        setAge: function(newAge) {
            if (newAge >= 0) {
                age = newAge;
            }
        }
    };
}

const person = createPerson('Alice');
console.log(person.getName()); // Alice
console.log(person.getAge()); // 0
person.setAge(30);
console.log(person.getAge()); // 30

// 4. 闭包在循环中的应用
function createFunctions() {
    const functions = [];

    for (var i = 0; i < 5; i++) {
        // 使用立即执行函数表达式 (IIFE) 创建闭包
        functions.push((function(index) {
            return function() {
                console.log(index);
            };
        })(i));
    }

    return functions;
}

const funcs = createFunctions();
funcs[0](); // 0
funcs[1](); // 1
funcs[2](); // 2

// 5. 闭包与 setTimeout
function delayedGreeting(name) {
    setTimeout(function() {
        console.log(`Hello, ${name}!`);
    }, 1000);
}

delayedGreeting('Bob'); // 1秒后输出: Hello, Bob!

// 6. 闭包实现模块化
const Calculator = (function() {
    let result = 0;

    function add(a, b) {
        return a + b;
    }

    function subtract(a, b) {
        return a - b;
    }

    function multiply(a, b) {
        return a * b;
    }

    function divide(a, b) {
        if (b !== 0) {
            return a / b;
        } else {
            return 'Error: Division by zero';
        }
    }

    return {
        add: add,
        subtract: subtract,
        multiply: multiply,
        divide: divide
    };
})();

console.log(Calculator.add(5, 3)); // 8
console.log(Calculator.subtract(5, 3)); // 2
console.log(Calculator.multiply(5, 3)); // 15
console.log(Calculator.divide(6, 3)); // 2

// 7. 闭包与 this
const obj = {
    value: 42,
    getValue: function() {
        return function() {
            console.log(this.value); // this 指向全局对象
        };
    },
    getValueArrow: function() {
        return () => {
            console.log(this.value); // this 指向 obj
        };
    }
};

const getValue = obj.getValue();
getValue(); // undefined

const getValueArrow = obj.getValueArrow();
getValueArrow(); // 42
