
# JDBC Program with User Input and Resource Handling
---
## Purpose of the Program

- Establish a database connection
- Accept **user input**
- Execute a **SELECT query**
- Display result if available
- Handle exceptions
- Close all resources properly
---
# JDBC Objects Used

```java
Connection connection
Statement statement
ResultSet resultSet
Scanner scanner
```
---
# Database Credentials

```java
String url
String username
String password
```
---
# JDBC Program Flow
## Step 1: Load and Register the Driver

```text
JRE : JVM + DB Environment
```
---
## Step 2: Establish the Connection

```java
connection = DriverManager.getConnection(url, username, password);
System.out.println("Connection to : " + url);
```
---
## Step 3: Send Query for Execution

- Accept input from use
- Build SQL query using input
- Execute query using `Statement`

```java
scanner = new Scanner(System.in);
System.out.print("Enter the USN : ");
int id = scanner.nextInt();

String sqlSelectQuery =
        "select sid,sname,sage from student where sid=" + id;
System.out.println(sqlSelectQuery);

resultSet = statement.executeQuery(sqlSelectQuery);
```
---
## Step 4: Process the Result

```java
if (resultSet.next()) {
    System.out.println("SID\tSNAME\tSAGE");

    int sid = resultSet.getInt(1);
    String sname = resultSet.getString(2);
    int sage = resultSet.getInt("sage");

    System.out.println(sid + "\t" + sname + "\t" + sage);
} else {
    System.out.println("Record not available for the given id : " + id);
}
```
---
## Step 5: Close the Resources (Finally Block)

```java
resultSet.close();
statement.close();
scanner.close();
connection.close();
```
---
# Complete JDBC Program

```java
package in.pw.ioi;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class TestApp {

    public static void main(String[] args) {

        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        Scanner scanner = null;

        String url = null;
        String username = null;
        String password = null;

        try {
            connection = DriverManager.getConnection(url, username, password);
            System.out.println("JRE : JVM + DB Environment");
            System.out.println("Connection to : " + url);

            if (connection != null) {
                statement = connection.createStatement();

                if (statement != null) {
                    scanner = new Scanner(System.in);
                    System.out.print("Enter the USN : ");
                    int id = scanner.nextInt();

                    String sqlSelectQuery =
                            "select sid,sname,sage from student where sid=" + id;
                    System.out.println(sqlSelectQuery);

                    resultSet = statement.executeQuery(sqlSelectQuery);

                    if (resultSet.next()) {
                        System.out.println("SID\tSNAME\tSAGE");

                        int sid = resultSet.getInt(1);
                        String sname = resultSet.getString(2);
                        int sage = resultSet.getInt("sage");

                        System.out.println(sid + "\t" + sname + "\t" + sage);
                    } else {
                        System.out.println("Record not available for the given id : " + id);
                    }
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                resultSet.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }

            try {
                if (statement != null) {
                    statement.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }

            scanner.close();

            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

---
![[Day-03__12-11-2025-jdbc-selectappwith try and catch-notes-images (1).png]]
___
**My Practice :**
1. 