// 面向对象编程示例

// 1. 构造函数
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.introduce = function() {
    return `My name is ${this.name}, I'm ${this.age} years old.`;
};

// 2. ES6 类
class PersonClass {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    introduce() {
        return `My name is ${this.name}, I'm ${this.age} years old.`;
    }

    static createPerson(name, age) {
        return new PersonClass(name, age);
    }
}

// 3. 继承
class Student extends PersonClass {
    constructor(name, age, major) {
        super(name, age);
        this.major = major;
    }

    introduce() {
        return `${super.introduce()} I'm majoring in ${this.major}.`;
    }
}

// 4. 封装
class BankAccount {
    constructor(balance) {
        this._balance = balance; // 私有属性
    }

    get balance() {
        return this._balance;
    }

    set balance(newBalance) {
        if (newBalance >= 0) {
            this._balance = newBalance;
        }
    }

    deposit(amount) {
        if (amount > 0) {
            this._balance += amount;
        }
    }

    withdraw(amount) {
        if (amount > 0 && amount <= this._balance) {
            this._balance -= amount;
        }
    }
}

// 5. 多态
class Animal {
    makeSound() {
        return 'Some generic sound';
    }
}

class Dog extends Animal {
    makeSound() {
        return 'Woof! Woof!';
    }
}

class Cat extends Animal {
    makeSound() {
        return 'Meow! Meow!';
    }
}

// 6. 抽象类
class AbstractShape {
    constructor() {
        if (new.target === AbstractShape) {
            throw new Error('Cannot instantiate abstract class');
        }
    }

    calculateArea() {
        throw new Error('Abstract method must be implemented');
    }
}

class Circle extends AbstractShape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    calculateArea() {
        return Math.PI * this.radius * this.radius;
    }
}

// 7. 接口
const ShapeInterface = {
    calculateArea: function() {}
};

class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    calculateArea() {
        return this.width * this.height;
    }
}

// 8. 混入
const CanFly = {
    fly() {
        return 'Flying...';
    }
};

const CanSwim = {
    swim() {
        return 'Swimming...';
    }
};

class Bird {
    constructor(name) {
        this.name = name;
    }
}

Object.assign(Bird.prototype, CanFly);

class Duck extends Bird {
    constructor(name) {
        super(name);
    }
}

Object.assign(Duck.prototype, CanSwim);
