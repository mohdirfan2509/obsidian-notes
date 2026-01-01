
# Stored Procedure in Hibernate
## Parameters
- **IN parameter**
- **OUT parameter**
---
## Stored Procedure Definition (MySQL)

```sql
DELIMITER $$

USE `ioi_24b1_batch`$$

DROP PROCEDURE IF EXISTS `GET_PRODUCT_DETAIlS_BY_ID`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_PRODUCT_DETAIlS_BY_ID`(
    IN productId INT,
    OUT productName VARCHAR(20),
    OUT productPrice INT,
    OUT productType VARCHAR(20)
)
BEGIN
    SELECT 
        pname, price, ptype
    INTO
        productName, productPrice, productType
    FROM
        Products
    WHERE pid = productId;
END$$

DELIMITER ;
```

---
## Calling Stored Procedure (MySQL)

```sql
SET @productName='';
SET @productPrice=0;
SET @productType='';

CALL GET_PRODUCT_DETAIlS_BY_ID(1, @productName, @productPrice, @productType);

SELECT @productName, @productPrice, @productType;
```
### Output

| productName | productPrice | productType |
| ----------- | ------------ | ----------- |
| fossil      | 100000       | Automatic   |

---
# Steps to Run Stored Procedure in Hibernate

1. Create `StoredProcedureQuery`

```java
StoredProcedureQuery query =
    session.createStoredProcedureQuery("STORED_PROCEDURE_NAME");
```

2. Register Parameters

```java
query.registerStoredProcedureParameter(
    String name,
    Class<T>,
    ParameterMode(E) : IN | OUT | INOUT
);
```

3. Set Input Parameter

```java
query.setParameter(String parameterName, Object value);
```

4. Execute Procedure

```java
query.execute(); // returns boolean
```

5. Get Output Parameter

```java
query.getOutputParameterValue(String name);
```

---
## Example: Hibernate Stored Procedure Call

```java
package in.pw.ioi;

import org.hibernate.Session;
import org.hibernate.cfg.Configuration;
import jakarta.persistence.ParameterMode;
import jakarta.persistence.StoredProcedureQuery;

public class TestApp {

    public static void main(String[] args) throws Exception {

        Session session = new Configuration()
                .configure()
                .addAnnotatedClass(Person.class)
                .buildSessionFactory()
                .openSession();

        StoredProcedureQuery query =
                session.createStoredProcedureQuery("GET_PRODUCT_DETAIlS_BY_ID");

        // IN parameter
        query.registerStoredProcedureParameter(
                "productId", Integer.class, ParameterMode.IN);
        query.setParameter("productId", 2);

        // OUT parameters
        query.registerStoredProcedureParameter(
                "productName", String.class, ParameterMode.OUT);
        query.registerStoredProcedureParameter(
                "productPrice", Integer.class, ParameterMode.OUT);
        query.registerStoredProcedureParameter(
                "productType", String.class, ParameterMode.OUT);

        query.execute();

        if (query.getOutputParameterValue("productName") != null) {
            System.out.println("ProductName : " +
                    query.getOutputParameterValue("productName"));
            System.out.println("ProductPrice : " +
                    query.getOutputParameterValue("productPrice"));
            System.out.println("ProductType : " +
                    query.getOutputParameterValue("productType"));
        } else {
            System.out.println("Record not for the given id : 2");
        }

        session.close();
    }
}
```

---
# Query with Named Parameter Supplying Multiple Values
## Case 1: `IN` Clause
### SQL

```sql
SELECT eid, ename, eage, eaddress, edept
FROM employee
WHERE edept IN ('IT', 'FINANCE', 'HR');
```
### HQL

```java
from Employee e
where e.empDept IN (:depts)
```
### Hibernate Code

```java
Session session = new Configuration()
        .configure()
        .buildSessionFactory()
        .openSession();

List<String> depts = List.of("IT", "FINANCE", "HR");

List<Employee> emps = session
        .createQuery("HQL", Employee.class)
        .setParameter("depts", depts)
        .getResultList();
```

---
## Case 2: `LIKE` Clause
### SQL

```sql
SELECT eid, ename, eage, eaddress, edept
FROM employee
WHERE ename LIKE 'A%';
```
### HQL

```java
from Employee e
where e.ename like :name
```
### Hibernate Code

```java
Session session = new Configuration()
        .configure()
        .buildSessionFactory()
        .openSession();

List<Employee> emps = session
        .createQuery("HQL", Employee.class)
        .setParameter("name", "A%")
        .getResultList();
```

---
# HQL Non-Select Operations
## Types

1. Update
2. Delete
3. Insert
---
## SQL Insert

```sql
INSERT INTO tablename(``, ``)
VALUES (?, ?, ?);
```

---
## HQL Insert Limitation

```text
INSERT INTO EntityName VALUES (?,?,?,?)  --> Not possible
```

- `?` represents **Primary Key**
- Entity must have:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
```

- Database handles primary key generation
---
## HQL Insert Using Select

### Concept

- Existing table already has records
- Copy values and insert into another table
### Syntax

```sql
insert into EntityName(fieldname1, fieldname2, fieldname3)
select fieldname1, fieldname2, fieldname3
from ExistingTable
where condition;
```

---
![Stored Procedures and Bulk Insert Operation in Hibernate](../Hibernate-images/Day-16__22-12-2025-storedprocured%20and%20bulk%20insert%20operation.png)
___
### **My Practice :**
   1.
   2.