import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class CollectionsDemo {
    public static void main(String[] args) {
        // 1. List接口
        System.out.println("=== List接口演示 ===");
        List<String> arrayList = new ArrayList<>();
        arrayList.add("Java");
        arrayList.add("Python");
        arrayList.add("C++");
        
        for (String language : arrayList) {
            System.out.println(language);
        }
        
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.addFirst("First");
        linkedList.addLast("Last");
        System.out.println("LinkedList第一个元素：" + linkedList.getFirst());
        
        // 2. Set接口
        System.out.println("\n=== Set接口演示 ===");
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Apple"); // 重复元素不会被添加
        System.out.println("HashSet大小：" + hashSet.size());
        
        LinkedHashSet<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("Red");
        linkedHashSet.add("Green");
        linkedHashSet.add("Blue");
        System.out.println("LinkedHashSet：" + linkedHashSet);
        
        TreeSet<Integer> treeSet = new TreeSet<>();
        treeSet.add(3);
        treeSet.add(1);
        treeSet.add(2);
        System.out.println("TreeSet：" + treeSet);
        
        // 3. Map接口
        System.out.println("\n=== Map接口演示 ===");
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("张三", 25);
        hashMap.put("李四", 30);
        hashMap.put("王五", 28);
        
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        LinkedHashMap<String, String> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("A", "Apple");
        linkedHashMap.put("B", "Banana");
        linkedHashMap.put("C", "Cherry");
        System.out.println("LinkedHashMap：" + linkedHashMap);
        
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("C", 3);
        treeMap.put("A", 1);
        treeMap.put("B", 2);
        System.out.println("TreeMap：" + treeMap);
        
        // 4. 集合工具类
        System.out.println("\n=== 集合工具类演示 ===");
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(2);
        Collections.sort(list);
        System.out.println("排序后的List：" + list);
        
        Collections.reverse(list);
        System.out.println("反转后的List：" + list);
        
        // 5. 泛型
        System.out.println("\n=== 泛型演示 ===");
        Box<String> box = new Box<>();
        box.setContent("Hello World");
        System.out.println("Box内容：" + box.getContent());
        
        // 6. 迭代器
        System.out.println("\n=== 迭代器演示 ===");
        List<String> iteratorList = new ArrayList<>();
        iteratorList.add("Java");
        iteratorList.add("Python");
        iteratorList.add("C++");
        
        Iterator<String> iterator = iteratorList.iterator();
        while (iterator.hasNext()) {
            String language = iterator.next();
            System.out.println(language);
        }
        
        // 7. 并发集合
        System.out.println("\n=== 并发集合演示 ===");
        ConcurrentHashMap<String, Integer> concurrentHashMap = new ConcurrentHashMap<>();
        concurrentHashMap.put("A", 1);
        concurrentHashMap.put("B", 2);
        concurrentHashMap.put("C", 3);
        System.out.println("ConcurrentHashMap：" + concurrentHashMap);
    }
}

// 泛型类
class Box<T> {
    private T content;
    
    public void setContent(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
}