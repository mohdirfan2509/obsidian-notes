
# JDBC
## Java Database Connectivity
---
## Definition

- JDBC is an **API** that allows a **Java program to communicate with a database**.
- **API** means a **collection of interfaces** (abstract methods / contracts).
- For JDBC:
    - The **database vendor** provides the implementation.
    - The implementation is available as a **JAR file**.
---
## JDBC Driver JARs
- Examples:
    
    - **MySQL** → `mysql-connector-java.jar`
    - **Oracle** → `oracle-connector-java.jar`
- To run JDBC applications:
    
    - The **appropriate driver JAR** must be kept along with the **JDK**.
- The JAR can be obtained:
    
    - Locally from the database vendor
    - Using a build tool like **Maven**
---
## Step 1: Download JDBC Driver

- Download manually from Maven Repository

```text
https://mvnrepository.com/artifact/com.mysql/mysql-connector-j/8.3.0
```

- File name:

```text
mysql-connector-j-8.3.0.jar
```
---
## Step 2: Project Setup

- Create a **standard Java project**
- Add:
    - **JDK JAR**

    - **JDBC Driver JAR**        
---
## Step 3: JDBC Programming Steps

1. **Load and register the driver**
2. **Establish the connection**
    - Provide valid URL and credentials
3. **Send the query and process the result** 
4. **Use the result**
5. **Close the connection**
---
![[Day-01__10-11-2025-jdbc-introduction-notes-images.png]]
___
### **My Practice :**
1. 