// Express 框架示例

// 1. 基本设置
const express = require('express');
const app = express();
const port = 3000;

// 2. 中间件
app.use(express.json()); // 解析JSON请求体
app.use(express.urlencoded({ extended: true })); // 解析URL编码的请求体

// 自定义中间件
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
    next();
});

// 3. 路由
app.get('/', (req, res) => {
    res.send('Hello Express!');
});

// 带参数的路由
app.get('/users/:id', (req, res) => {
    const { id } = req.params;
    res.send(`User ID: ${id}`);
});

// 带查询参数的路由
app.get('/search', (req, res) => {
    const { q } = req.query;
    res.send(`Search query: ${q}`);
});

// POST 请求
app.post('/users', (req, res) => {
    const user = req.body;
    res.status(201).json({ message: 'User created', user });
});

// PUT 请求
app.put('/users/:id', (req, res) => {
    const { id } = req.params;
    const user = req.body;
    res.json({ message: 'User updated', id, user });
});

// DELETE 请求
app.delete('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ message: 'User deleted', id });
});

// 4. 静态文件服务
app.use(express.static('public'));

// 5. 错误处理中间件
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// 6. 404 处理
app.use((req, res) => {
    res.status(404).send('Page not found');
});

// 7. 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});

// 8. 路由模块化
const userRoutes = express.Router();

userRoutes.get('/', (req, res) => {
    res.send('All users');
});

userRoutes.post('/', (req, res) => {
    res.send('Create user');
});

app.use('/api/users', userRoutes);

// 9. 模板引擎
// 首先安装模板引擎，例如 EJS
// npm install ejs

// app.set('view engine', 'ejs');
// app.set('views', './views');

// app.get('/template', (req, res) => {
//     res.render('index', { title: 'Express', message: 'Hello from EJS' });
// });

// 10. 中间件链
app.get('/chain', 
    (req, res, next) => {
        req.data = 'Middleware 1';
        next();
    },
    (req, res, next) => {
        req.data += ' -> Middleware 2';
        next();
    },
    (req, res) => {
        res.send(req.data);
    }
);
