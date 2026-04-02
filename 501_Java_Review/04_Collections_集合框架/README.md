# Java集合框架

## 1. 集合框架概述

### 1.1 集合与数组的区别
- **数组**：长度固定，只能存储相同类型的元素
- **集合**：长度可变，可以存储不同类型的元素（泛型出现后建议存储相同类型）

### 1.2 集合框架体系
```
Collection
├─ List：有序、可重复
│  ├─ ArrayList：基于动态数组实现，查询快、增删慢
│  ├─ LinkedList：基于双向链表实现，查询慢、增删快
│  └─ Vector：线程安全的ArrayList，性能较差
├─ Set：无序、不可重复
│  ├─ HashSet：基于哈希表实现，无序、不可重复
│  ├─ LinkedHashSet：基于哈希表和链表实现，有序、不可重复
│  └─ TreeSet：基于红黑树实现，可排序
└─ Queue：队列，先进先出
   ├─ LinkedList：实现了Queue接口
   └─ PriorityQueue：优先队列

Map
├─ HashMap：基于哈希表实现，无序、键唯一
├─ LinkedHashMap：基于哈希表和链表实现，有序、键唯一
├─ TreeMap：基于红黑树实现，可排序
└─ Hashtable：线程安全的HashMap，性能较差
```

## 2. List接口

### 2.1 ArrayList
```java
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");

// 遍历
for (String language : list) {
    System.out.println(language);
}

// 获取元素
String first = list.get(0);

// 删除元素
list.remove(1);
```

### 2.2 LinkedList
```java
LinkedList<String> linkedList = new LinkedList<>();
linkedList.addFirst("First");
linkedList.addLast("Last");

String first = linkedList.getFirst();
String last = linkedList.getLast();

linkedList.removeFirst();
linkedList.removeLast();
```

## 3. Set接口

### 3.1 HashSet
```java
Set<String> set = new HashSet<>();
set.add("Apple");
set.add("Banana");
set.add("Apple"); // 重复元素，不会被添加

System.out.println(set.size()); // 输出2
```

### 3.2 LinkedHashSet
```java
Set<String> linkedHashSet = new LinkedHashSet<>();
linkedHashSet.add("Red");
linkedHashSet.add("Green");
linkedHashSet.add("Blue");

// 输出顺序与添加顺序一致
for (String color : linkedHashSet) {
    System.out.println(color);
}
```

### 3.3 TreeSet
```java
Set<Integer> treeSet = new TreeSet<>();
treeSet.add(3);
treeSet.add(1);
treeSet.add(2);

// 输出顺序为1, 2, 3
for (Integer num : treeSet) {
    System.out.println(num);
}
```

## 4. Map接口

### 4.1 HashMap
```java
Map<String, Integer> map = new HashMap<>();
map.put("张三", 25);
map.put("李四", 30);
map.put("王五", 28);

// 获取值
int age = map.get("张三");

// 遍历
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

### 4.2 LinkedHashMap
```java
Map<String, String> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put("A", "Apple");
linkedHashMap.put("B", "Banana");
linkedHashMap.put("C", "Cherry");

// 输出顺序与添加顺序一致
for (Map.Entry<String, String> entry : linkedHashMap.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

### 4.3 TreeMap
```java
Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("C", 3);
treeMap.put("A", 1);
treeMap.put("B", 2);

// 输出顺序为A:1, B:2, C:3
for (Map.Entry<String, Integer> entry : treeMap.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

## 5. 集合工具类

### 5.1 Collections类
```java
List<Integer> list = new ArrayList<>();
list.add(3);
list.add(1);
list.add(2);

// 排序
Collections.sort(list);

// 反转
Collections.reverse(list);

// 随机打乱
Collections.shuffle(list);

// 二分查找
int index = Collections.binarySearch(list, 2);
```

### 5.2 Arrays类
```java
int[] arr = {3, 1, 2};

// 数组转集合
List<Integer> list = Arrays.asList(1, 2, 3);

// 排序
Arrays.sort(arr);

// 二分查找
int index = Arrays.binarySearch(arr, 2);

// 数组转字符串
String str = Arrays.toString(arr);
```

## 6. 泛型

### 6.1 泛型的作用
- 提高代码的安全性
- 避免类型转换
- 提高代码的复用性

### 6.2 泛型的使用
```java
// 泛型类
public class Box<T> {
    private T content;
    
    public void setContent(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
}

// 泛型方法
public <T> T getFirstElement(List<T> list) {
    if (list == null || list.isEmpty()) {
        return null;
    }
    return list.get(0);
}

// 通配符
public void printList(List<?> list) {
    for (Object obj : list) {
        System.out.println(obj);
    }
}
```

## 7. 迭代器

### 7.1 Iterator接口
```java
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");

Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String language = iterator.next();
    System.out.println(language);
    iterator.remove(); // 删除元素
}
```

### 7.2 ListIterator接口
```java
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");

ListIterator<String> listIterator = list.listIterator();
while (listIterator.hasNext()) {
    String language = listIterator.next();
    if (language.equals("Python")) {
        listIterator.add("JavaScript");
    }
}
```

## 8. 并发集合

### 8.1 ConcurrentHashMap
```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("C", 3);
```

### 8.2 CopyOnWriteArrayList
```java
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");
```

## 9. 集合选择指南

### 9.1 选择List
- 需要频繁查询：ArrayList
- 需要频繁增删：LinkedList
- 需要线程安全：Vector或CopyOnWriteArrayList

### 9.2 选择Set
- 需要快速查找：HashSet
- 需要保持插入顺序：LinkedHashSet
- 需要排序：TreeSet

### 9.3 选择Map
- 需要快速查找：HashMap
- 需要保持插入顺序：LinkedHashMap
- 需要排序：TreeMap
- 需要线程安全：ConcurrentHashMap

## 10. 集合性能分析

| 集合类型       | 插入性能 | 查询性能 | 删除性能 | 线程安全 |
|----------------|----------|----------|----------|----------|
| ArrayList      | 一般     | 优秀     | 一般     | 否       |
| LinkedList     | 优秀     | 一般     | 优秀     | 否       |
| HashSet        | 优秀     | 优秀     | 优秀     | 否       |
| LinkedHashSet  | 优秀     | 优秀     | 优秀     | 否       |
| TreeSet        | 一般     | 一般     | 一般     | 否       |
| HashMap        | 优秀     | 优秀     | 优秀     | 否       |
| LinkedHashMap  | 优秀     | 优秀     | 优秀     | 否       |
| TreeMap        | 一般     | 一般     | 一般     | 否       |
| ConcurrentHashMap | 优秀   | 优秀     | 优秀     | 是       |
| CopyOnWriteArrayList | 一般 | 优秀     | 一般     | 是       |