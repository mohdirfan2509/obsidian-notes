
# Hibernate 7.x
## JPA
---
# Hibernate Environment

## a. Configuration
- Configuration of **DB**
- Mapping details using **Annotations**
## b. SessionFactory

- Connection Pool
- Caching
- DB Dialect
- Transaction Object
## c. Session

- Connection object
- L2 Cache
- ORM MetaData
## d. Transaction

- `commit()`
- `rollback()`
---
# Single Row Operations
## a. Insert

```java
persist(obj);   // void
```
---
## b. Read

```java
find(ClassName, Object);          // returns Object
getReference(ClassName, Object);  // returns Object | ObjectNotFoundException
```
---
## c. Update

```java
merge(object);   // returns Object
```
---
## d. Delete

```java
remove(object);  // void
```
---
# Operations Involving Complex Data

## Date Handling

- `java.time.LocalTime`
- `java.time.LocalDate`
- `java.time.LocalDateTime`
---
# Working with Foreign Key in Hibernate

- Refer image
---
# Working with Object Version in Hibernate

- Refer image
---
![Composite Key and Object Versioning in Hibernate](../Hibernate-images/Day-06__3-12-2025-CompositeKey%20and%20Object%20Versioning-images%20(1).png)
___
### **My Practice :**
1. 