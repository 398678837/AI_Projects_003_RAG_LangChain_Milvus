import java.util.*;

// 1. 单例模式
class Singleton {
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

// 2. 工厂方法模式
interface Product {
    void use();
}

class ConcreteProduct implements Product {
    @Override
    public void use() {
        System.out.println("使用具体产品");
    }
}

interface Factory {
    Product createProduct();
}

class ConcreteFactory implements Factory {
    @Override
    public Product createProduct() {
        return new ConcreteProduct();
    }
}

// 3. 适配器模式
interface Target {
    void request();
}

class Adaptee {
    public void specificRequest() {
        System.out.println("适配者的特殊请求");
    }
}

class Adapter implements Target {
    private Adaptee adaptee;
    
    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }
    
    @Override
    public void request() {
        adaptee.specificRequest();
    }
}

// 4. 装饰模式
interface Component {
    void operation();
}

class ConcreteComponent implements Component {
    @Override
    public void operation() {
        System.out.println("具体组件的操作");
    }
}

abstract class Decorator implements Component {
    protected Component component;
    
    public Decorator(Component component) {
        this.component = component;
    }
    
    @Override
    public void operation() {
        component.operation();
    }
}

class ConcreteDecorator extends Decorator {
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

// 5. 观察者模式
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

class ConcreteSubject implements Subject {
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

interface Observer {
    void update();
}

class ConcreteObserver implements Observer {
    private ConcreteSubject subject;
    
    public ConcreteObserver(ConcreteSubject subject) {
        this.subject = subject;
    }
    
    @Override
    public void update() {
        System.out.println("观察者收到通知，状态：" + subject.getState());
    }
}

// 6. 策略模式
interface Strategy {
    void algorithmInterface();
}

class ConcreteStrategyA implements Strategy {
    @Override
    public void algorithmInterface() {
        System.out.println("具体策略A的算法实现");
    }
}

class ConcreteStrategyB implements Strategy {
    @Override
    public void algorithmInterface() {
        System.out.println("具体策略B的算法实现");
    }
}

class Context {
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

// 7. 代理模式
interface SubjectProxy {
    void request();
}

class RealSubject implements SubjectProxy {
    @Override
    public void request() {
        System.out.println("真实主题的请求");
    }
}

class Proxy implements SubjectProxy {
    private RealSubject realSubject;
    
    @Override
    public void request() {
        if (realSubject == null) {
            realSubject = new RealSubject();
        }
        realSubject.request();
    }
}

class DesignPatternsDemo {
    public static void main(String[] args) {
        // 1. 单例模式
        System.out.println("=== 单例模式 ===");
        Singleton singleton = Singleton.getInstance();
        System.out.println("单例对象：" + singleton);
        
        // 2. 工厂方法模式
        System.out.println("\n=== 工厂方法模式 ===");
        Factory factory = new ConcreteFactory();
        Product product = factory.createProduct();
        product.use();
        
        // 3. 适配器模式
        System.out.println("\n=== 适配器模式 ===");
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);
        target.request();
        
        // 4. 装饰模式
        System.out.println("\n=== 装饰模式 ===");
        Component component = new ConcreteComponent();
        Component decoratedComponent = new ConcreteDecorator(component);
        decoratedComponent.operation();
        
        // 5. 观察者模式
        System.out.println("\n=== 观察者模式 ===");
        ConcreteSubject subject = new ConcreteSubject();
        Observer observer = new ConcreteObserver(subject);
        subject.attach(observer);
        subject.setState("新状态");
        
        // 6. 策略模式
        System.out.println("\n=== 策略模式 ===");
        Context context = new Context(new ConcreteStrategyA());
        context.executeStrategy();
        context.setStrategy(new ConcreteStrategyB());
        context.executeStrategy();
        
        // 7. 代理模式
        System.out.println("\n=== 代理模式 ===");
        SubjectProxy proxy = new Proxy();
        proxy.request();
    }
}