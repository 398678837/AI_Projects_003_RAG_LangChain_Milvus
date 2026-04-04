# 结构体

## 1. 结构体基础

### 结构体定义与初始化
```c
#include <stdio.h>

// 结构体定义
typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    // 结构体初始化
    Person p1 = {
        "Alice",
        25,
        1.65
    };
    
    // 结构体初始化（指定成员）
    Person p2;
    strcpy(p2.name, "Bob");
    p2.age = 30;
    p2.height = 1.80;
    
    return 0;
}
```

### 结构体成员访问
```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    Person p = {"Alice", 25, 1.65};
    
    // 访问结构体成员
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Height: %.2f\n", p.height);
    
    // 修改结构体成员
    strcpy(p.name, "Alice Smith");
    p.age = 26;
    p.height = 1.66;
    
    printf("\nUpdated:\n");
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Height: %.2f\n", p.height);
    
    return 0;
}
```

### 结构体数组
```c
#include <stdio.h>

typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    // 结构体数组
    Person people[3] = {
        {"Alice", 25, 1.65},
        {"Bob", 30, 1.80},
        {"Charlie", 35, 1.75}
    };
    
    // 遍历结构体数组
    for (int i = 0; i < 3; i++) {
        printf("Person %d:\n", i+1);
        printf("  Name: %s\n", people[i].name);
        printf("  Age: %d\n", people[i].age);
        printf("  Height: %.2f\n", people[i].height);
    }
    
    return 0;
}
```

## 2. 结构体指针

### 结构体指针基础
```c
#include <stdio.h>

typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    Person p = {"Alice", 25, 1.65};
    Person *ptr = &p;
    
    // 通过指针访问结构体成员
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Height: %.2f\n", ptr->height);
    
    // 通过指针修改结构体成员
    ptr->age = 26;
    printf("\nUpdated age: %d\n", ptr->age);
    
    return 0;
}
```

### 动态结构体
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    // 动态分配结构体
    Person *ptr = (Person *)malloc(sizeof(Person));
    if (ptr == NULL) {
        printf("内存分配失败\n");
        return 1;
    }
    
    // 初始化结构体
    strcpy(ptr->name, "Alice");
    ptr->age = 25;
    ptr->height = 1.65;
    
    // 访问结构体成员
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Height: %.2f\n", ptr->height);
    
    // 释放内存
    free(ptr);
    
    return 0;
}
```

## 3. 结构体嵌套

### 嵌套结构体
```c
#include <stdio.h>

typedef struct {
    int day;
    int month;
    int year;
} Date;

typedef struct {
    char name[50];
    Date birthday;
    float height;
} Person;

int main() {
    // 初始化嵌套结构体
    Person p = {
        "Alice",
        {15, 5, 1995},
        1.65
    };
    
    // 访问嵌套结构体成员
    printf("Name: %s\n", p.name);
    printf("Birthday: %d/%d/%d\n", p.birthday.day, p.birthday.month, p.birthday.year);
    printf("Height: %.2f\n", p.height);
    
    return 0;
}
```

### 结构体指针嵌套
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int day;
    int month;
    int year;
} Date;

typedef struct {
    char name[50];
    Date *birthday;
    float height;
} Person;

int main() {
    // 动态分配日期结构体
    Date *date = (Date *)malloc(sizeof(Date));
    date->day = 15;
    date->month = 5;
    date->year = 1995;
    
    // 初始化Person结构体
    Person p = {
        "Alice",
        date,
        1.65
    };
    
    // 访问嵌套结构体成员
    printf("Name: %s\n", p.name);
    printf("Birthday: %d/%d/%d\n", p.birthday->day, p.birthday->month, p.birthday->year);
    printf("Height: %.2f\n", p.height);
    
    // 释放内存
    free(date);
    
    return 0;
}
```

## 4. 共用体

### 共用体定义与使用
```c
#include <stdio.h>

// 共用体定义
typedef union {
    int i;
    float f;
    char c;
} Data;

int main() {
    Data d;
    
    // 使用整型
    d.i = 100;
    printf("d.i = %d\n", d.i);
    
    // 使用浮点型
    d.f = 3.14;
    printf("d.f = %f\n", d.f);
    printf("d.i = %d (now contains float data)\n", d.i);
    
    // 使用字符型
    d.c = 'A';
    printf("d.c = %c\n", d.c);
    printf("d.i = %d (now contains char data)\n", d.i);
    
    return 0;
}
```

## 5. 结构体与函数

### 结构体作为函数参数
```c
#include <stdio.h>

typedef struct {
    char name[50];
    int age;
    float height;
} Person;

// 结构体作为参数（值传递）
void print_person(Person p) {
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Height: %.2f\n", p.height);
}

// 结构体作为参数（指针传递）
void update_person(Person *p) {
    p->age++;
    p->height += 0.01;
}

int main() {
    Person p = {"Alice", 25, 1.65};
    
    printf("Original:\n");
    print_person(p);
    
    update_person(&p);
    
    printf("\nUpdated:\n");
    print_person(p);
    
    return 0;
}
```

### 结构体作为函数返回值
```c
#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

// 结构体作为返回值
Point create_point(int x, int y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}

Point add_points(Point p1, Point p2) {
    Point p;
    p.x = p1.x + p2.x;
    p.y = p1.y + p2.y;
    return p;
}

int main() {
    Point p1 = create_point(1, 2);
    Point p2 = create_point(3, 4);
    Point p3 = add_points(p1, p2);
    
    printf("p1: (%d, %d)\n", p1.x, p1.y);
    printf("p2: (%d, %d)\n", p2.x, p2.y);
    printf("p3: (%d, %d)\n", p3.x, p3.y);
    
    return 0;
}
```

---

**更新时间：2026-04-04**