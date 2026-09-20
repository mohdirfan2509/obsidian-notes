# Day-62 — 07-09-2026 — Spring Data REST and Usage of Modules in Microservice Environment

---

## 🧩 Spring → Spring REST with HATEOAS

```text
Spring
  |=> SpringRest with HATEOS


Spring Rest ======> RestAPI's
			|=>   RestController [take request ---> generates JSON]
				  |
				Service
				  |
				 DAO [JDBC,ORM,DataJPA]
```

### RestController concerns

**a. HttpMethods**

- POST
- GET
- PUT
- DELETE
- PATCH

**b. Entity** — Employee, Student, Ticket, …

**c. Collection vs item**

- POST → Collection type data
- GET → Collection type data
- PUT → one item
- DELETE → one item

---

## 🚀 Designing a RestController without Logic — `spring-data-rest`

### pom.xml

```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-rest</artifactId>
</dependency>
```

### a. Create a new project with dependencies

- Lombok
- Data JPA
- spring-data-rest
- Spring MVC
- Devtools
- OpenAPI

### b. Entity `Employee`

Fields: `eid`, `ename`, `eage`, `eaddress`

### c. Repository

`JpaRepository<Employee, Integer>`

### Endpoints (auto-exposed)

| HTTP | Path |
| --- | --- |
| GET | `/employees` |
| GET | `/employees/{id}` |
| POST | `/employees` |
| PUT | `/employees/{id}` |
| DELETE | `/employees/{id}` |
| PATCH | `/employees/{id}` |

---

## 🔒 Disabling Endpoints — `RepositoryRestConfigurer`

To disable endpoints as per our needs we implement `RepositoryRestConfigurer`:

```text
RepositoryRestConfigurer
   |=> default void configureRepositoryRestConfiguration(RepositoryRestConfiguration config, CorsRegistry cors) {}
```

```java
in.pw.ioi.config
	   |   @Component
	   |=> public class DataRestConfig  implements  RepositoryRestConfigurer{

			
			public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config, CorsRegistry cors)
			{
					//1. ExposureConfiguration getExposureConfiguration()
					config
						.getExposureConfiguration()
						//ExposureConfigurer forDomainType(Class<?> type)
						.forDomainType(Employee.class)
						//ExposureConfigurer withItemExposure(AggregateResourceHttpMethodsFilter filter)
						.withItemExposure(

							//ConfigurableHttpMethods filter(ResourceMetadata metdata, ConfigurableHttpMethods httpMethods)

								(metadata,httpMethods)->

									//ConfigurableHttpMethods disable(HttpMethod... methods)
										httpMethods.disable(HttpMethod.PUT,HttpMtehod.PATCH,HttpMethod.DELETE)

							)
			}

		}
```

---

## 📦 JDK Modules (pre-JDK 8 vs JDK 9+)

### Before JDK 8

`rt.jar` (~60 MB) bundled everything:

- `java.sql`
- `java.util`
- `java.io`
- `java.rmi`
- `javax.naming`
- `java.logging`
- …

In this approach, we can't tell what our project really needs, so inside our JRE everything would be loaded (~210 MB).

### From JDK 9 — `jmods`

Modules such as `java.sql`, `java.io`, `java.util`, `java.rmi`, `javax.naming`, `java.logging`, …

Use `module-info` and tell what your project really needs:

```java
module IRCTCApp {
	requires java.sql;
	exports in.pw.ioi.controller;
}
```

Design a JRE with only the required libraries using **Jlink**:

```text
module-info
    |
   JRE  [ less than the original ] => suitable for IOT devices
    |=> java.sql, java.base, IRCTC
```

**Note:**

- `requires` → module
- `exports` → package

### ModuleA / ModuleB / ModuleC

**ModuleA** — `module-info.java`

```text
ModuleA :: requires transitive java.sql;
           requires static java.logging; //SLF4J  static : compile yes; runtime : need not be available
           export  in.pw.ioi.test;
```

**ModuleB**

```text
ModuleB :: requires java.util;
           requires in.pw.ioi.test;
           export com.app.pw.check;
```

**ModuleC**

```text
ModuleC :: requires java.io;
           requires com.app.pw.check;
           [modules by default won't be inherited, explicitly we should say or use transitive]
```

### DemoApp behavior

| Code | With transitive / static | Result |
| --- | --- | --- |
| JDBC code | `requires transitive java.sql` reached | Works |
| Logging code (no static available) | — | `NoClassDefFoundError` on `logger.info()` |
| Logging with `requires static` | runtime optional | Guard with `Class.forName` check |

```java
public boolean doLogging(){
	//check whether dependencies are there on your module, if yes return true otherwise return false
	try{
		Class.forName("path of class");
		return true;
	}catch(Exception e){
		return false;
	}	
}
```

```java
if(doLogging()){
	logger.info(...);
}else{
	//don't use logging
}
```

---

## 🤖 AI Points

1. **Production consideration:** Disable dangerous Data REST verbs (`PUT`/`PATCH`/`DELETE`) via `RepositoryRestConfigurer` when the domain must be read-mostly or write-gated.
2. **Industry practice:** Spring Data REST exposes CRUD from `JpaRepository` without a hand-written `@RestController`—great for admin/internal APIs, review carefully for public ones.
3. **Common mistake:** Assuming all HTTP methods stay enabled; forgetting exposure filters leaves update/delete open by default.
4. **Interview insight:** JDK 9+ modules (`requires` / `exports` / `transitive` / `static`) + `jlink` shrink runtime images for IoT and microservices.
5. **Modern Spring Boot connection:** Pair `spring-boot-starter-data-rest` with OpenAPI and HATEOAS-style HAL links that Data REST emits by default.

---

## 💻 My Codes


  
## 🖼️ Image
