// Promise 和 Async/Await 示例

// 1. Promise 基础
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = true;
            if (success) {
                resolve('Data fetched successfully');
            } else {
                reject('Error fetching data');
            }
        }, 1000);
    });
}

fetchData()
    .then(result => {
        console.log(result);
        return 'Processed data';
    })
    .then(processedData => {
        console.log(processedData);
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        console.log('Promise completed');
    });

// 2. Promise 链式调用
function getUser(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({ id: id, name: 'Alice' });
        }, 500);
    });
}

function getPosts(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve([{ id: 1, title: 'Post 1' }, { id: 2, title: 'Post 2' }]);
        }, 500);
    });
}

function getComments(postId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve([{ id: 1, content: 'Comment 1' }, { id: 2, content: 'Comment 2' }]);
        }, 500);
    });
}

// 链式调用
getUser(1)
    .then(user => {
        console.log('User:', user);
        return getPosts(user.id);
    })
    .then(posts => {
        console.log('Posts:', posts);
        return getComments(posts[0].id);
    })
    .then(comments => {
        console.log('Comments:', comments);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// 3. Promise.all
const promise1 = Promise.resolve(1);
const promise2 = Promise.resolve(2);
const promise3 = Promise.resolve(3);

Promise.all([promise1, promise2, promise3])
    .then(values => {
        console.log('Promise.all results:', values);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// 4. Promise.race
const promiseA = new Promise(resolve => setTimeout(() => resolve('A'), 100));
const promiseB = new Promise(resolve => setTimeout(() => resolve('B'), 50));

Promise.race([promiseA, promiseB])
    .then(result => {
        console.log('Promise.race result:', result);
    });

// 5. Promise.allSettled
const promiseX = Promise.resolve('Success');
const promiseY = Promise.reject('Error');

Promise.allSettled([promiseX, promiseY])
    .then(results => {
        console.log('Promise.allSettled results:', results);
    });

// 6. Async/Await 基础
async function fetchDataAsync() {
    try {
        const result = await fetchData();
        console.log('Async/Await result:', result);
        return 'Processed data';
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

fetchDataAsync()
    .then(processedData => {
        console.log('Processed data:', processedData);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// 7. Async/Await 链式调用
async function getUserData() {
    try {
        const user = await getUser(1);
        console.log('Async/Await User:', user);
        const posts = await getPosts(user.id);
        console.log('Async/Await Posts:', posts);
        const comments = await getComments(posts[0].id);
        console.log('Async/Await Comments:', comments);
        return { user, posts, comments };
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

getUserData();

// 8. Async/Await 与 Promise.all
async function fetchMultipleData() {
    try {
        const [user, posts, comments] = await Promise.all([
            getUser(1),
            getPosts(1),
            getComments(1)
        ]);
        console.log('Parallel User:', user);
        console.log('Parallel Posts:', posts);
        console.log('Parallel Comments:', comments);
    } catch (error) {
        console.error('Error:', error);
    }
}

fetchMultipleData();

// 9. 错误处理
async function fetchDataWithError() {
    try {
        const result = await new Promise((resolve, reject) => {
            setTimeout(() => {
                reject('Error fetching data');
            }, 1000);
        });
        console.log(result);
    } catch (error) {
        console.error('Caught error:', error);
    } finally {
        console.log('Cleanup');
    }
}

fetchDataWithError();
