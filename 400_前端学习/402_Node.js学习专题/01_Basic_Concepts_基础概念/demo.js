// Node.js 基础概念示例

// 1. 模块系统
// 导出模块
module.exports = {
    greet: function(name) {
        return `Hello, ${name}!`;
    },
    add: function(a, b) {
        return a + b;
    }
};

// 导入模块
const utils = require('./utils');
console.log(utils.greet('Node.js'));
console.log(utils.add(5, 3));

// 2. 文件系统操作
const fs = require('fs');

// 同步读取文件
const data = fs.readFileSync('example.txt', 'utf8');
console.log(data);

// 异步读取文件
fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});

// 写入文件
fs.writeFile('output.txt', 'Hello Node.js!', (err) => {
    if (err) throw err;
    console.log('File written successfully');
});

// 3. HTTP 服务器
const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});

// 4. 事件处理
const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();

myEmitter.on('event', () => {
    console.log('An event occurred!');
});

myEmitter.emit('event');

// 5. 路径处理
const path = require('path');

const filePath = '/home/user/file.txt';
console.log(path.dirname(filePath));
console.log(path.basename(filePath));
console.log(path.extname(filePath));

// 6. 环境变量
console.log('Node.js version:', process.version);
console.log('Platform:', process.platform);
console.log('Process ID:', process.pid);
console.log('Environment variables:', process.env);

// 7. 错误处理
try {
    const result = 10 / 0;
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
}

// 8. 包管理
// package.json 示例
/*
{
  "name": "nodejs-demo",
  "version": "1.0.0",
  "description": "Node.js demo",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": ["nodejs", "demo"],
  "author": "Your Name",
  "license": "MIT"
}
*/
