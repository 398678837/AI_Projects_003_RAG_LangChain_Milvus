import java.util.*;
import java.util.concurrent.*;

// 1. 编码规范示例
class BestPracticesDemo {
    
    // 常量定义
    private static final int MAX_RETRY_COUNT = 3;
    private static final long TIMEOUT = 1000;
    
    // 成员变量
    private String userName;
    private int userAge;
    
    // 构造方法
    public BestPracticesDemo(String userName, int userAge) {
        this.userName = userName;
        this.userAge = userAge;
    }
    
    // 方法示例
    /**
     * 获取用户信息
     * @return 用户信息
     */
    public String getUserInfo() {
        return "姓名：" + userName + "，年龄：" + userAge;
    }
    
    // 性能优化示例
    public List<String> processData(List<String> data) {
        // 避免在循环中创建对象
        List<String> result = new ArrayList<>(data.size());
        
        for (String item : data) {
            // 处理数据
            String processedItem = processItem(item);
            result.add(processedItem);
        }
        
        return result;
    }
    
    private String processItem(String item) {
        // 简单处理
        return item.toUpperCase();
    }
    
    // 并发优化示例
    public void processTasks(List<Runnable> tasks) {
        // 使用线程池
        ExecutorService executor = Executors.newFixedThreadPool(5);
        
        for (Runnable task : tasks) {
            executor.execute(task);
        }
        
        executor.shutdown();
        try {
            executor.awaitTermination(1, TimeUnit.HOURS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    // 安全编程示例
    public String sanitizeInput(String input) {
        if (input == null) {
            return null;
        }
        
        // 去除HTML标签
        return input.replaceAll("<.*?>", "");
    }
    
    // 异常处理示例
    public void handleException() {
        try {
            // 可能抛出异常的代码
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            // 处理异常
            System.err.println("算术异常：" + e.getMessage());
        } catch (Exception e) {
            // 处理其他异常
            System.err.println("其他异常：" + e.getMessage());
        } finally {
            // 清理资源
            System.out.println("清理资源");
        }
    }
    
    // 日志示例
    public void logExample() {
        // 使用Java自带日志框架
        java.util.logging.Logger logger = java.util.logging.Logger.getLogger(BestPracticesDemo.class.getName());
        
        logger.info("普通信息");
        logger.warning("警告信息");
        logger.severe("错误信息");
    }
    
    // 测试示例
    public static void main(String[] args) {
        BestPracticesDemo demo = new BestPracticesDemo("张三", 25);
        
        // 测试用户信息
        System.out.println(demo.getUserInfo());
        
        // 测试数据处理
        List<String> data = Arrays.asList("java", "python", "c++");
        List<String> processedData = demo.processData(data);
        System.out.println("处理后的数据：" + processedData);
        
        // 测试异常处理
        demo.handleException();
        
        // 测试输入清理
        String input = "<script>alert('xss')</script>";
        String sanitizedInput = demo.sanitizeInput(input);
        System.out.println("清理后的输入：" + sanitizedInput);
    }
}

// 2. 设计模式最佳实践
class SingletonBestPractice {
    private static volatile SingletonBestPractice instance;
    
    private SingletonBestPractice() {
        // 防止反射创建实例
        if (instance != null) {
            throw new IllegalStateException("单例对象已存在");
        }
    }
    
    public static SingletonBestPractice getInstance() {
        if (instance == null) {
            synchronized (SingletonBestPractice.class) {
                if (instance == null) {
                    instance = new SingletonBestPractice();
                }
            }
        }
        return instance;
    }
    
    // 防止反序列化创建实例
    private Object readResolve() {
        return instance;
    }
}

// 3. 并发最佳实践
class ConcurrentBestPractice {
    private final java.util.concurrent.locks.Lock lock = new java.util.concurrent.locks.ReentrantLock();
    private int count = 0;
    
    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }
    
    public int getCount() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }
}

// 4. 资源管理最佳实践
class ResourceManagementBestPractice implements AutoCloseable {
    private java.sql.Connection connection;
    
    public ResourceManagementBestPractice() {
        // 初始化资源
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "user", "password");
        } catch (java.sql.SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void executeQuery(String sql) throws java.sql.SQLException {
        java.sql.Statement statement = connection.createStatement();
        java.sql.ResultSet resultSet = statement.executeQuery(sql);
        
        // 处理结果
        while (resultSet.next()) {
            System.out.println(resultSet.getString(1));
        }
        
        // 关闭资源
        resultSet.close();
        statement.close();
    }
    
    @Override
    public void close() throws Exception {
        // 关闭资源
        if (connection != null) {
            connection.close();
        }
    }
}