# Day-47 — 09-07-2026 — Maven Life Cycle Methods

---

## 🧩 What is Maven?

Maven is a **build automation** and **dependency management** tool.

### Without Maven

```text
.java ---> compile---> .class ---> .jar ----> run a jar
.java ---> compile---> .class ----> .war ---> deploy war into container [ tomcat]
                           WEB-INF
			     |-> lib
				  |-> .jar
```

These actions are called, in Maven terminology, a **Life Cycle**.

---

## 🧩 Maven Life Cycles (`pom.xml`)

Model:

```text
phase ----> plugin  ---> goal
```

### A. Default life cycle (developers)

| Phase | Plugin / goal idea | Output |
|---|---|---|
| `validate` | validate project | — |
| `compile` | `maven-compiler-plugin` → `compile` (`javac`) | `target/classes/*.class` |
| `test` | `maven-surefire-plugin` | run unit tests |
| `package` | `maven-war-plugin` / `maven-jar-plugin` | `target/*.jar` or `*.war` |
| `install` | `maven-install-plugin` | install to local repo |
| `deploy` | `maven-deploy-plugin` | deploy to remote repo |

To run a Java `main` through Maven:

```text
plugins : mojo plugin -> exec:java
```

**Note — EmployeeCrudApp example:**

```text
EmployeeCrudApp
	|-> target		
		|-> EmployeeCrudApp-Version3.0.war -----> tomcat
    |-> pom.xml
	a. servlet api <scope>compile|runtime|test|provided</scope>
	b. jsp
	c. thymeleaf
	d. mysql
	e. hibernate
```

### Dependency scopes

| Scope | Meaning |
|---|---|
| `compile` (default) | Available at compile **and** runtime |
| `runtime` | Available only at runtime |
| `test` | Only while running tests |
| `provided` | Needed at compile time; supplied by container at runtime |

### B. Clean life cycle

`clean` — deletes the previous build (`target`).

### C. Site life cycle

`site` — documentation; generates HTML under:

```text
target
  |-> site
	|-> index.html [ summary of our project ]
```

---

## 🧩 Creating a JAR and Reusing It in Another Project

### Producer: `CalculatorApp`

```java
package in.ioi.pw.CalculatorApp;
public class CalculatorService {
	public static int add(int a, int b) {
		return a + b;
	}
}
```

```bash
mvn install
```

Creates a JAR in `target` **and** copies it to the **local repository**.

### Consumer: `OrderCartService`

`pom.xml`:

```xml
<dependencies>
		<dependency>
			<groupId>in.ioi.pw</groupId>
			<artifactId>CalculatorApp</artifactId>
			<version>1.0</version>
		</dependency>

	</dependencies>
	<build>
		<plugins>

			<plugin>
				<groupId>org.codehaus.mojo</groupId>
				<artifactId>exec-maven-plugin</artifactId>
				<version>3.5.0</version>

				<configuration>
					<mainClass>in.ioi.pw.TestApp</mainClass>
				</configuration>
			</plugin>
		</plugins>
	</build>

</project>
```

`TestApp`:

```java
package in.ioi.pw;

import in.ioi.pw.CalculatorApp.CalculatorService;

public class TestApp {

	public static void main(String[] args) {

		int output = CalculatorService.add(10, 20);
		System.out.println(output);
	}

}
```

```bash
mvn compile
mvn exec:java
```

```text
Output
  30
```

---

## 🤖 AI Points

1. **Production consideration:** Use `provided` for servlet APIs so the WAR does not ship a second copy of classes already in Tomcat.
2. **Industry practice:** `mvn install` a shared utility module into the local repo, then depend on it by `groupId`/`artifactId`/`version` from other services.
3. **Common mistake:** Running `package` without `install` when another local project needs the artifact — the consumer cannot resolve it from the local repository yet.
4. **Interview insight:** Maven phases bind plugins/goals; you usually invoke a phase (`compile`, `package`) and Maven runs all preceding phases automatically.
5. **Modern Spring Boot connection:** Spring Boot still sits on the same Maven default lifecycle; `spring-boot:run` / `repackage` are extra plugin goals on top of `package`.

---

## 💻 My Codes


  
## 🖼️ Image
