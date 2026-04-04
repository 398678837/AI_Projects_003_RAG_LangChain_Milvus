import io.seata.spring.annotation.GlobalTransactional;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class SeataDemo {
    public static void main(String[] args) {
        SpringApplication.run(SeataDemo.class, args);
    }
}

// 订单服务
@RestController
@RequestMapping("/api/orders")
class OrderController {
    private final List<Order> orders = new ArrayList<>();
    private Long nextOrderId = 1L;
    private final ProductService productService;
    private final AccountService accountService;
    
    public OrderController(ProductService productService, AccountService accountService) {
        this.productService = productService;
        this.accountService = accountService;
    }
    
    @GlobalTransactional
    @GetMapping("/create/{userId}/{productId}/{count}")
    public Order createOrder(@PathVariable Long userId, @PathVariable String productId, @PathVariable int count) {
        // 创建订单
        Order order = new Order();
        order.setId(nextOrderId++);
        order.setUserId(userId);
        order.setProductId(productId);
        order.setCount(count);
        order.setStatus(0); // 0: 待支付, 1: 已支付, 2: 已取消
        orders.add(order);
        System.out.println("Created order: " + order.getId());
        
        try {
            // 扣减库存
            productService.deductStock(productId, count);
            // 扣减账户余额
            accountService.deductBalance(userId, count * 100);
            // 确认订单
            order.setStatus(1);
            System.out.println("Order confirmed: " + order.getId());
        } catch (Exception e) {
            // 回滚订单
            order.setStatus(2);
            System.out.println("Order cancelled: " + order.getId());
            throw e;
        }
        
        return order;
    }
    
    @GetMapping
    public List<Order> getOrders() {
        return orders;
    }
}

// 产品服务
@RestController
@RequestMapping("/api/products")
class ProductController {
    private final List<Product> products = new ArrayList<>();
    
    public ProductController() {
        // 初始化一些测试数据
        products.add(new Product("1", "Product 1", 100, 1000));
        products.add(new Product("2", "Product 2", 200, 2000));
        products.add(new Product("3", "Product 3", 300, 3000));
    }
    
    @GetMapping
    public List<Product> getProducts() {
        return products;
    }
    
    @GetMapping("/{id}")
    public Product getProductById(@PathVariable String id) {
        return products.stream()
                .filter(product -> product.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}

// 账户服务
@RestController
@RequestMapping("/api/accounts")
class AccountController {
    private final List<Account> accounts = new ArrayList<>();
    
    public AccountController() {
        // 初始化一些测试数据
        accounts.add(new Account(1L, "User 1", 10000));
        accounts.add(new Account(2L, "User 2", 20000));
        accounts.add(new Account(3L, "User 3", 30000));
    }
    
    @GetMapping
    public List<Account> getAccounts() {
        return accounts;
    }
    
    @GetMapping("/{id}")
    public Account getAccountById(@PathVariable Long id) {
        return accounts.stream()
                .filter(account -> account.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}

// 服务实现
class ProductService {
    private final List<Product> products = new ArrayList<>();
    
    public ProductService() {
        // 初始化一些测试数据
        products.add(new Product("1", "Product 1", 100, 1000));
        products.add(new Product("2", "Product 2", 200, 2000));
        products.add(new Product("3", "Product 3", 300, 3000));
    }
    
    public void deductStock(String productId, int count) {
        Product product = products.stream()
                .filter(p -> p.getId().equals(productId))
                .findFirst()
                .orElse(null);
        
        if (product == null) {
            throw new RuntimeException("Product not found");
        }
        
        if (product.getStock() < count) {
            throw new RuntimeException("Insufficient stock");
        }
        
        product.setStock(product.getStock() - count);
        System.out.println("Deducted stock for product " + productId + ": " + count);
    }
}

class AccountService {
    private final List<Account> accounts = new ArrayList<>();
    
    public AccountService() {
        // 初始化一些测试数据
        accounts.add(new Account(1L, "User 1", 10000));
        accounts.add(new Account(2L, "User 2", 20000));
        accounts.add(new Account(3L, "User 3", 30000));
    }
    
    public void deductBalance(Long userId, double amount) {
        Account account = accounts.stream()
                .filter(a -> a.getId().equals(userId))
                .findFirst()
                .orElse(null);
        
        if (account == null) {
            throw new RuntimeException("Account not found");
        }
        
        if (account.getBalance() < amount) {
            throw new RuntimeException("Insufficient balance");
        }
        
        account.setBalance(account.getBalance() - amount);
        System.out.println("Deducted balance for user " + userId + ": " + amount);
    }
}

// 实体类
class Order {
    private Long id;
    private Long userId;
    private String productId;
    private int count;
    private int status;
    
    public Order() {
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public Long getUserId() {
        return userId;
    }
    
    public void setUserId(Long userId) {
        this.userId = userId;
    }
    
    public String getProductId() {
        return productId;
    }
    
    public void setProductId(String productId) {
        this.productId = productId;
    }
    
    public int getCount() {
        return count;
    }
    
    public void setCount(int count) {
        this.count = count;
    }
    
    public int getStatus() {
        return status;
    }
    
    public void setStatus(int status) {
        this.status = status;
    }
}

class Product {
    private String id;
    private String name;
    private double price;
    private int stock;
    
    public Product() {
    }
    
    public Product(String id, String name, double price, int stock) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public double getPrice() {
        return price;
    }
    
    public void setPrice(double price) {
        this.price = price;
    }
    
    public int getStock() {
        return stock;
    }
    
    public void setStock(int stock) {
        this.stock = stock;
    }
}

class Account {
    private Long id;
    private String name;
    private double balance;
    
    public Account() {
    }
    
    public Account(Long id, String name, double balance) {
        this.id = id;
        this.name = name;
        this.balance = balance;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public void setBalance(double balance) {
        this.balance = balance;
    }
}