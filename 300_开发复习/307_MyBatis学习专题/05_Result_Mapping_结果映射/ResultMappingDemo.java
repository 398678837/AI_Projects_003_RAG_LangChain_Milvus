import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

public class ResultMappingDemo {
    
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
        try (SqlSession sqlSession = sqlSessionFactory.openSession()) {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            
            // 测试基本结果映射
            testBasicResultMapping(userMapper);
            
            // 测试自定义结果映射
            testCustomResultMapping(userMapper);
            
            // 测试关联结果映射
            testAssociationResultMapping(userMapper);
            
            // 测试集合结果映射
            testCollectionResultMapping(userMapper);
            
            // 测试Map结果映射
            testMapResultMapping(userMapper);
        }
    }
    
    private static void testBasicResultMapping(UserMapper userMapper) {
        System.out.println("\n=== 测试基本结果映射 ===");
        User user = userMapper.getUserById(1);
        System.out.println("基本结果映射：" + user);
    }
    
    private static void testCustomResultMapping(UserMapper userMapper) {
        System.out.println("\n=== 测试自定义结果映射 ===");
        User user = userMapper.getUserByIdCustom(1);
        System.out.println("自定义结果映射：" + user);
    }
    
    private static void testAssociationResultMapping(UserMapper userMapper) {
        System.out.println("\n=== 测试关联结果映射 ===");
        User userWithAddress = userMapper.getUserWithAddress(1);
        System.out.println("用户信息：" + userWithAddress);
        System.out.println("地址信息：" + userWithAddress.getAddress());
    }
    
    private static void testCollectionResultMapping(UserMapper userMapper) {
        System.out.println("\n=== 测试集合结果映射 ===");
        User userWithOrders = userMapper.getUserWithOrders(1);
        System.out.println("用户信息：" + userWithOrders);
        System.out.println("订单列表：");
        for (Order order : userWithOrders.getOrders()) {
            System.out.println(order);
        }
    }
    
    private static void testMapResultMapping(UserMapper userMapper) {
        System.out.println("\n=== 测试Map结果映射 ===");
        Map<String, Object> userMap = userMapper.getUserMap(1);
        System.out.println("Map结果映射：" + userMap);
    }
}

// 实体类
class User {
    private int id;
    private String name;
    private String password;
    private Address address;
    private List<Order> orders;
    
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
    
    public Address getAddress() {
        return address;
    }
    
    public void setAddress(Address address) {
        this.address = address;
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

class Address {
    private int id;
    private String street;
    private String city;
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getStreet() {
        return street;
    }
    
    public void setStreet(String street) {
        this.street = street;
    }
    
    public String getCity() {
        return city;
    }
    
    public void setCity(String city) {
        this.city = city;
    }
    
    @Override
    public String toString() {
        return "Address{" +
                "id=" + id +
                ", street='" + street + '\'' +
                ", city='" + city + '\'' +
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
    // 基本结果映射
    User getUserById(int id);
    
    // 自定义结果映射
    User getUserByIdCustom(int id);
    
    // 关联结果映射
    User getUserWithAddress(int id);
    
    // 集合结果映射
    User getUserWithOrders(int id);
    
    // Map结果映射
    Map<String, Object> getUserMap(int id);
}