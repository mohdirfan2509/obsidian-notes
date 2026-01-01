# IoC Container (Spring)
## Inputs to IoC Container

1. **Spring Bean**
    - Class that follows Spring rules
2. **Configuration Details**
    - XML
    - Annotation
    - Pure Java
---
## Role of IoC Container

- Manages the **lifecycle of the object**
---
# Configuration (XML Based)
## Elements Used

```xml
<bean id="" class="">
<property name="" value="" ref=""/>
<constructor-arg name="" value="" ref=""/>
```
---
## Using Namespace

- **p-namespace**
- **c-namespace**
---
# Configuration Using Annotations
## Common Spring Annotations

- `@Component` – Creates an object
- `@ComponentScan` – Informs container where `@Component` classes exist
- `@Configuration` – Marks class as configuration provider
- `@Value` – Field injection
    
    - Direct value
    - Properties file
    - SPEL
- `@Controller`
- `@Service`
- `@Repository`
- `@Autowired`
- `@Qualifier`
- `@Primary`
- `@PostConstruct`
- `@PreDestroy`
---
# @Value Annotation
## Getting Data from Properties File
---
# Properties File
## Definition

- Text file that stores **critical data**
- Data format: `key = value`
## Rules

- Keys are **case-sensitive**
- If same key appears multiple times, **last value is considered**
- `#` indicates a **comment**
- Allowed symbols in key:

    - `_` (underscore)        
    - `.` (dot)
    - `-` (dash)
- **Auto parsing supported** based on variable datatype
- By default:
    - Key → String
    - Value → String
### Example

```text
app.sid=200
```

- `app.sid` → String
- `200` → String
---
## mydata.properties

```properties
my.data.id=10
my.data.name=sachin
my.data.age=55
```
---
# Student Bean (Using @Value)
## Student.java

```java
package com.app.bean;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class Student {

    @Value("${my.data.id}")
    private Integer sid;

    @Value("${my.data.name}")
    private String sname;

    @Value("${my.data.age}")
    private Integer sage;

    @Value("${my.data.address:IND}")
    private String saddress;

    public Student() {
        System.out.println("Student object created using Spring F/w....");
    }

    @Override
    public String toString() {
        return "Student [sid=" + sid + ", sname=" + sname +
               ", sage=" + sage + ", saddress=" + saddress + "]";
    }
}
```
---
# Java Configuration Class
## AppConfig.java

```java
package com.app.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@ComponentScan(basePackages = {"com.app.bean"})
@PropertySource("classpath:mydata.properties")
public class AppConfig {
}
```
---
# Test Application
## TestApp.java

```java
package com.app;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.app.bean.Student;
import com.app.config.AppConfig;

public class TestApp {

    public static void main(String[] args) {

        // 1. Start the container
        AnnotationConfigApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfig.class);

        // 2. Get the bean
        Student std = container.getBean("student", Student.class);

        // 3. Use the bean
        System.out.println(std);

        // 4. Close the container
        container.close();
    }
}
```
---
# Output

```text
Student object created using Spring F/w....
Student [sid=10, sname=sachin, sage=55, saddress=IND]
```
---
![[Day-06__29-09-2025-spring-with properties - introduction-images.png]]
___
### **My Practice :**
1. 