// 异步编程示例

// 1. 回调函数
function fetchData(callback) {
    setTimeout(() => {
        callback('Data fetched successfully');
    }, 1000);
}

fetchData((result) => {
    console.log(result);
});

// 2. Promise
function fetchDataPromise() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Data fetched successfully with Promise');
        }, 1000);
    });
}

fetchDataPromise()
    .then(result => {
        console.log(result);
        return 'Processed data';
    })
    .then(processedData => {
        console.log(processedData);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// 3. Async/Await
async function fetchDataAsync() {
    try {
        const result = await fetchDataPromise();
        console.log(result);
        return 'Processed data with async/await';
    } catch (error) {
        console.error('Error:', error);
    }
}

fetchDataAsync().then(processedData => {
    console.log(processedData);
});

// 4. Promise.all
const promise1 = Promise.resolve(1);
const promise2 = Promise.resolve(2);
const promise3 = Promise.resolve(3);

Promise.all([promise1, promise2, promise3])
    .then(values => {
        console.log('Promise.all results:', values);
    });

// 5. Promise.race
const promiseA = new Promise(resolve => setTimeout(() => resolve('A'), 100));
const promiseB = new Promise(resolve => setTimeout(() => resolve('B'), 50));

Promise.race([promiseA, promiseB])
    .then(result => {
        console.log('Promise.race result:', result);
    });
