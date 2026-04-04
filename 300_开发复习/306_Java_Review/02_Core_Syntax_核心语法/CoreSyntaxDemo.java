public class CoreSyntaxDemo {
    public static void main(String[] args) {
        // 1. 变量与数据类型
        byte b = 100;
        short s = 2000;
        int i = 100000;
        long l = 10000000000L;
        float f = 3.14f;
        double d = 3.1415926;
        char c = 'A';
        boolean flag = true;
        
        System.out.println("基本数据类型演示：");
        System.out.println("byte: " + b);
        System.out.println("short: " + s);
        System.out.println("int: " + i);
        System.out.println("long: " + l);
        System.out.println("float: " + f);
        System.out.println("double: " + d);
        System.out.println("char: " + c);
        System.out.println("boolean: " + flag);
        
        // 2. 运算符
        int a = 10, b1 = 3;
        System.out.println("\n运算符演示：");
        System.out.println("a + b1: " + (a + b1));
        System.out.println("a - b1: " + (a - b1));
        System.out.println("a * b1: " + (a * b1));
        System.out.println("a / b1: " + (a / b1));
        System.out.println("a % b1: " + (a % b1));
        
        // 3. 条件语句
        int score = 85;
        System.out.println("\n条件语句演示：");
        if (score >= 90) {
            System.out.println("优秀");
        } else if (score >= 80) {
            System.out.println("良好");
        } else if (score >= 60) {
            System.out.println("及格");
        } else {
            System.out.println("不及格");
        }
        
        // 4. 循环语句
        System.out.println("\n循环语句演示：");
        for (int k = 0; k < 5; k++) {
            System.out.println("for循环：" + k);
        }
        
        int count = 0;
        while (count < 3) {
            System.out.println("while循环：" + count);
            count++;
        }
        
        // 5. 数组
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("\n数组演示：");
        for (int num : arr) {
            System.out.println(num);
        }
        
        // 6. 字符串
        String str1 = "Hello";
        String str2 = "World";
        String str3 = str1 + " " + str2;
        System.out.println("\n字符串演示：");
        System.out.println(str3);
        System.out.println("字符串长度：" + str3.length());
        System.out.println("是否包含'World'：" + str3.contains("World"));
        
        // 7. 异常处理
        System.out.println("\n异常处理演示：");
        try {
            int[] arr2 = new int[3];
            System.out.println(arr2[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("捕获到异常：" + e.getMessage());
        }
    }
}