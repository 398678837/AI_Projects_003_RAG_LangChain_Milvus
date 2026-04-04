# MyBatis 结果映射

## 结果映射概述

结果映射是 MyBatis 中非常重要的一个概念，它用于将 SQL 查询结果映射到 Java 对象中。MyBatis 提供了多种结果映射方式，从简单的自动映射到复杂的自定义映射。

## 1. 基本结果映射

### 1.1 resultType

当 SQL 查询结果的列名与 Java 对象的属性名一致时，可以使用 `resultType` 直接指定返回类型。

#### XML 映射

```xml
<select id="getUserById" parameterType="int" resultType="User">
    select id, name, password from user where id = #{id}
</select>
```

#### 实体类

```java
public class User {
    private int id;
    private String name;
    private String password;
    // getter 和 setter 方法
}
```

### 1.2 resultMap

当 SQL 查询结果的列名与 Java 对象的属性名不一致时，需要使用 `resultMap` 进行自定义映射。

#### XML 映射

```xml
<resultMap id="UserResultMap" type="User">
    <id property="id" column="user_id"/>
    <result property="name" column="user_name"/>
    <result property="password" column="user_password"/>
</resultMap>

<select id="getUserById" parameterType="int" resultMap="UserResultMap">
    select user_id, user_name, user_password from user where user_id = #{id}
</select>
```

## 2. 高级结果映射

### 2.1 关联映射（一对一）

当需要映射一对一关系时，可以使用 `<association>` 标签。

#### XML 映射

```xml
<resultMap id="UserWithAddressResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <association property="address" column="address_id" javaType="Address">
        <id property="id" column="address_id"/>
        <result property="street" column="street"/>
        <result property="city" column="city"/>
    </association>
</resultMap>

<select id="getUserWithAddress" parameterType="int" resultMap="UserWithAddressResultMap">
    select u.id, u.name, u.password, a.id as address_id, a.street, a.city
    from user u
    left join address a on u.address_id = a.id
    where u.id = #{id}
</select>
```

### 2.2 集合映射（一对多）

当需要映射一对多关系时，可以使用 `<collection>` 标签。

#### XML 映射

```xml
<resultMap id="UserWithOrdersResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <collection property="orders" ofType="Order">
        <id property="id" column="order_id"/>
        <result property="orderNo" column="order_no"/>
        <result property="amount" column="amount"/>
    </collection>
</resultMap>

<select id="getUserWithOrders" parameterType="int" resultMap="UserWithOrdersResultMap">
    select u.id, u.name, u.password, o.id as order_id, o.order_no, o.amount
    from user u
    left join order o on u.id = o.user_id
    where u.id = #{id}
</select>
```

### 2.3 鉴别器映射

当需要根据条件选择不同的结果类型时，可以使用 `<discriminator>` 标签。

#### XML 映射

```xml
<resultMap id="PersonResultMap" type="Person">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <discriminator javaType="int" column="type">
        <case value="1" resultType="Student">
            <result property="studentId" column="student_id"/>
            <result property="grade" column="grade"/>
        </case>
        <case value="2" resultType="Teacher">
            <result property="teacherId" column="teacher_id"/>
            <result property="subject" column="subject"/>
        </case>
    </discriminator>
</resultMap>

<select id="getPerson" parameterType="int" resultMap="PersonResultMap">
    select id, name, type, student_id, grade, teacher_id, subject from person where id = #{id}
</select>
```

## 3. 结果映射技巧

### 3.1 自动映射

MyBatis 默认支持自动映射，当列名与属性名一致时，会自动进行映射。可以通过设置 `autoMappingBehavior` 来控制自动映射的行为。

```xml
<settings>
    <setting name="autoMappingBehavior" value="PARTIAL"/>
</settings>
```

### 3.2 驼峰命名转换

当数据库列名使用下划线命名（如 `user_name`），而 Java 属性使用驼峰命名（如 `userName`）时，可以开启驼峰命名转换。

```xml
<settings>
    <setting name="mapUnderscoreToCamelCase" value="true"/>
</settings>
```

### 3.3 级联查询

可以使用 `select` 属性来实现懒加载的级联查询。

```xml
<resultMap id="UserResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <association property="address" column="address_id" select="getAddressById"/>
</resultMap>

<select id="getAddressById" parameterType="int" resultType="Address">
    select * from address where id = #{id}
</select>
```

### 3.4 构造器注入

当需要通过构造器来创建对象时，可以使用 `<constructor>` 标签。

```xml
<resultMap id="UserResultMap" type="User">
    <constructor>
        <idArg column="id" javaType="int"/>
        <arg column="name" javaType="String"/>
        <arg column="password" javaType="String"/>
    </constructor>
</resultMap>
```

## 4. 结果映射类型

### 4.1 基本类型

```xml
<select id="getUserCount" resultType="int">
    select count(*) from user
</select>
```

### 4.2 字符串类型

```xml
<select id="getUserNameById" parameterType="int" resultType="string">
    select name from user where id = #{id}
</select>
```

### 4.3 日期类型

```xml
<select id="getUserCreateTime" parameterType="int" resultType="date">
    select create_time from user where id = #{id}
</select>
```

### 4.4 集合类型

```xml
<select id="getUserList" resultType="User">
    select * from user
</select>
```

### 4.5 Map类型

```xml
<select id="getUserMap" parameterType="int" resultType="map">
    select * from user where id = #{id}
</select>
```

## 5. 最佳实践

1. **使用 resultType**：当列名与属性名一致时，使用 `resultType` 可以简化配置。

2. **使用 resultMap**：当列名与属性名不一致时，使用 `resultMap` 可以实现自定义映射。

3. **开启驼峰命名转换**：对于下划线命名的数据库列，开启驼峰命名转换可以减少手动映射的工作量。

4. **合理使用关联映射**：对于复杂的关联关系，使用 `<association>` 和 `<collection>` 标签可以实现对象间的关联。

5. **注意性能问题**：对于复杂的关联查询，要注意 N+1 查询问题，可以使用连接查询或延迟加载来优化。

6. **使用类型别名**：为复杂的类型使用类型别名可以减少配置代码。