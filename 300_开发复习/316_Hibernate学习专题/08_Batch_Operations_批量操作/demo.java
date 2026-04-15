package com.example.hibernate.batch;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.StatelessSession;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

import java.util.List;

public class BatchDemo {

    private static final int BATCH_SIZE = 20;

    public static void main(String[] args) {
        System.out.println("=== Hibernate批量操作示例 ===");

        try {
            batchInsertDemo();
            statelessSessionDemo();
            batchUpdateDemo();
            batchDeleteDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void batchInsertDemo() {
        System.out.println("\n--- 1. 批量插入演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        long start = System.currentTimeMillis();

        for (int i = 1; i <= 100; i++) {
            Customer customer = new Customer("客户" + i, "customer" + i + "@example.com", "1380000" + String.format("%04d", i));
            session.save(customer);

            if (i % BATCH_SIZE == 0) {
                session.flush();
                session.clear();
                System.out.println("已插入 " + i + " 条记录");
            }
        }

        tx.commit();
        session.close();

        long end = System.currentTimeMillis();
        System.out.println("批量插入完成，耗时: " + (end - start) + "ms");

        sessionFactory.close();
    }

    private static void statelessSessionDemo() {
        System.out.println("\n--- 2. StatelessSession批量插入演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        StatelessSession session = sessionFactory.openStatelessSession();
        Transaction tx = session.beginTransaction();

        long start = System.currentTimeMillis();

        for (int i = 101; i <= 200; i++) {
            Customer customer = new Customer("客户" + i, "customer" + i + "@example.com", "1380000" + String.format("%04d", i));
            session.insert(customer);
        }

        tx.commit();
        session.close();

        long end = System.currentTimeMillis();
        System.out.println("StatelessSession批量插入完成，耗时: " + (end - start) + "ms");

        sessionFactory.close();
    }

    private static void batchUpdateDemo() {
        System.out.println("\n--- 3. 批量更新演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        String hql = "UPDATE Customer c SET c.status = :status WHERE c.id BETWEEN :startId AND :endId";
        Query query = session.createQuery(hql);
        query.setParameter("status", "VIP");
        query.setParameter("startId", 1L);
        query.setParameter("endId", 50L);

        int updatedCount = query.executeUpdate();
        System.out.println("批量更新了 " + updatedCount + " 条记录");

        tx.commit();

        Query checkQuery = session.createQuery("FROM Customer c WHERE c.status = :status", Customer.class);
        checkQuery.setParameter("status", "VIP");
        List<Customer> vipCustomers = checkQuery.list();
        System.out.println("VIP客户数量: " + vipCustomers.size());

        session.close();
        sessionFactory.close();
    }

    private static void batchDeleteDemo() {
        System.out.println("\n--- 4. 批量删除演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        String hql = "DELETE FROM Customer c WHERE c.id > :maxId";
        Query query = session.createQuery(hql);
        query.setParameter("maxId", 100L);

        int deletedCount = query.executeUpdate();
        System.out.println("批量删除了 " + deletedCount + " 条记录");

        tx.commit();

        Query countQuery = session.createQuery("SELECT COUNT(c) FROM Customer c", Long.class);
        Long count = countQuery.uniqueResult();
        System.out.println("剩余客户数量: " + count);

        session.close();
        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Customer.class);
        config.setProperty("hibernate.jdbc.batch_size", String.valueOf(BATCH_SIZE));
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "customers_batch")
class Customer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "email")
    private String email;

    @Column(name = "phone")
    private String phone;

    @Column(name = "status")
    private String status = "NORMAL";

    public Customer() {
    }

    public Customer(String name, String email, String phone) {
        this.name = name;
        this.email = email;
        this.phone = phone;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
