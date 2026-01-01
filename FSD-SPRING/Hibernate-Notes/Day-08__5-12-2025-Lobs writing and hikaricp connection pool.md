
# Working with LOBs (Read Operation)
## Annotations Used

```java
@Lob
```
---
## Copying Data from Input to Output Channel
### Utility Method Used

```java
IOUtils.copy(source, destination);
```
### Supported Streams

- `InputStream` → `FileOutputStream`
- `Reader` → `FileWriter`
---
## Data Representation

```text
jobSeeker:
    image  -> byte[]
    resume -> char[]
```
---
## Writing LOB Data to Files
### Output Streams

```java
FileOutputStream fos = new FileOutputStream("copied.jpg");
FileWriter fw = new FileWriter("copy_resume.txt");
```
### Write Using IOUtils

```java
IOUtils.write(jobSeeker.getImage(), fos);
IOUtils.write(jobSeeker.getResume(), fw);
```
---
## Reading LOB Data Using Streams
### Binary Data (Image)

```java
InputStream is = new ByteArrayInputStream(jobSeeker.getImage());
IOUtils.copy(is, fos);
```
---
### Character Data (Resume)

```java
Reader r = new CharArrayReader(jobSeeker.getResume());
IOUtils.copy(r, fw);
```
---
# Connection Pooling
## Hibernate Connection Pooling Types

- **Inbuilt connection pooling**
- **External supplied connection pooling** (3rd party vendor)
---
# Working with HikariCP Connection Pooling
## a. Maven Dependency
### pom.xml

```xml
<!-- https://mvnrepository.com/artifact/com.zaxxer/HikariCP -->
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-hikaricp</artifactId>
    <version>7.1.4.Final</version>
</dependency>
```
---
## b. Hibernate Configuration
### hibernate.cfg.xml

```xml
<property name="hibernate.connection.provider_class">
    org.hibernate.hikaricp.internal.HikariCPConnectionProvider
</property>

<!-- HikariCP Properties -->
<property name="hibernate.hikari.maximumPoolSize">20</property>
<property name="hibernate.hikari.idleTimeout">300000</property>      <!-- 5 min -->
<property name="hibernate.hikari.connectionTimeout">20000</property> <!-- 20 sec -->
<property name="hibernate.hikari.maxLifetime">1800000</property>     <!-- 30 min -->
<property name="hibernate.hikari.poolName">MyHikariPool</property>
```
---
# Testing the Application

```text
Run any code
```
---
# Output

```text
Instantiating explicit connection provider:
org.hibernate.hikaricp.internal.HikariCPConnectionProvider
```
---
![[Day-08__5-12-2025-Lobs writing and hikaricp connection pool-images.png]]
___
### **My Practice :**
1. 