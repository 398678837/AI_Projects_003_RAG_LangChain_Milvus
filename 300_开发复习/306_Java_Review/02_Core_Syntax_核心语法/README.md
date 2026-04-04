# Java核心语法

## 1. 变量与数据类型

### 1.1 基本数据类型
| 类型       | 大小  | 范围                  | 默认值  |
|------------|-------|-----------------------|---------|
| byte       | 1字节 | -128 ~ 127            | 0       |
| short      | 2字节 | -32768 ~ 32767        | 0       |
| int        | 4字节 | -2^31 ~ 2^31-1        | 0       |
| long       | 8字节 | -2^63 ~ 2^63-1        | 0L      |
| float      | 4字节 | 3.4e-45 ~ 3.4e+38     | 0.0f    |
| double     | 8字节 | 1.7e-308 ~ 1.7e+308   | 0.0d    |
| char       | 2字节 | '\u0000' ~ '\uffff'    | '\u0000'|
| boolean    | 1字节 | true / false          | false   |

### 1.2 引用数据类型
- 类（Class）
- 接口（Interface）
- 数组（Array）

### 1.3 变量声明与初始化
```java
// 声明变量
int age;
String name;

// 声明并初始化
int score = 90;
String city = "北京";

// 常量声明
final double PI = 3.14159;
```

## 2. 运算符

### 2.1 算术运算符
```java
int a = 10, b = 3;
System.out.println(a + b);  // 13
System.out.println(a - b);  // 7
System.out.println(a * b);  // 30
System.out.println(a / b);  // 3（整数除法）
System.out.println(a % b);  // 1（取余）
```

### 2.2 关系运算符
```java
int x = 5, y = 3;
System.out.println(x > y);  // true
System.out.println(x < y);  // false
System.out.println(x == y); // false
System.out.println(x != y); // true
```

### 2.3 逻辑运算符
```java
boolean condition1 = true, condition2 = false;
System.out.println(condition1 && condition2); // false（逻辑与）
System.out.println(condition1 || condition2); // true（逻辑或）
System.out.println(!condition1);              // false（逻辑非）
```

### 2.4 位运算符
```java
int m = 60; // 0011 1100
int n = 13; // 0000 1101
System.out.println(m & n);  // 12（0000 1100）
System.out.println(m | n);  // 61（0011 1101）
System.out.println(m ^ n);  // 49（0011 0001）
System.out.println(~m);     // -61（1100 0011）
```

### 2.5 赋值运算符
```java
int p = 10;
p += 5; // 等价于 p = p + 5
p -= 3; // 等价于 p = p - 3
```

## 3. 控制语句

### 3.1 条件语句
```java
int score = 85;
if (score >= 90) {
    System.out.println("优秀");
} else if (score >= 80) {
    System.out.println("良好");
} else if (score >= 60) {
    System.out.println("及格");
} else {
    System.out.println("不及格");
}
```

### 3.2 循环语句

#### 3.2.1 for循环
```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

#### 3.2.2 while循环
```java
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;
}
```

#### 3.2.3 do-while循环
```java
int num = 0;
do {
    System.out.println(num);
    num++;
} while (num < 5);
```

### 3.3 分支语句
```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("星期一");
        break;
    case 2:
        System.out.println("星期二");
        break;
    case 3:
        System.out.println("星期三");
        break;
    default:
        System.out.println("无效日期");
}
```

## 4. 数组

### 4.1 数组声明与初始化
```java
// 声明数组
int[] numbers;

// 初始化数组
numbers = new int[5];
int[] scores = {90, 85, 95, 80, 75};
```

### 4.2 数组遍历
```java
int[] arr = {1, 2, 3, 4, 5};
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

// 增强for循环
for (int num : arr) {
    System.out.println(num);
}
```

## 5. 字符串

### 5.1 String类
```java
String str1 = "Hello";
String str2 = new String("World");

// 字符串拼接
String str3 = str1 + " " + str2;

// 字符串长度
int length = str1.length();

// 字符串比较
boolean equals = str1.equals(str2);

// 字符串查找
int index = str1.indexOf("e");
```

### 5.2 StringBuffer与StringBuilder
```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String result = sb.toString();
```

## 6. 异常处理

### 6.1 try-catch-finally
```java
try {
    int[] arr = new int[5];
    System.out.println(arr[10]); // 数组越界异常
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("数组索引越界：" + e.getMessage());
} finally {
    System.out.println("无论是否发生异常，都会执行");
}
```

### 6.2 自定义异常
```java
class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

// 抛出异常
throw new MyException("自定义异常");
```