
# Role of Spring Framework
## Responsibilities of Spring

a. **Scan for a class**  
b. **Create object**  
c. **Provide data to object | Link 2 objects**  
d. **Destroy the object**

---
# Bean

- A **Spring-managed object**
- Created and maintained by the **Spring Container**
---
# Configuration Details
Spring configuration can be done using:

a. **XML**  
b. **Annotation**  
c. **Pure Java**

---
# Object Types
## a. User Defined

- Programmer-defined classes
    
    - `Customer`
    - `Product`
    - `OrderService`
## b. Inbuilt

- Provided by **JRE**
## c. Coming from 3rd Party

- Provided by **Spring Framework**
---
# Dependencies Example (Diagram Explanation)
## Customer

```text
cname : "zabi"
```

- Type: **PTD (Primitive Type Dependency)**
- Injected using:
    - **Setter Injection (SI)**
---
## Product

```text
pname : "iphone16"
```

- Type: **PTD (Primitive Type Dependency)**
- Injected using:
    - **Setter Injection (SI)**
---
## OrderService

```text
Customer customer;
Product product;
```

- Type: **RTD (Reference Type Dependency)**
### Injection Used

- **Constructor Injection (CI)**
---
# Dependency Injection Flow

- `Customer` object is created
- `Product` object is created
- Both objects are **injected into OrderService**
- Linking of objects is done by **Spring Container**
---
# Dependency Types Used in Diagram
## 1. PTD – Primitive Type Dependency

- `cname`
- `pname`
---
## 2. RTD – Reference Type Dependency

- `Customer customer`
- `Product product`
---
# Injection Types Used
## Setter Injection (SI)
- Used for:
    - `Customer`
    - `Product`
### Example

```java
customer.setCname("zabi");
product.setPname("iphone16");
```
---
## Constructor Injection (CI)
- Used for:
    - `OrderService`
### Example

```java
public OrderService(Customer customer, Product product) {
    this.customer = customer;
    this.product = product;
}
```
---
# Summary

- Spring scans classes
- Creates objects
- Injects primitive and reference dependencies
- Links objects
- Manages object lifecycle
---
![[Day-05__26-09-2025-class-notes-spring annotation introduction-images.png]]
___
### **My Practice :**
1. 