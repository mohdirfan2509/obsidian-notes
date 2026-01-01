# Steps Given by SUN Microsystems to Communicate with Database
## JDBC Communication Steps
a. **Load and register the driver**

- JRE = JVM + DB Environment
b. **Establish the connection** between Java application and database
c. **Send the query and execute the query**
d. **Get the result and process the result**
e. **Close the connection**

---
# Example: JDBC Program to Read Data from Database
## TestApp.java

```java
package in.pw.ioi;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestApp {

    public static void main(String[] args)
            throws ClassNotFoundException, SQLException {

        // Step 1: Load and register the driver
        Class.forName("com.mysql.cj.jdbc.Driver");
        System.out.println("JRE : JVM + DB Environment");

        // Step 2: Establish the connection
        String url = "jdbc:mysql://localhost:3306/ioi_24b2_batch";
        String username = "root";
        String password = "root123";

        Connection connection =
                DriverManager.getConnection(url, username, password);
        System.out.println("Connection to : " + url);

        // Step 3: Send the query for execution
        Statement statement = connection.createStatement();
        String sqlSelectQuery =
                "select sid, sname, sage from student";
        ResultSet resultSet =
                statement.executeQuery(sqlSelectQuery);

        System.out.println("SID\tSNAME\tSAGE");

        // Step 4: Use the data (ResultSet)
        while (resultSet.next()) {
            int sid = resultSet.getInt(1);
            String sname = resultSet.getString(2);
            int sage = resultSet.getInt("sage");

            System.out.println(sid + "\t" + sname + "\t" + sage);
        }

        // Step 5: Close the resources
        resultSet.close();
        statement.close();
        connection.close();
    }
}
```
---
![JDBC Select Application](../JDBC-images/Day-02__11-11-2025-jdbc-selectapp-images%20(1).png)
___
**My Practice :**
1. 