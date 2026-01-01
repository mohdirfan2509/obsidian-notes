# HQL Select Operations (Bulk Operations)
---
## Example 1: Partial Loading (Single Column)
### HQL Query

```java
SELECT sname FROM Student
```
### TestApp.java

```java
package in.pw.ioi;

import java.util.List;
import org.hibernate.Session;
import in.pw.ioi.utility.HibernateUtil;

public class TestApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSession();

        String hqlSelectQuery = "SELECT sname FROM Student"; // Partial Loading
        List<String> names = session
                .createQuery(hqlSelectQuery, String.class)
                .getResultList();

        for (String name : names) {
            System.out.println(name);
        }
    }
}
```
### Output

```text
select s1_0.sname from studentTab s1_0
dhoni
virat
sachin
Irfan
```
---
# Example 2: Partial Loading (Multiple Columns using Object[])
### HQL Query

```java
SELECT sname, sage, saddress FROM Student
```
### TestApp.java

```java
package in.pw.ioi;

import java.util.List;
import org.hibernate.Session;
import in.pw.ioi.utility.HibernateUtil;

public class TestApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSession();

        var hqlSelectQuery = "SELECT sname, sage, saddress FROM Student"; // Partial Loading
        List<Object[]> details = session
                .createQuery(hqlSelectQuery, Object[].class)
                .getResultList();

        for (Object[] obj : details) {
            System.out.println("SNAME    : " + (String) obj[0]);
            System.out.println("SAGE     : " + (Integer) obj[1]);
            System.out.println("SADDRESS : " + (String) obj[2]);
            System.out.println("*******************************");
        }
    }
}
```
### Output

```text
select s1_0.sname, s1_0.stdAge, s1_0.stdAddr from studentTab s1_0

SNAME    : dhoni
SAGE     : 41
SADDRESS : Chennai
*******************************
SNAME    : virat
SAGE     : 37
SADDRESS : London
*******************************
SNAME    : sachin
SAGE     : 55
SADDRESS : Mumbai
*******************************
SNAME    : Irfan
SAGE     : 21
SADDRESS : Bengaluru
*******************************
```
---
# Example 3: Partial Loading Using DTO

### HQL Query (DTO Projection)

```java
SELECT new in.pw.ioi.entity.StudentDTO(s.sname, s.sage, s.saddress)
FROM Student s
```
### TestApp.java

```java
package in.pw.ioi;

import java.util.List;
import org.hibernate.Session;
import in.pw.ioi.entity.StudentDTO;
import in.pw.ioi.utility.HibernateUtil;

public class TestApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSession();

        var hqlSelectQuery =
                "SELECT new in.pw.ioi.entity.StudentDTO(s.sname, s.sage, s.saddress) FROM Student s";
        List<StudentDTO> students = session
                .createQuery(hqlSelectQuery, StudentDTO.class)
                .getResultList();

        for (StudentDTO student : students) {
            System.out.println(student);
        }
    }
}
```
### Output

```text
select s1_0.sname, s1_0.stdAge, s1_0.stdAddr from studentTab s1_0

StudentDTO [sname=dhoni, sage=41, saddress=Chennai]
StudentDTO [sname=virat, sage=37, saddress=London]
StudentDTO [sname=sachin, sage=55, saddress=Mumbai]
StudentDTO [sname=Irfan, sage=21, saddress=Bengaluru]
```
---
# Example 4: Full Loading (Single Object with Named Parameter)
### HQL Query

```java
FROM Student s WHERE sid = :id
```
### TestApp.java

```java
package in.pw.ioi;

import org.hibernate.Session;
import in.pw.ioi.entity.Student;
import in.pw.ioi.utility.HibernateUtil;

public class TestApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSession();

        var hqlSelectQuery =
                "FROM Student s WHERE sid = :id"; // Full Loading with one object

        Student std = session
                .createQuery(hqlSelectQuery, Student.class)
                .setParameter("id", 1)
                .uniqueResult();

        System.out.println(std);
    }
}
```
---
![Bulk Operation – Partial & Full Loading with DTO](../Hibernate-images/Day-14__17-12-2025-bulk%20operation%20-%20partial%20and%20full%20loading%20with%20DTO%20and%20working%20with%20one%20record-images.png)
___
### **My Practice :**
1. 
