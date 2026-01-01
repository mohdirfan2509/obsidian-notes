# IoC Container (Spring)
## Inputs to IoC Container
a. **Spring Bean**
- Must follow Spring rules
b. **Configuration Details**

- XML
- Annotation
- Pure Java
---
## Role of IoC Container
- Manages the **lifecycle of an object**
---
# Configuration Using XML
## XML Elements

```xml
<bean id="" class=""/>
<property name="" value="" ref=""/>
<constructor-arg name="" value="" ref=""/>
```
---
## Namespaces

- **p-namespace**
- **c-namespace**
---
# Configuration Using Annotations
## Common Annotations

- `@Component`
- `@Configuration`
- `@ComponentScan(basePackages={""})`
- `@PropertySource("classpath:*.properties")`
- `@Value("${keyName}")`
---
# Lifecycle Methods of an Object
## Using XML Configuration
---
## Test Application
### TestApp.java

```java
package com.app;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.app.service.ExcelExportService;

public class TestApp {

    public static void main(String[] args) throws Exception {

        // 1. Start the container
        ApplicationContext container =
                new ClassPathXmlApplicationContext("applicationContext.xml");

        // 2. Get the bean
        ExcelExportService service =
                container.getBean("service", ExcelExportService.class);

        // 3. Use the bean
        System.out.println(service);

        // 4. Close the container
        Thread.sleep(5000);
        ((AbstractApplicationContext) container).close();
    }
}
```
---
## Service Class
### ExcelExportService.java

```java
package com.app.service;

public class ExcelExportService {

    private String fileName;
    private String mode;

    static {
        System.out.println("ExcelExportService.class file is loading...");
    }

    public ExcelExportService() {
        System.out.println("ExcelExportService object is created by Spring F/w...");
    }

    public void initLogic() {
        System.out.println(
            "********Some logic to process before calling the method*********");
    }

    public void cleanUpLogic() {
        System.out.println(
            "********Some logic to process after calling the method*********");
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    @Override
    public String toString() {
        return "ExcelExportService [fileName=" + fileName +
               ", mode=" + mode + "]";
    }
}
```
---
## XML Configuration
### applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="service"
          class="com.app.service.ExcelExportService"
          init-method="initLogic"
          destroy-method="cleanUpLogic">

        <property name="fileName" value="sample"/>
        <property name="mode" value="csv"/>
    </bean>

</beans>
```
---
## Output

```text
ExcelExportService.class file is loading...
ExcelExportService object is created by Spring F/w...
********Some logic to process before calling the method*********
ExcelExportService [fileName=sample, mode=csv]
********Some logic to process after calling the method*********
```
---
![[Day-07__30-09-2025-spring-lifecycle-methods.png]]
___
### **My Practice :**
1. 