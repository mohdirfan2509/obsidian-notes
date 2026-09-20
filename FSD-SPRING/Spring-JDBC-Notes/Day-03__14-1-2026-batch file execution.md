# 🌱 **Spring JDBC – Batch Processing**
---
## ⚙️ **Batch Update Method (JdbcTemplate)**

```java
<T> int[][] batchUpdate(
    String sql,
    Collection<T> batchArgs,
    int batchSize,
    ParameterizedPreparedStatementSetter<T> pss
) throws DataAccessException
```
---
## 🧩 **Use Case**
- Insert **multiple records** into the database efficiently
- Reduces repeated database calls
- Uses **PreparedStatement** internally
---
## 🏗️ **Project Flow**
1. **TestApp** – Runner class
2. **Service Layer** – Transaction handling
3. **DAO Layer** – Batch insert logic
4. **Database** – Stores product records
---
## ▶️ **a. TestApp (Runner Class)**

```java
package in.pw.ioi;

import java.util.ArrayList;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import in.pw.ioi.config.AppConfig;
import in.pw.ioi.model.Product;
import in.pw.ioi.service.ProductService;

public class TestApp {

	public static void main(String[] args) throws Exception {

		AnnotationConfigApplicationContext cfg =
				new AnnotationConfigApplicationContext(AppConfig.class);

		ProductService service = cfg.getBean("service", ProductService.class);

		ArrayList<Product> products = new ArrayList<>();
		products.add(new Product(10, "fossil", 35000.0, "chronography"));
		products.add(new Product(11, "tissot", 25000.0, "automatic"));
		products.add(new Product(12, "seiko", 32000.0, "chronography"));
		products.add(new Product(13, "guess", 31000.0, "analog"));
		products.add(new Product(14, "armani", 30000.0, "digital"));

		service.saveAllProducts(products);
		System.out.println("Products saved to database....");

		cfg.close();
	}
}
```
---
## 🗂️ **b. DAO Implementation (Batch Logic)**

```java
package in.pw.ioi.dao;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import in.pw.ioi.model.Product;

@Repository("dao")
public class ProductDaoImpl implements IProductDao {

	@Autowired
	private JdbcTemplate jdbcTemplate;

	@Override
	public void saveListOfProducts(List<Product> products) {

		jdbcTemplate.batchUpdate(
			"insert into product(`pid`,`pname`,`price`,`ptype`) values (?,?,?,?)",
			products,
			100,
			(ps, product) -> {
				ps.setInt(1, product.getPid());
				ps.setString(2, product.getPname());
				ps.setDouble(3, product.getPrice());
				ps.setString(4, product.getPtype());
			}
		);
	}
}
```

---
## 🧠 **c. Service Layer**

```java
package in.pw.ioi.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import in.pw.ioi.dao.IProductDao;
import in.pw.ioi.model.Product;

@Service("service")
public class ProductService {

	@Autowired
	private IProductDao productDao;

	@Transactional
	public void saveAllProducts(List<Product> products) {
		productDao.saveListOfProducts(products);
	}
}
```
---
## 📄 **d. DAO Interface**

```java
package in.pw.ioi.dao;

import java.util.List;
import in.pw.ioi.model.Product;

public interface IProductDao {
	void saveListOfProducts(List<Product> products);
}
```
---
## 📤 **Output**

```
Products saved to database....
```
---
## 🔑 **Key Points to Remember**
- `batchUpdate()` is used for **bulk insert operations**
- Uses **PreparedStatement** internally
- Batch size controls how many records are processed at once
- Service layer manages **transactions**
- DAO layer handles **database logic**
---
![Batch File Execution](Day-03__img.png)
___
### **My Practice :**
1. 