import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class BestPracticesDemo {
    
    private static SqlSessionFactory sqlSessionFactory;
    
    static {
        try {
            String resource = "mybatis-config.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        // 测试最佳实践
        testBestPractices();
    }
    
    private static void testBestPractices() {
        System.out.println("\n=== 测试 MyBatis 最佳实践 ===");
        
        try (SqlSession sqlSession = sqlSessionFactory.openSession()) {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            
            // 1. 测试参数传递
            testParameterPassing(userMapper);
            
            // 2. 测试批量操作
            testBatchOperations(userMapper, sqlSession);
            
            // 3. 测试动态 SQL
            testDynamicSQL(userMapper);
            
            // 4. 测试结果映射
            testResultMapping(userMapper);
        }
    }
    
    private static void testParameterPassing(UserMapper userMapper) {
        System.out.println("\n1. 测试参数传递");
        
        // 单个参数
        User user = userMapper.getUserById(1);
        System.out.println("单个参数查询：" + user);
        
        // 多个参数（@Param注解）
        User userByNameAndPassword = userMapper.getUserByNameAndPassword("张三", "123456");
        System.out.println("多个参数查询：" + userByNameAndPassword);
    }
    
    private static void testBatchOperations(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n2. 测试批量操作");
        
        // 批量插入
        List<User> users = new ArrayList<>();
        users.add(new User(0, "赵六", "666666"));
        users.add(new User(0, "孙七", "777777"));
        users.add(new User(0, "周八", "888888"));
        
        int batchInsertResult = userMapper.batchInsert(users);
        System.out.println("批量插入结果：" + batchInsertResult);
        
        // 批量删除
        List<Integer> ids = new ArrayList<>();
        ids.add(4);
        ids.add(5);
        ids.add(6);
        
        int batchDeleteResult = userMapper.batchDelete(ids);
        System.out.println("批量删除结果：" + batchDeleteResult);
        
        sqlSession.commit();
    }
    
    private static void testDynamicSQL(UserMapper userMapper) {
        System.out.println("\n3. 测试动态 SQL");
        
        // 条件查询
        User userCondition = new User();
        userCondition.setName("张");
        List<User> users = userMapper.getUserByCondition(userCondition);
        System.out.println("动态 SQL 查询结果：");
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testResultMapping(UserMapper userMapper) {
        System.out.println("\n4. 测试结果映射");
        
        // 关联查询
        User userWithOrders = userMapper.getUserWithOrders(1);
        System.out.println("用户信息：" + userWithOrders);
        System.out.println("订单列表：");
        for (Order order : userWithOrders.getOrders()) {
            System.out.println(order);
        }
    }
}

// 实体类
class User {
    private int id;
    private String name;
    private String password;
    private List<Order> orders;
    
    public User() {
    }
    
    public User(int id, String name, String password) {
        this.id = id;
        this.name = name;
        this.password = password;
    }
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getPassword() {
        return password;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }
    
    public List<Order> getOrders() {
        return orders;
    }
    
    public void setOrders(List<Order> orders) {
        this.orders = orders;
    }
    
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}

class Order {
    private int id;
    private String orderNo;
    private double amount;
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getOrderNo() {
        return orderNo;
    }
    
    public void setOrderNo(String orderNo) {
        this.orderNo = orderNo;
    }
    
    public double getAmount() {
        return amount;
    }
    
    public void setAmount(double amount) {
        this.amount = amount;
    }
    
    @Override
    public String toString() {
        return "Order{" +
                "id=" + id +
                ", orderNo='" + orderNo + '\'' +
                ", amount=" + amount +
                '}';
    }
}

// Mapper 接口
interface UserMapper {
    // 单个参数
    User getUserById(int id);
    
    // 多个参数
    User getUserByNameAndPassword(String name, String password);
    
    // 批量操作
    int batchInsert(List<User> users);
    int batchDelete(List<Integer> ids);
    
    // 动态 SQL
    List<User> getUserByCondition(User user);
    
    // 结果映射
    User getUserWithOrders(int id);
}