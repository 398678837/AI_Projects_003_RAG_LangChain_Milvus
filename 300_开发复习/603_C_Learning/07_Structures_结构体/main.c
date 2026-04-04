#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 结构体定义
typedef struct {
    char name[50];
    int age;
    float height;
} Person;

// 日期结构体
typedef struct {
    int day;
    int month;
    int year;
} Date;

// 嵌套结构体
typedef struct {
    char name[50];
    Date birthday;
    float height;
} PersonWithBirthday;

// 结构体指针嵌套
typedef struct {
    char name[50];
    Date *birthday;
    float height;
} PersonWithBirthdayPtr;

// 共用体定义
typedef union {
    int i;
    float f;
    char c;
} Data;

// 点结构体
typedef struct {
    int x;
    int y;
} Point;

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
    // 1. 结构体基础
    printf("=== 结构体基础 ===\n");
    
    // 结构体定义与初始化
    printf("\n=== 结构体定义与初始化 ===\n");
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
    
    // 结构体成员访问
    printf("\n=== 结构体成员访问 ===\n");
    Person p3 = {"Alice", 25, 1.65};
    
    // 访问结构体成员
    printf("Name: %s\n", p3.name);
    printf("Age: %d\n", p3.age);
    printf("Height: %.2f\n", p3.height);
    
    // 修改结构体成员
    strcpy(p3.name, "Alice Smith");
    p3.age = 26;
    p3.height = 1.66;
    
    printf("\nUpdated:\n");
    printf("Name: %s\n", p3.name);
    printf("Age: %d\n", p3.age);
    printf("Height: %.2f\n", p3.height);
    
    // 结构体数组
    printf("\n=== 结构体数组 ===\n");
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
    
    // 2. 结构体指针
    printf("\n=== 结构体指针 ===\n");
    
    // 结构体指针基础
    printf("\n=== 结构体指针基础 ===\n");
    Person p4 = {"Alice", 25, 1.65};
    Person *ptr = &p4;
    
    // 通过指针访问结构体成员
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Height: %.2f\n", ptr->height);
    
    // 通过指针修改结构体成员
    ptr->age = 26;
    printf("\nUpdated age: %d\n", ptr->age);
    
    // 动态结构体
    printf("\n=== 动态结构体 ===\n");
    // 动态分配结构体
    Person *ptr2 = (Person *)malloc(sizeof(Person));
    if (ptr2 == NULL) {
        printf("内存分配失败\n");
        return 1;
    }
    
    // 初始化结构体
    strcpy(ptr2->name, "Alice");
    ptr2->age = 25;
    ptr2->height = 1.65;
    
    // 访问结构体成员
    printf("Name: %s\n", ptr2->name);
    printf("Age: %d\n", ptr2->age);
    printf("Height: %.2f\n", ptr2->height);
    
    // 释放内存
    free(ptr2);
    
    // 3. 结构体嵌套
    printf("\n=== 结构体嵌套 ===\n");
    
    // 嵌套结构体
    printf("\n=== 嵌套结构体 ===\n");
    // 初始化嵌套结构体
    PersonWithBirthday p5 = {
        "Alice",
        {15, 5, 1995},
        1.65
    };
    
    // 访问嵌套结构体成员
    printf("Name: %s\n", p5.name);
    printf("Birthday: %d/%d/%d\n", p5.birthday.day, p5.birthday.month, p5.birthday.year);
    printf("Height: %.2f\n", p5.height);
    
    // 结构体指针嵌套
    printf("\n=== 结构体指针嵌套 ===\n");
    // 动态分配日期结构体
    Date *date = (Date *)malloc(sizeof(Date));
    date->day = 15;
    date->month = 5;
    date->year = 1995;
    
    // 初始化Person结构体
    PersonWithBirthdayPtr p6 = {
        "Alice",
        date,
        1.65
    };
    
    // 访问嵌套结构体成员
    printf("Name: %s\n", p6.name);
    printf("Birthday: %d/%d/%d\n", p6.birthday->day, p6.birthday->month, p6.birthday->year);
    printf("Height: %.2f\n", p6.height);
    
    // 释放内存
    free(date);
    
    // 4. 共用体
    printf("\n=== 共用体 ===\n");
    
    // 共用体定义与使用
    printf("\n=== 共用体定义与使用 ===\n");
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
    
    // 5. 结构体与函数
    printf("\n=== 结构体与函数 ===\n");
    
    // 结构体作为函数参数
    printf("\n=== 结构体作为函数参数 ===\n");
    Person p7 = {"Alice", 25, 1.65};
    
    printf("Original:\n");
    print_person(p7);
    
    update_person(&p7);
    
    printf("\nUpdated:\n");
    print_person(p7);
    
    // 结构体作为函数返回值
    printf("\n=== 结构体作为函数返回值 ===\n");
    Point p8 = create_point(1, 2);
    Point p9 = create_point(3, 4);
    Point p10 = add_points(p8, p9);
    
    printf("p8: (%d, %d)\n", p8.x, p8.y);
    printf("p9: (%d, %d)\n", p9.x, p9.y);
    printf("p10: (%d, %d)\n", p10.x, p10.y);
    
    return 0;
}