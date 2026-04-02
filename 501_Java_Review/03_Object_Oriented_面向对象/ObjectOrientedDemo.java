// 1. 类与对象
class Person {
    private String name;
    private int age;
    
    public Person() {
        this.name = "未知";
        this.age = 0;
    }
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void eat() {
        System.out.println(name + "在吃饭");
    }
    
    public void sleep() {
        System.out.println(name + "在睡觉");
    }
    
    // getter和setter
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
        if (age >= 0 && age <= 120) {
            this.age = age;
        } else {
            System.out.println("年龄不合法");
        }
    }
}

// 2. 继承
class Animal {
    protected String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    public void eat() {
        System.out.println(name + "在吃东西");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
    
    @Override
    public void eat() {
        System.out.println(name + "在吃狗粮");
    }
    
    public void bark() {
        System.out.println(name + "在汪汪叫");
    }
}

// 3. 抽象类
abstract class Shape {
    protected String color;
    
    public Shape(String color) {
        this.color = color;
    }
    
    public abstract double getArea();
    public abstract double getPerimeter();
}

class Circle extends Shape {
    private double radius;
    
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

// 4. 接口
interface Flyable {
    void fly();
    
    default void land() {
        System.out.println("降落");
    }
}

class Bird implements Flyable {
    private String name;
    
    public Bird(String name) {
        this.name = name;
    }
    
    @Override
    public void fly() {
        System.out.println(name + "在飞翔");
    }
}

// 主类
public class ObjectOrientedDemo {
    public static void main(String[] args) {
        // 类与对象
        Person person = new Person("张三", 25);
        person.eat();
        person.sleep();
        
        // 继承
        Dog dog = new Dog("旺财");
        dog.eat();
        dog.bark();
        
        // 抽象类
        Circle circle = new Circle("红色", 5.0);
        System.out.println("圆的面积：" + circle.getArea());
        System.out.println("圆的周长：" + circle.getPerimeter());
        
        // 接口
        Bird bird = new Bird("麻雀");
        bird.fly();
        bird.land();
        
        // 多态
        Animal animal = new Dog("小白");
        animal.eat();
    }
}