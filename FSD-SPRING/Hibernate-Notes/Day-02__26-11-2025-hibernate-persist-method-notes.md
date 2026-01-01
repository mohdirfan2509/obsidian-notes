# Hibernate Overview

- Hibernate is an **implementation of JPA (Sun Microsystems)**
- **JPA** provides rules in the form of **interfaces**
- These rules define how **database operations** should be performed using **objects**
---
# Mapping Requirements in Hibernate

To use Hibernate, the following details must be supplied:

- **Class Name** → Table Name
- **Fields** → Columns
- **1 Object** → **1 Record**
---
# Ways to Provide Mapping Details

1. **XML Configuration** – outdated
2. **Properties File** – not good in coding
3. **Annotations** – widely used in Java environment
---
# Hibernate Application Flow (Insert Operation)

## TestApp.java

```java
package in.pw.ioi;

import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import in.pw.ioi.entity.Student;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // Step 1: Activate Hibernate Environment
        Session session = new Configuration()
                .configure("hibernate.cfg.xml")
                .buildSessionFactory()
                .openSession();

        Transaction transaction = session.beginTransaction();
        boolean flag = false;

        try {
            Student std = new Student("sachin", 55, "Mumbai");
            session.persist(std); // insert query sent to DB, result stored in cache
            flag = true;
        } catch (Exception e) {
            flag = false;
            e.printStackTrace();
        }

        if (flag) {
            System.in.read();
            transaction.commit(); // cache -> database
            System.out.println("Record save to database");
        } else {
            transaction.rollback();
            System.out.println("Record not saved to database");
        }
    }
}
```
---
# Entity Class Mapping
## Student.java

```java
package in.pw.ioi.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "studentTab")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "stdId")
    private Integer sid;

    @Column
    private String sname;

    @Column(name = "stdAge")
    private Integer sage;

    @Column(name = "stdAddr")
    private String saddress;

    public Student(String sname, Integer sage, String saddress) {
        super();
        this.sname = sname;
        this.sage = sage;
        this.saddress = saddress;
    }
}
```
---
# Hibernate Configuration File
## hibernate.cfg.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://hibernate.org/dtd/hibernate-configuration-3.0.dtd">

<hibernate-configuration>
    <session-factory>

        <property name="hibernate.connection.url">
            jdbc:mysql://localhost:3306/ioi_24b2_batch
        </property>
        <property name="hibernate.connection.username">root</property>
        <property name="hibernate.connection.password">root123</property>

        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">true</property>

        <property name="hibernate.dialect">
            org.hibernate.dialect.MySQLDialect
        </property>
        <property name="hibernate.hbm2ddl.auto">update</property>

        <mapping class="in.pw.ioi.entity.Student" />
    </session-factory>
</hibernate-configuration>
```
---
# Configuration File Note

- Keep `hibernate.cfg.xml` inside **`src/main/resources`**    
- File name must be **hibernate.cfg.xml**
- **Benefit:** Autoloading happens automatically for `configure()`
---
# Output

```sql
Hibernate:
    insert
    into
        studentTab
        (stdAddr, stdAge, sname)
    values
        (?, ?, ?)
```

```
Record save to database
```
---
![Hibernate Architecture](../Hibernate-images/Day-02__26-11-2025-hibernate-architecture%20and%20code-images.png)
___
### **My Practice :** 
1. 