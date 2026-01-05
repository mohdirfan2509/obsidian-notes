# 🧠 **Core Concepts: Program, Process, and Thread**
---
## 📦 **A. Program**
### 📌 **Definition**
- An **executable file** containing instructions to perform a job.
### 💾 **Storage**
- Resides on **secondary storage (disk)**.
### 📄 **Format**
- A **compiled binary** (e.g., `.exe` on Windows).
- Cannot be read in a normal text editor.
- Includes **platform-specific details** required for execution.
---
## ⚙️ **B. Process**
### 📌 **Definition**
- A **program in execution**.
### ▶️ **Creation**
- When a program is launched (e.g., double-clicked), it is loaded into **primary memory (RAM)** and becomes a process.
### 🧠 **Execution Requirement**
- A program on disk **cannot run** until it is loaded into RAM.
### 🖌️ **Example**
- Opening **MS Paint** creates a process named _“MS Paint”_, visible in the taskbar.
---
## 🧵 **C. Thread (Lightweight Process)**
### 📌 **Definition**
- The **smallest independent unit of execution** within a process.
- Often called a **lightweight process**.
### 🧩 **Structure**
- A **single sequence stream** inside a process.
### 🎯 **Role**
- Handles **sub-tasks** that can run independently of the main flow.
### 📱 **Example**
- An application may use separate threads for:
    - User input
    - Network fetch
    - Computation
    - Saving data
- One thread can upload data asynchronously while others continue working.
---
## 🔁 **Multi-Threading**
### 📌 **Concept**
- Running **multiple threads concurrently** within a single process.
### 🚀 **Goal (Parallelism)**
- Allows different parts of a program to execute simultaneously.
- Reduces total **run time**.
### 🖼️ **Example**
- Converting a large image can be split across two threads to nearly halve processing time—if hardware allows true parallelism.
### 🧠 **Hardware Dependency**
- Real speedup occurs only on systems with **multiple cores/CPUs**.
- On a single core:
    - Threads only **time-share** via context switching.
    - Little or no performance gain.
### ✅ **Best Practice**
- Create a number of threads that matches the available **logical processors / cores**.
---
## ⚖️ **Multi-Tasking vs Multi-Threading — Key Differences**

| Feature                | Multi-Tasking                           | Multi-Threading                             |
| ---------------------- | --------------------------------------- | ------------------------------------------- |
| Scope of Concurrency   | Multiple **processes** run concurrently | Multiple **threads** run within one process |
| Isolation & Protection | Separate memory and full protection     | Shared memory, no isolation                 |
| Scheduling Unit        | OS schedules **processes**              | OS schedules **threads** (priority-based)   |
| CPU Requirement        | Works on a single CPU via time-sharing  | True gain when CPU/cores > 1                |

---
## 🔄 **Context Switching**
### 📌 **Meaning**
- Switching involves saving the current state (program counter, registers) and restoring the next task’s state.    
---
## 🧱 **A. Process Context Switching**
1. **Memory Space Switch**
    - Required because each process has its own protected address space.
2. **Speed**
    - Slower due to memory mapping overhead.
3. **CPU Cache**
    - Cache is flushed since previous process data is usually irrelevant.
---
## 🧵 **B. Thread Context Switching**
1. **Memory Space Switch**
    - Not required because threads share the same address space.
2. **Speed**
    - Faster due to no heavy memory mapping.
3. **CPU Cache**
    - Cache is preserved and reused.
---
## 🔑 **Key Takeaway**
- **Multi-Tasking** improves system responsiveness by allowing multiple processes to share CPU time.
- **Multi-Threading** improves a single program’s efficiency by allowing parallel task execution—**real speedup only when hardware supports it**.
--
# 📝 **Short Notes (LEC-3: Multi-Tasking vs Multi-Threading)**
---
## 📦 **Program**
- An executable file containing instructions to complete a specific job.
- Compiled code, ready to be executed.
- Stored on **disk**.
---
## ⚙️ **Process**
- A program under execution.
- Resides in **primary memory (RAM)**.
---
## 🧵 **Thread**
- Single sequence stream within a process.
- Independent path of execution.
- Lightweight process.
- Used to achieve parallelism by dividing independent tasks.
### 🌐 **Example**
- Browser tabs.
- Text editor tasks such as:
    - Typing
    - Spell-checking
    - Formatting
    - Saving text  
        (All handled concurrently by multiple threads.)
---
## ⚖️ **Multi-Tasking vs Multi-Threading (Short Comparison)**
### 🧩 **Multi-Tasking**
- Execution of more than one task simultaneously.
- Multiple processes are context-switched.
- Number of CPUs: **1**
- Isolation and memory protection exist
- OS allocates separate memory and resources.
### 🧵 **Multi-Threading**
- A process is divided into multiple threads.
- Threads are context-switched.
- Number of CPUs: **≥ 1** (better with more).
- No isolation or memory protection.
- Threads share memory and resources of the process.
___
## ⏱️ **Thread Scheduling**
- Threads are scheduled based on **priority**.
- All threads receive CPU time slices from the OS.
---
## 🔄 **Thread vs Process Context Switching**

| Thread Context Switching                 | Process Context Switching            |
| ---------------------------------------- | ------------------------------------ |
| Switches between threads of same process | Switches between different processes |
| No memory address space switch           | Memory address space switch required |
| Fast switching                           | Slow switching                       |
| CPU cache preserved                      | CPU cache flushed                    |

___
![Class 05 : Slides ](Class-05-slides.pdf)
___
