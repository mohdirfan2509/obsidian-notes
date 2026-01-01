# JDBC Project Structure

```
ProjectName
 ├── JRE
 ├── mysql-connector
 ├── src
 └── db.properties
```
---
# Reading Database Configuration from Properties File
## Java Code to Load Properties

```java
import java.io.*;
import java.util.*;

try {

    FileInputStream fis = new FileInputStream("db.properties");

    Properties props = new Properties();
    props.load(fis);

    url = props.getProperty("url");
    username = props.getProperty("username");
    password = props.getProperty("password");

} catch (FileNotFoundException e) {
    e.printStackTrace();
}
```
---
# Properties File
## mydb.properties

```properties
url=jdbc:mysql://localhost:3306/ioi_24b2_batch
username=root
password=root123
```
---
# Using Statement Object

```java
Statement stmt = connection.createStatement();

stmt.executeQuery(sqlSelectQuery);
stmt.executeUpdate(sqlNonSelectQuery);
```
---
# Using PreparedStatement
## SQL Insert Query

```java
String sqlInsertQuery =
    "insert into student(`sname`,`sage`) values(?,?)";
```
## Java Code

```java
PreparedStatement pst =
        connection.prepareStatement(sqlInsertQuery);

pst.setString(1, "yuvi");
pst.setInt(2, 42);

int rowCount = pst.executeUpdate();
```
---
![PreparedStatement Class Notes](../JDBC-images/Day-04__13-11-2025-preparedstatement-classnotes-images%20(2).png)
___
### **My Practice :**
1. 