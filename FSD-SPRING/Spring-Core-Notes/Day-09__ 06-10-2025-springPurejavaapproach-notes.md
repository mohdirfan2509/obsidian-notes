# IoC Container
## Inputs to IoC Container
a. **Spring Bean**
- Must follow **Spring rules**
b. **Configuration Details**

- XML
- Annotation
- Pure Java
---
## Role of IoC Container

- Manages the **life cycle of an object**
- From **creation to destruction**
---
# Configuration Details
## a. XML Configuration
### Elements (Tags)

```xml
<bean id="" class="" init-method="" destroy-method=""/>
<property name="" value="" ref=""/>
<constructor-arg name="" value="" ref=""/>
```
### Namespaces

- **p-namespace**
- **c-namespace**
---
## b. Annotation Configuration
### Common Annotations

```java
@Component("ref")
@ComponentScan(basePackages = "")
@Configuration
@Value("")
@PropertySource("classpath:...")
```
---
### @Autowired
- Used to **link two objects**
#### Default Behavior

```java
@Autowired(required = true)
```

- Throws: `NoSuchBeanDefinitionException` (if bean not found)

```java
@Autowired(required = false)
```

- **No exception** if bean not found    
---
### Multiple Bean Issue
- If **2 beans are found**:
    - Exception: `NoUniqueBeanDefinitionException`
#### Solution

- `@Primary`
- `@Qualifier("ref")` → High priority
---
### Interview Question
**Q. When to use Annotation approach to configure a container?**
**Ans.**
- If the bean is **user-defined**
- `@Component` creates **only one object per bean**
---
## c. Life Cycle Methods
### XML Based
- Method names are **not predefined**

```xml
init-method=""
destroy-method=""
```
---
### Annotation Based (Interfaces)
- `InitializingBean`
- `DisposableBean`
---
### JSR-250 (Recommended)
- `@PostConstruct`
- `@PreDestroy`
- Method names are **not predefined**
---
# Pure Java Configuration
## When to Use Pure Java Configuration?
**Ans.**
- When the bean is:
    - **User-defined**
    - **Predefined**
- When **multiple objects** need to be created for the **same bean**
---
## Syntax

```java
@Configuration
public class AppConfig {

    @Bean
    public ClassName refName() {
        // Logic to create the bean
    }
}
```
---
### Notes
- **One `@Bean` = One Object**
- To know how an object is created by Spring:

```java
container.getBeanDefinition("ref")
         .getResourceDescription();
```
---
## Example 1: Pure Java Configuration
### AppConfig.java

```java
package com.app.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.app.bean.Token;

@Configuration
@ComponentScan(basePackages = "com.app")
public class AppConfig {

    @Bean
    public Token obj1() {
        Token token = new Token();
        token.setCode(10);
        return token;
    }

    @Bean
    public Token obj2() {
        Token token = new Token();
        token.setCode(10);
        return token;
    }
}
```
---
# Java Configuration to Bind Data from Properties File
---
## Test Application
### TestApp.java

```java
package com.app;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import com.app.bean.DbConfig;
import com.app.config.AppConfig;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // 1. Start the container
        AnnotationConfigApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfig.class);

        String[] names = container.getBeanDefinitionNames();
        for (String bean : names) {
            System.out.println(bean);
        }

        String msg =
                container.getBeanDefinition("obj").getResourceDescription();
        System.out.println(msg);

        // 2. Get the bean
        DbConfig config = container.getBean(DbConfig.class);

        // 3. Use the bean
        System.out.println(config);

        // 4. Close the container
        ((AbstractApplicationContext) container).close();
    }
}
```
---
## Bean Class
### DbConfig.java

```java
package com.app.bean;

public class DbConfig {

    private String username;
    private String password;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public String toString() {
        return "DbConfig [username=" + username +
               ", password=" + password + "]";
    }
}
```
---
## Configuration Class
### AppConfig.java

```java
package com.app.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;

import com.app.bean.DbConfig;

@Configuration
@PropertySource("classpath:myDb.properties")
public class AppConfig {

    @Autowired
    private Environment env;

    @Bean
    public DbConfig obj() {
        System.out.println("***************************");

        DbConfig config = new DbConfig();
        config.setUsername(env.getProperty("my.db.userName"));
        config.setPassword(env.getProperty("my.db.password"));

        return config;
    }
}
```
---
## Properties File

```properties
my.db.userName=root
my.db.password=root123
```
---
![[Day-09__06-10-2025-springPurejava-images.png]]
___
### **My Practice :**
1. 