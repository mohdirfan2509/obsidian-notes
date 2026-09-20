# Day-33 — 18-06-2026 — EL Syntax EL Implicit Objects Param Paramvalues Header Headervalues

---

## 🧩 JSP Recap

UI technology built on top of Servlet.

### Tags

- Scriptlet: `<% statement; %>`
- Expression: `<%= expr %>`
- Declarative: `<%! statement; %>`

### Directives

- page: `<%@ page attributeName="attributeValue" %>`
- taglib: `<%@ taglib prefix="" uri=""%>`
- include: `<%@ include file=""%>`

### Implicit objects

- `request`, `response`, `session`, `out`, `config`, `application`, `exception`, `page`
- `pageContext`

### EL / JSTL overview

**EL**

- a. EL operators
- b. EL Implicit objects (11)

**JSTL**

- a. core libraries
- b. function libraries
- c. formatting libraries

EL: remove Java code from JSP.

---

## 🔤 EL Syntax for Reading Data

### Read from scoped object / properties

```text
Syntax: ${variable} :: Handles null with blank
		   |
		 pageContext.findAttribute(variable) ::  null

Syntax: ${obj.propertyName}
		   |
		  pageContext.findAttribute(variable) :: Object
		  					   |-> getPropertyName()

Syntax: ${param,paramValues,header,headerValues,cookie,initParam,
		  pageScope,requestScope,sessionScope,applicationScope,pagecontext}

		${param.key} or ${param['key']} or ${param["key"]}
			|
		    Map<K,V> -------> put(key)
				      get(key)
```

---

## 🫘 Working with Bean Properties via EL

```jsp
<%@page import="org.apache.catalina.valves.StuckThreadDetectionValve"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<%!public class Student {
		private Integer sid;
		private String sname;
		private Integer sage;
		private String saddress;

		public Student(Integer sid, String sname, Integer sage, String saddress) {
			this.sid = sid;
			this.sname = sname;
			this.sage = sage;
			this.saddress = saddress;
		}

		public String getSname() {
			return sname;
		}

		public String getSaddress() {
			return saddress;
		}

		public Integer getSage() {
			return sage;
		}

		public Integer getSid() {
			return sid;
		}

	}%>

	<%
	Student student = new Student(10,"sachin",55,"IND");
	request.setAttribute("student", student);
	%>
	
	Expression Language : ${student }
	<table border='1'>
		<tr>
			<th>ID</th>
			<th>NAME</th>
			<th>AGE</th>
			<th>ADDRESS</th>
		</tr>
		<tbody>
			<tr>
				<td>${student.sid }</td>
				<td>${student.sname }</td>
				<td>${student.sage }</td>
				<td>${student.saddress }</td>
			</tr>
		</tbody>
	</table>

</body>
</html>
```

### MVC reminder

```text
MVC 
  request ----> controller ---------> service --------------> DAO
		   |request.setAttribute("KEY",data)
		   |modelAttribute.setAttribute("KEY",data)
		  view
		    a. read the data from request object
			   a. using EL with JSTL i can validate the data and present

 ->if the object is not present then we get null and EL will suppress null with blank
 ->During the execution if exception occurs and if it is not handled 
   EL will not do any job.
```

---

## 🧪 Working with `${variable}`

### eg#1 — Local/instance field not in scope

```jsp
	<%!
		int a =10;
		
	%>

	<h1> The value of a is ${a}</h1>
```

**Response:** `The value of a is ` (blank — `a` not found via `findAttribute`)

### eg#2 — Put value into page scope

```jsp
	<%!
		int a =10;
		pageContext.setAttribute("data",a,1)
	%>

	<h1> The value of a is ${data}</h1>
```

**Response:** `The value of a is 10`

---

## 🔑 EL Implicit Objects — `param` and `paramValues`

| EL object | Underlying API | EL usage |
|-----------|----------------|----------|
| `param` | `request.getParameter('KEY')` → `String` \| null | `${param.KEY}` |
| `paramValues` | `request.getParameterValues('KEY')` → `String[]` \| null | `${paramValues.KEY[index]}`, `['index']`, `["index"]` |

If array index exceeds length, EL **suppresses** `ArrayIndexOutOfBoundsException` and prints nothing on UI.

### eg#1 — Single parameter

```text
KEY         VALUE
--------------------
 userName    sachin

code :: ${param.userName}
```

### eg#2 — Duplicate key with `param` (first value)

```text
  KEY         VALUE
 --------------------------
 userName      sachin
 course		java
 course		springboot
 course		microservices

code :: ${param.course}
```

### eg#3 — `paramValues` map entry

```text
 KEY         VALUE
 --------------------------
 userName      sachin
 course		java
 course		springboot
 course		microservices

code :: ${paramValues.course}
```

### eg#4 — Indexed access

```jsp
	UserName is : ${param.userName }<br/>
	CourseSelected is : ${paramValues.course[0] }<br>
	CourseSelected is : ${paramValues.course['1'] }<br>
	CourseSelected is : ${paramValues.course["2"] }<br>
	CourseSelected is : ${paramValues.course[3] } <%-- AIOBE :suppress --%>
```

**Output:**

```text
UserName is : sachin
CourseSelected is : java
CourseSelected is : springboot
CourseSelected is : microservices
CourseSelected is :
```

---

## 🧾 `header` and `headerValues`

```text
header ===> request.getHeader()  :: String | null
  |
  |EL uses 
  |
Map<K,V>
```

**Assume:**

```text
 cookie = JESSIONID=FADASG1f8fh
 ACCEPT-LANGUAGE = [en_uS,fr,GR]
  host  = localhost:9999
```

**MAP for `header`:**

| KEY | VALUE |
|-----|-------|
| cookie | JESSIONID=FADASG1f8fh |
| ACCEPT-LANGUAGE | [en_uS,fr,GR] |
| host | localhost:9999 |

```text
headerValues===> request.getHeaders() :: Enumeration<String> | null
  |
  |EL uses
  |
 Map<K,Values[]>
```

**MAP for `headerValues` (example):**

| KEY | VALUE |
|-----|-------|
| ACCEPT-LANGUAGE | [en_uS,fr,GR] |

### eg#1 — Header EL demo

```jsp
<%@page import="org.apache.catalina.valves.StuckThreadDetectionValve"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<h1>
		HEADER DATA: ${header}<br/>
		HEADER DATA : ${header.cookie }<br/>
		HEADER DATA : ${header['accept-language'] }<br/> 
		
		HEADERS DATA : ${headerValues.cookie[300]}
	</h1>
</body>
</html>
```

---

## 🤖 AI Points

1. **Production consideration:** EL null-to-blank is convenient for UI but can hide missing model attributes—validate required data in the controller.
2. **Industry practice:** Prefer `${paramValues.course[i]}` for multi-select form fields; `${param.course}` only returns the first value.
3. **Common mistake:** Expecting `${a}` to see a declarative `int a`—EL only sees scoped attributes, not class fields.
4. **Interview insight:** `${student.sname}` resolves via `getSname()` JavaBeans naming, not public fields.
5. **Real-world connection:** Out-of-range `${paramValues.course[3]}` printing blank (no AIOBE) is intentional EL leniency for views.

---

## 💻 My Codes


  
## 🖼️ Image
