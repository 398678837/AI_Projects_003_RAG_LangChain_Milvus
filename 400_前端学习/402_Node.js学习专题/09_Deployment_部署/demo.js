// Node.js 部署示例

// 1. 环境变量配置
// 创建 .env 文件
/*
PORT=3000
NODE_ENV=production
DATABASE_URL=mongodb://localhost:27017/production
SECRET_KEY=your_secret_key
*/

// 使用 dotenv 加载环境变量
// require('dotenv').config();

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// 2. 生产环境中间件
if (process.env.NODE_ENV === 'production') {
    // 日志中间件
    const morgan = require('morgan');
    app.use(morgan('combined'));
    
    // 安全中间件
    const helmet = require('helmet');
    app.use(helmet());
    
    // 压缩中间件
    const compression = require('compression');
    app.use(compression());
}

// 3. 静态文件服务
app.use(express.static('public'));

// 4. 路由
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// 5. 错误处理
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
    console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});

// 8. Docker 配置
// 创建 Dockerfile
/*
FROM node:14-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
*/

// 9. Docker Compose 配置
// 创建 docker-compose.yml
/*
version: '3'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mongodb://mongo:27017/production
    depends_on:
      - mongo
  mongo:
    image: mongo:4.4
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
volumes:
  mongo-data:
*/

// 10. 部署脚本
// 创建 deploy.sh
/*
#!/bin/bash

# 拉取最新代码
git pull

# 安装依赖
npm install --production

# 重启服务
pm run restart
*/

// 11. PM2 配置
// 创建 ecosystem.config.js
/*
module.exports = {
  apps : [
    {
      name: 'app',
      script: 'app.js',
      instances: 'max',
      exec_mode: 'cluster',
      env:
        NODE_ENV: 'production'
    }
  ]
};
*/

// 12. CI/CD 配置
// 创建 .github/workflows/deploy.yml
/*
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Use Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - name: Install dependencies
        run: npm install --production
      - name: Build
        run: npm run build
      - name: Deploy
        run: |
          ssh user@server 'bash -s' < deploy.sh
*/
