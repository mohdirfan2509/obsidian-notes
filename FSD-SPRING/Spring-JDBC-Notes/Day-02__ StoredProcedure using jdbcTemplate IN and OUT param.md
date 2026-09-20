# 🌱 **Spring JDBC: JdbcTemplate & NamedParameterJdbcTemplate**
---
## 🧩 **JdbcTemplate**
- Uses **PreparedStatement**
- Works with **positional parameters**
- Used for executing **queries**
### ⚙️ **API**

```java
new JdbcTemplate(DataSource)
```
---
## 🧷 **NamedParameterJdbcTemplate**
- Uses **PreparedStatement**
- Works with **named parameters**
- Makes queries more readable
### ⚙️ **API**

```java
new NamedParameterJdbcTemplate(DataSource)
```
---
## 🗄️ **Working with Stored Procedures & Batch Files**
### 🧠 **Spring JDBC Approach*
1. `SimpleJdbcCall(JdbcTemplate jdbcTemplate)`
2. `new JdbcTemplate(DataSource)`
3. `SimpleJdbcCall.withProcedureName(String procedureName)`
4. `SimpleJdbcCall.declareParameters(SqlParameter... sqlParameters)`
5. `SqlParameter(String name, int sqlType)`
6. `SqlOutParameter(String name, int sqlType)`
7. `Map<String, Object> execute(SqlParameterSource parameterSource)`
8. `MapSqlParameterSource.addValue(String paramName, Object value)`
---
## 📦 **Project Structure**
1. **Product**
    - `pid`
    - `pname`
    - `price`
    - `qty`
    - `ptype`
2. **Configuration**
3. **DAO Class**
4. **Runner Class (Main Code)**
---
## 🗃️ **Stored Procedure (Database Side)**

```sql
DELIMITER $$

USE `ioi_24b1_batch`$$

DROP PROCEDURE IF EXISTS `GET_PRODUCT_DETAIlS_BY_ID`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_PRODUCT_DETAIlS_BY_ID`(
    IN productId INT,
    OUT productName VARCHAR(20),
    OUT productPrice INT,
    OUT productType VARCHAR(20)
)
BEGIN
    SELECT 
        pname, price, ptype
    INTO
        productName, productPrice, productType
    FROM
        Products
    WHERE pid = productId;
END$$

DELIMITER ;
```
---
## ▶️ **Runner Class (Main Program)**

```java
package in.pw.ioi;

import java.util.Scanner;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import in.pw.ioi.config.AppConfig;
import in.pw.ioi.model.Product;
import in.pw.ioi.service.ProductService;

public class TestApp {

	public static void main(String[] args) throws Exception {

		AnnotationConfigApplicationContext cfg =
				new AnnotationConfigApplicationContext(AppConfig.class);

		ProductService service = cfg.getBean("service", ProductService.class);
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter the id of the product to be searched : ");
		int productId = scanner.nextInt();

		Product result = service.getProductFromDaoUsingId(productId);
		if (result != null) {
			System.out.println(result);
		} else {
			System.out.println("Record not available for the given id : " + productId);
		}

		scanner.close();
		cfg.close();
	}
}
```
---
## 🗂️ **DAO Class**

```java
package in.pw.ioi.dao;

import java.sql.Types;
import java.util.Map;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.SqlOutParameter;
import org.springframework.jdbc.core.SqlParameter;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.simple.SimpleJdbcCall;
import org.springframework.stereotype.Repository;
import in.pw.ioi.model.Product;

@Repository("dao")
public class ProductDao {

	private SimpleJdbcCall simpleJdbcCall;

	@Autowired
	public ProductDao(JdbcTemplate jdbcTemplate) {
		this.simpleJdbcCall = new SimpleJdbcCall(jdbcTemplate)
			.withProcedureName("GET_PRODUCT_DETAILS_BY_ID")
			.declareParameters(
				new SqlParameter("productId", Types.INTEGER),
				new SqlOutParameter("productName", Types.VARCHAR),
				new SqlOutParameter("productCost", Types.DOUBLE),
				new SqlOutParameter("productType", Types.VARCHAR)
			);
	}

	public Product getProductByid(Integer productId) {

		MapSqlParameterSource params =
			new MapSqlParameterSource().addValue("productId", productId);

		Map<String, Object> out = simpleJdbcCall.execute(params);

		if (out.get("productName") == null) {
			return null;
		} else {
			Product product = new Product();
			product.setPid(productId);
			product.setPname((String) out.get("productName"));
			product.setPrice((Double) out.get("productCost"));
			product.setPtype((String) out.get("productType"));
			return product;
		}
	}
}
```
---
## 🧠 **Service Class**

```java
package in.pw.ioi.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import in.pw.ioi.dao.ProductDao;
import in.pw.ioi.model.Product;

@Service("service")
public class ProductService {

	@Autowired
	private ProductDao productDao;

	@Transactional
	public Product getProductFromDaoUsingId(Integer productId) {
		return productDao.getProductByid(productId);
	}
}
```
---
## 📤 **Output**

```
Enter the id of the product to be searched : 100
Record not available for the given id : 100
```

```
Enter the id of the product to be searched : 2
Product [pid=2, pname=tissot, price=20000.0, ptype=automatic]
```
---
![Stored Procedure Using jdbc Template](Day-02__img.png)
___
### **My Practice :**
1. 