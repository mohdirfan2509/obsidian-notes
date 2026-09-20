# Day-35 — 22-06-2026 — EL Implicit Objects and Introduction to JSTL with Operators

---

## 🧩 JSP Recap (Legacy Tags)

UI technology built on top of Servlet.

### Tags (used in legacy projects)

- Scriptlet: `<% statement; %>`
- Expression: `<%= expr %>`
- Declarative: `<%! statement; %>`

### Directives — translation-time instructions to the engine for generated servlet code

- **page** — inform about the API used: `<%@ page attributeName="attributeValue" %>`
- **taglib** — import 3rd-party library (JSTL; Spring MVC form library): `<%@ taglib prefix="" uri=""%>`
- **include** — static inclusion (copy/paste into source): `<%@ include file=""%>`

### Implicit objects

- `request`, `response`, `session`, `out`, `config`, `application`, `exception`, `page`
- `pageContext` (`getXxx()` methods)

---

## 🔤 EL Syntax Recap

```text
 Syntax: ${variable}
	    |
	 pageContext.findAttribute(variable) :: pageScope,sessionScope,requestScope,applicationScope

 Syntax: ${obj.propertyName}
	    |
	   Map<String,String> :: getPropertyName() : String

 Syntax: ${obj['index']} | ${obj["index"]}
	     |
	   Map<String,String> :: getPropertyName() : String
```

---

## 🔑 EL Implicit Objects

### a. Scope maps

`pageScope`, `sessionScope`, `requestScope`, `applicationScope`

### b. `param` / `paramValues`

- `param` :: `request.getParameter(Key)` → `String` | null  
  - Map: `put(K,V)`, `get(k)`
- `paramValues` :: `request.getParameterValues()` → `String[]` | null  
  - Map: `Map<String, String[]>`

### c. `header` / `headerValues`

- `header` :: `request.getHeader(Key)` → `String` | null → `Map<String,String>`
- `headerValues` :: `request.getHeaders()` → `Enumeration<String>` | null → `Map<String,String[]>`

### d. `cookie`

```text
 cookie ==> request.getCookies() :: Cookie[]
  |
 Map<String,Cookie>

KEY    VALUE
=============
 K1    Cookie object :: [name,value,maxAge,domain,...]
 K2    Cookie object
```

Cookie API surface: `getName()`, `getValue()`, `getMaxAge()`, `getDomain()`, ...

#### eg#1

```jsp
<h1>
		Header data is : ${header.cookie }<br/>
		Cookie data is : ${cookie.JSESSIONID.name } and ${cookie.JSESSIONID.value } <br/>
		Max Age of cookie is : ${cookie.JSESSIONID.maxAge }<br/>
		Domain name is : ${cookie.iphone.domain }<br/>
		Comment name is : ${cookie.iphone.comment }<br/>
</h1>
```

### 5. `initParam`

```text
initParam
	|
      context.getInitParameter("KEY") : String | null
```

Access: `initParam.keyName` | `initParam['keyName']` | `initParam["KEYNAME"]`

#### eg#1 — `web.xml` context-param + JSP

```xml
<web-app>
	
	<context-param>
		<param-name>company</param-name>
		<param-value>IOI</param-value>
	</context-param>
	
	<context-param>
		<param-name>location</param-name>
		<param-value>Bengaluru</param-value>
	</context-param>
	
	
</web-app>
```

```jsp
     <%
		ServletContext ctx = getServletContext();
		ctx.setAttribute("company", "IOI");
		ctx.setAttribute("location", "Bengaluru");
	%>
	<h1>
		Context Object data : ${initParam['company'] }<br /> Context Object
		data : ${initParam.company }<br /> Context Object data :
		${initParam["location"] }<br />
	</h1>
	<hr />
	<h1>
		AplicationData is : ${applicationScope.company }<br /> AplicationData
		is : ${applicationScope.location }<br />

	</h1>
```

**Output:**

```text
Context Object data : IOI
Context Object data : IOI
Context Object data : Bengaluru

AplicationData is : IOI
AplicationData is : Bengaluru
```

> Note: `initParam` reads **context-param** init parameters; `applicationScope` reads attributes set on `ServletContext`. Mentor demo sets both to the same values.

### 6. Dynamic features without Java in the page

```text
6. JSP[ no java code still features should be dynamic] 
    | :: 9 implicit objects
    |
   EL[${} :: internally everything will happen]
   pageContext


Servlet :: upon request
		  | -> TYPE : GET
				:: doGet()
	          |-> Session
				:: id, isNew(),....
```

#### eg#1 — `pageContext` via EL

```jsp
Request type is :<span>${pageContext.request.method }</span><br/>
Session data is : <span>${pageContext.session.id }</span>
```

EL avoided Java code for reading method and session id.

---

## 📚 Why JSTL? (Collections / Conditionals / Formatting)

Example domain need:

```text
Collection : List<Employee> :: id,name[Syed,Haider,Ali,khan],joiningDate[Date: dd-MM-yyyy HH:mm:ss a],
					salary[Double:i18N ]
		 |
		 EL
		a. List : Employee objects — need operators / tags
		b. if 
			a. iterate the object [cursor]
			b. call getter methods on the object and present it 
		c. else
			a. No records are available
```

### JSP Standard Tag Library (JSTL) capabilities

- a. iteration  
- b. conditional check  
- c. I18N and Locale  
- d. Formatting (e.g. FirstName: UPPERCASE with Bold)

### JSTL tag libraries

- a. core library  
- b. formatting library  
- c. function library  

---

## ➕ EL Operator `+` (Introduced)

```text
EL operator
==========
 a. + 
	Rule 
		a. null will be treated as zero
		b. empty string is treated as zero and for other inputs it would use
				Integer.parseInt("input") : Number
		c. + operator is meant only for addition, so we say + operator is not overloaded.
```

> **Correction:** Mentor wrote `Integer.parseInput`; standard API is `Integer.parseInt`.

---

## 🤖 AI Points

1. **Production consideration:** Prefer `HttpOnly` session cookies; exposing `${cookie.JSESSIONID.value}` in HTML is for learning only—never echo session ids into pages in production.
2. **Industry practice:** Use `initParam` for deploy-time context params; use `applicationScope` for runtime shared attributes—know which you configured.
3. **Common mistake:** Treating EL `+` like Java string concatenation—it is numeric addition only (not overloaded).
4. **Interview insight:** Eleven EL implicit objects include scope maps, param(s), header(s), cookie, initParam, and pageContext.
5. **Real-world connection:** JSTL core/fmt/functions fill the gap EL cannot (iteration, `if`, i18n)—same problem Spring’s Thymeleaf `th:each` / `th:if` solve in modern stacks.

---

## 💻 My Codes


  
## 🖼️ Image
