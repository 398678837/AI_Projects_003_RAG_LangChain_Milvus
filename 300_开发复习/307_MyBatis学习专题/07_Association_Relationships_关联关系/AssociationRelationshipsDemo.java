import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class AssociationRelationshipsDemo {
    
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
            
            // 测试一对一关系
            testOneToOne(userMapper);
            
            // 测试一对多关系
            testOneToMany(userMapper);
            
            // 测试多对多关系
            testManyToMany(userMapper);
        }
    }
    
    private static void testOneToOne(UserMapper userMapper) {
        System.out.println("\n=== 测试一对一关系 ===");
        User userWithAddress = userMapper.getUserWithAddress(1);
        System.out.println("用户信息：" + userWithAddress);
        System.out.println("地址信息：" + userWithAddress.getAddress());
    }
    
    private static void testOneToMany(UserMapper userMapper) {
        System.out.println("\n=== 测试一对多关系 ===");
        User userWithOrders = userMapper.getUserWithOrders(1);
        System.out.println("用户信息：" + userWithOrders);
        System.out.println("订单列表：");
        for (Order order : userWithOrders.getOrders()) {
            System.out.println(order);
        }
    }
    
    private static void testManyToMany(UserMapper userMapper) {
        System.out.println("\n=== 测试多对多关系 ===");
        User userWithRoles = userMapper.getUserWithRoles(1);
        System.out.println("用户信息：" + userWithRoles);
        System.out.println("角色列表：");
        for (Role role : userWithRoles.getRoles()) {
            System.out.println(role);
        }
    }
}

// 实体类
class User {
    private int id;
    private String name;
    private String password;
    private Address address;
    private List<Order> orders;
    private List<Role> roles;
    
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
    
    public List<Role> getRoles() {
        return roles;
    }
    
    public void setRoles(List<Role> roles) {
        this.roles = roles;
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

class Role {
    private int id;
    private String roleName;
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getRoleName() {
        return roleName;
    }
    
    public void setRoleName(String roleName) {
        this.roleName = roleName;
    }
    
    @Override
    public String toString() {
        return "Role{" +
                "id=" + id +
                ", roleName='" + roleName + '\'' +
                '}';
    }
}

// Mapper 接口
interface UserMapper {
    // 测试一对一关系
    User getUserWithAddress(int id);
    
    // 测试一对多关系
    User getUserWithOrders(int id);
    
    // 测试多对多关系
    User getUserWithRoles(int id);
}