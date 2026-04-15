package com.example.hibernate.transaction;

import org.hibernate.LockMode;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class TransactionDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate事务示例 ===");

        try {
            initializeData();
            
            basicTransactionDemo();
            rollbackDemo();
            optimisticLockDemo();
            pessimisticLockDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void initializeData() {
        System.out.println("\n--- 初始化数据 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Account account = new Account("张三", 10000.00);
        session.save(account);

        Product product = new Product("iPhone", 7999.00, 10);
        session.save(product);

        tx.commit();
        session.close();
        sessionFactory.close();

        System.out.println("数据初始化完成");
    }

    private static void basicTransactionDemo() {
        System.out.println("\n--- 1. 基本事务演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();
            System.out.println("事务开始");

            Account account = session.get(Account.class, 1L);
            System.out.println("初始余额: " + account.getBalance());

            account.setBalance(account.getBalance() + 1000);
            session.update(account);
            System.out.println("存款1000，当前余额: " + account.getBalance());

            tx.commit();
            System.out.println("事务提交成功");

            Account updatedAccount = session.get(Account.class, 1L);
            System.out.println("提交后余额: " + updatedAccount.getBalance());

        } catch (Exception e) {
            if (tx != null) {
                tx.rollback();
                System.out.println("事务回滚: " + e.getMessage());
            }
        } finally {
            session.close();
            sessionFactory.close();
        }
    }

    private static void rollbackDemo() {
        System.out.println("\n--- 2. 事务回滚演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();
            System.out.println("事务开始");

            Account account = session.get(Account.class, 1L);
            System.out.println("初始余额: " + account.getBalance());

            account.setBalance(account.getBalance() - 5000);
            session.update(account);
            System.out.println("扣款5000，当前余额: " + account.getBalance());

            if (true) {
                throw new RuntimeException("模拟异常");
            }

            tx.commit();
            System.out.println("事务提交");

        } catch (Exception e) {
            if (tx != null) {
                tx.rollback();
                System.out.println("事务回滚: " + e.getMessage());
            }

            Account account = session.get(Account.class, 1L);
            System.out.println("回滚后余额: " + account.getBalance());
        } finally {
            session.close();
            sessionFactory.close();
        }
    }

    private static void optimisticLockDemo() {
        System.out.println("\n--- 3. 乐观锁演示 ---");

        SessionFactory sessionFactory = createSessionFactory();

        Session session1 = sessionFactory.openSession();
        Transaction tx1 = session1.beginTransaction();
        Product product1 = session1.get(Product.class, 1L);
        System.out.println("Session1获取产品，版本号: " + product1.getVersion());
        tx1.commit();
        session1.close();

        Session session2 = sessionFactory.openSession();
        Transaction tx2 = session2.beginTransaction();
        Product product2 = session2.get(Product.class, 1L);
        System.out.println("Session2获取产品，版本号: " + product2.getVersion());
        product2.setStock(product2.getStock() - 1);
        session2.update(product2);
        tx2.commit();
        session2.close();
        System.out.println("Session2更新产品，库存-1");

        Session session3 = sessionFactory.openSession();
        Transaction tx3 = session3.beginTransaction();
        try {
            product1.setStock(product1.getStock() - 1);
            session3.update(product1);
            tx3.commit();
            System.out.println("Session1尝试更新产品（应该失败）");
        } catch (Exception e) {
            tx3.rollback();
            System.out.println("Session1更新失败: " + e.getMessage());
        }
        session3.close();

        Session session4 = sessionFactory.openSession();
        Product finalProduct = session4.get(Product.class, 1L);
        System.out.println("最终库存: " + finalProduct.getStock() + "，版本号: " + finalProduct.getVersion());
        session4.close();

        sessionFactory.close();
    }

    private static void pessimisticLockDemo() {
        System.out.println("\n--- 4. 悲观锁演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Product product = session.get(Product.class, 1L, LockMode.PESSIMISTIC_WRITE);
        System.out.println("获取产品（悲观锁），当前库存: " + product.getStock());

        product.setStock(product.getStock() - 1);
        session.update(product);
        System.out.println("更新库存-1");

        tx.commit();
        session.close();

        Session session2 = sessionFactory.openSession();
        Product finalProduct = session2.get(Product.class, 1L);
        System.out.println("最终库存: " + finalProduct.getStock());
        session2.close();

        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Account.class);
        config.addAnnotatedClass(Product.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "accounts_tx")
class Account {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "balance")
    private Double balance;

    public Account() {
    }

    public Account(String name, Double balance) {
        this.name = name;
        this.balance = balance;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getBalance() { return balance; }
    public void setBalance(Double balance) { this.balance = balance; }
}

@Entity
@Table(name = "products_tx")
class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "price")
    private Double price;

    @Column(name = "stock")
    private Integer stock;

    @Version
    @Column(name = "version")
    private Long version;

    public Product() {
    }

    public Product(String name, Double price, Integer stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
    public Integer getStock() { return stock; }
    public void setStock(Integer stock) { this.stock = stock; }
    public Long getVersion() { return version; }
    public void setVersion(Long version) { this.version = version; }
}
