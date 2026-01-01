# Spring Bean
## Rules for a Spring Bean

1. **Class must be public**

```java
public class MyBean {
}
```
---
2. **Class must be inside a package**
- Must be in **base package** or **sub-package**

```java
package com.example.beans;
```
---
3. **Variables should be private**
- Methods should be **public**

```java
public class MyBean {
    private int id;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
```
---
4. **Constructor Requirement**
- Either:
    - Default constructor + setters/getters  
        **OR**
    - Parameterized constructor  
        **OR**
    - Both are valid


```java
public class MyBean {

    private int id;

    public MyBean() {
    }

    public MyBean(int id) {
        this.id = id;
    }
}
```
---
5. **Overriding Object Class Methods**
- Allowed methods:
    - `toString()`
    - `equals()`
    - `hashCode()`

```java
@Override
public String toString() {
    return "MyBean";
}
```
---
6. **Inheritance Rule**
- A Spring Bean:
    - Can `extend` or `implement` **other Spring Beans**
    - Cannot extend or implement:
        - Servlets
        - EJB            
        - Other external APIs
---
7. **Serializable Interface (Optional)**

```java
public class MyBean implements java.io.Serializable {
}
```
---
## Annotations Used in Spring Beans

- Core Annotations (java.lang package)
- **Spring Framework Annotations**
- Integration Annotations (JPA / etc.)
---
# Spring Container
## (Spring IoC – Inversion of Control)
---
## Responsibilities of Spring Container

1. **Find / Scan classes**
2. **Create objects**
3. **Provide data and link objects**
4. **Destroy objects / container**
---
## Inputs to Spring Container
Spring Container requires **two inputs**:
### A) Spring Bean
- Class + rules
### B) Spring Configuration File

- XML
- Java
- Annotation
---
![Maven and Spring Life Cycle](../Spring-Core-images/Day-02__23-09-2025-classnotes-Maven%20and%20Spring%20life%20cycle-images.png)
___
### **My Practice :**
1. 