# Day-07 — 29-04-2026 — Working with GenericServlet and HttpServlet

---

## 🧩 Servlet Interface Methods

```text
Servlet(I)
   | :: 5 abstract methods
                3 abstract methods : Life cycle methods
                                        init(SC)
                                        service(SR, SResp)  :: Request Processing
                                        destroy()
                2 inline methods   : getServletConfig(), getServletInfo()
 Developer
```

> **Correction:** The interface has **5** methods total: three lifecycle (`init`, `service`, `destroy`) and two non-lifecycle (`getServletConfig`, `getServletInfo`). Mentor note text said “3 inline methods” for the last two—there are two such methods.

---

## 🎭 Adapter Design Pattern — GenericServlet

```text
Servlet(I)
     |
GenericServlet(AC)
     init(SC){}
     init()
     destroy(){}
     abstract service(SR, SResp)

    |
 FirstServlet(/test)
    |
   public void service(SR, SResp){
        // Request processing logic
   }
```

### Deploy and invoke

1. Deploy the application
2. Start the server
3. Send the request:

```text
http://localhost:9999/FirstServletApp/test
```

---

## 🔄 Flow of GenericServlet

```text
 a. Loading the Servlet
 b. Instantiation  :: Zero param | default Constructor
                        Class.forName("fullyqualifiedname").newInstance()
 c. Initialization :: init(ServletConfig config){
                                this.config = config;
                                init();
                         }
                     init(){
                        // programmer written logic for the servlet
                     }
 d. Request Processing ::
        public void service(ServletRequest request, ServletResponse response){

        }
 e. Undeploying the application
        public void destroy(){
                // programmer written logic for the servlet
        }
```

---

## 🏗️ How is a Servlet Object Created?

How to create an Object in Java?

Using the `new` keyword we can create an object only if the name of the class is known from the beginning.

```text
       request         Object
        /test ------> pw.ioi.controller.FirstServlet
                        Class.forName("fullyqualifiedname").newInstance()
        /user ------> UserServlet
        /cart ------> CartServlet
```

The container resolves URL pattern → FQCN → reflective instantiation.

---

## ⚠️ Overriding init — Three Cases

### Case 1 — Override `init(ServletConfig)`

If we override `init(SC)` in our Servlet class:

- `init(SC)`: Initialization logic (your override)
- `init()`: **not called**
- `getServletConfig()`: **null** (because config was never stored by GenericServlet’s `init(SC)`)

```java
@Override
public void init(ServletConfig config) {
	System.out.println("Initialization logic");
}
```

### Case 2 — Override no-arg `init()`

If we override `init()` in our Servlet class:

- `init(SC)`: gets called (GenericServlet stores config, then calls `init()`)
- `init()`: programmer logic
- `getServletConfig()`: returns config data

```java
@Override
public void init() {
	// programmer written logic for the servlet
}
```

### Case 3 — Override neither

If we don't override any `init` in our Servlet class:

- `init(SC)`: logic of GenericServlet
- `init()`: dummy implementation
- `getServletConfig()`: return config data

---

## 🚫 Limitations of GenericServlet

HTTP protocol — Big 7 Methods:

- a. GET
- b. POST
- …

Also other protocols exist (SMTP, FTP, …).

**Solution:** use **Template Design Pattern** associated Servlet — `HttpServlet`.

---

## 📋 HttpServlet (Abstract Class) — Template Design Pattern

```text
HttpServlet[AC]
   |-> init(SC)
       init()
       public void service(ServletRequest, ServletResponse) throws SE, IOE {
                // convert ServletRequest : HttpServletRequest
                // convert ServletResponse: HttpServletResponse

                service(HttpServletRequest, HttpServletResponse);
       }
      protected void service(HttpServletRequest request, HttpServletResponse) {
                if (request.METHOD("GET")) {
                        doGet(request, response);
                }
                if (request.METHOD("POST")) {
                        doPost(request, response);
                }

      }
      public void doGet(...) {
                return "405|400 supported service is not available"
      }
      public void doPost(...) {
                return "405|400 support service is not available"
      }

}
```

> **Correction:** Default `doGet`/`doPost` in `HttpServlet` typically respond with **HTTP 405 Method Not Allowed** when not overridden (mentor note also mentioned 400).

### Developer Servlet

```java
public class FirstServlet extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response) {
		System.out.println("***POST Request*****");
	}

	public void doGet(HttpServletRequest request, HttpServletResponse response) {
		System.out.println("***GET Request*****");
	}
}
```

```text
request: Type : POST : doPost(request, response)
request: Type : GET  : doGet(request, response)
```

---

## 🧬 Lifecycle of HttpServlet

```text
  a. Loading        : Our Servlet class loading based on URL pattern
  b. Instantiation  : Zero param constructor
  c. Initialization : init(SC)
                      init()
  d. RequestProcessing: service(SR, SResp)
                        service(HSR, HSResp)
                        doXXXX(HSR, HSResp)
  e. Undeployment :
                        destroy()
```

---

## 🤖 AI Points

1. **Production consideration:** Always override no-arg `init()` (or call `super.init(config)` if you override `init(ServletConfig)`) so `getServletConfig()` remains usable.
2. **Industry practice:** Prefer `HttpServlet` + `doGet`/`doPost` over raw `GenericServlet.service` for HTTP apps—protocol dispatch is built in.
3. **Common mistake:** Overriding `init(ServletConfig)` without `super.init(config)` breaks config/init-param access.
4. **Interview insight:** GenericServlet = Adapter; HttpServlet = Template Method (`service` → `doXXX`).
5. **Modern Spring Boot connection:** DispatcherServlet is an `HttpServlet`; your `@GetMapping`/`@PostMapping` methods are the modern analogue of `doGet`/`doPost`.

---

## 💻 My Codes


  
## 🖼️ Image

