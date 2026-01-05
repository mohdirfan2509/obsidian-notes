# 💻 **Class 4: How Computer Programs Execute**
---
## 🧩 **Topics Covered**

1. Bootloader Program
2. User Program
3. Compiler
4. Machine Code
5. CPU Execution
---
## 🔌 **Bootloader Program (ROM & Primary-Memory Context)**
---
### 🧠 **Primary Memory and Why ROM Matters**

- Primary Memory consists of:
    - **RAM** (volatile)        
    - **ROM** (non-volatile)
- ROM retains data even when power is OFF, making it ideal for storing **firmware**.
- Firmware is tiny, permanent software that starts the computer.
- This firmware includes:
    - **BIOS** (Basic Input/Output System)
    - **UEFI** on modern PCs
---
### ⚡ **What Happens at Power-On**
---
#### 1️⃣ **Power-On Self-Test (POST)**
- After pressing the power button, the CPU fetches the **first instructions from ROM**.
- BIOS runs diagnostic checks on:
    - CPU
    - RAM modules
    - Keyboard
    - Other peripherals
- If an error occurs (e.g., loose RAM), BIOS issues **beep codes**.
---
#### 2️⃣ **Bootloader Code Execution**
- After POST succeeds:
    - BIOS/UEFI (still running from ROM) searches for a **secondary bootloader** on:
        - HDD / SSD
        - USB, etc.
- The bootloader is:
    - Copied into **RAM**
    - Control is transferred to it
- Examples:
    - **GRUB** (Linux)
    - **Windows Boot Manager**
---
#### 3️⃣ **Operating System Loading**
- Bootloader locates the **OS kernel** on disk.
- Loads the kernel into **RAM**.
- Transfers control to the OS.
- Only then does the **login screen** appear.
---
### 🧠 **Digital-Logic Architecture of ROM**
- ROM uses:
    - An **n-to-2ⁿ address decoder** to activate one word line.
    - A fixed ROM matrix with programmable connections.
- Connections are implemented using **fuses / antifuses**.
- These fixed patterns ensure:
    - The CPU always reads the same boot instructions.
    - A **reliable and consistent start-up**.
---
### 🧬 **Types of ROM Used in Bootloaders**
- **PROM**  
    Programmed once; fuses permanently set.
- **EPROM**  
    Erased using UV light and re-programmed.
- **EEPROM / Flash ROM**  
    Electrically erasable and re-writable; used in modern motherboards for BIOS/UEFI updates.
---
### 🔑 **Key Idea**
The bootloader stage is possible only because firmware stored in **ROM** (non-volatile, fuse-programmed digital logic) survives power cycles and is instantly available to the CPU at power-on.
---
### 📚 **Reference Links**
- Intel: System Boot Process
- Patterson & Hennessy, _Computer Organization and Design_ (Boot process chapters)
---
## 👨‍💻 **User Program**
---
### 📝 **What It Is**
- Source code written by a programmer.
- Written in high-level languages such as:
    - C
    - Java
    - Python
- Human-readable.
- Not directly understood by hardware.
---
### 💡 **Example**

```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```
---
### 📚 **Reference**
- Kernighan & Ritchie, _The C Programming Language_, Prentice Hall
---
## 🛠️ **Compiler**
---
### 🔄 **What It Does**
- Translates high-level source code into:
    - Machine code, or
    - Intermediate code
- Performs:
    - Lexical analysis
    - Parsing
    - Optimization
    - Code generation
---
### 🔁 **Flow**

```
Source Code → Compiler → Object / Machine Code
```

- Some languages (e.g., Java) compile to **bytecode**, later interpreted or JIT-compiled by the JVM.
---
### 📚 **Reference**
- Alfred V. Aho et al., _Compilers: Principles, Techniques, and Tools_ (Dragon Book)    
---
## 🔢 **Machine Code**
---
### ⚙️ **What It Is**
- Binary instructions (0s and 1s).
- Executed directly by the CPU.
- Architecture-specific:
    - x86
    - ARM
    - RISC-V
---
### 🧩 **Characteristics**
- Contains:
    - **Opcodes** (operations)
    - **Operands**
- Often written in hexadecimal for readability  
    (e.g., `B8 01 00` for x86).
---
### 📚 **Reference**
- Patterson & Hennessy, _Computer Organization and Design_
---
## ⚙️ **CPU Execution**
---
### 🔁 **How It Works**
- CPU:
    - Fetches instructions from RAM
    - Decodes them
    - Executes them
- This **fetch–decode–execute cycle** runs billions of times per second.
---
### 🧩 **Execution Steps**
1. **Fetch**  
    Program Counter (PC) points to the next instruction.
2. **Decode**  
    Instruction Decoder identifies the required operation.
3. **Execute**  
    ALU or other units perform computation, memory access, or I/O.
---
### 📚 **Reference**
- David A. Patterson & John L. Hennessy, _Computer Organization and Design_, Chapters 4–5
---
## 🔗 **Putting It All Together (Correct Order)**
1. **Bootloader Program**  
    Initializes hardware and loads the OS.
2. **User Program**  
    Programmer writes source code inside the OS.
3. **Compiler**  
    Converts source code into machine code.
4. **Machine Code**  
    Stored as an executable and loaded into RAM.
5. **CPU Execution**  
    CPU fetches and runs binary instructions.
---
## 🚗 **Quick Analogy**

| Computer Step      | Car Analogy                            |
| ------------------ | -------------------------------------- |
| Bootloader Program | Turning the ignition                   |
| User Program       | Driver planning the route              |
| Compiler           | Translating plan into GPS instructions |
| Machine Code       | Precise GPS directions                 |
| CPU Execution      | Engine moving the car                  |

---
## 🧾 **Summary**
When a computer powers on, the **bootloader** prepares the system.  
A programmer writes a **user program**, which a **compiler** converts into **machine code**.  
The **CPU** then fetches, decodes, and executes these instructions—making the software run.

---
## 🧠 **UEFI (Unified Extensible Firmware Interface)**
---
### 🎯 **Purpose**
UEFI is low-level firmware that:
- Initializes and tests hardware.
- Loads the OS bootloader into RAM.
- Provides a runtime environment for firmware utilities.
---
### ⚙️ **Key Characteristics**

| Feature       | UEFI                             | Legacy BIOS  |
| ------------- | -------------------------------- | ------------ |
| Interface     | Graphical, mouse support         | Text-only    |
| Storage       | Flash ROM                        | ROM / Flash  |
| Boot Method   | GPT, EFI System Partition        | MBR          |
| Extensibility | Drivers, networking, secure boot | Very limited |

---
### 🔁 **UEFI Boot Process**
1. Power On → CPU executes firmware from flash ROM
2. UEFI runs → POST checks
3. Boot Manager → Reads EFI System Partition
4. OS Loader → Loads OS kernel into RAM
---
### 🔐 **Why It Matters**
- **Secure Boot**: Blocks unauthorized bootloaders.
- **Faster Startup**: Parallel hardware initialization.
- **Large Disk Support**: Works with disks > 2 TB using GPT.
---
### 🧩 **GUID (Globally Unique Identifier)**
- Each disk partition is assigned a **128-bit GUID**.
- Ensures partitions are uniquely identified across systems.
---
![Class 04 : Slides ](Class-04-slides.pdf)