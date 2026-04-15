package com.example.hibernate.hql;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

import java.util.List;

public class HQLDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate HQL查询示例 ===");

        try {
            initializeData();
            
            basicQueryDemo();
            conditionalQueryDemo();
            sortingDemo();
            paginationDemo();
            aggregateQueryDemo();
            joinQueryDemo();
            subqueryDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void initializeData() {
        System.out.println("\n--- 初始化数据 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Category cat1 = new Category("电子产品");
        Category cat2 = new Category("图书");

        Product p1 = new Product("iPhone 15", 7999.00, 100, cat1);
        Product p2 = new Product("MacBook Pro", 14999.00, 50, cat1);
        Product p3 = new Product("iPad", 4999.00, 200, cat1);
        Product p4 = new Product("Java编程思想", 108.00, 500, cat2);
        Product p5 = new Product("Hibernate实战", 89.00, 300, cat2);

        session.save(cat1);
        session.save(cat2);
        session.save(p1);
        session.save(p2);
        session.save(p3);
        session.save(p4);
        session.save(p5);

        tx.commit();
        session.close();
        sessionFactory.close();

        System.out.println("数据初始化完成");
    }

    private static void basicQueryDemo() {
        System.out.println("\n--- 1. 基本查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Product";
        List<Product> products1 = session.createQuery(hql1, Product.class).list();
        System.out.println("查询所有产品，数量: " + products1.size());

        String hql2 = "SELECT p.name FROM Product p";
        List<String> names = session.createQuery(hql2, String.class).list();
        System.out.println("产品名称列表: " + names);

        String hql3 = "SELECT DISTINCT p.category FROM Product p";
        List<Category> categories = session.createQuery(hql3, Category.class).list();
        System.out.println("不同的分类，数量: " + categories.size());

        session.close();
        sessionFactory.close();
    }

    private static void conditionalQueryDemo() {
        System.out.println("\n--- 2. 条件查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Product p WHERE p.price > 5000";
        List<Product> products1 = session.createQuery(hql1, Product.class).list();
        System.out.println("价格大于5000的产品，数量: " + products1.size());

        String hql2 = "FROM Product p WHERE p.name LIKE 'i%'";
        List<Product> products2 = session.createQuery(hql2, Product.class).list();
        System.out.println("名称以i开头的产品，数量: " + products2.size());

        String hql3 = "FROM Product p WHERE p.price BETWEEN 100 AND 1000";
        List<Product> products3 = session.createQuery(hql3, Product.class).list();
        System.out.println("价格在100-1000之间的产品，数量: " + products3.size());

        String hql4 = "FROM Product p WHERE p.stock > 0 AND p.category.name = '电子产品'";
        List<Product> products4 = session.createQuery(hql4, Product.class).list();
        System.out.println("电子产品且有库存的产品，数量: " + products4.size());

        session.close();
        sessionFactory.close();
    }

    private static void sortingDemo() {
        System.out.println("\n--- 3. 排序 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Product p ORDER BY p.price ASC";
        List<Product> products1 = session.createQuery(hql1, Product.class).list();
        System.out.println("按价格升序排列:");
        for (Product p : products1) {
            System.out.println("  " + p.getName() + " - " + p.getPrice());
        }

        String hql2 = "FROM Product p ORDER BY p.price DESC, p.name ASC";
        List<Product> products2 = session.createQuery(hql2, Product.class).list();
        System.out.println("\n按价格降序、名称升序排列:");
        for (Product p : products2) {
            System.out.println("  " + p.getName() + " - " + p.getPrice());
        }

        session.close();
        sessionFactory.close();
    }

    private static void paginationDemo() {
        System.out.println("\n--- 4. 分页查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql = "FROM Product p ORDER BY p.price ASC";
        Query<Product> query = session.createQuery(hql, Product.class);

        int pageSize = 2;
        int pageNum = 1;

        query.setFirstResult((pageNum - 1) * pageSize);
        query.setMaxResults(pageSize);
        List<Product> page1 = query.list();
        System.out.println("第1页:");
        for (Product p : page1) {
            System.out.println("  " + p.getName());
        }

        pageNum = 2;
        query.setFirstResult((pageNum - 1) * pageSize);
        query.setMaxResults(pageSize);
        List<Product> page2 = query.list();
        System.out.println("\n第2页:");
        for (Product p : page2) {
            System.out.println("  " + p.getName());
        }

        session.close();
        sessionFactory.close();
    }

    private static void aggregateQueryDemo() {
        System.out.println("\n--- 5. 聚合函数 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "SELECT COUNT(p) FROM Product p";
        Long count = session.createQuery(hql1, Long.class).uniqueResult();
        System.out.println("产品总数: " + count);

        String hql2 = "SELECT AVG(p.price) FROM Product p";
        Double avgPrice = session.createQuery(hql2, Double.class).uniqueResult();
        System.out.println("平均价格: " + String.format("%.2f", avgPrice));

        String hql3 = "SELECT MAX(p.price), MIN(p.price) FROM Product p";
        Object[] minMax = (Object[]) session.createQuery(hql3).uniqueResult();
        System.out.println("最高价格: " + minMax[0] + ", 最低价格: " + minMax[1]);

        String hql4 = "SELECT p.category.name, COUNT(p), SUM(p.stock) FROM Product p GROUP BY p.category";
        List<Object[]> groupResults = session.createQuery(hql4).list();
        System.out.println("\n按分类统计:");
        for (Object[] row : groupResults) {
            System.out.println("  分类: " + row[0] + ", 数量: " + row[1] + ", 库存: " + row[2]);
        }

        session.close();
        sessionFactory.close();
    }

    private static void joinQueryDemo() {
        System.out.println("\n--- 6. 关联查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "SELECT p.name, c.name FROM Product p JOIN p.category c";
        List<Object[]> results1 = session.createQuery(hql1).list();
        System.out.println("内连接（产品-分类）:");
        for (Object[] row : results1) {
            System.out.println("  产品: " + row[0] + ", 分类: " + row[1]);
        }

        String hql2 = "FROM Product p LEFT JOIN FETCH p.category";
        List<Product> products = session.createQuery(hql2, Product.class).list();
        System.out.println("\n左连接（加载分类）:");
        for (Product p : products) {
            System.out.println("  产品: " + p.getName() + ", 分类: " + p.getCategory().getName());
        }

        session.close();
        sessionFactory.close();
    }

    private static void subqueryDemo() {
        System.out.println("\n--- 7. 子查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Product p WHERE p.price > (SELECT AVG(p2.price) FROM Product p2)";
        List<Product> products1 = session.createQuery(hql1, Product.class).list();
        System.out.println("价格高于平均价格的产品:");
        for (Product p : products1) {
            System.out.println("  " + p.getName() + " - " + p.getPrice());
        }

        String hql2 = "FROM Product p WHERE EXISTS (SELECT 1 FROM Category c WHERE c = p.category AND c.name = '电子产品')";
        List<Product> products2 = session.createQuery(hql2, Product.class).list();
        System.out.println("\nEXISTS查询（电子产品），数量: " + products2.size());

        session.close();
        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Product.class);
        config.addAnnotatedClass(Category.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "products_hql")
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

    @ManyToOne
    @JoinColumn(name = "category_id")
    private Category category;

    public Product() {
    }

    public Product(String name, Double price, Integer stock, Category category) {
        this.name = name;
        this.price = price;
        this.stock = stock;
        this.category = category;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
    public Integer getStock() { return stock; }
    public void setStock(Integer stock) { this.stock = stock; }
    public Category getCategory() { return category; }
    public void setCategory(Category category) { this.category = category; }
}

@Entity
@Table(name = "categories_hql")
class Category {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @OneToMany(mappedBy = "category")
    private List<Product> products;

    public Category() {
    }

    public Category(String name) {
        this.name = name;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Product> getProducts() { return products; }
    public void setProducts(List<Product> products) { this.products = products; }
}
