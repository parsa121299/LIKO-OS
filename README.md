# LIKO OS
### An Independent, Lightweight, Native x86_64 Operating System

<p align="center">
  <img src="Assets/Branding/liko-banner.png" alt="LIKO OS Banner" width="100%" />
</p>

<p align="center">
  <strong>ENGINEERED FOR EFFICIENCY. BUILT FOR INDEPENDENCE.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT-LIKO%20OS-101D35?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ARCHITECTURE-x86__64-1769AA?style=for-the-badge" />
  <img src="https://img.shields.io/badge/KERNEL-C%20%2B%20ASM-00599C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PLATFORM-VMware-607078?style=for-the-badge" />
  <img src="https://img.shields.io/badge/STATUS-EARLY%20DEVELOPMENT-orange?style=for-the-badge" />
</p>

---

## 01 — Project Overview

**LIKO OS** is an independent operating system development project focused on building a lightweight, native computing environment with a dedicated kernel and a custom graphical user interface.

Unlike desktop simulations and applications that imitate operating system interfaces, LIKO OS is intended to operate as a standalone system with its own boot process, kernel architecture, memory management, hardware interaction, and system-level services.

The primary development target is VMware Workstation, providing a controlled environment for kernel development, hardware compatibility testing, debugging, and system validation.

The central engineering objective is straightforward:

> Build a complete operating system while keeping its architecture, resource consumption, and internal complexity as efficient as possible.

LIKO OS is being developed with C as its primary implementation language, supported by Assembly for low-level operations where required.

---

## 02 — Engineering Philosophy

LIKO OS follows six fundamental engineering principles.

| Principle | Engineering Objective |
|---|---|
| Lightweight Architecture | Minimize unnecessary resource consumption |
| Native Execution | Run directly on the target machine's processor |
| Hardware Independence | Use hardware abstraction rather than application-level simulation |
| Offline Capability | Keep core system functionality independent of internet access |
| Modular Design | Separate kernel, drivers, graphics, and applications |
| Controlled Development | Validate components independently before integration |

### Lightweight by Design

Performance optimization is not intended to be a final development stage.

It is a design requirement that influences kernel architecture, memory allocation, graphics rendering, system services, and application development from the beginning.

### Native Hardware Access

LIKO OS is not designed around an internal virtual CPU or simulated RAM.

When running inside VMware, it will communicate with the virtual hardware devices presented by the hypervisor through appropriate operating system drivers.

The operating system itself will manage its own memory, processes, and hardware interfaces.

---

## 03 — Target Platform & System Specifications

### Target Architecture

| Parameter | Design Specification |
|---|---|
| System Architecture | x86_64 |
| Primary Language | C |
| Low-Level Language | x86_64 Assembly |
| Target Hypervisor | VMware Workstation |
| Boot Architecture | BIOS / UEFI |
| Kernel Type | Independent Native Kernel |
| Display Architecture | Framebuffer |
| Graphics Environment | Custom Desktop |
| Storage Interface | Virtual Storage Devices |
| Network Requirement | Optional |
| Internet Dependency | None for core operation |
| Distribution Target | Bootable ISO |

BIOS and UEFI support are planned capabilities, not yet confirmed implementations.

### Resource Engineering Targets

LIKO OS aims to operate within a constrained resource budget.

| Resource | Initial Design Target |
|---|---:|
| RAM | 256 MB |
| Processor | 1 Virtual CPU Core |
| Storage | 512 MB |
| Network | Optional |
| Installation Media | ISO |

These figures represent initial engineering targets. Actual minimum requirements will be determined through testing and optimization.

---

## 04 — System Architecture

LIKO OS is planned as a layered operating system architecture.

```text
+------------------------------------------+
|             LIKO DESKTOP                 |
|       Windows / Taskbar / Start          |
+------------------------------------------+
|          SYSTEM APPLICATIONS             |
|  Terminal | Explorer | Settings | Tools   |
+------------------------------------------+
|            SYSTEM SERVICES               |
|     Process Services / File Services     |
+------------------------------------------+
|             GRAPHICS ENGINE              |
|       Framebuffer / Rendering / Input    |
+------------------------------------------+
|              DEVICE DRIVERS              |
|     Display / Keyboard / Storage / Mouse |
+------------------------------------------+
|               LIKO KERNEL                |
|    Memory / Interrupts / Processes       |
|    Hardware Abstraction / System Calls  |
+------------------------------------------+
|              BOOT LAYER                  |
|          Bootloader / Initialization    |
+------------------------------------------+
|             x86_64 HARDWARE              |
|         CPU / RAM / Display / Disk        |
+------------------------------------------+
```

Each subsystem is intended to have a clearly defined responsibility and interface.

This separation is designed to reduce coupling and make independent development and debugging possible.

---

## 05 — Kernel Architecture

The kernel is the foundation of LIKO OS.

It will be responsible for controlling system resources and providing essential interfaces to higher-level components.

### Planned Kernel Subsystems

**Memory Management**
- Physical memory management
- Virtual memory management
- Page allocation
- Kernel heap
- Memory protection

**Interrupt Management**
- Interrupt Descriptor Table
- Exception handling
- Hardware interrupt handling
- Programmable Interrupt Controller support

**Process Management**
- Process structures
- Thread management
- Scheduling
- Context switching
- Process isolation

**System Interface**
- System calls
- Kernel services
- Driver communication
- User-space interaction

**Hardware Abstraction**
- Device interfaces
- Hardware initialization
- Platform-specific operations
- Driver abstraction

The kernel will initially prioritize essential functionality before introducing advanced process isolation and multitasking features.

---

## 06 — Boot Architecture

The boot process is planned as a sequence of controlled initialization stages.

```text
POWER ON
   |
   v
FIRMWARE INITIALIZATION
   |
   v
BOOTLOADER
   |
   v
KERNEL LOADING
   |
   v
CPU & MEMORY INITIALIZATION
   |
   v
INTERRUPT INITIALIZATION
   |
   v
DEVICE INITIALIZATION
   |
   v
FILESYSTEM INITIALIZATION
   |
   v
GRAPHICS INITIALIZATION
   |
   v
SYSTEM SERVICES
   |
   v
LIKO DESKTOP
```

The bootloader is expected to load the kernel and transfer execution to its entry point.

The kernel will then initialize the required subsystems and eventually start the graphical environment.

---

## 07 — Graphics & Desktop Environment

LIKO Desktop is the planned graphical environment of LIKO OS.

It is intended to provide a consistent interface without depending on an existing desktop environment.

### Desktop Components

| Component | Function |
|---|---|
| Desktop Manager | Main graphical workspace |
| Window Manager | Window positioning and management |
| Taskbar | Running applications and system controls |
| Start Menu | Application launcher |
| File Explorer | File and directory navigation |
| Settings | System configuration |
| Terminal | Native command-line interface |
| Notification System | System notifications |
| Icon Manager | Desktop and application icons |

### Visual Identity

The visual design language is planned around:

- Deep navy backgrounds
- Electric blue accents
- Cyan highlights
- Minimal interface elements
- High-contrast typography
- Consistent iconography
- Efficient rendering

### Offline Assets

The graphical environment will use locally stored resources.

Planned asset categories:

```text
Assets/
├── Branding/
├── Icons/
│   ├── System/
│   ├── Applications/
│   └── Files/
├── Fonts/
├── Wallpapers/
├── Sounds/
└── Themes/
```

No internet connection should be necessary to load the core desktop interface or its built-in assets.

---

## 08 — Hardware & Driver Architecture

LIKO OS is intended to use hardware resources directly through its native kernel and driver interfaces.

When running under VMware, the system will interact with the virtual hardware exposed by VMware.

### Planned Device Support

| Device | Planned Functionality |
|---|---|
| CPU | x86_64 execution |
| RAM | Native memory management |
| Display | Framebuffer output |
| Keyboard | Keyboard input |
| Mouse | Pointer input |
| Storage | Virtual disk access |
| Timer | System timing |
| Network Adapter | Optional networking |
| Audio | Future audio support |

Hardware virtualization is not an operating system requirement for ordinary native execution.

VMware provides the virtual hardware platform, while LIKO OS manages the resources made available to it.

---

## 09 — Storage & Filesystem

Storage management will be developed as an independent kernel subsystem.

Initial filesystem goals:

- File and directory operations
- Filesystem initialization
- File metadata
- Read and write operations
- Storage device abstraction

FAT32 is a candidate for the initial filesystem implementation.

Future filesystem support will depend on compatibility, reliability, and resource requirements.

---

## 10 — Terminal Environment

LIKO Terminal is intended to provide a native command-line interface.

The first terminal prototype is developed in C for Windows as an early interface experiment. It is separate from the future native kernel terminal.

Planned command categories:

```text
SYSTEM
  HELP
  CLEAR
  VERSION
  ABOUT

FILESYSTEM
  DIR
  CD
  MKDIR
  TYPE

PROCESS
  PROCESS LIST
  PROCESS INFO

HARDWARE
  CPU INFO
  MEMORY INFO
  DEVICE LIST
```

Commands will be implemented progressively as the underlying kernel services become available.

---

## 11 — Application Architecture

LIKO OS will use a modular application architecture.

Planned built-in applications:

| Application | Purpose |
|---|---|
| LIKO Terminal | Command-line interface |
| LIKO Explorer | File management |
| LIKO Settings | System configuration |
| LIKO Calculator | Calculations |
| LIKO System Monitor | Resource monitoring |
| LIKO App Manager | Application management |
| LIKO Browser | Future browsing application |

Applications are intended to use documented system interfaces instead of directly depending on internal kernel implementation details.

---

## 12 — Development Toolchain

The development environment is designed around open development tools.

| Tool | Purpose |
|---|---|
| GCC Cross Compiler | Kernel compilation |
| NASM | Assembly |
| GNU Make | Build automation |
| MSYS2 UCRT64 | Development environment |
| Visual Studio Code | Source editing |
| VMware Workstation | Virtual hardware testing |
| Git | Version control |

A dedicated cross-compilation toolchain will be used for native kernel development.

The Windows-hosted C prototype and the native kernel are separate build targets.

---

## 13 — Repository Structure

The intended source tree is modular and organized by subsystem.

```text
LIKO-OS/
│
├── Boot/
│   ├── bootloader/
│   ├── bios/
│   └── uefi/
│
├── Kernel/
│   ├── Core/
│   ├── Memory/
│   ├── Interrupts/
│   ├── Processes/
│   └── SystemCalls/
│
├── Drivers/
│   ├── Display/
│   ├── Keyboard/
│   ├── Mouse/
│   ├── Storage/
│   └── Timer/
│
├── Graphics/
│   ├── Engine/
│   ├── Desktop/
│   ├── WindowManager/
│   ├── Taskbar/
│   └── Icons/
│
├── System/
│   ├── Terminal/
│   ├── Explorer/
│   ├── Settings/
│   └── Services/
│
├── Applications/
│
├── Assets/
│   ├── Branding/
│   ├── Fonts/
│   ├── Icons/
│   ├── Wallpapers/
│   └── Sounds/
│
├── Build/
│
├── Documentation/
│
├── Makefile
└── README.md
```

This structure is an architectural proposal and will evolve as implementation progresses.

---

## 14 — Development Roadmap

### Stage 01 — Foundation
- [x] Initial Windows C terminal prototype
- [ ] Native x86_64 project setup
- [ ] Cross-compiler configuration
- [ ] Bootloader integration
- [ ] First native kernel entry point

### Stage 02 — Kernel Core
- [ ] Kernel initialization
- [ ] Physical memory manager
- [ ] Interrupt handling
- [ ] Basic hardware abstraction
- [ ] Kernel logging

### Stage 03 — Hardware
- [ ] Display driver
- [ ] Keyboard driver
- [ ] Timer driver
- [ ] Storage driver
- [ ] Mouse support

### Stage 04 — Graphics
- [ ] Framebuffer renderer
- [ ] Font rendering
- [ ] Graphics primitives
- [ ] Window management
- [ ] Desktop environment

### Stage 05 — System Services
- [ ] Filesystem
- [ ] Process manager
- [ ] System calls
- [ ] Terminal
- [ ] Application loading

### Stage 06 — Distribution
- [ ] ISO generation
- [ ] VMware boot testing
- [ ] Memory optimization
- [ ] Boot optimization
- [ ] Initial development release

---

## 15 — Performance & Optimization Strategy

Resource efficiency is a fundamental design constraint.

The development strategy prioritizes:

1. Small kernel footprint
2. Controlled memory allocation
3. Minimal background services
4. Efficient graphics rendering
5. Static or carefully managed memory where appropriate
6. Modular driver loading
7. Minimal unnecessary dependencies

Performance claims will be based on measurements rather than assumptions.

---

## 16 — Testing & Validation

VMware Workstation is the primary development and validation environment.

Testing objectives include:

- Successful boot
- Kernel initialization
- Memory management validation
- Interrupt handling
- Device detection
- Display output
- Keyboard and mouse input
- Filesystem operations
- Desktop stability
- Resource consumption

Each subsystem should be tested independently before integration into the main system.

---

## 17 — Security Principles

Security will be developed as part of the kernel and system architecture.

Long-term objectives include:

- Memory isolation
- Controlled system interfaces
- Permission management
- Safe application execution
- Input validation
- Filesystem access controls

Security features will be documented according to their actual implementation status.

---

## 18 — Project Status

**Development Stage:** Early Development

LIKO OS is currently in its architectural and foundational development phase.

The project roadmap describes intended functionality, not a claim that all listed subsystems are already implemented.

The first milestone is a bootable native kernel running in VMware Workstation.

---

## 19 — Contribution & Development

Contributions and technical discussions are welcome.

Potential areas of contribution:

- Kernel engineering
- C programming
- Assembly
- Graphics development
- Driver development
- Testing
- Documentation

All contributions should follow the project's modular architecture and coding conventions.

---

## 20 — Project Identity

**Project:** LIKO OS  
**Category:** Operating System Development  
**Architecture:** x86_64  
**Primary Language:** C  
**Low-Level Language:** Assembly  
**Primary Target:** VMware Workstation  
**Distribution Goal:** Bootable ISO  
**Development Status:** In Progress

---

<p align="center">

# LIKO OS

### Beyond Applications. Towards an Operating System.

**A native operating system project focused on lightweight engineering and independent architecture.**

</p>
