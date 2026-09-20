# Day-65 — 11-09-2026 — Microservicesarchitecture Admin Server Eurekaserver Zipkin Server REST API

---

## 🧩 Microservices Architecture — Spring Cloud Pieces

```text
SpringCloud
===========
a. Services [ Rest api's : Actuators, interservices : Tracing]
					  |
					FeignClient
b. Eureka Server
c. Admin Server
d. Zipkin Server
e. API Gateway
```

---

## 📒 Steps to Build Eureka Server

### a. Dependencies added

- Webtools / Devtools
- spring-web — port **8761**
- Eureka server:

```xml
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
		</dependency>
```

### application.properties

```properties
server.port = 8761
```

### d. Annotation

Add `@EnableEurekaServer` at the starter class.

`http://localhost:8761` — this application would register with Eureka as a client; to disable this application as client:

```properties
eureka.client.register-with-eureka=false
```

`http://localhost:8761/` → UI with services name

---

## 🖥️ Steps to Build Admin Server

### a. Dependencies added

- Devtools
- spring-web — port **1111**
- Admin server:

```xml
				<groupId>de.codecentric</groupId>
				<artifactId>spring-boot-admin-dependencies</artifactId>
```

### application.properties

```properties
server.port = 1111
```

### d. Annotation

Add `@EnableAdminServer` at the starter class.

`http://localhost:1111` → UI Page of admin server will be opened

---

## 📍 Steps to Build Zipkin Server

1. Go to Maven repository and search for Zipkin server
2. Download the jar and keep in microservice environment
3. Open cmd prompt and then run the executable jar:

```bash
java -jar zipkin-server-3.6.0-exec.jar
```

4. Open the browser and hit the URL:

`http://127.0.0.1:9411/zipkin/` → UI page

---

## 🌐 Steps to Build Rest APIs

### a. Refer to image

Dependencies: Devtools, spring-web, Lombok, Eureka client, Admin client, Actuator, Zipkin

### b. application.properties

```properties
spring.application.name=GREET-API
server.port= 8888
spring.boot.admin.client.url=http://localhost:1111/
management.endpoints.web.exposure.include=*
```

### c. Annotation

Add `@EnableDiscoveryClient` at the starter class

### d. Design REST API as per business requirement

```java
package in.ioi.pw.restcontroller;

import java.time.LocalTime;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/greet")
public class GreetRestController {

	// GET : NO input response : String
	@GetMapping("/user/{userName}")
	public String getGreetingMsg(@PathVariable String userName) {

		String msg = "";

		LocalTime now = LocalTime.now();
		int hour = now.getHour();
		if (hour < 12) {
			msg += "Good Morning :: " + userName;
		} else if (hour < 16) {
			msg += "Good Afternoon :: " + userName;
		} else if (hour < 20) {
			msg += "Good Evening :: " + userName;

		} else {

			msg += "Good Night :: " + userName;
		}

		return msg;
	}

}
```

---

## 🤖 AI Points

1. **Production consideration:** Eureka server should not register itself as a client (`eureka.client.register-with-eureka=false`) to avoid meaningless self-registration noise.
2. **Industry practice:** Standard lab ports—Eureka `8761`, Admin `1111`, Zipkin `9411`, business APIs on their own ports with unique `spring.application.name`.
3. **Common mistake:** Forgetting `@EnableDiscoveryClient` / Admin client URL / `management.endpoints.web.exposure.include=*` so services never appear in Eureka or Admin UI.
4. **Interview insight:** Name the stack roles—registry (Eureka), ops UI (Admin), distributed tracing (Zipkin), business REST (GREET-API).
5. **Modern Spring Boot connection:** Prefer Micrometer Tracing exporters to Zipkin; keep Boot Admin for aggregated Actuator dashboards across instances.

---

## 💻 My Codes


  
## 🖼️ Image
