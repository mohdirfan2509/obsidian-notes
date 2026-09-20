# Day-55 — 11-08-2026 — CRUD Operation using Springrest

---

## 🧩 EmployeeRestController — Full CRUD

```java
package in.ioi.pw.rest;

import java.util.ArrayList;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import in.ioi.pw.model.Employee;

@RestController
@RequestMapping("/employee")
public class EmployeeRestController {
	List<Employee> employees = new ArrayList<>(
			List.of(new Employee(10, "sachin", "MI", 45678.90), new Employee(18, "kohli", "RCB", 45545.05)));

	@GetMapping("/get")
	public ResponseEntity<?> findAllEmployees() {
		return new ResponseEntity<>(employees, HttpStatus.OK);
	}

	@PostMapping("/save")
	public ResponseEntity<?> saveEmployee(@RequestBody Employee employee) {
		employees.add(employee);
		System.out.println(employee);
		return new ResponseEntity<>("EMPLOYEE SAVED", HttpStatus.CREATED);
	}

	@GetMapping("/find/{id}")
	public ResponseEntity<?> getMethodName(@PathVariable Integer id) {

		for (Employee employee : employees) {
			if (employee.getEid().equals(id)) {
				return new ResponseEntity<>(employee, HttpStatus.OK);
			}
		}

		return new ResponseEntity<>("EMPLOYEE NOT FOUND", HttpStatus.NOT_FOUND);
	}

	@PutMapping("/update/{id}")
	public ResponseEntity<?> findEmployeeById(@PathVariable Integer id, @RequestBody Employee employee) {

		for (Employee emp : employees) {
			if(emp.getEid().equals(id)) {
				emp.setEaddress(employee.getEaddress());
				emp.setEname(employee.getEname());
				emp.setEsalary(employee.getEsalary());
				System.out.println(emp);
				return new ResponseEntity<>(emp,HttpStatus.OK);
			}
			
		}
		
		return new ResponseEntity<>("EMPLOYEE NOT FOUND", HttpStatus.NOT_FOUND);
	}
	
	@DeleteMapping("/delete/{id}")
	public ResponseEntity<?> deleteEmployeeById(@PathVariable Integer id) {

		for (Employee emp : employees) {
			if(emp.getEid().equals(id)) {
				employees.remove(emp);
				return new ResponseEntity<>("EMPLOYEE DELETED SUCCEFULLY",HttpStatus.OK);
			}
			
		}
		
		return new ResponseEntity<>("EMPLOYEE NOT FOUND", HttpStatus.NOT_FOUND);
	}
	

}
```

### Endpoint map

| HTTP | Path | Status on success | Purpose |
| --- | --- | --- | --- |
| GET | `/employee/get` | 200 OK | List all employees |
| POST | `/employee/save` | 201 CREATED | Save employee (`@RequestBody`) |
| GET | `/employee/find/{id}` | 200 OK / 404 | Find by id |
| PUT | `/employee/update/{id}` | 200 OK / 404 | Update fields |
| DELETE | `/employee/delete/{id}` | 200 OK / 404 | Delete by id |

In-memory store is an `ArrayList` seeded with two `Employee` objects (sachin / kohli).

---

## 🤖 AI Points

1. **Production consideration:** In-memory `List` CRUD is for learning only—replace with a transactional repository before multi-instance or restart-safe deployments.
2. **Industry practice:** Return proper HTTP statuses (`201` create, `404` missing, `200` update/delete) via `ResponseEntity` so clients can branch without parsing message strings.
3. **Common mistake:** Removing from a list while iterating with enhanced-for can throw `ConcurrentModificationException`—prefer iterator/`removeIf` in real code.
4. **Interview insight:** `@RestController` + `@GetMapping`/`@PostMapping`/`@PutMapping`/`@DeleteMapping` maps CRUD verbs to resource URLs with `@PathVariable` and `@RequestBody`.
5. **Modern Spring Boot connection:** Same controller shape later moves to Spring Data JPA repositories or Spring Data REST while keeping the REST verb contract.

---

## 💻 My Codes


  
## 🖼️ Image
