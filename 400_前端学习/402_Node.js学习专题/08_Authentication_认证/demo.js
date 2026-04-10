// Node.js 认证示例

const express = require('express');
const app = express();
const port = 3000;
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// 中间件
app.use(express.json());

// 模拟用户数据
const users = [];

// 1. 注册
app.post('/api/auth/register', async (req, res) => {
    try {
        const { username, password, email } = req.body;
        
        // 检查用户是否已存在
        const existingUser = users.find(user => user.email === email);
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }
        
        // 密码加密
        const hashedPassword = await bcrypt.hash(password, 10);
        
        // 创建新用户
        const newUser = {
            id: users.length + 1,
            username,
            email,
            password: hashedPassword
        };
        
        users.push(newUser);
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Internal server error' });
    }
});

// 2. 登录
app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // 查找用户
        const user = users.find(user => user.email === email);
        if (!user) {
            return res.status(401).json({ message: 'Invalid email or password' });
        }
        
        // 验证密码
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ message: 'Invalid email or password' });
        }
        
        // 生成JWT token
        const token = jwt.sign(
            { userId: user.id, email: user.email },
            'secret_key', // 实际应用中应该使用环境变量
            { expiresIn: '1h' }
        );
        
        res.json({ token, user: { id: user.id, username: user.username, email: user.email } });
    } catch (error) {
        res.status(500).json({ message: 'Internal server error' });
    }
});

// 3. 认证中间件
function authenticateToken(req, res, next) {
    const authHeader = req.headers.authorization;
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) {
        return res.status(401).json({ message: 'Access token required' });
    }
    
    jwt.verify(token, 'secret_key', (err, user) => {
        if (err) {
            return res.status(403).json({ message: 'Invalid or expired token' });
        }
        
        req.user = user;
        next();
    });
}

// 4. 受保护的路由
app.get('/api/protected', authenticateToken, (req, res) => {
    res.json({ message: 'Protected route accessed successfully', user: req.user });
});

// 5. 刷新token
app.post('/api/auth/refresh', authenticateToken, (req, res) => {
    try {
        const newToken = jwt.sign(
            { userId: req.user.userId, email: req.user.email },
            'secret_key',
            { expiresIn: '1h' }
        );
        
        res.json({ token: newToken });
    } catch (error) {
        res.status(500).json({ message: 'Internal server error' });
    }
});

// 6. 注销
app.post('/api/auth/logout', (req, res) => {
    // 在实际应用中，可能需要将token加入黑名单
    res.json({ message: 'Logged out successfully' });
});

// 7. 密码重置
app.post('/api/auth/forgot-password', (req, res) => {
    const { email } = req.body;
    
    // 查找用户
    const user = users.find(user => user.email === email);
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }
    
    // 生成重置令牌（实际应用中应该发送邮件）
    const resetToken = jwt.sign(
        { userId: user.id },
        'reset_secret_key',
        { expiresIn: '15m' }
    );
    
    console.log('Reset token:', resetToken);
    res.json({ message: 'Password reset link sent' });
});

// 8. 重置密码
app.post('/api/auth/reset-password', (req, res) => {
    const { token, newPassword } = req.body;
    
    jwt.verify(token, 'reset_secret_key', async (err, user) => {
        if (err) {
            return res.status(403).json({ message: 'Invalid or expired token' });
        }
        
        // 查找用户
        const foundUser = users.find(u => u.id === user.userId);
        if (!foundUser) {
            return res.status(404).json({ message: 'User not found' });
        }
        
        // 更新密码
        const hashedPassword = await bcrypt.hash(newPassword, 10);
        foundUser.password = hashedPassword;
        
        res.json({ message: 'Password reset successfully' });
    });
});

// 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
