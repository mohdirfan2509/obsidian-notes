# Day-06 — 28-04-2026 — Working with GenericServlet

---

## 🧩 Servlet Recap

A Servlet is a program which runs in a **server environment** to generate a dynamic response.

```text
Webapplication = static resources like HTML, CSS, images, ...
                 dynamic resources :: .java [ Servlet ]
                                         |
                                       J2EE
                                         |
                                   Server[Tomcat] : JVM
```

---

## 🏗️ Design a Servlet

- Start from `Servlet(I)` (the Servlet interface).

### Deployment styles

- Hard Deployment
- Cold Deployment
- Smooth Deployment [IDE]

---

## 📁 Tomcat Deployment Layout

```text
tomcat
  |-> webapps
        |-> FirstServletApp [ContextRoot]
                |-> WEB-INF [ deployment descriptor]
                        |-> web.xml [ legacy approach]
                        |-> classes
                              |-> FirstServlet.class [Annotations would be available]

                |-> FirstServlet.java [Servlet : servlet-api.jar : tomcat]
                        |
                       /test
```

### Runtime steps

1. Deploy the application in the server.
2. Start the server — e.g. `tomcat\bin\tomcat9.exe` (double click).
3. Send the request:

```text
request[input] : http://ipaddressofserver:portnoofserver/ContextRoot/urlPattern
```

---

## 🚀 loadOnStartup Behaviour

**Note:** Upon sending the request, if we want the servlet to load, instantiate and initialize then **don't** use `loadOnStartup`.

If we want the life cycle actions of a servlet to happen upon **starting the server**, then use `loadOnStartup` with a value as `0` or any **positive** number.

### Case 1 — Lower `loadOnStartup` value = more priority

```text
FirstServlet   :: loadOnStartup = 2
SecondServlet  :: loadOnStartup = 3
```

### Case 2 — Same value — order up to the container

```text
FirstServlet   :: loadOnStartup = 2
SecondServlet  :: loadOnStartup = 2
```

### Case 3 — Default is negative — load only on request

```text
FirstServlet   :: loadOnStartup = -1
SecondServlet  :: loadOnStartup = -100
```

Default value of `loadOnStartup` is **negative**, due to which loading will happen only upon request made.

---

## 🔁 Why GenericServlet?

**Note:** If we create a Servlet using `Servlet(I)` we need to give body for **5 methods**, so the code would be lengthy and complex.

**Solution:** `GenericServlet`

```text
Servlet(I)
 |
GenericServlet(AC)
        public void init(ServletConfig config) throws SE
        public void init() throws SE
        public abstract void service(ServletRequest, ServletResponse) throws SE, IOE
```

`GenericServlet` is an **abstract class (AC)** that implements most of `Servlet` and leaves `service(...)` abstract for the developer.

---

## 🤖 AI Points

1. **Production consideration:** Use `loadOnStartup` deliberately for connection warm-up or cache priming; negative/default keeps cold start fast for rarely used endpoints.
2. **Industry practice:** Deploy under `webapps/<ContextRoot>/WEB-INF/classes` with annotation-driven mapping; keep `web.xml` only for legacy or advanced descriptors.
3. **Common mistake:** Assuming equal `loadOnStartup` values guarantee a fixed order—the container may choose arbitrarily.
4. **Interview insight:** `GenericServlet` applies the Adapter idea: stub optional methods, force override of `service(ServletRequest, ServletResponse)`.
5. **Real-world connection:** IDE “smooth deploy” still expands to the same Tomcat layout; understanding `WEB-INF` prevents ClassNotFound and mapping 404s in production.

---

## 💻 My Codes


  
## 🖼️ No Image

