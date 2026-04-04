# 设计模式

## 1. 创建型模式

### 单例模式
```rust
use std::sync::Once;

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
```

### 工厂模式
```rust
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
```

## 2. 结构型模式

### 适配器模式
```rust
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
```

### 装饰器模式
```rust
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
```

## 3. 行为型模式

### 观察者模式
```rust
use std::rc::Rc;
use std::cell::RefCell;

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
```

---

**更新时间：2026-04-01**