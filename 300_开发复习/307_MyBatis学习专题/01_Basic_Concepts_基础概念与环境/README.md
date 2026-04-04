# MyBatis 基础概念与环境搭建

## 什么是 MyBatis？

MyBatis 是一个优秀的持久层框架，它支持定制化 SQL、存储过程以及高级映射。MyBatis 避免了几乎所有的 JDBC 代码和手动设置参数以及获取结果集的操作。

## MyBatis 的优势

- 简单易学，上手快
- 灵活，SQL 语句与代码分离
- 提供强大的映射功能，支持对象与数据库表的映射
- 支持动态 SQL
- 与 Spring 框架集成良好

## 环境搭建

### 1. Maven 依赖

```xml
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.10</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.30</version>
</dependency>
```

### 2. 配置文件

#### mybatis-config.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mybatis_demo?useSSL=false&amp;serverTimezone=UTC"/>
                <property name="username" value="root"/>
                <property name="password" value="password"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <mapper resource="mappers/UserMapper.xml"/>
    </mappers>
</configuration>
```

### 3. 目录结构

```
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── pojo/
│   │   │           │   └── User.java
│   │   │           ├── mapper/
│   │   │           │   └── UserMapper.java
│   │   │           └── utils/
│   │   │               └── MyBatisUtils.java
│   │   └── resources/
│   │       ├── mybatis-config.xml
│   │       └── mappers/
│   │           └── UserMapper.xml
```

## 快速入门示例

### 1. 创建实体类

```java
public class User {
    private int id;
    private String name;
    private String password;
    
    // getter 和 setter 方法
    // toString 方法
}
```

### 2. 创建 Mapper 接口

```java
public interface UserMapper {
    List<User> getUserList();
}
```

### 3. 创建 Mapper XML 文件

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">
    <select id="getUserList" resultType="com.example.pojo.User">
        select * from user
    </select>
</mapper>
```

### 4. 创建工具类

```java
public class MyBatisUtils {
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
    
    public static SqlSession getSqlSession() {
        return sqlSessionFactory.openSession();
    }
}
```

### 5. 测试代码

```java
public class MyBatisTest {
    @Test
    public void test() {
        SqlSession sqlSession = MyBatisUtils.getSqlSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        List<User> userList = userMapper.getUserList();
        
        for (User user : userList) {
            System.out.println(user);
        }
        
        sqlSession.close();
    }
}
```

## 数据库准备

```sql
CREATE DATABASE mybatis_demo;

USE mybatis_demo;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    password VARCHAR(20)
);

INSERT INTO user (name, password) VALUES
('张三', '123456'),
('李四', '654321'),
('王五', '111111');
```