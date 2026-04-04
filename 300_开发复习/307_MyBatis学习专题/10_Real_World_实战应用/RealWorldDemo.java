import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class RealWorldDemo {
    
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
        // 测试完整的CRUD操作
        testCRUD();
        
        // 测试复杂查询
        testComplexQuery();
        
        // 测试事务处理
        testTransaction();
    }
    
    private static void testCRUD() {
        System.out.println("\n=== 测试完整的CRUD操作 ===");
        
        try (SqlSession sqlSession = sqlSessionFactory.openSession()) {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            
            // 1. 创建用户
            System.out.println("1. 创建用户");
            User user = new User();
            user.setName("测试用户");
            user.setPassword("123456");
            user.setEmail("test@example.com");
            user.setAge(25);
            
            int createResult = userMapper.addUser(user);
            System.out.println("创建用户结果：" + createResult);
            System.out.println("创建的用户ID：" + user.getId());
            
            // 2. 查询用户
            System.out.println("\n2. 查询用户");
            User queriedUser = userMapper.getUserById(user.getId());
            System.out.println("查询到的用户：" + queriedUser);
            
            // 3. 更新用户
            System.out.println("\n3. 更新用户");
            queriedUser.setName("更新后的测试用户");
            queriedUser.setAge(26);
            int updateResult = userMapper.updateUser(queriedUser);
            System.out.println("更新用户结果：" + updateResult);
            
            // 4. 查询更新后的用户
            User updatedUser = userMapper.getUserById(user.getId());
            System.out.println("更新后的用户：" + updatedUser);
            
            // 5. 删除用户
            System.out.println("\n4. 删除用户");
            int deleteResult = userMapper.deleteUser(user.getId());
            System.out.println("删除用户结果：" + deleteResult);
            
            // 6. 验证删除
            User deletedUser = userMapper.getUserById(user.getId());
            System.out.println("删除后查询用户：" + deletedUser);
            
            sqlSession.commit();
        }
    }
    
    private static void testComplexQuery() {
        System.out.println("\n=== 测试复杂查询 ===");
        
        try (SqlSession sqlSession = sqlSessionFactory.openSession()) {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            OrderMapper orderMapper = sqlSession.getMapper(OrderMapper.class);
            
            // 1. 条件查询
            System.out.println("1. 条件查询");
            User condition = new User();
            condition.setName("张");
            List<User> users = userMapper.getUserByCondition(condition);
            System.out.println("条件查询结果：");
            for (User u : users) {
                System.out.println(u);
            }
            
            // 2. 关联查询
            System.out.println("\n2. 关联查询");
            if (!users.isEmpty()) {
                Long userId = users.get(0).getId();
                List<Order> orders = orderMapper.getOrderByUserId(userId);
                System.out.println("用户ID " + userId + " 的订单：");
                for (Order order : orders) {
                    System.out.println(order);
                }
            }
        }
    }
    
    private static void testTransaction() {
        System.out.println("\n=== 测试事务处理 ===");
        
        SqlSession sqlSession = null;
        try {
            sqlSession = sqlSessionFactory.openSession();
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            OrderMapper orderMapper = sqlSession.getMapper(OrderMapper.class);
            
            // 1. 创建用户
            User user = new User();
            user.setName("事务测试用户");
            user.setPassword("123456");
            user.setEmail("transaction@example.com");
            user.setAge(30);
            
            int createUserResult = userMapper.addUser(user);
            System.out.println("创建用户结果：" + createUserResult);
            
            // 2. 创建订单
            Order order = new Order();
            order.setOrderNo("ORDER" + System.currentTimeMillis());
            order.setUserId(user.getId());
            order.setAmount(100.0);
            order.setStatus(1);
            
            int createOrderResult = orderMapper.addOrder(order);
            System.out.println("创建订单结果：" + createOrderResult);
            
            // 3. 提交事务
            sqlSession.commit();
            System.out.println("事务提交成功");
            
            // 4. 验证数据
            User createdUser = userMapper.getUserById(user.getId());
            Order createdOrder = orderMapper.getOrderById(order.getId());
            System.out.println("创建的用户：" + createdUser);
            System.out.println("创建的订单：" + createdOrder);
            
        } catch (Exception e) {
            // 5. 回滚事务
            if (sqlSession != null) {
                sqlSession.rollback();
                System.out.println("事务回滚成功");
            }
            e.printStackTrace();
        } finally {
            if (sqlSession != null) {
                sqlSession.close();
            }
        }
    }
}

// 实体类
class User {
    private Long id;
    private String name;
    private String password;
    private String email;
    private Integer age;
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
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
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public Integer getAge() {
        return age;
    }
    
    public void setAge(Integer age) {
        this.age = age;
    }
    
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", password='" + password + '\'' +
                ", email='" + email + '\'' +
                ", age=" + age +
                '}';
    }
}

class Order {
    private Long id;
    private String orderNo;
    private Long userId;
    private Double amount;
    private Integer status;
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getOrderNo() {
        return orderNo;
    }
    
    public void setOrderNo(String orderNo) {
        this.orderNo = orderNo;
    }
    
    public Long getUserId() {
        return userId;
    }
    
    public void setUserId(Long userId) {
        this.userId = userId;
    }
    
    public Double getAmount() {
        return amount;
    }
    
    public void setAmount(Double amount) {
        this.amount = amount;
    }
    
    public Integer getStatus() {
        return status;
    }
    
    public void setStatus(Integer status) {
        this.status = status;
    }
    
    @Override
    public String toString() {
        return "Order{" +
                "id=" + id +
                ", orderNo='" + orderNo + '\'' +
                ", userId=" + userId +
                ", amount=" + amount +
                ", status=" + status +
                '}';
    }
}

// Mapper 接口
interface UserMapper {
    User getUserById(Long id);
    List<User> getUserList();
    int addUser(User user);
    int updateUser(User user);
    int deleteUser(Long id);
    List<User> getUserByCondition(User user);
}

interface OrderMapper {
    Order getOrderById(Long id);
    List<Order> getOrderList();
    int addOrder(Order order);
    int updateOrder(Order order);
    int deleteOrder(Long id);
    List<Order> getOrderByUserId(Long userId);
}