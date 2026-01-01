
![[Pasted image 20251206220040.jpg]]
![[Pasted image 20251206220100.jpg]]![[Pasted image 20251206220118.jpg]]![[Pasted image 20251206220123.jpg]]![[Pasted image 20251206220128.jpg]]![[Pasted image 20251206220144.jpg]]
___
# **Topic1: Understanding the Operating System (OS)** 

**Definition:**  An Operating System (OS) is a piece of software that manages all the resources of a computer system—both hardware and software—and provides an environment in which the user can execute programs conveniently and efficiently. It hides the underlying complexity of hardware and acts as a resource manager. 
___

**Why Do We Need an OS?** 

1. **Without an OS:** 
     - **Bulky and Complex Applications:** Every app would need its own hardware  interaction code, making the code base huge. 
     - **Resource Exploitation by a Single App:** Apps like Instagram or BGMI could monopolize CPU, memory, or GPU resources, causing instability.
     - No Memory Protection: One app could overwrite another app’s memory. 
2. **Efficient Resource Allocation:** 
     - The OS ensures fair and controlled distribution of resources (e.g., Instagram gets 5%, BGMI gets 50%).
     - Prevents conflicts and maintains system stability.
___
**Key Functions of an OS**

- **Resource Management (Arbitration)**: Allocates and manages CPU, memory, storage, devices, files, security, and processes.
- **Access to Hardware:** Provides controlled access to the computer’s hardware components. 
- **Interface/Bridge:** Acts as an interface between the user, applications, and the hardware. 
- **Isolation & Protection:** Prevents apps from interfering with each other (e.g., Instagram cannot overwrite BGMI’s memory).
- **Abstraction:** Hides the underlying hardware complexity, letting developers focus on application logic. 
- **Program Facilitation:** Enables smooth execution of applications by providing isolation and protection.
___
**Q :  Why in OS resource management is often called arbitration?**

  - **Arbitration – English meaning:** 
    The word arbitration comes from arbiter, meaning a neutral judge or referee. In everyday English it refers to **settling a dispute or making a fair decision when two or more parties want the same thing.** 
  - **In Operating Systems:** 
    Resources such as the CPU, memory, disk, or I/O devices are limited, while many programs may request them at the same time. The OS acts like that neutral judge—it **arbitrates** by deciding **who gets the resource, for how long, and in what order.**
  - Examples:
    - If several processes are ready to run, the OS scheduler **arbitrates** CPU time according to a scheduling algorithm. 
    - When multiple programs want to write to a file or send data to the printer, the OS **arbitrates** to prevent conflicts and ensure fairness or priority handling.
    
    So, in OS terminology, **resource management is often called arbitration** because the core of managing resources is this **decision-making process of fair allocation and conflict resolution**, just as an arbiter settles disputes in everyday life.  
___
___
# **Topic2: User View and System View:**

