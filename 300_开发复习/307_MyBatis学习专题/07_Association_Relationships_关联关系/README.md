# MyBatis 关联关系

## 关联关系概述

在实际的数据库设计中，表与表之间往往存在各种关联关系，如一对一、一对多、多对多等。MyBatis 提供了强大的关联映射功能，可以方便地处理这些关联关系。

## 1. 一对一关系

### 1.1 嵌套结果映射

使用 `<association>` 标签来映射一对一关系。

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

### 1.2 嵌套查询

使用 `select` 属性来实现懒加载的一对一关系。

#### XML 映射

```xml
<resultMap id="UserResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <association property="address" column="address_id" select="getAddressById"/>
</resultMap>

<select id="getUserById" parameterType="int" resultMap="UserResultMap">
    select * from user where id = #{id}
</select>

<select id="getAddressById" parameterType="int" resultType="Address">
    select * from address where id = #{id}
</select>
```

## 2. 一对多关系

### 2.1 嵌套结果映射

使用 `<collection>` 标签来映射一对多关系。

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

### 2.2 嵌套查询

使用 `select` 属性来实现懒加载的一对多关系。

#### XML 映射

```xml
<resultMap id="UserResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <collection property="orders" column="id" select="getOrdersByUserId"/>
</resultMap>

<select id="getUserById" parameterType="int" resultMap="UserResultMap">
    select * from user where id = #{id}
</select>

<select id="getOrdersByUserId" parameterType="int" resultType="Order">
    select * from order where user_id = #{id}
</select>
```

## 3. 多对多关系

多对多关系通常需要通过中间表来实现。

### 3.1 嵌套结果映射

#### XML 映射

```xml
<resultMap id="UserWithRolesResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <collection property="roles" ofType="Role">
        <id property="id" column="role_id"/>
        <result property="roleName" column="role_name"/>
    </collection>
</resultMap>

<select id="getUserWithRoles" parameterType="int" resultMap="UserWithRolesResultMap">
    select u.id, u.name, u.password, r.id as role_id, r.role_name
    from user u
    left join user_role ur on u.id = ur.user_id
    left join role r on ur.role_id = r.id
    where u.id = #{id}
</select>
```

### 3.2 嵌套查询

#### XML 映射

```xml
<resultMap id="UserResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <collection property="roles" column="id" select="getRolesByUserId"/>
</resultMap>

<select id="getUserById" parameterType="int" resultMap="UserResultMap">
    select * from user where id = #{id}
</select>

<select id="getRolesByUserId" parameterType="int" resultType="Role">
    select r.*
    from role r
    left join user_role ur on r.id = ur.role_id
    where ur.user_id = #{id}
</select>
```

## 4. 关联关系的加载方式

### 4.1 立即加载

立即加载是指在查询主对象的同时，立即查询关联对象。

```xml
<association property="address" column="address_id" javaType="Address" fetchType="eager">
    <!-- 映射配置 -->
</association>
```

### 4.2 延迟加载

延迟加载是指在查询主对象时，不立即查询关联对象，而是在需要使用关联对象时才进行查询。

```xml
<association property="address" column="address_id" javaType="Address" fetchType="lazy">
    <!-- 映射配置 -->
</association>
```

### 4.3 全局配置

可以在 MyBatis 配置文件中全局配置延迟加载。

```xml
<settings>
    <setting name="lazyLoadingEnabled" value="true"/>
    <setting name="aggressiveLazyLoading" value="false"/>
</settings>
```

## 5. 关联关系的最佳实践

1. **使用合适的加载方式**：根据实际需求选择立即加载或延迟加载。

2. **避免 N+1 查询问题**：对于一对多关系，使用嵌套结果映射可以避免 N+1 查询问题。

3. **合理使用连接查询**：对于复杂的关联关系，使用连接查询可以减少数据库查询次数。

4. **使用别名**：在多表连接查询中，使用别名可以避免列名冲突。

5. **注意性能问题**：对于复杂的关联关系，要注意查询性能，避免过度关联。

6. **使用缓存**：对于频繁查询的关联数据，可以使用缓存来提高性能。

## 6. 关联关系示例

### 6.1 一对一关系示例

#### 实体类

```java
public class User {
    private int id;
    private String name;
    private String password;
    private Address address;
    // getter 和 setter 方法
}

public class Address {
    private int id;
    private String street;
    private String city;
    // getter 和 setter 方法
}
```

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

### 6.2 一对多关系示例

#### 实体类

```java
public class User {
    private int id;
    private String name;
    private String password;
    private List<Order> orders;
    // getter 和 setter 方法
}

public class Order {
    private int id;
    private String orderNo;
    private double amount;
    // getter 和 setter 方法
}
```

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

### 6.3 多对多关系示例

#### 实体类

```java
public class User {
    private int id;
    private String name;
    private String password;
    private List<Role> roles;
    // getter 和 setter 方法
}

public class Role {
    private int id;
    private String roleName;
    // getter 和 setter 方法
}
```

#### XML 映射

```xml
<resultMap id="UserWithRolesResultMap" type="User">
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
    <collection property="roles" ofType="Role">
        <id property="id" column="role_id"/>
        <result property="roleName" column="role_name"/>
    </collection>
</resultMap>

<select id="getUserWithRoles" parameterType="int" resultMap="UserWithRolesResultMap">
    select u.id, u.name, u.password, r.id as role_id, r.role_name
    from user u
    left join user_role ur on u.id = ur.user_id
    left join role r on ur.role_id = r.id
    where u.id = #{id}
</select>
```

## 7. 总结

MyBatis 提供了强大的关联映射功能，可以方便地处理一对一、一对多和多对多等关联关系。通过使用 `<association>` 和 `<collection>` 标签，可以实现复杂的对象关联映射。在实际开发中，应该根据具体的需求选择合适的关联映射方式，并注意性能问题。