package com.example.hibernate.criteria;

import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.criterion.*;

import java.util.List;

public class CriteriaDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate Criteria API示例 ===");

        try {
            initializeData();
            
            basicCriteriaDemo();
            conditionalCriteriaDemo();
            sortingDemo();
            paginationDemo();
            projectionDemo();
            joinCriteriaDemo();
            dynamicQueryDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void initializeData() {
        System.out.println("\n--- 初始化数据 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Supplier s1 = new Supplier("Apple Inc.");
        Supplier s2 = new Supplier("Samsung Electronics");

        Item i1 = new Item("MacBook Pro", 1999.99, 50, s1);
        Item i2 = new Item("iPhone 15", 999.99, 200, s1);
        Item i3 = new Item("iPad", 799.99, 150, s1);
        Item i4 = new Item("Galaxy S24", 899.99, 180, s2);
        Item i5 = new Item("Galaxy Tab", 599.99, 120, s2);

        session.save(s1);
        session.save(s2);
        session.save(i1);
        session.save(i2);
        session.save(i3);
        session.save(i4);
        session.save(i5);

        tx.commit();
        session.close();
        sessionFactory.close();

        System.out.println("数据初始化完成");
    }

    @SuppressWarnings("deprecation")
    private static void basicCriteriaDemo() {
        System.out.println("\n--- 1. 基本查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Item.class);
        List<Item> items1 = criteria1.list();
        System.out.println("查询所有商品，数量: " + items1.size());

        Criteria criteria2 = session.createCriteria(Item.class);
        Item item = (Item) criteria2.add(Restrictions.idEq(1L)).uniqueResult();
        if (item != null) {
            System.out.println("查询ID为1的商品: " + item.getName());
        }

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void conditionalCriteriaDemo() {
        System.out.println("\n--- 2. 条件查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Item.class)
                .add(Restrictions.gt("price", 1000.0));
        List<Item> items1 = criteria1.list();
        System.out.println("价格大于1000的商品，数量: " + items1.size());

        Criteria criteria2 = session.createCriteria(Item.class)
                .add(Restrictions.like("name", "i%"));
        List<Item> items2 = criteria2.list();
        System.out.println("名称以i开头的商品，数量: " + items2.size());

        Criteria criteria3 = session.createCriteria(Item.class)
                .add(Restrictions.between("price", 500.0, 1500.0))
                .add(Restrictions.gt("stock", 100));
        List<Item> items3 = criteria3.list();
        System.out.println("价格在500-1500且库存大于100的商品，数量: " + items3.size());

        Criteria criteria4 = session.createCriteria(Item.class)
                .add(Restrictions.or(
                        Restrictions.lt("price", 800.0),
                        Restrictions.gt("stock", 150)
                ));
        List<Item> items4 = criteria4.list();
        System.out.println("价格小于800或库存大于150的商品，数量: " + items4.size());

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void sortingDemo() {
        System.out.println("\n--- 3. 排序 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Item.class)
                .addOrder(Order.asc("price"));
        List<Item> items1 = criteria1.list();
        System.out.println("按价格升序排列:");
        for (Item i : items1) {
            System.out.println("  " + i.getName() + " - " + i.getPrice());
        }

        Criteria criteria2 = session.createCriteria(Item.class)
                .addOrder(Order.desc("price"))
                .addOrder(Order.asc("name"));
        List<Item> items2 = criteria2.list();
        System.out.println("\n按价格降序、名称升序排列:");
        for (Item i : items2) {
            System.out.println("  " + i.getName() + " - " + i.getPrice());
        }

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void paginationDemo() {
        System.out.println("\n--- 4. 分页查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        int pageSize = 2;
        int pageNum = 1;

        Criteria criteria = session.createCriteria(Item.class)
                .addOrder(Order.asc("price"))
                .setFirstResult((pageNum - 1) * pageSize)
                .setMaxResults(pageSize);
        List<Item> page1 = criteria.list();
        System.out.println("第1页:");
        for (Item i : page1) {
            System.out.println("  " + i.getName());
        }

        pageNum = 2;
        criteria.setFirstResult((pageNum - 1) * pageSize)
                .setMaxResults(pageSize);
        List<Item> page2 = criteria.list();
        System.out.println("\n第2页:");
        for (Item i : page2) {
            System.out.println("  " + i.getName());
        }

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void projectionDemo() {
        System.out.println("\n--- 5. 投影与聚合 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Item.class)
                .setProjection(Projections.rowCount());
        Long count = (Long) criteria1.uniqueResult();
        System.out.println("商品总数: " + count);

        Criteria criteria2 = session.createCriteria(Item.class)
                .setProjection(Projections.avg("price"));
        Double avgPrice = (Double) criteria2.uniqueResult();
        System.out.println("平均价格: " + String.format("%.2f", avgPrice));

        Criteria criteria3 = session.createCriteria(Item.class)
                .setProjection(Projections.projectionList()
                        .add(Projections.max("price"))
                        .add(Projections.min("price"))
                        .add(Projections.sum("stock")));
        Object[] result = (Object[]) criteria3.uniqueResult();
        System.out.println("最高价格: " + result[0] + ", 最低价格: " + result[1] + ", 总库存: " + result[2]);

        Criteria criteria4 = session.createCriteria(Item.class)
                .createAlias("supplier", "s")
                .setProjection(Projections.projectionList()
                        .add(Projections.groupProperty("s.name"))
                        .add(Projections.count("id"))
                        .add(Projections.sum("stock")));
        List<Object[]> groupResults = criteria4.list();
        System.out.println("\n按供应商统计:");
        for (Object[] row : groupResults) {
            System.out.println("  供应商: " + row[0] + ", 商品数: " + row[1] + ", 总库存: " + row[2]);
        }

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void joinCriteriaDemo() {
        System.out.println("\n--- 6. 关联查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        Criteria criteria1 = session.createCriteria(Item.class, "item")
                .createAlias("item.supplier", "supplier")
                .add(Restrictions.eq("supplier.name", "Apple Inc."));
        List<Item> items1 = criteria1.list();
        System.out.println("Apple的商品，数量: " + items1.size());
        for (Item i : items1) {
            System.out.println("  " + i.getName());
        }

        Criteria criteria2 = session.createCriteria(Item.class, "item")
                .createCriteria("item.supplier", "supplier", Criteria.LEFT_JOIN)
                .add(Restrictions.gt("item.price", 800.0));
        List<Item> items2 = criteria2.list();
        System.out.println("\n价格大于800的商品（左连接），数量: " + items2.size());

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static void dynamicQueryDemo() {
        System.out.println("\n--- 7. 动态查询 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        List<Item> results = searchItems(session, "i", null, null, null);
        System.out.println("动态查询结果（名称含i），数量: " + results.size());

        List<Item> results2 = searchItems(session, null, 500.0, 1500.0, null);
        System.out.println("动态查询结果（价格500-1500），数量: " + results2.size());

        session.close();
        sessionFactory.close();
    }

    @SuppressWarnings("deprecation")
    private static List<Item> searchItems(Session session, String name, Double minPrice, Double maxPrice, Long supplierId) {
        Criteria criteria = session.createCriteria(Item.class);

        if (name != null && !name.isEmpty()) {
            criteria.add(Restrictions.like("name", "%" + name + "%"));
        }

        if (minPrice != null) {
            criteria.add(Restrictions.ge("price", minPrice));
        }

        if (maxPrice != null) {
            criteria.add(Restrictions.le("price", maxPrice));
        }

        if (supplierId != null) {
            criteria.createAlias("supplier", "s")
                    .add(Restrictions.eq("s.id", supplierId));
        }

        return criteria.list();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Item.class);
        config.addAnnotatedClass(Supplier.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "items_criteria")
class Item {

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
    @JoinColumn(name = "supplier_id")
    private Supplier supplier;

    public Item() {
    }

    public Item(String name, Double price, Integer stock, Supplier supplier) {
        this.name = name;
        this.price = price;
        this.stock = stock;
        this.supplier = supplier;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
    public Integer getStock() { return stock; }
    public void setStock(Integer stock) { this.stock = stock; }
    public Supplier getSupplier() { return supplier; }
    public void setSupplier(Supplier supplier) { this.supplier = supplier; }
}

@Entity
@Table(name = "suppliers_criteria")
class Supplier {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @OneToMany(mappedBy = "supplier")
    private List<Item> items;

    public Supplier() {
    }

    public Supplier(String name) {
        this.name = name;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Item> getItems() { return items; }
    public void setItems(List<Item> items) { this.items = items; }
}
