# MyBatis CRUD 操作

## CRUD 操作概述

CRUD 是指创建（Create）、读取（Read）、更新（Update）和删除（Delete）操作，这是数据库操作的基本功能。MyBatis 提供了丰富的映射标签来支持这些操作。

## 1. 查询操作（Read）

### 1.1 基本查询

```xml
<select id="getUserById" parameterType="int" resultType="User">
    select * from user where id = #{id}
</select>
```

### 1.2 模糊查询

```xml
<select id="getUserByName" parameterType="String" resultType="User">
    select * from user where name like concat('%', #{name}, '%')
</select>
```

### 1.3 查询所有

```xml
<select id="getUserList" resultType="User">
    select * from user
</select>
```

## 2. 插入操作（Create）

### 2.1 基本插入

```xml
<insert id="addUser" parameterType="User">
    insert into user (name, password) values (#{name}, #{password})
</insert>
```

### 2.2 插入并返回主键

```xml
<insert id="addUserReturnId" parameterType="User" useGeneratedKeys="true" keyProperty="id">
    insert into user (name, password) values (#{name}, #{password})
</insert>
```

## 3. 更新操作（Update）

### 3.1 基本更新

```xml
<update id="updateUser" parameterType="User">
    update user set name = #{name}, password = #{password} where id = #{id}
</update>
```

### 3.2 条件更新

```xml
<update id="updateUserSelective" parameterType="User">
    update user
    <set>
        <if test="name != null">name = #{name},</if>
        <if test="password != null">password = #{password}</if>
    </set>
    where id = #{id}
</update>
```

## 4. 删除操作（Delete）

### 4.1 根据 ID 删除

```xml
<delete id="deleteUserById" parameterType="int">
    delete from user where id = #{id}
</delete>
```

### 4.2 批量删除

```xml
<delete id="deleteUserByIds" parameterType="java.util.List">
    delete from user where id in
    <foreach collection="list" item="id" open="(" separator="," close=")">
        #{id}
    </foreach>
</delete>
```

## 5. Mapper 接口定义

```java
public interface UserMapper {
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
```

## 6. 测试代码

```java
public class CRUDTest {
    private SqlSession sqlSession;
    private UserMapper userMapper;
    
    @Before
    public void setUp() {
        sqlSession = MyBatisUtils.getSqlSession();
        userMapper = sqlSession.getMapper(UserMapper.class);
    }
    
    @After
    public void tearDown() {
        sqlSession.close();
    }
    
    // 测试查询
    @Test
    public void testSelect() {
        User user = userMapper.getUserById(1);
        System.out.println(user);
        
        List<User> userList = userMapper.getUserList();
        for (User u : userList) {
            System.out.println(u);
        }
    }
    
    // 测试插入
    @Test
    public void testInsert() {
        User user = new User();
        user.setName("赵六");
        user.setPassword("666666");
        int result = userMapper.addUser(user);
        if (result > 0) {
            System.out.println("插入成功！");
        }
        sqlSession.commit(); // 提交事务
    }
    
    // 测试更新
    @Test
    public void testUpdate() {
        User user = userMapper.getUserById(4);
        user.setPassword("888888");
        int result = userMapper.updateUser(user);
        if (result > 0) {
            System.out.println("更新成功！");
        }
        sqlSession.commit(); // 提交事务
    }
    
    // 测试删除
    @Test
    public void testDelete() {
        int result = userMapper.deleteUserById(4);
        if (result > 0) {
            System.out.println("删除成功！");
        }
        sqlSession.commit(); // 提交事务
    }
}
```

## 7. 注意事项

1. **事务管理**：对于增删改操作，需要手动提交事务（`sqlSession.commit()`），否则操作不会生效。

2. **参数传递**：
   - 单个参数可以直接使用 `#{参数名}`
   - 多个参数可以使用 `@Param` 注解或封装成对象

3. **返回值**：
   - 查询操作的返回值类型通过 `resultType` 或 `resultMap` 指定
   - 增删改操作的返回值是影响的行数

4. **SQL 注入**：MyBatis 使用 `#{}` 占位符可以防止 SQL 注入，而 `${}` 则不会，使用时需注意。

5. **主键返回**：对于自增主键，可以使用 `useGeneratedKeys` 和 `keyProperty` 属性来获取插入后的主键值。

6. **批量操作**：使用 `<foreach>` 标签可以实现批量操作，如批量删除、批量插入等。