# 🧠 **Introduction to Concurrency**
---
## 🔄 **1. Concurrency**
- Concurrency refers to the execution of **multiple instruction sequences** in an **overlapping time period**.
- In an operating system, concurrency occurs when **multiple processes or threads** are in progress at the same time.
- This allows **better utilization of system resources**.
### ⚠️ **Note**
- Concurrency does **not necessarily mean simultaneous execution**.
- **Simultaneous execution** is called **parallelism**.
---
## 🧵 **2. Thread**
A **thread** is:
- A **single sequence stream of execution** within a process
- An **independent path of execution** inside a process
- A **light-weight process**
- A mechanism to achieve **concurrency** by dividing a process into independent execution paths
### 🧪 **Examples**
- Multiple tabs running in a web browser
- In a text editor:
    - Typing
    - Spell checking
    - Formatting
    - Auto-saving  
        (All occur concurrently using multiple threads)
---
## ⏱️ **3. Thread Scheduling**
- Threads are scheduled based on:
    - **Priority**
    - **Scheduling policy**
- The **OS scheduler** assigns CPU **time slices** to threads.
- Even though threads belong to a process:
    - CPU allocation is controlled by the **Operating System**
    - Not by the runtime environment
---
## 🔁 **4. Thread Context Switching**
- Occurs when the OS switches the CPU from **one thread to another** within the same process.
### 🔧 **During Thread Context Switching**
- **Memory address space is NOT switched** (shared among threads)
- The following are switched:
    - Program Counter (PC)
    - CPU registers
    - Stack
### ⚡ **Characteristics**
- Faster than **process context switching**
- Cache performance may improve due to locality
- Cache contents are **not guaranteed** to be preserved
---
## 🎯 **5. How Does Each Thread Get Access to the CPU?**
- Each thread has its own **Program Counter (PC)**.
- The OS selects a thread based on the **thread scheduling algorithm**.
- The OS:
    - Fetches instructions using the selected thread’s PC
    - Executes them on the CPU
---
## 🔄 **6. I/O or Time-Quantum Based Context Switching*
- Context switching can occur due to:
    - I/O operations
    - Expiry of time quantum
### 🗂️ **Thread Control Block (TCB)**
- Each thread has a **TCB**
- Similar to a **Process Control Block (PCB)**
- Stores thread state information during context switching
---
## 🖥️ **7. Multithreading on a Single-CPU System**
- A single-CPU system does **not gain execution speed or throughput** from multithreading.
- Only **one thread executes at a time**.
- Multithreading still improves **responsiveness**, especially for **I/O-bound applications**.
---
## 🌟 **8. Benefits of Multithreading**
- **Responsiveness**  
    Applications remain active even if one thread is blocked.
- **Resource Sharing**  
    Threads efficiently share process resources.
- **Economy**
    - Thread creation and context switching are cheaper than process creation.
    - Process creation requires significant memory and resource allocation.
- **Scalability**  
    Efficient utilization of **multicore** and **multiprocessor** architectures.
___
![Class 15 : Slides ](../os-slides/Class-15-slides.pdf)
___
