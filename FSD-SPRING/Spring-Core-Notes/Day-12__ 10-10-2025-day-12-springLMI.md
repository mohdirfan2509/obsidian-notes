# Bean Scope in Spring
## Types of Scope
a. **Singleton**  
b. **Prototype**

---
## Eager Loading
- As soon as the **container starts**, the **bean life cycle actions** begin  
    (Loading, Instantiation, Initialization, …)
- Happens **only when the bean scope is `singleton`**
---
## Lazy Loading
- Bean life cycle actions are performed **only when the bean is requested**
- Happens when the bean scope is **`prototype`**
- **IoC cache is not needed**
---
## Important Questions
### Can the container perform Lazy Loading for singleton scope beans?
**Ans:** Yes, possible using

```xml
lazy-init="true"
```
---
### Can the container perform Eager Loading for prototype scope beans?
**Ans:** Not possible.

---
### Can we set two different scopes for a single bean?
**Ans:** Not possible.

---
# LookUp Method Injection (LMI)
## Solution Statement

- Programmer **cannot handle memory-related operations** in Spring/Java
- Memory handling is done **only by Spring Framework**
---
## Rules to Follow
_(Only in Dependent / Parent class)_  
_(No code changes in Child / Dependency class)_

1. Define a method that returns **child / dependency class**
    - Method body should return `null`
2. Add `@Lookup` annotation on the method
3. Call this method inside `getter`, `toString()`, or any required place
---
# LookUp Method Injection Example
---
## TokenService (Dependent / Parent Class)

```java
package com.app.bean;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Lookup;
import org.springframework.stereotype.Component;

@Component
public class TokenService {

    @Autowired
    private Token token;

    public Token getToken() {
        token = getMyToken();
        return token;
    }

    // logic for LookUp method
    @Lookup
    public Token getMyToken() {
        // .....
        return token;
    }

    @Override
    public String toString() {
        return "TokenService [token=" + token + "]";
    }
}
```
---
## Token Bean (Dependency / Child Class)

```java
package com.app.bean;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope("prototype")
public class Token {

    @Value("#{new java.util.Random().nextInt(1000)}")
    private Integer code;

    @Override
    public String toString() {
        return "Token [code=" + code + "]";
    }
}
```
---
## Java Configuration Class

```java
package com.app.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = "com.app.bean")
public class AppConfig {
}
```
---
## Test Application

```java
package com.app;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import com.app.bean.TokenService;
import com.app.config.AppConfig;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // 1. Start the container
        AnnotationConfigApplicationContext container =
                new AnnotationConfigApplicationContext(AppConfig.class);

        // 1st time
        TokenService t1 = container.getBean(TokenService.class);
        System.out.println(t1.hashCode() + "----> " + t1.getToken().hashCode());
        System.out.println(t1);
        System.out.println("********************************************");

        // 2nd time
        TokenService t2 = container.getBean(TokenService.class);
        System.out.println(t2.hashCode() + "----> " + t2.getToken().hashCode());
        System.out.println(t2);
        System.out.println("********************************************");

        // 3rd time
        TokenService t3 = container.getBean(TokenService.class);
        System.out.println(t3.hashCode() + "----> " + t3.getToken().hashCode());
        System.out.println(t3);

        // Close the container
        ((AbstractApplicationContext) container).close();
    }
}
```
---
## Output

```text
1325144078----> 1432536094
TokenService [token=Token [code=944]]
********************************************
1325144078----> 259219561
TokenService [token=Token [code=227]]
********************************************
1325144078----> 2146338580
TokenService [token=Token [code=620]]
```
---
## Observation from Output
- `TokenService` hashCode remains **same** → **Singleton**
- `Token` hashCode changes every time → **Prototype**
- `@Lookup` ensures **new prototype object** is injected each time
---
![[Day-12__10-10-2025-springLMI-images.png]]
___
### **My Practice :**
1. 