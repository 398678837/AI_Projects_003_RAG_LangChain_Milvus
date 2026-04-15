package com.example.hibernate.cache;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

import java.util.List;

public class CacheDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate缓存示例 ===");

        try {
            initializeData();
            
            firstLevelCacheDemo();
            firstLevelCacheEvictDemo();
            secondLevelCacheDemo();
            queryCacheDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void initializeData() {
        System.out.println("\n--- 初始化数据 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Book b1 = new Book("Java编程思想", "Bruce Eckel", 108.00);
        Book b2 = new Book("Effective Java", "Joshua Bloch", 99.00);
        Book b3 = new Book("Hibernate实战", "Christian Bauer", 89.00);

        session.save(b1);
        session.save(b2);
        session.save(b3);

        tx.commit();
        session.close();
        sessionFactory.close();

        System.out.println("数据初始化完成");
    }

    private static void firstLevelCacheDemo() {
        System.out.println("\n--- 1. 一级缓存演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Book book1 = session.get(Book.class, 1L);
        System.out.println("第一次查询: " + book1.getTitle());

        Book book2 = session.get(Book.class, 1L);
        System.out.println("第二次查询（一级缓存）: " + book2.getTitle());

        System.out.println("是否是同一个对象: " + (book1 == book2));

        boolean contains = session.contains(book1);
        System.out.println("是否在一级缓存中: " + contains);

        session.close();
        sessionFactory.close();
    }

    private static void firstLevelCacheEvictDemo() {
        System.out.println("\n--- 2. 一级缓存清除演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Book book1 = session.get(Book.class, 1L);
        System.out.println("第一次查询: " + book1.getTitle());
        System.out.println("是否在缓存中: " + session.contains(book1));

        session.evict(book1);
        System.out.println("调用evict()后，是否在缓存中: " + session.contains(book1));

        Book book2 = session.get(Book.class, 1L);
        System.out.println("再次查询: " + book2.getTitle());
        System.out.println("是否是同一个对象: " + (book1 == book2));

        session.close();
        sessionFactory.close();

        Session session2 = sessionFactory.openSession();
        Book book3 = session2.get(Book.class, 1L);
        System.out.println("\n新Session查询: " + book3.getTitle());
        session2.close();

        sessionFactory.close();
    }

    private static void secondLevelCacheDemo() {
        System.out.println("\n--- 3. 二级缓存演示 ---");

        SessionFactory sessionFactory = createSessionFactory();

        Session session1 = sessionFactory.openSession();
        Book book1 = session1.get(Book.class, 1L);
        System.out.println("Session1查询: " + book1.getTitle());
        session1.close();

        Session session2 = sessionFactory.openSession();
        Book book2 = session2.get(Book.class, 1L);
        System.out.println("Session2查询（二级缓存）: " + book2.getTitle());
        session2.close();

        sessionFactory.close();
    }

    private static void queryCacheDemo() {
        System.out.println("\n--- 4. 查询缓存演示 ---");

        SessionFactory sessionFactory = createSessionFactory();

        Session session1 = sessionFactory.openSession();
        String hql = "FROM Book b WHERE b.price > 50";
        Query<Book> query1 = session1.createQuery(hql, Book.class);
        query1.setCacheable(true);
        query1.setCacheRegion("bookCache");

        long start1 = System.currentTimeMillis();
        List<Book> books1 = query1.list();
        long end1 = System.currentTimeMillis();
        System.out.println("第一次查询，耗时: " + (end1 - start1) + "ms，数量: " + books1.size());
        session1.close();

        Session session2 = sessionFactory.openSession();
        Query<Book> query2 = session2.createQuery(hql, Book.class);
        query2.setCacheable(true);
        query2.setCacheRegion("bookCache");

        long start2 = System.currentTimeMillis();
        List<Book> books2 = query2.list();
        long end2 = System.currentTimeMillis();
        System.out.println("第二次查询（查询缓存），耗时: " + (end2 - start2) + "ms，数量: " + books2.size());
        session2.close();

        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Book.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "books_cache")
@Cacheable
@org.hibernate.annotations.Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "title")
    private String title;

    @Column(name = "author")
    private String author;

    @Column(name = "price")
    private Double price;

    public Book() {
    }

    public Book(String title, String author, Double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getAuthor() { return author; }
    public void setAuthor(String author) { this.author = author; }
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
}
