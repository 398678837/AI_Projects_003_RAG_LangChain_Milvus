import Foundation

print("=== Swift基础概念示例 ===")

print("\n--- 1. 变量和常量 ---")
var variable = 10
let constant = 20
variable = 15
print("变量: \(variable), 常量: \(constant)")

print("\n--- 2. 数据类型 ---")
let integer: Int = 42
let double: Double = 3.14
let string: String = "Hello, Swift!"
let boolean: Bool = true
let array: [String] = ["苹果", "香蕉", "橙子"]
let dictionary: [String: Int] = ["张三": 25, "李四": 30]
print("整数: \(integer), 浮点数: \(double), 字符串: \(string), 布尔值: \(boolean)")
print("数组: \(array), 字典: \(dictionary)")

print("\n--- 3. 控制流 ---")
let score = 85
if score >= 90 {
    print("优秀")
} else if score >= 80 {
    print("良好")
} else {
    print("继续努力")
}

for i in 1...5 {
    print("循环: \(i)")
}

let direction = "north"
switch direction {
case "north":
    print("向北")
case "south":
    print("向南")
case "east", "west":
    print("向东或向西")
default:
    print("未知方向")
}

print("\n--- 4. 函数 ---")
func greet(name: String, greeting: String = "你好") -> String {
    return "\(greeting), \(name)!"
}
print(greet(name: "小明"))
print(greet(name: "小红", greeting: "早上好"))

func sum(numbers: Int...) -> Int {
    return numbers.reduce(0, +)
}
print("求和: \(sum(numbers: 1, 2, 3, 4, 5))")

print("\n--- 5. 闭包 ---")
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map { $0 * 2 }
print("原数组: \(numbers), 加倍后: \(doubled)")

let sorted = numbers.sorted { $0 > $1 }
print("降序排列: \(sorted)")

print("\n--- 6. 可选类型 ---")
var optionalString: String? = "Hello"
print("可选字符串: \(optionalString ?? "nil")")

optionalString = nil
if let unwrapped = optionalString {
    print("解包后: \(unwrapped)")
} else {
    print("值为nil")
}

func process(number: Int?) {
    guard let num = number, num > 0 else {
        print("无效的数字")
        return
    }
    print("处理数字: \(num)")
}
process(number: 10)
process(number: nil)

print("\n--- 7. 结构体和类 ---")
struct Point {
    var x: Int
    var y: Int
    
    mutating func moveBy(x: Int, y: Int) {
        self.x += x
        self.y += y
    }
}

var point = Point(x: 10, y: 20)
print("初始点: (\(point.x), \(point.y))")
point.moveBy(x: 5, y: 5)
print("移动后: (\(point.x), \(point.y))")

class Person {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
    
    func introduce() {
        print("你好，我是\(name)，今年\(age)岁")
    }
}

let person = Person(name: "张三", age: 25)
person.introduce()

print("\n--- 8. 枚举 ---")
enum Direction {
    case north, south, east, west
    
    var description: String {
        switch self {
        case .north: return "北"
        case .south: return "南"
        case .east: return "东"
        case .west: return "西"
        }
    }
}

let dir = Direction.east
print("方向: \(dir.description)")

enum Result<T> {
    case success(T)
    case failure(Error)
}

enum NetworkError: Error {
    case invalidURL
    case timeout
    case noConnection
}

func fetchData() -> Result<String> {
    return .success("数据加载成功")
}

let result = fetchData()
switch result {
case .success(let data):
    print("结果: \(data)")
case .failure(let error):
    print("错误: \(error)")
}

print("\n--- 9. 协议 ---")
protocol Shape {
    var area: Double { get }
    func draw()
}

struct Circle: Shape {
    let radius: Double
    
    var area: Double {
        return Double.pi * radius * radius
    }
    
    func draw() {
        print("画一个半径为\(radius)的圆")
    }
}

struct Rectangle: Shape {
    let width: Double
    let height: Double
    
    var area: Double {
        return width * height
    }
    
    func draw() {
        print("画一个\(width)x\(height)的矩形")
    }
}

let shapes: [Shape] = [Circle(radius: 5), Rectangle(width: 10, height: 20)]
for shape in shapes {
    shape.draw()
    print("面积: \(shape.area)")
}

print("\n--- 10. 扩展 ---")
extension Int {
    var squared: Int {
        return self * self
    }
    
    func times(_ closure: () -> Void) {
        for _ in 0..<self {
            closure()
        }
    }
}

let num = 5
print("\(num)的平方: \(num.squared)")
print("重复3次:")
3.times {
    print("Hello!")
}

print("\n=== 示例结束 ===")
