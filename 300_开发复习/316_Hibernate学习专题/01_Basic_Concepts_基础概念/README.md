# 01_Basic_Concepts_基础概念

## 学习目标
- 理解ORM和Hibernate的基本概念
- 掌握Hibernate的核心优势
- 学会配置Hibernate
- 理解Hibernate的工作原理
- 掌握第一个Hibernate程序的编写

## 关键要点
### 1. ORM概述
- ORM（Object-Relational Mapping）：对象关系映射
- 将面向对象模型映射到关系型数据库
- 用对象操作代替SQL操作
- 提高开发效率，减少重复代码

### 2. Hibernate简介
- 开源的Java持久化框架
- 轻量级ORM框架
- 支持多种数据库
- 自动生成SQL
- 缓存机制
- 事务管理

### 3. Hibernate核心优势
- 消除大量JDBC代码
- 面向对象编程，不用写SQL
- 可移植性强，支持多种数据库
- 缓存机制提高性能
- 自动映射，减少配置

### 4. Hibernate架构
- Configuration：配置管理
- SessionFactory：Session工厂
- Session：会话，CRUD操作
- Transaction：事务管理
- Query：查询接口
- Criteria：查询接口

### 5. Hibernate配置
- hibernate.cfg.xml：主配置文件
- 数据库连接配置
- 方言配置
- 映射文件配置
- 缓存配置
- 日志配置

## 实践任务
1. 下载并配置Hibernate
2. 创建Hibernate配置文件
3. 编写第一个实体类
4. 实现CRUD操作

## 参考资料
- Hibernate官方文档：https://hibernate.org/orm/documentation/
- 《Hibernate实战》
