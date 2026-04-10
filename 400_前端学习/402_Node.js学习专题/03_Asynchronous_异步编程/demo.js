// Node.js 异步编程示例

// 1. 回调函数
const fs = require('fs');

console.log('=== 回调函数 ===');
fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('读取文件错误:', err);
        return;
    }
    console.log('文件内容:', data);
});

// 2. Promise
function readFilePromise(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(data);
        });
    });
}

console.log('\n=== Promise ===');
readFilePromise('example.txt')
    .then(data => {
        console.log('文件内容:', data);
        return 'Processed data';
    })
    .then(processedData => {
        console.log('处理后的数据:', processedData);
    })
    .catch(err => {
        console.error('错误:', err);
    });

// 3. Async/Await
async function readFileAsync() {
    try {
        const data = await readFilePromise('example.txt');
        console.log('\n=== Async/Await ===');
        console.log('文件内容:', data);
        return 'Processed data';
    } catch (err) {
        console.error('错误:', err);
        throw err;
    }
}

readFileAsync()
    .then(processedData => {
        console.log('处理后的数据:', processedData);
    })
    .catch(err => {
        console.error('错误:', err);
    });

// 4. 事件循环
console.log('\n=== 事件循环 ===');
console.log('开始');

setTimeout(() => {
    console.log('setTimeout 回调');
}, 0);

fs.readFile('example.txt', 'utf8', (err, data) => {
    console.log('fs.readFile 回调');
});

process.nextTick(() => {
    console.log('process.nextTick 回调');
});

console.log('结束');

// 5. 并行异步操作
const promises = [
    readFilePromise('example.txt'),
    readFilePromise('output.txt')
];

console.log('\n=== 并行异步操作 ===');
Promise.all(promises)
    .then(results => {
        console.log('所有文件内容:', results);
    })
    .catch(err => {
        console.error('错误:', err);
    });

// 6. 串行异步操作
async function serialRead() {
    console.log('\n=== 串行异步操作 ===');
    try {
        const data1 = await readFilePromise('example.txt');
        console.log('第一个文件内容:', data1);
        const data2 = await readFilePromise('output.txt');
        console.log('第二个文件内容:', data2);
        return [data1, data2];
    } catch (err) {
        console.error('错误:', err);
        throw err;
    }
}

serialRead();

// 7. 错误处理
async function errorHandling() {
    console.log('\n=== 错误处理 ===');
    try {
        const data = await readFilePromise('non-existent.txt');
        console.log('文件内容:', data);
    } catch (err) {
        console.error('捕获到错误:', err.message);
    } finally {
        console.log('无论成功失败都会执行');
    }
}

errorHandling();

// 8. Promise 链式调用
function step1() {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log('步骤 1');
            resolve(1);
        }, 1000);
    });
}

function step2(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log('步骤 2');
            resolve(value + 1);
        }, 1000);
    });
}

function step3(value) {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log('步骤 3');
            resolve(value + 1);
        }, 1000);
    });
}

console.log('\n=== Promise 链式调用 ===');
step1()
    .then(step2)
    .then(step3)
    .then(result => {
        console.log('最终结果:', result);
    });
