package com.example.hibernate.basic;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class HibernateBasicDemo {

    private static SessionFactory sessionFactory;

    public static void main(String[] args) {
        System.out.println("=== Hibernate基础概念示例 ===");

        try {
            initializeSessionFactory();
            
            createUser();
            getUser();
            updateUser();
            getAllUsers();
            deleteUser();
            
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (sessionFactory != null) {
                sessionFactory.close();
            }
        }
    }

    private static void initializeSessionFactory() {
        System.out.println("\n--- 1. 初始化SessionFactory ---");
        try {
            Configuration configuration = new Configuration();
            configuration.configure("hibernate.cfg.xml");
            configuration.addAnnotatedClass(User.class);
            
            sessionFactory = configuration.buildSessionFactory();
            System.out.println("SessionFactory初始化成功");
        } catch (Exception e) {
            System.err.println("SessionFactory初始化失败: " + e.getMessage());
            throw e;
        }
    }

    private static void createUser() {
        System.out.println("\n--- 2. 创建用户 ---");
        Session session = sessionFactory.openSession();
        Transaction transaction = null;

        try {
            transaction = session.beginTransaction();

            User user = new User();
            user.setName("张三");
            user.setEmail("zhangsan@example.com");
            user.setAge(25);

            session.save(user);
            transaction.commit();

            System.out.println("用户创建成功，ID: " + user.getId());
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            System.err.println("创建用户失败: " + e.getMessage());
        } finally {
            session.close();
        }
    }

    private static void getUser() {
        System.out.println("\n--- 3. 查询用户 ---");
        Session session = sessionFactory.openSession();

        try {
            User user = session.get(User.class, 1L);
            if (user != null) {
                System.out.println("查询到用户: ");
                System.out.println("  ID: " + user.getId());
                System.out.println("  姓名: " + user.getName());
                System.out.println("  邮箱: " + user.getEmail());
                System.out.println("  年龄: " + user.getAge());
            } else {
                System.out.println("未找到用户");
            }
        } catch (Exception e) {
            System.err.println("查询用户失败: " + e.getMessage());
        } finally {
            session.close();
        }
    }

    private static void updateUser() {
        System.out.println("\n--- 4. 更新用户 ---");
        Session session = sessionFactory.openSession();
        Transaction transaction = null;

        try {
            transaction = session.beginTransaction();

            User user = session.get(User.class, 1L);
            if (user != null) {
                user.setAge(26);
                user.setEmail("zhangsan_new@example.com");
                session.update(user);
                transaction.commit();
                System.out.println("用户更新成功");
            }
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            System.err.println("更新用户失败: " + e.getMessage());
        } finally {
            session.close();
        }
    }

    private static void getAllUsers() {
        System.out.println("\n--- 5. 查询所有用户 ---");
        Session session = sessionFactory.openSession();

        try {
            String hql = "FROM User";
            List<User> users = session.createQuery(hql, User.class).list();

            System.out.println("用户列表:");
            for (User user : users) {
                System.out.println("  - " + user.getName() + " (" + user.getEmail() + ")");
            }
        } catch (Exception e) {
            System.err.println("查询用户列表失败: " + e.getMessage());
        } finally {
            session.close();
        }
    }

    private static void deleteUser() {
        System.out.println("\n--- 6. 删除用户 ---");
        Session session = sessionFactory.openSession();
        Transaction transaction = null;

        try {
            transaction = session.beginTransaction();

            User user = session.get(User.class, 1L);
            if (user != null) {
                session.delete(user);
                transaction.commit();
                System.out.println("用户删除成功");
            }
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            System.err.println("删除用户失败: " + e.getMessage());
        } finally {
            session.close();
        }
    }
}

@Entity
@Table(name = "users")
class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "email", unique = true, nullable = false)
    private String email;

    @Column(name = "age")
    private Integer age;

    public User() {
    }

    public User(String name, String email, Integer age) {
        this.name = name;
        this.email = email;
        this.age = age;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}
