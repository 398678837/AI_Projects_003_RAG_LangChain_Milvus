// Next.js API 路由示例

// 1. 基本 API 路由
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' });
}

// 2. 带参数的 API 路由
// pages/api/posts/[id].js
export default function handler(req, res) {
  const { id } = req.query;
  res.status(200).json({ id, name: `Post ${id}` });
}

// 3. 动态 API 路由
// pages/api/[...slug].js
export default function handler(req, res) {
  const { slug } = req.query;
  res.status(200).json({ slug });
}

// 4. POST 请求
// pages/api/submit.js
export default function handler(req, res) {
  if (req.method === 'POST') {
    const data = req.body;
    res.status(200).json({ message: 'Data received', data });
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}

// 5. 数据库操作
// pages/api/users.js
import { connectToDatabase } from '../../lib/mongodb';

export default async function handler(req, res) {
  const { method } = req;
  
  const { db } = await connectToDatabase();
  
  switch (method) {
    case 'GET':
      const users = await db.collection('users').find({}).toArray();
      res.status(200).json(users);
      break;
    case 'POST':
      const newUser = await db.collection('users').insertOne(req.body);
      res.status(201).json(newUser);
      break;
    default:
      res.setHeader('Allow', ['GET', 'POST']);
      res.status(405).end(`Method ${method} Not Allowed`);
  }
}

// 6. 认证 API
// pages/api/auth/login.js
export default function handler(req, res) {
  if (req.method === 'POST') {
    const { email, password } = req.body;
    
    // 模拟认证
    if (email === 'user@example.com' && password === 'password') {
      res.status(200).json({ token: 'your-token', user: { email } });
    } else {
      res.status(401).json({ message: 'Invalid credentials' });
    }
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}

// 7. 错误处理
// pages/api/error.js
export default function handler(req, res) {
  try {
    // 模拟错误
    throw new Error('Something went wrong');
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
}

// 8. 中间件
// pages/api/protected.js
export default function handler(req, res) {
  // 模拟认证中间件
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ message: 'Unauthorized' });
  }
  
  // 验证 token
  if (token !== 'valid-token') {
    return res.status(403).json({ message: 'Forbidden' });
  }
  
  res.status(200).json({ message: 'Protected resource' });
}

// 9. 文件上传
// pages/api/upload.js
import formidable from 'formidable';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default function handler(req, res) {
  if (req.method === 'POST') {
    const form = new formidable.IncomingForm();
    
    form.parse(req, (err, fields, files) => {
      if (err) {
        return res.status(500).json({ message: 'Error parsing form' });
      }
      
      res.status(200).json({ fields, files });
    });
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}

// 10. 速率限制
// pages/api/rate-limited.js
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 10, // limit each IP to 10 requests per windowMs
});

export default function handler(req, res) {
  limiter(req, res, () => {
    res.status(200).json({ message: 'Rate limited endpoint' });
  });
}
