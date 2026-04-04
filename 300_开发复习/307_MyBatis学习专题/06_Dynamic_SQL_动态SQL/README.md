# MyBatis 动态 SQL

## 动态 SQL 概述

动态 SQL 是 MyBatis 的一个强大特性，它允许在 SQL 语句中根据条件动态地构建查询。通过使用 MyBatis 提供的动态 SQL 标签，可以编写更加灵活和可维护的 SQL 语句。

## 1. 动态 SQL 标签

### 1.1 if 标签

`if` 标签用于条件判断，当条件为真时，包含的 SQL 语句才会被执行。

```xml
<select id="getUserList" parameterType="User" resultType="User">
    select * from user
    <where>
        <if test="name != null and name != ''">
            and name = #{name}
        </if>
        <if test="password != null and password != ''">
            and password = #{password}
        </if>
    </where>
</select>
```

### 1.2 choose、when、otherwise 标签

`choose`、`when`、`otherwise` 标签用于多条件选择，类似于 Java 中的 switch-case 语句。

```xml
<select id="getUserList" parameterType="User" resultType="User">
    select * from user
    <where>
        <choose>
            <when test="id != null">
                and id = #{id}
            </when>
            <when test="name != null and name != ''">
                and name = #{name}
            </when>
            <otherwise>
                and 1=1
            </otherwise>
        </choose>
    </where>
</select>
```

### 1.3 trim、where、set 标签

`trim`、`where`、`set` 标签用于处理 SQL 语句中的空白和多余的关键字。

#### where 标签

```xml
<select id="getUserList" parameterType="User" resultType="User">
    select * from user
    <where>
        <if test="name != null and name != ''">
            name = #{name}
        </if>
        <if test="password != null and password != ''">
            and password = #{password}
        </if>
    </where>
</select>
```

#### set 标签

```xml
<update id="updateUser" parameterType="User">
    update user
    <set>
        <if test="name != null and name != ''">
            name = #{name},
        </if>
        <if test="password != null and password != ''">
            password = #{password}
        </if>
    </set>
    where id = #{id}
</update>
```

#### trim 标签

```xml
<select id="getUserList" parameterType="User" resultType="User">
    select * from user
    <trim prefix="where" prefixOverrides="and | or">
        <if test="name != null and name != ''">
            and name = #{name}
        </if>
        <if test="password != null and password != ''">
            and password = #{password}
        </if>
    </trim>
</select>
```

### 1.4 foreach 标签

`foreach` 标签用于遍历集合或数组，常用于构建 IN 条件或批量操作。

#### 遍历集合

```xml
<select id="getUserByIds" parameterType="list" resultType="User">
    select * from user
    where id in
    <foreach collection="list" item="id" open="(" separator="," close=")">
        #{id}
    </foreach>
</select>
```

#### 批量插入

```xml
<insert id="batchInsert" parameterType="list">
    insert into user (name, password) values
    <foreach collection="list" item="user" separator=",">
        (#{user.name}, #{user.password})
    </foreach>
</insert>
```

### 1.5 bind 标签

`bind` 标签用于创建一个变量并绑定到上下文，常用于模糊查询。

```xml
<select id="getUserByName" parameterType="User" resultType="User">
    <bind name="nameLike" value="'%' + name + '%'"/>
    select * from user
    where name like #{nameLike}
</select>
```

## 2. 动态 SQL 示例

### 2.1 条件查询

```xml
<select id="getUserList" parameterType="User" resultType="User">
    select * from user
    <where>
        <if test="id != null">
            and id = #{id}
        </if>
        <if test="name != null and name != ''">
            and name like concat('%', #{name}, '%')
        </if>
        <if test="password != null and password != ''">
            and password = #{password}
        </if>
    </where>
</select>
```

### 2.2 动态更新

```xml
<update id="updateUser" parameterType="User">
    update user
    <set>
        <if test="name != null and name != ''">
            name = #{name},
        </if>
        <if test="password != null and password != ''">
            password = #{password},
        </if>
        <if test="updateTime != null">
            update_time = #{updateTime}
        </if>
    </set>
    where id = #{id}
</update>
```

### 2.3 批量操作

```xml
<delete id="batchDelete" parameterType="list">
    delete from user
    where id in
    <foreach collection="list" item="id" open="(" separator="," close=")">
        #{id}
    </foreach>
</delete>
```

### 2.4 复杂条件查询

```xml
<select id="getUserList" parameterType="Map" resultType="User">
    select * from user
    <where>
        <if test="id != null">
            and id = #{id}
        </if>
        <if test="name != null and name != ''">
            and name like concat('%', #{name}, '%')
        </if>
        <choose>
            <when test="age != null">
                and age = #{age}
            </when>
            <otherwise>
                and age > 18
            </otherwise>
        </choose>
        <if test="ids != null and ids.size() > 0">
            and id in
            <foreach collection="ids" item="id" open="(" separator="," close=")">
                #{id}
            </foreach>
        </if>
    </where>
    <if test="orderBy != null and orderBy != ''">
        order by #{orderBy}
    </if>
</select>
```

## 3. 动态 SQL 最佳实践

1. **使用 where 标签**：`where` 标签会自动处理多余的 `and` 或 `or` 关键字，使 SQL 语句更加简洁。

2. **使用 set 标签**：`set` 标签会自动处理多余的逗号，使更新语句更加简洁。

3. **使用 foreach 标签**：`foreach` 标签是处理批量操作的最佳选择，可以简化代码。

4. **使用 bind 标签**：`bind` 标签可以避免在 SQL 语句中使用字符串拼接，提高代码的可读性和安全性。

5. **使用 choose 标签**：当有多个条件需要选择时，使用 `choose` 标签可以使代码更加清晰。

6. **合理使用 if 标签**：`if` 标签是最常用的动态 SQL 标签，适用于大多数条件判断场景。

7. **注意参数类型**：在使用动态 SQL 时，要注意参数的类型，特别是集合类型和数组类型。

8. **测试动态 SQL**：由于动态 SQL 会根据不同的条件生成不同的 SQL 语句，因此需要测试各种条件下生成的 SQL 语句是否正确。

## 4. 动态 SQL 的优缺点

### 优点

- **灵活性高**：可以根据不同的条件生成不同的 SQL 语句。
- **可维护性好**：将条件判断逻辑集中在 XML 文件中，使代码更加清晰。
- **减少代码量**：避免了在 Java 代码中拼接 SQL 语句的繁琐工作。
- **提高可读性**：使用标签化的语法，使 SQL 语句更加易于理解。

### 缺点

- **学习成本**：需要学习 MyBatis 的动态 SQL 标签语法。
- **调试困难**：动态生成的 SQL 语句可能难以调试。
- **性能影响**：复杂的动态 SQL 可能会影响性能。

## 5. 总结

动态 SQL 是 MyBatis 的一个强大特性，它允许在 SQL 语句中根据条件动态地构建查询。通过使用 MyBatis 提供的动态 SQL 标签，可以编写更加灵活和可维护的 SQL 语句。在实际开发中，应该根据具体的需求选择合适的动态 SQL 标签，以达到最佳的效果。