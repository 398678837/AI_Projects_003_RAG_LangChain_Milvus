# 02_Core_Components_核心组件

## 学习目标
- 理解Configuration的作用和配置
- 掌握SessionFactory的创建和管理
- 理解Session的生命周期和使用
- 掌握Transaction的管理
- 理解Query和Criteria的使用

## 关键要点
### 1. Configuration
- 负责加载Hibernate配置
- 加载映射文件
- 配置数据库连接
- 配置Hibernate属性
- 创建SessionFactory

### 2. SessionFactory
- Session工厂，线程安全
- 应用启动时创建一次
- 重量级对象，消耗资源
- 负责创建Session
- 管理二级缓存

### 3. Session
- 单线程对象，非线程安全
- 提供CRUD操作
- 管理一级缓存
- 事务边界
- openSession() vs getCurrentSession()

### 4. Transaction
- 事务管理
- 原子性操作
- commit()和rollback()
- 声明式事务 vs 编程式事务

### 5. Query
- HQL查询
- 命名查询
- 参数绑定
- 分页查询

### 6. Criteria
- 类型安全的查询
- 动态查询
- 面向对象的查询方式

## 实践任务
1. 使用Configuration配置Hibernate
2. 创建和管理SessionFactory
3. 使用Session进行CRUD操作
4. 管理事务
5. 使用Query和Criteria查询

## 参考资料
- Hibernate Core Components
