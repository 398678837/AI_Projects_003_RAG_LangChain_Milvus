// Node.js 数据库操作示例

// 1. MongoDB 示例
// 首先安装 mongoose
// npm install mongoose

const mongoose = require('mongoose');

// 连接 MongoDB
mongoose.connect('mongodb://localhost:27017/testdb', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// 定义模式
const userSchema = new mongoose.Schema({
    name: String,
    age: Number,
    email: String
});

// 创建模型
const User = mongoose.model('User', userSchema);

// 增删改查操作
async function mongoOperations() {
    console.log('=== MongoDB 操作 ===');
    
    // 创建用户
    const user = new User({ name: 'John', age: 30, email: 'john@example.com' });
    await user.save();
    console.log('用户创建成功:', user);
    
    // 查询用户
    const foundUser = await User.findOne({ name: 'John' });
    console.log('查询到的用户:', foundUser);
    
    // 更新用户
    foundUser.age = 31;
    await foundUser.save();
    console.log('用户更新成功:', foundUser);
    
    // 删除用户
    await User.deleteOne({ name: 'John' });
    console.log('用户删除成功');
}

// mongoOperations();

// 2. MySQL 示例
// 首先安装 mysql2
// npm install mysql2

const mysql = require('mysql2/promise');

async function mysqlOperations() {
    console.log('\n=== MySQL 操作 ===');
    
    // 创建连接
    const connection = await mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'password',
        database: 'testdb'
    });
    
    // 创建表
    await connection.execute(`
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
    `);
    console.log('表创建成功');
    
    // 插入数据
    await connection.execute(
        'INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
        ['John', 30, 'john@example.com']
    );
    console.log('数据插入成功');
    
    // 查询数据
    const [rows] = await connection.execute('SELECT * FROM users');
    console.log('查询到的数据:', rows);
    
    // 更新数据
    await connection.execute(
        'UPDATE users SET age = ? WHERE name = ?',
        [31, 'John']
    );
    console.log('数据更新成功');
    
    // 删除数据
    await connection.execute('DELETE FROM users WHERE name = ?', ['John']);
    console.log('数据删除成功');
    
    // 关闭连接
    await connection.end();
}

// mysqlOperations();

// 3. SQLite 示例
// 首先安装 sqlite3
// npm install sqlite3

const sqlite3 = require('sqlite3').verbose();

function sqliteOperations() {
    console.log('\n=== SQLite 操作 ===');
    
    // 创建数据库连接
    const db = new sqlite3.Database('./test.db');
    
    // 创建表
    db.run(`
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    `, (err) => {
        if (err) {
            console.error('创建表错误:', err);
            return;
        }
        console.log('表创建成功');
        
        // 插入数据
        db.run(
            'INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
            ['John', 30, 'john@example.com'],
            function(err) {
                if (err) {
                    console.error('插入数据错误:', err);
                    return;
                }
                console.log('数据插入成功，ID:', this.lastID);
                
                // 查询数据
                db.all('SELECT * FROM users', (err, rows) => {
                    if (err) {
                        console.error('查询数据错误:', err);
                        return;
                    }
                    console.log('查询到的数据:', rows);
                    
                    // 更新数据
                    db.run(
                        'UPDATE users SET age = ? WHERE name = ?',
                        [31, 'John'],
                        (err) => {
                            if (err) {
                                console.error('更新数据错误:', err);
                                return;
                            }
                            console.log('数据更新成功');
                            
                            // 删除数据
                            db.run('DELETE FROM users WHERE name = ?', ['John'], (err) => {
                                if (err) {
                                    console.error('删除数据错误:', err);
                                    return;
                                }
                                console.log('数据删除成功');
                                
                                // 关闭连接
                                db.close();
                            });
                        }
                    );
                });
            }
        );
    });
}

// sqliteOperations();

// 4. Redis 示例
// 首先安装 redis
// npm install redis

const redis = require('redis');

async function redisOperations() {
    console.log('\n=== Redis 操作 ===');
    
    // 创建客户端
    const client = redis.createClient();
    
    await client.connect();
    
    // 设置键值对
    await client.set('name', 'John');
    await client.set('age', '30');
    console.log('键值对设置成功');
    
    // 获取值
    const name = await client.get('name');
    const age = await client.get('age');
    console.log('获取到的值:', { name, age });
    
    // 设置过期时间
    await client.set('temp', 'value', { EX: 10 });
    console.log('带过期时间的键值对设置成功');
    
    // 哈希操作
    await client.hSet('user:1', {
        name: 'John',
        age: '30',
        email: 'john@example.com'
    });
    console.log('哈希设置成功');
    
    // 获取哈希值
    const user = await client.hGetAll('user:1');
    console.log('获取到的哈希值:', user);
    
    // 列表操作
    await client.lPush('tasks', 'task1', 'task2', 'task3');
    console.log('列表设置成功');
    
    // 获取列表值
    const tasks = await client.lRange('tasks', 0, -1);
    console.log('获取到的列表值:', tasks);
    
    // 关闭连接
    await client.quit();
}

// redisOperations();
