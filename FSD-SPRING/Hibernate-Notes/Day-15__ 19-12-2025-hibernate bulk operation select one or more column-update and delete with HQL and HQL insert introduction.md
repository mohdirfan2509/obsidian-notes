
# Named Parameter in HQL
## Single Named Parameter
### HQL Query

```java
from Employee e where e.eid = :id
```
### Hibernate Code

```java
session.createQuery(hql, Employee.class)
       .setParameter("id", 10)
       .uniqueResult();
```
---
# Working with Multiple Named Parameters
## Entity Class

```java
@Entity
public class Employee {

    @Id
    private Integer id;

    private String name;
    private Double salary;
    private String department;
}
```
---
## HQL with Multiple Named Parameters

```java
from Employee e
where e.salary > :sal and e.deparatment = :dept
```
### Hibernate Code

```java
session.createQuery(hql, Employee.class)
       .setParameter("dept", "CSE")
       .setParameter("sal", 60000)
       .getResultList();
```
---
# Working with One Column Using Named Parameter
## HQL Query

```java
select e.name from Employee e where department = :dept
```
### Hibernate Code

```java
List<String> list = session.createQuery(hql, String.class)
       .setParameter("dept", "CSE")
       .getResultList();
```
---
# Working with Multiple Columns Using Named Parameter
## DTO Class

```java
public class EmployeeDTO {

    private Integer id;
    private String name;
    private String department;

    EmployeeDTO(Integer id, String name, String department) {
        this.id = id;
        this.name = name;
        this.department = department;
    }

    toString() {}
}
```
---
## HQL Query (DTO Projection)

```java
select new in.pw.ioi.Model.EmployeeDTO(e.name, e.id, e.deparatment)
from Employee e
where e.salary >= :sal
```
### Hibernate Code

```java
List<EmployeeDTO> list = session.createQuery(hql, EmployeeDTO.class)
       .setParameter("dept", "CSE")
       .getResultList();
```
---
# Non-Select Operations in HQL
## Transaction Handling

```java
Transaction tx = session.beginTransaction();

tx.commit(flag = true);
tx.rollback(flag = false);
```
---
## a. Update Operation
### HQL

```java
update Employee e
set e.esal = esal + :sal
where e.department = :dept
```
### Hibernate Code

```java
int noOfRows = session.createMutationQuery(hql)
       .setParameter("sal", 60000)
       .setParameter("dept", "CSE")
       .executeUpdate();
```
---
## b. Delete Operation
### HQL

```java
delete
from Employee e
where e.eid = :id
```
### Hibernate Code

```java
int noOfRows = session.createMutationQuery(hql)
       .setParameter("id", 11)
       .executeUpdate();
```
---
## c. Insert Operation (Very Dangerous)
### Invalid HQL Insert

```java
insert
into Employee
values(:id, :name, :age, :address, :salary);   // invalid
```
### Notes
- Direct insertion of values in HQL **cannot be used**
- Row must be taken from **one table and inserted into another**
- Direct value insertion causes **primary key adjustment**
- Hence, **HQL insertion with direct values is not allowed**
---
### **My Practice :**
1. 