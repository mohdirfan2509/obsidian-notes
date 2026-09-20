# Day-20 — 25-05-2026 — DispatcherType with Examples and Introduction to FilterChain

---

## 🧩 How a Request Can Reach a Servlet (and Which Filter DispatcherType Applies)

### a. Direct browser request — `DispatcherType.REQUEST` (default)

```text
browser ---------Filter-------------------> servlet
			 ^
	   dispatcherTypes = DispatcherType.REQUEST [Default type]
```

### b. Forward — `DispatcherType.FORWARD`

```text
servlet ----forward(request,response)------> servlet
			Filter
			  ^
	    dispatcherTypes = DispatcherType.FORWARD
```

### c. Include — `DispatcherType.INCLUDE`

```text
servlet ----include(request,response)------> servlet
			Filter
			  ^
	    dispatcherTypes = DispatcherType.INCLUDE
```

---

## ⚠️ Configuring Error Pages in Servlet — `DispatcherType.ERROR`

### d. Error dispatch

```text
browser ---------------------servlet
					a. SC_INTERNAL_SERVER_ERROR
					b. Exception occurred

				   container 
				    a. web.xml [500, ArithmeticException]
						 | forward("/error")
						 |
					/error -----Filter-----> ErrorServlet
					              ^
						dispatcherTypes = DispatcherType.ERROR
```

---

## 📄 `web.xml` Error-Page Shape

Path: `src/main/webapp/WEB-INF/web.xml`

```xml
<web-app
    xmlns="http://xmlns.jcp.org/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="
        http://xmlns.jcp.org/xml/ns/javaee
        http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
    version="4.0">

	<error-page>
		<error-code>404|500|404</error-code>
		<exception-type>FullyQualifiedExceptionClassName</exception-type>
		<location>/urlPattern | /pathofjspfilewithextension</location>
	</error-page>

</web-app>
```

> Mentor sketch shows the *shape* of tags; in a real file you typically use separate `<error-page>` blocks (one for `<error-code>`, one for `<exception-type>`), as in the concrete example below.

---

## 💻 ServletA Triggering an Error

```java
package in.pw.ioi.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns =  "/s1")
public class ServletA extends HttpServlet {
	private static final long serialVersionUID = 1L;

	@Override
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws 			ServletException, IOException {
		System.out.println("Requesting coming from browser to /s1");
		
		//response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
		System.out.println(10/0);
	}
}
```

---

## 📄 Concrete `web.xml` Error Mappings

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app
    xmlns="http://xmlns.jcp.org/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="
        http://xmlns.jcp.org/xml/ns/javaee
        http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
    version="4.0">
    
    <error-page>
    	<error-code>500</error-code>
    	<location>/error</location>
    </error-page>
    
    <error-page>
    	<exception-type>java.lang.ArithmeticException</exception-type>
		<location>/error</location>
    </error-page>

</web-app>
```

---

## 🧩 ErrorServlet Reading Error Attributes

```java
package in.pw.ioi.error;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/error")
public class ErrorServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	@Override
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws 
			ServletException, IOException {
		Throwable th = (Throwable)request.getAttribute(RequestDispatcher.ERROR_EXCEPTION);
		String servletName= (String)request.getAttribute(RequestDispatcher.ERROR_SERVLET_NAME);
		Integer statusCode = (Integer)request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);
		System.out.println("Status code is : "+statusCode);
		System.out.println("Cause of Error by Servlet called : "+servletName);
		
		PrintWriter out = response.getWriter();
		if (th != null) {
			out.println(th.getClass().getName());
			out.println(th.getMessage());
		    out.println("Hey, provide valid inputs to perform operation....");
		}else {
			out.println("Currently out of service, wait for while we would resume back...");	
		}
		out.close();	
	}

}
```

Attributes used:

- `RequestDispatcher.ERROR_EXCEPTION`
- `RequestDispatcher.ERROR_SERVLET_NAME`
- `RequestDispatcher.ERROR_STATUS_CODE`

---

## 🔗 Filter Declaring Multiple DispatcherTypes

```java
package in.pw.ioi.filter;

import java.io.IOException;

import javax.servlet.DispatcherType;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;

@WebFilter(urlPatterns = { "/*"},dispatcherTypes = {
					DispatcherType.REQUEST,
					DispatcherType.FORWARD,
					DispatcherType.INCLUDE,
					DispatcherType.ERROR})
public class MyFilter implements Filter {

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		System.out.println("filter is executing on " + request.getDispatcherType());

		// pass the request along the filter chain
		chain.doFilter(request, response);
	}
}
```

By default, filters only see `REQUEST`. Explicitly listing `FORWARD`, `INCLUDE`, and `ERROR` makes the filter run on those dispatches too. Logging `request.getDispatcherType()` shows which path triggered it.

---

## 🔐 Realtime Usage: Error Handling with Spring Security

```text
AuthenticationFilter --AuthenticationException---> maps to /error
AuthorizationFilter  --AuthorizationException ---> maps to /login
```

---

## 🤖 AI Points

1. **Production consideration:** Map both HTTP status codes and exception types in `web.xml` (or Spring Boot error pages) so arithmetic bugs and deliberate `sendError(500)` both reach a safe error view.
2. **Industry practice:** Default filter dispatcher is `REQUEST` only—enable `FORWARD`/`ERROR` only when you truly need filters on internal dispatches (logging, security).
3. **Common mistake:** Writing an error page Filter with only default dispatcher types—ERROR dispatches skip it, so auth/logging never runs on `/error`.
4. **Interview insight:** `RequestDispatcher.ERROR_*` attributes are how the container passes exception, servlet name, and status to the error resource.
5. **Modern Spring Boot connection:** Spring Security maps auth failures similarly—AuthenticationException → error/login flows mirror the ERROR dispatcher pattern.

---

## 💻 My Codes


  
## 🖼️ Image
