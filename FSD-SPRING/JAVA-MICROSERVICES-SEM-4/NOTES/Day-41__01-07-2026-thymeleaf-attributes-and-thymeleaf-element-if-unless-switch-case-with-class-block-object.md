# Day-41 — 01-07-2026 — Thymeleaf Attributes and Thymeleaf Element If Unless Switch Case with Class Block Object

---

## 🧩 Attributes Recap

```text
a. th:text="${}"
b. th:each="ref: ${iterator}"
```

### Domain model used

```text
Employee
  |-> id,name,age,Address
		    |-> city,state,country
```

### Context keys

```text
new Employee() ; --> employee
List.of(e1,e2) ; --> employees
```

---

## 🧩 Expression Symbols

| Symbol | Name |
|---|---|
| `${}` | Value expression |
| `th:object="${}"` + `*{}` | Selection expression |

**Syntax:** `th:object="${keyName}"` and `*{propertyName}`

---

## 🧩 Thymeleaf Element — `<th:block>`

`<th:block>...</th:block>` is processed by the Thymeleaf engine but **is not part of the final HTML page** (wrapper disappears after processing).

### Case 1 — Selection on row + nested property paths

```html
<tr style='text-align:center;' th:object="${employee}">
	<td th:text="*{eid}">EID</td> <!-- employee.getEid() -->
	<td th:text="*{ename}">ENAME</td>

	<td th:text="*{address.city}">CITY</td>
	<td th:text="*{address.state}">CITY</td>
	<td th:text="*{address.country}">CITY</td>
</tr>
```

### Case 2 — Nested `th:object` on `td` (extra wrappers)

```html
<tr style='text-align:center;' th:object="${employee}">
		<td th:text="*{eid}">EID</td> <!-- employee.getEid() -->
		<td th:text="*{ename}">ENAME</td>
				
		<td th:object="*{address}">
			<span th:text="*{city}"></span>
		</td>
		<td th:object="*{address}">
			<span th:text="*{state}"></span>
		</td>
		<td th:object="*{address}">
			<span th:text="*{country}"></span>
		</td>				
</tr>
```

### Case 3 — Preferred: `<th:block th:object="*{address}">` for multiple cells

```html
<tr style='text-align:center;' th:object="${employee}">
		<td th:text="*{eid}">EID</td> <!-- employee.getEid() -->
		<td th:text="*{ename}">ENAME</td>
				
		<!-- THYMELEAF element : <th:block></th:block> -->		
		<th:block th:object="*{address}">
			<td th:text="*{city}"></td>
			<td th:text="*{state}"></td>
			<td th:text="*{country}"></td>
		</th:block>
								
</tr>
```

---

## 🧩 Working with Multiple Objects

| Attribute | Role |
|---|---|
| `th:if="${true}"` | Show when condition true |
| `th:unless="${!true}"` | Show when condition false |
| `th:class="${expression}"` | Expression returns a CSS class name string |
| `th:each="ref,stat:${keyName}"` | Iteration + status variable |

### Status object (`stat`) fields

| Field | Meaning |
|---|---|
| `count` | `i + 1` |
| `index` | `i` |
| `even` | even row |
| `odd` | odd row |
| `first` | boolean |
| `last` | boolean |

### Full table demo — Bootstrap striping, role via if/unless

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Employees Data</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class='container'>
		<h3 class='m-3'>Employee Details</h3>
	<table  class='table table-striped m-3 border border-3'>
		<thead>
			<tr>
				<th>SNO</th>
				<th>EID</th>
				<th>ENAME</th>
				<th>CITY</th>
				<th>STATE</th>
				<th>COUNTRY</th>
				<th>ROLE</th>
			</tr>
		</thead>
		<tbody>
			<tr style='text-align:center;'  th:each="emp,stat :${employees}" th:object="${emp}" th:class="${stat.even} ? 'table-primary' : 'table-danger'">
				
				<td th:text="${stat.count}"></td>
				<td th:text="*{eid}">EID</td> <!-- employee.getEid() -->
				<td th:text="*{ename}">ENAME</td>
				
				
				<th:block th:object="*{address}">
					<td th:text="*{city}"></td>
					<td th:text="*{state}"></td>
					<td th:text="*{country}"></td>
				</th:block>
				
				<td th:if="${stat.last}">
					<span>🧑‍💼MANAGER</span>
				</td>
				
				<td th:unless="${stat.last}">
					<span>👩‍💻 DEVELOPER</span>
				</td>	
			</tr>
		</tbody>
	</table>
</body>
</html>
```

---

## 🧩 Switch / Case

```text
a. th:switch = "${} or *{}"
   th:case="data"   [condition evaluates to true]
   th:case="*"      [default]
```

Also used: `th:with="bonus = ${emp.salary gt 80000.0 ? 10000 : 0.0}"` for local variables in the row.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Employees Data</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class='container'>
		<h3 class='m-3'>Employee Details</h3>
	<table  class='table table-striped m-3 border border-3'>
		<thead>
			<tr>
				<th>SNO</th>
				<th>EID</th>
				<th>ENAME</th>
				<th>CITY</th>
				<th>STATE</th>
				<th>COUNTRY</th>
				<th>ROLE</th>
				<th>Department</th>
				<th>Salary</th>
				<th>Bonus</th>
			</tr>
		</thead>
		<tbody>
			<tr style='text-align:center;'  
				th:each="emp,stat :${employees}" 
				th:object="${emp}" 
				th:class="${stat.even} ? 'table-primary' : 'table-danger'"
				th:with="bonus = ${emp.salary gt 80000.0 ? 10000 : 0.0}"
				>
				
				<td th:text="${stat.count}"></td>
				<td th:text="*{eid}">EID</td> <!-- employee.getEid() -->
				<td th:text="*{ename}">ENAME</td>
				
				
				<th:block th:object="*{address}">
					<td th:text="*{city}"></td>
					<td th:text="*{state}"></td>
					<td th:text="*{country}"></td>
				</th:block>
				
				<td th:if="${stat.last}">
					<span>🧑‍💼MANAGER</span>
				</td>
				
				<td th:unless="${stat.last}">
					<span>👩‍💻 DEVELOPER</span>
				</td>
				
				<td th:switch="*{department}">
					<span th:case="'IT'">
						💻Software Developer
					</span>
					<span th:case="'HR'">
						🚺 Human Resource
					</span>
					<span th:case="'Sales'">
						💹 Sales Manager
					</span>
					<span th:case="'Finance'">
						💰💲Finance Department
					</span>
					<span th:case="*">
						Works for Other Department
					</span>
				</td>
				
				<td th:text="*{salary}  + ${bonus}">
				
				</td>
				<td th:text="${bonus}">
				
				</td>
			</tr>
		</tbody>
	</table>
</body>
</html>
```

Department cases: `'IT'`, `'HR'`, `'Sales'`, `'Finance'`, default `*`.

---

## 🤖 AI Points

1. **Production consideration:** Use `<th:block>` when you need a Thymeleaf scope (`th:object` / `th:each`) without injecting an extra real DOM node into table layouts.
2. **Industry practice:** Drive zebra striping with `th:class` + `stat.even` / `stat.odd` instead of hard-coding CSS classes per row.
3. **Common mistake:** Putting nested `<td th:object="*{address}">` wrappers around spans — breaks table structure; prefer `th:block` spanning multiple `td`s.
4. **Interview insight:** `th:switch` / `th:case="*"` is the Thymeleaf equivalent of JSTL’s multi-`c:when` + `c:otherwise`.
5. **Modern Spring Boot connection:** Combining `th:each`, `th:object`, `th:with`, and Bootstrap classes is the typical pattern for admin CRUD tables in Boot + Thymeleaf apps.

---

## 💻 My Codes


  
## 🖼️ Image
