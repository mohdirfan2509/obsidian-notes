# Day-24 — 02-06-2026 — Session Cookie and Its Limitation

---

## 🧩 Why Session Management?

In order to process a later request, we need previous request input, but **HTTP is stateless**, so it will not remember the previous request and every request is treated as a new request.

**Solution:** Session management at the server side.

### Getting a session

- `request.getSession()` → Session
- `request.getSession(false)` → Session | `null`

### `HttpSession` methods

- `isNew()`
- `getId()`
- `setMaxInactiveInterval(int seconds)`
- `getMaxInactiveInterval()` — returns seconds available
- `invalidate()` — logout mechanism
- `getLastAccessedTime()` → `Long`
- `getCreationTime()` → `Long`
- `setAttribute(k, v)` → `void`
- `getAttribute(K)` → `Object`

> **Note:** Mentor notes listed `getMaxInactiveInterval(int seconds)`; the API getter takes **no** argument and returns `int`. Setter is `setMaxInactiveInterval(int seconds)`.

### Default timeout

- Default time available for a session object is **30 minutes** (1800 seconds).
- Control availability with `setMaxInactiveInterval(120)` (example: 120 seconds).

---

## 🍪 How Data Is Exchanged for a Session Object

```text
 => client sent the request
		a. server checks is it sending firstTime or not
		b. if Yes
			Create a session : SessionID is managed by tomcat
		c. **send the response to client
				response header : K -> V
						Set-cookie -> SessionId

 =>client again send the request
	     a. browser in request header will attach the session information
		through a key called 'cookie'
				request header : K -> V
						cookie -> JESSIONID=SessionId

				request.getHeaderNames(); :: Enumeration<String>
				request.getHeader(name)   :: String
```

> **Correction:** Standard cookie name is typically `JSESSIONID` (mentor text shows `JESSIONID`).

---

## 💻 DisplayServlet — Inspect Headers and Session Metadata

```java
package in.pw.ioi.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/session/display")
public class DisplayServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html");
		HttpSession session = request.getSession(false);
		PrintWriter out = response.getWriter();
		if (session == null) {
			out.print("<h2>Session object not available for request type</h2>");
		} else {
			out.println("<table border='1'>");
			out.println("<caption>Session Object Info</caption>");
			out.println("<thead><tr><th>NAME</th><th>VALUE</th></tr></thead>");
			out.println("<tbody>");	
			Enumeration<String> attributeNames = request.getHeaderNames();
			while (attributeNames.hasMoreElements()) {
				String name = (String) attributeNames.nextElement();
				out.println("<tr>");
				out.println("<td>"+name+"</td>");
				out.println("<td>"+request.getHeader(name)+"</td>");
				out.println("</tr>");
			}
			out.println("<tbody>");
			out.println("</table>");
			
			System.out.println("Session created at : "+new Date(session.getCreationTime()));
			System.out.println("Session Last accessed at : "+new Date(session.getLastAccessedTime()));
			System.out.println("Session available for : "+session.getMaxInactiveInterval() + " seconds");
			Enumeration<String> names = session.getAttributeNames();
			while (names.hasMoreElements()) {
				String key = (String) names.nextElement();
				System.out.println(key + "===>"+session.getAttribute(key));
			}
		}
	
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
```

This demo prints **request headers** (including the cookie carrying the session id) and logs creation time, last accessed time, max inactive interval, and session attributes.

---

## 📉 Limitation of Server-Side Sessions

For each client the server should create and maintain a separate session object. If clients increase, the number of session objects at the server side increases, which uses more memory on the server.

**Solution idea:** use Cookies (every information is kept at the client side, not at the server side).

```text
Cookie ---> client side [ browser]
			    |
			end user [ nontech | tech person]
				  (no prob)   (open browser and handles something)


client send the request ------> cookie
				   K -> V
				  role -> user

  browser<--cookie---- send it is as response
	   role - user
	   role - ADMIN
		
  broser -----------cookie----------------> server
		[role - admin]			|-> privileges will assigned as ADMIN
```

### Recommended hybrid approach

Use a Session object only, and inside the cookie keep the **sessionId**; keep the actual data in the Session object:

```java
HttpSession session = request.getSession();
session.setAttribute("ROLE", role);
session.setAttribute("ADMIN", admin);
// response carries Set-Cookie = JSESSIONID; ...
```

---

## 🍪 Creating and Reading Cookies

**How to create a cookie?**

```java
Cookie c = new Cookie(String Key, String value);
```

**How to add a cookie to the response object?**

```java
response.addCookie(c);
```

**How to read cookies from the request object?**

```java
Cookie[] cookies = request.getCookies();
```

---

## 🤖 AI Points

1. **Production consideration:** Storing roles only in client cookies is forgeable—prefer server session (or signed JWT) for authorization data.
2. **Industry practice:** Default 30-minute idle timeout; tune `setMaxInactiveInterval` per app (banking shorter, forums longer).
3. **Common mistake:** Putting sensitive privileges in a plain cookie the user can edit in DevTools.
4. **Interview insight:** Session tracking cookie (`JSESSIONID`) is how a stateful server maps a browser back to an `HttpSession` on a stateless protocol.
5. **Real-world connection:** Scaling sticky sessions / Redis session stores exists because per-node in-memory sessions do not share across a cluster.

---

## 💻 My Codes


  
## 🖼️ Image
