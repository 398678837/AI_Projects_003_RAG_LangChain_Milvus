# 08_CoreData_CoreData

## 学习目标
- 理解CoreData的基本概念
- 学会创建CoreData模型
- 掌握数据的增删改查
- 理解NSManagedObjectContext
- 掌握CoreData与SwiftUI的集成

## 关键要点
### 1. CoreData概述
- Apple的对象图管理和持久化框架
- ORM（对象关系映射）
- 支持SQLite、XML、In-Memory存储
- 数据模型编辑器

### 2. 核心组件
- NSManagedObjectContext：管理对象上下文
- NSManagedObjectModel：数据模型
- NSPersistentStoreCoordinator：持久化存储协调器
- NSPersistentContainer：iOS 10+简化容器

### 3. 数据模型
- Entity：实体
- Attribute：属性
- Relationship：关系
- Fetch Request：抓取请求

### 4. 基本操作
- Create：创建对象
- Read：查询（NSFetchRequest）
- Update：修改对象
- Delete：删除对象
- Save：保存上下文

### 5. 高级功能
- 谓词（NSPredicate）
- 排序（NSSortDescriptor）
-  fetchedResultsController
- 数据迁移
- 轻量级迁移

## 实践任务
1. 创建CoreData数据模型
2. 实现增删改查
3. 使用NSFetchedResultsController
4. 在SwiftUI中使用CoreData

## 参考资料
- Core Data Programming Guide
