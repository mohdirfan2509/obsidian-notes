# 💻 **Class 6: Application Program, System Program & Kernel**
---
## 📚 **Topics**
1. Application Program
2. System Program
3. Kernel
---
## 🧩 **1. Application Program**
### 📌 **Definition**
- Software designed to perform a **specific task for the user**.
### 🎯 **Purpose**
- Directly helps the user with:
    - Work
    - Entertainment
    - Communication
### 🧪 **Examples**
- MS Word → Writing
- Photoshop → Editing
- Chrome → Browsing
- VLC → Media playback
### 🪑 **Analogy**
- Application programs are like **furniture in a house**.
- Customized for user needs (sofa, table, TV).
- Similar to **apps on a smartphone**.
---
## ⚙️ **2. System Program**
### 📌 **Definition**
- Software that helps **run computer hardware** and provides a platform for application programs.
### 🌉 **Purpose**
- Acts as a **bridge** between applications and hardware.
- Ensures smooth execution of programs.
### 🧰 **Examples**
- Operating system components:
    - File management utilities
    - Disk defragmenter
- Compilers
- Assemblers
- Device drivers
### 🔌 **Analogy**
- System programs are like **electric wiring and plumbing** in a house.
- Hidden but essential.
- Without them, furniture (applications) cannot function.
---
## 🧠 **3. Kernel**
### 📌 **Definition**
- The **core part of the operating system** that directly interacts with hardware
### 🎯 **Purpose**
- Manages:
    - CPU
    - Memory
    - I/O devices
- Provides essential services to system and application programs.
### 🧪 **Examples**
- Linux kernel
- Windows NT kernel
### 🏗️ **Analogy**
- Kernel is like the **foundation and skeleton** of a house.
- Not directly visible, but without it everything collapses.
---
## 🔗 **Relationship Between Application, System Program & Kernel**
- **Application Program** → User-facing  
    _“What you see and use”_
- **System Program** → Middle layer  
    _“Helps applications run smoothly”_
- **Kernel** → Deepest layer  
    _“Controls hardware resources”_
---
## 🧱 **Layered View of the System**

```
[Application Programs] → Games, Browsers, MS Office
[System Programs]      → Compiler, File Manager, Drivers
[Kernel]               → CPU, Memory, Device Control
[Hardware]             → Actual computer hardware
```
---
## 🖥️ **I. Components of the Operating System**
- The OS is divided into:
    - **User Space (User Mode)**
    - **Kernel Space (Kernel Mode)**
- Together, they form the **Operating System**.
---
## 🔒 **A. Kernel Space (Kernel Mode)**
- Protected area where the **kernel runs**.
- Heart and core of the OS.
- First part of the OS to load at startup.
- Has **direct access to hardware**:
    - CPU
    - Memory
    - Devices
- Performs the most **critical tasks** of the OS
### 🏗️ **Analogy**
- Like the **foundation and skeleton** of a house.
---
## 👤 **B. User Space (User Mode)**
- Environment where:
    - Applications
    - Shells  
        run.
- Applications **cannot directly access hardware**.
- Must interact with the kernel.
- Provides user interaction with the OS.
---
## 🖱️⌨️ **Shells in User Space**
### 🖼️ **GUI (Graphical Shell)**
- Windows Explorer
- Desktop, Taskbar, File Explorer
- Finder in macOS
### ⌨️ **CLI (Command-Line Shell)**
- Command Prompt
- PowerShell
- Bash
### 🚪 **Analogy**
- GUI and CLI are **two doors to the same house**.
- Different paths, same kernel doing the real work.
---
## 📁 **Interaction Example: Creating / Deleting a Folder**
### 🧩 **Creating a Folder*
1. **User**
    - GUI: Right-click → New → Folder → “OS”
    - CLI: `mkdir OS`
2. **Shell (GUI/CLI)**
    - Interprets the action.
3. **System Programs**
    - File manager routines decide how and where.
4. **Kernel**
    - Updates file system metadata.
    - Allocates space.
    - Communicates with disk.
5. **Hardware**
    - Physically stores the folder entry.
---
### 🗑️ **Deleting a Folder**
- GUI delete:

    - Moves to Recycle Bin (unless Shift+Delete)        
- CLI delete:
    - `rmdir OS` removes it directly
➡️ The shell never deletes anything itself—it only **requests the kernel**.
---
## ⚙️ **II. Functions of the Kernel**
---
### 🔄 **1. Process Management**
- Create, terminate, suspend, resume processes.
- CPU scheduling.
- Context switching.
- Process synchronization and communication.
---
### 🧠 **2. Memory Management**
- Allocate and deallocate memory.
- Track memory usage per process.
- Reclaim memory when processes exit.
---
### 📂 **3. File Management**
- Create and delete files/directories.
- Maintain hierarchical structure.
- Map files to secondary storage.
- Provide backup and recovery support.
---
### 🔌 **4. I/O Management**
- Add and manage I/O devices.
- Coordinate data transfer.
- Notify OS when new devices connect.
#### 🛠️ **Key Techniques**
- **Spooling** → Handling speed mismatch (print jobs).
- **Buffering** → Temporary storage (YouTube buffering).
- **Caching** → Frequently used data kept nearby.
---
## 🧬 **III. Types of Kernels**
---
### 🧱 **1. Monolithic Kernel**
- All functions inside one large kernel.
- High performance.
- Less reliable (one crash affects entire OS).
- Examples:
    - Linux
    - Unix
    - MS-DOS
---
### 🧩 **2. Microkernel**
- Only essential services inside kernel.
- File and I/O management in User Space.
- More reliable.
- Slower due to frequent mode switching.
- Examples:
    - MINIX
    - Symbian OS
    - L4
---
### ⚖️ **3. Hybrid Kernel**
- Combination of monolithic and microkernel.
- Balances speed and stability.
- Examples:
    - Windows NT
    - Windows 10
    - macOS
---
## 🔁 **IV. Inter-Process Communication (IPC)**
- Needed because processes are isolated.
### 🧩 **Types**
- **Shared Memory**  
    Multiple processes read/write the same memory block.
- **Message Passing**  
    Processes communicate via pipes or message queues.
---
## 🏠 **House Analogy Recap*
- **Application Programs** → Furniture
- **System Programs** → Wiring & Plumbing
- **Shells (GUI/CLI)** → Doors
- **Kernel** → Foundation & Control Room
- **Hardware** → Building materials (CPU, RAM, Disk)
___
![Class 01 : Slides ](../os-slides/Class-06-slides.pdf)
___