## 🔌 **JDBC**
---
### 🛠️ **CRUD Operations**
- **Connection**
- **Statement**
- **PreparedStatement**
- **CallableStatement**
- **ResultSet**
---
### ▶️ **Execution Methods**
- **C, U, D** → `executeUpdate()` : `int`
- **R** → `executeQuery()` : `ResultSet`
- **Query** → `execute()` : `boolean`
---
## 🧠 **Hibernate**
---
### 🛠️ **CRUD Operations**
- **SessionFactory**
- **Session**
    - SRO
    - Bulk operations
---
## 🌱 **Spring JDBC**
---
### 🛠️ **CRUD Methods**
- **Create, Update, Delete**
    - `update(String sqlQuery, Object...) : int`
- **Select (Single Record)**
    - `queryForObject(String sqlQuery, RowMapper<T>, Object...)`
- **Select (Multiple Records)**
    - `query(String sqlQuery, RowMapper<T>)`
---
## 📦 **1. Maven Dependencies**
---

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>6.1.3</version>
    </dependency>

    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-jdbc</artifactId>
        <version>6.1.3</version>
    </dependency>

    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.3.0</version>
    </dependency>
</dependencies>
```
---
## ⚙️ **2. Configuration Code**
---
```java
package in.pw.ioi.config;

import javax.sql.DataSource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

@Configuration
@ComponentScan(basePackages = "in.pw.ioi")
public class AppConfig {

	@Bean
	public DataSource ds() {
		DriverManagerDataSource ds = new DriverManagerDataSource();
		ds.setUrl("jdbc:mysql:///");
		ds.setUsername("root");
		ds.setPassword("root123");
		return ds;
	}
	
	@Bean
	public JdbcTemplate jdbcTemplate() {
		return new JdbcTemplate(ds());
	}
}
```
---
## 🧷 **NamedParameterJdbcTemplate**
---
### 🧩 **Constructor**

```java
public NamedParameterJdbcTemplate(DataSource dataSource)
```
---
## 🎓 **Student Entity**
---
- **sid**
- **sname**
- **semail**
---
## 🧾 **Queries Using Named Parameters**
---
### ➕ **Insert**

```java
update(
  "insert into student values(:sid, :sname, :semail)",
  new BeanPropertySqlParameterSource(student)
);
```
---
### ❌ **Delete**

```java
update(
  "delete from student where sid = :sid",
  Map.of("sid", id)
);
```
---
### 🔍 **Select One Record**

```java
queryForObject(
  "select * from student where sid = :sid",
  Map.of("sid", id),
  new BeanPropertyRowMapper<>(Student.class)
);
```
---
### 📋 **Select All Records**

```java
query(
  "select * from student",
  new BeanPropertyRowMapper<>(Student.class)
);
```
---
## 🔑 **Quick View**
- JDBC → Low-level database access
- Hibernate → ORM with Session API
- Spring JDBC → Simplified JDBC using templates
- NamedParameterJdbcTemplate → Readable queries with named parameters
---
![Day 01 – JdbcTemplate and NamedParameterJdbcTemplate Notes](Day-01__img.png)
___
### **My Practice :**

1. 