# Java面向对象

## 1. 面向对象编程思想

### 1.1 面向对象与面向过程的区别
- **面向过程**：关注步骤，将问题分解为若干步骤，通过函数实现
- **面向对象**：关注对象，将问题分解为若干对象，通过对象之间的交互解决问题

### 1.2 面向对象的三大特性
- **封装**：隐藏对象的属性和实现细节，仅对外提供公共访问方式
- **继承**：子类继承父类的属性和方法，实现代码复用
- **多态**：同一方法在不同对象上有不同的行为表现

## 2. 类与对象

### 2.1 类的定义
```java
public class Person {
    // 属性（成员变量）
    private String name;
    private int age;
    
    // 构造方法
    public Person() {
        // 无参构造
    }
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // 方法
    public void eat() {
        System.out.println(name + "在吃饭");
    }
    
    public void sleep() {
        System.out.println(name + "在睡觉");
    }
    
    // getter和setter方法
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        this.age = age;
    }
}
```

### 2.2 对象的创建与使用
```java
// 创建对象
Person person = new Person("张三", 25);

// 调用方法
person.eat();
person.sleep();

// 访问属性（通过getter和setter）
String name = person.getName();
int age = person.getAge();
```

## 3. 封装

### 3.1 封装的意义
- 提高代码的安全性
- 提高代码的复用性
- 隐藏实现细节，提供公共访问方式

### 3.2 封装的实现
- 使用private修饰属性
- 提供public的getter和setter方法
- 可以在setter方法中添加逻辑控制

```java
public void setAge(int age) {
    if (age >= 0 && age <= 120) {
        this.age = age;
    } else {
        System.out.println("年龄不合法");
    }
}
```

## 4. 继承

### 4.1 继承的定义
```java
// 父类
public class Animal {
    protected String name;
    
    public void eat() {
        System.out.println(name + "在吃东西");
    }
}

// 子类
public class Dog extends Animal {
    public void bark() {
        System.out.println(name + "在汪汪叫");
    }
}
```

### 4.2 继承的特点
- Java中类只能单继承，但可以实现多个接口
- 子类可以继承父类的非private属性和方法
- 子类可以重写父类的方法
- 子类可以调用父类的构造方法（super()）

### 4.3 方法重写
```java
@Override
public void eat() {
    System.out.println(name + "在吃狗粮");
}
```

## 5. 多态

### 5.1 多态的实现方式
- 方法重载（Overload）：同一类中方法名相同，参数列表不同
- 方法重写（Override）：子类重写父类的方法
- 接口实现

### 5.2 多态的使用
```java
Animal animal = new Dog();
animal.eat(); // 调用Dog类的eat方法
```

### 5.3 多态的好处
- 提高代码的扩展性
- 提高代码的可维护性
- 符合开闭原则

## 6. 抽象类与接口

### 6.1 抽象类
```java
public abstract class Shape {
    protected String color;
    
    public abstract double getArea();
    public abstract double getPerimeter();
    
    public void setColor(String color) {
        this.color = color;
    }
}
```

### 6.2 接口
```java
public interface Flyable {
    void fly();
    
    default void land() {
        System.out.println("降落");
    }
}
```

### 6.3 抽象类与接口的区别
| 区别点       | 抽象类               | 接口                 |
|--------------|----------------------|----------------------|
| 关键字       | abstract class       | interface            |
| 继承方式     | extends              | implements           |
| 方法实现     | 可以有具体方法       | 只能有抽象方法（Java 8+可以有默认方法） |
| 构造方法     | 可以有构造方法       | 不能有构造方法       |
| 成员变量     | 可以有实例变量       | 只能有常量           |
| 多继承       | 单继承               | 多实现               |

## 7. 内部类

### 7.1 成员内部类
```java
public class OuterClass {
    private int outerVar;
    
    public class InnerClass {
        public void display() {
            System.out.println(outerVar);
        }
    }
}
```

### 7.2 静态内部类
```java
public class OuterClass {
    private static int outerVar;
    
    public static class StaticInnerClass {
        public void display() {
            System.out.println(outerVar);
        }
    }
}
```

### 7.3 局部内部类
```java
public class OuterClass {
    public void method() {
        class LocalInnerClass {
            public void display() {
                System.out.println("局部内部类");
            }
        }
        
        LocalInnerClass localInner = new LocalInnerClass();
        localInner.display();
    }
}
```

### 7.4 匿名内部类
```java
public interface Greeting {
    void sayHello();
}

public class Test {
    public static void main(String[] args) {
        Greeting greeting = new Greeting() {
            @Override
            public void sayHello() {
                System.out.println("Hello");
            }
        };
        greeting.sayHello();
    }
}
```

## 8. 常用类

### 8.1 Object类
- 所有类的父类
- 常用方法：equals()、hashCode()、toString()、getClass()

### 8.2 String类
- 不可变字符串
- 常用方法：length()、charAt()、substring()、equals()

### 8.3 包装类
- 基本数据类型对应的引用类型
- 常用包装类：Integer、Double、Boolean、Character

### 8.4 日期时间类
- Date、Calendar、LocalDate、LocalTime、LocalDateTime

## 9. 设计原则

### 9.1 单一职责原则
- 一个类应该只有一个引起变化的原因

### 9.2 开闭原则
- 对扩展开放，对修改关闭

### 9.3 里氏替换原则
- 子类可以替换父类出现的任何地方

### 9.4 依赖倒置原则
- 依赖抽象，不依赖具体实现

### 9.5 接口隔离原则
- 客户端不应该依赖它不需要的接口

### 9.6 迪米特法则
- 一个对象应该对其他对象保持最少的了解

### 9.7 合成复用原则
- 优先使用组合/聚合关系，而不是继承关系