// Node.js 核心模块示例

// 1. fs 模块 - 文件系统
const fs = require('fs');

// 同步读取文件
console.log('=== fs 模块 ===');
try {
    const data = fs.readFileSync('example.txt', 'utf8');
    console.log('同步读取文件:', data);
} catch (err) {
    console.error('读取文件错误:', err);
}

// 异步读取文件
fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('异步读取文件错误:', err);
        return;
    }
    console.log('异步读取文件:', data);
});

// 写入文件
fs.writeFile('output.txt', 'Hello Node.js!', (err) => {
    if (err) {
        console.error('写入文件错误:', err);
        return;
    }
    console.log('文件写入成功');
});

// 创建目录
if (!fs.existsSync('test')) {
    fs.mkdirSync('test');
    console.log('目录创建成功');
}

// 2. http 模块 - HTTP 服务器
const http = require('http');

console.log('\n=== http 模块 ===');
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});

// 3. path 模块 - 路径处理
const path = require('path');

console.log('\n=== path 模块 ===');
const filePath = '/home/user/file.txt';
console.log('目录名:', path.dirname(filePath));
console.log('文件名:', path.basename(filePath));
console.log('扩展名:', path.extname(filePath));
console.log('绝对路径:', path.resolve('file.txt'));
console.log('路径拼接:', path.join(__dirname, 'test', 'file.txt'));

// 4. url 模块 - URL 解析
const url = require('url');

console.log('\n=== url 模块 ===');
const urlString = 'https://www.example.com:8080/path?query=value#hash';
const parsedUrl = url.parse(urlString, true);
console.log('解析后的URL:', parsedUrl);
console.log('协议:', parsedUrl.protocol);
console.log('主机:', parsedUrl.host);
console.log('路径:', parsedUrl.pathname);
console.log('查询参数:', parsedUrl.query);

// 5. querystring 模块 - 查询字符串处理
const querystring = require('querystring');

console.log('\n=== querystring 模块 ===');
const query = 'name=John&age=30&city=New%20York';
const parsedQuery = querystring.parse(query);
console.log('解析后的查询字符串:', parsedQuery);

const obj = { name: 'John', age: 30, city: 'New York' };
const stringifiedQuery = querystring.stringify(obj);
console.log('字符串化的查询对象:', stringifiedQuery);

// 6. events 模块 - 事件处理
const EventEmitter = require('events');

console.log('\n=== events 模块 ===');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();

// 监听事件
myEmitter.on('greet', (name) => {
    console.log(`Hello, ${name}!`);
});

// 触发事件
myEmitter.emit('greet', 'Node.js');

// 7. os 模块 - 操作系统信息
const os = require('os');

console.log('\n=== os 模块 ===');
console.log('操作系统类型:', os.type());
console.log('操作系统平台:', os.platform());
console.log('操作系统架构:', os.arch());
console.log('操作系统版本:', os.release());
console.log('CPU 信息:', os.cpus());
console.log('内存总量:', os.totalmem());
console.log('可用内存:', os.freemem());

// 8. process 模块 - 进程信息
const process = require('process');

console.log('\n=== process 模块 ===');
console.log('Node.js 版本:', process.version);
console.log('进程 ID:', process.pid);
console.log('当前工作目录:', process.cwd());
console.log('环境变量:', process.env.NODE_ENV);

// 9. crypto 模块 - 加密
const crypto = require('crypto');

console.log('\n=== crypto 模块 ===');
const hash = crypto.createHash('sha256');
hash.update('Hello Node.js');
console.log('SHA256 哈希:', hash.digest('hex'));

// 10. zlib 模块 - 压缩
const zlib = require('zlib');

console.log('\n=== zlib 模块 ===');
const input = Buffer.from('Hello Node.js!');
zlib.gzip(input, (err, compressed) => {
    if (err) {
        console.error('压缩错误:', err);
        return;
    }
    console.log('压缩后:', compressed);
    
    zlib.gunzip(compressed, (err, decompressed) => {
        if (err) {
            console.error('解压错误:', err);
            return;
        }
        console.log('解压后:', decompressed.toString());
    });
});
