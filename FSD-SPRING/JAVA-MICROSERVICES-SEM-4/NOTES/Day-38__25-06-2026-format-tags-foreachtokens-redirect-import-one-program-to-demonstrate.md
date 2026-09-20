# Day-38 — 25-06-2026 — Format Tags Foreachtokens Redirect Import One Program to Demonstrate

---

## 🧩 JSP → EL + JSTL Recap

### EL syntax

```text
${variable}
${obj.property}
${obj['property']}, ${obj["property"]}
```

### Core tags covered so far

| Tag | Purpose |
|---|---|
| `<c:set value="" var="" scope=""/>` | Set attribute |
| `<c:out value="${var}"/>` | Output |
| `<c:remove var=""/>` | Remove |
| `<c:if test=""/>` | Conditional |
| `<c:choose>` / `<c:when>` / `<c:otherwise>` | if-else / switch |
| `<c:forEach begin="" end="" step="" var="">` | Numeric loop |
| `<c:forEach items="" var="">` | Collection loop |
| `<c:url var="" value="">` + `<c:param>` | Build URL with query params |

### New core tags today

#### `c:forTokens` — split and iterate

```jsp
<c:forTokens items="" delims="" var="">
</c:forTokens>
```

```jsp
<c:forTokens items="Learning-JSTL-is-very-Easy" delims="-" var="data">
		<span style='color:red;'>${data }</span><br/>
</c:forTokens>
```

#### `c:redirect` — equivalent to `response.sendRedirect(...)`

```jsp
<%--response.sendRedirect(url?name=""&age="") --%>
<c:redirect url="">
	<c:param name="" value=""/>
	<c:param name="" value=""/>
</c:redirect>
```

#### `c:import` — equivalent to `rd.include("url")`

```jsp
<%-- rd.include("url") --%>
<c:import url=""/>
```

---

## 🧩 Formatting Tags (`fmt`)

Formatting covers:

- **Date**
- **Salary / Double** (as per locale)

Taglib:

```jsp
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
```

### Currency by locale

```jsp
<fmt:setLocale value="en_IN"/>
<fmt:formatNumber value="850003.23" var="salary" type="currency"/>
```

### Date formatting

```jsp
<fmt:setLocale value="en_US"/>
<%
	Date d = new Date();
	pageContext.setAttribute("date",d);
%>
<fmt:formatDate value="${date }" var="joiningDate" pattern="MM-dd-yyyy hh:mm:ss a"/>
```

---

## 🧩 Demo Sketch — Employee with Bonus + Formatted Salary

Mentor sketch for one program demonstrating format + choose + set/remove:

**Employee fields:** `eid`, `ename`, `salary`, `joiningDate`

`pageContext` holds company / bonus rules: if `salary < 75000`, `total = salary + bonus`.

```jsp
<c:set var="bonus" value="${bonus}"/>

<c:choose>
	<c:when test="${emp.salary lt 75000}">
		<c:set var="total" value="${bonus+salary}"/>
	</c:when>
	<c:otherwise>
		<c:set var="" value="${}"/>
	</c:otherwise>
</c:choose>
<fmt:formatNumber>
	
</fmt:formatNumber>

<c:remove var="total"/>
```

> **Correction:** Raw notes used incomplete attributes (`val=` / empty `var`). Intended pattern is `<c:set var="total" value="${bonus + emp.salary}"/>` (and a clear otherwise branch for salary without bonus).

### Assignment direction from lecture

- Format **salary** and **joiningDate** for **5 employee objects**
- Show total employees: `<%= emp.size()%>` (or prefer EL/`fn:length` in cleaner JSP)

---

## 🤖 AI Points

1. **Production consideration:** Always pair `fmt:formatNumber` / `fmt:formatDate` with an explicit `fmt:setLocale` so currency and date formats match the user’s region.
2. **Industry practice:** Prefer `c:redirect` with nested `c:param` over hand-built query strings when leaving a JSP after a POST-like action.
3. **Common mistake:** Confusing `c:import` (include content into the current response) with `c:redirect` (HTTP redirect to another URL).
4. **Interview insight:** `c:forTokens` is the JSTL equivalent of `String.split` + loop — useful for delimited CSV-style display without Java.
5. **Real-world connection:** Locale-aware salary/date formatting in JSTL maps to Spring’s `MessageSource` / Thymeleaf `#numbers` / `#temporals` utilities in Boot apps.

---

## 💻 My Codes


  
## 🖼️ Image
