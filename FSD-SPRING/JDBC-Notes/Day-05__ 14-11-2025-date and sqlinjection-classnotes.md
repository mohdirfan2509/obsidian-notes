
# PreparedStatement
## Advantages :

a. **Avoid SQL Injection** (Statement and PreparedStatement)  
b. **Date Operations** (Read and Write)  
c. **BLOB and CLOB Operations**

---
# SQL Injection
## Example 1

```sql
select count(*) from users 
where uname='sachin'-- and password='tendulkar'
```
### SQL Comments

- Single-line comment: `--`
- Multi-line comment: `/* comment */`

**Output:**

- Validation happens only for `uname`
---
## Example 2

```sql
select * from users where uid = 100 or 1 = 1
```
**Output:**

- Retrieves **all records**
---
# throw vs throws
## throws

```java
public ResultSet executeQuery(String sqlSelectQuery) throws SQLException {
    // logic of executing the input query is written here
}
```

- Used in **method declaration**
---
## throw

- Used while working with **custom exceptions**
- Mainly used with **unchecked exceptions**
---
# Working with Date Object
## Example 1: `java.util.Date` to `java.sql.Date`

```java
package in.pw.test;

import java.util.Date;

public class CheckApp {

    public static void main(String[] args) {

        Date uDate = new Date();
        System.out.println(uDate);

        long time = uDate.getTime();
        java.sql.Date sqlDate = new java.sql.Date(time);
        System.out.println(sqlDate); // yyyy-MM-dd format
    }
}
```
### Output

```text
Fri Nov 14 11:32:40 IST 2025
2025-11-14
```
---
# Working with Date Input from User
## Example 2: String Date to `java.sql.Date`

```java
package in.pw.test;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class DateApp {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the DOB : (yyyy-mm-dd)");
        String sDate = scanner.next();

        SimpleDateFormat sdf =
                new SimpleDateFormat("yyyy-MM-dd");

        Date date = null;
        try {
            date = sdf.parse(sDate);

            java.sql.Date sqlDate = new java.sql.Date(date.getTime());
            System.out.println(sqlDate); // yyyy-MM-dd

        } catch (ParseException e) {
            e.printStackTrace();
        }

        scanner.close();
    }
}
```
---
![[Day-05__14-11-2025-date and sqlinjection (1).png]]
___
### **My Practice :**
1. 
