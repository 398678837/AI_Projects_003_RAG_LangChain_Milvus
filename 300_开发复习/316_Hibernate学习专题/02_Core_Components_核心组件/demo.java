package com.example.hibernate.core;

import org.hibernate.*;
import org.hibernate.cfg.Configuration;
import org.hibernate.criterion.Restrictions;

import java.util.List;
import java.util.Properties;

public class CoreComponentsDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate核心组件示例 ===");

        try {
            configurationDemo();
            sessionFactoryDemo();
            sessionDemo();
            transactionDemo();
            queryDemo();
            criteriaDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void configurationDemo() {
        System.out.println("\n--- 1. Configuration示例 ---");

        Configuration config1 = new Configuration();
        config1.configure("hibernate.cfg.xml");
        System.out.println("方式1: 使用hibernate.cfg.xml配置");

        Configuration config2 = new Configuration();
        Properties props = new Properties();
        props.setProperty("hibernate.dialect", "org.hibernate.dialect.MySQL8Dialect");
        props.setProperty("hibernate.connection.driver_class", "com.mysql.cj.jdbc.Driver");
        props.setProperty("hibernate.connection.url", "jdbc:mysql://localhost:3306/hibernate_demo");
        props.setProperty("hibernate.connection.username", "root");
        props.setProperty("hibernate.connection.password", "password");
        config2.setProperties(props);
        config2.addAnnotatedClass(Product.class);
        System.out.println("方式2: 使用Properties配置");
    }

    private static void sessionFactoryDemo() {
        System.out.println("\n--- 2. SessionFactory示例 ---");

        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Product.class);

        SessionFactory sessionFactory = config.buildSessionFactory();
        System.out.println("SessionFactory创建成功");
        System.out.println("SessionFactory是线程安全的，可以在多线程环境中使用");

        sessionFactory.close();
        System.out.println("SessionFactory已关闭");
    }

    private static void sessionDemo() {
        System.out.println("\n--- 3. Session示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session1 = sessionFactory.openSession();
        System.out.println("openSession(): 创建新的Session");

        session1.beginTransaction();
        Product product1 = new Product("iPhone", 999.99);
        session1.save(product1);
        session1.getTransaction().commit();

        Product product2 = session1.get(Product.class, product1.getId());
        System.out.println("从数据库获取产品: " + product2.getName());

        Product product3 = session1.get(Product.class, product1.getId());
        System.out.println("再次获取同一产品（一级缓存）: " + (product2 == product3));

        session1.close();
        System.out.println("Session已关闭");

        Session session2 = sessionFactory.openSession();
        Product product4 = session2.get(Product.class, product1.getId());
        System.out.println("新Session获取产品: " + product4.getName());
        session2.close();

        sessionFactory.close();
    }

    private static void transactionDemo() {
        System.out.println("\n--- 4. Transaction示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();
            System.out.println("事务开始");

            Product product1 = new Product("MacBook", 1999.99);
            session.save(product1);
            System.out.println("保存产品1");

            Product product2 = new Product("iPad", 799.99);
            session.save(product2);
            System.out.println("保存产品2");

            tx.commit();
            System.out.println("事务提交成功");
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

    private static void queryDemo() {
        System.out.println("\n--- 5. Query示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Product";
        List<Product> products1 = session.createQuery(hql1, Product.class).list();
        System.out.println("查询所有产品，数量: " + products1.size());

        String hql2 = "FROM Product p WHERE p.price > :minPrice";
        List<Product> products2 = session.createQuery(hql2, Product.class)
                .setParameter("minPrice", 1000.0)
                .list();
        System.out.println("价格大于1000的产品，数量: " + products2.size());

        String hql3 = "FROM Product p ORDER BY p.price DESC";
        List<Product> products3 = session.createQuery(hql3, Product.class)
                .setFirstResult(0)
                .setMaxResults(5)
                .list();
        System.out.println("分页查询（前5条），数量: " + products3.size());

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void criteriaDemo() {
        System.out.println("\n--- 6. Criteria示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Product.class);
        List<Product> products1 = criteria1.list();
        System.out.println("Criteria查询所有产品，数量: " + products1.size());

        Criteria criteria2 = session.createCriteria(Product.class)
                .add(Restrictions.gt("price", 500.0))
                .add(Restrictions.like("name", "i%"));
        List<Product> products2 = criteria2.list();
        System.out.println("Criteria条件查询，数量: " + products2.size());

        session.close();
        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Product.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "products")
class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "price", nullable = false)
    private Double price;

    public Product() {
    }

    public Product(String name, Double price) {
        this.name = name;
        this.price = price;
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

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }
}
