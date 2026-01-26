# 🌱 **Spring Boot – Introduction**
---
## 🚀 **What is Spring Boot?**
- A mechanism to build **Spring-based projects** in a **productive way**.
- **Spring Boot =**
    - Spring
    - Auto-Configuration
    - Inbuilt Server
    - Actuators
---
## 📝 **Important Notes**
- In **Spring JDBC**:
    - Configuration is written **explicitly**.
- In **Spring Boot**:
    - Use **`spring-boot-starter-jdbc`**
    - Configuration is provided **automatically**.
---
## ⚙️ **Spring Boot Working Style**
While working with Spring Boot projects:
### ✅ **a. Auto Configuration**
- Configuration is **auto handled**
- Uses **predefined beans**
### 🧾 **b. Supplying Values**
- Values are supplied using **key–value pairs**
- Written in:
    
    ```
    src/main/resources/application.properties
    ```
### 📦 **c. Base Package Scanning**
- Base package is taken automatically from:

    ```
    src/main/java
    ```    
- Default base package:
    
    ```
    in.pw.ioi
    ```

- Common structure:    
    - `in.pw.ioi.model`
    - `in.pw.ioi.service` → `@Service`, `@Transactional`
    - `in.pw.ioi.dao` → `@Repository`
    - `in.pw.ioi.config` → user-defined beans (if any)
---
## 🔗 **Reference Links**
- Application Properties:
    
    ```
    https://docs.spring.io/spring-boot/appendix/application-properties/index.html
    ```
    
- Spring Initializr:
    
    ```
    https://start.spring.io
    ```
---
## 🧩 **Spring Initializer Configuration (Used)**
- Project Type: Maven
- Language: Java
- Java Version: 21
- Packaging: Jar
- Dependencies:
    - JDBC
    - MySQL
---
## 🧠 **Key Annotations**
### 🧩 **@SpringBootApplication**

```
@SpringBootApplication
= @ComponentScan
+ @EnableAutoConfiguration
+ @SpringBootConfiguration
```
### ⚙️ **@SpringBootConfiguration**

```
@SpringBootConfiguration = @Configuration
```
---
## ▶️ **Example: Spring Boot Main Class**

```java
package in.pw.ioi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;

@SpringBootApplication
public class SpringBootJdbcAppApplication {

	public static void main(String[] args) {

		ConfigurableApplicationContext container =
				SpringApplication.run(SpringBootJdbcAppApplication.class, args);

		JdbcTemplate jdbcTemplate =
				container.getBean("jdbcTemplate", JdbcTemplate.class);

		NamedParameterJdbcTemplate namedParameterJdbcTemplate =
				container.getBean("namedParameterJdbcTemplate", NamedParameterJdbcTemplate.class);

		System.out.println(namedParameterJdbcTemplate);
		System.out.println(jdbcTemplate);
	}
}
```
---
## 📁 **application.properties**

📍 Location:

```
src/main/resources/application.properties
```

```properties
spring.application.name=SpringBoot-JDBC-App

spring.datasource.url=jdbc:mysql:///ioi_24b2_batch
spring.datasource.username=root
spring.datasource.password=root123
```
---
## 📤 **Output**

```
org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate@42210be1
org.springframework.jdbc.core.JdbcTemplate@1eb2d371
```
---
## 🔑 **Key Takeaways**
- Spring Boot reduces **manual configuration**
- Uses **starter dependencies** 
- Automatically creates:
    - `JdbcTemplate`
    - `NamedParameterJdbcTemplate`
- Configuration values are supplied via `application.properties`
---
![Introduction to Spring Boot](Day-01-img.png)
___
### **My Practice :**
1. 