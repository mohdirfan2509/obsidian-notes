# Spring Bean Scope
## Scope
- Scope indicates **variable / object access limits and lifetime**
---
## Scope in Core Java

- **Local Scope** → Block scope
- **Instance / Object Scope** → Object creation to destruction
- **Static Scope** → Class loading to unloading
---
## Scope in Advanced Java (Servlets)

1. **Page Scope** (JSP)
2. **Request Scope** → Until response is given
3. **Session Scope** → Login to Logout
4. **Application / Context Scope** → Server start to stop
---
## Scope in Spring
### 1. Singleton (Default Scope)

- Only **one object** is created by Spring container per configuration
- Mapping:

```text
1 <bean> = 1 object = 1 @Bean = 1 @Component
```

Example:

```xml
<bean id="a1" class="A"/>
<bean id="a2" class="A"/>
```
---
### 2. Prototype
- Creates a **new object on every access**
---
### 3. Request (Web Application)
- Creates a new object **for every request**
---
### 4. Session (Web Application)
- Creates a new object **when session is created / login success**
---
# XML Configuration Example (Prototype Scope)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean class="com.app.bean.Student"
          id="student"
          lazy-init="true
          scope="prototype">

        <!-- Setter Injection -->
        <property name="sid" value="10"/>
        <property name="sname" value="sachin"/>
        <property name="saddress" value="IND"/>
    </bean>

</beans>
```
---
# Test Application

```java
package com.app;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.app.bean.Student;

public class TestApp {

    public static void main(String[] args) throws Exception {

        System.out.println("**************Container Started*******************");

        ApplicationContext container =
                new ClassPathXmlApplicationContext("applicationContext.xml");

        Student s1 = container.getBean(Student.class);
        Student s2 = container.getBean(Student.class);

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s1 == s2);

        ((AbstractApplicationContext) container).close();
        System.out.println("**************Container Stopped*******************");
    }
}
```
---
# Student Bean

```java
package com.app.bean;

public class Student {

    private Integer sid;
    private String sname;
    private String saddress;

    static {
        System.out.println("****Bean Loading*******");
    }

    public Student() {
        System.out.println("****Bean Instantiation*******");
    }

    public void setSid(Integer sid) {
        System.out.println("****Bean Initialization**********");
        this.sid = sid;
    }

    public void setSname(String sname) {
        this.sname = sname;
    }

    public void setSaddress(String saddress) {
        this.saddress = saddress;
    }

    @Override
    public String toString() {
        return "Student [sid=" + sid +
               ", sname=" + sname +
               ", saddress=" + saddress + "]";
    }
}
```
---
# Output

```text
**************Container Started*******************
****Bean Loading*******
****Bean Instantiation*******
****Bean Initialization**********
****Bean Instantiation*******
****Bean Initialization**********
Student [sid=10, sname=sachin, saddress=IND]
Student [sid=10, sname=sachin, saddress=IND]
false
**************Container Stopped*******************
```
---
# FAQ
## What is Singleton Class and Singleton Scope?
- **Singleton Class**
    - Design pattern ensuring **only one object** is created for a class
- **Singleton Scope**
    - Even with multiple requests, **only one object** is created

```xml
<bean id="s1" class="com.app.Student"/>  <!-- Singleton -->
<bean id="s2" class="com.app.Student"/>  <!-- Singleton -->
```
---
# Annotation Approach
## Annotations Used
- `@Scope`
- `@Lazy
### Example

```java
@Component("s1")
@Scope("prototype")
@Lazy
public class Student {
    ...
}
```
---
# Pure Java Configuration

```java
package com.app.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Lazy;
import org.springframework.context.annotation.Scope;

import com.app.bean.Student;

@Configuration
@Lazy
public class AppConfig {

    @Bean
    public Student std1() {
        Student s1 = new Student();
        s1.setSname("kohli");
        s1.setSid(18);
        s1.setSaddress("RCB");
        return s1;
    }

    @Bean
    @Scope("prototype")
    public Student std2() {
        Student s1 = new Student();
        s1.setSname("dhoni");
        s1.setSid(7);
        s1.setSaddress("CSK");
        return s1;
    }
}
```
---
# Notes
- By default, Spring container uses **Eager Loading**
- To enable **Lazy Loading**, use:

```java
@Lazy
```

- Default bean scope is **singleton**    
- To change scope:

```java
@Scope("prototype")
```
---
![[Day-11__09-10-2025-spring bean scope-images.png]]
___
### **My Practice :**
1. 