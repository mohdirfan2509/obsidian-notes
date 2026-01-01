
# Bulk Operations in Hibernate
## Single Record Operations

```java
persist(obj);     // inserts one record (id : primary key)
find(Class, pk);  // reads a record using primary key
```
---
## Requirement for Bulk Operations
When we want to:

- Read **all records** from database
- Read records based on **non-primary key**
- Read **only one column** from a table
### Solution
Use **Bulk Operations** in Hibernate using:

- a. **HQL | JPQL**
- b. **Native Query**
- c. **QBC**
---
# JDBC vs Hibernate Query Processing
## JDBC

```text
JDBC → SQL
      → MySQL        (correct)
      → PostgreSQL   (wrong)
      → Oracle       (wrong)
```
---
## Hibernate

```text
Hibernate → HQL → Dialect(URL) → SQL → DB (runtime)

          → MySQL        (correct)
          → PostgreSQL  (correct)
          → Oracle      (correct)
```
---
# Syntax of HQL vs SQL
## SQL

- Uses **table names** and **column names**
- Keywords:
    - select, insert, update, from, etc.
- Keywords, table names, column names are **case-insensitive**
---
## HQL

- Uses **class names** and **field names**
- Java identifiers are **case-sensitive**
- HQL keywords are **case-insensitive**
---
# SQL vs HQL Examples
## Example 1
### SQL

```sql
select eid, ename, eage from empTab where eid = 10;
```
### HQL

```java
select empId, empName, empAge
from in.pw.ioi.Model.Employee
where empId = 10;
```

OR

```java
select e.empId, e.empName, e.empAge
from in.pw.ioi.Model.Employee e
where e.empId = 10;
```
---
## Example 2
### SQL

```sql
select * from empTab where salary > 25000;
```
### HQL

```java
from in.pw.io.Model.Employee e where e.salary > :amount;
```
---
## Example 3
### SQL

```sql
select eid, ename from emptab;
```
### HQL

```java
select empId, empName from com.app.model.Employee;
```
---
## Example 4
### SQL

```sql
update emptab set ename = ?, esal = ? where eid = ?;
```
### HQL

```java
update com.app.model.Employee
set empName = ?, empSal = ?
where empId = ?;
```
---
## Example 5
### SQL

```sql
select * from emptab;
```
### HQL

```java
from com.app.model.Employee;
```
---
## Example 6

### SQL

```sql
delete from emptab where eid = ?;
```
### HQL

```java
delete from com.app.model.Employee where empId = ?;
```
---
## Example 7
### SQL

```sql
select count(eid) from emptab group by eid;
```
### HQL

```java
select count(empId) from com.app.Employee group by empId;
```
---
# HQL Bulk Select Example
## TestApp.java

```java
package in.pw.ioi;

import java.util.List;

import org.hibernate.Session;

import in.pw.ioi.entity.Student;
import in.pw.ioi.utility.HibernateUtil;

public class TestApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSession();

        String hqlSelectQuery = "FROM Student";
        List<Student> students =
                session.createQuery(hqlSelectQuery, Student.class)
                       .getResultList();

        for (Student student : students) {
            System.out.println(student);
        }
    }
}
```
---
![Bulk Operations in Hibernate](../Hibernate-images/Day-13__16-12-2025-bulkoperation%20in%20hibernate.png)
___
### **My Practice :**
1. 