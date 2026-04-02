use std::fmt;

fn main() {
    // 1. Trait定义与实现
    println!("=== Trait定义与实现 ===");
    
    let article = NewsArticle {
        headline: String::from("Penguins win the Stanley Cup Championship!"),
        location: String::from("Pittsburgh, PA, USA"),
        author: String::from("Iceburgh"),
        content: String::from("The Pittsburgh Penguins once again are the best hockey team in the NHL."),
    };
    
    println!("New article available! {}", article.summarize());
    
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    };
    
    println!("1 new tweet: {}", tweet.summarize());
    
    // 2. 默认实现
    println!("\n=== 默认实现 ===");
    
    let article2 = NewsArticle2 {
        headline: String::from("Penguins win the Stanley Cup Championship!"),
        location: String::from("Pittsburgh, PA, USA"),
        author: String::from("Iceburgh"),
        content: String::from("The Pittsburgh Penguins once again are the best hockey team in the NHL."),
    };
    
    println!("New article available! {}", article2.summarize());
    
    // 3. Trait作为参数
    println!("\n=== Trait作为参数 ===");
    
    notify(&article);
    notify(&tweet);
    
    // 4. Trait对象
    println!("\n=== Trait对象 ===");
    
    let items: Vec<&dyn Summary> = vec![&article, &tweet];
    
    for item in items {
        println!("{} ", item.summarize());
    }
    
    // 5. 泛型与Trait
    println!("\n=== 泛型与Trait ===");
    
    let number_list = vec![34, 50, 25, 100, 65];
    let result = largest(&number_list);
    
    println!("The largest number is {}", result);
    
    let char_list = vec!['y', 'm', 'a', 'q'];
    let result2 = largest(&char_list);
    
    println!("The largest char is {}", result2);
}

trait Summary {
    fn summarize(&self) -> String;
}

struct NewsArticle {
    headline: String,
    location: String,
    author: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

struct Tweet {
    username: String,
    content: String,
    reply: bool,
    retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

trait Summary2 {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}

struct NewsArticle2 {
    headline: String,
    location: String,
    author: String,
    content: String,
}

impl Summary2 for NewsArticle2 {}

fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];
    
    for &item in list {
        if item > largest {
            largest = item;
        }
    }
    
    largest
}