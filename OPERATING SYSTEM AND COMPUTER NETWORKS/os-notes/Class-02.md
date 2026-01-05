# 🧠 **Topic: Types of Operating Systems**
---
## 🎯 **I. Goals of an Operating System**
- **Maximum CPU Utilization**  
    Keep the CPU busy; if a process waits for I/O, the CPU immediately works on another job.
- **Minimal Process Starvation**  
    Prevent indefinite blocking so every process eventually executes.
- **Timely Execution of High-Priority Jobs**  
    Critical tasks (e.g., antivirus scans) must run promptly.
---
## 🖥️ **II. Types of Operating Systems**
---
### 1️⃣ **Single-Process (Single-User, Single-Tasking) OS**

- Runs only **one job at a time**
- **Drawbacks**
    - Low CPU utilization
    - Possible starvation
    - High-priority jobs must wait
- **Example**: Early MS-DOS
---
### 2️⃣ **Batch Processing OS**

- Users submitted jobs on **punch cards**
- Operator grouped similar jobs into **batches**
- CPU executes jobs **batch by batch**
- **Drawback**:  
    If one job runs long, later jobs wait
- **Historical Example**: Atlas computer’s batch system
---
### 3️⃣ **Multiprogramming OS**

- Multiple jobs stored in a **ready queue** on a single CPU
- When one job waits for I/O, the OS performs **context switching**
- **Goal**: Maximize CPU utilization
- **Example**: IBM OS/360, early UNIX
---
### 4️⃣ **Multitasking / Time-Sharing OS**

- Logical extension of multiprogramming
- CPU time divided into fixed **time quanta** (e.g., 100 ms)
- **Pre-emptive scheduling** improves responsiveness and fairness
- **Example**: CTSS (Compatible Time-Sharing System)
---

### 5️⃣ **Multiprocessing OS**

- Uses **multiple CPUs**
- Provides:
    - Higher throughput
    - Better reliability (failure of one CPU doesn’t halt the system)
- **Example**: Modern Windows, Linux on multi-core processors
---
### 6️⃣ **Distributed OS**

- Loosely coupled computers connected via a **network**
- Share tasks and resources
- Nodes may have **different configurations**
- **Example**: Amoeba, modern cloud clusters
---
### 7️⃣ **Real-Time OS (RTOS)**

- Guarantees task completion within **strict time limits**
- Used in:
    - Flight control
    - Industrial automation
    - Nuclear systems
---

## 🔄 **III. Context Switching**
---
### 📌 **Definition**
Context switching is the act of **saving the state of a running process** and **loading the state of another** so multiple processes can share a single CPU.

---
### 🧩 **Steps in Context Switching**

1. Save the current process state  
    _(program counter, CPU registers, stack pointer)_ into its **Process Control Block (PCB)**
2. Load the next process’s saved state from its **PCB**
3. Resume execution of the next process

---
### ✨ **Key Idea**
This rapid save-and-restore creates the **illusion of simultaneous execution**.
___
![Class 02 : Slides ](Class-02-slides.pdf)
___
