# 05_Data_Storage_数据存储

## 学习目标
- 掌握UserDefaults的使用
- 学会文件存储
- 理解Property List
- 掌握Keychain的使用
- 理解SQLite和Core Data的区别

## 关键要点
### 1. UserDefaults
- 存储小量键值对数据
- 适用于用户偏好设置
- 数据类型：Int、Double、Bool、String、Array、Dictionary、Data
- 自动持久化
- 注意：不适合存储敏感数据

### 2. 文件存储
- Sandbox目录结构：
  - Documents：用户生成的文件，iCloud备份
  - Library/Caches：缓存文件，可删除
  - Library/Preferences：UserDefaults
  - tmp：临时文件，随时删除
- FileManager：管理文件系统
- 读写文件：String、Data、Array、Dictionary

### 3. Property List
- plist文件，XML格式
- 支持类型：Array、Dictionary、String、Number、Date、Data
- Swift类型与plist互相转换

### 4. Keychain
- 存储敏感信息（密码、令牌）
- 系统级加密存储
- API较复杂，通常使用第三方库
- KeychainAccess、SAMKeychain等

### 5. 数据存储对比
- UserDefaults：小量配置
- 文件：文档、缓存
- Keychain：敏感数据
- SQLite：大量结构化数据
- Core Data：对象关系映射

## 实践任务
1. 使用UserDefaults保存用户设置
2. 读写文件到Documents目录
3. 使用Property List存储数据
4. 使用Keychain保存密码

## 参考资料
- File System Programming Guide
