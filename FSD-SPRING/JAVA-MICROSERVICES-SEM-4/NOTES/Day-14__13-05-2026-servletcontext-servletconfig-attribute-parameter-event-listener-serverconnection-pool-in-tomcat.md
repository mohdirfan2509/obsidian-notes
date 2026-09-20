# Day-14 — 13-05-2026 — ServletContext ServletConfig Attribute Parameter Event Listener Serverconnection Pool in Tomcat

---

## 🧩 Parameters vs Attributes — Request Scope

### ServletRequest / HttpServletRequest

Used to store parameter data from the client.

- Annotation analogy: `@RequestParam("paramname")` → `String|Integer name` or `String[] name`

**Data: parameter**

| Aspect | Detail |
|--------|--------|
| Datatype | K: String, V: String |
| Mode | **readonly** |

**Data: attribute** (developers should use)

| Aspect | Detail |
|--------|--------|
| Datatype | K: String and V: **any type** |
| Mode | read, update, delete |

---

## ⚙️ ServletConfig

Initialisation parameter needed for a **particular** Servlet.

```java
@WebInitParam(name = "", value = "")
```

**Data: initialization parameter**

| Aspect | Detail |
|--------|--------|
| Datatype | K: String, value: String |
| Mode | **readonly** |

Spring MVC analogy: `@Value("")` or `application.properties`

---

## 🌐 ServletContext

We need to inject the data needed **globally** for all the servlets in an application.

- Data: initialization parameter (we use **listeners**)
- Data: attribute (developers should use)
  - Datatype: K: String and V: any type
  - Mode: read, update, delete

Spring MVC analogy: `@Autowired ServletContext context;`

---

## 🚀 Container Startup Flow

```text
Tomcat container started : Event started for a container
                                |
                           Deploy the application [event occured]
                                |
                           ServletContextObject [Parameter data | Attribute data]
                                |
                        As per our servlet configuration
                                a. loading
                                b. instantiation
                                c. initialization :: ServletConfig object
                                                        [parameter data]
```

---

## 👂 Use Listeners

```text
Event occured ---> Listener -----> logic we should write
                                        set up our ServletContext object parameter
```

**Note:** `request` (param : client → server) ----> `/user` ----- request: attribute --------> `/login`

---

## 🔌 Shared Connection Object Problem → Connection Pool

**Note:** Context object holding one connection object:

```text
Servlet1  :: t1 ----> use connection object and did the job [Thread safety]
Servlet2  :: t2 ----> use connection object and did the job [Thread safety]
```

**Solution:**

```text
tomcat container started ---> event occured ---> pool of connection objects

                initialContext ---> service ----> created a pool of connection object
                                                         look up table
                                                                K         V
                                                            con-1     DataSource
                                                            con-2     DataSource


         Servlet1  :: t1 ----> init() ---> ask InitialContext and go to look up table
                                                get DataSource object : connection and use
                                doXXX() ---> con.close() : send back to pool.

         Servlet2  :: t2 ----> init() ---> ask InitialContext and go to look up table
                                                get DataSource object : connection and use
                                doXXX() ---> con.close() : send back to pool.
```

---

## ☕ Java Event / Listener Types

```text
Java ---> Event    :  ServletContextEvent(C)
         Listeners :  ServletContextListener(I): functional programming : functional interface
```

---

## 🛠️ Server Setup — Step 1: context.xml Resource

```xml
<Resource auth="Container"
	driverClassName="com.mysql.cj.jdbc.Driver"
	maxIdle="4"
	maxTotal="8"
	name="jdbc/EmployeeDB"
	password="root123"
	type="javax.sql.DataSource"
	url="jdbc:mysql://localhost:3306/octbatch"
	username="root"/>
```

### Lookup table of InitialContext service

```text
lookupTableName :
                jdbc/EmployeeDB
                   CON ------> javax.sql.DataSource
                   CON ------> javax.sql.DataSource
                        ;;;;;
```

---

## 🛠️ Step 2 — Ask Container for InitialContext / DataSource

```java
InitialContext context = new InitialContext();
DataSource ds = (DataSource) context.lookup("java:/comp/env/jdbc/EmployeeDB");
Connection con = ds.getConnection();
System.out.println(con); // hashcode value    URL :    MYSQL/jar
;;;;;
con.close();
```

For Catalina container of Tomcat to access the service we use:

```text
java:/comp/env/locationName
```

---

## 🤖 AI Points

1. **Production consideration:** Never share one JDBC `Connection` on `ServletContext` across threads—use a pooled `DataSource` and `close()` to return connections to the pool.
2. **Industry practice:** Configure JNDI `Resource` in Tomcat `context.xml` / `server.xml` and look up `java:/comp/env/jdbc/...` from servlet `init()`.
3. **Common mistake:** Treating `con.close()` on a pooled connection as destroying the TCP link forever—with pooling it returns the connection to the pool.
4. **Interview insight:** Parameters are String/String read-only; attributes are String/Object mutable; Config is per-servlet init; Context is app-wide.
5. **Modern Spring Boot connection:** Boot auto-configures a pooled DataSource (HikariCP); `@Autowired DataSource` replaces manual `InitialContext` lookup in most apps.

---

## 💻 My Codes


  
## 🖼️ Image

