# 🧠 **Class 8: System Calls & User–Kernel Interaction**
---
## 🔗 **How Do Applications Interact with the Kernel?**
➡️ **Using system calls**

---
## 📞 **System Call – Core Idea**
- A **system call** is a mechanism through which a **user program requests a service from the kernel**.
- These are operations that user programs **do not have permission** to perform directly.
- Examples of restricted operations:
    - Accessing I/O devices
    - Creating processes
    - Communicating with other programs
- **System calls are implemented in C**.
- Transitions from **User Space (US)** to **Kernel Space (KS)** are done using **software interrupts**.
---
## 📁 **Example: `mkdir OS`**
- `mkdir` **does not create a directory by itself**.
- It indirectly calls the kernel and asks the **file management module** to create a directory
- `mkdir` is just a **wrapper** around actual system calls.
- Interaction flow:
    - User executes `mkdir OS`
    - `mkdir` makes a **system call**
    - Kernel performs the directory creation
---
## ⚙️ **Example: Creating a Process**
1. User executes a program (**User Space**).
2. A **system call** is triggered.
3. Kernel executes the request (**Kernel Space**).
4. Control returns to **User Space**.
---
## 🧾 **Definition (Formal)**
A system call is a mechanism using which a user program can request a service from the kernel, which it does not have the permission to perform.

---
## 🧩 **Types of System Calls**
---
### 🔄 **1. Process Control**
- end, abort
- load, execute    
- create process, terminate process
- get / set process attributes
- wait for time
- wait event, signal event
- allocate and free memory
---
### 📂 **2. File Management**
- create file, delete file
- open, close
- read, write, reposition
- get / set file attributes
---
### 🔌 **3. Device Management**
- request device, release device
- read, write, reposition
- get / set device attributes
- logically attach or detach devices
---
### ℹ️ **4. Information Maintenance**
- get / set time or date
- get / set system data
- get / set process, file, or device attributes
---
## 🖥️ **Examples of System Calls (Windows vs Unix)**
### 🔄 **Process Control**
- **Windows**: `CreateProcess()`, `ExitProcess()`, `WaitForSingleObject()`
- **Unix**: `fork()`, `exit()`, `wait()`
### 📂 **File Management**
- **Windows**: `CreateFile()`, `ReadFile()`, `WriteFile()`, `CloseHandle()`
- **Unix**: `open()`, `read()`, `write()`, `close()`, `chmod()`, `chown()`
### 🔌 **Device Management**
- **Windows**: `SetConsoleMode()`, `ReadConsole()`, `WriteConsole()`
- **Unix**: `ioctl()`, `read()`, `write()`
### ℹ️ **Information Management**
- **Windows**: `GetCurrentProcessID()`, `SetTimer()`, `Sleep()`
- **Unix**: `getpid()`, `alarm()`, `sleep()`
### 🔗 **Communication**
- **Windows**: `CreatePipe()`, `CreateFileMapping()`, `MapViewOfFile()`
- **Unix**: `pipe()`, `shmget()`, `mmap()`
---
## 🧪 **C Program Example: File Copy**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *src, *dest;
    char ch;

    src = fopen("input.txt", "r");
    if (src == NULL) {
        printf("Cannot open source file.\n");
        return 1;
    }

    dest = fopen("output.txt", "w");
    if (dest == NULL) {
        printf("Cannot open destination file.\n");
        fclose(src);
        return 1;
    }

    while ((ch = fgetc(src)) != EOF) {
        fputc(ch, dest);
    }

    printf("File copied successfully!\n");
    fclose(src);
    fclose(dest);
    return 0;
}
```
---
## 🖨️ **What Happens When You Print “Hello World”?**
> “If I print Hello World on the console, some system call must be made.”
✔️ True — but it’s **hidden by abstractions**.
---
## 🔍 **Hidden Call Chain for `printf()` (Windows)**

```
printf()
↓
fwrite()
↓
WriteFile()
↓
NtWriteFile()
↓
Windows Kernel
```

- The **actual kernel system call** is `NtWriteFile()`.
- `WriteConsole()` is **not used** by `printf()`.
---
## ❓ **Why `WriteConsole()` Is Not Seen**
- `WriteConsole()` is part of the **Win32 API**.
- The C runtime library:
    - Uses `WriteFile()` instead
    - Treats the console as a **file-like stream**
- Console output is rendered by **conhost.exe**, not directly by your app.
---
## 📥 **STDIN, STDOUT, STDERR**
At program start, the OS provides:
1. **STDIN** → Keyboard
2. **STDOUT** → Console
3. **STDERR** → Console
- `printf()` writes to **STDOUT**
- Redirection example:

```
     a.exe > output.txt
```

STDOUT now points to a file — system calls remain the same.

---
## 🔎 **Tracing in Process Monitor (ProcMon)**
Steps:
1. Open ProcMon
2. Filter:
    - Process Name → `a.exe`
    - Operation → `WriteFile`
3. Run the program
You’ll see:

```
WriteFile  conhost.exe  SUCCESS  Length: 12
```
---
## 🧠 **What Is `conhost.exe`**
- Console Host process
- Responsible for rendering text in Command Prompt
- Console output path:
    
    ```
    YourApp → kernel32.dll → conhost.exe
    ```
    
---
## 📝 **Summary (System Calls)**
- `printf()` does **not** call `WriteConsole()`
- It uses `WriteFile()` → `NtWriteFile()`
- Console is treated as a **file**
- Kernel interaction is **abstracted**
---
# 🧩 **Class 8: Kernel Data Structures**
---
## 🏗️ **Kernel Data Structures – Core Importance**
- Central to **OS implementation**
- Enable efficient:
    - Scheduling
    - Memory management
    - File systems
    - Process control
---
## 📋 **1. Lists, Stacks, and Queues**
---
### 🧮 **1.1 Arrays**
- Direct access data structure
- Limitations:
    - Inefficient for variable-sized items
    - Deletion requires shifting
- OS Example:
    - Main memory organization
---
### 🔗 **1.2 Lists**
- Sequential collection of data
- Implemented using **linked lists**
- Advantages:
    - Easy insertion and deletion
    - Supports variable sizes
- Disadvantages:
    - Linear-time search
- Uses:
    - Kernel algorithms
    - Building stacks and queue
#### Types:
- Singly linked list
- Doubly linked list
- Circular linked list
- OS Example:
    - Linux process lists (doubly linked lists)
---
### 📚 **1.3 Stacks**
- Follows **LIFO**
- Operations:
    - Push
    - Pop
- OS Example:
    - Function calls
    - Parameters, local variables, return addresses
---
### 🚶 **1.4 Queues**
- Follows **FIFO**
- OS Examples:
    - Printer job scheduling
    - CPU ready queues
---
## 🌳 **2. Trees**
- Hierarchical data structure
- Types:
    - General tree
    - Binary tree
    - Binary Search Tree (BST)
- BST:
    - Worst case: O(n)
    - Balanced BST: O(log n)
- OS Example:
    - Linux uses **Red-Black trees** for CPU scheduling
---
## 🔑 **3. Hash Functions and Maps**
---
### 🔢 **3.1 Hash Functions**
- Convert input into numeric index
- Retrieval near O(1)
- Collision handling:
    - Linked lists
- OS Example:
    - Process table lookup
    - File descriptor tables
---
### 🗺️ **3.2 Hash Maps**
- Maps **key → value**
- OS Example:
    - Username → Password mapping
---
## 🧮 **4. Bitmaps**
- String of binary digits
- Usage:
    - 0 → available
    - 1 → unavailable
- Space efficient
- OS Example:
    - Disk block allocation in Linux
---
## 🐧 **5. Linux Kernel Data Structures**

| Data Structure | Linux Implementation | OS Example     |
| -------------- | -------------------- | -------------- |
| Linked Lists   | `<linux/list.h>`     | Process lists  |
| Queues         | `kfifo.c`            | I/O buffers    |
| Balanced BST   | `<linux/rbtree.h>`   | CPU scheduling |

---
## 🧾 **Final Summary**
- Kernel data structures:
    - Lists
    - Stacks
    - Queues
    - Trees
    - Hash maps
    - Bitmaps
- Essential for **efficient OS operation**
- Linux provides optimized implementations inside the kernel source.
___
![Class 01 : Slides ](Class-08-slides.pdf)
___
