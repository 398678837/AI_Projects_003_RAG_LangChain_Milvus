import java.lang.reflect.Method;
import java.lang.reflect.Field;

public class JVMDemo {
    public static void main(String[] args) {
        // 1. 类加载器
        System.out.println("=== 类加载器 ===");
        ClassLoader classLoader = ClassLoader.getSystemClassLoader();
        System.out.println("系统类加载器：" + classLoader);
        
        ClassLoader parent = classLoader.getParent();
        System.out.println("扩展类加载器：" + parent);
        
        ClassLoader grandParent = parent.getParent();
        System.out.println("启动类加载器：" + grandParent);
        
        // 2. 内存信息
        System.out.println("\n=== 内存信息 ===");
        Runtime runtime = Runtime.getRuntime();
        long maxMemory = runtime.maxMemory();
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        
        System.out.println("最大内存：" + maxMemory / 1024 / 1024 + "MB");
        System.out.println("总内存：" + totalMemory / 1024 / 1024 + "MB");
        System.out.println("空闲内存：" + freeMemory / 1024 / 1024 + "MB");
        System.out.println("已使用内存：" + (totalMemory - freeMemory) / 1024 / 1024 + "MB");
        
        // 3. 反射
        System.out.println("\n=== 反射 ===");
        try {
            Class<?> clazz = Class.forName("java.lang.String");
            System.out.println("类名：" + clazz.getName());
            
            Method[] methods = clazz.getDeclaredMethods();
            System.out.println("方法数量：" + methods.length);
            
            Field[] fields = clazz.getDeclaredFields();
            System.out.println("字段数量：" + fields.length);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        
        // 4. 垃圾回收
        System.out.println("\n=== 垃圾回收 ===");
        for (int i = 0; i < 10000; i++) {
            new Object();
        }
        System.gc(); // 建议垃圾回收
        
        // 5. 类的初始化
        System.out.println("\n=== 类的初始化 ===");
        MyClass myClass = new MyClass();
        System.out.println("静态变量：" + MyClass.staticVar);
        System.out.println("实例变量：" + myClass.instanceVar);
    }
}

class MyClass {
    public static String staticVar = "静态变量";
    public String instanceVar = "实例变量";
    
    static {
        System.out.println("静态代码块执行");
    }
    
    public MyClass() {
        System.out.println("构造方法执行");
    }
}