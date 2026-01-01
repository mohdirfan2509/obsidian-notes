
# Java Overview

## a. Java as a Language
- **Compiler + JVM**
- Set of APIs given by **JDK team**
- Core library: **`rt.jar`**
---
## b. Java as a Technology

- APIs given by JDK team are **not sufficient**
- Requires **additional collection of JAR files**
- Examples:
    - JDBC
    - Servlet
    - JSP
---
# Limitations of JDBC
## 1. Programming Steps in JDB
### Steps:

a. Load and register the driver  
b. Establish the connection  
c. Use `Statement` / `PreparedStatement` / `CallableStatement`  
d. Send the query and process the result  
e. Close the resources
### Logic Classification

- **Application Logic**
    - Steps: a, b, e
- **Business Logic**
    - Steps: c, d
---
## 2. Common Exception

- JDBC provides only **one common exception class**:
    - `SQLException`
---
## 3. Checked Exception Issue

- `SQLException` is a **checked exception**
- Handling logic is **mandatory**
- Without handling, code will not run
- Checked exception **does not permit exception propagation by default**
---
## 4. Transaction Support

- JDBC does **not permit good transaction support**

---
## 5. No Variable Name Binding

```java
String sqlInsertQuery = "insert into employee values(?,?,?)";
PreparedStatement pstmt = connection.prepareStatement(sqlInsertQuery);
```

- JDBC does **not support variable name binding**
---
## 6. ResultSet Limitation

- `ResultSet` object is **not Serializable**
- Data **cannot be transmitted over the network**
---
## 7. Object Data Limitation

- Object data **cannot be used directly**
- SQL supports only **primitive value injection**
---
## 8. Lack of OOP Concepts

- SQL does **not support**:
    - Encapsulation
    - Inheritance
    - Polymorphism
    - Abstraction
- OOP features **cannot be used by an OOP developer**
---
## 9. No Caching Support

- JDBC does **not support caching**
- Same request multiple times causes:
    - Multiple database hits
---
## 10. No Object Versioning and Time Stamping

- **Object Versioning**
    - Keeping count of how many times a record is modified
- **Time Stamping**
    - Keeping track of:
        - When the record is opened
        - When the record is closed
---
# Solution
## ORM (Object Relational Mapping) Framework
---
![[Day01__24-11-2025-hibernate-introduction-classnotes-images (1).png]]
___
### **My Practice :** 
1. 