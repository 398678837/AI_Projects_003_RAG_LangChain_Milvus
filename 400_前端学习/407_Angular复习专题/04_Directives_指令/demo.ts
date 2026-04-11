// Angular 指令示例代码

import { Directive, ElementRef, Renderer2, HostListener, Input, TemplateRef, ViewContainerRef } from '@angular/core';
import { Component } from '@angular/core';

// 1. 自定义属性指令 - 高亮指令
@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(private el: ElementRef, private renderer: Renderer2) { }

  @Input() appHighlight: string = 'yellow';

  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.appHighlight);
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.highlight(null);
  }

  private highlight(color: string | null) {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', color);
  }
}

// 2. 自定义属性指令 - 字体大小指令
@Directive({
  selector: '[appFontSize]'
})
export class FontSizeDirective {
  constructor(private el: ElementRef, private renderer: Renderer2) { }

  @Input() set appFontSize(size: number) {
    this.renderer.setStyle(this.el.nativeElement, 'fontSize', size + 'px');
  }
}

// 3. 自定义结构指令 - unless（ngIf的相反）
@Directive({
  selector: '[appUnless]'
})
export class UnlessDirective {
  private hasView = false;

  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) { }

  @Input() set appUnless(condition: boolean) {
    if (!condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.templateRef);
      this.hasView = true;
    } else if (condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}

// 4. 使用自定义指令的组件
@Component({
  selector: 'app-directives-demo',
  template: `
    <h2>Angular 指令示例</h2>
    
    <!-- 自定义属性指令 - 高亮 -->
    <div class="section">
      <h3>1. 自定义属性指令 - 高亮</h3>
      <p appHighlight="lightblue">鼠标悬停时高亮（浅蓝色）</p>
      <p appHighlight="lightgreen">鼠标悬停时高亮（浅绿色）</p>
      <p [appHighlight]="highlightColor">鼠标悬停时高亮（动态颜色）</p>
      <input type="color" [(ngModel)]="highlightColor">
    </div>
    
    <!-- 自定义属性指令 - 字体大小 -->
    <div class="section">
      <h3>2. 自定义属性指令 - 字体大小</h3>
      <p [appFontSize]="12">12px 字体</p>
      <p [appFontSize]="16">16px 字体</p>
      <p [appFontSize]="24">24px 字体</p>
      <p [appFontSize]="fontSize">动态字体大小: {{ fontSize }}px</p>
      <input type="range" [(ngModel)]="fontSize" min="12" max="36">
    </div>
    
    <!-- 自定义结构指令 - unless -->
    <div class="section">
      <h3>3. 自定义结构指令 - unless</h3>
      <button (click)="toggleCondition()">切换条件</button>
      <p>条件值: {{ condition }}</p>
      
      <p *ngIf="condition">*ngIf: 条件为真时显示</p>
      <p *appUnless="condition">*appUnless: 条件为假时显示</p>
    </div>
    
    <!-- 组合使用 -->
    <div class="section">
      <h3>4. 组合使用指令</h3>
      <div 
        *ngFor="let item of items"
        [appFontSize]="14 + item.size"
        [appHighlight]="item.color">
        {{ item.name }}
      </div>
    </div>
  `,
  styles: [`
    .section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
  `]
})
export class DirectivesDemoComponent {
  highlightColor = '#ffff00';
  fontSize = 18;
  condition = true;
  
  items = [
    { name: '项目1', size: 0, color: '#ffcccc' },
    { name: '项目2', size: 2, color: '#ccffcc' },
    { name: '项目3', size: 4, color: '#ccccff' }
  ];

  toggleCondition() {
    this.condition = !this.condition;
  }
}
