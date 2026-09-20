# Day-17 — 19-05-2026 — Include Forward using Request and Context Object Diff bw Redirect and Forward

---

## 🧩 Design Guidance

```text
Servlet
=======
    Servlet
        entire logic of an application , I write in SingleServlet
        Don't write in SingleServlet.
```

Split responsibilities across servlets (e.g. validate vs home vs error).

```text
ServletA ---> to take request
                validate inputs
                        ---- success :: redirect to home page
                        ---- failure :: redirect to error page
```

---

## 🔁 Request Dispatching — forward

```text
eg#1.                                  ContextDispatching
browser ====> Servlet(req,resp) --RequestDispatching-[forward]-----> Servlet(req,resp)
                           |                                                   |
                        output(p1)                                          output(p2)
                                                                               |
   p2    <---------------------------------------------------------------------+
```

```text
browser ====> Servlet(req,resp) ---  ContextDispatching ------> JSP(dynamic)
browser ====> Servlet(req,resp) ---- RequestDispatching ----> HTML
```

---

## 🖨️ PrintStream vs PrintWriter

```text
PrintStream
   System.out.println(); // Not a buffered based output
                                u write ---> show it to screen [no flush()]

PrintWriter
    |-> out.println(); // It is a buffered based output
                        u write -----> keep in buffer -- flush() -> finally write to UI
```

---

## 📬 ServletRequest.getRequestDispatcher

```java
ServletRequest(I)
     public RequestDispatcher getRequestDispatcher(String path);
                                                           |-> relative
                                                           |-> absolute
```

### Case1

In request object, we can keep the data and we can forward to next resource.  
Next resource holds the **same** request and response object.

### Case2

In case of forward request, upon finishing the execution of resource, thread comes back to first resource and executes the remaining statement.  
If the resource uses `PrintWriter` object, then that response **won't be added** to the UI (for forward semantics as taught).

### Case3

While executing the remaining lines of code, if exception occurs the response sent to browser won't have any impact.

### Case4

Before forwarding if we `flush()` the first resource response, then we can't use **Request Dispatching** mechanism; it would lead to `IllegalStateException`.

### Case5

While forwarding the request to the next resource it adds few extra attributes for its internal usage:

```text
javax.servlet.forward.request_uri----> /FirstServletApp/home
javax.servlet.forward.context_path----> /FirstServletApp
javax.servlet.forward.servlet_path----> /home
javax.servlet.forward.mapping----> org.apache.catalina.core.
                                        ApplicationMapping$MappingImpl@5efaab37
```

---

## 📎 Working with include(request, response)

```text
ServletContext(I)
        public RequestDispatcher getRequestDispatcher(String path);
                                                              |-> absolute
```

### Example — include approach

```text
browser ====> Servlet(req,resp) --RequestDispatching-[include]-----> Servlet(req,resp)
                           |                                                   |
   p1+p2 <------------ output(p1) -------------------------------------- output(p2)
```

```java
ServletContext context = getServletContext();
RequestDispatcher rd = context.getRequestDispatcher("/user");
rd.include(request, response);
```

**Output:** Servlet-1 + Servlet-2

---

## 🌍 Foreign / Cross Context

**Note:** Using `ServletContext` object we can perform **Foreign Context**:

```java
public ServletContext getContext(String uripath);
```

```text
APP-1
  |-> App1servlet : /home
                ServletContext context = getServletContext();
                ServletContext fc = context.getContext("/App2");
                RequestDispatcher rd = fc.getRequestDispatcher("/user");
                rd.include(request, response);


APP-2
  |-> App2servlet : /user
```

Inform the container for cross-context communication:

```xml
<Context crossContext="true">

</Context>
```

---

## ⚖️ difference: `response.sendRedirect()` vs `rd.forward(req, response)`

| Aspect | `response.sendRedirect()` | `rd.forward(req, resp)` |
|--------|---------------------------|-------------------------|
| URL rewriting / browser URL | URL Rewriting will happen on the URL | No URL Rewriting |
| Data sharing | Data cannot be shared (same request attributes) | Data would be shared |
| Direction | server to client | server – server |
| Request/response objects | **new** request and response object upon redirection | **same** request and response object upon forwarding |
| Typical use | resource migration / external navigation | communication between resources of same or different project [app] |

---

## 🤖 AI Points

1. **Production consideration:** Never flush/commit the response before `forward`/`include` if you still need to dispatch—`IllegalStateException` awaits.
2. **Industry practice:** Use **forward** for MVC “controller → view”; use **include** for composing headers/footers/shared fragments into one response.
3. **Common mistake:** Expecting `sendRedirect` to preserve request attributes—use forward/session/query params instead.
4. **Interview insight:** Forward keeps same req/resp and URL bar; Redirect is a new client round-trip with visible URL change.
5. **Modern Spring Boot connection:** `forward:` vs `redirect:` prefixes in Spring MVC views map directly onto these Servlet dispatching vs redirect semantics; cross-context is rare in Boot monoliths but still appears in multi-WAR Tomcat hosts.

---

## 💻 My Codes


  
## 🖼️ Image

