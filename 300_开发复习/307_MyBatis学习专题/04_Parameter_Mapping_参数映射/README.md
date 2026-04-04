# MyBatis 参数映射

## 参数映射概述

MyBatis 提供了多种参数映射方式，用于将 Java 方法参数传递到 SQL 语句中。了解这些参数映射方式对于编写灵活的 SQL 语句非常重要。

## 1. 单个参数

### 1.1 基本类型参数

对于单个基本类型参数（如 int、String 等），MyBatis 会直接将参数值传递给 SQL 语句中的占位符。

#### Mapper 接口

```java
User getUserById(int id);
```

#### XML 映射

```xml
<select id="getUserById" parameterType="int" resultType="User">
    select * from user where id = #{id}
</select>
```

### 1.2 字符串参数

```java
List<User> getUserByName(String name);
```

```xml
<select id="getUserByName" parameterType="String" resultType="User">
    select * from user where name = #{name}
</select>
```

## 2. 多个参数

### 2.1 使用 @Param 注解

当方法有多个参数时，可以使用 `@Param` 注解为每个参数指定名称。

#### Mapper 接口

```java
User getUserByNameAndPassword(@Param("name") String name, @Param("password") String password);
```

#### XML 映射

```xml
<select id="getUserByNameAndPassword" resultType="User">
    select * from user where name = #{name} and password = #{password}
</select>
```

### 2.2 使用 Map

可以使用 Map 来传递多个参数。

#### Mapper 接口

```java
User getUserByMap(Map<String, Object> map);
```

#### XML 映射

```xml
<select id="getUserByMap" parameterType="map" resultType="User">
    select * from user where name = #{name} and password = #{password}
</select>
```

#### 调用示例

```java
Map<String, Object> map = new HashMap<>();
map.put("name", "张三");
map.put("password", "123456");
User user = userMapper.getUserByMap(map);
```

### 2.3 使用对象

可以使用 Java 对象来传递多个参数。

#### Mapper 接口

```java
List<User> getUserByCondition(User user);
```

#### XML 映射

```xml
<select id="getUserByCondition" parameterType="User" resultType="User">
    select * from user where name = #{name} and password = #{password}
</select>
```

## 3. 特殊参数类型

### 3.1 数组参数

当参数是数组时，可以使用 `<foreach>` 标签来处理。

#### Mapper 接口

```java
List<User> getUserByIds(int[] ids);
```

#### XML 映射

```xml
<select id="getUserByIds" parameterType="int[]" resultType="User">
    select * from user where id in
    <foreach collection="array" item="id" open="(" separator="," close=")">
        #{id}
    </foreach>
</select>
```

### 3.2 集合参数

当参数是集合时，同样可以使用 `<foreach>` 标签来处理。

#### Mapper 接口

```java
List<User> getUserByIdList(List<Integer> ids);
```

#### XML 映射

```xml
<select id="getUserByIdList" parameterType="list" resultType="User">
    select * from user where id in
    <foreach collection="list" item="id" open="(" separator="," close=")">
        #{id}
    </foreach>
</select>
```

### 3.3 日期参数

对于日期类型参数，可以使用 JDBC 类型来指定。

#### Mapper 接口

```java
List<User> getUserByCreateTime(@Param("startTime") Date startTime, @Param("endTime") Date endTime);
```

#### XML 映射

```xml
<select id="getUserByCreateTime" resultType="User">
    select * from user where create_time between #{startTime, jdbcType=TIMESTAMP} and #{endTime, jdbcType=TIMESTAMP}
</select>
```

## 4. 参数传递方式

### 4.1 #{}

`#{}` 是 MyBatis 的参数占位符，它会将参数值进行预处理，防止 SQL 注入。

```xml
select * from user where id = #{id}
```

### 4.2 ${}

`${}` 是字符串替换，它会直接将参数值替换到 SQL 语句中，可能导致 SQL 注入，使用时需谨慎。

```xml
select * from user order by ${columnName}
```

### 4.3 区别

| 特性 | `#{}` | `${}` |
|------|-------|-------|
| SQL 注入 | 防止 | 可能导致 |
| 预处理 | 是 | 否 |
| 适用场景 | 大多数场景 | 表名、列名等动态部分 |

## 5. 高级参数映射

### 5.1 复杂对象

当参数是复杂对象时，可以使用点号（.）来访问对象的属性。

#### Mapper 接口

```java
List<User> getUserByUserQuery(UserQuery query);
```

#### XML 映射

```xml
<select id="getUserByUserQuery" parameterType="UserQuery" resultType="User">
    select * from user where name like concat('%', #{name}, '%') and age > #{age}
</select>
```

### 5.2 嵌套对象

对于嵌套对象，可以使用多级点号来访问。

#### Mapper 接口

```java
List<User> getUserByUserInfo(UserInfo userInfo);
```

#### XML 映射

```xml
<select id="getUserByUserInfo" parameterType="UserInfo" resultType="User">
    select * from user where name = #{user.name} and address = #{address.city}
</select>
```

## 6. 最佳实践

1. **使用 @Param 注解**：当方法有多个参数时，使用 `@Param` 注解可以使代码更清晰。

2. **使用对象传递参数**：对于多个相关参数，封装成对象可以提高代码的可维护性。

3. **优先使用 #{}**：在大多数情况下，使用 `#{}` 可以防止 SQL 注入，更安全。

4. **合理使用 ${}**：在需要动态表名或列名时，可以使用 `${}`，但要注意 SQL 注入的风险。

5. **使用 JDBC 类型**：对于特殊类型（如日期），指定 JDBC 类型可以避免类型转换错误。

6. **使用集合处理批量操作**：对于批量操作，使用集合参数配合 `<foreach>` 标签可以简化代码。