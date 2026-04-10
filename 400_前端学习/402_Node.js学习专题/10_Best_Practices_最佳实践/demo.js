// Node.js 最佳实践示例

// 1. 环境变量管理
require('dotenv').config();

// 2. 模块化
// utils.js
const utils = {
    formatDate: function(date) {
        return new Date(date).toISOString();
    },
    validateEmail: function(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
};

module.exports = utils;

// 3. 错误处理
class AppError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.statusCode = statusCode;
        this.status = `${statusCode}`.startsWith('4') ? 'fail' : 'error';
        this.isOperational = true;
        
        Error.captureStackTrace(this, this.constructor);
    }
}

// 4. 中间件
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// 日志中间件
const morgan = require('morgan');
app.use(morgan('combined'));

// 安全中间件
const helmet = require('helmet');
app.use(helmet());

// 压缩中间件
const compression = require('compression');
app.use(compression());

// 解析请求体
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 5. 路由模块化
const userRoutes = require('./routes/users');
const postRoutes = require('./routes/posts');

app.use('/api/users', userRoutes);
app.use('/api/posts', postRoutes);

// 6. 数据库连接
const mongoose = require('mongoose');

async function connectDB() {
    try {
        await mongoose.connect(process.env.DATABASE_URL, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('Database connected successfully');
    } catch (error) {
        console.error('Database connection error:', error);
        process.exit(1);
    }
}

connectDB();

// 7. 密码加密
const bcrypt = require('bcrypt');

async function hashPassword(password) {
    return await bcrypt.hash(password, 10);
}

async function comparePassword(password, hashedPassword) {
    return await bcrypt.compare(password, hashedPassword);
}

// 8. JWT 认证
const jwt = require('jsonwebtoken');

function generateToken(user) {
    return jwt.sign(
        { id: user._id, email: user.email },
        process.env.SECRET_KEY,
        { expiresIn: '1h' }
    );
}

function verifyToken(token) {
    return jwt.verify(token, process.env.SECRET_KEY);
}

// 9. 认证中间件
function authenticate(req, res, next) {
    const token = req.headers.authorization?.split(' ')[1];
    
    if (!token) {
        return res.status(401).json({ message: 'Access token required' });
    }
    
    try {
        const decoded = verifyToken(token);
        req.user = decoded;
        next();
    } catch (error) {
        return res.status(403).json({ message: 'Invalid or expired token' });
    }
}

// 10. 错误处理中间件
app.use((err, req, res, next) => {
    err.statusCode = err.statusCode || 500;
    err.status = err.status || 'error';
    
    res.status(err.statusCode).json({
        status: err.status,
        message: err.message
    });
});

// 11. 404 处理
app.use((req, res) => {
    res.status(404).json({
        status: 'fail',
        message: 'Route not found'
    });
});

// 12. 生产环境优化
if (process.env.NODE_ENV === 'production') {
    // 生产环境特定配置
    app.use(express.static('public'));
}

// 13. 测试
// 使用 Jest 进行测试
/*
const request = require('supertest');
const app = require('../app');

describe('GET /api/users', () => {
    test('should return all users', async () => {
        const response = await request(app).get('/api/users');
        expect(response.statusCode).toBe(200);
        expect(Array.isArray(response.body)).toBe(true);
    });
});
*/

// 14. 代码风格
// 使用 ESLint 和 Prettier
/*
// .eslintrc.json
{
  "extends": ["airbnb-base", "prettier"],
  "plugins": ["prettier"],
  "rules": {
    "prettier/prettier": "error"
  }
}

// .prettierrc
{
  "singleQuote": true,
  "trailingComma": "es5",
  "tabWidth": 4,
  "semi": true
}
*/

// 15. 性能优化
// 1. 使用连接池
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// 2. 缓存
const NodeCache = require('node-cache');
const cache = new NodeCache({ stdTTL: 60 });

app.get('/api/data', (req, res) => {
    const cacheKey = 'data';
    const cachedData = cache.get(cacheKey);
    
    if (cachedData) {
        return res.json(cachedData);
    }
    
    // 从数据库获取数据
    const data = { message: 'Hello World' };
    cache.set(cacheKey, data);
    res.json(data);
});

// 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
