
# Hibernate Core Methods
## persist(Object) : void

```java
persist(object);
```
---
## merge(T) : T

```java
merge(T);
```

- **With id** → `select(id) + update`
- **Without id** → `insert`
---
## remove(Object) : void

```java
remove(object);
```

- **With id** → delete
- **Without id** → Exception
---
## find(Class, Object) : T

```java
find(Class<T>, object);
```

- **Eager Loading**
---
## getReference(Class, Object) : T

```java
getReference(Class<T>, object);
```

- **Lazy Loading**
- May throw **ObjectNotFoundException**
---
# Working with DB Configuration Details
## a. Java Approach
### Configuration in Java Code

```java
Configuration cfg = new Configuration();
cfg.setProperty("", "");
cfg.addAnnotatedClass(Student.class);
```
### Disadvantages

- Change in DB configuration → **code must be recompiled**
- More properties → **more lines of code**
---
## b. Properties File Approach

### File Location

```
hibernate.properties
(src/main/resources)
```
### Example Properties

```properties
hibernate.connection.url=jdbc:mysql://localhost:3306/ioi_24b2_batch
;;;;
;;;;
;;;;
```
### Java Code

```java
Configuration cfg = new Configuration();
cfg.configure(); // loads hibernate.properties
cfg.addAnnotatedClass(Student.class);
```
### Disadvantage

- **Mapping details cannot be supplied** via properties file
---
## c. XML Approach
### Java Code

```java
Configuration cfg = new Configuration();
cfg.configure(); // loads hibernate.cfg.xml
```
---
# Priority Rules for Configuration Approaches
## Using All Three Approaches Together

- **Java Approach** gets priority
---
## Using `hibernate.properties` and `hibernate.cfg.xml`

- **hibernate.cfg.xml** gets priority
- Considered the **efficient approach**
---
![[Day-04__28-11-2025-hibernate-find-getreference-configuration-approaches-notes-images (2).png]]
___
### **My Practice :**
1. 