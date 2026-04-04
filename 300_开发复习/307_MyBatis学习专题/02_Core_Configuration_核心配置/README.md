# MyBatis 核心配置

## 配置文件结构

MyBatis 的核心配置文件是 `mybatis-config.xml`，它包含了 MyBatis 运行所需的各种设置。

## 配置文件详解

### 1. 配置文件结构

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- 配置项 -->
</configuration>
```

### 2. 配置顺序

MyBatis 配置文件中的元素必须按照以下顺序排列：

1. `properties` - 属性
2. `settings` - 设置
3. `typeAliases` - 类型别名
4. `typeHandlers` - 类型处理器
5. `objectFactory` - 对象工厂
6. `plugins` - 插件
7. `environments` - 环境配置
8. `databaseIdProvider` - 数据库厂商标识
9. `mappers` - 映射器

### 3. 详细配置项

#### 3.1 properties

用于引入外部属性文件或定义属性。

```xml
<properties resource="db.properties">
    <property name="username" value="root"/>
    <property name="password" value="password"/>
</properties>
```

#### 3.2 settings

MyBatis 的核心设置，影响 MyBatis 的运行行为。

```xml
<settings>
    <!-- 全局开启或关闭延迟加载 -->
    <setting name="lazyLoadingEnabled" value="true"/>
    <!-- 开启驼峰命名转换 -->
    <setting name="mapUnderscoreToCamelCase" value="true"/>
    <!-- 开启二级缓存 -->
    <setting name="cacheEnabled" value="true"/>
    <!-- 配置默认的执行器 -->
    <setting name="defaultExecutorType" value="REUSE"/>
    <!-- 设置超时时间 -->
    <setting name="defaultStatementTimeout" value="30"/>
</settings>
```

#### 3.3 typeAliases

为 Java 类型设置别名，减少全限定名的使用。

```xml
<typeAliases>
    <!-- 单个类型别名 -->
    <typeAlias type="com.example.pojo.User" alias="User"/>
    <!-- 包扫描，会为包下的所有类设置别名（默认为类名小写） -->
    <package name="com.example.pojo"/>
</typeAliases>
```

#### 3.4 typeHandlers

类型处理器，用于 Java 类型和 JDBC 类型之间的转换。

```xml
<typeHandlers>
    <typeHandler handler="com.example.handler.CustomTypeHandler"/>
</typeHandlers>
```

#### 3.5 environments

环境配置，可以配置多个环境，默认使用的环境通过 `default` 属性指定。

```xml
<environments default="development">
    <environment id="development">
        <!-- 事务管理器 -->
        <transactionManager type="JDBC"/>
        <!-- 数据源 -->
        <dataSource type="POOLED">
            <property name="driver" value="${driver}"/>
            <property name="url" value="${url}"/>
            <property name="username" value="${username}"/>
            <property name="password" value="${password}"/>
        </dataSource>
    </environment>
    <environment id="test">
        <!-- 测试环境配置 -->
    </environment>
</environments>
```

#### 3.6 mappers

映射器配置，指定 MyBatis 映射文件的位置。

```xml
<mappers>
    <!-- 通过资源路径引入 -->
    <mapper resource="mappers/UserMapper.xml"/>
    <!-- 通过类路径引入 -->
    <mapper class="com.example.mapper.UserMapper"/>
    <!-- 通过包扫描引入 -->
    <package name="com.example.mapper"/>
</mappers>
```

## 配置示例

### 完整配置文件示例

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- 引入外部属性文件 -->
    <properties resource="db.properties"/>
    
    <!-- 核心设置 -->
    <settings>
        <setting name="lazyLoadingEnabled" value="true"/>
        <setting name="mapUnderscoreToCamelCase" value="true"/>
        <setting name="cacheEnabled" value="true"/>
    </settings>
    
    <!-- 类型别名 -->
    <typeAliases>
        <package name="com.example.pojo"/>
    </typeAliases>
    
    <!-- 环境配置 -->
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${driver}"/>
                <property name="url" value="${url}"/>
                <property name="username" value="${username}"/>
                <property name="password" value="${password}"/>
            </dataSource>
        </environment>
    </environments>
    
    <!-- 映射器 -->
    <mappers>
        <package name="com.example.mapper"/>
    </mappers>
</configuration>
```

### 属性文件示例 (db.properties)

```properties
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/mybatis_demo?useSSL=false&serverTimezone=UTC
username=root
password=password
```

## 最佳实践

1. **使用外部属性文件**：将数据库连接信息等配置放到外部属性文件中，便于维护和环境切换。

2. **使用包扫描**：对于类型别名和映射器，使用包扫描可以减少配置代码。

3. **合理配置 settings**：根据实际需求配置 settings，例如开启驼峰命名转换可以减少手动映射的工作量。

4. **配置多个环境**：为开发、测试、生产等不同环境配置不同的环境信息，便于切换。

5. **使用连接池**：MyBatis 内置了三种数据源类型：UNPOOLED、POOLED、JNDI。在生产环境中建议使用 POOLED 或 JNDI 数据源。