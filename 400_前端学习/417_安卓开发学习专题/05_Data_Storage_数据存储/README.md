# 05_Data_Storage_数据存储

## 学习目标
- 掌握SharedPreferences的使用
- 学会文件存储（内部/外部）
- 理解SQLite数据库的使用
- 掌握Room数据库框架
- 了解其他存储方式

## 关键要点
### 1. SharedPreferences
- 存储键值对数据
- 适用于配置信息、用户偏好
- 数据格式：XML
- 获取方式：getSharedPreferences()、getPreferences()
- 提交方式：commit()（同步）、apply()（异步）

### 2. 文件存储
- 内部存储：
  - 应用私有，卸载时删除
  - 路径：/data/data/&lt;package&gt;/files/
  - API：openFileInput()、openFileOutput()
- 外部存储：
  - 公共存储，需要权限
  - 路径：/sdcard/
  - API：Environment.getExternalStorageDirectory()
- 资源文件：
  - assets：使用AssetManager
  - res/raw：使用Resources.openRawResource()

### 3. SQLite数据库
- 轻量级关系型数据库
- API：SQLiteOpenHelper、SQLiteDatabase
- 操作：insert()、delete()、update()、query()、execSQL()
- 事务：beginTransaction()、setTransactionSuccessful()、endTransaction()

### 4. Room数据库
- Google推荐的ORM框架
- 基于SQLite的封装
- 三个主要组件：
  - Entity：实体类，对应数据库表
  - DAO：数据访问对象，定义操作方法
  - Database：数据库持有者，创建数据库实例
- 支持LiveData、RxJava、Kotlin协程

### 5. 其他存储方式
- ContentProvider：应用间数据共享
- 网络存储：云存储、服务器数据库

## 实践任务
1. 使用SharedPreferences保存用户设置
2. 使用内部存储保存文件
3. 使用SQLite创建数据库并增删改查
4. 使用Room实现数据持久化

## 参考资料
- Android官方文档：Data and file storage overview
- Room文档：https://developer.android.com/training/data-storage/room
