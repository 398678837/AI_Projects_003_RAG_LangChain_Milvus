import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;

public class CacheDemo {
    
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
        // 测试一级缓存
        testFirstLevelCache();
        
        // 测试二级缓存
        testSecondLevelCache();
    }
    
    private static void testFirstLevelCache() {
        System.out.println("\n=== 测试一级缓存 ===");
        
        SqlSession sqlSession = sqlSessionFactory.openSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        
        // 第一次查询，从数据库获取
        System.out.println("第一次查询：");
        User user1 = userMapper.getUserById(1);
        System.out.println(user1);
        
        // 第二次查询，从一级缓存获取
        System.out.println("\n第二次查询：");
        User user2 = userMapper.getUserById(1);
        System.out.println(user2);
        
        // 检查是否是同一个对象
        System.out.println("\n是否是同一个对象：" + (user1 == user2));
        
        // 执行更新操作，清空一级缓存
        System.out.println("\n执行更新操作：");
        userMapper.updateUser(new User(1, "张三", "999999"));
        sqlSession.commit();
        
        // 第三次查询，从数据库获取（因为缓存已清空）
        System.out.println("\n第三次查询：");
        User user3 = userMapper.getUserById(1);
        System.out.println(user3);
        
        // 检查是否是同一个对象
        System.out.println("\n是否是同一个对象：" + (user1 == user3));
        
        sqlSession.close();
    }
    
    private static void testSecondLevelCache() {
        System.out.println("\n=== 测试二级缓存 ===");
        
        // 第一个 SqlSession
        SqlSession sqlSession1 = sqlSessionFactory.openSession();
        UserMapper userMapper1 = sqlSession1.getMapper(UserMapper.class);
        
        // 第一次查询，从数据库获取
        System.out.println("第一个 SqlSession 查询：");
        User user1 = userMapper1.getUserById(1);
        System.out.println(user1);
        
        // 关闭 SqlSession，将数据写入二级缓存
        sqlSession1.close();
        
        // 第二个 SqlSession
        SqlSession sqlSession2 = sqlSessionFactory.openSession();
        UserMapper userMapper2 = sqlSession2.getMapper(UserMapper.class);
        
        // 第二次查询，从二级缓存获取
        System.out.println("\n第二个 SqlSession 查询：");
        User user2 = userMapper2.getUserById(1);
        System.out.println(user2);
        
        // 检查是否是同一个对象
        System.out.println("\n是否是同一个对象：" + (user1 == user2));
        
        // 执行更新操作，清空二级缓存
        System.out.println("\n执行更新操作：");
        userMapper2.updateUser(new User(1, "张三", "123456"));
        sqlSession2.commit();
        
        // 第三次查询，从数据库获取（因为缓存已清空）
        System.out.println("\n更新后的查询：");
        User user3 = userMapper2.getUserById(1);
        System.out.println(user3);
        
        sqlSession2.close();
    }
}

// 实体类
class User implements java.io.Serializable {
    private int id;
    private String name;
    private String password;
    
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
    User getUserById(int id);
    int updateUser(User user);
}