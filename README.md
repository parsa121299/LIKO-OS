# LIKO OS
### A Native 64-Bit Operating System Project

<p align="center">
  <strong>Independent Kernel · Native Execution · Modular Architecture · Custom Desktop Environment</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-x86__64-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Kernel-C%20%2B%20Assembly-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-VMware%20Workstation-607078?style=for-the-badge">
  <img src="https://img.shields.io/badge/Boot-BIOS%20%7C%20UEFI-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Memory-4--32%20GB-success?style=for-the-badge">
</p>

---

## 1. Project Overview

**LIKO OS** is an independent operating system development project focused on building a native 64-bit computing environment with its own kernel, hardware abstraction architecture, memory management, device drivers, system services, and graphical desktop environment.

The project aims to establish a modular operating system architecture capable of running as a bootable ISO image inside VMware Workstation.

LIKO OS is not intended to be a conventional desktop application or a graphical simulation running on top of another operating system.

Its long-term objective is to execute its own kernel and manage the hardware resources exposed to it by the virtualization platform.

### Core Objectives

- Independent native kernel development.
- 64-bit x86 architecture.
- Direct interaction with VMware-presented hardware.
- Modular hardware abstraction architecture.
- Advanced memory management.
- Process and thread management.
- Custom graphical desktop environment.
- Native system utilities and applications.
- Offline-first operation.
- Bootable ISO distribution.

---

## 2. Technical Specifications

| Specification | Target |
|---|---|
| Project Name | LIKO OS |
| Architecture | x86_64 |
| Operating System Type | Native OS |
| Kernel Type | Custom kernel |
| Main Languages | C, Assembly |
| Boot Distribution | ISO |
| Firmware Targets | BIOS / UEFI |
| Primary Platform | VMware Workstation |
| Memory Support Target | 4 GB – 32 GB |
| Recommended VM Memory | 8–16 GB |
| Virtual CPU Target | 2–8 vCPUs |
| Virtual Storage Target | 30–100 GB |
| Graphics | Custom desktop renderer |
| Filesystem | FAT32 initially |
| Network | Optional subsystem |
| Internet Dependency | None for core operation |
| Interface | Graphical Desktop + Terminal |

**Resource configuration note:** These values describe project targets and recommended virtual-machine configurations. They are not yet verified minimum or maximum limits of an implemented kernel.

---

## 3. System Architecture

LIKO OS is designed around independent subsystems with clearly defined responsibilities.

### Architectural Layers

1. Boot and initialization layer
2. Kernel core
3. Hardware abstraction layer
4. Memory management subsystem
5. Interrupt and exception subsystem
6. Process and thread management
7. Device driver framework
8. Filesystem and storage services
9. Graphics and window management
10. System services
11. Native applications

The architecture is intended to support incremental development without requiring the entire operating system to be rewritten when an individual subsystem changes.

---

## 4. Kernel Architecture

The kernel is the central component responsible for managing system execution and coordinating hardware-facing services.

### Planned Kernel Components

| Component | Responsibility |
|---|---|
| Kernel Core | Initialization and subsystem coordination |
| Memory Manager | Physical memory allocation |
| Virtual Memory | Address-space management |
| Paging | Virtual-to-physical address translation |
| Interrupt Manager | Hardware and software interrupts |
| Exception Handler | CPU exception management |
| Process Manager | Process lifecycle |
| Thread Manager | Thread scheduling |
| Scheduler | CPU execution scheduling |
| System Calls | Kernel-service interface |
| HAL | Hardware abstraction |
| IPC | Inter-process communication |

### Kernel Design Goals

- Predictable execution.
- Modular subsystem interfaces.
- Controlled memory allocation.
- Hardware abstraction.
- Fault isolation where supported.
- Efficient resource management.
- Expandable kernel services.

---

## 5. Boot Architecture

LIKO OS is intended to be distributed as a bootable ISO image.

### Boot Sequence

1. Firmware initialization.
2. Bootloader execution.
3. Kernel image loading.
4. CPU environment initialization.
5. Memory subsystem initialization.
6. Interrupt configuration.
7. Hardware discovery.
8. Driver initialization.
9. System service startup.
10. Graphical environment initialization.
11. Desktop launch.

### Firmware Compatibility Targets

- Legacy BIOS
- UEFI

The bootloader and kernel will be developed and tested against the firmware interfaces supported by the selected VMware virtual-machine configuration.

---

## 6. Memory Management

Memory management is a major engineering priority.

### Planned Features

- Physical memory manager.
- Virtual memory manager.
- Paging support.
- Kernel memory allocation.
- Heap management.
- Memory-region tracking.
- Process address spaces.
- Memory protection.
- Allocation diagnostics.

### Target Memory Configuration

| Configuration | RAM |
|---|---:|
| Minimum design target | 4 GB |
| Standard configuration | 8 GB |
| Advanced configuration | 16 GB |
| Maximum design target | 32 GB |

The kernel will be designed to support configurable memory limits rather than relying on a single fixed memory configuration.

---

## 7. Processor Architecture

LIKO OS targets the x86_64 instruction set.

### Planned CPU Features

- 64-bit execution.
- CPU feature detection.
- Descriptor tables.
- Interrupt descriptor table.
- Timer integration.
- Multicore awareness.
- Scheduling infrastructure.
- CPU exception handling.

Actual multicore execution and advanced CPU capabilities will depend on their implementation and availability through VMware.

---

## 8. Hardware Abstraction Layer

The Hardware Abstraction Layer provides a consistent interface between the kernel and hardware-specific implementations.

### Planned Driver Categories

| Driver | Purpose |
|---|---|
| Display Driver | Framebuffer output |
| Keyboard Driver | Keyboard input |
| Mouse Driver | Pointer input |
| Storage Driver | Virtual disk access |
| Timer Driver | Timekeeping and scheduling |
| Network Driver | Network connectivity |
| Audio Driver | Audio output |

Drivers will be implemented according to the virtual hardware presented by VMware.

---

## 9. Graphics Architecture

LIKO OS plans to include a custom graphical environment rather than depending on the desktop of a host operating system.

### Desktop Components

- Desktop Manager
- Window Manager
- Graphics Renderer
- Taskbar
- Start Menu
- Application Launcher
- Notification System
- Desktop Icons
- Theme Manager
- Input Management

### Graphics Goals

- Hardware-independent rendering interfaces.
- Window management.
- Multiple application windows.
- Responsive desktop layout.
- Custom visual effects.
- Local graphics assets.
- Offline fonts and icon resources.

---

## 10. Native System Environment

The operating system is planned to include a collection of native system utilities.

### Planned Applications

| Application | Purpose |
|---|---|
| LIKO Terminal | Command-line environment |
| LIKO Explorer | File management |
| LIKO Settings | System configuration |
| LIKO System Monitor | Resource monitoring |
| LIKO App Manager | Application management |
| LIKO Text Editor | Text editing |
| LIKO Calculator | Calculations |

Applications will progressively integrate with the operating system's native system interfaces.

---

## 11. Storage Architecture

The storage subsystem will provide persistent data access and filesystem services.

### Initial Goals

- Virtual disk detection.
- Disk read/write interfaces.
- Filesystem mounting.
- Directory management.
- File creation and deletion.
- Storage diagnostics.
- Filesystem error handling.

FAT32 is an initial compatibility target. A dedicated LIKO filesystem may be considered in a later development stage.

---

## 12. Offline-First Architecture

LIKO OS is designed to operate without requiring an internet connection for core system functionality.

Local resources will include:

- Fonts
- Icons
- Wallpapers
- Sounds
- System configuration
- Desktop themes
- Built-in applications

Network functionality will be optional and will not be required for the basic boot process or desktop operation.

---

## 13. Security Architecture

Security is intended to be integrated into the system architecture rather than added only at the application level.

### Planned Security Mechanisms

- Kernel/user privilege separation.
- Memory protection.
- Controlled system calls.
- Process isolation.
- Driver interface validation.
- Filesystem access controls.
- Application permission model.
- Input validation.
- System integrity checks.

These are design objectives, not claims that the mechanisms have already been implemented.

---

## 14. Development Toolchain

### Primary Languages

- C — Kernel and system components.
- Assembly — Architecture-specific startup and low-level operations.

### Development Environment

- GCC
- GNU Binutils
- GNU Make
- MSYS2 UCRT64
- Visual Studio Code
- VMware Workstation

### Development Principles

- Modular source code.
- Clear subsystem boundaries.
- Reproducible builds.
- Incremental testing.
- Hardware abstraction.
- Documented interfaces.
- Separation of host-side tools and guest-side kernel code.

---

## 15. Repository Structure

```text
LIKO-OS/
│
├── Boot/
│   ├── BIOS/
│   ├── UEFI/
│   └── Bootloader/
│
├── Kernel/
│   ├── Core/
│   ├── Memory/
│   ├── Interrupts/
│   ├── Processes/
│   ├── Threads/
│   ├── Scheduler/
│   ├── SystemCalls/
│   └── HAL/
│
├── Drivers/
│   ├── Display/
│   ├── Keyboard/
│   ├── Mouse/
│   ├── Storage/
│   ├── Timer/
│   ├── Audio/
│   └── Network/
│
├── Graphics/
│   ├── Engine/
│   ├── Renderer/
│   ├── Desktop/
│   ├── WindowManager/
│   ├── Taskbar/
│   └── Themes/
│
├── System/
│   ├── Terminal/
│   ├── Explorer/
│   ├── Settings/
│   ├── Services/
│   └── Security/
│
├── Applications/
│
├── Filesystem/
│
├── Assets/
│   ├── Icons/
│   ├── Fonts/
│   ├── Wallpapers/
│   └── Sounds/
│
├── Build/
├── Documentation/
│
├── Makefile
└── README.md
```

---

## 16. Performance Engineering

Performance is a core design consideration.

### Optimization Objectives

- Efficient memory allocation.
- Minimal unnecessary background services.
- Fast boot initialization.
- Efficient graphics operations.
- Reduced kernel overhead.
- Configurable system services.
- Scalable memory management.
- Efficient filesystem access.

The system will be optimized through measurement and testing rather than assuming performance from hardware specifications alone.

---

## 17. Testing Strategy

Testing will be performed incrementally.

### Planned Testing Environments

- VMware BIOS virtual machines.
- VMware UEFI virtual machines.
- 4 GB RAM configurations.
- 8 GB RAM configurations.
- 16 GB RAM configurations.
- 32 GB RAM configurations.
- Different virtual CPU configurations.
- Virtual storage configurations.

### Testing Priorities

1. Boot reliability.
2. Kernel initialization.
3. Memory correctness.
4. Interrupt handling.
5. Driver stability.
6. Filesystem integrity.
7. Graphics stability.
8. Application execution.

---

## 18. Development Roadmap

### Phase 1 — Foundation
- [ ] Project architecture.
- [ ] Bootloader integration.
- [ ] Native kernel entry.
- [ ] Basic kernel initialization.
- [ ] Serial/debug output.

### Phase 2 — Kernel Engineering
- [ ] Physical memory management.
- [ ] Paging.
- [ ] Interrupt handling.
- [ ] Timer support.
- [ ] Basic scheduler.
- [ ] System calls.

### Phase 3 — Hardware Support
- [ ] Display output.
- [ ] Keyboard input.
- [ ] Mouse input.
- [ ] Virtual storage.
- [ ] Filesystem integration.

### Phase 4 — Graphics
- [ ] Graphics renderer.
- [ ] Window manager.
- [ ] Desktop environment.
- [ ] Taskbar.
- [ ] Start menu.
- [ ] Theme system.

### Phase 5 — System Applications
- [ ] Terminal.
- [ ] File manager.
- [ ] Settings.
- [ ] System monitor.
- [ ] Application framework.

### Phase 6 — Distribution
- [ ] Bootable ISO.
- [ ] VMware compatibility testing.
- [ ] Installation workflow.
- [ ] Documentation.
- [ ] Release preparation.

---

## 19. Project Status

LIKO OS is an active development project.

The Windows-hosted terminal prototype is an early development utility and is separate from the planned native kernel.

The native bootable operating system, desktop environment, hardware drivers, and other subsystems must be implemented and validated independently.

No unimplemented feature should be considered production-ready.

---

## 20. Project Philosophy

LIKO OS is built around a simple engineering principle:

**Build the operating system from the foundation upward.**

The objective is not merely to create an interface that looks like an operating system. The objective is to develop the kernel, system architecture, hardware interfaces, and native user environment that make an independent operating system possible.

---

## 21. License and Contributions

License and contribution policies will be defined as the project matures.

Contributions should prioritize:

- Code clarity.
- Technical correctness.
- Architecture consistency.
- Documentation.
- Reproducible testing.
- Long-term maintainability.

---

<p align="center">
  <strong>LIKO OS — Designed as an Independent Computing Platform.</strong>
</p>

<p align="center">
  Native Architecture · Independent Kernel · Custom Desktop
</p>
