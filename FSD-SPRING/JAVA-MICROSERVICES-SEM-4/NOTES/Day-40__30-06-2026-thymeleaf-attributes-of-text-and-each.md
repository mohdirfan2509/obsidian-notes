# Day-40 — 30-06-2026 — Thymeleaf Attributes of Text and Each

---

## 🧩 What is Thymeleaf?

Thymeleaf is a **server-side template engine** capable of generating HTML pages dynamically.

```text
HTML PAGE ==> Static[Template] + dynamic features
			     		|
				Thymeleaf Engine[TemplateResolver + Context(data)]
						 [location and specify template]
```

---

## 🧩 Core Attributes Today

| Attribute | Purpose |
|---|---|
| `th:text="${}"` | Read data and print it onto the element |
| `th:each="variable:${iterator}"` | Iterate Array, String, List — one element at a time |

---

## 🧩 Example 1 — Standalone Java + ClassLoaderTemplateResolver

```java
package in.pw.ioi;

import java.nio.file.Files;
import java.nio.file.Path;

import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;
import org.thymeleaf.templateresolver.ClassLoaderTemplateResolver;

import in.pw.ioi.bean.Address;
import in.pw.ioi.bean.Employee;

public class TestApp {

	public static void main(String[] args) throws Throwable {

		ClassLoaderTemplateResolver templateResolver = new ClassLoaderTemplateResolver();
		templateResolver.setSuffix(".html");
		templateResolver.setPrefix("/templates/");
		templateResolver.setCharacterEncoding("UTF-8");
		templateResolver.setTemplateMode("HTML");
		
		TemplateEngine engine = new TemplateEngine();
		engine.setTemplateResolver(templateResolver);
		
		Context context = new Context();
		
		Address address = new Address("Bandra","Maharashtra","IND");
		
		Employee employee = new Employee(10, "sachin",address);
		
		context.setVariable("employee", employee);
		
		//start the engine
		String html = engine.process("employees", context);
		//System.out.println(html);
		
		
		//nio -> Asynchronous code
		Files.writeString(Path.of("output.html"), html);
		
		
	}

}
```

Key setup points:

1. `ClassLoaderTemplateResolver` — prefix `/templates/`, suffix `.html`, mode `HTML`, UTF-8
2. `TemplateEngine` uses that resolver
3. `Context` holds model variables (`employee`)
4. `engine.process("employees", context)` renders template name `employees`
5. Write result with NIO `Files.writeString`

---

## 🧩 Example 2 — HTML Template with `th:each` + `th:text`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Employees Data</title>
</head>
<body>
	<table border='1' cellpadding='10'>
		<caption>Employee Details</caption>
		<thead>
			<tr>
				<th>EID</th>
				<th>ENAME</th>
				<th>CITY</th>
				<th>STATE</th>
				<th>COUNTRY</th>
			</tr>
		</thead>
		<tbody>
			<tr style='text-align:center;' th:each="employee:${employees}">
				<td th:text="${employee.eid}">EID</td>
				<td th:text="${employee.ename}">ENAME</td>
				<td th:text="${employee.address.city}">CITY</td>
				<td th:text="${employee.address.state}">CITY</td>
				<td th:text="${employee.address.country}">CITY</td>
			</tr>
		</tbody>
	</table>
</body>
</html>
```

Nested property navigation: `${employee.address.city}` / `state` / `country`.

Prototype cell text (`EID`, `ENAME`, `CITY`, …) remains visible when the file is opened statically in a browser.

---

## 🤖 AI Points

1. **Production consideration:** Always set `characterEncoding` (UTF-8) and `templateMode` on the resolver so international content and HTML parsing stay consistent.
2. **Industry practice:** Keep prototype text inside tags (`th:text` body) so designers can open HTML without a running server.
3. **Common mistake:** Calling `engine.process("employees", ...)` while the file is named differently or not under the configured prefix — template name must match resolver rules.
4. **Interview insight:** Thymeleaf needs both a **TemplateResolver** (where/how to find templates) and a **Context** (data) before `TemplateEngine` can render.
5. **Modern Spring Boot connection:** Boot auto-configures Thymeleaf; you rarely wire `ClassLoaderTemplateResolver` manually — but the same `th:text` / `th:each` attributes apply.

---

## 💻 My Codes


  
## 🖼️ Image
