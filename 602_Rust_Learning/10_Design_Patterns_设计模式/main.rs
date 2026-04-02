use std::sync::Once;
use std::rc::Rc;
use std::cell::RefCell;

fn main() {
    // 1. 创建型模式
    println!("=== 创建型模式 ===");
    
    // 单例模式
    let singleton = Singleton::get_instance();
    println!("Singleton value: {}", singleton.value);
    
    // 工厂模式
    let factory = ShapeFactory;
    let circle = factory.create_shape("circle");
    circle.draw();
    
    let rectangle = factory.create_shape("rectangle");
    rectangle.draw();
    
    // 2. 结构型模式
    println!("\n=== 结构型模式 ===");
    
    // 适配器模式
    let adaptee = Adaptee;
    let adapter = Adapter { adaptee };
    println!("Adapter request: {}", adapter.request());
    
    // 装饰器模式
    let component = Box::new(ConcreteComponent);
    let decorator = Box::new(ConcreteDecoratorA { component });
    println!("Decorator operation: {}", decorator.operation());
    
    // 3. 行为型模式
    println!("\n=== 行为型模式 ===");
    
    // 观察者模式
    let mut subject = Subject::new();
    let observer1 = Rc::new(RefCell::new(ConcreteObserver { name: String::from("Observer 1") }));
    let observer2 = Rc::new(RefCell::new(ConcreteObserver { name: String::from("Observer 2") }));
    
    subject.attach(observer1);
    subject.attach(observer2);
    
    subject.notify("Hello, observers!");
}

// 单例模式
struct Singleton {
    value: i32,
}

static mut INSTANCE: Option<Singleton> = None;
static ONCE: Once = Once::new();

impl Singleton {
    fn get_instance() -> &'static Singleton {
        unsafe {
            ONCE.call_once(|| {
                INSTANCE = Some(Singleton { value: 42 });
            });
            
            INSTANCE.as_ref().unwrap()
        }
    }
}

// 工厂模式
trait Shape {
    fn draw(&self);
}

struct Circle;
impl Shape for Circle {
    fn draw(&self) {
        println!("Drawing a circle");
    }
}

struct Rectangle;
impl Shape for Rectangle {
    fn draw(&self) {
        println!("Drawing a rectangle");
    }
}

struct ShapeFactory;
impl ShapeFactory {
    fn create_shape(&self, shape_type: &str) -> Box<dyn Shape> {
        match shape_type {
            "circle" => Box::new(Circle),
            "rectangle" => Box::new(Rectangle),
            _ => panic!("Unknown shape type"),
        }
    }
}

// 适配器模式
trait Target {
    fn request(&self) -> String;
}

struct Adaptee;
impl Adaptee {
    fn specific_request(&self) -> String {
        String::from("Specific request")
    }
}

struct Adapter {
    adaptee: Adaptee,
}

impl Target for Adapter {
    fn request(&self) -> String {
        format!("Adapter: {}", self.adaptee.specific_request())
    }
}

// 装饰器模式
trait Component {
    fn operation(&self) -> String;
}

struct ConcreteComponent;
impl Component for ConcreteComponent {
    fn operation(&self) -> String {
        String::from("ConcreteComponent")
    }
}

struct ConcreteDecoratorA {
    component: Box<dyn Component>,
}

impl Component for ConcreteDecoratorA {
    fn operation(&self) -> String {
        format!("ConcreteDecoratorA({})", self.component.operation())
    }
}

// 观察者模式
trait Observer {
    fn update(&self, message: &str);
}

struct Subject {
    observers: Vec<Rc<RefCell<dyn Observer>>>,
}

impl Subject {
    fn new() -> Subject {
        Subject { observers: Vec::new() }
    }
    
    fn attach(&mut self, observer: Rc<RefCell<dyn Observer>>) {
        self.observers.push(observer);
    }
    
    fn notify(&self, message: &str) {
        for observer in &self.observers {
            observer.borrow().update(message);
        }
    }
}

struct ConcreteObserver {
    name: String,
}

impl Observer for ConcreteObserver {
    fn update(&self, message: &str) {
        println!("{} received message: {}", self.name, message);
    }
}