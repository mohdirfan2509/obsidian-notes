
# Hibernate
---
## Core Components
### Configuration

- **`hibernate.cfg.xml`**
---
### SessionFactory

- Connection Pooling
- Transaction
- Dialect
- L2 Cache
---
### Session

- Connection Object
- Transaction (Non-Select operations)
- Dialect Object
- L1 Cache
- ORM MetaData
---
# Single Row Operations (CRUD)

## a. Create (Insert)

```java
persist(object);   // void
```
---
## b. Read

```java
find(ClassName<T>, object);                 // returns T
getReference(ClassName<T>, object);         // returns T | ObjectNotFoundException
```
---
## c. Update

```java
merge(object);     // returns Object
```
---
## d. Delete

```java
remove(object);    // void
```
---
# Working with Date and Time

- `java.time.LocalDate`
- `java.time.LocalTime`
- `java.time.LocalDateTime`
---
# Working with Composite Key

- `@Embeddable`
- `@EmbeddedId`
---
# Working with Object Version

```java
@Version
```
---
# Working with TimeStamping

```java
@CreationTimestamp
@UpdateTimestamp
```
---
# Working with LOBs (Large Objects)

```java
@Lob
```
---
![[Day-07__4-12-2025-lobs and TimeStamping-notes (1).png]]
___
### **My Practice :**
1. 