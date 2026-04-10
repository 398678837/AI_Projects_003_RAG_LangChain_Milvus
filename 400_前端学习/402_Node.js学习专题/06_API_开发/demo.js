// Node.js API 开发示例

const express = require('express');
const app = express();
const port = 3000;

// 中间件
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 模拟数据
let users = [
    { id: 1, name: 'John', age: 30, email: 'john@example.com' },
    { id: 2, name: 'Jane', age: 25, email: 'jane@example.com' },
    { id: 3, name: 'Bob', age: 35, email: 'bob@example.com' }
];

// 1. GET 请求 - 获取所有用户
app.get('/api/users', (req, res) => {
    res.json(users);
});

// 2. GET 请求 - 获取单个用户
app.get('/api/users/:id', (req, res) => {
    const { id } = req.params;
    const user = users.find(user => user.id === parseInt(id));
    
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }
    
    res.json(user);
});

// 3. POST 请求 - 创建新用户
app.post('/api/users', (req, res) => {
    const { name, age, email } = req.body;
    
    if (!name || !age || !email) {
        return res.status(400).json({ message: 'Name, age, and email are required' });
    }
    
    const newUser = {
        id: users.length + 1,
        name,
        age,
        email
    };
    
    users.push(newUser);
    res.status(201).json(newUser);
});

// 4. PUT 请求 - 更新用户
app.put('/api/users/:id', (req, res) => {
    const { id } = req.params;
    const { name, age, email } = req.body;
    
    const user = users.find(user => user.id === parseInt(id));
    
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }
    
    if (name) user.name = name;
    if (age) user.age = age;
    if (email) user.email = email;
    
    res.json(user);
});

// 5. DELETE 请求 - 删除用户
app.delete('/api/users/:id', (req, res) => {
    const { id } = req.params;
    const userIndex = users.findIndex(user => user.id === parseInt(id));
    
    if (userIndex === -1) {
        return res.status(404).json({ message: 'User not found' });
    }
    
    users.splice(userIndex, 1);
    res.json({ message: 'User deleted successfully' });
});

// 6. 分页查询
app.get('/api/users/paginated', (req, res) => {
    const { page = 1, limit = 2 } = req.query;
    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + parseInt(limit);
    
    const paginatedUsers = users.slice(startIndex, endIndex);
    
    res.json({
        total: users.length,
        page: parseInt(page),
        limit: parseInt(limit),
        data: paginatedUsers
    });
});

// 7. 搜索功能
app.get('/api/users/search', (req, res) => {
    const { q } = req.query;
    
    if (!q) {
        return res.status(400).json({ message: 'Search query is required' });
    }
    
    const searchResults = users.filter(user => 
        user.name.toLowerCase().includes(q.toLowerCase()) ||
        user.email.toLowerCase().includes(q.toLowerCase())
    );
    
    res.json(searchResults);
});

// 8. 错误处理中间件
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Internal server error' });
});

// 9. 404 处理
app.use((req, res) => {
    res.status(404).json({ message: 'API endpoint not found' });
});

// 10. 启动服务器
app.listen(port, () => {
    console.log(`API server running at http://localhost:${port}/`);
});
