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

public class ParameterMappingDemo {
    
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
            
            // 测试单个参数
            testSingleParameter(userMapper);
            
            // 测试多个参数（@Param注解）
            testMultipleParameters(userMapper);
            
            // 测试Map参数
            testMapParameter(userMapper);
            
            // 测试对象参数
            testObjectParameter(userMapper);
            
            // 测试数组参数
            testArrayParameter(userMapper);
            
            // 测试集合参数
            testListParameter(userMapper);
        }
    }
    
    private static void testSingleParameter(UserMapper userMapper) {
        System.out.println("\n=== 测试单个参数 ===");
        User user = userMapper.getUserById(1);
        System.out.println("根据ID查询：" + user);
        
        List<User> users = userMapper.getUserByName("张");
        System.out.println("根据名称查询：");
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testMultipleParameters(UserMapper userMapper) {
        System.out.println("\n=== 测试多个参数（@Param注解） ===");
        User user = userMapper.getUserByNameAndPassword("张三", "123456");
        System.out.println("根据名称和密码查询：" + user);
    }
    
    private static void testMapParameter(UserMapper userMapper) {
        System.out.println("\n=== 测试Map参数 ===");
        Map<String, Object> map = new HashMap<>();
        map.put("name", "李四");
        map.put("password", "654321");
        User user = userMapper.getUserByMap(map);
        System.out.println("根据Map查询：" + user);
    }
    
    private static void testObjectParameter(UserMapper userMapper) {
        System.out.println("\n=== 测试对象参数 ===");
        User user = new User();
        user.setName("王五");
        user.setPassword("111111");
        List<User> users = userMapper.getUserByCondition(user);
        System.out.println("根据对象查询：");
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testArrayParameter(UserMapper userMapper) {
        System.out.println("\n=== 测试数组参数 ===");
        int[] ids = {1, 2, 3};
        List<User> users = userMapper.getUserByIds(ids);
        System.out.println("根据ID数组查询：");
        for (User u : users) {
            System.out.println(u);
        }
    }
    
    private static void testListParameter(UserMapper userMapper) {
        System.out.println("\n=== 测试集合参数 ===");
        List<Integer> ids = new ArrayList<>();
        ids.add(1);
        ids.add(2);
        List<User> users = userMapper.getUserByIdList(ids);
        System.out.println("根据ID集合查询：");
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
    // 单个参数
    User getUserById(int id);
    List<User> getUserByName(String name);
    
    // 多个参数（@Param注解）
    User getUserByNameAndPassword(String name, String password);
    
    // Map参数
    User getUserByMap(Map<String, Object> map);
    
    // 对象参数
    List<User> getUserByCondition(User user);
    
    // 数组参数
    List<User> getUserByIds(int[] ids);
    
    // 集合参数
    List<User> getUserByIdList(List<Integer> ids);
}