public class HelloWorld {
    public static void main(String[] args) {
        // 输出Hello World
        System.out.println("Hello, World!");
        
        // 变量声明与使用
        int age = 25;
        String name = "张三";
        System.out.println("姓名：" + name + "，年龄：" + age);
        
        // 条件判断
        if (age >= 18) {
            System.out.println("成年人");
        } else {
            System.out.println("未成年人");
        }
        
        // 循环结构
        for (int i = 1; i <= 5; i++) {
            System.out.println("循环次数：" + i);
        }
    }
}