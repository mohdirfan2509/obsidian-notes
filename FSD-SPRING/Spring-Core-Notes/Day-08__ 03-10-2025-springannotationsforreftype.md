# IoC Container (Spring)
## Inputs to IoC Container
- **Spring Bean**
    - Must follow Spring rules
- **Configuration Details*
    - XML
    - Annotation
    - Pure Java
---
## Role of IoC Container
- Manages the **life cycle of an object**
---
# Annotations (Basics)

- `@Component`
- `@Value`
- `@Configuration`
- `@ComponentScan`
- `@PropertySource`
---
# Life Cycle of an Object
## XML Configuration

```xml
<bean id="" class="" init-method="" destroy-method="">
```
---
## Annotation Configuration (Spring Interfaces)

- `InitializingBean`
    - `afterPropertiesSet()`
- `DisposableBean`
    - `destroy()
### Drawback
- Bean becomes **HeavyWeight**
- Bean becomes **Tightly Coupled**
---
## Solution: JSR-250 Annotations

- `@PostConstruct`
- `@PreDestroy`
---
# Maven Dependency (JSR-250)

```xml
<!-- https://mvnrepository.com/artifact/javax.annotation/javax.annotation-api -->
<dependency>
    <groupId>javax.annotation</groupId>
    <artifactId>javax.annotation-api</artifactId>
    <version>1.3.2</version>
</dependency>
```
---
# XML Configuration with Annotations Enabled
## applicationContext.xml

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>

    <bean id="service" class="com.app.service.ExcelExportService">
        <property name="fileName" value="smsdata"/>
        <property name="mode" value="xlsx"/>
    </bean>

</beans>
```
---
## Note

```text
<context:annotation-config/>
```
- Informs IoC container that **JSR annotations** are used in Spring Beans
---
# Autowiring Annotations

- `@Autowired`
- `@Qualifier`
- `@Primary`
---
# Test Application
## TestApp.java

```java
package com.app;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import com.app.config.AppConfing;
import com.app.service.StudentService;

public class TestApp {

    public static void main(String[] args) {

        ApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfing.class);

        String[] beanNames = container.getBeanDefinitionNames();
        for (String bean : beanNames) {
            System.out.println(bean);
        }

        StudentService service =
                container.getBean("service", StudentService.class);
        System.out.println(service);

        ((AbstractApplicationContext) container).close();
    }
}
```
---
# Repository Layer
## IStudentRepo.java

```java
package com.app.repo;

public interface IStudentRepo {
}
```
---
## StudentRepoImpl1.java

```java
package com.app.repo;

import org.springframework.stereotype.Component;

@Component("std1")
public class StudentRepoImpl1 implements IStudentRepo {
}
```
---
## StudentRepoImpl2.java

```java
package com.app.repo;

import org.springframework.stereotype.Component;

@Component("std2")
public class StudentRepoImpl2 implements IStudentRepo {
}
```
---
# Service Layer
## StudentService.java

```java
package com.app.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.app.repo.IStudentRepo;

@Component("service")
public class StudentService {

    @Autowired(required = false)
    private IStudentRepo repo;

    @Override
    public String toString() {
        return "StudentService [repo=" + repo + "]";
    }
}
```
---
![[Day-08__03-10-2025-springannotationsforreftype-images.png]]
___
### **My Practice :**
1. 