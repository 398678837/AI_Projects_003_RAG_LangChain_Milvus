package com.example.hibernate.mapping;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class EntityMappingDemo {

    public static void main(String[] args) {
        System.out.println("=== Hibernate实体映射示例 ===");

        try {
            basicMappingDemo();
            oneToManyDemo();
            manyToManyDemo();
            inheritanceDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void basicMappingDemo() {
        System.out.println("\n--- 1. 基本映射示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Employee employee = new Employee();
        employee.setName("李四");
        employee.setEmail("lisi@example.com");
        employee.setBirthDate(new Date());
        employee.setStatus(EmployeeStatus.ACTIVE);
        employee.setDescription("这是一个详细的描述信息");

        session.save(employee);
        tx.commit();

        Employee savedEmployee = session.get(Employee.class, employee.getId());
        System.out.println("员工姓名: " + savedEmployee.getName());
        System.out.println("员工邮箱: " + savedEmployee.getEmail());
        System.out.println("员工状态: " + savedEmployee.getStatus());

        session.close();
        sessionFactory.close();
    }

    private static void oneToManyDemo() {
        System.out.println("\n--- 2. 一对多关系示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Department department = new Department();
        department.setName("技术部");

        Employee emp1 = new Employee();
        emp1.setName("王五");
        emp1.setEmail("wangwu@example.com");
        emp1.setDepartment(department);

        Employee emp2 = new Employee();
        emp2.setName("赵六");
        emp2.setEmail("zhaoliu@example.com");
        emp2.setDepartment(department);

        department.getEmployees().add(emp1);
        department.getEmployees().add(emp2);

        session.save(department);
        session.save(emp1);
        session.save(emp2);

        tx.commit();

        Department savedDept = session.get(Department.class, department.getId());
        System.out.println("部门: " + savedDept.getName());
        System.out.println("员工数量: " + savedDept.getEmployees().size());
        for (Employee emp : savedDept.getEmployees()) {
            System.out.println("  - " + emp.getName());
        }

        session.close();
        sessionFactory.close();
    }

    private static void manyToManyDemo() {
        System.out.println("\n--- 3. 多对多关系示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Course course1 = new Course();
        course1.setName("Java编程");

        Course course2 = new Course();
        course2.setName("数据库原理");

        Student student1 = new Student();
        student1.setName("小明");
        student1.getCourses().add(course1);
        student1.getCourses().add(course2);

        Student student2 = new Student();
        student2.setName("小红");
        student2.getCourses().add(course1);

        course1.getStudents().add(student1);
        course1.getStudents().add(student2);
        course2.getStudents().add(student1);

        session.save(course1);
        session.save(course2);
        session.save(student1);
        session.save(student2);

        tx.commit();

        Student savedStudent = session.get(Student.class, student1.getId());
        System.out.println("学生: " + savedStudent.getName());
        System.out.println("选修课程:");
        for (Course course : savedStudent.getCourses()) {
            System.out.println("  - " + course.getName());
        }

        session.close();
        sessionFactory.close();
    }

    private static void inheritanceDemo() {
        System.out.println("\n--- 4. 继承映射示例 ---");

        SessionFactory sessionFactory = createSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Car car = new Car();
        car.setBrand("Tesla");
        car.setModel("Model 3");
        car.setDoorCount(4);

        Bike bike = new Bike();
        bike.setBrand("Giant");
        bike.setModel("Escape 1");
        bike.setHasGear(true);

        session.save(car);
        session.save(bike);

        tx.commit();

        List<Vehicle> vehicles = session.createQuery("FROM Vehicle", Vehicle.class).list();
        System.out.println("所有交通工具:");
        for (Vehicle v : vehicles) {
            System.out.println("  - " + v.getBrand() + " " + v.getModel());
        }

        session.close();
        sessionFactory.close();
    }

    private static SessionFactory createSessionFactory() {
        Configuration config = new Configuration();
        config.configure("hibernate.cfg.xml");
        config.addAnnotatedClass(Employee.class);
        config.addAnnotatedClass(Department.class);
        config.addAnnotatedClass(Course.class);
        config.addAnnotatedClass(Student.class);
        config.addAnnotatedClass(Vehicle.class);
        config.addAnnotatedClass(Car.class);
        config.addAnnotatedClass(Bike.class);
        return config.buildSessionFactory();
    }
}

@Entity
@Table(name = "employees")
class Employee {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, length = 100)
    private String name;

    @Column(name = "email", unique = true, nullable = false)
    private String email;

    @Column(name = "birth_date")
    @Temporal(TemporalType.DATE)
    private Date birthDate;

    @Enumerated(EnumType.STRING)
    @Column(name = "status")
    private EmployeeStatus status;

    @Lob
    @Column(name = "description")
    private String description;

    @ManyToOne
    @JoinColumn(name = "department_id")
    private Department department;

    public Employee() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Date getBirthDate() { return birthDate; }
    public void setBirthDate(Date birthDate) { this.birthDate = birthDate; }
    public EmployeeStatus getStatus() { return status; }
    public void setStatus(EmployeeStatus status) { this.status = status; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public Department getDepartment() { return department; }
    public void setDepartment(Department department) { this.department = department; }
}

enum EmployeeStatus {
    ACTIVE, INACTIVE, ON_LEAVE
}

@Entity
@Table(name = "departments")
class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Employee> employees = new ArrayList<>();

    public Department() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Employee> getEmployees() { return employees; }
    public void setEmployees(List<Employee> employees) { this.employees = employees; }
}

@Entity
@Table(name = "courses")
class Course {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @ManyToMany(mappedBy = "courses", fetch = FetchType.LAZY)
    private List<Student> students = new ArrayList<>();

    public Course() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Student> getStudents() { return students; }
    public void setStudents(List<Student> students) { this.students = students; }
}

@Entity
@Table(name = "students")
class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "student_course",
        joinColumns = @JoinColumn(name = "student_id"),
        inverseJoinColumns = @JoinColumn(name = "course_id")
    )
    private List<Course> courses = new ArrayList<>();

    public Student() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public List<Course> getCourses() { return courses; }
    public void setCourses(List<Course> courses) { this.courses = courses; }
}

@Entity
@Table(name = "vehicles")
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "vehicle_type")
abstract class Vehicle {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "brand")
    private String brand;

    @Column(name = "model")
    private String model;

    public Vehicle() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getBrand() { return brand; }
    public void setBrand(String brand) { this.brand = brand; }
    public String getModel() { return model; }
    public void setModel(String model) { this.model = model; }
}

@Entity
@DiscriminatorValue("CAR")
class Car extends Vehicle {

    @Column(name = "door_count")
    private Integer doorCount;

    public Car() {
    }

    public Integer getDoorCount() { return doorCount; }
    public void setDoorCount(Integer doorCount) { this.doorCount = doorCount; }
}

@Entity
@DiscriminatorValue("BIKE")
class Bike extends Vehicle {

    @Column(name = "has_gear")
    private Boolean hasGear;

    public Bike() {
    }

    public Boolean getHasGear() { return hasGear; }
    public void setHasGear(Boolean hasGear) { this.hasGear = hasGear; }
}
