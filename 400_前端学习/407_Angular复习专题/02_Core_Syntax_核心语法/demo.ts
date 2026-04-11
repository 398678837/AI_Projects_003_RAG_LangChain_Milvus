// Angular 核心语法示例代码

import { Component } from '@angular/core';

@Component({
  selector: 'app-core-syntax',
  template: `
    <h2>Angular 核心语法</h2>
    
    <!-- 1. 插值表达式 -->
    <div class="section">
      <h3>1. 插值表达式</h3>
      <p>名称: {{ name }}</p>
      <p>年龄: {{ age }}</p>
      <p>问候: {{ getGreeting() }}</p>
    </div>
    
    <!-- 2. 属性绑定 -->
    <div class="section">
      <h3>2. 属性绑定</h3>
      <img [src]="logoUrl" [alt]="logoAlt" [width]="100">
      <button [disabled]="isDisabled">禁用按钮</button>
      <input [value]="defaultValue">
    </div>
    
    <!-- 3. 事件绑定 -->
    <div class="section">
      <h3>3. 事件绑定</h3>
      <button (click)="onButtonClick()">点击按钮</button>
      <input (input)="onInputChange($event)" placeholder="输入内容">
      <p>输入的内容: {{ inputValue }}</p>
    </div>
    
    <!-- 4. 双向绑定 -->
    <div class="section">
      <h3>4. 双向绑定</h3>
      <input [(ngModel)]="username" placeholder="输入用户名">
      <p>用户名: {{ username }}</p>
    </div>
    
    <!-- 5. 结构指令 - *ngIf -->
    <div class="section">
      <h3>5. 结构指令 - *ngIf</h3>
      <button (click)="toggleShow()">切换显示</button>
      <p *ngIf="isShown">这段文字会根据条件显示或隐藏</p>
      <p *ngIf="isShown; else elseBlock">条件为真时显示</p>
      <ng-template #elseBlock>
        <p>条件为假时显示</p>
      </ng-template>
    </div>
    
    <!-- 6. 结构指令 - *ngFor -->
    <div class="section">
      <h3>6. 结构指令 - *ngFor</h3>
      <ul>
        <li *ngFor="let fruit of fruits; let i = index">
          {{ i + 1 }}. {{ fruit }}
        </li>
      </ul>
    </div>
    
    <!-- 7. 结构指令 - *ngSwitch -->
    <div class="section">
      <h3>7. 结构指令 - *ngSwitch</h3>
      <select [(ngModel)]="currentColor">
        <option value="red">红色</option>
        <option value="green">绿色</option>
        <option value="blue">蓝色</option>
      </select>
      <div [ngSwitch]="currentColor">
        <p *ngSwitchCase="'red'" style="color: red;">红色</p>
        <p *ngSwitchCase="'green'" style="color: green;">绿色</p>
        <p *ngSwitchCase="'blue'" style="color: blue;">蓝色</p>
        <p *ngSwitchDefault>请选择颜色</p>
      </div>
    </div>
    
    <!-- 8. 属性指令 - ngClass -->
    <div class="section">
      <h3>8. 属性指令 - ngClass</h3>
      <p [ngClass]="{'highlight': isHighlighted, 'bold': isBold}">
        这段文字可以动态改变样式
      </p>
      <button (click)="toggleHighlight()">切换高亮</button>
      <button (click)="toggleBold()">切换加粗</button>
    </div>
    
    <!-- 9. 属性指令 - ngStyle -->
    <div class="section">
      <h3>9. 属性指令 - ngStyle</h3>
      <p [ngStyle]="{'color': textColor, 'font-size': fontSize + 'px'}">
        这段文字的样式可以动态修改
      </p>
      <input type="color" [(ngModel)]="textColor">
      <input type="range" [(ngModel)]="fontSize" min="12" max="36">
    </div>
    
    <!-- 10. 管道 -->
    <div class="section">
      <h3>10. 管道</h3>
      <p>原始文本: {{ message }}</p>
      <p>大写: {{ message | uppercase }}</p>
      <p>小写: {{ message | lowercase }}</p>
      <p>标题: {{ message | titlecase }}</p>
      <p>日期: {{ today | date:'yyyy-MM-dd HH:mm:ss' }}</p>
      <p>货币: {{ price | currency:'CNY' }}</p>
      <p>数字: {{ pi | number:'1.2-2' }}</p>
      <p>百分比: {{ percentage | percent }}</p>
      <p>JSON: {{ user | json }}</p>
    </div>
  `,
  styles: [`
    .section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
    .highlight { background-color: yellow; }
    .bold { font-weight: bold; }
  `]
})
export class CoreSyntaxComponent {
  name = '张三';
  age = 25;
  logoUrl = 'https://angular.io/assets/images/logos/angular/angular.svg';
  logoAlt = 'Angular Logo';
  isDisabled = false;
  defaultValue = '默认值';
  inputValue = '';
  username = '';
  isShown = true;
  fruits = ['苹果', '香蕉', '橙子', '葡萄'];
  currentColor = 'red';
  isHighlighted = false;
  isBold = false;
  textColor = '#000000';
  fontSize = 16;
  message = 'Hello Angular World!';
  today = new Date();
  price = 99.99;
  pi = 3.1415926;
  percentage = 0.75;
  user = { name: '李四', age: 30, email: 'lisi@example.com' };

  getGreeting() {
    return `你好，${this.name}！`;
  }

  onButtonClick() {
    alert('按钮被点击了！');
  }

  onInputChange(event: Event) {
    this.inputValue = (event.target as HTMLInputElement).value;
  }

  toggleShow() {
    this.isShown = !this.isShown;
  }

  toggleHighlight() {
    this.isHighlighted = !this.isHighlighted;
  }

  toggleBold() {
    this.isBold = !this.isBold;
  }
}
