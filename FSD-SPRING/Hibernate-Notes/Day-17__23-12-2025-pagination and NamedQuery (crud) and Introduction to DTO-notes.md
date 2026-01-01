# Bulk Operations

## a. HQL
### 1. Insert
### 2. Update | Delete
### 3. Select
- **Full Loading**
    - 1 entity
    - More than 1 entity
    - **Type:** Entity Query
- **Partial Loading**
    - 1 column
    - More than 1 column
    - **Type:**
        - DT
        - DTO
    - **Query Type:** Scalar Query

---
# Entity Class

```java
@Entity
@Table(name = "")
public class Entity {

}
```

---
# Persistence Logic
## Session Object Usage

```java
Session session = ...;
```
### Creating Query

```java
Query<T> query = session.createQuery(hqlQuery, Class<T>);
```
### Setting Parameters

```java
query.setParameter("", Object);
```
### Fetching Results (Select)

```java
query.getResultList();   // returns List<T>
```
### Executing Update / Delete

```java
int count = query.executeUpdate();
```

---
# Working with NamedQuery
## Syntax

```java
@Entity
@Table
@NamedQueries(
    value = {
        @NamedQuery(
            name = "",
            query = "HQL",
            resultClass = EntityName.class
        )
        // .........
    }
)
public class EntityName {

}
```

---
## Executing Named Queries

### 1. Entity Result

```java
session.createNamedQuery(name, Class<T>)
       .setParameter(name, Object)
       .getResultList();   // List<T>
```
---
### 2. DT Result

```java
session.createNamedQuery(name, DT.class)
       .getResultList();   // List<DT>
```

---
### 3. Multiple Columns Result

```java
session.createNamedQuery(name, Object[].class)
       .getResultList();   // List<Object[]>
```
---
## Named Query with Transaction (Update / Delete)

```java
Transaction tx = session.beginTransaction();

int result = session.createNamedQuery(name, Integer.class)
                    .executeUpdate();

tx.commit();      // or
tx.rollBack();     
```

---
![Pagination, NamedQuery (CRUD) and Introduction to DTO](../Hibernate-images/Day-17__23-12-2025-pagination%20and%20NamedQuery%20(crud)%20and%20Introduction%20to%20DTO.png)
___
### **My Practice :**
   1. [HibernateNamedQueryInsert01](https://github.com/mohdirfan2509/spring-core-projects/tree/main/HibernateNamedQueryInsert01)
   2. [HibernateNamedQueryPagination01](https://github.com/mohdirfan2509/spring-core-projects/tree/main/HibernateNamedQueryPagination01)
   3. [HibernateNamedQuerySelect01](https://github.com/mohdirfan2509/spring-core-projects/tree/main/HibernateNamedQuerySelect01)
   4. [HibernateNamedQuerySelect02](https://github.com/mohdirfan2509/spring-core-projects/tree/main/HibernateNamedQuerySelect02)
   5. 
