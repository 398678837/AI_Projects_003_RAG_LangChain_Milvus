// DOM 操作示例

// 选择元素
const container = document.getElementById('container');
const paragraphs = document.getElementsByClassName('paragraph');
const headings = document.getElementsByTagName('h1');
const firstPara = document.querySelector('.paragraph:first-child');
const allParas = document.querySelectorAll('.paragraph');

// 修改元素内容
firstPara.textContent = 'This is the first paragraph';
firstPara.innerHTML = '<strong>This is the first paragraph</strong>';

// 修改元素属性
const link = document.createElement('a');
link.href = 'https://www.example.com';
link.textContent = 'Visit Example';
link.setAttribute('target', '_blank');

// 添加元素
container.appendChild(link);

// 插入元素
const newPara = document.createElement('p');
newPara.textContent = 'This is a new paragraph';
container.insertBefore(newPara, link);

// 删除元素
container.removeChild(link);

// 修改样式
newPara.style.color = 'blue';
newPara.style.fontSize = '18px';
newPara.classList.add('highlight');

// 事件处理
newPara.addEventListener('click', function() {
    this.style.backgroundColor = 'yellow';
});

// 事件冒泡和捕获
document.addEventListener('click', function() {
    console.log('Document clicked');
}, true); // 捕获阶段

container.addEventListener('click', function() {
    console.log('Container clicked');
});

newPara.addEventListener('click', function(e) {
    console.log('Paragraph clicked');
    e.stopPropagation(); // 阻止冒泡
});
