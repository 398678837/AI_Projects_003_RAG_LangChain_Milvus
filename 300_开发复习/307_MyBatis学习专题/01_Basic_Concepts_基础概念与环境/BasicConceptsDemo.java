import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class BasicConceptsDemo {
    
    //  SqlSessionFactory 实例
    private static SqlSessionFactory sqlSessionFactory;
    
    static {
        try {
            // 读取配置文件
            String resource = "mybatis-config.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            // 构建 SqlSessionFactory
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    // 获取 SqlSession 实例
    public static SqlSession getSqlSession() {
        return sqlSessionFactory.openSession();
    }
    
    public static void main(String[] args) {
        // 获取 SqlSession
        SqlSession sqlSession = getSqlSession();
        
        try {
            // 获取 Mapper 接口
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            
            // 调用方法查询用户列表
            List<User> userList = userMapper.getUserList();
            
            // 输出结果
            System.out.println("用户列表：");
            for (User user : userList) {
                System.out.println(user);
            }
        } finally {
            // 关闭 SqlSession
            sqlSession.close();
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