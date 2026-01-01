
# Stored Procedure
---
## What is a Stored Procedure?

- In programming, when a **set of statements** needs to be written **multiple times**, we group those statements and give a name to the block.
- This block is called a **function**.
- Instead of rewriting the statements, we **call the function** whenever required.
---

## Stored Procedure in Database
- On the database side, when the **same query** needs to be executed **multiple times with different inputs**,  
    instead of writing the query repeatedly, it is written **once inside a procedure**.
---
# Why Stored Procedures are Needed (Database Side)

1. **Query should not be tampered**
2. **Query can run with multiple inputs**, promoting **modularity**
3. **Stored procedures are stored in the database**
---
# Syntax of Writing a Stored Procedure

```sql
DELIMITER $$

CREATE
    PROCEDURE `ioi_24b2_batch`.`GET_PRODUCT_DETAILS_BY_ID`
    (
        IN productId INT,
        OUT productName VARCHAR(20),
        OUT productCost FLOAT,
        OUT productType VARCHAR(20)
    )
BEGIN
    SELECT
        PNAME, PCOST, PTYPE
    INTO
        productName, productCost, productType
    FROM
        product
    WHERE pid = productId;
END$$

DELIMITER ;
```
---
# IN and OUT Parameters
## Syntax

```text
IN  variableName datatype
OUT variableName datatype
```
---
## Calling Stored Procedure

```sql
SET @productName = '';
SET @productCost = 0.0;
SET @productType = '';

CALL GET_PRODUCT_DETAILS_BY_ID(1, @productName, @productCost, @productType);

SELECT @productName, @productCost, @productType;
```
---
## Output

```text
@productName   @productCost   @productType
fossil         1000           quartz
```
---
# PRODUCT Table

```text
PID   PNAME    PCOST   QTY   PTYPE
1     fossil   1000    1     quartz
2     tissot   2000    2     automatic
3     armani   3000    3     manual
```
---
# Question
## How would you execute a stored procedure using JDBC?
---
![[Day-07__18-11-2025-storedprocedure-notes-images.png]]
___
### **My practice :**
1. 