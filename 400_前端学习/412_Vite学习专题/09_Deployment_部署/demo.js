// Vite 部署示例代码

// 1. 构建命令
const buildCommands = `
# 构建
npm run build

# 预览构建结果
npm run preview

# 使用特定模式构建
npm run build -- --mode staging

# 指定输出目录
# 在 vite.config.js 中配置
`;

console.log('=== 构建命令 ===');
console.log(buildCommands);

// 2. 部署到 GitHub Pages
const githubPages = `
// vite.config.js - 配置 base
import { defineConfig } from 'vite'

export default defineConfig({
  base: '/repo-name/'  // 你的仓库名
})

// package.json - 添加 deploy 脚本
{
  "scripts": {
    "build": "vite build",
    "deploy": "gh-pages -d dist"
  }
}

// 安装 gh-pages
npm install -D gh-pages

// 部署
npm run build
npm run deploy

// 或者使用 GitHub Actions
// .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm ci
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: \${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
`;

console.log('\n=== 部署到 GitHub Pages ===');
console.log(githubPages);

// 3. 部署到 Vercel
const vercelDeploy = `
// 1. 安装 Vercel CLI
npm i -g vercel

// 2. 部署
vercel

// 3. 生产环境部署
vercel --prod

// 或者直接推送到 GitHub，自动部署
// vercel.json (可选配置)
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": "vite"
}

// .env 配置在 Vercel 后台设置
`;

console.log('\n=== 部署到 Vercel ===');
console.log(vercelDeploy);

// 4. 部署到 Netlify
const netlifyDeploy = `
// 1. 安装 Netlify CLI
npm i -g netlify-cli

// 2. 部署
netlify init
netlify deploy

// 3. 生产环境部署
netlify deploy --prod

// netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

// 或者直接推送到 GitHub，自动部署
`;

console.log('\n=== 部署到 Netlify ===');
console.log(netlifyDeploy);

// 5. Nginx 部署配置
const nginxConfig = `
# nginx.conf
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/dist;
    index index.html;

    # Gzip 压缩
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript 
               application/x-javascript application/xml+rss 
               application/json application/javascript;

    # 静态资源缓存
    location ~* \\.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # SPA 路由
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API 代理
    location /api/ {
        proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# 部署步骤
# 1. 上传 dist 目录到服务器
# 2. 配置 nginx
# 3. 重启 nginx
sudo systemctl restart nginx
`;

console.log('\n=== Nginx 部署配置 ===');
console.log(nginxConfig);

// 6. 部署到 Docker
const dockerDeploy = `
# Dockerfile
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# .dockerignore
node_modules
dist
.git
.env

# 构建镜像
docker build -t my-vite-app .

# 运行容器
docker run -p 8080:80 my-vite-app

# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "8080:80"
`;

console.log('\n=== 部署到 Docker ===');
console.log(dockerDeploy);

// 7. GitHub Actions CI/CD
const githubActions = `
# .github/workflows/deploy.yml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Build
        run: npm run build
        env:
          VITE_API_URL: \${{ secrets.VITE_API_URL }}
      
      - name: Deploy to Server
        uses: easingthemes/ssh-deploy@v2
        with:
          SSH_PRIVATE_KEY: \${{ secrets.SSH_PRIVATE_KEY }}
          REMOTE_HOST: \${{ secrets.REMOTE_HOST }}
          REMOTE_USER: \${{ secrets.REMOTE_USER }}
          TARGET: /var/www/my-app
          SOURCE: dist/
`;

console.log('\n=== GitHub Actions CI/CD ===');
console.log(githubActions);

// 8. 不同部署平台的 base 配置
const baseConfig = `
// GitHub Pages
export default defineConfig({
  base: '/repo-name/'
})

// Vercel / Netlify / 自己的域名
export default defineConfig({
  base: '/'
})

// 子路径部署
export default defineConfig({
  base: '/sub-path/'
})
`;

console.log('\n=== 不同部署平台的 base 配置 ===');
console.log(baseConfig);

// 9. 部署检查清单
const deployChecklist = [
  '✅ 运行 npm run build 成功',
  '✅ 运行 npm run preview 预览正常',
  '✅ 配置正确的 base 路径',
  '✅ 配置环境变量',
  '✅ SPA 路由重定向配置',
  '✅ 静态资源缓存配置',
  '✅ Gzip 压缩配置',
  '✅ HTTPS 配置',
  '✅ API 代理配置'
];

console.log('\n=== 部署检查清单 ===');
deployChecklist.forEach(item => console.log(item));
