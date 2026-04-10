// TypeScript 接口示例

// 1. 基本接口
interface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// 2. 可选属性
interface Product {
  id: number;
  name: string;
  price: number;
  description?: string;
  category?: string;
}

const product: Product = {
  id: 1,
  name: "Laptop",
  price: 999.99,
};

// 3. 只读属性
interface ReadonlyUser {
  readonly id: number;
  name: string;
  email: string;
}

const readonlyUser: ReadonlyUser = {
  id: 1,
  name: "John",
  email: "john@example.com",
};

// readonlyUser.id = 2; // 错误，id 是只读的

// 4. 索引签名
interface StringMap {
  [key: string]: string;
}

const map: StringMap = {
  a: "Hello",
  b: "World",
  c: "TypeScript",
};

interface NumberArray {
  [index: number]: number;
}

const numbers: NumberArray = [1, 2, 3, 4, 5];

// 5. 函数类型
interface GreetFunction {
  (name: string, age: number): string;
}

const greet: GreetFunction = (name, age) => {
  return `Hello, ${name}! You are ${age} years old.`;
};

// 6. 可索引类型
interface StringArray {
  [index: number]: string;
}

const strings: StringArray = ["Hello", "World", "TypeScript"];

// 7. 类类型
interface ClockInterface {
  currentTime: Date;
  setTime(d: Date): void;
}

class Clock implements ClockInterface {
  currentTime: Date = new Date();
  
  setTime(d: Date) {
    this.currentTime = d;
  }
}

// 8. 接口继承
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

const circle1: Circle = {
  name: "Circle",
  radius: 5,
  area() {
    return Math.PI * this.radius * this.radius;
  },
};

const rectangle1: Rectangle = {
  name: "Rectangle",
  width: 10,
  height: 5,
  area() {
    return this.width * this.height;
  },
};

// 9. 多重继承
interface A {
  a: string;
}

interface B {
  b: number;
}

interface C extends A, B {
  c: boolean;
}

const c: C = {
  a: "Hello",
  b: 42,
  c: true,
};

// 10. 接口合并
interface Box {
  height: number;
  width: number;
}

interface Box {
  depth: number;
}

const box: Box = {
  height: 10,
  width: 20,
  depth: 15,
};

// 11. 接口与类型别名的区别
interface UserInterface {
  id: number;
  name: string;
}

type UserType = {
  id: number;
  name: string;
};

// 接口可以被合并，类型别名不行
interface UserInterface {
  email: string;
}

// type UserType = { // 错误，类型别名不能重复声明
//   email: string;
// };

// 12. 接口作为函数参数
function printUser(user: User) {
  console.log(`User: ${user.name}, Email: ${user.email}`);
}

printUser(user);

// 13. 接口作为函数返回值
function createUser(id: number, name: string, email: string): User {
  return { id, name, email };
}

const newUser = createUser(2, "Jane", "jane@example.com");

// 14. 接口与泛型
interface GenericInterface<T> {
  value: T;
  getValue(): T;
}

const genericString: GenericInterface<string> = {
  value: "Hello",
  getValue() {
    return this.value;
  },
};

const genericNumber: GenericInterface<number> = {
  value: 42,
  getValue() {
    return this.value;
  },
};

// 15. 接口与联合类型
interface Cat {
  name: string;
  purr(): void;
}

interface Dog {
  name: string;
  bark(): void;
}

function makeSound(animal: Cat | Dog) {
  if ("purr" in animal) {
    animal.purr();
  } else {
    animal.bark();
  }
}

// 16. 接口与交叉类型
interface Person {
  name: string;
  age: number;
}

interface Employee {
  employeeId: number;
  department: string;
}

const employee1: Person & Employee = {
  name: "John",
  age: 30,
  employeeId: 12345,
  department: "Engineering",
};

// 17. 接口与类型保护
function isCat(animal: Cat | Dog): animal is Cat {
  return "purr" in animal;
}

function processAnimal(animal: Cat | Dog) {
  if (isCat(animal)) {
    animal.purr();
  } else {
    animal.bark();
  }
}

// 18. 接口与可选链
interface Address {
  street?: string;
  city?: string;
  country?: string;
}

interface PersonWithAddress {
  name: string;
  address?: Address;
}

const person1: PersonWithAddress = {
  name: "John",
};

const city1 = person1.address?.city;

// 19. 接口与空值合并
const country1 = person1.address?.country ?? "Unknown";

// 20. 接口与断言
const anyValue1: any = { id: 1, name: "John", email: "john@example.com" };
const userFromAny = anyValue1 as User;
