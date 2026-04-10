// Node.js 中间件示例

const express = require('express');
const app = express();
const port = 3000;

// 1. 应用级中间件
// 日志中间件
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
    next();
});

// 认证中间件
function authenticate(req, res, next) {
    const token = req.headers.authorization;
    
    if (!token) {
        return res.status(401).json({ message: 'Unauthorized' });
    }
    
    // 这里应该验证token的有效性
    // 简化示例，假设token为'valid-token'
    if (token !== 'valid-token') {
        return res.status(401).json({ message: 'Invalid token' });
    }
    
    next();
}

// 2. 路由级中间件
const userRoutes = express.Router();

// 应用认证中间件到所有用户路由
userRoutes.use(authenticate);

userRoutes.get('/', (req, res) => {
    res.json({ message: 'All users' });
});

userRoutes.post('/', (req, res) => {
    res.json({ message: 'Create user' });
});

app.use('/api/users', userRoutes);

// 3. 错误处理中间件
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Internal server error' });
});

// 4. 内置中间件
app.use(express.json()); // 解析JSON请求体
app.use(express.urlencoded({ extended: true })); // 解析URL编码的请求体
app.use(express.static('public')); // 静态文件服务

// 5. 第三方中间件
// 首先安装第三方中间件，例如 helmet
// npm install helmet

// const helmet = require('helmet');
// app.use(helmet()); // 安全中间件

// 6. 中间件链
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

// 7. 条件中间件
function conditionalMiddleware(req, res, next) {
    if (req.query.apiKey) {
        console.log('API Key provided:', req.query.apiKey);
        // 验证API Key
        next();
    } else {
        next();
    }
}

app.get('/conditional', conditionalMiddleware, (req, res) => {
    res.send('Conditional middleware executed');
});

// 8. 错误处理中间件
app.get('/error', (req, res, next) => {
    const error = new Error('Something went wrong');
    next(error);
});

// 9. 404 处理中间件
app.use((req, res) => {
    res.status(404).json({ message: 'Page not found' });
});

// 10. 中间件顺序
// 中间件的顺序很重要，先定义的中间件先执行

// 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
