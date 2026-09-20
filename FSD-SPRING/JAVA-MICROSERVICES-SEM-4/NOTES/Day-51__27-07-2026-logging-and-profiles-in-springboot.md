# Day-51 — 27-07-2026 — Logging and Profiles in Spring Boot

---

## ⚠️ Problem with `System.out.println()`

- Only print statements.
- Cannot disable print statements based on needs.
- No debugging levels like `debug`, `trace`, `info`, `warn`, `error`, `fatal`.
- No timestamps.
- Once the console is cleared, log statements are gone.

---

## 📦 Logging Frameworks

1. Log4j
2. Logback
3. `java.util.logging`

If we work with Log4j directly:

```java
private static final Logger logger = Logger.getLogger(EmployeeService.class);
// tightly bound to Log4j only
```

If we later change the logging framework to Logback, then in our application the entire logging-related code would need to change.

**Solution:** use **SLF4J** (interface / facade).

---

## 🔌 Simple Logging Facade for Java (SLF4J)

Implementation classes:

- Log4j
- Logback
- `java.util.logging`

With SLF4J:

```java
private static final Logger logger = LoggerFactory.getLogger(EmployeeService.class);
```

Depending upon the implementation classes available on the classpath, a suitable logger is picked.

> **Note:** If we use Lombok, Lombok can automatically generate `private static final Logger log = LoggerFactory.getLogger(...)`.

```java
@Slf4j
public class EmployeeService {

    public void save() {
        log.info("Employee Saved");
    }
}
```

---

## 🏗️ Logging Architecture

### 🔑 Logger

| Method | Level | Typical use |
|---|---|---|
| `debug()` | DEBUG | Print message with data, e.g. employee saved with id `1234` |
| `info()` | INFO | Simple message, e.g. email sent, if-block ended |
| `warning()` / `warn()` | WARN | Warning message, e.g. collection without generics, local variable not used, resource not closed |
| `error()` | ERROR | Print exceptions, e.g. `NullPointerException`, `AIOBE`, `FileNotFoundException`, `IOException` |
| `fatal()` | FATAL | High-level problems, e.g. server/DB down, connection timeout, network error |

> **Correction:** In SLF4J / Logback the common API method is `warn()` (not always named `warning()`). FATAL is not a first-class SLF4J level; Log4j historically had FATAL, while Logback maps severe failures mainly through ERROR.

### 📤 Appender — where to print the message

| Appender | Target |
|---|---|
| `FileAppender` | File |
| `JdbcAppender` | Database |
| `SmtpAppender` | Email |
| `ConsoleAppender` | Console |
| FTP / Telnet appender | Network |

### 🧾 Layout — format of the message

| Layout | Behavior |
|---|---|
| Simple Layout | Print message as-is |
| HTML Layout | Print message in HTML format (`<html><body>…`) |
| XML Layout | Print message in XML format (`<Errors><Type>…<Message>…`) |
| Pattern Layout | Print messages in a given pattern, e.g. Date-Time / Line Number : Class-method :- Message |

---

## 💻 Example 1 — Log4j2 Console Configuration

### `src/main/resources/log4j2.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>

<Configuration>

    <Appenders>

        <Console name="Console" target="SYSTEM_OUT">

            <PatternLayout
                pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>

        </Console>

    </Appenders>

    <Loggers>

        <Root level="info">

            <AppenderRef ref="Console"/>

        </Root>

    </Loggers>

</Configuration>
```

### Pattern tokens

| Token | Meaning |
|---|---|
| `%t` | Thread name |
| `%-5level` | Level with width 5, left-aligned |
| `%logger{36}` | Fully qualified class name with 36 characters reserved |
| `-` | Separator |
| `%msg` | Message from `log.XXX(msg)` |
| `%n` | New line |

### Java usage (Log4j2 API)

```java
package in.pw.ioi;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class EmployeeService {

    private static final Logger log =
            LogManager.getLogger(EmployeeService.class);

    public static void main(String[] args) {

        log.trace("Trace Message");

        log.debug("Debug Message");

        log.info("Employee Saved Successfully");

        log.warn("Salary is very high");

        log.error("Database Connection Failed");

    }

}
```

### `pom.xml` dependencies

```xml
<dependencies>

    <!-- Log4j2 API -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-api</artifactId>
        <version>2.25.1</version>
    </dependency>

    <!-- Log4j2 Core -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>2.25.1</version>
    </dependency>

</dependencies>
```

### Sample output

```text
2026-07-27 10:30:15 [main] INFO  com.demo.EmployeeService - Employee Saved Successfully

2026-07-27 10:30:15 [main] WARN  com.demo.EmployeeService - Salary is very high

2026-07-27 10:30:15 [main] ERROR com.demo.EmployeeService - Database Connection Failed
```

---

## 🚀 With Spring Boot

With respect to Spring Boot, SLF4J uses **Logback** as its implementation, with pattern layout and a console appender, and default log level **INFO**.

Default configuration in `application.properties`:

```properties
logging.level.root=INFO
```

```text
SLF4J (API)
    │
    ▼
Logback (Implementation)
    │
    ├── Logger
    ├── LoggerFactory
    ├── ConsoleAppender
    ├── PatternLayoutEncoder
    └── Default Configuration
```

```java
private static final Logger logger = LoggerFactory.getLogger(EmployeeService.class);
```

```properties
logging.level.root=INFO
```

### Magic of Spring Boot

Spring Boot automatically creates a console appender with a sensible default pattern (implemented via Logback’s `PatternLayoutEncoder`) and wires everything together for you.

### Can we change the appender to file in Spring Boot?

Yes — possible with:

```properties
logging.file.name=application.log
```

> **Correction (typo in original notes):** original text used `applicaiton.log` — the property value should be a correct filename such as `application.log`. Prefer also `logging.file.path` / Logback `logback-spring.xml` for richer file rolling policies in production.

---

## 🗂️ Profiles in Spring Boot

**Question:** Will an application always run in the same environment?

**Answer:** No — it runs in different environments and each environment has different configuration.

### Scenario 1 — Different databases

**Development**

```text
URL = jdbc:mysql://localhost:3306/devdb
Username = root
Password = root
```

**Testing**

```text
URL = jdbc:mysql://192.168.10.20:3306/testdb
Username = tester
Password = test123
```

**Production**

```text
URL = jdbc:mysql://10.10.10.10:3306/proddb
Username = admin
Password = ********
```

### Scenario 2 — Email

Real email service won’t be sent during development; only in production we send real emails.

### Scenario 3 — Logging

| Environment | Setting |
|---|---|
| Development | `logging.level.root=DEBUG` |
| Production | `logging.level.root=INFO` |

### Without profiling

We constantly change configuration — database, email logic, logging level — then deploy to production.

**Solution:** use Spring Boot profiles.

### Step 1 — Separate files per environment

- `application.properties`
- `application-dev.properties`
- `application-test.properties`
- `application-prod.properties`

### How to activate a profile

In `application.properties`:

```properties
spring.profiles.active=dev
```

Now Spring Boot loads `application.properties` + `application-dev.properties` and also creates the beans suitable for that environment.

---

## 📧 Profile-specific Email Services

```java
public interface EmailService {

    void sendEmail();

}
```

```java
@Service
@Profile("dev")
public class DevEmailService implements EmailService {

    @Override
    public void sendEmail() {

        System.out.println("Dummy Email Sent");

    }

}
```

```java
@Service
@Profile("prod")
public class ProdEmailService implements EmailService {

    @Override
    public void sendEmail() {

        System.out.println("Real Email Sent");

    }

}
```

### Suggested project layout

```text
src/main/java
|
|-- in.pw.ioi
    |
    |-- SpringProfileApplication.java
    |
    |-- controller
    |      |
    |      |-- EmailController.java
    |
    |-- service
           |
           |-- EmailService.java
           |
           |-- DevEmailService.java
           |
           |-- ProdEmailService.java

src/main/resources
|
|-- application.properties
|
|-- application-dev.properties
|
|-- application-prod.properties
```

---

## 💻 Full Profile Demo Code

### `EmailService`

```java
package in.pw.ioi.service;

public interface EmailService {

    void sendEmail(String to, String subject, String body);

}
```

### `DevEmailService`

```java
package in.pw.ioi.service;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Service;

@Service
@Profile("dev")
public class DevEmailService implements EmailService {

    @Override
    public void sendEmail(String to,
                          String subject,
                          String body) {

        System.out.println("--------------------------------");
        System.out.println("Development Profile Activated");
        System.out.println("--------------------------------");

        System.out.println("Dummy Email");
        System.out.println("To      : " + to);
        System.out.println("Subject : " + subject);
        System.out.println("Body    : " + body);

        System.out.println("\nEmail NOT Sent.");
        System.out.println("Only printed for testing.");

    }

}
```

### `ProdEmailService`

```java
package in.pw.ioi.service;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Service;

@Service
@Profile("prod")
public class ProdEmailService implements EmailService {

    @Override
    public void sendEmail(String to,
                          String subject,
                          String body) {

        System.out.println("--------------------------------");
        System.out.println("Production Profile Activated");
        System.out.println("--------------------------------");

        /*
            Actual Email Logic

            JavaMailSender

            mailSender.send(...)

        */

        System.out.println("Email Sent Successfully");

    }

}
```

### `EmailController`

```java
package in.pw.ioi.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import in.pw.ioi.EmailService;

@RestController
public class EmailController {

    @Autowired
    private EmailService emailService;

    @GetMapping("/send")
    public String sendEmail() {

        emailService.sendEmail(
                "abc@gmail.com",
                "Registration",
                "Welcome to Physics Wallah");

        return "Request Processed Successfully";

    }

}
```

> **Correction:** The import `in.pw.ioi.EmailService` in the mentor notes likely should be `in.pw.ioi.service.EmailService` to match the package of the interface above.

### `SpringProfileApplication`

```java
package in.pw.ioi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringProfileApplication {

    public static void main(String[] args) {

        SpringApplication.run(
                SpringProfileApplication.class,
                args);

    }

}
```

### Properties files

`application.properties`:

```properties
spring.application.name=SpringProfileDemo
spring.profiles.active=dev
```

`application-dev.properties`:

```properties
spring.profiles.active=dev
logging.level.root=DEBUG
```

`application-prod.properties`:

```properties
spring.profiles.active=prod
logging.level.root=INFO
```

> **Correction:** Prefer setting `spring.profiles.active` only in the base `application.properties` (or via env/`SPRING_PROFILES_ACTIVE`). Repeating `spring.profiles.active` inside `application-dev.properties` / `application-prod.properties` is redundant and can be confusing.

---

## 🔄 Profile Selection Flow

```text
                EmailService
                     ▲
                     │
        -----------------------------
        │                           │
        │                           │
@Profile("dev")             @Profile("prod")
DevEmailService             ProdEmailService
(Dummy Email)               (Real Email)
        ▲                           ▲
        └──────────────┬────────────┘
                       │
         spring.profiles.active
                       │
             ┌─────────┴─────────┐
             │                   │
            dev                 prod
             │                   │
             ▼                   ▼
   DevEmailService      ProdEmailService
        Bean                  Bean
```

---

## 🤖 AI Points

1. **Production consideration:** Ship one immutable JAR/image and activate `prod` (or cloud-specific profiles) externally; never rebuild just to flip DB URLs or log levels.
2. **Industry practice:** Use `logback-spring.xml` with profile-specific appenders (JSON to stdout in containers, rolling files on VMs) rather than only `logging.file.name`.
3. **Common mistake:** Calling Log4j/`LogManager` APIs directly inside a Spring Boot app while Boot already manages Logback — prefer SLF4J (`LoggerFactory`) everywhere so the facade stays portable.
4. **Interview insight:** Describe the chain SLF4J → Logback → Appender → Layout, and how `logging.level.root` vs package-level overrides filter which logger calls actually emit.
5. **Modern Spring Boot connection:** Combine `@Profile` beans with `@ConfigurationProperties` and externalized config (env vars / Config Server) so email, DataSource, and logging differ cleanly across environments without `if (env.equals("prod"))` branches.

---

## 💻 My Codes


  
## 🖼️ Image

![Logging and profiles in Spring Boot](../IMAGES/Day-51__27-07-2026-logging-basic-and-profiling-with-springboot.png)
