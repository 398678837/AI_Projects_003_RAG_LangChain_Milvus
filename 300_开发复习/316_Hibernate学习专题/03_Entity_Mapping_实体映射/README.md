# 03_Entity_Mapping_实体映射

## 学习目标
- 理解实体类的基本映射
- 掌握主键生成策略
- 学会属性映射
- 掌握关联关系映射
- 理解继承映射

## 关键要点
### 1. 基本映射
- @Entity：标记实体类
- @Table：指定表名
- @Column：指定列属性
- @Id：标记主键
- @GeneratedValue：主键生成策略

### 2. 主键生成策略
- GenerationType.AUTO：自动选择
- GenerationType.IDENTITY：自增
- GenerationType.SEQUENCE：序列
- GenerationType.TABLE：表生成

### 3. 属性映射
- @Transient：不映射到数据库
- @Temporal：日期时间类型
- @Lob：大对象
- @Enumerated：枚举类型

### 4. 关联关系映射
- 一对一：@OneToOne
- 一对多：@OneToMany
- 多对一：@ManyToOne
- 多对多：@ManyToMany
- @JoinColumn：外键列
- @JoinTable：关联表
- cascade：级联操作
- fetch：加载策略

### 5. 继承映射
- SINGLE_TABLE：单表继承
- JOINED：连接表继承
- TABLE_PER_CLASS：每个类一张表

## 实践任务
1. 实现基本实体映射
2. 使用不同的主键生成策略
3. 实现一对多和多对一关系
4. 实现多对多关系
5. 实现继承映射

## 参考资料
- Hibernate Entity Mapping
