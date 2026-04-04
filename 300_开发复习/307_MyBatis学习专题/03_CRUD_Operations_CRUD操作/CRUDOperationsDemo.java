import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class CRUDOperationsDemo {
    
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
            
            // 测试查询操作
            testSelect(userMapper);
            
            // 测试插入操作
            testInsert(userMapper, sqlSession);
            
            // 测试更新操作
            testUpdate(userMapper, sqlSession);
            
            // 测试删除操作
            testDelete(userMapper, sqlSession);
            
            // 测试批量删除操作
            testBatchDelete(userMapper, sqlSession);
        }
    }
    
    private static void testSelect(UserMapper userMapper) {
        System.out.println("\n=== 测试查询操作 ===");
        
        // 根据ID查询
        User user = userMapper.getUserById(1);
        System.out.println("根据ID查询：" + user);
        
        // 查询所有
        List<User> userList = userMapper.getUserList();
        System.out.println("查询所有用户：");
        for (User u : userList) {
            System.out.println(u);
        }
        
        // 模糊查询
        List<User> usersByName = userMapper.getUserByName("张");
        System.out.println("模糊查询：");
        for (User u : usersByName) {
            System.out.println(u);
        }
    }
    
    private static void testInsert(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n=== 测试插入操作 ===");
        
        User user = new User();
        user.setName("赵六");
        user.setPassword("666666");
        
        int result = userMapper.addUser(user);
        if (result > 0) {
            System.out.println("插入成功！");
        }
        
        // 测试插入并返回主键
        User user2 = new User();
        user2.setName("孙七");
        user2.setPassword("777777");
        
        int result2 = userMapper.addUserReturnId(user2);
        if (result2 > 0) {
            System.out.println("插入并返回主键成功！ID: " + user2.getId());
        }
        
        sqlSession.commit();
    }
    
    private static void testUpdate(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n=== 测试更新操作 ===");
        
        User user = userMapper.getUserById(4);
        System.out.println("更新前：" + user);
        
        user.setPassword("888888");
        int result = userMapper.updateUser(user);
        if (result > 0) {
            System.out.println("更新成功！");
        }
        
        User updatedUser = userMapper.getUserById(4);
        System.out.println("更新后：" + updatedUser);
        
        sqlSession.commit();
    }
    
    private static void testDelete(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n=== 测试删除操作 ===");
        
        int result = userMapper.deleteUserById(5);
        if (result > 0) {
            System.out.println("删除成功！");
        }
        
        sqlSession.commit();
    }
    
    private static void testBatchDelete(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n=== 测试批量删除操作 ===");
        
        List<Integer> ids = new ArrayList<>();
        ids.add(6);
        ids.add(7);
        
        int result = userMapper.deleteUserByIds(ids);
        if (result > 0) {
            System.out.println("批量删除成功！删除了 " + result + " 条记录");
        }
        
        sqlSession.commit();
    }
}

// 实体类
class User {
    private int id;
    private String name;
    private String password;
    
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
    
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}

// Mapper 接口
interface UserMapper {
    // 查询操作
    User getUserById(int id);
    List<User> getUserList();
    List<User> getUserByName(String name);
    
    // 插入操作
    int addUser(User user);
    int addUserReturnId(User user);
    
    // 更新操作
    int updateUser(User user);
    int updateUserSelective(User user);
    
    // 删除操作
    int deleteUserById(int id);
    int deleteUserByIds(List<Integer> ids);
}