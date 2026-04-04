#include <iostream>
#include <string>

// 基类 - 动物
class Animal {
protected:
    std::string name;
    int age;

public:
    // 构造函数
    Animal(const std::string& n, int a) : name(n), age(a) {}
    
    // 析构函数
    virtual ~Animal() {}
    
    // 虚函数 - 发出声音
    virtual void makeSound() const {
        std::cout << "动物发出声音" << std::endl;
    }
    
    // 普通成员函数
    void eat() const {
        std::cout << name << " 在吃东西" << std::endl;
    }
    
    // 获取年龄
    int getAge() const {
        return age;
    }
};

// 派生类 - 狗
class Dog : public Animal {
private:
    std::string breed;

public:
    // 构造函数
    Dog(const std::string& n, int a, const std::string& b) : Animal(n, a), breed(b) {}
    
    // 重写虚函数
    void makeSound() const override {
        std::cout << name << " 汪汪叫" << std::endl;
    }
    
    // 特有方法
    void fetch() const {
        std::cout << name << " 在捡球" << std::endl;
    }
};

// 派生类 - 猫
class Cat : public Animal {
private:
    bool isIndoor;

public:
    // 构造函数
    Cat(const std::string& n, int a, bool indoor) : Animal(n, a), isIndoor(indoor) {}
    
    // 重写虚函数
    void makeSound() const override {
        std::cout << name << " 喵喵叫" << std::endl;
    }
    
    // 特有方法
    void climbTree() const {
        std::cout << name << " 在爬树" << std::endl;
    }
};

// 抽象类 - 形状
class Shape {
public:
    // 虚析构函数
    virtual ~Shape() {}
    
    // 纯虚函数 - 计算面积
    virtual double calculateArea() const = 0;
    
    // 虚函数 - 显示信息
    virtual void display() const {
        std::cout << "这是一个形状" << std::endl;
    }
};

// 派生类 - 圆形
class Circle : public Shape {
private:
    double radius;

public:
    // 构造函数
    Circle(double r) : radius(r) {}
    
    // 实现纯虚函数
    double calculateArea() const override {
        return 3.14159 * radius * radius;
    }
    
    // 重写虚函数
    void display() const override {
        std::cout << "圆形，半径: " << radius << std::endl;
    }
};

// 派生类 - 矩形
class Rectangle : public Shape {
private:
    double width;
    double height;

public:
    // 构造函数
    Rectangle(double w, double h) : width(w), height(h) {}
    
    // 实现纯虚函数
    double calculateArea() const override {
        return width * height;
    }
    
    // 重写虚函数
    void display() const override {
        std::cout << "矩形，宽度: " << width << ", 高度: " << height << std::endl;
    }
};

int main() {
    // 测试动物类
    std::cout << "=== 动物类测试 ===" << std::endl;
    
    // 创建狗对象
    Dog dog("旺财", 3, "金毛");
    dog.makeSound();
    dog.eat();
    dog.fetch();
    std::cout << "年龄: " << dog.getAge() << std::endl;
    
    // 创建猫对象
    Cat cat("咪咪", 2, true);
    cat.makeSound();
    cat.eat();
    cat.climbTree();
    std::cout << "年龄: " << cat.getAge() << std::endl;
    
    // 多态测试
    std::cout << "\n=== 多态测试 ===" << std::endl;
    
    Animal* animals[2];
    animals[0] = new Dog("小黑", 1, "拉布拉多");
    animals[1] = new Cat("小白", 1, false);
    
    for (int i = 0; i < 2; i++) {
        animals[i]->makeSound();
        animals[i]->eat();
        delete animals[i];
    }
    
    // 测试形状类
    std::cout << "\n=== 形状类测试 ===" << std::endl;
    
    Shape* shapes[2];
    shapes[0] = new Circle(5.0);
    shapes[1] = new Rectangle(4.0, 6.0);
    
    for (int i = 0; i < 2; i++) {
        shapes[i]->display();
        std::cout << "面积: " << shapes[i]->calculateArea() << std::endl;
        delete shapes[i];
    }
    
    return 0;
}