import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DynamicSQLDemo {
    
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
            
            // 测试if标签
            testIfTag(userMapper);
            
            // 测试where标签
            testWhereTag(userMapper);
            
            // 测试set标签
            testSetTag(userMapper, sqlSession);
            
            // 测试foreach标签
            testForeachTag(userMapper);
            
            // 测试choose标签
            testChooseTag(userMapper);
            
            // 测试bind标签
            testBindTag(userMapper);
        }
    }
    
    private static void testIfTag(UserMapper userMapper) {
        System.out.println("\n=== 测试if标签 ===");
        User user = new User();
        user.setName("张三");
        List<User> users = userMapper.getUserListIf(user);
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testWhereTag(UserMapper userMapper) {
        System.out.println("\n=== 测试where标签 ===");
        User user = new User();
        user.setName("李四");
        user.setPassword("654321");
        List<User> users = userMapper.getUserListWhere(user);
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testSetTag(UserMapper userMapper, SqlSession sqlSession) {
        System.out.println("\n=== 测试set标签 ===");
        User user = new User();
        user.setId(1);
        user.setPassword("999999");
        int result = userMapper.updateUserSet(user);
        if (result > 0) {
            System.out.println("更新成功！");
        }
        sqlSession.commit();
    }
    
    private static void testForeachTag(UserMapper userMapper) {
        System.out.println("\n=== 测试foreach标签 ===");
        List<Integer> ids = new ArrayList<>();
        ids.add(1);
        ids.add(2);
        ids.add(3);
        List<User> users = userMapper.getUserListForeach(ids);
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testChooseTag(UserMapper userMapper) {
        System.out.println("\n=== 测试choose标签 ===");
        User user = new User();
        user.setName("王五");
        List<User> users = userMapper.getUserListChoose(user);
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testBindTag(UserMapper userMapper) {
        System.out.println("\n=== 测试bind标签 ===");
        User user = new User();
        user.setName("张");
        List<User> users = userMapper.getUserListBind(user);
        for (User u : users) {
            System.out.println(u);
        }
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
    // 测试if标签
    List<User> getUserListIf(User user);
    
    // 测试where标签
    List<User> getUserListWhere(User user);
    
    // 测试set标签
    int updateUserSet(User user);
    
    // 测试foreach标签
    List<User> getUserListForeach(List<Integer> ids);
    
    // 测试choose标签
    List<User> getUserListChoose(User user);
    
    // 测试bind标签
    List<User> getUserListBind(User user);
}