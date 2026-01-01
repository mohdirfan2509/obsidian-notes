
# Dependency Injection Example (Constructor + Setter Injection)
---
## Product Bean

```java
package com.app.bean;

public class Product {

    private String pname;

    public String getPname() {
        return pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }

    @Override
    public String toString() {
        return "Product [pname=" + pname + "]";
    }
}
```
---
## Customer Bean

```java
package com.app.bean;

public class Customer {

    private String cname;

    public Customer() {
    }

    public String getCname() {
        return cname;
    }

    public void setCname(String cname) {
        this.cname = cname;
    }

    @Override
    public String toString() {
        return "Customer [cname=" + cname + "]";
    }
}
```
---
## OrderService Bean (Constructor Injection)

```java
package com.app.bean;

public class OrderService {

    private Customer customer;
    private Product product;

    public OrderService(Customer customer, Product product) {
        super();
        this.customer = customer;
        this.product = product;
    }

    // Business Logic
    public void order() {
        System.out.println(
            product.getPname() +
            "  is purchsed from the customer :   " +
            customer.getCname()
        );
    }
}
```
---
# Spring Configuration (applicationContext.xml)
## Using Setter and Constructor Injection

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <!-- Setter Injection -->
    <bean class="com.app.bean.Customer" id="customer">
        <property name="cname" value="Zabi"/>
    </bean>

    <!-- Setter Injection -->
    <bean class="com.app.bean.Product" id="product">
        <property name="pname" value="iPhone16"/>
    </bean>

    <!-- Constructor Injection -->
    <bean class="com.app.bean.OrderService" id="service">
        <constructor-arg name="customer" ref="customer"/>
        <constructor-arg name="product" ref="product"/>
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

import com.app.bean.OrderService;

public class TestApp {

    public static void main(String[] args) {

        // 1. Start the container
        ApplicationContext container =
                new ClassPathXmlApplicationContext("applicationContext.xml");

        // 2. Get the bean
        OrderService service = container.getBean(OrderService.class);

        // 3. Use the bean
        service.order();

        // 4. Close the container
        ((AbstractApplicationContext) container).close();
    }
}
```
---
## Output

```text
iPhone16  is purchsed from the customer :   Zabi
```
---
# Working with Namespace (Shortcut)

- Useful when **number of arguments is more**
- Simplifies Dependency Injection syntax
---
## Namespaces

```xml
xmlns:p="http://www.springframework.org/schema/p"
xmlns:c="http://www.springframework.org/schema/c"
```
---
## Normal Syntax

```xml
<bean id="" class="">
    <property name="" value=""/>
    <constructor name="" value=""/>
    <property name="" ref=""/>
    <constructor name="" ref=""/>
</bean>
```
---
## Shortcut Syntax

```xml
<bean id="" class="" p:variableName=""/>
<bean id="" class="" p:variableName-ref=""/>
<bean id="" class="" c:variableName=""/>
<bean id="" class="" c:variableName-ref=""/>
```
---
# applicationContext.xml (Using p & c Namespace)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:p="http://www.springframework.org/schema/p"
       xmlns:c="http://www.springframework.org/schema/c"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd">

    <!-- Setter Injection -->
    <bean class="com.app.bean.Customer" id="customer" p:cname="Nitin"/>

    <!-- Setter Injection -->
    <bean class="com.app.bean.Product" id="product" p:pname="MACM4"/>

    <!-- Constructor Injection -->
    <bean class="com.app.bean.OrderService" id="service"
          c:product-ref="product"
          c:customer-ref="customer"/>
</beans>
```
---
![[Day-04__25-09-2025-class-notes-FirstSpringApp-notes-images.png]]
___
### **My Practice :**
1. 