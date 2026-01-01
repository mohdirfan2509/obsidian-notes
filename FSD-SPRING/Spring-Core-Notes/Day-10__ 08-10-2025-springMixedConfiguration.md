# @Component vs @Bean (Object Creation Priority)
---
## Example 1: `@Component` and `@Bean` Together
---
### Service Bean (`@Component`)

```java
package com.app.bean;

import org.springframework.stereotype.Component;

@Component
public class Service {

    public Service() {
        System.out.println("Object created using @Component...");
    }

    public void doWork() {
        System.out.println("I am doing work.....");
    }
}
```
---
### Configuration Class (`@Bean` Method)

```java
package com.app.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.app.bean.Service;

@Configuration
@ComponentScan("com.app")
public class AppConfig {

    @Bean
    public Service service() {
        System.out.println("Object created using @Bean method");
        Service service = new Service();
        return service;
    }
}
```
---
### Test Application

```java
package com.app;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import com.app.bean.Service;
import com.app.config.AppConfig;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // 1. Start the container
        AnnotationConfigApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfig.class);

        System.out.println(
            container.getBeanDefinition("service").getResourceDescription()
        );

        // 2. Get the bean
        Service service =
                container.getBean("service", Service.class);

        // 3. Use the bean
        service.doWork();

        // 4. Close the container
        ((AbstractApplicationContext) container).close();
    }
}
```
---
### Output

```text
Object created using @Bean method
Object created using @Component...
com.app.config.AppConfig
I am doing work.....
```
---
### Note

```text
@Bean will override the @Component annotation based object creation.
```
---
# Example 2: Missing Bean and `@Autowired(required = false)`
---
### Controller Bean

```java
package com.app.bean;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component("controller")
public class Controller {

    @Autowired(required = false)
    private Service service;

    public void sayHello() {
        service.doWork();
    }
}
```
---
### Service Class (No `@Component`)

```java
package com.app.bean;

// @Component
public class Service {

    public void doWork() {
        System.out.println("I am doing work.....");
    }
}
```
---
### Configuration Class

```java
package com.app.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.app")
public class AppConfig {
}
```
---
### Test Application

```java
package com.app;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import com.app.bean.Controller;
import com.app.config.AppConfig;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // 1. Start the container
        AnnotationConfigApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfig.class);

        // 2. Get the bean
        Controller c =
                container.getBean("controller", Controller.class);

        // 3. Use the bean
        c.sayHello();

        // 4. Close the container
        ((AbstractApplicationContext) container).close();
    }
}
```
---
### Output

```text
java.lang.NullPointerException
```
---
## Reason (From Given Data)

- `Service` is **not annotated with `@Component`**
- No `@Bean` method is provided
- `@Autowired(required = false)` allows **null injection**
- Calling `service.doWork()` results in **NullPointerException**
---
![[Day-10__08-10-2025-springMixedConfiguration-images.png]]
___
### **My Practice :**
1. 