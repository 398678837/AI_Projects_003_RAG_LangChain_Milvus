# Java实战应用

## 1. 项目概述

### 1.1 项目背景
- 随着互联网的发展，Java在企业级应用开发中占据重要地位
- 本实战应用将展示如何使用Java开发一个完整的企业级应用

### 1.2 项目目标
- 掌握Java企业级应用开发流程
- 掌握Spring Boot框架的使用
- 掌握数据库设计与开发
- 掌握前后端分离开发

### 1.3 技术栈
- **后端**：Java 8+、Spring Boot、Spring MVC、MyBatis
- **前端**：Vue.js、Element UI
- **数据库**：MySQL
- **工具**：Maven、Git、Docker

## 2. 项目架构

### 2.1 系统架构
```
前端
├─ Vue.js
├─ Element UI
└─ Axios

后端
├─ Spring Boot
├─ Spring MVC
├─ MyBatis
└─ MySQL

部署
├─ Docker
└─ Nginx
```

### 2.2 模块划分
- **用户管理模块**：用户注册、登录、权限管理
- **商品管理模块**：商品列表、商品详情、商品搜索
- **订单管理模块**：订单创建、订单查询、订单支付
- **购物车模块**：商品添加、购物车结算
- **支付模块**：支付宝支付、微信支付

### 2.3 数据库设计
```sql
-- 用户表
CREATE TABLE user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    create_time DATETIME NOT NULL,
    update_time DATETIME NOT NULL
);

-- 商品表
CREATE TABLE product (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    stock INT NOT NULL,
    create_time DATETIME NOT NULL,
    update_time DATETIME NOT NULL
);

-- 订单表
CREATE TABLE order (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    create_time DATETIME NOT NULL,
    update_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
```

## 3. 项目搭建

### 3.1 创建Spring Boot项目
```bash
# 使用Spring Initializr创建项目
curl https://start.spring.io/starter.zip \
  -d groupId=com.example \
  -d artifactId=demo \
  -d dependencies=web,mybatis,mysql \
  -o demo.zip

# 解压项目
unzip demo.zip

# 进入项目目录
cd demo
```

### 3.2 配置文件
```yaml
# application.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/demo
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
  
mybatis:
  mapper-locations: classpath:mapper/*.xml
  type-aliases-package: com.example.demo.entity

server:
  port: 8080
```

### 3.3 项目结构
```
demo
├─ src
│  ├─ main
│  │  ├─ java
│  │  │  ├─ com
│  │  │  │  ├─ example
│  │  │  │  │  ├─ demo
│  │  │  │  │  │  ├─ controller
│  │  │  │  │  │  ├─ service
│  │  │  │  │  │  ├─ mapper
│  │  │  │  │  │  ├─ entity
│  │  │  │  │  │  └─ DemoApplication.java
│  │  └─ resources
│  │     ├─ mapper
│  │     └─ application.yml
│  └─ test
│     └─ java
│        └─ com
│           └─ example
│              └─ demo
│                 └─ DemoApplicationTests.java
└─ pom.xml
```

## 4. 后端开发

### 4.1 实体类
```java
// User.java
public class User {
    private Long id;
    private String username;
    private String password;
    private String email;
    private String phone;
    private Date createTime;
    private Date updateTime;
    
    // getter和setter
}
```

### 4.2 Mapper接口
```java
// UserMapper.java
@Mapper
public interface UserMapper {
    User findById(Long id);
    User findByUsername(String username);
    int insert(User user);
    int update(User user);
    int delete(Long id);
}
```

### 4.3 Mapper XML
```xml
<!-- UserMapper.xml -->
<mapper namespace="com.example.demo.mapper.UserMapper">
    <select id="findById" resultType="com.example.demo.entity.User">
        SELECT * FROM user WHERE id = #{id}
    </select>
    
    <select id="findByUsername" resultType="com.example.demo.entity.User">
        SELECT * FROM user WHERE username = #{username}
    </select>
    
    <insert id="insert" parameterType="com.example.demo.entity.User">
        INSERT INTO user (username, password, email, phone, create_time, update_time)
        VALUES (#{username}, #{password}, #{email}, #{phone}, #{createTime}, #{updateTime})
    </insert>
    
    <update id="update" parameterType="com.example.demo.entity.User">
        UPDATE user SET
        username = #{username},
        password = #{password},
        email = #{email},
        phone = #{phone},
        update_time = #{updateTime}
        WHERE id = #{id}
    </update>
    
    <delete id="delete" parameterType="java.lang.Long">
        DELETE FROM user WHERE id = #{id}
    </delete>
</mapper>
```

### 4.4 Service层
```java
// UserService.java
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;
    
    public User findById(Long id) {
        return userMapper.findById(id);
    }
    
    public User findByUsername(String username) {
        return userMapper.findByUsername(username);
    }
    
    public int insert(User user) {
        Date now = new Date();
        user.setCreateTime(now);
        user.setUpdateTime(now);
        return userMapper.insert(user);
    }
    
    public int update(User user) {
        user.setUpdateTime(new Date());
        return userMapper.update(user);
    }
    
    public int delete(Long id) {
        return userMapper.delete(id);
    }
}
```

### 4.5 Controller层
```java
// UserController.java
@RestController
@RequestMapping("/api/user")
public class UserController {
    @Autowired
    private UserService userService;
    
    @GetMapping("/{id}")
    public User findById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping
    public int insert(@RequestBody User user) {
        return userService.insert(user);
    }
    
    @PutMapping
    public int update(@RequestBody User user) {
        return userService.update(user);
    }
    
    @DeleteMapping("/{id}")
    public int delete(@PathVariable Long id) {
        return userService.delete(id);
    }
}
```

## 5. 前端开发

### 5.1 创建Vue项目
```bash
# 使用Vue CLI创建项目
vue create frontend

# 进入项目目录
cd frontend

# 安装Element UI
npm install element-ui --save

# 安装Axios
npm install axios --save
```

### 5.2 配置文件
```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'

Vue.use(ElementUI)
Vue.prototype.$axios = axios

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### 5.3 页面组件
```vue
<!-- UserList.vue -->
<template>
  <div>
    <el-table :data="users" border>
      <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column prop="username" label="用户名"></el-table-column>
      <el-table-column prop="email" label="邮箱"></el-table-column>
      <el-table-column prop="phone" label="电话"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="editUser(scope.row)">编辑</el-button>
          <el-button @click="deleteUser(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: []
    }
  },
  mounted() {
    this.loadUsers()
  },
  methods: {
    async loadUsers() {
      const response = await this.$axios.get('/api/user')
      this.users = response.data
    },
    editUser(user) {
      // 编辑用户
    },
    async deleteUser(id) {
      await this.$axios.delete(`/api/user/${id}`)
      this.loadUsers()
    }
  }
}
</script>
```

## 6. 项目部署

### 6.1 打包项目
```bash
# 打包后端项目
mvn clean package

# 打包前端项目
cd frontend
npm run build
```

### 6.2 Docker部署
```dockerfile
# Dockerfile
FROM openjdk:8-jdk-alpine
COPY target/demo.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

```bash
# 构建Docker镜像
docker build -t demo:latest .

# 运行Docker容器
docker run -d -p 8080:8080 demo:latest
```

### 6.3 Nginx部署
```nginx
# nginx.conf
server {
    listen 80;
    server_name localhost;
    
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
    
    location /api {
        proxy_pass http://localhost:8080/api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 7. 项目测试

### 7.1 单元测试
```java
// UserServiceTest.java
@SpringBootTest
public class UserServiceTest {
    @Autowired
    private UserService userService;
    
    @Test
    public void testFindById() {
        User user = userService.findById(1L);
        assertNotNull(user);
    }
    
    @Test
    public void testInsert() {
        User user = new User();
        user.setUsername("test");
        user.setPassword("test");
        user.setEmail("test@example.com");
        int result = userService.insert(user);
        assertEquals(1, result);
    }
}
```

### 7.2 集成测试
```bash
# 使用Postman测试API
curl http://localhost:8080/api/user/1
curl -X POST -H "Content-Type: application/json" -d '{"username":"test","password":"test","email":"test@example.com"}' http://localhost:8080/api/user
```

### 7.3 性能测试
```bash
# 使用JMeter进行性能测试
jmeter -n -t test.jmx -l result.jtl
```

## 8. 项目优化

### 8.1 性能优化
- 使用Redis缓存
- 使用消息队列
- 使用异步处理

### 8.2 安全优化
- 使用JWT认证
- 使用HTTPS
- 使用防火墙

### 8.3 可维护性优化
- 使用代码生成器
- 使用自动化测试
- 使用持续集成

## 9. 项目扩展

### 9.1 功能扩展
- 添加搜索功能
- 添加推荐功能
- 添加支付功能

### 9.2 技术扩展
- 使用微服务架构
- 使用容器化部署
- 使用云服务

## 10. 项目总结

### 10.1 项目成果
- 完成了一个完整的企业级应用
- 掌握了Java企业级应用开发流程
- 掌握了Spring Boot框架的使用

### 10.2 项目经验
- 团队协作的重要性
- 代码质量的重要性
- 测试的重要性

### 10.3 未来展望
- 学习新技术
- 参与更多项目
- 提升技术水平