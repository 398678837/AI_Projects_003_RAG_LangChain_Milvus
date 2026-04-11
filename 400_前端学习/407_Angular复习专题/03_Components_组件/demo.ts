// Angular 组件示例代码

import { Component, Input, Output, EventEmitter, OnInit, OnChanges, OnDestroy, SimpleChanges } from '@angular/core';

// 1. 简单的组件示例
@Component({
  selector: 'app-simple-component',
  template: `
    <div class="simple-component">
      <h3>{{ title }}</h3>
      <p>{{ content }}</p>
    </div>
  `,
  styles: [`
    .simple-component { padding: 15px; background: #f5f5f5; border-radius: 5px; }
  `]
})
export class SimpleComponent {
  title = '简单组件';
  content = '这是一个简单的Angular组件';
}

// 2. 子组件 - 接收父组件数据
@Component({
  selector: 'app-child',
  template: `
    <div class="child-component">
      <h4>子组件</h4>
      <p>来自父组件的消息: {{ messageFromParent }}</p>
      <p>来自父组件的数字: {{ numberFromParent }}</p>
      <button (click)="sendToParent()">发送消息给父组件</button>
    </div>
  `,
  styles: [`
    .child-component { padding: 10px; background: #e3f2fd; border: 1px solid #2196f3; border-radius: 5px; margin: 10px 0; }
  `]
})
export class ChildComponent {
  @Input() messageFromParent: string = '';
  @Input() numberFromParent: number = 0;
  @Output() messageToParent = new EventEmitter<string>();

  sendToParent() {
    this.messageToParent.emit('Hello from Child!');
  }
}

// 3. 父组件 - 传递数据给子组件并接收子组件消息
@Component({
  selector: 'app-parent',
  template: `
    <div class="parent-component">
      <h3>父组件</h3>
      <p>父组件消息: {{ parentMessage }}</p>
      <p>父组件数字: {{ parentNumber }}</p>
      <p>来自子组件的消息: {{ messageFromChild }}</p>
      <button (click)="updateChild()">更新子组件数据</button>
      
      <app-child 
        [messageFromParent]="parentMessage"
        [numberFromParent]="parentNumber"
        (messageToParent)="onMessageFromChild($event)">
      </app-child>
    </div>
  `,
  styles: [`
    .parent-component { padding: 15px; background: #fff3e0; border: 1px solid #ff9800; border-radius: 5px; }
  `]
})
export class ParentComponent {
  parentMessage = 'Hello from Parent!';
  parentNumber = 100;
  messageFromChild = '';

  updateChild() {
    this.parentNumber++;
  }

  onMessageFromChild(message: string) {
    this.messageFromChild = message;
  }
}

// 4. 生命周期组件
@Component({
  selector: 'app-lifecycle',
  template: `
    <div class="lifecycle-component">
      <h3>生命周期示例</h3>
      <p>输入值: {{ inputValue }}</p>
      <input [(ngModel)]="inputValue" placeholder="输入值">
      <p>生命周期日志:</p>
      <ul>
        <li *ngFor="let log of lifecycleLogs">{{ log }}</li>
      </ul>
    </div>
  `,
  styles: [`
    .lifecycle-component { padding: 15px; background: #e8f5e9; border: 1px solid #4caf50; border-radius: 5px; }
  `]
})
export class LifecycleComponent implements OnInit, OnChanges, OnDestroy {
  @Input() inputValue: string = '';
  lifecycleLogs: string[] = [];

  ngOnChanges(changes: SimpleChanges) {
    this.log('ngOnChanges - 输入属性变化');
    console.log('ngOnChanges', changes);
  }

  ngOnInit() {
    this.log('ngOnInit - 组件初始化');
    console.log('ngOnInit');
  }

  ngOnDestroy() {
    this.log('ngOnDestroy - 组件销毁');
    console.log('ngOnDestroy');
  }

  log(message: string) {
    const timestamp = new Date().toLocaleTimeString();
    this.lifecycleLogs.push(`${timestamp}: ${message}`);
  }
}

// 5. 内容投影组件
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <div class="card-header">
        <ng-content select="[header]"></ng-content>
      </div>
      <div class="card-body">
        <ng-content></ng-content>
      </div>
      <div class="card-footer">
        <ng-content select="[footer]"></ng-content>
      </div>
    </div>
  `,
  styles: [`
    .card { border: 1px solid #ddd; border-radius: 5px; margin: 10px 0; }
    .card-header { padding: 10px; background: #f5f5f5; border-bottom: 1px solid #ddd; }
    .card-body { padding: 15px; }
    .card-footer { padding: 10px; background: #f5f5f5; border-top: 1px solid #ddd; }
  `]
})
export class CardComponent { }

// 6. 使用卡片组件的示例
@Component({
  selector: 'app-card-demo',
  template: `
    <h3>内容投影示例</h3>
    <app-card>
      <div header>卡片标题</div>
      <p>这是卡片的主要内容</p>
      <p>可以放置任意内容在这里</p>
      <div footer>卡片底部</div>
    </app-card>
  `
})
export class CardDemoComponent { }

// 7. 主组件 - 整合所有示例
@Component({
  selector: 'app-components-demo',
  template: `
    <h2>Angular 组件示例</h2>
    
    <app-simple-component></app-simple-component>
    
    <hr>
    
    <app-parent></app-parent>
    
    <hr>
    
    <lifecycle-demo *ngIf="showLifecycle"></lifecycle-demo>
    <button (click)="toggleLifecycle()">
      {{ showLifecycle ? '销毁' : '创建' }}生命周期组件
    </button>
    
    <hr>
    
    <app-card-demo></app-card-demo>
  `
})
export class ComponentsDemoComponent {
  showLifecycle = true;

  toggleLifecycle() {
    this.showLifecycle = !this.showLifecycle;
  }
}
