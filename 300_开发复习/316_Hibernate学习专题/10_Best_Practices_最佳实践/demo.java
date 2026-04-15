package com.example.hibernate.bestpractice;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.Objects;

public class BestPracticeDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate最佳实践示例 ===");

        try {
            entityDesignDemo();
            equalsHashCodeDemo();
            cascadeDemo();
            resourceManagementDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void entityDesignDemo() {
        System.out.println("\n--- 1. 实体类设计演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        User user = new User("张三", "zhangsan@example.com");
        session.save(user);

        Address address = new Address("北京市", "朝阳区", "100000");
        address.setUser(user);
        user.getAddresses().add(address);
        session.save(address);

        tx.commit();

        User savedUser = session.get(User.class, user.getId());
        System.out.println("用户: " + savedUser.getName());
        System.out.println("邮箱: " + savedUser.getEmail());
        System.out.println("地址数量: " + savedUser.getAddresses().size());

        session.close();
        sessionFactory.close();
    }

    private static void equalsHashCodeDemo() {
        System.out.println("\n--- 2. equals()和hashCode()演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        User user1 = new User("李四", "lisi@example.com");
        session.save(user1);
        tx.commit();

        User user2 = session.get(User.class, user1.getId());

        System.out.println("user1 == user2: " + (user1 == user2));
        System.out.println("user1.equals(user2): " + user1.equals(user2));
        System.out.println("user1.hashCode() == user2.hashCode(): " + (user1.hashCode() == user2.hashCode()));

        User user3 = new User("王五", "wangwu@example.com");
        System.out.println("\nuser1.equals(user3): " + user1.equals(user3));

        session.close();
        sessionFactory.close();
    }

    private static void cascadeDemo() {
        System.out.println("\n--- 3. 级联操作演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Order order = new Order("ORD001");

        OrderItem item1 = new OrderItem("商品A", 2, 100.0);
        OrderItem item2 = new OrderItem("商品B", 1, 200.0);

        order.addItem(item1);
        order.addItem(item2);

        session.save(order);
        tx.commit();
        System.out.println("级联保存订单和订单项");

        session.clear();

        Order savedOrder = session.get(Order.class, order.getId());
        System.out.println("订单号: " + savedOrder.getOrderNo());
        System.out.println("订单项数量: " + savedOrder.getItems().size());

        tx = session.beginTransaction();
        session.delete(savedOrder);
        tx.commit();
        System.out.println("级联删除订单和订单项");

        session.close();
        sessionFactory.close();
    }

    private static void resourceManagementDemo() {
        System.out.println("\n--- 4. 资源管理演示 ---");

        SessionFactory sessionFactory = null;
        Session session = null;
        Transaction tx = null;

        try {
            sessionFactory = createSessionFactory();
            session = sessionFactory.openSession();
            tx = session.beginTransaction();

            User user = new User("赵六", "zhaoliu@example.com");
            session.save(user);

            tx.commit();
            System.out.println("操作成功");

        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
                System.out.println("事务回滚: " + e.getMessage());
            }
            throw e;
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
            if (sessionFactory != null && !sessionFactory.isClosed()) {
                sessionFactory.close();
            }
            System.out.println("资源已释放");
        }
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(User.class);
        config.addAnnotatedClass(Address.class);
        config.addAnnotatedClass(Order.class);
        config.addAnnotatedClass(OrderItem.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "users_bp")
class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "email", unique = true, nullable = false)
    private String email;

    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Address> addresses = new ArrayList<>();

    public User() {
    }

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public List<Address> getAddresses() { return addresses; }
    public void setAddresses(List<Address> addresses) { this.addresses = addresses; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(email, user.email);
    }

    @Override
    public int hashCode() {
        return Objects.hash(email);
    }
}

@Entity
@Table(name = "addresses_bp")
class Address {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "city")
    private String city;

    @Column(name = "district")
    private String district;

    @Column(name = "zip_code")
    private String zipCode;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;

    public Address() {
    }

    public Address(String city, String district, String zipCode) {
        this.city = city;
        this.district = district;
        this.zipCode = zipCode;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    public String getDistrict() { return district; }
    public void setDistrict(String district) { this.district = district; }
    public String getZipCode() { return zipCode; }
    public void setZipCode(String zipCode) { this.zipCode = zipCode; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
}

@Entity
@Table(name = "orders_bp")
class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "order_no", unique = true)
    private String orderNo;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<OrderItem> items = new ArrayList<>();

    public Order() {
    }

    public Order(String orderNo) {
        this.orderNo = orderNo;
    }

    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }

    public void removeItem(OrderItem item) {
        items.remove(item);
        item.setOrder(null);
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getOrderNo() { return orderNo; }
    public void setOrderNo(String orderNo) { this.orderNo = orderNo; }
    public List<OrderItem> getItems() { return items; }
    public void setItems(List<OrderItem> items) { this.items = items; }
}

@Entity
@Table(name = "order_items_bp")
class OrderItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "product_name")
    private String productName;

    @Column(name = "quantity")
    private Integer quantity;

    @Column(name = "price")
    private Double price;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id")
    private Order order;

    public OrderItem() {
    }

    public OrderItem(String productName, Integer quantity, Double price) {
        this.productName = productName;
        this.quantity = quantity;
        this.price = price;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getProductName() { return productName; }
    public void setProductName(String productName) { this.productName = productName; }
    public Integer getQuantity() { return quantity; }
    public void setQuantity(Integer quantity) { this.quantity = quantity; }
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
    public Order getOrder() { return order; }
    public void setOrder(Order order) { this.order = order; }
}
