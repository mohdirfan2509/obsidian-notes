   Add.java                   Add.class
+-------------+           +--------------+
| Source File | --compile→| Byte Code    |
+-------------+           +--------------+
                               |
                               v
                           +--------+
                           |   JVM  |
                           +--------+
                               |
                               v
                            +------+
                            | O/P  |
                            +------+
### **Compile Phase / Compilation Time**

- Compile-Time Mistake / Compile-Time Error  
   → Faulty coding by programmer

### **Execution Phase / Execution Time / Run-Time**

- Execution-Time Mistake / Exception  
    → Faulty input by user
---
### **1. What is an exception?**

Exceptions refer to such mistakes that occur during the execution of a program.

---
### **2. What causes a program to generate an exception?**

Faulty input provided by the user to the program.

---

### **3. When does an exception occur?**

During the execution of the program.

---

### **4. What happens if an exception occurs?**

It disturbs the normal flow of the program resulting in abrupt termination.  
Hence, valuable resources may be lost.

---

### **5. What is meant by exception handling?**

Exception handling refers to the process of handling the exception object in such a manner that it prevents abrupt termination.  
The main objective of exception handling is **graceful termination of the program**.

---

### **6. List the keywords related to exception handling.**

```java
try 
catch 
finally
throw 
throws
```

---
Page **1**

**Types of Architectures**

## **1) 1-Tier Architecture / Stand-alone Architecture**

There was no need for exception handling.  
Hence **C language doesn’t support exception handling** (no chance of exception handling).

**Years:** 1940s, 1950s, 1960s, 1970s

**Process:**

- App development
- App compilation
- App execution
---
## **2) 2-Tier Architecture / Client-Server Architecture**

**C++ (1960s)**

**Server side:**

- App development
- App compilation
- App execution
    

**Client side (multiple clients):**

- App execution
    
- App execution
    
- App execution
    

**Note:**  
Here, it was possible for exceptions to occur, but however it could be rectified.  
Hence exception handling is **not given much importance in C++**.

---
## **3) N-Tier Architecture / Internet Architecture**

**Java (1990s)**

Multiple machines connected through the Internet performing:

- Upload
- Download
- App execution
This architecture supports full exception handling because faults can occur at any level due to distributed execution.
---
Page **2**

- In this architecture, exception handling becomes extremely important, as the users of the application are spread across different part of the world. Hence, any faulty input by any user can not be corrected immediately by the developer. Therefore, exception handling becomes extremely important.

![[image1.excalidraw]]

---
Page 3

![[internet.excalidraw.md]]

---
Page 4

![[internet2.excalidraw.md]]

---
Page **5**

![[exceptionHandlingFlowChart.excalidraw]]

---
## Disadvantage of Single Try with Single Catch Hierarchy :

- The advantage of default exception handler is that it provides suitable message regarding the exception that is generated.
- However, the disadvantage of default exception handler is that abrupt termination of the program occurred.
- The advantage of user-defined exception handler is abrupt termination of the program would never occur.
- However, the disadvantage of user-defined exception handler is that a suitable message about the exception cannot be provided (using a single catch block).
- The above disadvantages can be overcome by using **single try with multiple catch** hierarchy.

---
Page **6**

Example :

```java
import java.util.Scanner;
class Demo
{
    public static void main(String[] args)
    {
        System.out.println("connection is established");
        Scanner scan = new Scanner(System.in);
        
        //---Risky Code----
        try
        {
            System.out.println("Enter the numerator:");
            int a = scan.nextInt();

            System.out.println("Enter the denominator:");
            int b = scan.nextInt();

            int c = a / b;
            System.out.println(c);

            System.out.println("Enter the size of the array:");
            int size = scan.nextInt();
            int[] arr = new int[size];

            System.out.println("Enter the element to be stored:");
            int elem = scan.nextInt();

            System.out.println("Enter the position at which the element has to be stored:");
            int pos = scan.nextInt();

            arr[pos] = elem;
            System.out.println(arr[pos]);
        }
        
        //---Alternate Code---
        catch (Exception e)
        {
            System.out.println("Some problem occurred");
        }

        System.out.println("connection is Terminated");
    }
}

```

output 1:

```java
Connection is established
Enter the numerator:
100
Enter the denominator:
2
50
Enter the size of array:
5
Enter the element to be stored:
25
Enter the position at which the element has to be stored:
1
Connection is Terminated

```

output 2:

```java
Connection is established
Enter the numerator:
100
Enter the denominator:
0
Some problem occurred 
Connection is Terminated

```

output 3:

```java
Connection is established
Enter the numerator:
100
Enter the denominator:
-5
Some problem occurred 
Connection is Terminated
```

output 4:

```java
Connection is established
Enter the numerator:
100
Enter the denominator:
2
Enter the size of array:
50
Enter the position at which the elemen has to be stored:
5
Some problem occurred 
Connection is Terminated
```

---
Page **7** 

## Single `try` with multiple `catch` :
```java
import java.util.Scanner;
class Demo
{
    public static void main(String[] args)
    {
        System.out.println("connection is established");
        Scanner scan = new Scanner(System.in);
        
        //--- Risky code ---
        try
        {
            System.out.println("Enter the numerator:");
            int a = scan.nextInt();

            System.out.println("Enter the denominator:");
            int b = scan.nextInt();

            int c = a / b;
            System.out.println(c);

            System.out.println("Enter the size of the array:");
            int size = scan.nextInt();
            int[] arr = new int[size];

            System.out.println("Enter the element to be stored:");
            int elem = scan.nextInt();

            System.out.println("Enter the position at which the element has to be stored:");
            int pos = scan.nextInt();

            arr[pos] = elem;
            System.out.println(arr[pos]);
        }
        
        
        // --- Alternate code ---
        catch(ArithmeticException e)
        {
            System.out.println("Please provide non-zero denominator");
        }
        catch(NegativeArraySizeException e)
        {
            System.out.println("Please provide the non-negative array size");
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Please provide an index value within the range of array");
        }
        catch(Exception e)
        {
            System.out.println("Some problem occurred");
        }

        System.out.println("connection is terminated");
    }
}

```


