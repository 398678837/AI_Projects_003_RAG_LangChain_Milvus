import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class CoreConfigurationDemo {
    
    public static void main(String[] args) {
        try {
            // 读取核心配置文件
            String resource = "mybatis-config.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            
            // 构建 SqlSessionFactory
            SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
            
            // 获取 SqlSession
            try (SqlSession sqlSession = sqlSessionFactory.openSession()) {
                // 获取 Mapper 接口
                UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
                
                // 测试不同配置的效果
                testBasicQuery(userMapper);
                testTypeAlias(sqlSession);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    private static void testBasicQuery(UserMapper userMapper) {
        System.out.println("\n=== 测试基本查询 ===");
        List<User> userList = userMapper.getUserList();
        for (User user : userList) {
            System.out.println(user);
        }
    }
    
    private static void testTypeAlias(SqlSession sqlSession) {
        System.out.println("\n=== 测试类型别名 ===");
        // 使用类型别名查询
        List<User> userList = sqlSession.selectList("com.example.mapper.UserMapper.getUserList");
        for (User user : userList) {
            System.out.println(user);
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
    List<User> getUserList();
}