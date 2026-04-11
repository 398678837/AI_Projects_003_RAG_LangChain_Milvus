// Angular 基础概念示例代码

// 1. 创建Angular项目的命令（在终端执行）
// ng new my-app
// cd my-app
// ng serve

// 2. 简单的组件示例
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h1>{{ title }}</h1>
    <p>欢迎学习Angular！</p>
  `,
  styles: [`
    h1 { color: #1976d2; }
  `]
})
export class AppComponent {
  title = '我的第一个Angular应用';
}

// 3. 模块示例
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

// 4. 数据绑定示例
@Component({
  selector: 'app-data-binding',
  template: `
    <h2>数据绑定示例</h2>
    
    <!-- 插值表达式 -->
    <p>消息: {{ message }}</p>
    
    <!-- 属性绑定 -->
    <img [src]="imageUrl" alt="图片">
    
    <!-- 事件绑定 -->
    <button (click)="onClick()">点击我</button>
    
    <!-- 双向绑定 -->
    <input [(ngModel)]="name" placeholder="输入姓名">
    <p>你好, {{ name }}!</p>
  `
})
export class DataBindingComponent {
  message = 'Hello Angular!';
  imageUrl = 'https://angular.io/assets/images/logos/angular/angular.svg';
  name = '';

  onClick() {
    alert('按钮被点击了！');
  }
}
