// Angular 服务示例代码

import { Injectable, Component } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

// 1. 简单的数据服务
@Injectable({
  providedIn: 'root'
})
export class DataService {
  private data: string[] = ['数据1', '数据2', '数据3'];

  getData(): string[] {
    return this.data;
  }

  addData(item: string) {
    this.data.push(item);
  }

  removeData(index: number) {
    this.data.splice(index, 1);
  }
}

// 2. 使用 Subject 的消息服务
@Injectable({
  providedIn: 'root'
})
export class MessageService {
  private messageSubject = new BehaviorSubject<string>('');
  message$: Observable<string> = this.messageSubject.asObservable();

  sendMessage(message: string) {
    this.messageSubject.next(message);
  }

  clearMessage() {
    this.messageSubject.next('');
  }
}

// 3. 计数器服务
@Injectable({
  providedIn: 'root'
})
export class CounterService {
  private count = 0;
  private countSubject = new BehaviorSubject<number>(0);
  count$: Observable<number> = this.countSubject.asObservable();

  increment() {
    this.count++;
    this.countSubject.next(this.count);
  }

  decrement() {
    this.count--;
    this.countSubject.next(this.count);
  }

  reset() {
    this.count = 0;
    this.countSubject.next(this.count);
  }
}

// 4. 使用数据服务的组件
@Component({
  selector: 'app-data-list',
  template: `
    <div class="component">
      <h3>数据列表组件</h3>
      <ul>
        <li *ngFor="let item of data; let i = index">
          {{ item }}
          <button (click)="remove(i)">删除</button>
        </li>
      </ul>
      <input [(ngModel)]="newItem" placeholder="输入新数据">
      <button (click)="add()">添加</button>
    </div>
  `,
  styles: ['.component { padding: 15px; background: #e3f2fd; border-radius: 5px; margin: 10px 0; }']
})
export class DataListComponent {
  data: string[] = [];
  newItem = '';

  constructor(private dataService: DataService) {
    this.data = this.dataService.getData();
  }

  add() {
    if (this.newItem) {
      this.dataService.addData(this.newItem);
      this.newItem = '';
    }
  }

  remove(index: number) {
    this.dataService.removeData(index);
  }
}

// 5. 发送消息的组件
@Component({
  selector: 'app-message-sender',
  template: `
    <div class="component">
      <h3>消息发送组件</h3>
      <input [(ngModel)]="message" placeholder="输入消息">
      <button (click)="send()">发送</button>
      <button (click)="clear()">清除</button>
    </div>
  `,
  styles: ['.component { padding: 15px; background: #fff3e0; border-radius: 5px; margin: 10px 0; }']
})
export class MessageSenderComponent {
  message = '';

  constructor(private messageService: MessageService) { }

  send() {
    if (this.message) {
      this.messageService.sendMessage(this.message);
      this.message = '';
    }
  }

  clear() {
    this.messageService.clearMessage();
  }
}

// 6. 接收消息的组件
@Component({
  selector: 'app-message-receiver',
  template: `
    <div class="component">
      <h3>消息接收组件</h3>
      <p *ngIf="receivedMessage">收到消息: {{ receivedMessage }}</p>
      <p *ngIf="!receivedMessage">暂无消息</p>
    </div>
  `,
  styles: ['.component { padding: 15px; background: #e8f5e9; border-radius: 5px; margin: 10px 0; }']
})
export class MessageReceiverComponent {
  receivedMessage = '';

  constructor(private messageService: MessageService) {
    this.messageService.message$.subscribe(message => {
      this.receivedMessage = message;
    });
  }
}

// 7. 使用计数器服务的组件
@Component({
  selector: 'app-counter-display',
  template: `
    <div class="component">
      <h3>计数器显示组件</h3>
      <p class="count">当前计数: {{ count }}</p>
    </div>
  `,
  styles: [`
    .component { padding: 15px; background: #fce4ec; border-radius: 5px; margin: 10px 0; }
    .count { font-size: 24px; font-weight: bold; text-align: center; }
  `]
})
export class CounterDisplayComponent {
  count = 0;

  constructor(private counterService: CounterService) {
    this.counterService.count$.subscribe(count => {
      this.count = count;
    });
  }
}

@Component({
  selector: 'app-counter-controls',
  template: `
    <div class="component">
      <h3>计数器控制组件</h3>
      <button (click)="increment()">+1</button>
      <button (click)="decrement()">-1</button>
      <button (click)="reset()">重置</button>
    </div>
  `,
  styles: ['.component { padding: 15px; background: #f3e5f5; border-radius: 5px; margin: 10px 0; } button { margin: 5px; padding: 10px 20px; }']
})
export class CounterControlsComponent {
  constructor(private counterService: CounterService) { }

  increment() {
    this.counterService.increment();
  }

  decrement() {
    this.counterService.decrement();
  }

  reset() {
    this.counterService.reset();
  }
}

// 8. 主组件 - 整合所有服务示例
@Component({
  selector: 'app-services-demo',
  template: `
    <h2>Angular 服务示例</h2>
    
    <div class="section">
      <h3>数据服务示例</h3>
      <app-data-list></app-data-list>
    </div>
    
    <hr>
    
    <div class="section">
      <h3>消息服务示例（组件间通信）</h3>
      <app-message-sender></app-message-sender>
      <app-message-receiver></app-message-receiver>
    </div>
    
    <hr>
    
    <div class="section">
      <h3>计数器服务示例</h3>
      <app-counter-display></app-counter-display>
      <app-counter-controls></app-counter-controls>
    </div>
  `,
  styles: ['.section { margin: 20px 0; }']
})
export class ServicesDemoComponent { }
