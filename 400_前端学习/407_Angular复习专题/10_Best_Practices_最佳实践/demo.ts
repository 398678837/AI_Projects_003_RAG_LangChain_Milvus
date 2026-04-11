// Angular 最佳实践示例代码

import { Component, Input, Output, EventEmitter, ChangeDetectionStrategy, OnInit, TrackByFunction } from '@angular/core';
import { CommonModule } from '@angular/common';

// 1. 使用 OnPush 变更检测策略的组件
interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
}

@Component({
  selector: 'app-product-card',
  template: `
    <div class="product-card">
      <h4>{{ product.name }}</h4>
      <p class="category">{{ product.category }}</p>
      <p class="price">¥{{ product.price }}</p>
      <button (click)="addToCart()">加入购物车</button>
    </div>
  `,
  styles: [`
    .product-card { padding: 15px; border: 1px solid #ddd; border-radius: 5px; text-align: center; }
    .category { color: #666; font-size: 12px; }
    .price { font-size: 20px; font-weight: bold; color: #e91e63; }
    button { padding: 8px 20px; background: #2196f3; color: white; border: none; border-radius: 4px; cursor: pointer; }
  `],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProductCardComponent {
  @Input({ required: true }) product!: Product;
  @Output() addToCartClicked = new EventEmitter<Product>();

  addToCart() {
    this.addToCartClicked.emit(this.product);
  }
}

// 2. 智能组件
@Component({
  selector: 'app-product-list',
  template: `
    <div class="product-list">
      <h3>商品列表</h3>
      <div class="filter">
        <label>分类筛选:</label>
        <select [(ngModel)]="selectedCategory" (change)="filterProducts()">
          <option value="">全部</option>
          <option *ngFor="let category of categories" [value]="category">{{ category }}</option>
        </select>
      </div>
      <div class="products-grid">
        <app-product-card 
          *ngFor="let product of filteredProducts; trackBy: trackByProductId"
          [product]="product"
          (addToCartClicked)="onAddToCart($event)">
        </app-product-card>
      </div>
      <div class="cart-info" *ngIf="cart.length > 0">
        <h4>购物车 ({{ cart.length }})</h4>
        <ul>
          <li *ngFor="let item of cart">
            {{ item.name }} - ¥{{ item.price }}
          </li>
        </ul>
        <p>总计: ¥{{ cartTotal }}</p>
      </div>
    </div>
  `,
  styles: [`
    .product-list { padding: 20px; }
    .filter { margin-bottom: 20px; }
    .filter select { margin-left: 10px; padding: 5px; }
    .products-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }
    .cart-info { margin-top: 30px; padding: 20px; background: #fff3e0; border-radius: 5px; }
    .cart-info ul { list-style: none; padding: 0; }
    .cart-info li { padding: 5px 0; border-bottom: 1px solid #ddd; }
  `],
  changeDetection: ChangeDetectionStrategy.Default
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  filteredProducts: Product[] = [];
  categories: string[] = [];
  selectedCategory = '';
  cart: Product[] = [];

  get cartTotal(): number {
    return this.cart.reduce((sum, item) => sum + item.price, 0);
  }

  ngOnInit() {
    this.products = this.getProducts();
    this.filteredProducts = [...this.products];
    this.categories = [...new Set(this.products.map(p => p.category))];
  }

  trackByProductId: TrackByFunction<Product> = (index, product) => product.id;

  filterProducts() {
    if (this.selectedCategory) {
      this.filteredProducts = this.products.filter(p => p.category === this.selectedCategory);
    } else {
      this.filteredProducts = [...this.products];
    }
  }

  onAddToCart(product: Product) {
    this.cart.push(product);
    console.log('已添加到购物车:', product.name);
  }

  private getProducts(): Product[] {
    return [
      { id: 1, name: 'iPhone 15', price: 7999, category: '手机' },
      { id: 2, name: 'MacBook Pro', price: 14999, category: '电脑' },
      { id: 3, name: 'AirPods Pro', price: 1899, category: '配件' },
      { id: 4, name: 'iPad Air', price: 4799, category: '平板' },
      { id: 5, name: 'Apple Watch', price: 2999, category: '手表' },
      { id: 6, name: 'Samsung Galaxy', price: 6999, category: '手机' },
      { id: 7, name: 'Sony WH-1000XM5', price: 2499, category: '配件' },
      { id: 8, name: 'Dell XPS', price: 9999, category: '电脑' }
    ];
  }
}

// 3. 使用纯管道
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'formatPrice',
  pure: true
})
export class FormatPricePipe implements PipeTransform {
  transform(value: number, currency: string = '¥'): string {
    return `${currency}${value.toFixed(2)}`;
  }
}

@Component({
  selector: 'app-pipe-demo',
  template: `
    <div class="pipe-demo">
      <h3>纯管道示例</h3>
      <p>原价: {{ price }}</p>
      <p>格式化: {{ price | formatPrice }}</p>
      <p>美元: {{ price | formatPrice:'$' }}</p>
      <p>使用管道计算: {{ calculateTotal() | formatPrice }}</p>
      <p>使用 getter: {{ total | formatPrice }}</p>
    </div>
  `,
  styles: ['.pipe-demo { padding: 20px; background: #e8f5e9; border-radius: 5px; margin-top: 20px; }']
})
export class PipeDemoComponent {
  price = 99.9;
  items = [10, 20, 30, 40];

  get total(): number {
    console.log('计算总价 (getter)');
    return this.items.reduce((sum, item) => sum + item, 0);
  }

  calculateTotal(): number {
    console.log('计算总价 (方法)');
    return this.items.reduce((sum, item) => sum + item, 0);
  }
}

// 4. 主组件
@Component({
  selector: 'app-best-practices-demo',
  template: `
    <h2>Angular 最佳实践示例</h2>
    
    <div class="section">
      <h3>1. 使用 OnPush 变更检测</h3>
      <p class="tip">ProductCardComponent 使用了 OnPush 策略，只有当输入属性变化时才会检查</p>
      <app-product-list></app-product-list>
    </div>
    
    <div class="section">
      <h3>2. 使用纯管道</h3>
      <p class="tip">纯管道只在输入变化时重新计算，提高性能</p>
      <app-pipe-demo></app-pipe-demo>
    </div>
    
    <div class="section">
      <h3>3. 使用 trackBy 优化 *ngFor</h3>
      <p class="tip">在商品列表中使用了 trackByProductId，避免不必要的 DOM 操作</p>
    </div>
    
    <div class="section">
      <h3>4. 组件分层</h3>
      <p class="tip">ProductListComponent 是智能组件，ProductCardComponent 是展示组件</p>
    </div>
    
    <div class="tips">
      <h3>其他最佳实践建议:</h3>
      <ul>
        <li>使用特性模块组织代码</li>
        <li>懒加载非核心模块</li>
        <li>避免在模板中调用复杂方法</li>
        <li>使用 async 管道自动管理订阅</li>
        <li>遵循 Angular 命名约定</li>
        <li>编写单元测试和端到端测试</li>
      </ul>
    </div>
  `,
  styles: [`
    .section { margin-bottom: 30px; padding: 20px; background: #f5f5f5; border-radius: 5px; }
    .tip { color: #666; font-style: italic; margin-bottom: 15px; }
    .tips { margin-top: 30px; padding: 20px; background: #fff3e0; border-radius: 5px; }
    .tips ul { margin: 10px 0 0 20px; }
    .tips li { margin: 5px 0; }
  `]
})
export class BestPracticesDemoComponent { }

// 5. 最佳实践模块
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    FormsModule
  ],
  declarations: [
    ProductCardComponent,
    ProductListComponent,
    FormatPricePipe,
    PipeDemoComponent,
    BestPracticesDemoComponent
  ]
})
export class BestPracticesDemoModule { }
