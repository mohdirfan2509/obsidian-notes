
# Session (L1 Cache)
## Student – L1 Cache Behavior

```java
// Check in L1 → not there
// Check in L2 → not there
// Hit DB → select query is generated
Student std = session.find(Student.class, 1);
System.out.println(std);

System.in.read(); // Thread is paused

// Get it from L1 Cache
std = session.find(Student.class, 1);
System.out.println(std);

// Remove from L1 Cache
session.evict(std);
System.out.println("Object is removed from L1Cache");

System.in.read(); // Thread is paused

// Hit DB → select query is generated
std = session.find(Student.class, 1);
System.out.println(std);
```
---
# SessionFactory Cache (L2 Cache)
## 1. Maven Dependencies
### pom.xml

```xml
<dependencies>

    <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>7.1.0.Final</version>
    </dependency>

    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.3.0</version>
    </dependency>

    <dependency>
        <groupId>org.ehcache</groupId>
        <artifactId>ehcache</artifactId>
        <version>3.10.8</version>
    </dependency>

    <!-- JCache API -->
    <dependency>
        <groupId>javax.cache</groupId>
        <artifactId>cache-api</artifactId>
        <version>1.1.1</version>
    </dependency>

    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>2.0.7</version>
    </dependency>

    <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-jcache</artifactId>
        <version>7.1.0.Final</version>
    </dependency>

    <dependency>
        <groupId>jakarta.xml.bind</groupId>
        <artifactId>jakarta.xml.bind-api</artifactId>
        <version>4.0.2</version>
    </dependency>

    <dependency>
        <groupId>org.glassfish.jaxb</groupId>
        <artifactId>jaxb-runtime</artifactId>
        <version>4.0.2</version>
    </dependency>

</dependencies>
```
---
## 2. Hibernate Configuration
### hibernate.cfg.xml

```xml
<property name="hibernate.cache.use_second_level_cache">true</property>
<property name="hibernate.cache.use_query_cache">true</property>

<!-- JCache Region Factory -->
<property name="hibernate.cache.region.factory_class">
    org.hibernate.cache.jcache.JCacheRegionFactory
</property>

<!-- Caching provider -->
<property name="hibernate.jcache.provider">
    org.ehcache.jsr107.EhcacheCachingProvider
</property>

<!-- Ehcache XML location -->
<property name="hibernate.jcache.uri">classpath:/ehcache.xml</property>
```
---
## 3. Ehcache Configuration
### ehcache.xml
_(Location: `src/main/resources`)_

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config xmlns="http://www.ehcache.org/v3"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.ehcache.org/v3 
                            https://www.ehcache.org/schema/ehcache-core.xsd">

    <cache alias="Student">
        <key-type>java.lang.Long</key-type>
        <value-type>in.pw.ioi.entity.Student</value-type>

        <expiry>
            <ttl unit="minutes">10</ttl>
        </expiry>

        <resources>
            <heap unit="entries">1000</heap>
        </resources>
    </cache>

    <cache alias="org.hibernate.cache.internal.StandardQueryCache">
        <key-type>java.lang.String</key-type>
        <value-type>java.lang.Object</value-type>
        <resources>
            <heap unit="entries">200</heap>
        </resources>
    </cache>

    <cache alias="org.hibernate.cache.spi.UpdateTimestampsCache">
        <key-type>java.lang.String</key-type>
        <value-type>java.lang.Long</value-type>
        <resources>
            <heap unit="entries">200</heap>
        </resources>
    </cache>

</config>
```
---
# Test Application (L1 + L2 Cache Flow)

```java
SessionFactory factory =
        new Configuration().configure().buildSessionFactory();
Session session = factory.openSession();

// L1 → not there, L2 → not there
// Hit DB → select query is generated
Student std = session.find(Student.class, 1);
System.out.println(std);

System.in.read(); // Thread is paused

// Get it from L1 Cache
std = session.find(Student.class, 1);
System.out.println(std);

// Remove from L1 Cache
session.evict(std);
System.out.println("Object is removed from L1Cache");

System.in.read(); // Thread is paused

// L1 → not there, L2 → available
// L2 → L1 → Application
std = session.find(Student.class, 1);
System.out.println(std);

System.in.read(); // Thread is paused

// L1 → available
std = session.find(Student.class, 1);
System.out.println(std);

// Remove all objects from L1 Cache
session.clear();

System.in.read();

// Remove from L2 Cache
factory.getCache().evictEntityData(Student.class, 11);
System.out.println("Removed from L2 Cache...");

System.in.read();

// L1 → not there, L2 → not there
// Hit DB → select query is generated
std = session.find(Student.class, 1);
System.out.println(std);
```
---
# Maven Dependencies : 

```xml
<dependencies>  
  
       <dependency>  
<groupId>org.hibernate.orm</groupId>  
<artifactId>hibernate-core</artifactId>  
<version>7.1.0.Final</version>  
</dependency>  
  
<!-- [https://mvnrepository.com/artifact/com.mysql/mysql-connector-j](https://mvnrepository.com/artifact/com.mysql/mysql-connector-j) -->  
       <dependency>  
        <groupId>com.mysql</groupId>  
        <artifactId>mysql-connector-j</artifactId>  
        <version>8.3.0</version>  
       </dependency>  
         
       <!-- [https://mvnrepository.com/artifact/org.ehcache/ehcache](https://mvnrepository.com/artifact/org.ehcache/ehcache) -->  
       <dependency>  
        <groupId>org.ehcache</groupId>  
        <artifactId>ehcache</artifactId>  
        <version>3.10.8</version>  
       </dependency>  
                 
       <!-- JCache API -->  
    <dependency>  
    <groupId>javax.cache</groupId>  
    <artifactId>cache-api</artifactId>  
    <version>1.1.1</version>  
    </dependency>  
  
<dependency>  
<groupId>org.slf4j</groupId>  
<artifactId>slf4j-simple</artifactId>  
<version>2.0.7</version>  
</dependency>  
  
<dependency>  
    <groupId>org.hibernate.orm</groupId>  
    <artifactId>hibernate-jcache</artifactId>  
    <version>7.1.0.Final</version>  
   </dependency>  
     
   <dependency>  
        <groupId>jakarta.xml.bind</groupId>  
        <artifactId>jakarta.xml.bind-api</artifactId>  
        <version>4.0.2</version>  
       </dependency>  
  
       <dependency>  
        <groupId>org.glassfish.jaxb</groupId>  
        <artifactId>jaxb-runtime</artifactId>  
        <version>4.0.2</version>  
       </dependency>
```
___
```xml
<property name=_"hibernate.cache.use_second_level_cache"_>true</property>  
<property name=_"hibernate.cache.use_query_cache"_>true</property>  
  
<!-- JCache Region Factory -->  
<property name=_"hibernate.cache.region.factory_class"_>  
org.hibernate.cache.jcache.JCacheRegionFactory  
</property>  
  
<!-- Caching provider -->  
<property name=_"hibernate.jcache.provider"_>  
           org.ehcache.jsr107.EhcacheCachingProvider  
       </property>  
  
<!-- Ehcache XML location -->  
<property name=_"hibernate.jcache.uri"_>classpath:/ehcache.xml</property>
```
___
```xml
<?xml version=_"1.0"_ encoding=_"UTF-8"_?>  
<config xmlns=_"_[_http://www.ehcache.org/v3_](http://www.ehcache.org/v3)_"_  
xmlns:xsi=_"_[_http://www.w3.org/2001/XMLSchema-instance_](http://www.w3.org/2001/XMLSchema-instance)_"_  
xsi:schemaLocation=_"_[_http://www.ehcache.org/v3_](http://www.ehcache.org/v3)  
[_https://www.ehcache.org/schema/ehcache-core.xsd_](https://www.ehcache.org/schema/ehcache-core.xsd)_"_>  
  
<cache alias=_"Student"_>  
<key-type>java.lang.Long</key-type>  
<value-type>in.pw.ioi.entity.Student</value-type>  
  
<expiry>  
<ttl unit=_"minutes"_>10</ttl>  
</expiry>  
  
<resources>  
<heap unit=_"entries"_>1000</heap>  
</resources>  
</cache>  
  
<cache alias=_"org.hibernate.cache.internal.StandardQueryCache"_>  
<key-type>java.lang.String</key-type>  
<value-type>java.lang.Object</value-type>  
<resources>  
<heap unit=_"entries"_>200</heap>  
</resources>  
</cache>  
  
<cache alias=_"org.hibernate.cache.spi.UpdateTimestampsCache"_>  
<key-type>java.lang.String</key-type>  
<value-type>java.lang.Long</value-type>  
<resources>  
<heap unit=_"entries"_>200</heap>  
</resources>  
</cache>  
  
</config>
```
___
![[Day-09__9-12-2025-L1 and L2 caching in hibernate-images.png]]
___
### **My Practice :** 
1. 