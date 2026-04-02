# Java设计模式

## 1. 设计模式概述

### 1.1 设计模式的定义
- 一套被反复使用、多数人知晓的、经过分类编目的、代码设计经验的总结
- 描述了在特定场景下解决某一类问题的最佳方案

### 1.2 设计模式的分类
- **创建型模式**：关注对象的创建过程
- **结构型模式**：关注类和对象的组合
- **行为型模式**：关注对象之间的交互

### 1.3 设计模式的原则
- **单一职责原则**：一个类应该只有一个引起变化的原因
- **开闭原则**：对扩展开放，对修改关闭
- **里氏替换原则**：子类可以替换父类出现的任何地方
- **依赖倒置原则**：依赖抽象，不依赖具体实现
- **接口隔离原则**：客户端不应该依赖它不需要的接口
- **迪米特法则**：一个对象应该对其他对象保持最少的了解
- **合成复用原则**：优先使用组合/聚合关系，而不是继承关系

## 2. 创建型模式

### 2.1 单例模式
```java
// 饿汉式单例
public class Singleton {
    private static final Singleton instance = new Singleton();
    
    private Singleton() {}
    
    public static Singleton getInstance() {
        return instance;
    }
}

// 懒汉式单例
public class Singleton {
    private static Singleton instance;
    
    private Singleton() {}
    
    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}

// 双重检查锁定
public class Singleton {
    private static volatile Singleton instance;
    
    private Singleton() {}
    
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

### 2.2 工厂方法模式
```java
// 产品接口
public interface Product {
    void use();
}

// 具体产品
public class ConcreteProduct implements Product {
    @Override
    public void use() {
        System.out.println("使用具体产品");
    }
}

// 工厂接口
public interface Factory {
    Product createProduct();
}

// 具体工厂
public class ConcreteFactory implements Factory {
    @Override
    public Product createProduct() {
        return new ConcreteProduct();
    }
}
```

### 2.3 抽象工厂模式
```java
// 产品A接口
public interface ProductA {
    void use();
}

// 产品B接口
public interface ProductB {
    void use();
}

// 具体产品A1
public class ConcreteProductA1 implements ProductA {
    @Override
    public void use() {
        System.out.println("使用产品A1");
    }
}

// 具体产品B1
public class ConcreteProductB1 implements ProductB {
    @Override
    public void use() {
        System.out.println("使用产品B1");
    }
}

// 抽象工厂
public interface AbstractFactory {
    ProductA createProductA();
    ProductB createProductB();
}

// 具体工厂1
public class ConcreteFactory1 implements AbstractFactory {
    @Override
    public ProductA createProductA() {
        return new ConcreteProductA1();
    }
    
    @Override
    public ProductB createProductB() {
        return new ConcreteProductB1();
    }
}
```

### 2.4 建造者模式
```java
// 产品
public class Product {
    private String partA;
    private String partB;
    private String partC;
    
    public void setPartA(String partA) {
        this.partA = partA;
    }
    
    public void setPartB(String partB) {
        this.partB = partB;
    }
    
    public void setPartC(String partC) {
        this.partC = partC;
    }
    
    public void show() {
        System.out.println("产品部件：" + partA + ", " + partB + ", " + partC);
    }
}

// 建造者
public abstract class Builder {
    protected Product product = new Product();
    
    public abstract void buildPartA();
    public abstract void buildPartB();
    public abstract void buildPartC();
    
    public Product getResult() {
        return product;
    }
}

// 具体建造者
public class ConcreteBuilder extends Builder {
    @Override
    public void buildPartA() {
        product.setPartA("部件A");
    }
    
    @Override
    public void buildPartB() {
        product.setPartB("部件B");
    }
    
    @Override
    public void buildPartC() {
        product.setPartC("部件C");
    }
}

// 指挥者
public class Director {
    public Product construct(Builder builder) {
        builder.buildPartA();
        builder.buildPartB();
        builder.buildPartC();
        return builder.getResult();
    }
}
```

### 2.5 原型模式
```java
// 原型接口
public interface Prototype {
    Prototype clone();
}

// 具体原型
public class ConcretePrototype implements Prototype {
    private String field;
    
    public ConcretePrototype(String field) {
        this.field = field;
    }
    
    @Override
    public Prototype clone() {
        return new ConcretePrototype(field);
    }
    
    public String getField() {
        return field;
    }
}
```

## 3. 结构型模式

### 3.1 适配器模式
```java
// 目标接口
public interface Target {
    void request();
}

// 适配者
public class Adaptee {
    public void specificRequest() {
        System.out.println("适配者的特殊请求");
    }
}

// 适配器
public class Adapter implements Target {
    private Adaptee adaptee;
    
    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }
    
    @Override
    public void request() {
        adaptee.specificRequest();
    }
}
```

### 3.2 桥接模式
```java
// 实现接口
public interface Implementor {
    void operationImpl();
}

// 具体实现A
public class ConcreteImplementorA implements Implementor {
    @Override
    public void operationImpl() {
        System.out.println("具体实现A的操作");
    }
}

// 抽象类
public abstract class Abstraction {
    protected Implementor implementor;
    
    public Abstraction(Implementor implementor) {
        this.implementor = implementor;
    }
    
    public abstract void operation();
}

// 扩展抽象类
public class RefinedAbstraction extends Abstraction {
    public RefinedAbstraction(Implementor implementor) {
        super(implementor);
    }
    
    @Override
    public void operation() {
        implementor.operationImpl();
    }
}
```

### 3.3 组合模式
```java
// 抽象组件
public abstract class Component {
    protected String name;
    
    public Component(String name) {
        this.name = name;
    }
    
    public abstract void add(Component component);
    public abstract void remove(Component component);
    public abstract void display(int depth);
}

// 叶子组件
public class Leaf extends Component {
    public Leaf(String name) {
        super(name);
    }
    
    @Override
    public void add(Component component) {
        System.out.println("叶子节点不能添加子节点");
    }
    
    @Override
    public void remove(Component component) {
        System.out.println("叶子节点不能删除子节点");
    }
    
    @Override
    public void display(int depth) {
        System.out.println("-" + depth + " " + name);
    }
}

// 组合组件
public class Composite extends Component {
    private List<Component> children = new ArrayList<>();
    
    public Composite(String name) {
        super(name);
    }
    
    @Override
    public void add(Component component) {
        children.add(component);
    }
    
    @Override
    public void remove(Component component) {
        children.remove(component);
    }
    
    @Override
    public void display(int depth) {
        System.out.println("-" + depth + " " + name);
        for (Component component : children) {
            component.display(depth + 1);
        }
    }
}
```

### 3.4 装饰模式
```java
// 抽象组件
public interface Component {
    void operation();
}

// 具体组件
public class ConcreteComponent implements Component {
    @Override
    public void operation() {
        System.out.println("具体组件的操作");
    }
}

// 抽象装饰类
public abstract class Decorator implements Component {
    protected Component component;
    
    public Decorator(Component component) {
        this.component = component;
    }
    
    @Override
    public void operation() {
        component.operation();
    }
}

// 具体装饰类
public class ConcreteDecorator extends Decorator {
    public ConcreteDecorator(Component component) {
        super(component);
    }
    
    @Override
    public void operation() {
        super.operation();
        addedFunction();
    }
    
    public void addedFunction() {
        System.out.println("添加的额外功能");
    }
}
```

### 3.5 外观模式
```java
// 子系统类A
public class SubSystemA {
    public void operationA() {
        System.out.println("子系统A的操作");
    }
}

// 子系统类B
public class SubSystemB {
    public void operationB() {
        System.out.println("子系统B的操作");
    }
}

// 外观类
public class Facade {
    private SubSystemA subSystemA;
    private SubSystemB subSystemB;
    
    public Facade() {
        subSystemA = new SubSystemA();
        subSystemB = new SubSystemB();
    }
    
    public void operation() {
        subSystemA.operationA();
        subSystemB.operationB();
    }
}
```

### 3.6 享元模式
```java
// 享元接口
public interface Flyweight {
    void operation(String extrinsicState);
}

// 具体享元
public class ConcreteFlyweight implements Flyweight {
    private String intrinsicState;
    
    public ConcreteFlyweight(String intrinsicState) {
        this.intrinsicState = intrinsicState;
    }
    
    @Override
    public void operation(String extrinsicState) {
        System.out.println("内部状态：" + intrinsicState + "，外部状态：" + extrinsicState);
    }
}

// 享元工厂
public class FlyweightFactory {
    private Map<String, Flyweight> flyweights = new HashMap<>();
    
    public Flyweight getFlyweight(String key) {
        if (flyweights.containsKey(key)) {
            return flyweights.get(key);
        } else {
            Flyweight flyweight = new ConcreteFlyweight(key);
            flyweights.put(key, flyweight);
            return flyweight;
        }
    }
}
```

### 3.7 代理模式
```java
// 主题接口
public interface Subject {
    void request();
}

// 真实主题
public class RealSubject implements Subject {
    @Override
    public void request() {
        System.out.println("真实主题的请求");
    }
}

// 代理
public class Proxy implements Subject {
    private RealSubject realSubject;
    
    @Override
    public void request() {
        if (realSubject == null) {
            realSubject = new RealSubject();
        }
        realSubject.request();
    }
}
```

## 4. 行为型模式

### 4.1 模板方法模式
```java
// 抽象类
public abstract class AbstractClass {
    public void templateMethod() {
        primitiveOperation1();
        primitiveOperation2();
        primitiveOperation3();
    }
    
    public abstract void primitiveOperation1();
    public abstract void primitiveOperation2();
    
    public void primitiveOperation3() {
        System.out.println("默认实现的操作3");
    }
}

// 具体类
public class ConcreteClass extends AbstractClass {
    @Override
    public void primitiveOperation1() {
        System.out.println("具体实现的操作1");
    }
    
    @Override
    public void primitiveOperation2() {
        System.out.println("具体实现的操作2");
    }
}
```

### 4.2 策略模式
```java
// 策略接口
public interface Strategy {
    void algorithmInterface();
}

// 具体策略A
public class ConcreteStrategyA implements Strategy {
    @Override
    public void algorithmInterface() {
        System.out.println("具体策略A的算法实现");
    }
}

// 具体策略B
public class ConcreteStrategyB implements Strategy {
    @Override
    public void algorithmInterface() {
        System.out.println("具体策略B的算法实现");
    }
}

// 环境类
public class Context {
    private Strategy strategy;
    
    public Context(Strategy strategy) {
        this.strategy = strategy;
    }
    
    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }
    
    public void executeStrategy() {
        strategy.algorithmInterface();
    }
}
```

### 4.3 命令模式
```java
// 命令接口
public interface Command {
    void execute();
}

// 具体命令
public class ConcreteCommand implements Command {
    private Receiver receiver;
    
    public ConcreteCommand(Receiver receiver) {
        this.receiver = receiver;
    }
    
    @Override
    public void execute() {
        receiver.action();
    }
}

// 接收者
public class Receiver {
    public void action() {
        System.out.println("接收者的动作");
    }
}

// 调用者
public class Invoker {
    private Command command;
    
    public void setCommand(Command command) {
        this.command = command;
    }
    
    public void executeCommand() {
        command.execute();
    }
}
```

### 4.4 职责链模式
```java
// 抽象处理者
public abstract class Handler {
    protected Handler successor;
    
    public void setSuccessor(Handler successor) {
        this.successor = successor;
    }
    
    public abstract void handleRequest(int request);
}

// 具体处理者1
public class ConcreteHandler1 extends Handler {
    @Override
    public void handleRequest(int request) {
        if (request < 10) {
            System.out.println("处理者1处理请求：" + request);
        } else if (successor != null) {
            successor.handleRequest(request);
        }
    }
}

// 具体处理者2
public class ConcreteHandler2 extends Handler {
    @Override
    public void handleRequest(int request) {
        if (request >= 10 && request < 20) {
            System.out.println("处理者2处理请求：" + request);
        } else if (successor != null) {
            successor.handleRequest(request);
        }
    }
}
```

### 4.5 状态模式
```java
// 状态接口
public interface State {
    void handle(Context context);
}

// 具体状态A
public class ConcreteStateA implements State {
    @Override
    public void handle(Context context) {
        System.out.println("当前状态是A");
        context.setState(new ConcreteStateB());
    }
}

// 具体状态B
public class ConcreteStateB implements State {
    @Override
    public void handle(Context context) {
        System.out.println("当前状态是B");
        context.setState(new ConcreteStateA());
    }
}

// 环境类
public class Context {
    private State state;
    
    public Context() {
        state = new ConcreteStateA();
    }
    
    public void setState(State state) {
        this.state = state;
    }
    
    public void request() {
        state.handle(this);
    }
}
```

### 4.6 观察者模式
```java
// 主题接口
public interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

// 具体主题
public class ConcreteSubject implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String state;
    
    public void setState(String state) {
        this.state = state;
        notifyObservers();
    }
    
    public String getState() {
        return state;
    }
    
    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }
    
    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update();
        }
    }
}

// 观察者接口
public interface Observer {
    void update();
}

// 具体观察者
public class ConcreteObserver implements Observer {
    private ConcreteSubject subject;
    
    public ConcreteObserver(ConcreteSubject subject) {
        this.subject = subject;
    }
    
    @Override
    public void update() {
        System.out.println("观察者收到通知，状态：" + subject.getState());
    }
}
```

### 4.7 中介者模式
```java
// 中介者接口
public interface Mediator {
    void send(String message, Colleague colleague);
}

// 具体中介者
public class ConcreteMediator implements Mediator {
    private Colleague colleague1;
    private Colleague colleague2;
    
    public void setColleague1(Colleague colleague1) {
        this.colleague1 = colleague1;
    }
    
    public void setColleague2(Colleague colleague2) {
        this.colleague2 = colleague2;
    }
    
    @Override
    public void send(String message, Colleague colleague) {
        if (colleague == colleague1) {
            colleague2.receive(message);
        } else {
            colleague1.receive(message);
        }
    }
}

// 同事类
public abstract class Colleague {
    protected Mediator mediator;
    
    public Colleague(Mediator mediator) {
        this.mediator = mediator;
    }
    
    public abstract void send(String message);
    public abstract void receive(String message);
}

// 具体同事类1
public class ConcreteColleague1 extends Colleague {
    public ConcreteColleague1(Mediator mediator) {
        super(mediator);
    }
    
    @Override
    public void send(String message) {
        mediator.send(message, this);
    }
    
    @Override
    public void receive(String message) {
        System.out.println("同事1收到消息：" + message);
    }
}

// 具体同事类2
public class ConcreteColleague2 extends Colleague {
    public ConcreteColleague2(Mediator mediator) {
        super(mediator);
    }
    
    @Override
    public void send(String message) {
        mediator.send(message, this);
    }
    
    @Override
    public void receive(String message) {
        System.out.println("同事2收到消息：" + message);
    }
}
```

### 4.8 迭代器模式
```java
// 迭代器接口
public interface Iterator {
    boolean hasNext();
    Object next();
}

// 聚合接口
public interface Aggregate {
    Iterator createIterator();
}

// 具体聚合类
public class ConcreteAggregate implements Aggregate {
    private Object[] items;
    
    public ConcreteAggregate(Object[] items) {
        this.items = items;
    }
    
    @Override
    public Iterator createIterator() {
        return new ConcreteIterator(this);
    }
    
    public int getCount() {
        return items.length;
    }
    
    public Object getItem(int index) {
        return items[index];
    }
}

// 具体迭代器
public class ConcreteIterator implements Iterator {
    private ConcreteAggregate aggregate;
    private int index = 0;
    
    public ConcreteIterator(ConcreteAggregate aggregate) {
        this.aggregate = aggregate;
    }
    
    @Override
    public boolean hasNext() {
        return index < aggregate.getCount();
    }
    
    @Override
    public Object next() {
        if (hasNext()) {
            return aggregate.getItem(index++);
        }
        return null;
    }
}
```

### 4.9 访问者模式
```java
// 元素接口
public interface Element {
    void accept(Visitor visitor);
}

// 具体元素A
public class ConcreteElementA implements Element {
    @Override
    public void accept(Visitor visitor) {
        visitor.visitConcreteElementA(this);
    }
    
    public void operationA() {
        System.out.println("具体元素A的操作");
    }
}

// 具体元素B
public class ConcreteElementB implements Element {
    @Override
    public void accept(Visitor visitor) {
        visitor.visitConcreteElementB(this);
    }
    
    public void operationB() {
        System.out.println("具体元素B的操作");
    }
}

// 访问者接口
public interface Visitor {
    void visitConcreteElementA(ConcreteElementA element);
    void visitConcreteElementB(ConcreteElementB element);
}

// 具体访问者
public class ConcreteVisitor implements Visitor {
    @Override
    public void visitConcreteElementA(ConcreteElementA element) {
        element.operationA();
    }
    
    @Override
    public void visitConcreteElementB(ConcreteElementB element) {
        element.operationB();
    }
}
```

### 4.10 备忘录模式
```java
// 原发器
public class Originator {
    private String state;
    
    public void setState(String state) {
        this.state = state;
    }
    
    public String getState() {
        return state;
    }
    
    public Memento createMemento() {
        return new Memento(state);
    }
    
    public void restoreMemento(Memento memento) {
        state = memento.getState();
    }
}

// 备忘录
public class Memento {
    private String state;
    
    public Memento(String state) {
        this.state = state;
    }
    
    public String getState() {
        return state;
    }
}

// 管理者
public class Caretaker {
    private Memento memento;
    
    public void setMemento(Memento memento) {
        this.memento = memento;
    }
    
    public Memento getMemento() {
        return memento;
    }
}
```

### 4.11 解释器模式
```java
// 抽象表达式
public abstract class Expression {
    public abstract int interpret(Context context);
}

// 终结符表达式
public class TerminalExpression extends Expression {
    private String data;
    
    public TerminalExpression(String data) {
        this.data = data;
    }
    
    @Override
    public int interpret(Context context) {
        return context.getValue(data);
    }
}

// 非终结符表达式
public class NonTerminalExpression extends Expression {
    private Expression left;
    private Expression right;
    
    public NonTerminalExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }
    
    @Override
    public int interpret(Context context) {
        return left.interpret(context) + right.interpret(context);
    }
}

// 环境类
public class Context {
    private Map<String, Integer> variables = new HashMap<>();
    
    public void setVariable(String name, int value) {
        variables.put(name, value);
    }
    
    public int getValue(String name) {
        return variables.get(name);
    }
}
```

## 5. 设计模式的选择

### 5.1 设计模式的适用场景
- **创建型模式**：当需要控制对象的创建过程时
- **结构型模式**：当需要处理类或对象的组合时
- **行为型模式**：当需要处理对象之间的交互时

### 5.2 设计模式的权衡
- 灵活性与复杂性的权衡
- 可维护性与性能的权衡
- 可扩展性与可读性的权衡

### 5.3 设计模式的反模式
- 过度设计：使用不必要的设计模式
- 模式滥用：在不适合的场景使用设计模式
- 模式僵化：设计模式导致代码难以修改

## 6. 设计模式的最佳实践

### 6.1 遵循设计原则
- 单一职责原则
- 开闭原则
- 里氏替换原则
- 依赖倒置原则
- 接口隔离原则
- 迪米特法则
- 合成复用原则

### 6.2 合理使用设计模式
- 根据问题选择合适的设计模式
- 避免过度设计
- 保持代码简洁

### 6.3 文档化设计模式
- 在代码中注释使用的设计模式
- 说明使用设计模式的原因
- 提供设计模式的使用示例

### 6.4 不断学习和实践
- 学习新的设计模式
- 实践设计模式的应用
- 总结设计模式的经验