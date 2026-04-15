package com.example.hibernate.performance;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

import java.util.ArrayList;
import java.util.List;

public class PerformanceDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate性能优化示例 ===");

        try {
            initializeData();
            
            nPlusOneProblemDemo();
            joinFetchDemo();
            batchSizeDemo();
            projectionDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void initializeData() {
        System.out.println("\n--- 初始化数据 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        for (int i = 1; i <= 5; i++) {
            Department dept = new Department("部门" + i);
            session.save(dept);

            for (int j = 1; j <= 3; j++) {
                Employee emp = new Employee("员工" + i + "-" + j, dept);
                session.save(emp);
            }
        }

        tx.commit();
        session.close();
        sessionFactory.close();

        System.out.println("数据初始化完成");
    }

    private static void nPlusOneProblemDemo() {
        System.out.println("\n--- 1. N+1查询问题演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql = "FROM Department";
        List<Department> departments = session.createQuery(hql, Department.class).list();

        System.out.println("查询部门数量: " + departments.size());
        System.out.println("遍历部门，获取员工（N+1查询）:");

        for (Department dept : departments) {
            System.out.println("  部门: " + dept.getName() + ", 员工数: " + dept.getEmployees().size());
        }

        session.close();
        sessionFactory.close();
    }

    private static void joinFetchDemo() {
        System.out.println("\n--- 2. JOIN FETCH优化演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql = "FROM Department d LEFT JOIN FETCH d.employees";
        List<Department> departments = session.createQuery(hql, Department.class).list();

        System.out.println("使用JOIN FETCH查询部门数量: " + departments.size());
        System.out.println("遍历部门，获取员工（1次查询）:");

        for (Department dept : departments) {
            System.out.println("  部门: " + dept.getName() + ", 员工数: " + dept.getEmployees().size());
        }

        session.close();
        sessionFactory.close();
    }

    private static void batchSizeDemo() {
        System.out.println("\n--- 3. @BatchSize优化演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql = "FROM Department";
        List<Department> departments = session.createQuery(hql, Department.class).list();

        System.out.println("使用@BatchSize查询部门数量: " + departments.size());
        System.out.println("遍历部门，获取员工（批量加载）:");

        for (Department dept : departments) {
            System.out.println("  部门: " + dept.getName() + ", 员工数: " + dept.getEmployees().size());
        }

        session.close();
        sessionFactory.close();
    }

    private static void projectionDemo() {
        System.out.println("\n--- 4. 投影查询演示 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();

        String hql1 = "FROM Employee";
        long start1 = System.currentTimeMillis();
        List<Employee> employees = session.createQuery(hql1, Employee.class).list();
        long end1 = System.currentTimeMillis();
        System.out.println("查询所有字段，耗时: " + (end1 - start1) + "ms，数量: " + employees.size());

        String hql2 = "SELECT e.id, e.name FROM Employee e";
        long start2 = System.currentTimeMillis();
        List<Object[]> projections = session.createQuery(hql2).list();
        long end2 = System.currentTimeMillis();
        System.out.println("投影查询（只查id和name），耗时: " + (end2 - start2) + "ms，数量: " + projections.size());

        String hql3 = "SELECT new com.example.hibernate.performance.EmployeeDTO(e.id, e.name) FROM Employee e";
        long start3 = System.currentTimeMillis();
        List<EmployeeDTO> dtos = session.createQuery(hql3, EmployeeDTO.class).list();
        long end3 = System.currentTimeMillis();
        System.out.println("DTO投影查询，耗时: " + (end3 - start3) + "ms，数量: " + dtos.size());

        session.close();
        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Department.class);
        config.addAnnotatedClass(Employee.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "depts_perf")
class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @OneToMany(mappedBy = "department", fetch = FetchType.LAZY)
    @org.hibernate.annotations.BatchSize(size = 10)
    private List<Employee> employees = new ArrayList<>();

    public Department() {
    }

    public Department(String name) {
        this.name = name;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Employee> getEmployees() { return employees; }
    public void setEmployees(List<Employee> employees) { this.employees = employees; }
}

@Entity
@Table(name = "emps_perf")
class Employee {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "department_id")
    private Department department;

    public Employee() {
    }

    public Employee(String name, Department department) {
        this.name = name;
        this.department = department;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Department getDepartment() { return department; }
    public void setDepartment(Department department) { this.department = department; }
}

class EmployeeDTO {
    private Long id;
    private String name;

    public EmployeeDTO(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
